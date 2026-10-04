import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const read = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));
const fixture = await read('tests/fixtures/cleric.json');
const fixtures = {en: fixture};
for (const locale of ['ja', 'es', 'de']) fixtures[locale] = await read(`tests/fixtures/cleric-${locale}.json`);
const items = await read('src/content/game-data/items.json');
const metadata = await read('src/content/game-data/meta.json');
const output = new URL('../.qa/tools/', import.meta.url);
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined)});
const context = await browser.newContext({viewport: {width: 390, height: 844}, timezoneId: 'Asia/Tokyo'});
const page = await context.newPage();
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
page.on('console', (message) => {if (message.type() === 'error' && !message.text().includes('Failed to load resource')) errors.push(message.text());});
let mode = 'normal';
let searchRequest;
const equipmentRequests = [];
const profile = fixture.character.data.info.profile;
const cid = profile.characterId;
const respond = (route, body, status = 200) => route.fulfill({status, contentType: 'application/json', body: JSON.stringify(body)});
// Real archived game responses make the UI test repeatable without sending extra game queries.
await context.route('**/api/aion2/**', async (route) => {
  const url = new URL(route.request().url());
  const locale = url.searchParams.get('locale') || 'en';
  const region = url.searchParams.get('region') || 'nae';
  if (url.pathname.endsWith('/meta')) {
    const record = metadata[region];
    return respond(route, {data: {servers: record.servers.data.serverList, classes: record.classes.data.classList.map((c) => ({id: c.id, name: c.text || c.name})), pcData: record.pcdata.data.pcDataList}, meta: null, error: null});
  }
  if (url.pathname.endsWith('/equipment-examples')) {
    equipmentRequests.push(url.href);
    return respond(route, {items: items.slice(2).map((record) => ({data: record.locales[locale].item, meta: {...record.locales[locale].meta, service: 'Global', region: 'nae', locale, freshness: 'snapshot'}, error: null}))});
  }
  if (url.pathname.endsWith('/search')) {
    searchRequest = url;
    if (mode === 'busy') return respond(route, {data: null, meta: null, error: {code: 'rate-limited', retryAfter: 60}}, 429);
    if (mode === 'blocked') return respond(route, {data: null, meta: null, error: {code: 'cache-unavailable'}}, 503);
    return respond(route, {data: {list: mode === 'empty' ? [] : [{characterId: cid, name: profile.characterName, level: profile.characterLevel, pcId: profile.pcId, race: profile.raceId, serverId: profile.serverId, serverName: profile.serverName, region}], pagination: {page: 1, size: 20, total: mode === 'empty' ? 0 : 1, endPage: 1}}, meta: fixture.character.meta, error: null});
  }
  if (url.pathname.includes('/equipment/')) return respond(route, fixtures[locale].item);
  if (url.pathname.includes('/characters/')) return respond(route, fixtures[locale].character);
  if (url.pathname.includes('/items/')) {
    if (region === 'as') return respond(route, {data: null, meta: null, error: {code: 'region-unavailable'}}, 503);
    const id = Number(url.pathname.split('/').at(-1));
    const record = items.find((r) => r.id === id)?.locales[locale];
    assert.ok(record, 'UI only requests observed template IDs');
    assert.equal(url.searchParams.get('enchantLevel'), '0', 'Default comparison uses verified +0 templates');
    return respond(route, {data: record.item, meta: {...record.meta, service: 'Global', locale, region, freshness: 'snapshot'}, error: null});
  }
  throw new Error(`Unexpected tool URL: ${url.pathname}`);
});
const path = (locale, slug) => `${base}${locale === 'en' ? '' : `/${locale}`}/${slug}`;
const overflow = async (label) => assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${label} fits the viewport`);

try {
  await page.clock.install({time: new Date('2026-10-03T11:00:00Z')});
  for (const locale of ['en', 'ja', 'es', 'de']) {
    await page.goto(path(locale, 'builds'));
    const equipment = page.locator('[data-equipment-cards]');
    await expect(equipment).toBeVisible();
    await expect(equipment.locator('[data-item-id]')).toHaveCount(2);
    assert.equal(equipmentRequests.length, ['en', 'ja', 'es', 'de'].indexOf(locale), 'Collapsed equipment does not request additional cards');
    await equipment.locator(':scope > details > summary').click();
    await expect(equipment.locator('[data-item-id]')).toHaveCount(22);
    assert.equal(equipmentRequests.length, ['en', 'ja', 'es', 'de'].indexOf(locale) + 1, 'First expansion makes one request');
    await expect(equipment.locator('[data-item-id="110760001"]')).toBeVisible();
    await overflow(`${locale} equipment cards`);

    await page.goto(path(locale, 'tools/character'));
    const tool = page.locator('[data-character-tool]');
    await tool.locator('input').first().fill('Testa');
    await tool.locator('button[type="submit"]').click();
    await expect(tool.locator('.character-match')).toHaveCount(1);
    assert.equal(searchRequest.searchParams.get('locale'), locale);
    await tool.locator('.character-match').click();
    await expect(tool.locator('h2')).toHaveText(profile.characterName);
    await tool.locator('.equipped-item').first().click();
    await expect(tool.locator('[data-item-id="110730048"]')).toBeVisible();
    const candidate = tool.locator('select').nth(3);
    await candidate.selectOption('110760001');
    await tool.locator('button.primary').last().click();
    await expect(tool.locator('[data-item-comparison]')).toBeVisible();
    await expect(tool.locator('[data-item-comparison] [data-item-id="110760001"]')).toBeVisible();
    await expect(tool.locator('[data-item-comparison] .tool-stats').first()).not.toHaveText('');
    await overflow(`${locale} character comparison`);
    await page.screenshot({path: fileURLToPath(new URL(`character-${locale}-mobile.png`, output)), fullPage: true});
  }

  await page.goto(path('en', 'tools/character'));
  const tool = page.locator('[data-character-tool]');
  await tool.locator('input').first().fill('Testa');
  await tool.locator('select').nth(2).selectOption('Cleric');
  await tool.locator('button[type="submit"]').click();
  await expect(tool.locator('.character-match')).toHaveCount(1);
  assert.equal(searchRequest.searchParams.get('class'), 'Cleric');
  await tool.locator('.character-match').click();
  await tool.getByRole('button', {name: 'Bookmark character', exact: true}).click();
  await expect(tool.getByText('Saved in this browser', {exact: true})).toBeVisible();
  await page.reload();
  await expect(page.locator('[data-character-tool] h2')).toHaveText(profile.characterName);
  await expect(page.locator('[data-character-tool] summary').first()).toContainText('(1)');
  await page.locator('.language-switcher select').selectOption('ja');
  await page.waitForURL('**/ja/tools/character?**');
  await expect(page.locator('[data-character-tool] h2')).toHaveText(profile.characterName);
  assert.equal(new URL(page.url()).searchParams.get('cid'), cid);

  for (const region of ['nae', 'naw', 'eu', 'la', 'as']) {
    await tool.locator('select').first().selectOption(region);
    await expect(tool.locator('select').nth(1).locator('option')).toHaveCount(metadata[region].servers.data.serverList.length + 1);
  }
  for (const [value, message] of [['empty', '該当する'], ['busy', '検索が混み'], ['blocked', 'キャラクター検索は一時']]) {
    mode = value;
    await tool.locator('input').first().fill('NoMatch');
    await tool.locator('button[type="submit"]').click();
    await expect(tool).toContainText(message);
  }
  mode = 'normal';

  await page.goto(path('en', 'maintenance'));
  const event = page.locator('[data-event="launch-transition-20261005"]');
  await page.locator('[data-event-timers] select').selectOption('UTC');
  await expect(event.locator('time').first()).toContainText('5:00');
  await page.locator('[data-event-timers] select').selectOption('Asia/Tokyo');
  await expect(event.locator('time').first()).toContainText('2:00 PM');
  await page.clock.setSystemTime(new Date('2026-10-05T05:00:00Z'));
  await page.clock.runFor(1100);
  await expect(event).toHaveAttribute('data-event-status', 'ongoing');
  await page.clock.setSystemTime(new Date('2026-10-05T13:00:00Z'));
  await page.clock.runFor(1100);
  await expect(event).toHaveAttribute('data-event-status', 'ended');
  const downloading = page.waitForEvent('download');
  await event.getByRole('button', {name: 'Add to calendar'}).click();
  const download = await downloading;
  const calendar = await readFile(await download.path(), 'utf8');
  assert.match(calendar, /DTSTART:20261005T050000Z/);
  assert.match(calendar, /DTEND:20261005T130000Z/);

  await page.goto(path('en', 'twitch-drops'));
  const pending = page.locator('[data-event="war-for-atreia-2-20261007"]');
  await expect(pending).toHaveAttribute('data-event-status', 'unconfirmed');
  await expect(pending.locator('.event-countdown')).toHaveCount(0);
  await expect(pending.locator('button')).toHaveCount(0);
  await pending.locator('input[type="checkbox"]').check();
  await page.goto(path('de', 'twitch-drops'));
  await expect(page.locator('[data-event="war-for-atreia-2-20261007"] input')).toBeChecked();

  await page.goto(path('en', 'monetization'));
  const budget = page.locator('[data-budget-planner]');
  const inputs = budget.locator('input');
  for (const [i, value] of ['5', '2', '10', 'Ore', '4', '5', '2.5'].entries()) await inputs.nth(i).fill(value);
  await budget.getByRole('button', {name: 'Calculate budget'}).click();
  await expect(budget.locator('.budget-total')).toContainText('47.5');
  await page.goto(path('de', 'monetization'));
  await expect(budget.locator('input').first()).toHaveValue('5');
  await expect(budget.locator('input').nth(3)).toHaveValue('Ore');
  await budget.locator('button[type="submit"]').click();
  await expect(budget.locator('.budget-total')).toContainText('47,5');
  await page.screenshot({path: fileURLToPath(new URL('budget-de-mobile.png', output)), fullPage: true});

  for (const width of [320, 390, 1440]) {
    await page.setViewportSize({width, height: 900});
    for (const slug of ['tools/character', 'builds', 'maintenance', 'monetization']) {
      await page.goto(path('de', slug));
      await overflow(`de ${slug} ${width}`);
    }
  }

  const blocked = await browser.newContext({viewport: {width: 320, height: 800}});
  await blocked.addInitScript(() => {
    Storage.prototype.getItem = () => {throw new DOMException('Blocked for verification', 'SecurityError');};
    Storage.prototype.setItem = () => {throw new DOMException('Blocked for verification', 'SecurityError');};
  });
  const blockedPage = await blocked.newPage();
  await blockedPage.goto(path('en', 'monetization'));
  const localInputs = blockedPage.locator('[data-budget-planner] input');
  for (const [i, value] of ['5', '2', '10', 'Ore', '4', '5', '2.5'].entries()) await localInputs.nth(i).fill(value);
  await blockedPage.locator('[data-budget-planner] button[type="submit"]').click();
  await expect(blockedPage.locator('.budget-total')).toContainText('47.5');
  await blocked.close();
  await page.setViewportSize({width: 312, height: 844});
  await page.clock.setSystemTime(new Date());
  await page.goto(`${base}/de`, {waitUntil: 'networkidle'});
  await page.evaluate(() => {
    const sizes = [...document.querySelectorAll('*')].filter((element) => element instanceof HTMLElement && !['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(element.tagName)).map((element) => [element, parseFloat(getComputedStyle(element).fontSize)]);
    for (const [element, size] of sizes) if (Number.isFinite(size)) element.style.fontSize = `${size * 2}px`;
  });
  await overflow('de home 312px 200% text');
  await mkdir(new URL('../review/', output), {recursive: true});
  await page.screenshot({path: fileURLToPath(new URL('../review/de-mobile-200.png', output))});
  assert.deepEqual(errors, [], 'No hydration or runtime errors');
  console.log('PASS: four-language equipment and character UI; regions, filters, template comparison, bookmarks/reload, UTC boundaries, calendar, pending times, local plans, blocked storage and 320/390/1440px layouts.');
} finally {
  await context.close();
  await browser.close();
}
