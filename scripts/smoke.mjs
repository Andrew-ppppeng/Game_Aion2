import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const origin = (process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000').replace(/\/$/, '');
const plan = JSON.parse(await readFile(new URL('../content-topics.json', import.meta.url), 'utf8'));
const source = JSON.parse(await readFile(new URL('../home.en.json', import.meta.url), 'utf8'));
const locales = ['en', 'ja', 'es', 'de'];
const slugs = plan.categories.flatMap((category) => category.keywords.map((keyword) => keyword.replace(/^aion 2 /, '').replaceAll(' ', '-')));
assert.ok(slugs.length > 0, 'Published topics must not be empty');
assert.equal(new Set(slugs).size, slugs.length, 'Unique published topic slugs');
const existingTopics = ['guide', 'gathering', 'leveling', 'classes', 'chanter', 'tier-list', 'gladiator', 'ranger', 'spiritmaster', 'races', 'map', 'code', 'character-creation', 'presets', 'pvp', 'spacetime-rift', 'builds', 'cleric-build', 'macro-guide', 'twitch-drops', 'server', 'maintenance', 'server-transfer', 'steam', 'download', 'monetization', 'notmeter', 'player-count'];
for (const slug of existingTopics) assert.ok(slugs.includes(slug), `Existing topic retained: ${slug}`);
const path = (locale, slug = '') => `${locale === 'en' ? '' : `/${locale}`}${slug ? `/${slug}` : ''}` || '/';
const feedbackPlaceholder = /has not been configured|No hay un contacto configurado|連絡先はまだ設定|noch nicht eingerichtet/i;
let checks = 0;

async function request(pathname, options) {
  const response = await fetch(`${base}${pathname}`, {signal: AbortSignal.timeout(15_000), ...options});
  return {response, html: await response.text()};
}

function sameShape(reference, translation, prefix = '') {
  if (typeof reference === 'string') {assert.equal(typeof translation, 'string', prefix); return;}
  assert.deepEqual(Object.keys(translation).sort(), Object.keys(reference).sort(), prefix);
  for (const key of Object.keys(reference)) sameShape(reference[key], translation[key], `${prefix}.${key}`);
}

const englishUi = JSON.parse(await readFile(new URL('../src/messages/en.json', import.meta.url), 'utf8'));
for (const locale of locales) {
  const translated = JSON.parse(await readFile(new URL(`../src/messages/${locale}.json`, import.meta.url), 'utf8'));
  const m = {...source, ...translated};
  for (const key of ['ui', 'categories', 'topics']) sameShape(englishUi[key], translated[key], `${locale}.${key}`);
  sameShape(source.home, m.home, `${locale}.home`);
  sameShape(source.footer, m.footer, `${locale}.footer`);
  sameShape(source.metadata, m.metadata, `${locale}.metadata`);
  const {response, html} = await request(path(locale));
  assert.equal(response.status, 200, `${locale} homepage`);
  assert.match(html, new RegExp(`<html\\b[^>]*\\blang="${locale}"`), `${locale} html language`);
  const canonical = new URL(html.match(/<link rel="canonical" href="([^"]+)"/)?.[1] || 'http://invalid');
  assert.equal(canonical.origin, new URL(origin).origin, `${locale} canonical origin`);
  assert.equal(canonical.pathname, path(locale), `${locale} canonical path`);
  assert.equal((html.match(/<link[^>]*rel="alternate"/g) || []).length, 5, `${locale} language alternates`);
  assert.match(html, /<meta name="robots" content="index, follow"/);
  assert.equal((html.match(/<h1[ >]/g) || []).length, 1);
  assert.ok(!html.includes('暂无'), 'The placeholder is not a coupon');
  for (const slug of slugs) assert.ok(html.includes(`href="${path(locale, slug)}"`), `${locale}/${slug} navigation`);
  for (const slug of ['tools/character', 'monetization#material-budget', 'guide#starter-checklist']) assert.ok(html.includes(`href="${path(locale, slug)}"`), `${locale}/${slug} tool navigation`);
  assert.doesNotMatch(html, /class="(?:sidebar-status|coupon-details)"/, `${locale}: removed sidebar text`);
  checks++;

  await Promise.all([...slugs, 'privacy-policy', 'terms-of-service'].map(async (slug) => {
    const {response, html} = await request(path(locale, slug));
    assert.equal(response.status, 200, `${locale}/${slug}`);
    const published = slugs.includes(slug);
    assert.match(html, published ? /<meta name="robots" content="index, follow"/ : /<meta name="robots" content="noindex, follow"/);
    assert.match(html, published ? /data-page-status="published"/ : /data-page-status="site-info"/);
    if (published) {
      const metadata = JSON.parse(await readFile(new URL(`../src/content/${locale}/${slug}.json`, import.meta.url), 'utf8'));
      assert.equal((html.match(/<link[^>]*rel="alternate"/g) || []).length, 5, `${locale}/${slug} language alternates`);
      assert.ok(html.includes(`href="${origin}${path(locale, slug)}"`), `${locale}/${slug} self canonical`);
      assert.ok(html.includes('class="article-body"'), `${locale}/${slug} article content`);
      assert.ok(metadata.quickAnswer && metadata.quickAnswer !== metadata.summary, `${locale}/${slug} independent quick answer`);
      for (const section of metadata.toc) assert.ok(html.includes(`id="${section.id}"`), `${locale}/${slug} section ${section.id}`);
      assert.ok(html.includes('application/ld+json'), `${locale}/${slug} structured data`);
      assert.doesNotMatch(html, /<[^>]+class="[^"]*\bplaceholder-content\b/, `${locale}/${slug} no rendered placeholder`);
    } else {
      const required = slug === 'privacy-policy' ? ['local-data', 'usage-statistics', 'privacy-controls', 'requests-and-services', 'external-services', 'corrections'] : ['editorial-policy', 'maintenance-policy', 'terms-of-use', 'corrections'];
      for (const section of required) assert.ok(html.includes(`id="${section}"`), `${locale}/${slug}: complete site information ${section}`);
      assert.doesNotMatch(html, /class="[^"]*placeholder-content/, `${locale}/${slug}: no placeholder page`);
      const contacts = [...html.matchAll(/<a\b(?=[^>]*\bdata-feedback-contact(?:[=\s>]))[^>]*>([\s\S]*?)<\/a>/g)];
      assert.equal(contacts.length, 1, `${locale}/${slug}: one feedback contact`);
      assert.equal(contacts[0][0].match(/\bhref="([^"]+)"/)?.[1], 'mailto:feedback@aion2wiki.space', `${locale}/${slug}: real feedback email target`);
      assert.ok(contacts[0][1].replace(/<[^>]+>/g, '').includes('feedback@aion2wiki.space'), `${locale}/${slug}: feedback email visible`);
      const publicText = html.replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '').replace(/<style\b[^>]*>[\s\S]*?<\/style>/gi, '').replace(/<[^>]+>/g, '');
      assert.doesNotMatch(publicText, feedbackPlaceholder, `${locale}/${slug}: no public contact placeholder`);
    }
    assert.doesNotMatch(html, /id="(?:article-sources|sources-title)"|class="(?:guide-asset-credit|source-context)"|href="#article-sources"/, `${locale}/${slug} research provenance stays internal`);
    assert.match(html, new RegExp(`<html\\b[^>]*\\blang="${locale}"`));
    assert.equal((html.match(/<h1[ >]/g) || []).length, 1);
    checks++;
  }));

  for (const slug of ['does-not-exist', 'missing/nested-page']) {
    const {response} = await request(path(locale, slug));
    assert.equal(response.status, 404, `${locale} unknown route: ${slug}`);
    checks++;
  }
}

