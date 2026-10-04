import 'server-only';
import {createHash} from 'node:crypto';
import {cached, limited} from './cache';
import {curatedIds, officialLocales, snapshotItem, snapshotMeta} from './data';
import {characterId, DataError, positiveInteger, readRegion, validateCharacterInfo, validateEquipment, validateItem, validateSearch} from './model';
import type {ApiResult, CharacterData, CharacterInfo, EquipmentData, GameLocale, Item, MetaData, Region, SearchData, SourceMeta} from './types';

type Context = {region: Region; locale: GameLocale; lang: string};
export function context(params: URLSearchParams): Context {
  const value = params.get('locale') ?? 'en';
  if (!['en', 'ja', 'es', 'de'].includes(value)) throw new DataError('invalid-input', 400);
  const locale = value as GameLocale;
  return {region: readRegion(params.get('region')), locale, lang: officialLocales[locale]};
}
function url(path: string, ctx: Context, query: Record<string, string | number>, search = false) {
  const origin = search ? 'https://api-search.plaync.com' : 'https://aion2.plaync.com';
  return `${origin}${path}?${new URLSearchParams({...Object.fromEntries(Object.entries(query).map(([k, v]) => [k, String(v)])), region: ctx.region, ...(search ? {localeInfo: ctx.lang} : {lang: ctx.lang})})}`;
}
async function upstream<T>(sourceUrl: string, ctx: Context): Promise<ApiResult<T>> {
  const started = Date.now();
  return limited(async () => {
    try {
      const response = await fetch(sourceUrl, {headers: {Accept: 'application/json'}, cache: 'no-store', signal: AbortSignal.timeout(8000), redirect: 'error'});
      if (response.status === 429 || response.status === 403) throw new DataError('upstream-refused', 503, Math.min(3600, Math.max(60, Number(response.headers.get('Retry-After')) || 60)));
      if (!response.ok) throw new DataError('upstream-unavailable', 502);
      if (!response.headers.get('content-type')?.includes('application/json')) throw new DataError('invalid-data', 502);
      let data: T;
      try {data = await response.json();} catch {throw new DataError('invalid-data', 502);}
      const meta: SourceMeta = {service: 'Global', region: ctx.region, locale: ctx.locale, sourceUrl,
        fetchedAt: new Date().toISOString(), gameVersion: null, freshness: 'fresh'};
      console.info(JSON.stringify({module: 'aion2', outcome: 'success', durationMs: Date.now() - started}));
      return {data, meta, error: null};
    } catch (error) {
      const known = error instanceof DataError ? error : new DataError('upstream-unavailable', 502);
      console.info(JSON.stringify({module: 'aion2', outcome: known.code, durationMs: Date.now() - started}));
      throw known;
    }
  });
}
const key = (value: string) => createHash('sha256').update(value).digest('hex');
const minutes = (n: number) => n * 60_000;

