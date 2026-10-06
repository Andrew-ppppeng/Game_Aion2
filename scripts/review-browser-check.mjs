import assert from 'node:assert/strict';
import {existsSync} from 'node:fs';
import {mkdir, writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium, expect} from '@playwright/test';
import {installGameFixtures, readQaJson} from './qa-fixtures.mjs';

const base = (process.env.QA_BASE_URL || 'http://127.0.0.1:3000').replace(/\/$/, '');
const output = new URL('../.qa/review/', import.meta.url);
await mkdir(output, {recursive: true});
const systemChrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_BROWSER_PATH || (existsSync(systemChrome) ? systemChrome : undefined)});
const context = await browser.newContext({viewport: {width: 390, height: 844}, reducedMotion: 'reduce'});
await context.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: base});
const fixtures = await installGameFixtures(context);
const page = await context.newPage();
const errors = [];
const checks = [];
const classGuides = ['cleric-build', 'chanter', 'ranger', 'gladiator', 'spiritmaster', 'templar', 'assassin', 'sorcerer', 'cleric'];
const feedbackPlaceholder = /has not been configured|No hay un contacto configurado|連絡先はまだ設定|noch nicht eingerichtet/i;
let failure = null;
page.on('pageerror', (error) => errors.push(error.message));
const url = (locale, path = '') => `${base}${locale === 'en' ? '' : `/${locale}`}${path ? `/${path}` : '/'}`;

async function fit(label) {
  const result = await page.evaluate(() => {
    const controls = [...document.querySelectorAll('main button, main input, main select, main textarea, .hero-buttons a, .language-switcher select, .mobile-menu-button')]
      .filter((element) => element.getClientRects().length && !element.closest('.mdx-table-wrap'))
      .map((element) => ({label: element.getAttribute('aria-label') || element.textContent?.trim().slice(0, 70) || element.tagName, left: element.getBoundingClientRect().left, right: element.getBoundingClientRect().right}));
    return {width: innerWidth, scrollWidth: document.documentElement.scrollWidth, controls};
  });
  assert.ok(result.scrollWidth <= result.width + 1, `${label}: document overflow ${result.scrollWidth - result.width}px`);
  for (const control of result.controls) assert.ok(control.left >= -1 && control.right <= result.width + 1, `${label}: control outside viewport: ${JSON.stringify(control)}`);
}

