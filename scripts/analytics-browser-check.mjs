import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {readFile} from 'node:fs/promises';
import {chromium, expect, request} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3002';
const privateValue = 'PrivateAnalyticsQA90210';
const fixture = JSON.parse(await readFile(new URL('../tests/fixtures/cleric.json', import.meta.url), 'utf8'));
const metadata = JSON.parse(await readFile(new URL('../src/content/game-data/meta.json', import.meta.url), 'utf8'));
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined)});
const errors = [];
const allEvents = [];
const allowedKeys = new Set(['name', 'path', 'locale', 'target', 'metric', 'value', 'cohort']);
const validEvents = new Set(['page_view', 'new_browser', 'session_start', 'return_7d', 'next_guide_click', 'tool_use', 'bookmark_save', 'budget_save', 'checklist_save', 'web_vital']);
let cases = 0;

async function contextFor({privacy, visit, forceFetch} = {}) {
  const context = await browser.newContext({viewport: {width: 390, height: 844}});
  const events = [];
  await context.addInitScript(({privacy, visit, forceFetch}) => {
    if (privacy === 'dnt') Object.defineProperty(Navigator.prototype, 'doNotTrack', {get: () => '1', configurable: true});
    if (privacy === 'gpc') Object.defineProperty(Navigator.prototype, 'globalPrivacyControl', {get: () => true, configurable: true});
    if (privacy === 'optout') localStorage.setItem('aion2-analytics-opt-out-v1', 'true');
    if (forceFetch) Object.defineProperty(navigator, 'sendBeacon', {value: () => false, configurable: true});
    if (visit && !localStorage.getItem('aion2-visit-state-v1')) {
      const now = Date.now();
      localStorage.setItem('aion2-visit-state-v1', JSON.stringify({firstAt: now - visit.age, lastAt: now - visit.inactive, returned: visit.returned || false, locale: 'ja', path: '/guide'}));
    }
  }, {privacy, visit, forceFetch});
  await context.route('**/api/analytics', async (route) => {
    const headers = await route.request().allHeaders();
    if (forceFetch) assert.equal(headers.referer, undefined, 'Fallback keepalive fetch uses no-referrer');
    if (headers.referer) {
      assert.equal(new URL(headers.referer).search, '', 'Analytics Referer must not expose the current URL query');
      assert.ok(!headers.referer.includes(privateValue) && !headers.referer.includes(fixture.character.data.info.profile.characterId), 'Analytics request headers must not expose private values or character IDs');
    }
    const incoming = JSON.parse(route.request().postData() || '[]');
    assert.ok(Array.isArray(incoming) && incoming.length && incoming.length <= 12);
    const body = JSON.stringify(incoming);
    assert.ok(!body.includes(privateValue) && !body.includes(fixture.character.data.info.profile.characterId), 'Analytics never includes typed values or character IDs');
    for (const event of incoming) {
      assert.ok(Object.keys(event).every((key) => allowedKeys.has(key)), 'Only safe aggregate fields may leave the browser');
      assert.ok(validEvents.has(event.name));
      assert.ok(event.path.startsWith('/') && !/[?#]/.test(event.path), 'Only canonical pathname, never query string or fragment');
      assert.ok(!/^\/(ja|es|de)(\/|$)/.test(event.path), 'Locale is separate from canonical pathname');
    }
    events.push(...incoming); allEvents.push(...incoming);
    await route.fulfill({status: 204});
  });
  await context.route('**/api/aion2/**', async (route) => {
    const url = new URL(route.request().url());
    const region = url.searchParams.get('region') || 'nae';
    const profile = fixture.character.data.info.profile;
    const respond = (body) => route.fulfill({status: 200, contentType: 'application/json', body: JSON.stringify(body)});
    if (url.pathname.endsWith('/meta')) {
      const data = metadata[region];
      return respond({data: {servers: data.servers.data.serverList, classes: data.classes.data.classList.map((c) => ({id: c.id, name: c.text || c.name})), pcData: data.pcdata.data.pcDataList}, meta: null, error: null});
    }
    if (url.pathname.endsWith('/search')) return respond({data: {list: [{characterId: profile.characterId, name: privateValue, level: profile.characterLevel, pcId: profile.pcId, serverId: profile.serverId, serverName: profile.serverName, region}], pagination: {page: 1, size: 20, total: 1, endPage: 1}}, meta: fixture.character.meta, error: null});
    if (url.pathname.includes('/characters/')) {
      const result = structuredClone(fixture.character); result.data.info.profile.characterName = privateValue;
      return respond(result);
    }
    throw new Error('Unexpected mocked tool request');
  });
  const page = await context.newPage();
  page.on('pageerror', (error) => errors.push(error.message));
  return {context, page, events};
}

async function flush(page) {await page.waitForTimeout(2300);}
async function checklist(page) {
  await page.goto(`${base}/guide?qa_private=${privateValue}#starter-checklist`);
  const box = page.locator('[data-checklist="guide"] input').first();
  await expect(box).toBeVisible(); await box.check();
  assert.ok((await page.evaluate(() => localStorage.getItem('aion2-checklist-v1:guide')))?.includes('official-client'), 'Checklist still saves independently of analytics');
}
async function budget(page) {
  await page.goto(`${base}/monetization?qa_private=${privateValue}#material-budget`);
  const tool = page.locator('[data-budget-planner]');
  await expect(tool).toBeVisible();
  const values = ['2', '1', '10', privateValue, '3', '1', '20'];
  const inputs = tool.locator('input');
  assert.equal(await inputs.count(), values.length);
  for (let i = 0; i < values.length; i++) await inputs.nth(i).fill(values[i]);
  await tool.locator('button[type="submit"]').click();
  await expect(tool.locator('.budget-result')).toBeVisible();
  assert.ok((await page.evaluate(() => localStorage.getItem('aion2-budget-v1')))?.includes(privateValue), 'Budget stores private text locally');
}
async function character(page) {
  await page.goto(`${base}/tools/character?qa_private=${privateValue}`);
  const tool = page.locator('[data-character-tool]');
  await tool.locator('input').first().fill(privateValue);
  await tool.locator('button[type="submit"]').click();
  await expect(tool.locator('.character-match')).toHaveCount(1);
  await tool.locator('.character-match').click();
  await expect(tool.locator('h2')).toHaveText(privateValue);
  await tool.locator('[data-analytics="bookmark_save"]').click();
  assert.ok((await page.evaluate(() => localStorage.getItem('aion2-characters-v1')))?.includes(privateValue), 'Character name stays in local bookmarks');
}

try {
  const ordinary = await contextFor();
  await ordinary.page.goto(`${base}/ja/builds?qa_private=${privateValue}`);
  await expect(ordinary.page.locator('meta[name="referrer"]')).toHaveAttribute('content', 'origin');
  await expect.poll(() => ordinary.events.some((event) => event.name === 'page_view')).toBe(true);
  assert.ok(ordinary.events.some((event) => event.name === 'new_browser'));
  assert.ok(ordinary.events.some((event) => event.name === 'session_start'));
  await ordinary.page.locator('.article-next-card a').first().click();
  await expect.poll(() => ordinary.events.some((event) => event.name === 'next_guide_click')).toBe(true);
  await checklist(ordinary.page); await flush(ordinary.page);
  await budget(ordinary.page); await flush(ordinary.page);
  await character(ordinary.page); await flush(ordinary.page);
  for (const event of ['next_guide_click', 'checklist_save', 'budget_save', 'bookmark_save', 'tool_use']) assert.ok(ordinary.events.some((entry) => entry.name === event), `Expected ${event} without recording private values`);
  assert.equal(ordinary.events.filter((event) => event.name === 'new_browser').length, 1, 'Reloads/navigation do not create another browser');
  await ordinary.context.close(); cases++;

  const fallback = await contextFor({forceFetch: true});
  await fallback.page.goto(`${base}/guide?qa_private=${privateValue}`);
  await expect.poll(() => fallback.events.some((event) => event.name === 'page_view')).toBe(true);
  await fallback.context.close(); cases++;

  for (const privacy of ['dnt', 'gpc', 'optout']) {
    const sample = await contextFor({privacy});
    await checklist(sample.page); await budget(sample.page); await character(sample.page); await flush(sample.page);
    assert.deepEqual(sample.events, [], `${privacy} blocks analytics requests while all three tools continue working`);
    await sample.context.close(); cases++;
  }

  const disabled = await contextFor();
  await disabled.page.goto(`${base}/privacy-policy`);
  const preference = disabled.page.locator('.analytics-preference input');
  await expect(preference).toBeChecked(); await preference.uncheck();
  const baseline = disabled.events.length;
  await checklist(disabled.page); await budget(disabled.page); await flush(disabled.page);
  assert.equal(disabled.events.length, baseline, 'Changing the privacy toggle stops queued and future sends');
  assert.equal(await disabled.page.evaluate(() => localStorage.getItem('aion2-visit-state-v1')), null, 'Opt-out removes local retention state');
  await disabled.context.close(); cases++;

  const returning = await contextFor({visit: {age: 2 * 86400000, inactive: 31 * 60000}});
  await returning.page.goto(`${base}/map?qa_private=${privateValue}`); await flush(returning.page);
  await returning.page.reload(); await flush(returning.page);
  await returning.page.goto(`${base}/guide`); await flush(returning.page);
  const returns = returning.events.filter((event) => event.name === 'return_7d');
  assert.equal(returns.length, 1, 'A returning local browser contributes to its cohort only once');
  assert.equal(returns[0].path, '/guide'); assert.equal(returns[0].locale, 'ja', 'Original entry locale and page receive the cohort return');
  assert.match(returns[0].cohort, /^\d{4}-\d{2}-\d{2}$/);
  assert.equal(returning.events.filter((event) => event.name === 'new_browser').length, 0);
  assert.equal(returning.events.filter((event) => event.name === 'session_start').length, 1);
  assert.equal(await returning.page.evaluate(() => JSON.parse(localStorage.getItem('aion2-visit-state-v1')).returned), true);
  await returning.context.close(); cases++;

  for (const visit of [{age: 12 * 3600000, inactive: 31 * 60000}, {age: 8 * 86400000, inactive: 31 * 60000}, {age: 2 * 86400000, inactive: 29 * 60000}, {age: 2 * 86400000, inactive: 31 * 60000, returned: true}]) {
    const sample = await contextFor({visit});
    await sample.page.goto(`${base}/guide`); await flush(sample.page);
    assert.equal(sample.events.filter((event) => event.name === 'return_7d').length, 0, 'Invalid age, active session or previously counted return does not increment retention');
    await sample.context.close(); cases++;
  }

  const client = await request.newContext({baseURL: base});
  try {
    assert.equal((await client.get('/api/analytics')).status(), 401);
    assert.equal((await client.get('/api/analytics?token=private')).status(), 401, 'Read authorization must be in the Bearer header');
    assert.equal((await client.get('/api/analytics', {headers: {Authorization: 'Bearer invalid-offline-test-token'}})).status(), 401, 'An arbitrary Bearer header must not authorize a read');
    assert.equal((await client.post('/api/analytics', {data: [{name: 'page_view', path: '/guide', locale: 'en'}]})).status(), 403, 'Cross-origin/absent-origin writes are denied');
    assert.equal((await client.post('/api/analytics', {headers: {Origin: 'https://example.invalid'}, data: [{name: 'page_view', path: '/guide', locale: 'en'}]})).status(), 403, 'A foreign origin must not write counters');
    const headers = {Origin: new URL(base).origin};
    for (const data of [[{name: 'page_view', path: '/guide', locale: 'en', characterName: privateValue}], [{name: 'page_view', path: `/guide?name=${privateValue}`, locale: 'en'}], [{name: 'unknown', path: '/guide', locale: 'en'}]]) assert.equal((await client.post('/api/analytics', {headers, data})).status(), 400);
    assert.equal((await client.post('/api/analytics', {headers: {...headers, 'Content-Type': 'application/json'}, data: '{'})).status(), 400);
    assert.equal((await client.post('/api/analytics', {headers: {...headers, 'Content-Type': 'application/json'}, data: 'x'.repeat(8193)})).status(), 413);
    const token = process.env.ANALYTICS_READ_TOKEN;
    if (token) {
      const date = new Date().toISOString().slice(0, 10);
      const readHeaders = {Authorization: `Bearer ${token}`};
      const read = async () => {
        const response = await client.get(`/api/analytics?date=${date}`, {headers: readHeaders});
        assert.equal(response.status(), 200); assert.match(response.headers()['cache-control'], /no-store/); assert.match(response.headers()['x-robots-tag'], /noindex/);
        return (await response.json()).counters;
      };
      const before = await read();
      const response = await client.post('/api/analytics', {headers, data: [{name: 'page_view', path: '/privacy-policy', locale: 'de'}, {name: 'web_vital', path: '/privacy-policy', locale: 'de', metric: 'LCP', value: 2499}]});
      assert.equal(response.status(), 204);
      const after = await read();
      assert.equal(after['de|/privacy-policy|page_view'], (before['de|/privacy-policy|page_view'] || 0) + 1);
      assert.equal(after['de|/privacy-policy|web_vital|LCP|24'], (before['de|/privacy-policy|web_vital|LCP|24'] || 0) + 1);
      assert.equal((await client.get('/api/analytics?date=2026-09-31', {headers: readHeaders})).status(), 400);
      cases++;
    } else process.stdout.write('SKIP: Authorized counter-read checks require ANALYTICS_READ_TOKEN.\n');
  } finally {await client.dispose();}
  assert.deepEqual(errors, [], 'No uncaught browser errors');
  process.stdout.write(`PASS: ${cases} anonymous analytics scenarios; privacy controls, working tools, payload whitelist, once-only browser retention and API rejection checks (${allEvents.length} intercepted events).\n`);
} finally {await browser.close();}