const {response: englishRedirect} = await request('/en', {redirect: 'manual'});
assert.ok([307, 308].includes(englishRedirect.status));
assert.equal(new URL(englishRedirect.headers.get('location'), base).pathname, '/');
const {html: rootWithPreference} = await request('/', {headers: {'Accept-Language': 'ja', Cookie: 'NEXT_LOCALE=de'}});
assert.match(rootWithPreference, /<html\b[^>]*\blang="en"/);
const {html: sitemap} = await request('/sitemap.xml');
const sitemapEntries = locales.length * (slugs.length + 3);
assert.equal((sitemap.match(/<loc>/g) || []).length, sitemapEntries);
for (const locale of locales) assert.ok(sitemap.includes(`${origin}${path(locale, 'tools/character')}</loc>`));
for (const locale of locales) for (const slug of slugs) assert.ok(sitemap.includes(`${origin}${path(locale, slug)}</loc>`));
assert.ok(!sitemap.includes('privacy-policy') && !sitemap.includes('terms-of-service'));
const {html: robots} = await request('/robots.txt');
assert.ok(robots.includes(`Sitemap: ${origin}/sitemap.xml`));
for (const asset of ['/media/hero.jpg', '/media/atreia.jpg', '/favicon.ico', '/site.webmanifest']) {
  const response = await fetch(`${base}${asset}`, {method: 'HEAD'});
  assert.equal(response.status, 200, asset);
}
console.log(`PASS: ${checks} page checks; ${locales.length * slugs.length} published articles, complete site information, tool navigation, language alternates, redirects, 404s, ${sitemapEntries} sitemap entries, robots and assets.`);
