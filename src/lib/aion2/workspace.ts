import type {Region} from './types';

export const workspaceKey = 'aion2-workspace-v1';
export type ItemRef = {id: number; region: Region};
export type Goal = ItemRef & {done: boolean};
export type Build = {id: string; name: string; region: Region; items: {slot: string; itemId: number; enchantLevel: number}[]};
export type Snapshot = {key: string; name: string; region: Region; serverId: number; characterId: string; capturedAt: string;
  power: number; stats: {id: string; name: string; value: number}[]; equipment: {id: number; slot: number; level: number}[]};
export type Workspace = {version: 1; favorites: ItemRef[]; recent: ItemRef[]; goals: Goal[];
  builds: Build[]; tasks: {id: string; text: string; done: boolean}[]; snapshots: Snapshot[]};
export const emptyWorkspace: Workspace = {version: 1, favorites: [], recent: [], goals: [], builds: [], tasks: [], snapshots: []};
const object = (v: unknown): v is Record<string, unknown> => !!v && typeof v === 'object' && !Array.isArray(v);
const text = (v: unknown, max = 160): v is string => typeof v === 'string' && v.length > 0 && v.length <= max && !/[\u0000-\u001f]/.test(v);
const integer = (v: unknown, max = Number.MAX_SAFE_INTEGER): v is number => Number.isSafeInteger(v) && Number(v) >= 0 && Number(v) <= max;
const region = (v: unknown): v is Region => typeof v === 'string' && ['nae', 'naw', 'eu', 'la', 'as'].includes(v);
export const refKey = (v: ItemRef) => `${v.region}:${v.id}`;
const ref = (v: unknown): v is ItemRef => object(v) && integer(v.id) && Number(v.id) > 0 && region(v.region);
const list = (v: unknown, max: number, check: (entry: unknown) => boolean) => Array.isArray(v) && v.length <= max && v.every(check);
export function validBuild(v: unknown): v is Build {
  return object(v) && Object.keys(v).every((k) => ['id','name','region','items'].includes(k)) && text(v.id, 80) && text(v.name, 80) && region(v.region) && list(v.items, 30, (i) => object(i) && Object.keys(i).every((k) => ['slot','itemId','enchantLevel'].includes(k)) && text(i.slot, 80) && integer(i.itemId) && Number(i.itemId) > 0 && integer(i.enchantLevel, 30)) &&
    new Set((v.items as Build['items']).map((i) => i.slot)).size === (v.items as Build['items']).length;
}
export function validWorkspace(v: unknown): v is Workspace {
  return object(v) && v.version === 1 && list(v.favorites, 200, ref) && list(v.recent, 30, ref) &&
    list(v.goals, 100, (g) => ref(g) && typeof (g as Goal).done === 'boolean') && list(v.builds, 30, validBuild) &&
    list(v.tasks, 100, (t) => object(t) && text(t.id, 80) && text(t.text) && typeof t.done === 'boolean') &&
    list(v.snapshots, 40, (s) => object(s) && text(s.key, 200) && text(s.name, 80) && region(s.region) && integer(s.serverId) && text(s.characterId, 160) &&
      text(s.capturedAt, 40) && Number.isFinite(Date.parse(String(s.capturedAt))) && typeof s.power === 'number' && Number.isFinite(s.power) && s.power >= 0 &&
      list(s.stats, 100, (a) => object(a) && text(a.id, 80) && text(a.name) && typeof a.value === 'number' && Number.isFinite(a.value)) &&
      list(s.equipment, 40, (i) => object(i) && integer(i.id) && integer(i.slot, 100) && integer(i.level, 30)));
}
function unique<T>(values: T[], key: (v: T) => string, max: number) {return [...new Map(values.map((v) => [key(v), v])).values()].slice(0, max);}
export function mergeWorkspace(current: Workspace, incoming: unknown): Workspace {
  if (!validWorkspace(incoming)) throw new Error('invalid-import');
  return {version: 1, favorites: unique([...incoming.favorites, ...current.favorites], refKey, 200),
    recent: unique([...current.recent, ...incoming.recent], refKey, 30), goals: unique([...incoming.goals, ...current.goals], refKey, 100),
    builds: unique([...incoming.builds, ...current.builds], (v) => v.id, 30), tasks: unique([...incoming.tasks, ...current.tasks], (v) => v.id, 100),
    snapshots: unique([...incoming.snapshots, ...current.snapshots], (v) => v.key, 40)};
}
export function withRecent(current: Workspace, item: ItemRef): Workspace {return {...current, recent: [item, ...current.recent.filter((i) => refKey(i) !== refKey(item))].slice(0, 30)};}
export function encodeBuild(build: Build): string {
  if (!validBuild(build)) throw new Error('invalid-plan');
  return btoa(String.fromCharCode(...new TextEncoder().encode(JSON.stringify(build)))).replaceAll('+', '-').replaceAll('/', '_').replaceAll('=', '');
}
export function decodeBuild(value: string): Build {
  if (!/^[a-zA-Z0-9_-]{1,12000}$/.test(value)) throw new Error('invalid-plan');
  const raw: unknown = JSON.parse(new TextDecoder('utf-8', {fatal: true}).decode(Uint8Array.from(atob(value.replaceAll('-', '+').replaceAll('_', '/')), (c) => c.charCodeAt(0))));
  if (!validBuild(raw)) throw new Error('invalid-plan');
  return raw;
}
