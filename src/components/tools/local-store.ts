'use client';
import {useMemo, useSyncExternalStore} from 'react';

const memory = new Map<string, string>();
const failed = new Set<string>();
function subscribe(callback: () => void) {
  const storage = (event: StorageEvent) => {if (event.key) {memory.delete(event.key); failed.delete(event.key);} callback();};
  window.addEventListener('storage', storage);
  window.addEventListener('aion2-tool-storage', callback);
  return () => {window.removeEventListener('storage', storage); window.removeEventListener('aion2-tool-storage', callback);};
}
export function useStored<T>(key: string, initial: T, validate: (value: unknown) => value is T): [T, (value: T) => void] {
  const fallback = JSON.stringify(initial);
  const text = useSyncExternalStore(subscribe, () => {
    if (failed.has(key)) return memory.get(key) ?? fallback;
    try {return localStorage.getItem(key) ?? memory.get(key) ?? fallback;} catch {return memory.get(key) ?? fallback;}
  }, () => fallback);
  const value = useMemo(() => {try {const parsed: unknown = JSON.parse(text); return validate(parsed) ? parsed : initial;} catch {return initial;}}, [text, initial, validate]);
  return [value, (next) => {
    const serialized = JSON.stringify(next);
    memory.set(key, serialized);
    try {localStorage.setItem(key, serialized); failed.delete(key);} catch {failed.add(key);}
    window.dispatchEvent(new Event('aion2-tool-storage'));
  }];
}
let now = 0;
function subscribeClock(callback: () => void) {
  now = Date.now();
  const timer = setInterval(() => {now = Date.now(); callback();}, 1000);
  return () => clearInterval(timer);
}
export function useClock(initialNow: number) {return useSyncExternalStore(subscribeClock, () => now || initialNow, () => initialNow);}
