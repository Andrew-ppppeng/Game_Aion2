import assert from 'node:assert/strict';
import {test} from 'node:test';
import {counterField, eventNames, returningVisit, validateEvents} from '../src/lib/analytics-model.ts';
import type {AnalyticsEvent} from '../src/lib/analytics-model.ts';

const day = 86400000;
const now = Date.parse('2026-10-04T12:00:00Z');
const pages = new Set(['/', '/guide', '/builds', '/tools/character', '/privacy-policy']);
const view: AnalyticsEvent = {name: 'page_view', path: '/guide', locale: 'en'};

test('anonymous events admit only published canonical paths and supported event labels', () => {
  for (const name of eventNames) {
    const event: AnalyticsEvent = {...view, name,
      ...(name === 'web_vital' ? {metric: 'LCP' as const, value: 2500} : {}),
      ...(name === 'return_7d' ? {cohort: '2026-10-02'} : {}),
    };
    assert.deepEqual(validateEvents([event], pages, now), [event]);
  }
  for (const path of ['/unknown', '/guide?name=Private', '/guide#private', '/ja/guide', '/tools/character?cid=Private', 'https://example.com/guide']) {
    assert.equal(validateEvents([{...view, path}], pages, now), null, path);
  }
  for (const locale of ['zh', '', 'en-US']) assert.equal(validateEvents([{...view, locale}], pages, now), null);
  assert.equal(validateEvents([{...view, name: 'typed_character_name'}], pages, now), null);
});

test('privacy whitelist rejects names, IDs, raw URLs, query strings, storage values and extra keys', () => {
  for (const key of ['characterName', 'characterId', 'nameValue', 'id', 'query', 'url', 'referrer', 'ip', 'userAgent', 'sessionId', 'browserId', 'recipe', 'savedValue', 'timestamp']) {
    assert.equal(validateEvents([{...view, [key]: 'Private value 90210'}], pages, now), null, key);
  }
  assert.equal(validateEvents([{...view}, {...view, query: 'Private'}], pages, now), null, 'Reject the complete batch, not only its unsafe item');
  for (const input of [null, {}, [], [null], [3], [true], Array(13).fill(view)]) assert.equal(validateEvents(input, pages, now), null);
  assert.equal(validateEvents(Array(12).fill(view), pages, now)?.length, 12);
});

test('tool targets and metric/cohort fields cannot carry arbitrary strings', () => {
  for (const target of ['character', 'budget', 'checklist', 'calendar', 'equipment', 'classes']) {
    assert.ok(validateEvents([{...view, name: 'tool_use', target}], pages, now));
  }
  assert.equal(validateEvents([{...view, name: 'tool_use', target: 'PrivateCharacter'}], pages, now), null);
  for (const extra of [{metric: 'LCP'}, {value: 2}, {cohort: '2026-10-02'}]) assert.equal(validateEvents([{...view, ...extra}], pages, now), null);
});

test('vitals reject nonfinite, negative, string and out-of-range samples', () => {
  for (const metric of ['LCP', 'INP', 'CLS'] as const) {
    const maximum = metric === 'CLS' ? 10 : 60000;
    for (const value of [0, maximum]) assert.ok(validateEvents([{...view, name: 'web_vital', metric, value}], pages, now));
    for (const value of [-1, maximum + 1, NaN, Infinity, '2500', null]) assert.equal(validateEvents([{...view, name: 'web_vital', metric, value}], pages, now), null);
  }
  assert.equal(validateEvents([{...view, name: 'web_vital', metric: 'FID', value: 5}], pages, now), null);
  assert.equal(validateEvents([{...view, name: 'web_vital', value: 5}], pages, now), null);
});

test('metric counters use stable 100 ms and 0.01 CLS histogram bins', () => {
  const metric = (name: 'LCP' | 'INP' | 'CLS', value: number) => counterField({...view, name: 'web_vital', metric: name, value});
  assert.equal(metric('LCP', 2499), 'en|/guide|web_vital|LCP|24');
  assert.equal(metric('LCP', 2500), 'en|/guide|web_vital|LCP|25');
  assert.equal(metric('INP', 201), 'en|/guide|web_vital|INP|2');
  assert.equal(metric('CLS', .109), 'en|/guide|web_vital|CLS|10');
  assert.equal(metric('CLS', 10), 'en|/guide|web_vital|CLS|600');
  assert.equal(metric('LCP', 60000), 'en|/guide|web_vital|LCP|600');
  assert.equal(counterField({...view, name: 'tool_use', target: 'budget'}), 'en|/guide|tool_use|budget');
  assert.equal(counterField({...view, name: 'return_7d', cohort: '2026-10-02'}), 'en|/guide|return_7d', 'Cohort belongs to the daily storage key, not a per-browser identifier');
});

test('returning browsers require elapsed first-visit age of 1 to 7 days and 30 minutes inactivity', () => {
  const state = {firstAt: now - 2 * day, lastAt: now - 1800000, returned: false};
  assert.equal(returningVisit(state, now), true);
  assert.equal(returningVisit({...state, firstAt: now - day + 1}, now), false);
  assert.equal(returningVisit({...state, firstAt: now - day}, now), true);
  assert.equal(returningVisit({...state, firstAt: now - 7 * day}, now), true);
  assert.equal(returningVisit({...state, firstAt: now - 7 * day - 1}, now), false);
  assert.equal(returningVisit({...state, lastAt: now - 1800000 + 1}, now), false);
  assert.equal(returningVisit({...state, lastAt: now}, now), false);
  assert.equal(returningVisit({...state, returned: true}, now), false, 'A browser contributes once to its original cohort');
});

test('return event cohorts reject future, excessively old, malformed and impossible dates', () => {
  const returning = {...view, name: 'return_7d', cohort: '2026-10-02'};
  assert.ok(validateEvents([returning], pages, now));
  for (const cohort of ['2026-10-05', '2026-09-25', '2026-13-01', '2026-10-xx', '2026-10-02?name=Private', '2026-09-31']) {
    assert.equal(validateEvents([{...returning, cohort}], pages, now), null, cohort);
  }
});
