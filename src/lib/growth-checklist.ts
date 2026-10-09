export const growthStorageKey = 'aion2-growth-checklist-v1';
export const starterStorageKey = 'aion2-checklist-v1:guide';
export const growthRevision = 1;
export const starterGoalLinks = {
  'official-client': '/download',
  'coordinate-server': '/server',
  'choose-class': '/classes',
  'check-controls': '/settings',
  'follow-story': '/guide#main-story-first',
  'upgrade-skills': '/builds#find-a-starting-build',
} as const;
export const growthGoals = [
  {id: 'campaign-route', stage: 1, href: '/leveling'},
  {id: 'skill-options', stage: 1, href: '/builds#check-region-and-progression'},
  {id: 'manual-loop', stage: 1, href: '/builds#three-concrete-examples'},
  {id: 'starting-rewards', stage: 2, href: '/gear-progression#fresh-level-45'},
  {id: 'daevanion-points', stage: 2, href: '/gear-progression#fresh-level-45'},
  {id: 'equipment-upgrade', stage: 2, href: '/gear-progression#growth-and-enhancement'},
] as const;
export type GrowthGoal = {id: string; stage: number; label: string; condition: string; href: string};
export type GrowthProgress = {schemaVersion: 1; templateRevision: number; completedIds: string[]};
export const emptyGrowth: GrowthProgress = {schemaVersion: 1, templateRevision: growthRevision, completedIds: []};

export function isGrowthProgress(value: unknown): value is GrowthProgress {
  if (!value || typeof value !== 'object') return false;
  const progress = value as GrowthProgress;
  return progress.schemaVersion === 1 && Number.isSafeInteger(progress.templateRevision) && progress.templateRevision > 0 && Array.isArray(progress.completedIds)
    && progress.completedIds.length <= 200 && progress.completedIds.every((id) => typeof id === 'string' && id.length <= 100);
}

export function decodeGrowth(raw: string | null, starterRaw: string | null, starterIds: readonly string[]): GrowthProgress {
  try {
    const parsed: unknown = JSON.parse(raw || 'null');
    if (isGrowthProgress(parsed)) return parsed;
  } catch { /* Invalid local data is replaced by a usable initial state. */ }
  try {
    const selected: unknown = JSON.parse(starterRaw || 'null');
    if (Array.isArray(selected)) return {...emptyGrowth, completedIds: [...new Set(selected.filter((id): id is string => typeof id === 'string' && starterIds.includes(id)))]};
  } catch { /* The starter list is optional. */ }
  return emptyGrowth;
}

export function completedGrowth(progress: GrowthProgress, ids: readonly string[]): Set<string> {
  return new Set(progress.completedIds.filter((id) => ids.includes(id)));
}

export function toggleGrowth(progress: GrowthProgress, id: string, complete: boolean): GrowthProgress {
  // Keep retired IDs so template updates never erase an earlier completion.
  const selected = new Set(progress.completedIds);
  if (complete) selected.add(id); else selected.delete(id);
  return {schemaVersion: 1, templateRevision: growthRevision, completedIds: [...selected]};
}
