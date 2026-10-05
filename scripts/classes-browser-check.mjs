import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';
import {installGameFixtures, installItemIconFixtures} from './qa-fixtures.mjs';

const base = process.env.QA_BASE_URL || 'http://localhost:3000';
const read = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));
const identities = await read('src/content/class-identities.json');
const skills = await read('src/content/class-skills.json');
const output = new URL('../.qa/classes/', import.meta.url);
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: existsSync(systemChrome) ? systemChrome : undefined});
const context = await browser.newContext({viewport: {width: 320, height: 900}, reducedMotion: 'reduce'});
await installGameFixtures(context);
await installItemIconFixtures(context);
// Rapid QA navigation must not consume the production analytics rate budget.
await context.route('**/api/analytics', (route) => route.fulfill({status: 204}));
const page = await context.newPage();
const errors = [];
const checked = [];
page.on('pageerror', (error) => errors.push(error.message));
page.on('response', (response) => {if (response.url().startsWith(base) && response.status() >= 400) errors.push(`${response.status()} ${response.url()}`);});

async function fit(label) {
  const metrics = await page.evaluate(() => ({width: innerWidth, scroll: document.documentElement.scrollWidth}));
  assert.ok(metrics.scroll <= metrics.width + 1, `${label}: document overflow ${JSON.stringify(metrics)}`);
}

try {
  for (const locale of ['en', 'ja', 'es', 'de']) {
    const prefix = locale === 'en' ? '' : `/${locale}`;
    await page.goto(`${base}${prefix}/classes`, {waitUntil: 'networkidle'});
    await expect(page.locator('.class-guide-card')).toHaveCount(8);
    await expect(page.locator('[data-class-icon]')).toHaveCount(8);
    await expect(page.locator('h2#class-icons')).toHaveCount(0);
    await fit(`${locale}/classes 320px`);
    for (const {id, names} of identities) {
      const card = page.locator(`[data-class="${id}"]`);
      await expect(card.locator('h3')).toHaveText(names[locale]);
      await expect(card.locator('a')).toHaveAttribute('href', `${prefix}/${id}`);
    }
    if (locale === 'en') {
      await page.locator('.class-finder').scrollIntoViewIfNeeded();
      await page.screenshot({path: fileURLToPath(new URL('classes-en-mobile.png', output))});
      await page.setViewportSize({width: 1440, height: 1000});
      await page.screenshot({path: fileURLToPath(new URL('classes-en-desktop.png', output))});
      await page.setViewportSize({width: 320, height: 900});
    }
    for (const {id} of identities) {
      await page.goto(`${base}${prefix}/${id}`, {waitUntil: 'networkidle'});
      await expect(page.locator('h1')).toHaveText((await read(`src/content/${locale}/${id}.json`)).title);
      await expect(page.locator(`[data-skill-focus="${id}"] tbody tr`)).toHaveCount(12);
      await expect(page.locator(`[data-skill-class="${id}"] [data-skill-id]`)).toHaveCount(35);
      for (const kind of ['active', 'passive', 'stigma']) {
        const index = ['active', 'passive', 'stigma'].indexOf(kind);
        const group = page.locator(`[data-skill-class="${id}"] details`).nth(index);
        if (index > 0) await group.locator('summary').click();
        for (const skill of skills[id].filter((entry) => entry.kind === kind)) await expect(group.locator(`[data-skill-id="${skill.id}"] th`)).toContainText(skill.names[locale]);
        await expect(group.locator('tbody tr').first()).toBeVisible();
        if (index > 0) await group.locator('summary').click();
      }
      await expect(page.locator('#article-sources, [data-article-edition]')).toHaveCount(0);
      await fit(`${locale}/${id} 320px`);
      if (locale === 'en' && id === 'templar') {
        await page.locator('#key-skills').scrollIntoViewIfNeeded();
        await page.screenshot({path: fileURLToPath(new URL('templar-skills-en.png', output))});
      }
      checked.push(`${locale}/${id}`);
    }
    await page.goto(`${base}${prefix}/builds`, {waitUntil: 'networkidle'});
    await expect(page.locator('.article-body table').nth(0).locator('tbody tr')).toHaveCount(8);
    await expect(page.locator('#three-concrete-examples + .guide-table-block tbody tr')).toHaveCount(8);
    for (const {id} of identities) await expect(page.locator(`.article-body a[href="${prefix}/${id}#key-skills"]`)).toHaveCount(1);
    await fit(`${locale}/builds 320px`);
    if (locale === 'en') {
      await page.locator('#three-concrete-examples').scrollIntoViewIfNeeded();
      await page.screenshot({path: fileURLToPath(new URL('builds-en-mobile.png', output))});
    }
    // Check enlarged text where class names and long skill notes are most constrained.
    await page.addStyleTag({content: '.article-body {font-size:32px} .article-body table {font-size:28px}'});
    await fit(`${locale}/builds enlarged text`);
    checked.push(`${locale}/builds`);
  }
  assert.deepEqual(errors, [], 'No failed local resources or browser errors');
  await writeFile(new URL('results.json', output), JSON.stringify({checked, errors, width: 320}, null, 2));
  console.log(`PASS: ${checked.length} class/build pages, all skill groups and four-language names, eight linked combat loops, 320px layout and enlarged text.`);
} finally {
  await browser.close();
}
