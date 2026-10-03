import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const origin = (process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000').replace(/\/$/, '');
const plan = JSON.parse(await readFile(new URL('../keywords-priority-20.json', import.meta.url), 'utf8'));
const source = JSON.parse(await readFile(new URL('../home.en.json', import.meta.url), 'utf8'));
const locales = ['en', 'ja', 'es', 'de'];
const slugs = plan.categories.flatMap((category) => category.keywords.map((keyword) => keyword.replace(/^aion 2 /, '').replaceAll(' ', '-')));
assert.equal(slugs.length, 20);
assert.equal(new Set(slugs).size, 20);
const path = (locale, slug = '') => `${locale === 'en' ? '' : `/${locale}`}${slug ? `/${slug}` : ''}` || '/';
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
  assert.ok(html.includes(`<html lang="${locale}"`), `${locale} html language`);
  const canonical = new URL(html.match(/<link rel="canonical" href="([^"]+)"/)?.[1] || 'http://invalid');
  assert.equal(canonical.origin, new URL(origin).origin, `${locale} canonical origin`);
  assert.equal(canonical.pathname, path(locale), `${locale} canonical path`);
  assert.equal((html.match(/<link[^>]*rel="alternate"/g) || []).length, 5, `${locale} language alternates`);
  assert.match(html, /<meta name="robots" content="index, follow"/);
  assert.equal((html.match(/<h1[ >]/g) || []).length, 1);
  assert.ok(!html.includes('暂无'), 'The placeholder is not a coupon');
  for (const slug of slugs) assert.ok(html.includes(`href="${path(locale, slug)}"`), `${locale}/${slug} navigation`);
  checks++;

  await Promise.all([...slugs, 'privacy-policy', 'terms-of-service'].map(async (slug) => {
    const {response, html} = await request(path(locale, slug));
    assert.equal(response.status, 200, `${locale}/${slug}`);
    const published = slugs.includes(slug);
    assert.match(html, published ? /<meta name="robots" content="index, follow"/ : /<meta name="robots" content="noindex, follow"/);
    assert.match(html, published ? /data-page-status="published"/ : /data-page-status="planned"/);
    if (published) {
      const metadata = JSON.parse(await readFile(new URL(`../src/content/${locale}/${slug}.json`, import.meta.url), 'utf8'));
      assert.equal((html.match(/<link[^>]*rel="alternate"/g) || []).length, 5, `${locale}/${slug} language alternates`);
      assert.ok(html.includes(`href="${origin}${path(locale, slug)}"`), `${locale}/${slug} self canonical`);
      assert.ok(html.includes('class="article-body"'), `${locale}/${slug} article content`);
      for (const section of metadata.toc) assert.ok(html.includes(`id="${section.id}"`), `${locale}/${slug} section ${section.id}`);
      assert.ok(html.includes('application/ld+json'), `${locale}/${slug} structured data`);
      assert.doesNotMatch(html, /<[^>]+class="[^"]*\bplaceholder-content\b/, `${locale}/${slug} no rendered placeholder`);
    }
    assert.ok(html.includes(`<html lang="${locale}"`));
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
assert.ok(rootWithPreference.includes('<html lang="en"'));
const {html: sitemap} = await request('/sitemap.xml');
assert.equal((sitemap.match(/<loc>/g) || []).length, 84);
for (const locale of locales) for (const slug of slugs) assert.ok(sitemap.includes(`${origin}${path(locale, slug)}</loc>`));
assert.ok(!sitemap.includes('privacy-policy') && !sitemap.includes('terms-of-service'));
const {html: robots} = await request('/robots.txt');
assert.ok(robots.includes(`Sitemap: ${origin}/sitemap.xml`));
for (const asset of ['/media/hero.jpg', '/media/atreia.jpg', '/favicon.ico', '/site.webmanifest']) {
  const response = await fetch(`${base}${asset}`, {method: 'HEAD'});
  assert.equal(response.status, 200, asset);
}
console.log(`PASS: ${checks} page checks; 80 published articles, legal placeholders, language alternates, redirects, 404s, 84 sitemap entries, robots and assets.`);
