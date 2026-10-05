import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
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
// Exercise the user-triggered iframe without depending on YouTube availability in CI.
await context.route('https://www.youtube-nocookie.com/embed/**', (route) => route.fulfill({status: 200, contentType: 'text/html', body: '<title>Video player fixture</title>'}));
const page = await context.newPage();
const errors = [];
const checked = [];
const videos = await read('src/content/class-videos.json');
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
    await expect(page.locator('[data-video-gallery] select option')).toHaveCount(8);
    for (const {id} of identities) {
      await page.locator('[data-video-gallery] select').selectOption(id);
      await expect(page.locator(`[data-class-video="${id}"]`)).toBeVisible();
      await expect(page.locator('.class-video a')).toHaveAttribute('href', `https://www.youtube.com/watch?v=${videos[id].videoId}`);
    }
    for (const {id} of identities) {
      await page.goto(`${base}${prefix}/${id}`, {waitUntil: 'networkidle'});
      await expect(page.locator('h1')).toHaveText((await read(`src/content/${locale}/${id}.json`)).title);
      await expect(page.locator(`[data-skill-focus="${id}"] tbody tr`)).toHaveCount(12);
      await expect(page.locator(`[data-skill-class="${id}"] [data-skill-id]`)).toHaveCount(35);
      await expect(page.locator(`[data-skill-map="${id}"] .skill-map-row`)).toHaveCount(3);
      await expect(page.locator(`[data-class-video="${id}"]`)).toHaveCount(1);
      await expect(page.locator('iframe')).toHaveCount(0);
      for (const kind of ['active', 'passive', 'stigma']) {
        const index = ['active', 'passive', 'stigma'].indexOf(kind);
        const group = page.locator(`[data-skill-class="${id}"] details`).nth(index);
        if (index > 0) await group.locator('summary').click();
        for (const skill of skills[id].filter((entry) => entry.kind === kind)) await expect(group.locator(`[data-skill-id="${skill.id}"] th`)).toContainText(skill.names[locale]);
        await expect(group.locator('tbody tr').first()).toBeVisible();
        const loaded = await group.locator('img').evaluateAll(async (images) => {
          await Promise.all(images.map((image) => {image.loading = 'eager'; return image.decode();}));
          return images.every((image) => image.naturalWidth >= 32);
        });
        assert.ok(loaded, `${locale}/${id}/${kind}: real skill icons load`);
        if (index > 0) await group.locator('summary').click();
      }
      await expect(page.locator('#article-sources, [data-article-edition]')).toHaveCount(0);
      await fit(`${locale}/${id} 320px`);
      if (locale === 'en' && id === 'templar') {
        const skillLink = page.locator('[data-map-skill="12240000"]').first();
        await skillLink.click();
        await expect(page.locator('#skill-12240000')).toBeInViewport();
        await page.locator('#key-skills').scrollIntoViewIfNeeded();
        await page.screenshot({path: fileURLToPath(new URL('templar-skills-en.png', output))});
        const [download] = await Promise.all([page.waitForEvent('download'), page.locator('[data-skill-map="templar"] .skill-map-actions a[download]').click()]);
        assert.equal(download.suggestedFilename(), 'skill-map-templar-en.png');
        const downloadPath = fileURLToPath(new URL('download-templar-en.png', output));
        await download.saveAs(downloadPath);
        assert.equal(await download.failure(), null);
        assert.equal(createHash('sha256').update(await readFile(downloadPath)).digest('hex'), createHash('sha256').update(await readFile(new URL('../public/media/guides/skill-map-templar-en.png', import.meta.url))).digest('hex'), 'Saved diagram is the actual image');
        await page.setViewportSize({width:1440,height:1000});
        await page.locator('[data-skill-map="templar"]').screenshot({path:fileURLToPath(new URL('templar-map-desktop.png',output))});
        await page.setViewportSize({width:320,height:900});
        await page.locator('.class-video-play').click();
        await expect(page.locator('.class-video iframe')).toHaveAttribute('src', `https://www.youtube-nocookie.com/embed/${videos[id].videoId}?autoplay=1&rel=0&playsinline=1`);
      }
      checked.push(`${locale}/${id}`);
    }
    await page.goto(`${base}${prefix}/builds`, {waitUntil: 'networkidle'});
    await expect(page.locator('.article-body table').nth(0).locator('tbody tr')).toHaveCount(8);
    await expect(page.locator('#three-concrete-examples + .guide-table-block tbody tr')).toHaveCount(8);
    for (const {id} of identities) await expect(page.locator(`.article-body a[href="${prefix}/${id}#key-skills"]`)).toHaveCount(1);
    for (const {id} of identities) {
      await page.locator('[data-build-maps] select').selectOption(id);
      await expect(page.locator('[data-build-map-panel]:visible')).toHaveCount(1);
      await expect(page.locator(`[data-build-map-panel="${id}"] [data-skill-map]`)).toBeVisible();
    }
    for (const value of ['speed', 'damage', 'mobile']) {
      await page.locator(`[data-specialization-tree] input[value="${value}"]`).check();
      await expect(page.locator('[data-specialization-tree] input:checked')).toHaveCount(1);
      await expect(page.locator('[data-specialization-tree] label.selected input')).toHaveAttribute('value', value);
    }
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
  console.log(`PASS: ${checked.length} class/build pages, actual skill icons, diagram links, class selectors, video activation, exclusive specialization choices, 320px layout and enlarged text.`);
} finally {
  await browser.close();
}