export async function getMeta(params: URLSearchParams): Promise<ApiResult<MetaData>> {
  const ctx = context(params);
  try {
    return await cached(`metadata:${ctx.region}`, minutes(1440), minutes(20160), async () => {
      const sources: SourceMeta[] = [];
      const english = {...ctx, locale: 'en' as const, lang: 'en-US'};
      const servers = await upstream<{serverList: MetaData['servers']}>(url('/en-us/api/gameinfo/servers', english, {}), english); sources.push(servers.meta!);
      const classes = await upstream<{classList: {id: number; name: string; text?: string}[]}>(url('/en-us/api/gameinfo/classes', english, {}), english);
      const pcs = await upstream<{pcDataList: MetaData['pcData']}>(url('/en-us/api/gameinfo/pcdata', english, {}), english);
      if (!Array.isArray(servers.data?.serverList) || !servers.data.serverList.length || servers.data.serverList.some((s) => !Number.isInteger(s.serverId) || typeof s.serverName !== 'string') ||
        !Array.isArray(classes.data?.classList) || classes.data.classList.length !== 8 || classes.data.classList.some((c) => !c || !Number.isInteger(c.id) || typeof c.name !== 'string' || (c.text != null && typeof c.text !== 'string')) ||
        !Array.isArray(pcs.data?.pcDataList) || !pcs.data.pcDataList.length || pcs.data.pcDataList.some((p) => !p || !Number.isInteger(p.id) || typeof p.className !== 'string' || typeof p.classText !== 'string')) throw new DataError('invalid-data');
      return {data: {servers: servers.data.serverList, classes: classes.data.classList.map((c) => ({id: c.id, name: c.text || c.name})), pcData: pcs.data.pcDataList}, meta: sources[0], error: null};
    });
  } catch (error) {
    return {...snapshotMeta(ctx.region, ctx.locale), error: {code: error instanceof DataError ? error.code : 'upstream-unavailable'}};
  }
}
export async function searchCharacters(params: URLSearchParams): Promise<ApiResult<SearchData>> {
  const ctx = context(params);
  const query = (params.get('q') ?? '').trim();
  if (!query || [...query].length > 64 || /[\u0000-\u001f]/.test(query)) throw new DataError('invalid-input', 400);
  const page = positiveInteger(params.get('page') ?? '1', 500);
  const input: Record<string, string | number> = {keyword: query, page, size: 20};
  const meta = (await getMeta(params)).data!;
  if (params.get('serverId')) {
    const server = positiveInteger(params.get('serverId'));
    if (!meta.servers.some((s) => s.serverId === server)) throw new DataError('invalid-input', 400);
    input.serverId = server;
  }
  if (params.get('class')) {
    const pcs = meta.pcData.filter((p) => p.className === params.get('class') || p.classText === params.get('class'));
    if (!pcs.length) throw new DataError('invalid-input', 400);
    input.pcId = pcs.map((p) => p.id).join(',');
  }
  const source = url('/aion2global/search/v2/character', ctx, input, true);
  return cached(key(source), minutes(1), 0, async () => {
    const result = await upstream<SearchData>(source, ctx);
    return {...result, data: validateSearch(result.data)};
  });
}
export async function getCharacter(id: string, params: URLSearchParams): Promise<ApiResult<CharacterData>> {
  const ctx = context(params);
  const cid = characterId(id);
  const serverId = positiveInteger(params.get('serverId'));
  if (!(await getMeta(params)).data!.servers.some((s) => s.serverId === serverId)) throw new DataError('invalid-input', 400);
  const identity = {characterId: cid, serverId};
  return cached(key(JSON.stringify({cid, serverId, ...ctx})), minutes(15), minutes(45), async () => {
    const info = await upstream<CharacterInfo>(url('/api/character/info', ctx, identity), ctx);
    const profile = validateCharacterInfo(info.data, cid, serverId);
    const equipment = await upstream<EquipmentData>(url('/api/character/equipment', ctx, identity), ctx);
    return {data: {info: profile, equipment: validateEquipment(equipment.data), sources: [info.meta!, equipment.meta!]}, meta: info.meta, error: null};
  });
}
export async function getEquipped(id: string, slot: string, params: URLSearchParams): Promise<ApiResult<Item>> {
  const ctx = context(params);
  const slotPos = positiveInteger(slot, 100);
  const result = await getCharacter(id, params);
  const equipped = result.data!.equipment.equipment.equipmentList.find((i) => i.slotPos === slotPos);
  if (!equipped) throw new DataError('unknown-item', 404);
  const source = url('/api/character/equipment/item', ctx, {characterId: characterId(id), serverId: positiveInteger(params.get('serverId')),
    id: equipped.id, enchantLevel: equipped.enchantLevel, slotPos});
  return cached(key(source), minutes(15), minutes(45), async () => {
    const value = await upstream<Item>(source, ctx);
    return {...value, data: validateItem(value.data, equipped.id)};
  });
}
export async function getItem(id: string, params: URLSearchParams): Promise<ApiResult<Item>> {
  const ctx = context(params);
  const itemId = positiveInteger(id);
  let allowed = curatedIds.includes(itemId);
  if (!allowed && params.get('characterId') && params.get('serverId')) {
    const character = await getCharacter(params.get('characterId')!, params);
    allowed = character.data!.equipment.equipment.equipmentList.some((i) => i.id === itemId);
  }
  if (!allowed) throw new DataError('unknown-item', 404);
  const enhancement = params.get('enchantLevel') ?? '0';
  if (!/^\d+$/.test(enhancement) || Number(enhancement) > 30) throw new DataError('invalid-input', 400);
  const snapshot = curatedIds.includes(itemId) ? snapshotItem(itemId, ctx.locale, ctx.region) : null;
  if (snapshot && Number(enhancement) > (snapshot.data!.maxEnchantLevel ?? 0)) throw new DataError('invalid-input', 400);
  const source = url(`/${ctx.lang.toLowerCase()}/api/gameconst/item`, ctx, {id: itemId, enchantLevel: enhancement});
  try {
    return await cached(key(source), minutes(1440), minutes(1440), async () => {
      const result = await upstream<Item>(source, ctx);
      const item = validateItem(result.data, itemId);
      if (item.enchantLevel !== Number(enhancement)) throw new DataError('invalid-data');
      return {...result, data: item};
    });
  } catch (error) {
    if (snapshot && enhancement === '0' && !(error instanceof DataError && error.status === 400)) return {
      ...snapshot, meta: {...snapshot.meta!, freshness: 'snapshot'}, error: {code: error instanceof DataError ? error.code : 'upstream-unavailable'},
    };
    throw error;
  }
}
