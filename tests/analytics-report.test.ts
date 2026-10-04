import assert from 'node:assert/strict';
import {execFile} from 'node:child_process';
import {createServer} from 'node:http';
import {test} from 'node:test';
import {fileURLToPath} from 'node:url';
import {promisify} from 'node:util';
import {reportDates, summarizeAnalytics} from '../scripts/analytics-report.mjs';

const now = Date.parse('2026-10-04T12:00:00Z');

test('report dates reject impossible/future dates and enforce the storage window', () => {
  assert.deepEqual(reportDates([], now), ['2026-10-04']);
  assert.deepEqual(reportDates(['2026-10-02'], now), ['2026-10-02']);
  assert.deepEqual(reportDates(['--from', '2026-10-01', '--to', '2026-10-03'], now), ['2026-10-01', '2026-10-02', '2026-10-03']);
  for (const args of [['2026-09-31'], ['2026-10-05'], ['2026-08-01'], ['--from', '2026-10-03'], ['--token', 'private'], ['--from', '2026-10-03', '--to', '2026-10-02']]) assert.throws(() => reportDates(args, now));
});

test('retention includes only fully mature seven-day browser cohorts and preserves the original cohort date', () => {
  const result = summarizeAnalytics([
    {date: '2026-09-25', counters: {'en|/guide|new_browser': 20, 'en|/guide|return_7d': 5}},
    {date: '2026-09-26', counters: {'ja|/builds|new_browser': 40, 'ja|/builds|return_7d': 10}},
    {date: '2026-09-27', counters: {'en|/guide|new_browser': 100, 'en|/guide|return_7d': 90}},
  ], now);
  assert.equal(result.retention.newBrowsers, 60);
  assert.equal(result.retention.returnedBrowsers, 15);
  assert.equal(result.retention.returnRatePercent, 25);
  assert.equal(result.retention.cohorts[2].mature, false, 'The latest browser on this cohort date has not had seven full days');
  assert.equal(result.retention.cohorts[2].returnRatePercent, null);
  assert.equal(result.retention.smallSample, false);
  assert.match(result.retention.definition, /Browsers/);
});

test('histogram p75 uses count-weighted nearest ranks and reports bin ranges rather than invented precision', () => {
  const result = summarizeAnalytics([{date: '2026-10-02', counters: {
    'en|/guide|web_vital|LCP|10': 1,
    'en|/guide|web_vital|LCP|20': 2,
    'ja|/builds|web_vital|LCP|40': 1,
    'en|/guide|web_vital|CLS|9': 3,
    'en|/guide|web_vital|CLS|600': 1,
  }}], now);
  assert.equal(result.vitals.LCP.samples, 4);
  assert.deepEqual(result.vitals.LCP.p75, {lowerInclusive: 2000, upper: 2100, upperInclusive: false, unit: 'ms'});
  assert.equal(result.vitals.CLS.p75?.lowerInclusive, .09);
  assert.equal(result.vitals.INP.samples, 0);
  assert.equal(result.vitals.INP.p75, null);
  assert.match(result.vitals.INP.availability, /no eligible interaction/);
  assert.equal(result.vitals.LCP.smallSample, true);
  const capped = summarizeAnalytics([{date: '2026-10-02', counters: {'en|/guide|web_vital|CLS|600': 2}}], now);
  assert.deepEqual(capped.vitals.CLS.p75, {lowerInclusive: 6, upper: 10, upperInclusive: true, unit: 'score'});
});

test('next-guide and tool usage rates expose page-view denominators and do not claim unique conversion', () => {
  const result = summarizeAnalytics([{date: '2026-10-04', counters: {
    'en|/guide|page_view': 10, 'ja|/builds|page_view': 10,
    'en|/guide|next_guide_click': 4,
    'en|/guide|tool_use|character': 3,
    'ja|/builds|tool_use|budget': 2,
    'en|/tools/character|bookmark_save|character': 2,
  }}], now);
  assert.equal(result.interactions.pageViews, 20);
  assert.equal(result.interactions.nextGuideClicksPer100PageViews, 20);
  assert.equal(result.interactions.toolUsesPer100PageViews, 25);
  assert.equal(result.interactions.tools.character, 3);
  assert.equal(result.interactions.byPage['en|/guide'].nextGuideClicksPer100PageViews, 40);
  assert.match(result.interactions.denominator, /not unique-browser/);
  assert.equal(result.currentUtcDatePartial, true);
});

test('empty and inconsistent aggregate data remain visible without dividing by zero or clamping rates', () => {
  const empty = summarizeAnalytics([{date: '2026-10-01', counters: {}}], now);
  assert.equal(empty.retention.returnRatePercent, null);
  assert.equal(empty.interactions.toolUsesPer100PageViews, null);
  assert.equal(empty.vitals.LCP.p75, null);
  const inconsistent = summarizeAnalytics([{date: '2026-09-25', counters: {'en|/guide|new_browser': 1, 'en|/guide|return_7d': 2}}], now);
  assert.equal(inconsistent.retention.returnRatePercent, 200);
  assert.equal(inconsistent.retention.inconsistent, true);
  assert.equal(inconsistent.retention.smallSample, true);
  const invalidCounters: Record<string, number>[] = [{'en|/guide?private=secret|page_view': 2}, {'en|/guide|private': 2}, {'en|/guide|page_view': -1}, {'en|/guide|web_vital|LCP|601': 1}];
  for (const counters of invalidCounters) {
    assert.throws(() => summarizeAnalytics([{date: '2026-10-01', counters}], now));
  }
});

test('report CLI authorizes reads in the header, combines dates and never prints its token', async () => {
  const token = 'offline-report-token-not-for-output';
  const dates = [10, 9].map((age) => new Date(Date.now() - age * 86400000).toISOString().slice(0, 10));
  const requests: string[] = [];
  const server = createServer((request, response) => {
    const url = new URL(request.url || '/', 'http://local.invalid');
    requests.push(url.href);
    assert.equal(request.headers.authorization, `Bearer ${token}`);
    assert.equal(url.pathname, '/api/analytics');
    const date = url.searchParams.get('date');
    assert.ok(date && dates.includes(date));
    response.setHeader('Content-Type', 'application/json');
    response.end(JSON.stringify({date, counters: {'en|/guide|new_browser': 20, 'en|/guide|return_7d': 5, 'en|/guide|page_view': 30}}));
  });
  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve));
  try {
    const address = server.address();
    assert.ok(address && typeof address === 'object');
    const result = await promisify(execFile)(process.execPath, [fileURLToPath(new URL('../scripts/analytics-report.mjs', import.meta.url)), '--from', dates[0], '--to', dates[1]], {
      env: {...process.env, QA_BASE_URL: `http://127.0.0.1:${address.port}`, ANALYTICS_READ_TOKEN: token}, timeout: 15000,
    });
    assert.equal(requests.length, 2);
    assert.ok(requests.every((url) => !url.includes(token) && !url.includes('token=')));
    assert.ok(!result.stdout.includes(token) && !result.stderr.includes(token));
    const report = JSON.parse(result.stdout);
    assert.equal(report.retention.newBrowsers, 40);
    assert.equal(report.retention.returnRatePercent, 25);
    assert.equal(report.interactions.pageViews, 60);
    assert.equal(report.vitals.INP.p75, null);
  } finally {await new Promise<void>((resolve, reject) => server.close((error) => error ? reject(error) : resolve()));}
});
