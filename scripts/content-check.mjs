import assert from 'node:assert/strict';
import {readFile, readdir} from 'node:fs/promises';

const root = new URL('../', import.meta.url);
const read = (path) => readFile(new URL(path, root), 'utf8');
const json = async (path) => JSON.parse(await read(path));
const plan = await json('keywords-priority-20.json');
const keywords = plan.categories.flatMap(({keywords}) => keywords);
const slugs = keywords.map((keyword) => keyword.replace(/^aion 2 /, '').replaceAll(' ', '-'));
const locales = (process.env.CONTENT_LOCALES || 'en,ja,es,de').split(',');
assert.equal(locales[0], 'en', 'English is the reference locale');
const metadata = {};
const bodies = {};
const reserved = ['article-top', 'article-sources', 'sources-title', 'related-title'];
const assets = await json('src/content/guide-assets.json');
const assetIds = new Set(assets.map(({id}) => id));
assert.equal(assetIds.size, assets.length, 'Unique media asset IDs');
for (const asset of assets) {
  assert.match(asset.src, /^\/media\/guides\//, `${asset.id}: local media`);
  assert.ok(asset.width > 0 && asset.height > 0 && asset.checkedAt && asset.region && asset.version && asset.publisher, `${asset.id}: media provenance`);
  for (const field of ['sourceUrl', 'originalUrl']) assert.equal(new URL(asset[field]).protocol, 'https:', `${asset.id}: ${field}`);
  assert.ok((await readFile(new URL(`public${asset.src}`, root))).length > 0, `${asset.id}: media exists`);
  if (asset.desktopSrc) assert.ok((await readFile(new URL(`public${asset.desktopSrc}`, root))).length > 0, `${asset.id}: desktop media exists`);
}
let checks = 0;

assert.equal(slugs.length, 20);
assert.equal(new Set(slugs).size, 20);
for (const locale of locales) {
  const files = await readdir(new URL(`src/content/${locale}/`, root));
  assert.deepEqual(files.filter((file) => file.endsWith('.mdx')).sort(), slugs.map((slug) => `${slug}.mdx`).sort(), `${locale}: exact topic coverage`);
  metadata[locale] = {};
  bodies[locale] = {};
  for (const slug of slugs) {
    const label = `${locale}/${slug}`;
    const meta = await json(`src/content/${locale}/${slug}.json`);
    const body = await read(`src/content/${locale}/${slug}.mdx`);
    metadata[locale][slug] = meta;
    bodies[locale][slug] = body;
    for (const key of ['title', 'description', 'summary']) assert.ok(typeof meta[key] === 'string' && meta[key].trim().length > (key === 'title' ? 7 : 20), `${label}: ${key}`);
    assert.ok(Array.isArray(meta.toc) && meta.toc.length >= 4, `${label}: useful sections`);
    assert.ok(body.trim().length > (locale === 'ja' ? 900 : 1800), `${label}: substantive body`);
    assert.doesNotMatch(body, /(^#\s|<h1[\s>])/m, `${label}: H1 supplied by shell`);
    assert.doesNotMatch(JSON.stringify(meta) + body, /\bTODO\b|\bTBD\b|\?{3,}|\uFFFD/, `${label}: no placeholders or encoding damage`);
    if (['es', 'de'].includes(locale)) assert.doesNotMatch((JSON.stringify(meta) + body).replace(/https?:\/\/[^\s)"<]+/g, ''), /[A-Za-z]\?[A-Za-z]/, `${label}: no damaged accented words`);
    assert.doesNotMatch(JSON.stringify(meta), /Coming soon/, `${label}: published metadata`);
    if (locale !== 'ja') assert.doesNotMatch(JSON.stringify(meta) + body, /[\u3400-\u9fff]/, `${label}: no untranslated Chinese`);
    const headings = [...body.matchAll(/<h2\s+id="([a-z0-9-]+)"[^>]*>/g)].map((match) => match[1]);
    const ids = meta.toc.map((section) => section.id);
    assert.deepEqual(headings, ids, `${label}: table of contents matches headings`);
    assert.equal(new Set(ids).size, ids.length, `${label}: unique anchors`);
    for (const id of ids) assert.ok(!reserved.includes(id), `${label}: reserved anchor ${id}`);
    for (const section of meta.toc) assert.ok(section.title?.trim(), `${label}: translated section title`);
    assert.ok(meta.visuals && Object.keys(meta.visuals).length >= 1, `${label}: informative visuals`);
    const visualIds = [...body.matchAll(/<GuideVisual\s+id="([a-z0-9-]+)"\s*\/>/g)].map((match) => match[1]);
    assert.deepEqual(visualIds.toSorted(), Object.keys(meta.visuals).toSorted(), `${label}: every visual is used`);
    assert.equal(new Set(visualIds).size, visualIds.length, `${label}: unique visual placements`);
    for (const [id, visual] of Object.entries(meta.visuals)) {
      assert.ok(visual.caption?.trim().length > 10, `${label}/${id}: explanatory caption`);
      if (visual.assetId) {
        assert.ok(assetIds.has(visual.assetId), `${label}/${id}: known asset ${visual.assetId}`);
        assert.ok(visual.alt?.trim().length > 3, `${label}/${id}: localized alt text`);
      } else {
        assert.ok(visual.title?.trim(), `${label}/${id}: diagram title`);
        assert.ok(visual.steps?.length >= 3 || visual.rows?.length >= 3, `${label}/${id}: substantive diagram`);
        for (const step of visual.steps || []) assert.ok(step.label?.trim() && step.description?.trim(), `${label}/${id}: useful steps`);
      }
    }
    if (['guide', 'download'].includes(slug)) {
      assert.match(body, /<GuideChecklist\s*\/>/, `${label}: task checklist`);
      assert.ok(meta.checklist?.title && meta.checklist.items.length >= 6, `${label}: checklist content`);
      assert.equal(new Set(meta.checklist.items.map(({id}) => id)).size, meta.checklist.items.length, `${label}: stable checklist IDs`);
    }
    assert.match(body, /<GuideNext\s+slug="[a-z0-9-]+"\s*\/>/, `${label}: contextual next step`);
    assert.deepEqual(meta.inlineNext, [...body.matchAll(/<GuideNext\s+slug="([a-z0-9-]+)"\s*\/>/g)].map((match) => match[1]), `${label}: registered inline next steps`);
    for (const [, target] of body.matchAll(/<GuideNext\s+slug="([a-z0-9-]+)"\s*\/>/g)) assert.ok(slugs.includes(target) && target !== slug, `${label}: next guide ${target}`);
    if (slug === 'classes') assert.match(body, /<GuideClasses\s*\/>/);
    if (slug === 'leveling') for (const faction of ['elyos', 'asmodians']) assert.ok(body.includes(`<GuideFaction faction="${faction}">`), `${label}: faction group ${faction}`);
    if (slug === 'server') for (const region of ['eu', 'naWest', 'naEast', 'latam', 'asia']) assert.ok(body.includes(`<GuideRegion region="${region}">`), `${label}: region group ${region}`);
    for (const [, href] of body.matchAll(/\]\((\/[^\s)]*)\)/g)) {
      const url = new URL(href, 'http://content.local');
      const target = url.pathname.slice(1);
      assert.ok(slugs.includes(target), `${label}: known topic link ${href}`);
    }
    checks++;
  }
  for (const key of ['title', 'description']) assert.equal(new Set(slugs.map((slug) => metadata[locale][slug][key])).size, 20, `${locale}: unique page ${key}`);
  assert.equal(new Set(slugs.map((slug) => bodies[locale][slug].trim())).size, 20, `${locale}: distinct topic bodies`);
}

for (let i = 0; i < slugs.length; i++) {
  const slug = slugs[i];
  const data = await json(`src/content/article-data/${slug}.json`);
  assert.equal(data.slug, slug);
  assert.equal(data.keyword, keywords[i], `${slug}: original keyword`);
  assert.match(data.checkedAt, /^\d{4}-\d{2}-\d{2}$/);
  assert.ok(!Number.isNaN(Date.parse(data.checkedAt)), `${slug}: review date`);
  assert.ok(typeof data.revision === 'string' && data.revision.length > 0);
  assert.ok(data.regions.includes('Global'), `${slug}: Global coverage`);
  assert.ok(data.related.length >= 2, `${slug}: useful related topics`);
  for (const related of data.related) assert.ok(slugs.includes(related) && related !== slug, `${slug}: related ${related}`);
  assert.ok(data.sources.length >= 2, `${slug}: identifiable evidence`);
  assert.equal(new Set(data.sources.map((source) => source.id)).size, data.sources.length);
  for (const source of data.sources) {
    assert.ok(source.title && source.version && source.id, `${slug}: source description`);
    assert.ok(['official', 'player', 'community', 'tool'].includes(source.kind), `${slug}: source kind`);
    assert.ok(['Global', 'KR', 'TW', 'KR/TW', 'Mixed'].includes(source.region), `${slug}: source region`);
    assert.equal(new URL(source.url).protocol, 'https:');
    assert.ok(source.publishedAt === null || !Number.isNaN(Date.parse(source.publishedAt)), `${slug}: source publication date`);
  }
  const paragraphs = bodies.en[slug].split(/\r?\n\s*\r?\n/).filter((paragraph) => paragraph.length > 100 && !paragraph.startsWith('|') && !paragraph.startsWith('<'));
  for (const locale of locales.slice(1)) {
    assert.deepEqual(metadata[locale][slug].toc.map(({id}) => id), metadata.en[slug].toc.map(({id}) => id), `${locale}/${slug}: stable cross-language anchors`);
    assert.deepEqual(Object.keys(metadata[locale][slug].visuals).toSorted(), Object.keys(metadata.en[slug].visuals).toSorted(), `${locale}/${slug}: visual coverage`);
    for (const [id, visual] of Object.entries(metadata.en[slug].visuals)) {
      const translated = metadata[locale][slug].visuals[id];
      assert.equal(translated.assetId, visual.assetId, `${locale}/${slug}/${id}: shared image`);
      assert.equal(translated.steps?.length, visual.steps?.length, `${locale}/${slug}/${id}: complete diagram`);
      assert.deepEqual(translated.rows?.map(({values}) => values), visual.rows?.map(({values}) => values), `${locale}/${slug}/${id}: preserved comparison values`);
    }
    if (metadata.en[slug].checklist) assert.deepEqual(metadata[locale][slug].checklist.items.map(({id}) => id), metadata.en[slug].checklist.items.map(({id}) => id), `${locale}/${slug}: shared checklist progress`);
    const components = (body) => [...body.matchAll(/<Guide(?:Visual|Next|Faction|Region)\s+[^>]+>/g)].map(([tag]) => tag);
    assert.deepEqual(components(bodies[locale][slug]), components(bodies.en[slug]), `${locale}/${slug}: stable interactive and image placements`);
    assert.notEqual(bodies[locale][slug].trim(), bodies.en[slug].trim(), `${locale}/${slug}: translated body`);
    for (const paragraph of paragraphs) assert.ok(!bodies[locale][slug].includes(paragraph), `${locale}/${slug}: untranslated paragraph`);
    const links = (body) => [...body.matchAll(/\]\(([^\s)]+)\)/g)].map((match) => match[1]).sort();
    assert.deepEqual(links(bodies[locale][slug]), links(bodies.en[slug]), `${locale}/${slug}: same evidence and internal links`);
    const tableRows = (body) => body.split(/\r?\n/).filter((line) => line.trim().startsWith('|')).map((line) => line.split('|').length);
    assert.deepEqual(tableRows(bodies[locale][slug]), tableRows(bodies.en[slug]), `${locale}/${slug}: complete table rows and columns`);
    if (slug === 'tier-list') {
      const tiers = (body) => [...body.matchAll(/\|\s*(S\+|S|A\+|A|B|C|D)\s*\|\s*(S\+|S|A\+|A|B|C|D)\s*\|/g)].map((match) => [match[1], match[2]]);
      assert.equal(tiers(bodies.en[slug]).length, 8, 'Eight class ratings per author');
      assert.deepEqual(tiers(bodies[locale][slug]), tiers(bodies.en[slug]), `${locale}: preserved author tiers`);
    }
  }
}
console.log(`PASS: ${checks} enriched localized articles; ${assets.length} sourced assets; keywords, sources, visuals, checklists, anchors, evidence links, related topics and encoding.`);
