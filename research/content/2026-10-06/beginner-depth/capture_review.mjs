import {chromium} from '@playwright/test';
import {existsSync} from 'node:fs';
import {mkdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';

// One-time visual review of the rebuilt production preview.
const output = new URL('../../../../.qa/beginner-depth/', import.meta.url);
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: existsSync(systemChrome) ? systemChrome : undefined});
const context = await browser.newContext({viewport: {width: 390, height: 844}, reducedMotion: 'reduce'});
await context.route('**/api/analytics', (route) => route.fulfill({status: 204}));
const page = await context.newPage();
const capture = async (path, name, selector) => {
  await page.goto(`http://127.0.0.1:3100${path}`, {waitUntil: 'networkidle'});
  if (selector) {
    await page.locator(selector).scrollIntoViewIfNeeded();
    await page.locator(selector).screenshot({path: fileURLToPath(new URL(`${name}.png`, output))});
  } else {
    await page.evaluate(() => scrollTo(0, 0));
    await page.screenshot({path: fileURLToPath(new URL(`${name}.png`, output))});
  }
};
try {
  await capture('/beginner-videos', 'videos-mobile');
  await capture('/crafting', 'crafting-mobile');
  await capture('/crafting', 'crafting-recipe-mobile', '.guide-figure');
  await capture('/daily-weekly-checklist', 'daily-checklist-mobile', '.guide-checklist');
  await capture('/ja/crafting', 'crafting-ja-mobile');
  await capture('/macro-guide', 'macro-editor-mobile', '[data-asset-id="macro-global-editor"]');
  await page.setViewportSize({width: 1440, height: 1000});
  await capture('/beginner-videos', 'videos-desktop');
  await page.locator('[data-video-id="NdsTPYuL6E4"] img').scrollIntoViewIfNeeded();
  await page.locator('[data-video-id="NdsTPYuL6E4"]').screenshot({path: fileURLToPath(new URL('spiritmaster-card.png', output))});
  console.log('Captured 8 production-preview views.');
} finally {await browser.close();}
