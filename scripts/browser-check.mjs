import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';
import {installGameFixtures, installItemIconFixtures} from './qa-fixtures.mjs';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const output = new URL('../.qa/', import.meta.url);
const readJson = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));
const plan = await readJson('content-topics.json');
const slugs = plan.categories.flatMap(({keywords}) => keywords.map((keyword) => keyword.replace(/^aion 2 /, '').replaceAll(' ', '-')));
const classIdentities = await readJson('src/content/class-identities.json');
const guideAssets = await readJson('src/content/guide-assets.json');
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const executablePath = process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined);
const browser = await chromium.launch({headless: true, executablePath});
const failures = [];
const context = await browser.newContext({viewport: {width: 1440, height: 1000}, reducedMotion: 'reduce'});
await installGameFixtures(context);
await installItemIconFixtures(context);
await context.route('**/api/analytics', (route) => route.fulfill({status: 204}));
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
  await expect(page.locator('.desktop-sidebar nav a')).toHaveCount(slugs.length + 4);
  await expect(page.locator('.desktop-sidebar .sidebar-status, .desktop-sidebar .coupon-details')).toHaveCount(0);
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
  await page.locator('.language-switcher select').selectOption('ja');
  await page.waitForURL('**/ja/classes?view=qa#main-content');
  await expect(page.locator('html')).toHaveAttribute('lang', 'ja');
  await expect(page.locator('h1')).toHaveText((await readJson('src/content/ja/classes.json')).title);
  await expect(page.locator('.desktop-sidebar a[href="/ja/classes"]')).toHaveAttribute('aria-current', 'page');

  const layouts = [
    ['en', 1440, 1000], ['en', 1024, 768], ['en', 768, 1024], ['en', 390, 844], ['en', 320, 700],
    ['ja', 390, 844], ['es', 390, 844], ['de', 390, 844], ['ja', 1440, 1000], ['es', 1440, 1000], ['de', 1440, 1000],
  ];
  for (const [locale, width, height] of layouts) {
    await page.setViewportSize({width, height});
    await page.goto(`${base}${locale === 'en' ? '/' : `/${locale}`}`, {waitUntil: 'domcontentloaded'});
    await expect(page.locator('html')).toHaveAttribute('lang', locale);
    await expect(page.locator('h1')).toHaveText((await readJson(`src/messages/${locale}.json`)).home.hero.title);
    await expect(page.locator('.hero-buttons')).toBeVisible();
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
  const guideGroup = dialog.locator('details').filter({has: page.locator('a[href="/de/guide"]')});
  if (await guideGroup.getAttribute('open') === null) await guideGroup.locator('summary').click();
  await dialog.getByRole('link', {name: 'Einsteigerguide', exact: true}).click();
  await page.waitForURL('**/de/guide');
  await expect(page.locator('h1')).toHaveText((await readJson('src/content/de/guide.json')).title);
  await expect(dialog).not.toBeVisible();

  for (const slug of slugs) {
    const firstSection = (await readJson(`src/content/en/${slug}.json`)).toc[0].id;
    await page.setViewportSize({width: 1440, height: 1000});
    await page.goto(`${base}/${slug}?view=qa#${firstSection}`, {waitUntil: 'networkidle'});
    for (const locale of ['en', 'ja', 'es', 'de']) {
      if (locale !== 'en') {
        await page.locator('.language-switcher select').selectOption(locale);
        await page.waitForURL(`**/${locale}/${slug}?view=qa#${firstSection}`);
        await page.setViewportSize({width: 390, height: 844});
      }
      const meta = await readJson(`src/content/${locale}/${slug}.json`);
      await expect(page.locator('html')).toHaveAttribute('lang', locale);
      await expect(page.locator('h1')).toHaveText(meta.title);
      await expect(page.locator('.article-answer p')).toHaveText(meta.quickAnswer);
      await expect(page.locator('article.article-page')).toHaveAttribute('data-page-status', 'published');
      await expect(page.locator('.article-answer p')).toHaveText(meta.quickAnswer);
      assert.notEqual(meta.quickAnswer, meta.summary, `${locale}/${slug}: quick answer is a separate answer`);
      await expect(page.locator(`#${firstSection}`)).toBeVisible();
      const overflow = await page.evaluate(() => ({scroll: document.documentElement.scrollWidth, width: window.innerWidth}));
      assert.ok(overflow.scroll <= overflow.width + 1, `${locale}/${slug} overflow: ${JSON.stringify(overflow)}`);
      const prefix = locale === 'en' ? '' : `/${locale}`;
      for (const link of await page.locator('.article-body a[href^="/"]').all()) {
        const href = await link.getAttribute('href');
        if (href.startsWith('/media/')) {
          assert.ok((await readFile(new URL(`../public${href}`, import.meta.url))).length > 0, `${locale}/${slug}: downloadable diagram exists`);
          continue;
        }
        assert.ok(href.startsWith(`${prefix}/`) && !href.startsWith('/en/'), `${locale}/${slug} localized internal link: ${href}`);
      }
      for (const section of meta.toc) await expect(page.locator(`#${section.id}`)).toHaveCount(1);
      if (slug === 'tier-list') {
        const comparison = page.locator('.article-body table').nth(0);
        const priorities = page.locator('.article-body table').nth(1);
        await expect(comparison.locator('tbody tr')).toHaveCount(8);
        for (const width of [1440, 390]) {
          await page.setViewportSize({width, height: 844});
          const metrics = await priorities.evaluate((table) => {
            const cells = table.querySelectorAll('tbody tr:first-child td');
            return {firstColumn: cells[0].getBoundingClientRect().width, whiteSpace: getComputedStyle(cells[1]).whiteSpace, height: table.getBoundingClientRect().height};
          });
          assert.equal(metrics.whiteSpace, 'normal', `${locale}/${slug} ${width}px: activity guidance wraps`);
          assert.ok(metrics.firstColumn >= 90, `${locale}/${slug} ${width}px: readable priority column, ${JSON.stringify(metrics)}`);
          assert.ok(metrics.height < 900, `${locale}/${slug} ${width}px: activity table avoids excessive height, ${JSON.stringify(metrics)}`);
        }
        await page.setViewportSize({width: locale === 'en' ? 1440 : 390, height: locale === 'en' ? 1000 : 844});
      }
      if (slug === 'classes') {
        const iconRows = page.locator('[data-class-icon]');
        await expect(iconRows).toHaveCount(classIdentities.length);
        assert.deepEqual(await iconRows.evaluateAll((rows) => rows.map((row) => row.dataset.classIcon)), classIdentities.map(({id}) => id), `${locale}: all eight class icons`);
        for (const identity of classIdentities) {
          const row = page.locator(`[data-class-icon="${identity.id}"]`);
          const asset = guideAssets.find(({id}) => id === `emblem-${identity.id}`);
          await expect(row.locator('h3')).toHaveText(identity.names[locale]);
          if (locale !== 'en') await expect(row.locator('.class-english-name')).toHaveText(identity.names.en);
          await expect(row.locator('img')).toHaveAttribute('width', String(asset.width));
          await expect(row.locator('img')).toHaveAttribute('height', String(asset.height));
          const source = await row.locator('img').evaluate((image) => {
            const url = new URL(image.getAttribute('src'), location.origin);
            return url.searchParams.get('url') || url.pathname;
          });
          assert.equal(source, asset.src, `${locale}/${identity.id}: matching official emblem`);
          await expect(row.locator('button')).toHaveAttribute('aria-label', new RegExp(identity.names[locale]));
        }
        for (const classSlug of classIdentities.map(({id}) => id)) {
          await expect(page.locator(`.class-guide-card[data-class="${classSlug}"] a`)).toHaveAttribute('href', `${locale === 'en' ? '' : `/${locale}`}/${classSlug}`);
        }
        await expect(page.locator('h2#class-icons')).toHaveCount(0);
      }
      if (classIdentities.some(({id}) => id === slug)) {
        await expect(page.locator(`[data-skill-focus="${slug}"] tbody tr`)).toHaveCount(12);
        const groups = page.locator(`[data-skill-class="${slug}"] details`);
        await expect(groups).toHaveCount(3);
        await expect(groups.nth(0)).toHaveAttribute('open', '');
        await expect(groups.nth(1)).not.toHaveAttribute('open');
        await expect(groups.nth(2)).not.toHaveAttribute('open');
        for (const [index, count] of [12, 10, 13].entries()) {
          await expect(groups.nth(index).locator('tbody tr')).toHaveCount(count);
          if (index > 0) {
            await groups.nth(index).locator('summary').click();
            await expect(groups.nth(index).locator('tbody tr').first()).toBeVisible();
            await groups.nth(index).locator('summary').click();
            await expect(groups.nth(index).locator('tbody tr').first()).toBeHidden();
          }
        }
        if (slug === 'ranger' || slug === 'spiritmaster') await expect(page.locator('#solo-party-and-pvp')).toHaveCount(1);
        if (slug === 'chanter') await expect(page.locator('#party-role-switch')).toHaveCount(1);
      }
      await expect(page.locator('.guide-figure, .guide-diagram')).not.toHaveCount(0);
      for (const [id, visual] of Object.entries(meta.visuals)) await expect(page.locator(`[data-visual-id="${id}"] figcaption p`)).toHaveText(visual.caption);
      await expect(page.locator('.article-next-section .article-next-card')).toHaveCount(2);
      const nextTargets = await page.locator('.article-next-card').evaluateAll((cards) => cards.map((card) => card.dataset.nextGuide));
      assert.equal(new Set(nextTargets).size, nextTargets.length, `${locale}/${slug}: no duplicate next cards`);
      await expect(page.locator('#article-sources, #sources-title, .guide-asset-credit, .source-context')).toHaveCount(0);
      await expect(page.locator('.article-toc a[href="#article-sources"], .article-toc-mobile a[href="#article-sources"]')).toHaveCount(0);
      assert.ok(await page.evaluate(() => !!(document.querySelector('.article-next-section').compareDocumentPosition(document.querySelector('.article-related')) & Node.DOCUMENT_POSITION_FOLLOWING)), `${locale}/${slug}: next step before related guides`);
      if (locale !== 'en') assert.equal(await page.locator('.article-body').evaluate((element) => getComputedStyle(element).fontSize), '16px', `${locale}/${slug}: readable mobile body`);
    }
  }

  await page.setViewportSize({width: 390, height: 844});
  await page.goto(`${base}/guide`, {waitUntil: 'networkidle'});
  const contents = page.locator('.article-toc-mobile');
  await expect(contents).not.toHaveAttribute('open');
  await contents.locator('summary').click();
  await expect(contents).toHaveAttribute('open', '');
  await contents.locator('a[href="#main-story-first"]').click();
  await expect(contents).not.toHaveAttribute('open');
  await expect(page.locator('#main-story-first')).toBeVisible();
  const checklist = page.locator('[data-checklist="guide"]');
  await checklist.locator('input').first().check();
  await page.reload({waitUntil: 'networkidle'});
  await expect(page.locator('[data-checklist="guide"] input').first()).toBeChecked();
  await page.locator('.language-switcher select').selectOption('ja');
  await page.waitForURL('**/ja/guide**');
  await expect(page.locator('[data-checklist="guide"] input').first()).toBeChecked();
  await page.locator('.guide-checklist-heading button').click();
  await expect(page.locator('[data-checklist="guide"] input:checked')).toHaveCount(0);

  await page.goto(`${base}/classes`, {waitUntil: 'networkidle'});
  for (const width of [390, 1440]) {
    await page.setViewportSize({width, height: 844});
    const iconTrigger = page.locator('[data-class-icon="gladiator"] .guide-image-button');
    await iconTrigger.scrollIntoViewIfNeeded();
    await iconTrigger.focus();
    await page.keyboard.press('Enter');
    await expect(page.locator('.guide-image-dialog')).toBeVisible();
    const emblem = guideAssets.find(({id}) => id === 'emblem-gladiator');
    await expect(page.locator('.guide-image-dialog img')).toHaveAttribute('src', emblem.src);
    await expect(page.locator('.guide-image-dialog img')).toHaveJSProperty('complete', true);
    assert.deepEqual(await page.locator('.guide-image-dialog img').evaluate((image) => [image.naturalWidth, image.naturalHeight]), [emblem.width, emblem.height], `${width}px: original icon resolution`);
    await page.keyboard.press('Tab');
    assert.ok(await page.evaluate(() => !!document.activeElement?.closest('dialog')), `${width}px: icon dialog traps focus`);
    await page.keyboard.press('Escape');
    await expect(page.locator('.guide-image-dialog')).toHaveCount(0);
    await expect(iconTrigger).toBeFocused();
    assert.equal(await page.evaluate(() => document.body.style.overflow), '', `${width}px: icon dialog restores scrolling`);
  }
  await page.setViewportSize({width: 390, height: 844});
  await expect(page.locator('.class-guide-card')).toHaveCount(8);
  await page.locator('.class-finder button').filter({hasText: 'Healing & recovery'}).click();
  await expect(page.locator('.class-guide-card')).toHaveCount(1);
  await expect(page.locator('.class-guide-card')).toHaveAttribute('data-class', 'cleric');
  const imageTrigger = page.locator('.class-guide-card > .guide-image-button');
  await imageTrigger.click();
  await expect(page.locator('.guide-image-dialog')).toBeVisible();
  assert.equal(await page.evaluate(() => document.body.style.overflow), 'hidden');
  await page.keyboard.press('Shift+Tab');
  assert.ok(await page.evaluate(() => !!document.activeElement?.closest('dialog')), 'Image dialog traps focus');
  await page.keyboard.press('Escape');
  await expect(page.locator('.guide-image-dialog')).toHaveCount(0);
  await expect(imageTrigger).toBeFocused();
  assert.equal(await page.evaluate(() => document.body.style.overflow), '');
  await page.locator('.class-finder button').filter({hasText: 'Show all'}).click();
  await expect(page.locator('.class-guide-card')).toHaveCount(8);
  const compareRoleLink = page.locator('.class-guide-card[data-class="gladiator"] a');
  if (slugs.includes('gladiator')) {
    await expect(compareRoleLink).toHaveAttribute('href', '/gladiator');
    await compareRoleLink.click();
    await page.waitForURL('**/gladiator');
    await expect(page.locator('h1')).toHaveText((await readJson('src/content/en/gladiator.json')).title);
    await page.goto(`${base}/classes`, {waitUntil: 'networkidle'});
  }
  const templarRoleLink = page.locator('.class-guide-card[data-class="templar"] a');
  await expect(templarRoleLink).toHaveAttribute('href', '/templar');
  await templarRoleLink.click();
  await page.waitForURL('**/templar');
  await expect(page.locator('h1')).toHaveText((await readJson('src/content/en/templar.json')).title);

  await page.goto(`${base}/leveling`, {waitUntil: 'networkidle'});
  await page.locator('[data-guide-filter="faction"] select').selectOption('elyos');
  await expect(page.locator('[data-faction-section="elyos"]')).toBeVisible();
  await expect(page.locator('[data-faction-section="asmodians"]')).toBeHidden();
  await page.locator('.article-toc-mobile summary').click();
  await page.locator('.article-toc-mobile a[href="#asmodian-route"]').click();
  await expect(page.locator('[data-faction-section="asmodians"]')).toBeVisible();
  await expect(page.locator('[data-guide-filter="faction"] select')).toHaveValue('all');
  await expect(page.locator('.article-toc-mobile a[href="#asmodian-route"]')).toHaveAttribute('aria-current', 'location');
  await page.locator('[data-guide-filter="faction"] select').selectOption('elyos');
  await expect(page.locator('[data-faction-section="asmodians"]')).toBeHidden();
  await page.locator('.article-toc-mobile summary').click();
  await page.locator('.article-toc-mobile a[href="#asmodian-route"]').click();
  await expect(page.locator('[data-faction-section="asmodians"]')).toBeVisible();
  await expect(page.locator('.article-toc-mobile a[href="#asmodian-route"]')).toHaveAttribute('aria-current', 'location');
  await page.locator('.language-switcher select').selectOption('de');
  await page.waitForURL('**/de/leveling#asmodian-route');
  await expect(page.locator('#asmodian-route')).toBeVisible();

  await page.goto(`${base}/server`, {waitUntil: 'networkidle'});
  await page.locator('[data-guide-filter="region"] select').selectOption('naWest');
  await expect(page.locator('[data-region-section="naWest"]')).toBeVisible();
  await expect(page.locator('[data-region-section="eu"]')).toBeHidden();
  await expect(page.locator('[data-region-section="naWest"] tbody tr')).toHaveCount(2);
  await page.locator('[data-guide-filter="region"] select').selectOption('all');
  await expect(page.locator('[data-region-section="eu"]')).toBeVisible();
  await expect(page.locator('[data-region-section="eu"] tbody tr')).toHaveCount(9);
  await page.locator('[data-guide-filter="region"] select').selectOption('eu');
  await expect(page.locator('#other-region-pairings')).toBeHidden();
  await page.locator('.article-toc-mobile summary').click();
  await page.locator('.article-toc-mobile a[href="#other-region-pairings"]').click();
  await expect(page.locator('#other-region-pairings')).toBeVisible();
  await expect(page.locator('[data-guide-filter="region"] select')).toHaveValue('all');

  await page.goto(`${base}/map`, {waitUntil: 'networkidle'});
  await expect(page.locator('.guide-table-hint').first()).toBeVisible();
  const mapImage = page.locator('.guide-figure .guide-image-button').first();
  await mapImage.scrollIntoViewIfNeeded();
  await expect(mapImage.locator('img')).toHaveJSProperty('complete', true);
  assert.ok(await mapImage.locator('img').evaluate((image) => image.naturalWidth > 0), 'Real map screenshot loads');
  await mapImage.click();
  await expect(page.locator('.guide-image-dialog')).toBeVisible();
  await page.locator('.guide-image-close').click();
  await expect(mapImage).toBeFocused();

  for (const width of [320, 390, 1440]) for (const slug of ['guide', 'classes', 'leveling', 'map', 'server']) {
    await page.setViewportSize({width, height: width === 1440 ? 1000 : 844});
    await page.goto(`${base}/${slug}`, {waitUntil: 'networkidle'});
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    assert.ok(overflow <= 1, `${slug} ${width}px enriched layout overflow`);
  }

  const noStorage = await browser.newContext({viewport: {width: 390, height: 844}});
  await noStorage.addInitScript(() => {
    Storage.prototype.getItem = function () {throw new DOMException('QA blocked storage', 'SecurityError');};
    Storage.prototype.setItem = function () {throw new DOMException('QA blocked storage', 'SecurityError');};
  });
  const blockedPage = await noStorage.newPage();
  await blockedPage.goto(`${base}/download`, {waitUntil: 'networkidle'});
  await blockedPage.locator('[data-checklist="download"] input').first().check();
  await expect(blockedPage.locator('[data-checklist="download"] input').first()).toBeChecked();
  await blockedPage.locator('.guide-checklist-heading button').click();
  await expect(blockedPage.locator('[data-checklist="download"] input:checked')).toHaveCount(0);
  await noStorage.close();

  const readOnlyStorage = await browser.newContext({viewport: {width: 390, height: 844}});
  await readOnlyStorage.addInitScript(() => {
    Storage.prototype.setItem = function () {throw new DOMException('QA full storage', 'QuotaExceededError');};
  });
  const quotaPage = await readOnlyStorage.newPage();
  await quotaPage.goto(`${base}/guide`, {waitUntil: 'networkidle'});
  await quotaPage.locator('[data-checklist="guide"] input').first().check();
  await expect(quotaPage.locator('[data-checklist="guide"] input').first()).toBeChecked();
  await quotaPage.locator('.guide-checklist-heading button').click();
  await expect(quotaPage.locator('[data-checklist="guide"] input:checked')).toHaveCount(0);
  await readOnlyStorage.close();

  await page.goto(`${base}/code`, {waitUntil: 'networkidle'});
  await page.locator('.article-coupon .coupon-code-row button').click();
  await expect(page.locator('.article-coupon .coupon-code-row button')).toHaveAttribute('aria-label', 'Copied');
  assert.equal(await page.evaluate(() => navigator.clipboard.readText()), 'TAKEFLIGHTAION2');
  await page.clock.setSystemTime(new Date('2026-10-14T06:00:01Z'));
  await page.clock.runFor(30_000);
  await expect(page.locator('.article-coupon .coupon-state')).toHaveText('Expired');
  await page.clock.setSystemTime(new Date('2026-10-02T11:00:00Z'));

  for (const [locale, slug, width] of [['en', 'classes', 1440], ['ja', 'guide', 390], ['es', 'twitch-drops', 390], ['de', 'monetization', 390]]) {
    await page.setViewportSize({width, height: width === 1440 ? 1000 : 844});
    await page.goto(`${base}${locale === 'en' ? '' : `/${locale}`}/${slug}`, {waitUntil: 'networkidle'});
    await page.screenshot({path: fileURLToPath(new URL(`article-${locale}-${slug}-${width}.png`, output)), fullPage: true});
    await page.screenshot({path: fileURLToPath(new URL(`article-${locale}-${slug}-${width}-fold.png`, output))});
  }

  // Keep full-page image screenshots separate from the clock-driven interactions.
  const screenshotPage = await browser.newPage({reducedMotion: 'reduce'});
  screenshotPage.on('pageerror', (error) => failures.push(error.message));
  screenshotPage.on('console', (message) => {if (message.type() === 'error') failures.push(message.text());});
  screenshotPage.on('response', (response) => {if (response.status() >= 400 && response.url().startsWith(base)) failures.push(`${response.status()} ${response.url()}`);});
  for (const [name, width, height] of [['desktop', 1440, 1000], ['mobile', 390, 844]]) {
    await screenshotPage.setViewportSize({width, height});
    await screenshotPage.goto(base, {waitUntil: 'networkidle'});
    await screenshotPage.locator('.about-visual').scrollIntoViewIfNeeded();
    await expect(screenshotPage.locator('.about-visual img')).toBeVisible();
    await screenshotPage.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));
    await screenshotPage.evaluate(() => window.scrollTo(0, 0));
    await screenshotPage.screenshot({path: fileURLToPath(new URL(`home-${name}.png`, output)), fullPage: true});
    await screenshotPage.screenshot({path: fileURLToPath(new URL(`home-${name}-fold.png`, output))});
  }
  await screenshotPage.close();
  assert.deepEqual(failures, [], 'No runtime, console, or local network errors');
  console.log(`PASS: ${slugs.length * 4} enriched articles; responsive images, diagrams, class finder, checklist persistence/reset/blocked storage, faction/region filtering, zoom keyboard/focus, next steps and mobile contents; language query/hash, coupon behavior and no runtime errors.`);
} finally {
  await context.close();
  await browser.close();
}
