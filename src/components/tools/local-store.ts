'use client';
import {useMemo, useSyncExternalStore} from 'react';

const memory = new Map<string, string>();
const failed = new Set<string>();
function subscribe(callback: () => void) {
  const storage = (event: StorageEvent) => {if (event.key) {memory.delete(event.key); failed.delete(event.key);} else {memory.clear(); failed.clear();} callback();};
  window.addEventListener('storage', storage);
  window.addEventListener('aion2-tool-storage', callback);
  return () => {window.removeEventListener('storage', storage); window.removeEventListener('aion2-tool-storage', callback);};
}
export function useStorageFailure(key: string | string[]) {
  return useSyncExternalStore(subscribe, () => (Array.isArray(key) ? key : [key]).some((k) => failed.has(k)), () => false);
}
export function readStoredValue(key: string): unknown {
  try {return JSON.parse((failed.has(key) ? memory.get(key) : localStorage.getItem(key) || memory.get(key)) || 'null');} catch {return null;}
}
export function writeStoredValue(key: string, value: unknown) {
  const serialized = JSON.stringify(value); memory.set(key, serialized);
  try {localStorage.setItem(key, serialized); failed.delete(key);} catch {failed.add(key);}
  window.dispatchEvent(new CustomEvent('aion2-tool-storage', {detail: {key}}));
}
export function useStored<T>(key: string, initial: T, validate: (value: unknown) => value is T): [T, (value: T) => void] {
  const fallback = JSON.stringify(initial);
  const text = useSyncExternalStore(subscribe, () => {
    if (failed.has(key)) return memory.get(key) ?? fallback;
    try {return localStorage.getItem(key) ?? memory.get(key) ?? fallback;} catch {failed.add(key); return memory.get(key) ?? fallback;}
  }, () => fallback);
  const value = useMemo(() => {try {const parsed: unknown = JSON.parse(text); return validate(parsed) ? parsed : initial;} catch {return initial;}}, [text, initial, validate]);
  return [value, (next) => {
    writeStoredValue(key, next);
  }];
}
let now = 0;
function subscribeClock(callback: () => void) {
  now = Date.now();
  const timer = setInterval(() => {now = Date.now(); callback();}, 1000);
  return () => clearInterval(timer);
}
export function useClock(initialNow: number) {return useSyncExternalStore(subscribeClock, () => now || initialNow, () => initialNow);}