async function textZoom200() {
  // Text-only enlargement includes fixed px typography. Root font changes alone
  // would leave explicit px sizes untested.
  await page.evaluate(() => {
    const sizes = [...document.querySelectorAll('*')].filter((element) => element instanceof HTMLElement && !['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(element.tagName))
      .map((element) => [element, parseFloat(getComputedStyle(element).fontSize)]);
    for (const [element, size] of sizes) if (Number.isFinite(size)) element.style.fontSize = `${size * 2}px`;
    document.documentElement.dataset.qaTextZoom = '200';
  });
}

async function assertAnswer(locale, slug) {
  const meta = await readQaJson(`src/content/${locale}/${slug}.json`);
  await expect(page.locator('.article-answer p')).toHaveText(meta.quickAnswer);
  assert.notEqual(meta.quickAnswer, meta.summary, `${locale}/${slug}: independent quick answer`);
  await expect(page.locator('[data-article-author]')).toContainText('AION 2 Wiki');
  const articleSchema = await page.locator('article script[type="application/ld+json"]').evaluate((element) => JSON.parse(element.textContent)['@graph'].find((entry) => entry['@type'] === 'Article'));
  assert.equal(articleSchema.author?.['@type'], 'Organization');
  assert.equal(articleSchema.author?.name, 'AION 2 Wiki editorial team');
  if (classGuides.includes(slug)) await expect(page.locator('[data-article-edition]')).toHaveCount(0);
}

try {
  for (const locale of ['en', 'ja', 'es', 'de']) {
    const prefix = locale === 'en' ? '' : `/${locale}`;
    for (const width of [312, 390, 1440]) for (const textScale of [1, 2]) {
      await page.setViewportSize({width, height: width === 1440 ? 1000 : 844});
      for (const slug of ['', 'builds', 'cleric-build', 'chanter', 'twitch-drops', 'guide', 'monetization', 'tools/character']) {
        await page.goto(url(locale, slug), {waitUntil: 'networkidle'});
        await expect(page.locator('html')).toHaveAttribute('lang', locale);
        if (textScale === 2) await textZoom200();
        const label = `${locale}/${slug || 'home'} ${width}px ${textScale * 100}% text`;
        await fit(label);
        if (slug && slug !== 'tools/character') await assertAnswer(locale, slug);
        if (!slug) {
          for (const target of ['/tools/character', '/monetization#material-budget', '/guide#starter-checklist']) await expect(page.locator(`[data-return-tools] a[href="${prefix}${target}"]`)).toBeVisible();
          if (width < 1024) {
            await page.locator('.mobile-menu-button').click();
            await expect(page.locator('#mobile-navigation')).toBeVisible();
            await expect(page.locator(`#mobile-navigation a[href="${prefix}/tools/character"]`)).toBeVisible();
            await page.keyboard.press('Escape');
          }
        } else if (slug === 'guide') {
          const input = page.locator('#starter-checklist input').first();
          await input.check(); await expect(input).toBeChecked(); await input.uncheck();
        } else if (slug === 'tools/character') {
          await page.locator('[data-character-tool] input').first().fill('Testa');
          await page.locator('[data-character-tool] button[type="submit"]').click();
          await expect(page.locator('.character-match')).toHaveCount(1);
        }
        await fit(`${label} after interaction`);
        checks.push({locale, slug: slug || 'home', width, textScale});
      }
    }
    console.log(`${locale}: passed 48 page/viewport/text-size checks`);

    for (const slug of ['ranger', 'gladiator', 'spiritmaster']) {
      await page.goto(url(locale, slug), {waitUntil: 'networkidle'});
      await assertAnswer(locale, slug);
    }

    await page.setViewportSize({width: 1440, height: 1000});
    await page.goto(url(locale), {waitUntil: 'networkidle'});
    await page.locator(`.desktop-sidebar a[href="${prefix}/guide#starter-checklist"]`).click();
    await page.waitForURL(`**${prefix}/guide#starter-checklist`);
    await expect(page.locator('#starter-checklist')).toBeInViewport();
    await page.locator(`.desktop-sidebar a[href="${prefix}/monetization#material-budget"]`).click();
    await page.waitForURL(`**${prefix}/monetization#material-budget`);
    await expect(page.locator('#material-budget')).toBeInViewport();
    for (const legal of ['privacy-policy', 'terms-of-service']) {
      await page.goto(url(locale, legal), {waitUntil: 'networkidle'});
      await expect(page.locator('article')).toHaveAttribute('data-page-status', 'site-info');
      assert.doesNotMatch(await page.locator('body').innerText(), feedbackPlaceholder, `${locale}/${legal}: no public contact placeholder`);
      const contact = page.locator('#corrections').locator('..').locator('a[data-feedback-contact]');
      await expect(contact).toHaveCount(1);
      await expect(contact).toHaveAttribute('href', 'mailto:feedback@aion2wiki.space');
      await expect(contact).toContainText('feedback@aion2wiki.space');
      const template = page.locator('.feedback-template textarea');
      await expect(template).toHaveAttribute('readonly', '');
      assert.ok((await template.inputValue()).length > 40);
      await page.locator('.feedback-template button').click();
      await expect(page.locator('.feedback-template [role="status"]')).not.toHaveText('');
      await fit(`${locale}/${legal}`);
    }
  }

  await page.goto(`${base}/twitch-drops`, {waitUntil: 'networkidle'});
  await expect(page.locator('#war-for-atreia')).toHaveText('War For Atreia creator rewards');
  const timerScope = await page.locator('[data-event-timers]').evaluate((element) => {
    let sibling = element.previousElementSibling;
    while (sibling && sibling.tagName !== 'H2') sibling = sibling.previousElementSibling;
    return sibling?.id;
  });
  assert.equal(timerScope, 'war-for-atreia', 'Timer belongs to the creator-only campaign');
  await expect(page.locator('[data-event="war-for-atreia-2-20261007"]')).toHaveAttribute('data-event-status', 'unconfirmed');
  await expect(page.locator('[data-event="war-for-atreia-3-20261012"]')).toHaveAttribute('data-event-status', 'unconfirmed');
  assert.match(await page.locator('.article-body').textContent(), /participating War For Atreia creator/);
  await expect(page.locator('#advanced-access-rewards')).toBeVisible();
  await expect(page.locator('#launch-rewards')).toBeVisible();

  const equipmentStart = fixtures.fulfilled.length;
  await page.goto(`${base}/cleric-build`, {waitUntil: 'networkidle'});
  const equipment = page.locator('[data-equipment-cards]');
  await expect(equipment.locator('[data-item-id]')).toHaveCount(2);
  assert.equal(fixtures.fulfilled.slice(equipmentStart).filter(({url}) => url.includes('/equipment-examples')).length, 0);
  await equipment.locator('[data-more-equipment] > summary').click();
  await expect(equipment.locator('[data-item-id]')).toHaveCount(7);
  await equipment.locator('[data-more-equipment] > summary').click();
  await equipment.locator('[data-more-equipment] > summary').click();
  assert.equal(fixtures.fulfilled.slice(equipmentStart).filter(({url}) => url.includes('/equipment-examples')).length, 1, 'Additional cards fetched only once per mounted guide');

  // APIRequestContext bypasses the browser fixture: this endpoint uses archived
  // local cards and must preserve locale/provenance without a live game request.
  for (const locale of ['en', 'ja', 'es', 'de']) {
    const response = await context.request.get(`${base}/api/aion2/equipment-examples?locale=${locale}&slug=builds`);
    assert.equal(response.status(), 200);
    assert.match(response.headers()['x-robots-tag'], /noindex/);
    const {items} = await response.json();
    assert.equal(items.length, 20);
    assert.ok(items.every(({data, meta}) => data && meta.locale === locale && meta.freshness === 'snapshot'));
  }
  const invalidEquipment = await context.request.get(`${base}/api/aion2/equipment-examples?locale=fr&slug=steam`);
  assert.equal(invalidEquipment.status(), 400);

  const ordinary = await browser.newContext({viewport: {width: 390, height: 844}});
  await installGameFixtures(ordinary);
  const ordinaryPage = await ordinary.newPage();
  const scripts = [];
  ordinaryPage.on('response', (response) => {if (response.request().resourceType() === 'script') scripts.push(response.text());});
  await ordinaryPage.goto(`${base}/steam`, {waitUntil: 'networkidle'});
  const scriptText = (await Promise.all(scripts)).join('\n');
  // Shared analytics legitimately references these DOM selectors. A rendered
  // JSX prop key identifies the widget implementation rather than its selector.
  for (const marker of ['data-character-tool', 'data-budget-planner', 'data-event-timers', 'data-more-equipment', 'data-class-icon']) {
    const implementation = new RegExp(`["']${marker}["']\\s*:`);
    assert.ok(!implementation.test(scriptText), `/steam does not load unused ${marker} implementation`);
  }
  for (const [slug, marker] of [['tools/character', 'data-character-tool'], ['monetization', 'data-budget-planner'], ['twitch-drops', 'data-event-timers'], ['cleric-build', 'data-more-equipment'], ['classes', 'data-class-icon']]) {
    scripts.length = 0;
    await ordinaryPage.goto(`${base}/${slug}`, {waitUntil: 'networkidle'});
    assert.ok(new RegExp(`["']${marker}["']\\s*:`).test((await Promise.all(scripts)).join('\n')), `${slug}: loaded widget signature is recognized`);
  }
  await ordinary.close();

  await page.setViewportSize({width: 390, height: 844});
  await page.goto(`${base}/builds`, {waitUntil: 'networkidle'});
  await textZoom200();
  await page.screenshot({path: fileURLToPath(new URL('builds-390-text200.png', output)), fullPage: true});
  assert.deepEqual(errors, [], 'No review runtime errors');
  console.log(`PASS: ${checks.length} four-language layout checks at 312/390/1440px and 100/200% text; usable controls, tool anchors, author/quick answers, regional limits, legal information, campaign scope and deferred equipment/JS.`);
} catch (error) {
  failure = error instanceof Error ? error.message : String(error);
  await page.screenshot({path: fileURLToPath(new URL('failure.png', output)), fullPage: true}).catch(() => {});
  throw error;
} finally {
  await writeFile(new URL('results.json', output), `${JSON.stringify({baseUrl: base, measuredAtUtc: new Date().toISOString(), chrome: browser.version(), checks, errors, failure, passed: failure === null}, null, 2)}\n`);
  await context.close();
  await browser.close();
}
