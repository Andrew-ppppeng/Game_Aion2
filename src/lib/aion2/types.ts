export const regions = ['nae', 'naw', 'eu', 'la', 'as'] as const;
export type Region = (typeof regions)[number];
export type GameLocale = 'en' | 'ja' | 'es' | 'de';
export type Freshness = 'fresh' | 'cached' | 'snapshot' | 'stale' | 'unavailable';
export type SourceMeta = {
  service: 'Global'; region: Region; locale: GameLocale; sourceUrl: string;
  fetchedAt: string; gameVersion: string | null; freshness: Freshness;
};
export type ApiResult<T> = {data: T | null; meta: SourceMeta | null; error: {code: string; retryAfter?: number} | null};
export type RawStat = {id: string; name: string; minValue?: string; value: string; extra?: string; exceed?: boolean};
export type Item = {
  id: number; name: string; grade: string; gradeName?: string; icon?: string; level?: number;
  equipLevel: number; enchantLevel: number; maxEnchantLevel?: number; maxExceedEnchantLevel?: number;
  classNames?: string[]; categoryName?: string; raceName?: string; mainStats: RawStat[]; subStats?: RawStat[];
  subStatCount?: number; subStatRandom?: boolean; magicStoneSlotCount?: number; godStoneSlotCount?: number;
  sources?: string[]; tradable?: boolean; storable?: boolean; decomposable?: boolean;
};
export type EquippedItem = {id: number; name: string; grade: string; icon?: string; slotPos: number; slotPosName: string; enchantLevel: number; exceedLevel?: number};
export type CharacterMatch = {characterId: string; name: string; level: number; pcId: number; race: number; serverId: number; serverName: string; region: Region};
export type SearchData = {list: CharacterMatch[]; pagination: {page: number; size: number; total: number; endPage: number}};
export type CharacterInfo = {
  profile: {characterId: string; characterName: string; characterLevel: number; className: string; pcId?: number; combatPower: number; serverId: number; serverName: string; raceName: string; regionName?: string};
  stat?: {statList: {type: string; name: string; value: number; statSecondList?: string[] | null}[]};
  title?: {ownedCount: number; totalCount: number; titleList: {name: string | null; equipCategory: string; equipStatList?: {desc: string}[] | null}[]};
  daevanion?: {boardList: {id: number; name: string; openNodeCount: number; totalNodeCount: number}[]};
};
export type Skill = {id: number; name: string; level?: number; skillLevel?: number; skillType?: string; category?: string; acquired?: number; equip?: number};
export type EquipmentData = {equipment: {equipmentList: EquippedItem[]}; skill?: {skillList: Skill[]}; petwing?: {pet?: {name?: string | null; level?: number | null} | null; wing?: {name?: string | null; grade?: string | null} | null}};
export type CharacterData = {info: CharacterInfo; equipment: EquipmentData; sources: SourceMeta[]};
export type MetaData = {servers: {raceId: number; serverId: number; serverName: string; serverShortName?: string}[]; classes: {id: number; name: string}[]; pcData: {id: number; className: string; classText: string; raceName: string; genderName: string}[]};
export type EventRecord = {id: string; topics: string[]; titles: Record<GameLocale, string>; startAt: string | null; endAt: string | null; sourceTime: string; sourceUrl: string; checkedAt: string; gameVersion: null; dateRange?: string; completedAt?: string; deadlineOnly?: boolean};
