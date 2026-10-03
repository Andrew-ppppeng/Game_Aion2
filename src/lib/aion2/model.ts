import type {CharacterInfo, EquipmentData, EventRecord, Item, RawStat, Region, SearchData} from './types.ts';

export class DataError extends Error {
  code: string; status: number; retryAfter?: number;
  constructor(code: string, status = 502, retryAfter?: number) {super(code); this.code = code; this.status = status; this.retryAfter = retryAfter;}
}
export function readRegion(value: string | null): Region {
  if (value === null) return 'nae';
  if (!['nae', 'naw', 'eu', 'la', 'as'].includes(value)) throw new DataError('invalid-region', 400);
  return value as Region;
}
export function positiveInteger(value: string | null, max = 2_147_483_647): number {
  if (!value || !/^\d+$/.test(value)) throw new DataError('invalid-input', 400);
  const number = Number(value);
  if (!Number.isSafeInteger(number) || number < 1 || number > max) throw new DataError('invalid-input', 400);
  return number;
}
export function characterId(value: string): string {
  // URLSearchParams already decoded an incoming URL. Search responses may retain %3D.
  let decoded = value;
  try {decoded = decodeURIComponent(value);} catch {throw new DataError('invalid-input', 400);}
  if (!/^[A-Za-z0-9_-]{20,100}={0,2}$/.test(decoded)) throw new DataError('invalid-input', 400);
  return decoded;
}
export function plainName(value: string): string {
  return value.replace(/<[^>]*>/g, '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
}
export function validateItem(value: unknown, expectedId: number): Item {
  if (!value || typeof value !== 'object') throw new DataError('invalid-data');
  const item = value as Item;
  if (item.id !== expectedId || typeof item.name !== 'string' || !item.name || !Array.isArray(item.mainStats) || !item.mainStats.length) throw new DataError('invalid-item', 404);
  const stats = [...item.mainStats, ...(Array.isArray(item.subStats) ? item.subStats : [])];
  if (stats.some((stat) => !stat || !stat.id || typeof stat.name !== 'string' || typeof stat.value !== 'string' || (stat.extra !== undefined && typeof stat.extra !== 'string') || (stat.minValue !== undefined && typeof stat.minValue !== 'string')) ||
    !Number.isInteger(item.enchantLevel) || !Number.isInteger(item.equipLevel) || item.enchantLevel < 0 || item.equipLevel < 0 || typeof item.grade !== 'string' ||
    [item.classNames, item.sources].some((list) => list !== undefined && (!Array.isArray(list) || list.some((v) => typeof v !== 'string'))) ||
    (item.subStats !== undefined && !Array.isArray(item.subStats))) throw new DataError('invalid-data');
  return item;
}
export function validateSearch(value: unknown): SearchData {
  const data = value as SearchData | null;
  if (!data || !Array.isArray(data.list) || data.list.length > 20 || !data.pagination ||
    ![data.pagination.page, data.pagination.size, data.pagination.total, data.pagination.endPage].every((n) => Number.isInteger(n) && n >= 0)) throw new DataError('invalid-data');
  return {...data, list: data.list.map((entry) => {
    if (!entry || typeof entry.name !== 'string' || typeof entry.serverName !== 'string' || !Number.isInteger(entry.serverId) || !Number.isInteger(entry.level) || !Number.isInteger(entry.pcId)) throw new DataError('invalid-data');
    return {...entry, characterId: characterId(entry.characterId), name: plainName(entry.name)};
  })};
}
export function validateCharacterInfo(value: unknown, cid: string, serverId: number): CharacterInfo {
  const data = value as CharacterInfo | null;
  const p = data?.profile;
  if (!p || typeof p.characterName !== 'string' || !p.characterName || p.serverId !== serverId || typeof p.characterId !== 'string' || characterId(p.characterId) !== cid) throw new DataError('character-unavailable', 404);
  if (![p.className, p.serverName, p.raceName].every((v) => typeof v === 'string') || ![p.characterLevel, p.combatPower].every((v) => typeof v === 'number' && Number.isFinite(v)) || (p.regionName !== undefined && p.regionName !== null && typeof p.regionName !== 'string')) throw new DataError('invalid-data');
  if (data?.stat && (!Array.isArray(data.stat.statList) || data.stat.statList.some((s) => !s || typeof s.name !== 'string' || typeof s.type !== 'string' || typeof s.value !== 'number' || (s.statSecondList != null && (!Array.isArray(s.statSecondList) || s.statSecondList.some((t) => typeof t !== 'string')))))) throw new DataError('invalid-data');
  if (data?.daevanion && (!Array.isArray(data.daevanion.boardList) || data.daevanion.boardList.some((b) => !b || typeof b.name !== 'string' || ![b.openNodeCount, b.totalNodeCount].every(Number.isInteger)))) throw new DataError('invalid-data');
  if (data?.title && (!Array.isArray(data.title.titleList) || ![data.title.ownedCount, data.title.totalCount].every(Number.isInteger) || data.title.titleList.some((t) => !t || (t.name !== null && typeof t.name !== 'string') || (t.equipStatList != null && (!Array.isArray(t.equipStatList) || t.equipStatList.some((s) => !s || typeof s.desc !== 'string')))))) throw new DataError('invalid-data');
  return data!;
}
export function validateEquipment(value: unknown): EquipmentData {
  const data = value as EquipmentData | null;
  if (!data || !Array.isArray(data.equipment?.equipmentList) || data.equipment.equipmentList.some((i) => !i || ![i.id, i.slotPos, i.enchantLevel].every(Number.isInteger) || typeof i.name !== 'string' || typeof i.grade !== 'string' || typeof i.slotPosName !== 'string')) throw new DataError('invalid-data');
  if (data.skill && (!Array.isArray(data.skill.skillList) || data.skill.skillList.some((s) => !s || typeof s.name !== 'string' || !Number.isInteger(s.id) || (s.category != null && typeof s.category !== 'string')))) throw new DataError('invalid-data');
  if (data.petwing && [data.petwing.pet, data.petwing.wing].some((v) => v && v.name != null && typeof v.name !== 'string')) throw new DataError('invalid-data');
  return data;
}
export function statNumber(value: string | undefined): {value: number; unit: 'points' | 'percent'} | null {
  if (value === undefined || !/^-?\d+(?:\.\d+)?%?$/.test(value)) return null;
  const number = Number(value.replace('%', ''));
  if (!Number.isFinite(number)) return null;
  return {value: number, unit: value.endsWith('%') ? 'percent' : 'points'};
}
export function formatStat(stat: RawStat): string {
  const base = stat.minValue && stat.minValue !== stat.value ? `${stat.minValue}–${stat.value}` : stat.value;
  if (stat.exceed) return stat.extra || base;
  return stat.extra && !/^0(?:\.0+)?%?$/.test(stat.extra) ? `${base} (+${stat.extra})` : base;
}
export function compareStats(current: Item, candidate: Item): {id: string; name: string; min: number; max: number; unit: string}[] {
  // Compare fixed template main stats only. Random pools and breakthrough behavior are excluded.
  return candidate.mainStats.flatMap((next) => {
    const prev = current.mainStats.find((stat) => stat.id === next.id);
    if (!prev || next.exceed || prev.exceed) return [];
    const a = statNumber(prev.value), b = statNumber(next.value);
    const aMin = statNumber(prev.minValue ?? prev.value), bMin = statNumber(next.minValue ?? next.value);
    const aExtra = statNumber(prev.extra ?? '0'), bExtra = statNumber(next.extra ?? '0');
    if (!a || !b || !aMin || !bMin || !aExtra || !bExtra || a.unit !== b.unit || aMin.unit !== a.unit || bMin.unit !== b.unit) return [];
    if ((aExtra.value !== 0 && aExtra.unit !== a.unit) || (bExtra.value !== 0 && bExtra.unit !== b.unit)) return [];
    return [{id: next.id, name: next.name, min: bMin.value + bExtra.value - aMin.value - aExtra.value,
      max: b.value + bExtra.value - a.value - aExtra.value, unit: b.unit}];
  });
}
export function eventStatus(event: EventRecord, now: number): 'upcoming' | 'ongoing' | 'ended' | 'unconfirmed' {
  if (event.completedAt && now >= Date.parse(event.completedAt)) return 'ended';
  if (event.deadlineOnly && event.endAt && Number.isFinite(Date.parse(event.endAt))) return now >= Date.parse(event.endAt) ? 'ended' : 'upcoming';
  if (!event.startAt || !event.endAt || !Number.isFinite(Date.parse(event.startAt)) || !Number.isFinite(Date.parse(event.endAt)) || Date.parse(event.endAt) <= Date.parse(event.startAt)) return 'unconfirmed';
  if (now >= Date.parse(event.endAt)) return 'ended';
  return now < Date.parse(event.startAt) ? 'upcoming' : 'ongoing';
}
export function calendarFile(event: EventRecord, title: string): string | null {
  if ((!event.startAt && !event.deadlineOnly) || !event.endAt || !Number.isFinite(Date.parse(event.endAt)) || (event.startAt && (!Number.isFinite(Date.parse(event.startAt)) || Date.parse(event.endAt) <= Date.parse(event.startAt)))) return null;
  const date = (value: string) => value.replace(/[-:]/g, '').replace(/\.\d{3}/, '');
  const escape = (value: string) => value.replace(/\\/g, '\\\\').replace(/\r?\n/g, '\\n').replace(/[,;]/g, (v) => `\\${v}`);
  return ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//AION2 Wiki//Event Calendar//EN', 'BEGIN:VEVENT',
    `UID:${event.id}@aion2-wiki`, `DTSTAMP:${date(event.checkedAt + 'T00:00:00Z')}`, `DTSTART:${date(event.startAt || event.endAt)}`,
    ...(event.deadlineOnly ? [] : [`DTEND:${date(event.endAt)}`]), `SUMMARY:${escape(title)}`, `URL:${event.sourceUrl}`, 'END:VEVENT', 'END:VCALENDAR', ''].join('\r\n');
}
export type MaterialInput = {quantity: number; owned: number; price: number};
export function budget(goal: number, yieldPerAttempt: number, fee: number, materials: MaterialInput[]) {
  if (![goal, yieldPerAttempt, fee, ...materials.flatMap((m) => [m.quantity, m.owned, m.price])].every(Number.isFinite) || goal <= 0 || yieldPerAttempt <= 0 || fee < 0 || materials.some((m) => m.quantity < 0 || m.owned < 0 || m.price < 0)) throw new DataError('invalid-input', 400);
  const attempts = Math.ceil(goal / yieldPerAttempt);
  const rows = materials.map((m) => ({required: m.quantity * attempts, missing: Math.max(0, m.quantity * attempts - m.owned), cost: Math.max(0, m.quantity * attempts - m.owned) * m.price}));
  const total = rows.reduce((sum, row) => sum + row.cost, attempts * fee);
  if (![goal, yieldPerAttempt, ...materials.flatMap((m) => [m.quantity, m.owned])].every(Number.isSafeInteger) || !Number.isSafeInteger(attempts) || !Number.isFinite(total) || total > Number.MAX_SAFE_INTEGER || rows.some((r) => !Number.isSafeInteger(r.required))) throw new DataError('invalid-input', 400);
  return {attempts, rows, total};
}
