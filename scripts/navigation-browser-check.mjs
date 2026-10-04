import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';
import {installGameFixtures, readQaJson} from './qa-fixtures.mjs';

const base = (process.env.QA_BASE_URL || 'http://127.0.0.1:3000').replace(/\/$/, '');
const output = new URL('../.qa/navigation/', import.meta.url);
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined)});
const context = await browser.newContext({viewport: {width: 390, height: 844}, reducedMotion: 'reduce'});
await installGameFixtures(context);
const page = await context.newPage();
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
const prefix = (locale) => locale === 'en' ? '' : `/${locale}`;

try {
  for (const locale of ['en', 'ja', 'es', 'de']) {
    await page.goto(`${base}${prefix(locale)}/`, {waitUntil: 'networkidle'});
    const desktopGroups = page.locator('.desktop-sidebar .nav-group');
    assert.ok(await desktopGroups.count() > 0);
    await expect(page.locator('.desktop-sidebar .nav-group[open]')).toHaveCount(await desktopGroups.count());
    const trigger = page.locator('.mobile-menu-button');
    const dialog = page.locator('#mobile-navigation');
    await expect(dialog).not.toBeVisible();
    assert.equal(await dialog.getAttribute('open'), null);
    const closedButton = dialog.locator('button').first();
    await closedButton.evaluate((element) => element.focus());
    await expect(closedButton).not.toBeFocused();
    await trigger.focus();
    await page.keyboard.press('Tab');
    assert.ok(await page.evaluate(() => !document.activeElement?.closest('#mobile-navigation')), `${locale}: closed menu is excluded from Tab order`);
    for (const control of [trigger, page.locator('.hero-buttons a').first()]) {
      assert.ok(await control.evaluate((element) => {
        const bounds = element.getBoundingClientRect();
        const hit = document.elementFromPoint(bounds.left + bounds.width / 2, bounds.top + bounds.height / 2);
        return hit === element || element.contains(hit);
      }), `${locale}: closed menu does not block visible controls`);
    }
    await trigger.click();
    await expect(dialog).toBeVisible();
    await expect(dialog.locator('.nav-group[open]')).toHaveCount(0);
    const href = `${prefix(locale)}/gladiator`;
    const classGroup = dialog.locator('.nav-group').filter({has: page.locator(`a[href="${href}"]`)});
    await classGroup.locator('summary').focus();
    await page.keyboard.press('Enter');
    await expect(classGroup).toHaveAttribute('open', '');
    await dialog.locator(`a[href="${href}"]`).click();
    await page.waitForURL(`**${href}`);
    await expect(page.locator('h1')).toHaveText((await readQaJson(`src/content/${locale}/gladiator.json`)).title);
    await expect(dialog).not.toBeVisible();
    await expect(trigger).toHaveAttribute('aria-expanded', 'false');

    await trigger.click();
    await expect(classGroup).toHaveAttribute('open', '');
    await expect(dialog.locator('.nav-group[open]')).toHaveCount(1);
    const close = dialog.locator('button').first();
    await close.focus();
    await page.keyboard.press('Shift+Tab');
    assert.ok(await dialog.evaluate((element) => {
      const candidates = [...element.querySelectorAll('a[href], button:not(:disabled), summary, [tabindex="0"]')].filter((item) => item.getClientRects().length > 0);
      return document.activeElement === candidates.at(-1);
    }), `${locale}: Shift+Tab wraps inside the menu`);
    await page.keyboard.press('Tab');
    await expect(close).toBeFocused();
    await page.keyboard.press('Escape');
    await expect(dialog).not.toBeVisible();
    await expect(trigger).toBeFocused();
    await expect.poll(() => page.evaluate(() => document.body.style.overflow)).toBe('');

    const firstAnchor = (await readQaJson(`src/content/${locale}/steam.json`)).toc[0].id;
    await page.goto(`${base}${prefix(locale)}/steam?review=nav#${firstAnchor}`, {waitUntil: 'networkidle'});
    const next = {en: 'ja', ja: 'es', es: 'de', de: 'en'}[locale];
    await page.locator('.language-switcher select').selectOption(next);
    await page.waitForURL((value) => value.pathname === `${prefix(next)}/steam` && value.searchParams.get('review') === 'nav' && value.hash === `#${firstAnchor}`);
    await expect(page.locator('html')).toHaveAttribute('lang', next);
    const destination = new URL(page.url());
    assert.equal(destination.searchParams.get('review'), 'nav', `${locale}: language switch keeps query`);
    assert.equal(destination.hash, `#${firstAnchor}`, `${locale}: language switch keeps section`);
    await trigger.click();
    await expect(dialog.locator(`a[href="${prefix(next)}/steam"]`)).toHaveAttribute('aria-current', 'page');
    await page.keyboard.press('Escape');
    await expect(dialog).not.toBeVisible();
    await expect(trigger).toBeFocused();
    console.log(`${locale}: menu disclosure, article navigation, current group, Tab/Escape/focus and language/query/hash passed`);
  }
  await page.setViewportSize({width: 312, height: 844});
  for (const locale of ['en', 'ja', 'es', 'de']) {
    await page.goto(`${base}${prefix(locale)}/`, {waitUntil: 'networkidle'});
    await page.evaluate(() => {
      const elements = [...document.querySelectorAll('*')].filter((element) => element instanceof HTMLElement && !['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(element.tagName));
      const sizes = elements.map((element) => parseFloat(getComputedStyle(element).fontSize));
      elements.forEach((element, index) => {element.style.fontSize = `${sizes[index] * 2}px`;});
    });
    const assertNoOverflow = async (state) => {
      const dimensions = await page.evaluate(() => ({scroll: document.documentElement.scrollWidth, width: innerWidth}));
      assert.ok(dimensions.scroll <= dimensions.width + 1, `${locale}: 312px/200% ${state} does not overflow: ${JSON.stringify(dimensions)}`);
    };
    const assertControl = async (control, name) => {
      await expect(control).toBeVisible();
      await expect(control).toBeEnabled();
      const bounds = await control.boundingBox();
      assert.ok(bounds && bounds.x >= -1 && bounds.y >= -1 && bounds.x + bounds.width <= 313 && bounds.y + bounds.height <= 845, `${locale}: 312px/200% ${name} remains in the viewport`);
      await control.click({trial: true});
      assert.ok(await control.evaluate((element) => {
        const bounds = element.getBoundingClientRect();
        const hit = document.elementFromPoint(bounds.left + bounds.width / 2, bounds.top + bounds.height / 2);
        return hit === element || element.contains(hit);
      }), `${locale}: 312px/200% ${name} is not obstructed`);
    };
    const trigger = page.locator('.mobile-menu-button');
    const language = page.locator('.language-switcher select');
    const dialog = page.locator('#mobile-navigation');
    await expect(dialog).not.toBeVisible();
    await assertNoOverflow('closed menu');
    await assertControl(trigger, 'menu button');
    await assertControl(language, 'language selector');
    await language.selectOption(locale);
    await expect(page.locator('html')).toHaveAttribute('lang', locale);
    await trigger.click();
    await expect(dialog).toBeVisible();
    await assertNoOverflow('open menu');
    const close = dialog.locator('button').first();
    await assertControl(close, 'close button');
    await close.click();
    await expect(dialog).not.toBeVisible();
    await expect(trigger).toBeFocused();
    await trigger.click();
    await page.keyboard.press('Escape');
    await expect(dialog).not.toBeVisible();
    await expect(trigger).toBeFocused();
    await assertNoOverflow('menu closed with Escape');
    console.log(`${locale}: 312px/200% closed/open menu fits, controls are actionable and Escape returns focus`);
  }
  // Pre-layout must not turn hidden navigation into eager tool downloads.
  const payloadPage = await context.newPage();
  const scripts = [];
  payloadPage.on('pageerror', (error) => errors.push(error.message));
  payloadPage.on('response', (response) => {if (response.request().resourceType() === 'script') scripts.push(response.text());});
  await payloadPage.goto(`${base}/steam`, {waitUntil: 'networkidle'});
  const scriptText = (await Promise.all(scripts)).join('\n');
  for (const marker of ['data-character-tool', 'data-budget-planner', 'data-event-timers', 'data-more-equipment', 'data-class-icon']) {
    assert.ok(!new RegExp(`["']${marker}["']\\s*:`).test(scriptText), `Hidden navigation does not eagerly load ${marker}`);
  }
  await payloadPage.close();
  assert.deepEqual(errors, [], 'No navigation runtime errors');
  console.log('PASS: four-language mobile navigation, safe hidden pre-layout, preserved desktop groups and deferred tool implementations.');
} catch (error) {
  await page.screenshot({path: fileURLToPath(new URL('failure.png', output)), fullPage: true});
  throw error;
} finally {
  await context.close();
  await browser.close();
}
