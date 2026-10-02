import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const output = new URL('../.qa/', import.meta.url);
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const executablePath = process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined);
const browser = await chromium.launch({headless: true, executablePath});
const failures = [];
const context = await browser.newContext({viewport: {width: 1440, height: 1000}, reducedMotion: 'reduce'});
await context.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: base});
const page = await context.newPage();
page.on('pageerror', (error) => failures.push(error.message));
page.on('console', (message) => {if (message.type() === 'error') failures.push(message.text());});
page.on('response', (response) => {if (response.status() >= 400 && response.url().startsWith(base)) failures.push(`${response.status()} ${response.url()}`);});

try {
  await page.clock.install({time: new Date('2026-10-02T11:00:00Z')});
  await page.goto(base, {waitUntil: 'networkidle'});
  await expect(page.locator('html')).toHaveAttribute('lang', 'en');
  await expect(page.locator('h1')).toHaveText('AION 2');
  await expect(page.locator('.desktop-sidebar nav a')).toHaveCount(21);
  await expect(page.locator('.journey-card')).toHaveCount(4);
  await expect(page.locator('.desktop-sidebar .coupon-state')).toHaveText('Announced');
  await page.locator('.desktop-sidebar .coupon-code-row button').click();
  await expect(page.locator('.desktop-sidebar .coupon-code-row button')).toHaveAttribute('aria-label', 'Copied');
  assert.equal(await page.evaluate(() => navigator.clipboard.readText()), 'TAKEFLIGHTAION2');
  await page.evaluate(() => Object.defineProperty(navigator.clipboard, 'writeText', {value: async () => {throw new Error('QA: clipboard denied');}, configurable: true}));
  await page.locator('.desktop-sidebar .coupon-code-row button').click();
  await expect(page.locator('.desktop-sidebar [role="alert"]')).toContainText('copy it manually');
  await page.clock.setSystemTime(new Date('2026-10-14T06:00:01Z'));
  await page.clock.runFor(30_000);
  await expect(page.locator('.desktop-sidebar .coupon-state')).toHaveText('Expired');
  await page.clock.setSystemTime(new Date('2026-10-02T11:00:00Z'));

  await page.goto(`${base}/classes?view=qa#main-content`, {waitUntil: 'networkidle'});
  await page.getByRole('combobox').selectOption('ja');
  await page.waitForURL('**/ja/classes?view=qa#main-content');
  await expect(page.locator('html')).toHaveAttribute('lang', 'ja');
  await expect(page.locator('h1')).toHaveText('全クラス');
  await expect(page.locator('.desktop-sidebar a[href="/ja/classes"]')).toHaveAttribute('aria-current', 'page');

  const layouts = [
    ['en', 1440, 1000], ['en', 1024, 768], ['en', 768, 1024], ['en', 390, 844], ['en', 320, 700],
    ['ja', 390, 844], ['es', 390, 844], ['de', 390, 844], ['ja', 1440, 1000], ['es', 1440, 1000], ['de', 1440, 1000],
  ];
  for (const [locale, width, height] of layouts) {
    await page.setViewportSize({width, height});
    await page.goto(`${base}${locale === 'en' ? '/' : `/${locale}`}`, {waitUntil: 'networkidle'});
    await expect(page.locator('html')).toHaveAttribute('lang', locale);
    const overflow = await page.evaluate(() => ({scroll: document.documentElement.scrollWidth, width: window.innerWidth}));
    assert.ok(overflow.scroll <= overflow.width + 1, `${locale} ${width}px horizontal overflow: ${JSON.stringify(overflow)}`);
    for (const button of await page.locator('.hero-buttons a').all()) {
      const bounds = await button.boundingBox();
      assert.ok(bounds && bounds.x >= 0 && bounds.x + bounds.width <= width, `${locale} hero button outside viewport`);
    }
  }

  await page.goto(`${base}/de`, {waitUntil: 'networkidle'});
  await page.setViewportSize({width: 390, height: 844});
  const menuButton = page.getByRole('button', {name: 'Navigation öffnen'});
  await menuButton.click();
  const dialog = page.getByRole('dialog');
  await expect(dialog).toBeVisible();
  assert.equal(await page.evaluate(() => document.body.style.overflow), 'hidden');
  await page.keyboard.press('Shift+Tab');
  assert.ok(await page.evaluate(() => !!document.activeElement?.closest('dialog')), 'Dialog traps keyboard focus');
  await page.keyboard.press('Escape');
  await expect(dialog).not.toBeVisible();
  await expect(menuButton).toBeFocused();
  assert.equal(await page.evaluate(() => document.body.style.overflow), '');
  await menuButton.click();
  await dialog.getByRole('link', {name: 'Einsteigerguide', exact: true}).click();
  await page.waitForURL('**/de/guide');
  await expect(page.locator('h1')).toHaveText('Einsteigerguide');
  await expect(dialog).not.toBeVisible();

  for (const [name, width, height] of [['desktop', 1440, 1000], ['mobile', 390, 844]]) {
    await page.setViewportSize({width, height});
    await page.goto(base, {waitUntil: 'networkidle'});
    await page.locator('.about-visual').scrollIntoViewIfNeeded();
    await expect(page.locator('.about-visual img')).toBeVisible();
    await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.screenshot({path: fileURLToPath(new URL(`home-${name}.png`, output)), fullPage: true});
    await page.screenshot({path: fileURLToPath(new URL(`home-${name}-fold.png`, output))});
  }
  assert.deepEqual(failures, [], 'No runtime, console, or local network errors');
  console.log('PASS: desktop and mobile; 11 locale/viewport combinations; language switching preserves page/query/hash; coupon copy/failure/expiry; keyboard focus, Escape and navigation; all images; no runtime errors.');
} finally {
  await context.close();
  await browser.close();
}
