import 'server-only';
import rawItems from '@/content/game-data/items.json';
import rawMeta from '@/content/game-data/meta.json';
import events from '@/content/game-data/events.json';
import type {ApiResult, EventRecord, GameLocale, Item, MetaData, Region, SourceMeta} from './types';
import {DataError, validateItem} from './model';

type ItemRecord = {id: number; locales: Record<GameLocale, {item: Item; meta: {sourceUrl: string; fetchedAt: string; gameVersion: null}}>;
  regionChecks: Record<Region, Record<GameLocale, {valid: boolean; fetchedAt: string; sourceUrl: string}>>};
const items = rawItems as unknown as ItemRecord[];
export const curatedIds = items.map((record) => record.id);
export const gameEvents = events as EventRecord[];
export const officialLocales: Record<GameLocale, string> = {en: 'en-US', ja: 'ja-JP', es: 'es-ES', de: 'de-DE'};
export function snapshotItem(id: number, locale: GameLocale, region: Region = 'nae'): ApiResult<Item> {
  const record = items.find((entry) => entry.id === id);
  if (!record) throw new DataError('unknown-item', 404);
  const check = record.regionChecks[region]?.[locale];
  if (!check?.valid) throw new DataError('region-unavailable', 503);
  const data = record.locales[locale];
  return {data: validateItem(data.item, id), meta: {service: 'Global', region, locale, sourceUrl: check.sourceUrl,
    fetchedAt: check.fetchedAt, gameVersion: null, freshness: 'snapshot'}, error: null};
}
export function snapshotMeta(region: Region, locale: GameLocale): ApiResult<MetaData> {
  const record = rawMeta[region];
  const sources = [record.servers.meta, record.classes.meta, record.pcdata.meta];
  const meta: SourceMeta = {service: 'Global', region, locale, sourceUrl: sources[0].sourceUrl,
    fetchedAt: sources[0].fetchedAt, gameVersion: null, freshness: 'snapshot'};
  return {data: {servers: record.servers.data.serverList, classes: record.classes.data.classList.map((c) => ({id: c.id, name: c.text || c.name})), pcData: record.pcdata.data.pcDataList}, meta, error: null};
}
export function itemCards(locale: GameLocale, slug: string) {
  const selected = slug === 'cleric-build' ? [110730048, 110760001, 115030041, 210130038, 210530038, 310140035, 311030001]
    : slug === 'chanter' ? [110830047, 110860001, 115030040, 210130038, 210630038, 310340035, 311030001] : curatedIds;
  return selected.map((id) => snapshotItem(id, locale));
}
