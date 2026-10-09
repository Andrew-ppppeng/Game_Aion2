'use client';

import {useCallback, useMemo, useSyncExternalStore} from 'react';
import {decodeGrowth, growthStorageKey, starterStorageKey, isGrowthProgress, type GrowthProgress} from '@/lib/growth-checklist';

let memory: string | null = null;
let storageFailed = false;
function subscribe(callback: () => void) {
  const storage = (event: StorageEvent) => {
    if (!event.key || event.key === growthStorageKey) {memory = null; storageFailed = false;}
    callback();
  };
  window.addEventListener('storage', storage);
  window.addEventListener('aion2-tool-storage', callback);
  window.addEventListener('aion-checklist', callback);
  window.addEventListener('aion2-growth-initialized', callback);
  return () => {window.removeEventListener('storage', storage); window.removeEventListener('aion2-tool-storage', callback); window.removeEventListener('aion-checklist', callback); window.removeEventListener('aion2-growth-initialized', callback);};
}
function read(key: string) {try {return localStorage.getItem(key);} catch {return null;}}
function snapshot() {
  return JSON.stringify([storageFailed ? memory : read(growthStorageKey) ?? memory, read(starterStorageKey)]);
}
export function useGrowthProgress(starterIds: readonly string[]) {
  const value = useSyncExternalStore(subscribe, snapshot, () => '[null,null]');
  const progress = useMemo(() => {
    const [growth, starter] = JSON.parse(value) as [string | null, string | null];
    return decodeGrowth(growth, starter, starterIds);
  }, [value, starterIds]);
  function save(next: GrowthProgress) {
    memory = JSON.stringify(next);
    try {localStorage.setItem(growthStorageKey, memory); storageFailed = false;} catch {storageFailed = true;}
    window.dispatchEvent(new CustomEvent('aion2-tool-storage', {detail: {key: growthStorageKey}}));
  }
  // Initialization saves an inherited plan once; it is not a player save event.
  const initialize = useCallback(() => {
    try {if (isGrowthProgress(JSON.parse(read(growthStorageKey) ?? memory ?? 'null'))) return;} catch { /* Recover corrupt local state. */ }
    // Read the browser here: the first hydration render still uses the SSR
    // snapshot and must not overwrite inherited progress with an empty plan.
    memory = JSON.stringify(decodeGrowth(read(growthStorageKey), read(starterStorageKey), starterIds));
    try {localStorage.setItem(growthStorageKey, memory); storageFailed = false;} catch {storageFailed = true;}
    window.dispatchEvent(new CustomEvent('aion2-growth-initialized'));
  }, [starterIds]);
  return {progress, save, initialize, temporary: storageFailed};
}
