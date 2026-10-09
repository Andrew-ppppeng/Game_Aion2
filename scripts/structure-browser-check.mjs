import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';
import {installGameFixtures} from './qa-fixtures.mjs';

const base = (process.env.QA_BASE_URL || 'http://127.0.0.1:3000').replace(/\/$/, '');
const directory = new URL('../.qa/structure/', import.meta.url);
await mkdir(directory, {recursive: true});
const chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(chrome) ? chrome : undefined)});
const path = (locale, route) => `${base}${locale === 'en' ? '' : `/${locale}`}${route}`;
const locales = ['en', 'ja', 'es', 'de'];
const errors = [];
const context = await browser.newContext({viewport: {width: 1440, height: 1000}, reducedMotion: 'reduce'});
await installGameFixtures(context);
const payloads = [];
await context.route('**/api/analytics', async (route) => {
  if (route.request().method() === 'POST') payloads.push(...JSON.parse(route.request().postData() || '[]'));
  await route.fulfill({status: 204});
});
const page = await context.newPage();
page.on('pageerror', (error) => errors.push(error.message));
const overflow = async (label) => assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${label}: no horizontal overflow`);
const growthKey = 'aion2-growth-checklist-v1';
const starterKey = 'aion2-checklist-v1:guide';
const sessionKey = 'aion2-checklist-v1:daily-weekly-checklist';
let checks = 0;
try {
  for (const locale of locales) for (const route of ['/tools', '/guides', '/resources', '/tools/growth-checklist']) {
    await page.goto(path(locale, route), {waitUntil: 'networkidle'});
    await expect(page.locator('h1')).toHaveCount(1);
    await expect(page.locator('[data-primary-navigation] a')).toHaveCount(4);
    await expect(page.locator('[data-primary-navigation] a[aria-current]')).toHaveCount(1);
    assert.equal(await page.locator('link[rel="alternate"]').count(), 5);
    const canonical = await page.locator('link[rel="canonical"]').getAttribute('href');
    assert.equal(new URL(canonical).pathname, `${locale === 'en' ? '' : `/${locale}`}${route}`);
    await expect(page.locator('.desktop-sidebar [data-nav-section]')).toHaveCount(1);
    await overflow(`${locale}${route} desktop`);
    if (route === '/guides') await expect(page.locator('[data-directory-topic]')).toHaveCount(16);
    if (route === '/resources') await expect(page.locator('[data-directory-topic]')).toHaveCount(8);
    if (route === '/tools') {
      await expect(page.locator('[data-player-tool]')).toHaveCount(5);
      await expect(page.locator('[data-external-tool]')).toHaveCount(4);
      await expect(page.locator('[data-external-tool="meter"] a')).toHaveCount(1);
      for (const link of await page.locator('[data-external-tool] a[target="_blank"]').all()) assert.equal(await link.getAttribute('rel'), 'noopener noreferrer');
    }
    if (route.includes('growth')) {
      await expect(page.locator('[data-growth-goal]')).toHaveCount(12);
      await expect(page.locator('[data-growth-stage]')).toHaveCount(3);
      const links = await page.locator('[data-growth-goal] > a').evaluateAll((elements) => elements.map((element) => element.getAttribute('href')));
      for (const href of links) {
        const [slug, anchor] = href.replace(/^\/(ja|es|de)/, '').slice(1).split('#');
        const body = await readFile(new URL(`../src/content/${locale}/${slug}.mdx`, import.meta.url), 'utf8');
        if (anchor) assert.ok(body.includes(`id="${anchor}"`), `${locale}: growth guide anchor ${href}`);
      }
    }
    await page.setViewportSize({width: 320, height: 844});
    await overflow(`${locale}${route} mobile`);
    await page.locator('.mobile-menu-button').click();
    await expect(page.locator('#mobile-navigation [data-nav-section]')).toHaveCount(4);
    await expect(page.locator('#mobile-navigation .nav-group[open]')).toHaveCount(1);
    await page.keyboard.press('Escape');
    await expect(page.locator('.mobile-menu-button')).toBeFocused();
    await page.setViewportSize({width: 1440, height: 1000});
    checks++;
  }
  await page.goto(path('en', '/guide'), {waitUntil: 'networkidle'});
  await page.evaluate(({growthKey, starterKey, sessionKey}) => {
    localStorage.removeItem(growthKey);
    localStorage.setItem(starterKey, JSON.stringify(['official-client', 'coordinate-server']));
    localStorage.setItem(sessionKey, JSON.stringify(['duty']));
  }, {growthKey, starterKey, sessionKey});
  await page.goto(path('en', '/tools/growth-checklist'), {waitUntil: 'networkidle'});
  await expect(page.locator('.growth-total strong')).toHaveText('2 / 12');
  await page.locator('[data-growth-goal="manual-loop"] input').check();
  await expect(page.locator('.growth-total strong')).toHaveText('3 / 12');
  await expect.poll(() => payloads.some((event) => event.name === 'checklist_save' && event.target === 'growth')).toBe(true);
  await page.reload({waitUntil: 'networkidle'});
  await expect(page.locator('[data-growth-goal="manual-loop"] input')).toBeChecked();
  await page.locator('.language-switcher select').selectOption('ja');
  await expect(page.locator('html')).toHaveAttribute('lang', 'ja');
  await expect(page.locator('.growth-total strong')).toHaveText('3 / 12');
  await page.locator('[data-growth-goal="manual-loop"] input').uncheck();
  await expect(page.locator('.growth-total strong')).toHaveText('2 / 12');
  const tab = await context.newPage();
  await tab.goto(path('de', '/tools/growth-checklist'), {waitUntil: 'networkidle'});
  await page.locator('[data-growth-goal="skill-options"] input').check();
  await expect(tab.locator('[data-growth-goal="skill-options"] input')).toBeChecked();
  await tab.close();
  await page.locator('.growth-reset > button').click();
  await page.locator('[data-growth-reset-cancel]').click();
  await expect(page.locator('.growth-total strong')).toHaveText('3 / 12');
  await page.locator('.growth-reset > button').click();
  await page.locator('[data-growth-reset-confirm]').click();
  await expect(page.locator('.growth-total strong')).toHaveText('0 / 12');
  assert.equal(await page.evaluate((key) => localStorage.getItem(key), starterKey), '["official-client","coordinate-server"]');
  assert.equal(await page.evaluate((key) => localStorage.getItem(key), sessionKey), '["duty"]');
  await page.reload({waitUntil: 'networkidle'});
  await expect(page.locator('.growth-total strong')).toHaveText('0 / 12');
  await page.locator('[data-growth-goal="equipment-upgrade"] input').check();
  await page.goto(path('ja', '/'), {waitUntil: 'networkidle'});
  await expect(page.locator('[data-growth-resume] small')).toContainText('1 / 12');
  assert.deepEqual(await page.locator('.journey-card').evaluateAll((cards) => cards.map((card) => new URL(card.href).pathname.replace(/^\/ja/, ''))), ['/guide', '/tools/growth-checklist', '/classes', '/resources']);
  await page.goto(path('en', '/cleric'), {waitUntil: 'networkidle'});
  await expect(page.locator('.breadcrumbs a[href="/classes"]')).toHaveCount(1);
  await page.goto(path('en', '/classes'), {waitUntil: 'networkidle'});
  await expect(page.locator('[data-section-directory="classes"] [data-directory-topic]')).toHaveCount(3);
  await page.goto(path('de', '/tools/growth-checklist'), {waitUntil: 'networkidle'});
  await page.setViewportSize({width: 390, height: 844});
  await page.screenshot({path: fileURLToPath(new URL('growth-de-mobile.png', directory)), fullPage: true});
  await page.setViewportSize({width: 1440, height: 1000});
  await page.goto(path('en', '/tools'), {waitUntil: 'networkidle'});
  await page.screenshot({path: fileURLToPath(new URL('tools-en-desktop.png', directory)), fullPage: true});
  await page.goto(path('en', '/tools/growth-checklist'), {waitUntil: 'networkidle'});
  await page.screenshot({path: fileURLToPath(new URL('growth-en-desktop.png', directory)), fullPage: true});
  await page.waitForTimeout(2300);
  assert.ok(payloads.some((event) => event.name === 'checklist_save' && event.target === 'growth'), 'Growth saves emit anonymous counters');
  for (const event of payloads) assert.ok(Object.keys(event).every((key) => ['name', 'path', 'locale', 'target', 'metric', 'value', 'cohort'].includes(key)), 'No saved goal contents in analytics');

  const blocked = await browser.newContext({viewport: {width: 390, height: 844}});
  await blocked.addInitScript(() => {Storage.prototype.getItem = () => {throw new Error('Blocked');}; Storage.prototype.setItem = () => {throw new Error('Blocked');};});
  const blockedPage = await blocked.newPage();
  blockedPage.on('pageerror', (error) => errors.push(error.message));
  await blockedPage.goto(path('en', '/tools/growth-checklist'), {waitUntil: 'networkidle'});
  await blockedPage.locator('[data-growth-goal="manual-loop"] input').check();
  await expect(blockedPage.locator('.growth-total strong')).toHaveText('1 / 12');
  await expect(blockedPage.locator('[data-growth-storage]')).toContainText('will not survive a reload');
  await blocked.close();
  const noJs = await browser.newContext({javaScriptEnabled: false, viewport: {width: 390, height: 844}});
  const noJsPage = await noJs.newPage();
  await noJsPage.goto(path('en', '/tools/growth-checklist'));
  await expect(noJsPage.locator('[data-growth-goal] > a')).toHaveCount(12);
  await expect(noJsPage.locator('[data-growth-goal] input:disabled')).toHaveCount(12);
  await expect(noJsPage.locator('noscript .tool-note')).toBeVisible();
  await expect(noJsPage.locator('noscript .tool-note')).toContainText('Enable JavaScript');
  await noJs.close();
  assert.deepEqual(errors, []);
  await writeFile(new URL('results.json', directory), JSON.stringify({passed: true, localizedPageChecks: checks, growthGoals: 12, scenarios: ['migration', 'reload', 'language', 'cross-tab', 'undo', 'reset/cancel', 'independent old lists', 'home resume', 'blocked storage', 'no-JS', 'anonymous analytics']}, null, 2));
  console.log(`PASS: ${checks} localized hub/growth pages and persistent growth, privacy, no-JS, independent lists, mobile/desktop navigation.`);
} catch (error) {
  await page.screenshot({path: fileURLToPath(new URL('failure.png', directory)), fullPage: true});
  throw error;
} finally {await context.close(); await browser.close();}
