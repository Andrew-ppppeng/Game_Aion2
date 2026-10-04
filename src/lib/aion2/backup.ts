import {validWorkspace, type Workspace} from './workspace.ts';
export const toolKeys = ['aion2-characters-v1', 'aion2-budget-v1', 'aion2-region-v1', 'aion2-timezone-v1', 'aion2-event-reminders-v1', 'aion2-checklist-v1:guide'] as const;
export type ToolKey = typeof toolKeys[number];
export type Backup = {format: 'aion2-backup'; version: 1; workspace: Workspace; tools: Partial<Record<ToolKey, unknown>>};
const record = (v: unknown): v is Record<string, unknown> => !!v && typeof v === 'object' && !Array.isArray(v);
const string = (v: unknown, max = 160) => typeof v === 'string' && v.length <= max && !/[\u0000-\u001f]/.test(v);
export function validToolValue(key: ToolKey, v: unknown): boolean {
  if (key === 'aion2-region-v1') return typeof v === 'string' && ['nae','naw','eu','la','as'].includes(v);
  if (key === 'aion2-timezone-v1') return typeof v === 'string' && ['local','UTC','America/New_York','America/Los_Angeles','Europe/Berlin','America/Sao_Paulo','Asia/Tokyo','Asia/Shanghai'].includes(v);
  if (key === 'aion2-event-reminders-v1' || key === 'aion2-checklist-v1:guide') return Array.isArray(v) && v.length <= 200 && v.every((i) => string(i, 100));
  if (key === 'aion2-characters-v1') return Array.isArray(v) && v.length <= 30 && v.every((b) => record(b) && string(b.id) && string(b.name, 80) && validToolValue('aion2-region-v1', b.region) && Number.isSafeInteger(b.serverId) && Number(b.serverId) > 0);
  return record(v) && ['craft','enhance'].includes(String(v.mode)) && ['goal','yield','fee'].every((k) => string(v[k], 40)) && Array.isArray(v.rows) && v.rows.length > 0 && v.rows.length <= 20 && v.rows.every((r) => record(r) && string(r.name) && ['quantity','owned','price'].every((k) => string(r[k], 40)));
}
export function parseBackup(v: unknown): Backup {
  if (validWorkspace(v)) return {format: 'aion2-backup', version: 1, workspace: v, tools: {}};
  if (!record(v) || v.format !== 'aion2-backup' || v.version !== 1 || !validWorkspace(v.workspace) || !record(v.tools) || Object.entries(v.tools).some(([key, value]) => !toolKeys.includes(key as ToolKey) || !validToolValue(key as ToolKey, value))) throw new Error('invalid-import');
  return v as Backup;
}
