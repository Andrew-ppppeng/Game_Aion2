import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';

export const readQaJson = async (path) => JSON.parse(await readFile(new URL(`../${path}`, import.meta.url), 'utf8'));

// Keep layout checks independent of transient CDN connections while retaining
// the exact official icons, dimensions and original image URLs.
export async function installItemIconFixtures(context) {
  const manifest = await readQaJson('tests/fixtures/item-icons/sources.json');
  for (const entry of manifest) {
    const body = await readFile(new URL(`../tests/fixtures/item-icons/${entry.file}`, import.meta.url));
    await context.route(entry.sourceUrl, (route) => route.fulfill({status: 200, contentType: 'image/png', body}));
  }
}

// Browser checks use archived public responses and never query NC's live API.
export async function installGameFixtures(context) {
  const [metadata, items, character] = await Promise.all([
    readQaJson('src/content/game-data/meta.json'), readQaJson('src/content/game-data/items.json'), readQaJson('tests/fixtures/cleric.json'),
  ]);
  const profile = character.character.data.info.profile;
  const fulfilled = [];
  await context.route('**/api/aion2/**', async (route) => {
    const url = new URL(route.request().url());
    const locale = url.searchParams.get('locale') || 'en';
    const region = url.searchParams.get('region') || 'nae';
    let body;
    if (url.pathname.endsWith('/meta')) {
      const record = metadata[region];
      body = {data: {servers: record.servers.data.serverList, classes: record.classes.data.classList.map((entry) => ({id: entry.id, name: entry.text || entry.name})), pcData: record.pcdata.data.pcDataList}, meta: null, error: null};
    } else if (url.pathname.endsWith('/equipment-examples')) {
      const slug = url.searchParams.get('slug');
      const ids = slug === 'cleric-build' ? [110730048, 110760001, 115030041, 210130038, 210530038, 310140035, 311030001]
        : slug === 'chanter' ? [110830047, 110860001, 115030040, 210130038, 210630038, 310340035, 311030001] : items.map(({id}) => id);
      body = {items: ids.slice(2).map((id) => {
        const record = items.find((entry) => entry.id === id);
        const data = record.locales[locale];
        return {data: data.item, meta: {...data.meta, service: 'Global', locale, region: 'nae', freshness: 'snapshot'}, error: null};
      })};
    } else if (url.pathname.endsWith('/search')) {
      body = {data: {list: [{characterId: profile.characterId, name: profile.characterName, level: profile.characterLevel, pcId: profile.pcId, race: profile.raceId, serverId: profile.serverId, serverName: profile.serverName, region}], pagination: {page: 1, size: 20, total: 1, endPage: 1}}, meta: character.character.meta, error: null};
    } else if (url.pathname.includes('/characters/')) {
      body = locale === 'en' ? character.character : (await readQaJson(`tests/fixtures/cleric-${locale}.json`)).character;
    } else {
      assert.fail(`Unexpected game request in review check: ${url.pathname}`);
    }
    const serialized = JSON.stringify(body);
    fulfilled.push({url: url.href, bytes: Buffer.byteLength(serialized)});
    await route.fulfill({status: 200, contentType: 'application/json', body: serialized});
  });
  return {fulfilled, profile};
}
