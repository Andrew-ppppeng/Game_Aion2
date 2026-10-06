import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const readJson = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));
const videos = await readJson('src/content/beginner-videos.json');
const slugs = ['settings', 'gear-progression', 'daily-weekly-checklist', 'crafting', 'guide', 'leveling', 'gathering', 'macro-guide'];
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
      await card.locator('img').scrollIntoViewIfNeeded();
      await expect.poll(() => card.locator('img').evaluate((img) => img.complete && img.naturalWidth > 0), {message: `${video.id}: lazy cover loads when scrolled into view`}).toBe(true);
      const mainUrl = `https://www.youtube.com/watch?v=${video.id}${video.startSeconds ? `&t=${video.startSeconds}s` : ''}`;
      await expect(card.locator('.video-card-cover')).toHaveAttribute('href', mainUrl);
      for (const [index, chapter] of video.chapters.entries()) {
        await expect(card.locator('.video-chapters a').nth(index)).toHaveAttribute('href', `https://www.youtube.com/watch?v=${video.id}${chapter.seconds ? `&t=${chapter.seconds}s` : ''}`);
        await expect(card.locator('.video-chapters a').nth(index)).toContainText(chapter.labels[locale]);
      }
      for (const link of await card.locator('a').all()) {
        const href = new URL(await link.getAttribute('href'));
        assert.equal(href.hostname, 'www.youtube.com');
        assert.equal(href.searchParams.get('v'), video.id);
        await expect(link).toHaveAttribute('target', '_blank');
        await expect(link).toHaveAttribute('rel', 'noopener noreferrer');
      }
    }
    for (const category of [...new Set(videos.map((v) => v.category))]) {
      const button = page.locator(`[data-category="${category}"]`);
      await button.click();
      await expect(button).toHaveAttribute('aria-pressed', 'true');
      await expect(page.locator('.video-card')).toHaveCount(videos.filter((v) => v.category === category).length);
      await expect(page.locator('.video-count')).toContainText(String(videos.filter((v) => v.category === category).length));
      await page.locator('.video-filters button').first().click();
    }
    const search = page.locator('#video-search');
    await search.fill('  sywo  ');
    await expect(page.locator('.video-card')).toHaveCount(1);
    await expect(page.locator('.video-card')).toHaveAttribute('data-video-id', 'J8WVY3FxPQM');
    await search.fill('sywo   gear');
    await expect(page.locator('.video-card')).toHaveCount(1);
    await expect(page.locator('.video-card')).toHaveAttribute('data-video-id', 'J8WVY3FxPQM');
    await search.fill(videos.find((v) => v.category === 'crafting').titles[locale]);
    await expect(page.locator('.video-card')).toHaveCount(1);
    await search.fill('no-such-video-xyz');
    await expect(page.locator('.video-card')).toHaveCount(0);
    await page.locator('.video-empty button').click();
    await expect(page.locator('.video-card')).toHaveCount(videos.length);
    await page.locator('.video-class-toggle input').check();
    await expect(page.locator('.video-card')).toHaveCount(videos.filter((v) => v.category !== 'class').length);
    await expect(page.locator('[data-category="class"]')).toHaveCount(0);
    await page.locator('.video-class-toggle input').uncheck();
    for (const width of [1440, 390, 320]) {
      await page.setViewportSize({width, height: width === 1440 ? 1000 : 844});
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${locale}/${width}: video layout overflow`);
      for (const button of await page.locator('.video-filters button').all()) assert.ok((await button.boundingBox()).height >= 44);
      if (locale === 'en' && width !== 320) await page.screenshot({path: fileURLToPath(new URL(`beginner-videos-${width}.png`, output)), fullPage: true});
    }
    await page.evaluate(() => {
      const sizes = [...document.querySelectorAll('*')].filter((element) => element instanceof HTMLElement && !['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(element.tagName))
        .map((element) => [element, parseFloat(getComputedStyle(element).fontSize)]);
      for (const [element, size] of sizes) if (Number.isFinite(size)) element.style.fontSize = `${size * 2}px`;
    });
    const enlarged = await page.evaluate(() => ({width: innerWidth, scrollWidth: document.documentElement.scrollWidth,
      controls: [...document.querySelectorAll('.video-search input, .video-filters button')].map((element) => ({left: element.getBoundingClientRect().left, right: element.getBoundingClientRect().right}))}));
    assert.ok(enlarged.scrollWidth <= enlarged.width + 1, `${locale}/320px: video layout at 200% text`);
    for (const control of enlarged.controls) assert.ok(control.left >= -1 && control.right <= enlarged.width + 1, `${locale}/320px: enlarged video controls fit`);
    await page.locator('[data-category="settings"]').click();
    await expect(page.locator('.video-card')).toHaveCount(videos.filter((v) => v.category === 'settings').length);
    if (locale === 'de') {await page.evaluate(() => scrollTo(0, 0)); await page.screenshot({path: fileURLToPath(new URL('beginner-videos-de-320-text200.png', output))});}
    cases++;
    for (const slug of slugs) {
      const metadata = await readJson(`src/content/${locale}/${slug}.json`);
      await page.goto(`${base}${path(locale, slug)}`, {waitUntil: 'networkidle'});
      await expect(page.locator('h1')).toHaveText(metadata.title);
      const recommendations = videos.filter((v) => v.topics.includes(slug)).slice(0, 3);
      await expect(page.locator('.video-card')).toHaveCount(recommendations.length);
      for (const v of recommendations) {
        const seconds = v.articleStarts[slug];
        await expect(page.locator(`[data-video-id="${v.id}"] .video-card-cover`)).toHaveAttribute('href', `https://www.youtube.com/watch?v=${v.id}${seconds ? `&t=${seconds}s` : ''}`);
      }
      for (const section of metadata.toc) await expect(page.locator(`[id="${section.id}"]`)).toHaveCount(1);
      if (slug === 'daily-weekly-checklist') {
        const checklist = page.locator('[data-checklist="daily-weekly-checklist"]');
        const boxes = checklist.locator('input[type="checkbox"]');
        await expect(boxes).toHaveCount(6);
        await boxes.first().check();
        await page.reload({waitUntil: 'networkidle'});
        await expect(boxes.first()).toBeChecked();
        await checklist.locator('button').click();
        await expect(boxes.first()).not.toBeChecked();
      }
      assert.doesNotMatch(await page.locator('body').innerText(), serviceRegions);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${locale}/${slug}: article overflow`);
      if (locale === 'en' && ['gear-progression', 'daily-weekly-checklist'].includes(slug)) await page.screenshot({path: fileURLToPath(new URL(`${slug}-mobile.png`, output)), fullPage: true});
      cases++;
    }
  }
  await page.setViewportSize({width: 1440, height: 1000});
  await page.goto(base, {waitUntil: 'networkidle'});
  await expect(page.locator('.video-card')).toHaveCount(Math.min(6, videos.filter((v) => v.featuredRank !== undefined).length));
  await page.screenshot({path: fileURLToPath(new URL('beginner-home-desktop.png', output)), fullPage: true});
  await page.setViewportSize({width: 390, height: 844});
  await page.screenshot({path: fileURLToPath(new URL('beginner-home-mobile.png', output)), fullPage: true});
  assert.deepEqual(youtubeRequests, [], 'No YouTube connection before a user follows a link');
  assert.deepEqual(errors, [], 'No browser errors');
  const plainContext = await browser.newContext({javaScriptEnabled: false});
  const plainPage = await plainContext.newPage();
  await plainPage.goto(`${base}/beginner-videos`);
  await expect(plainPage.locator('.video-card')).toHaveCount(videos.length);
  await expect(plainPage.locator('.video-card a')).toHaveCount(videos.reduce((count, v) => count + 2 + v.chapters.length, 0));
  await plainContext.close();
  await writeFile(new URL('beginner-check.json', output), JSON.stringify({cases, videos: videos.map(({id}) => id), noPreClickYouTubeRequests: true, noJavaScriptLinks: true, locales}, null, 2));
  console.log(`PASS: ${cases} localized beginner pages, topic/search/class filtering, chapter links, saved checklist reset, external-link privacy, no-JS recommendations, 320/390/1440px layouts and 200% video text.`);
} finally {await browser.close();}
