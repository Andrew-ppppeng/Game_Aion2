import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(chrome) ? chrome : undefined)});
const context = await browser.newContext({viewport: {width: 390, height: 844}, reducedMotion: 'reduce'});
await context.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: base});
const page = await context.newPage();
const errors = [];
const feedbackPlaceholder = /has not been configured|No hay un contacto configurado|連絡先はまだ設定|noch nicht eingerichtet/i;
page.on('pageerror', (error) => errors.push(error.message));
await mkdir(new URL('../.qa/', import.meta.url), {recursive: true});
let checked = 0;
try {
  for (const locale of ['en', 'ja', 'es', 'de']) {
    const prefix = locale === 'en' ? '' : `/${locale}`;
    for (const slug of ['privacy-policy', 'terms-of-service']) {
      const response = await page.goto(`${base}${prefix}/${slug}`);
      assert.equal(response.status(), 200, `${locale}/${slug}: available`);
      await expect(page.locator('[data-page-status="site-info"]')).toBeVisible();
      await expect(page.locator('h1')).toHaveCount(1);
      assert.match(await page.locator('meta[name="robots"]').getAttribute('content'), /noindex/, `${locale}/${slug}: noindex retained`);
      const body = await page.locator('main').innerText();
      assert.doesNotMatch(body, /\?{3,}|\uFFFD|[A-Za-z]\?[A-Za-z]/, `${locale}/${slug}: translated text encoding`);
      assert.doesNotMatch(await page.locator('body').innerText(), feedbackPlaceholder, `${locale}/${slug}: no public contact placeholder`);
      await expect(page.locator('#corrections')).toHaveCount(1);
      const contact = page.locator('#corrections').locator('..').locator('a[data-feedback-contact]');
      await expect(contact).toHaveCount(1);
      await expect(contact).toHaveAttribute('href', 'mailto:feedback@aion2wiki.space');
      await expect(contact).toContainText('feedback@aion2wiki.space');
      if (slug === 'terms-of-service') await expect(page.locator('#editorial-policy')).toHaveCount(1);
      const template = page.locator('.feedback-template textarea');
      const value = await template.inputValue();
      assert.ok(value.length > 60, `${locale}: useful local correction template`);
      await page.locator('.feedback-template button').click();
      await expect.poll(async () => (await page.evaluate(() => navigator.clipboard.readText())).replace(/\r\n/g, '\n')).toBe(value);
      assert.ok((await page.locator('.feedback-template [role="status"]').innerText()).length > 10);
      await expect(page.locator('.footer-bottom a[href$="terms-of-service#editorial-policy"]')).toHaveCount(1);
      await expect(page.locator('.footer-bottom a[href$="terms-of-service#corrections"]')).toHaveCount(1);
      if (slug === 'privacy-policy') {
        const checkbox = page.locator('.analytics-preference input');
        await checkbox.uncheck();
        await expect.poll(() => page.evaluate(() => localStorage.getItem('aion2-analytics-opt-out-v1'))).toBe('true');
        await page.reload();
        await expect(checkbox).not.toBeChecked();
      }
      for (const width of [320, 390]) {
        await page.setViewportSize({width, height: 844});
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${locale}/${slug}/${width}: no horizontal overflow`);
        await page.locator('.article-body').evaluate((element) => {element.style.fontSize = '32px';});
        await page.locator('.footer-bottom').evaluate((element) => {element.style.fontSize = '28px';});
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${locale}/${slug}/${width}: doubled body/footer text fits`);
        await page.locator('.article-body').evaluate((element) => {element.style.fontSize = '';});
        await page.locator('.footer-bottom').evaluate((element) => {element.style.fontSize = '';});
      }
      if (locale === 'en' && slug === 'terms-of-service') {
        await page.evaluate(() => {if (document.activeElement instanceof HTMLElement) document.activeElement.blur(); window.scrollTo({top: 0, behavior: 'instant'});});
        await page.screenshot({path: fileURLToPath(new URL('../.qa/site-info-mobile.png', import.meta.url)), fullPage: true});
      }
      checked++;
    }
  }
  assert.deepEqual(errors, [], 'No site-information runtime errors');
  console.log(`PASS: ${checked} localized information pages, copy-only correction templates, persistent analytics opt-out and 320/390px doubled-text layout.`);
} finally {
  await browser.close();
}
