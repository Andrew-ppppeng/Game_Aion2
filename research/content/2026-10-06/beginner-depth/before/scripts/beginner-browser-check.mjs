import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const readJson = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));
const videos = await readJson('src/content/beginner-videos.json');
const slugs = ['settings', 'gear-progression', 'daily-weekly-checklist', 'crafting'];
const locales = ['en', 'ja', 'es', 'de'];
const output = new URL('../.qa/', import.meta.url);
await mkdir(output, {recursive: true});
const chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(chrome) ? chrome : undefined)});
const context = await browser.newContext({viewport: {width: 1440, height: 1000}, reducedMotion: 'reduce'});
await context.route('**/api/analytics', (route) => route.fulfill({status: 204}));
const page = await context.newPage();
const errors = [];
const youtubeRequests = [];
page.on('pageerror', (error) => errors.push(error.message));
page.on('request', (request) => {if (/youtube\.com|youtu\.be|ytimg\.com|googlevideo\.com/.test(new URL(request.url()).hostname)) youtubeRequests.push(request.url());});
const path = (locale, slug) => `${locale === 'en' ? '' : `/${locale}`}/${slug}`;
const serviceRegions = /(?<![A-Za-z])(?:KR|TW)(?![A-Za-z])|Taiwan|Taiwán|Korea(?!n)|Corea(?!no)|韓国(?!語)|台湾|韓台/i;
let cases = 0;
try {
  for (const locale of locales) {
    const old = await fetch(`${base}${path(locale, 'global-changes')}`, {redirect: 'manual'});
    assert.equal(old.status, 308);
    assert.equal(new URL(old.headers.get('location'), base).pathname, path(locale, 'guide'));
    const response = await page.goto(`${base}${path(locale, 'beginner-videos')}`, {waitUntil: 'networkidle'});
    assert.equal(response.status(), 200);
    await expect(page.locator('html')).toHaveAttribute('lang', locale);
    await expect(page.locator('h1')).toHaveCount(1);
    await expect(page.locator('.video-card')).toHaveCount(videos.length);
    await expect(page.locator('link[rel="alternate"]')).toHaveCount(5);
    assert.equal(new URL(await page.locator('link[rel="canonical"]').getAttribute('href')).pathname, path(locale, 'beginner-videos'));
    const schema = JSON.parse(await page.locator('script[type="application/ld+json"]').last().textContent());
    assert.equal(schema['@type'], 'CollectionPage');
    assert.equal(schema.mainEntity.itemListElement.length, videos.length);
    assert.doesNotMatch(await page.locator('body').innerText(), serviceRegions);
    await expect(page.locator('iframe')).toHaveCount(0);
    for (const video of videos) {
      const card = page.locator(`[data-video-id="${video.id}"]`);
      await expect(card.locator('h3')).toHaveText(video.titles[locale]);
      await expect(card.locator('time')).toHaveAttribute('datetime', video.publishedAt);
      assert.ok(await card.locator('img').evaluate((img) => img.complete && img.naturalWidth > 0));
      for (const link of await card.locator('a').all()) {
        await expect(link).toHaveAttribute('href', `https://www.youtube.com/watch?v=${video.id}`);
        await expect(link).toHaveAttribute('target', '_blank');
        await expect(link).toHaveAttribute('rel', 'noopener noreferrer');
      }
    }
    for (const [index, stage] of [[1, 'start'], [2, 'gear']]) {
      const button = page.locator('.video-filters button').nth(index);
      await button.click();
      await expect(button).toHaveAttribute('aria-pressed', 'true');
      await expect(page.locator('.video-card')).toHaveCount(videos.filter((v) => v.stage === stage).length);
      await expect(page.locator('.video-count')).toContainText(String(videos.filter((v) => v.stage === stage).length));
      await page.locator('.video-filters button').first().click();
    }
    for (const width of [1440, 390, 320]) {
      await page.setViewportSize({width, height: width === 1440 ? 1000 : 844});
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${locale}/${width}: video layout overflow`);
      for (const button of await page.locator('.video-filters button').all()) assert.ok((await button.boundingBox()).height >= 44);
      if (locale === 'en' && width !== 320) await page.screenshot({path: fileURLToPath(new URL(`beginner-videos-${width}.png`, output)), fullPage: true});
    }
    cases++;
    for (const slug of slugs) {
      const metadata = await readJson(`src/content/${locale}/${slug}.json`);
      await page.goto(`${base}${path(locale, slug)}`, {waitUntil: 'networkidle'});
      await expect(page.locator('h1')).toHaveText(metadata.title);
      await expect(page.locator('.video-card')).toHaveCount(videos.filter((v) => v.topics.includes(slug)).length);
      for (const section of metadata.toc) await expect(page.locator(`[id="${section.id}"]`)).toHaveCount(1);
      assert.doesNotMatch(await page.locator('body').innerText(), serviceRegions);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${locale}/${slug}: article overflow`);
      if (locale === 'en' && ['gear-progression', 'daily-weekly-checklist'].includes(slug)) await page.screenshot({path: fileURLToPath(new URL(`${slug}-mobile.png`, output)), fullPage: true});
      cases++;
    }
  }
  await page.setViewportSize({width: 1440, height: 1000});
  await page.goto(base, {waitUntil: 'networkidle'});
  await expect(page.locator('.video-card')).toHaveCount(videos.length);
  await page.screenshot({path: fileURLToPath(new URL('beginner-home-desktop.png', output)), fullPage: true});
  await page.setViewportSize({width: 390, height: 844});
  await page.screenshot({path: fileURLToPath(new URL('beginner-home-mobile.png', output)), fullPage: true});
  assert.deepEqual(youtubeRequests, [], 'No YouTube connection before a user follows a link');
  assert.deepEqual(errors, [], 'No browser errors');
  const plainContext = await browser.newContext({javaScriptEnabled: false});
  const plainPage = await plainContext.newPage();
  await plainPage.goto(`${base}/beginner-videos`);
  await expect(plainPage.locator('.video-card')).toHaveCount(videos.length);
  await expect(plainPage.locator('.video-card a')).toHaveCount(videos.length * 2);
  await plainContext.close();
  await writeFile(new URL('beginner-check.json', output), JSON.stringify({cases, videos: videos.map(({id}) => id), noPreClickYouTubeRequests: true, noJavaScriptLinks: true, locales}, null, 2));
  console.log(`PASS: ${cases} localized beginner pages, stage filtering, external-link privacy, no-JS recommendations, old-page redirects and 320/390/1440px layouts.`);
} finally {await browser.close();}
