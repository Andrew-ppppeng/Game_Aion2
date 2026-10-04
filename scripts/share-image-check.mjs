import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {mkdir, writeFile} from 'node:fs/promises';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:3000';
const locales = ['en', 'ja', 'es', 'de'];
const hashes = new Set();
await mkdir(new URL('../.qa/', import.meta.url), {recursive: true});
let checked = 0;
for (const locale of locales) {
  for (const slug of ['guide', 'chanter', 'twitch-drops', 'character', 'player-count']) {
    const response = await fetch(`${base}/api/share/${locale}/${slug}`, {signal: AbortSignal.timeout(30_000)});
    assert.equal(response.status, 200, `${locale}/${slug}: available image`);
    assert.match(response.headers.get('content-type') || '', /image\/png/, `${locale}/${slug}: PNG type`);
    const png = Buffer.from(await response.arrayBuffer());
    assert.deepEqual([...png.subarray(0, 8)], [137, 80, 78, 71, 13, 10, 26, 10], `${locale}/${slug}: PNG signature`);
    assert.equal(png.readUInt32BE(16), 1200, `${locale}/${slug}: card width`);
    assert.equal(png.readUInt32BE(20), 630, `${locale}/${slug}: card height`);
    const hash = createHash('sha256').update(png).digest('hex');
    assert.ok(!hashes.has(hash), `${locale}/${slug}: locale/topic card must be distinct`);
    hashes.add(hash);
    if (slug === 'guide' && ['en', 'ja'].includes(locale)) await writeFile(new URL(`../.qa/share-${locale}.png`, import.meta.url), png);
    if (slug === 'player-count' && locale === 'ja') await writeFile(new URL('../.qa/share-ja-player-count.png', import.meta.url), png);
    if (slug === 'chanter' && locale === 'en') await writeFile(new URL('../.qa/share-en-chanter.png', import.meta.url), png);
    checked++;
  }
  const prefix = locale === 'en' ? '' : `/${locale}`;
  const html = await (await fetch(`${base}${prefix}/guide`, {signal: AbortSignal.timeout(15_000)})).text();
  assert.match(html, new RegExp(`/api/share/${locale}/guide\\?v=`), `${locale}: metadata uses versioned localized card`);
}
for (const target of ['fr/guide', 'en/not-an-article', 'en/privacy-policy']) {
  const response = await fetch(`${base}/api/share/${target}`, {signal: AbortSignal.timeout(15_000)});
  assert.equal(response.status, 404, `${target}: unsupported image rejected`);
}
console.log(`PASS: ${checked} distinct localized PNG cards, versioned article metadata and invalid-route 404s.`);
