'use client';

import {useMemo, useSyncExternalStore} from 'react';
import {RotateCcw} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';

const fallback = new Map<string, string>();
const failedWrites = new Set<string>();
function subscribe(onChange: () => void) {
  const onStorage = (event: StorageEvent) => {
    if (event.key) {fallback.delete(event.key); failedWrites.delete(event.key);} else {fallback.clear(); failedWrites.clear();}
    onChange();
  };
  window.addEventListener('storage', onStorage);
  window.addEventListener('aion-checklist', onChange);
  return () => {window.removeEventListener('storage', onStorage); window.removeEventListener('aion-checklist', onChange);};
}
function snapshot(key: string) {
  if (failedWrites.has(key)) return fallback.get(key) ?? '[]';
  try {return localStorage.getItem(key) ?? fallback.get(key) ?? '[]';} catch {return fallback.get(key) ?? '[]';}
}
function save(key: string, ids: string[]) {
  const value = JSON.stringify(ids);
  fallback.set(key, value);
  try {localStorage.setItem(key, value); failedWrites.delete(key);} catch {failedWrites.add(key);}
  window.dispatchEvent(new Event('aion-checklist'));
}

export function GuideChecklist({slug, locale, title, items}: {slug: string; locale: Locale; title: string; items: {id: string; label: string}[]}) {
  const key = `aion2-checklist-v1:${slug}`;
  const value = useSyncExternalStore(subscribe, () => snapshot(key), () => '[]');
  const selected = useMemo(() => {
    try {const ids: unknown = JSON.parse(value); return new Set(Array.isArray(ids) ? ids.filter((id) => typeof id === 'string' && items.some((item) => item.id === id)) : []);} catch {return new Set<string>();}
  }, [value, items]);
  const m = guideMessages[locale];
  return <section className="guide-checklist" aria-label={title} data-checklist={slug}>
    <div className="guide-checklist-heading"><h3>{title}</h3><button type="button" onClick={() => save(key, [])}><RotateCcw size={14} aria-hidden="true" />{m.reset}</button></div>
    <p className="guide-checklist-count" role="status">{selected.size} / {items.length} {m.complete}</p>
    <progress value={selected.size} max={items.length} aria-label={title} />
    <ul>{items.map((item) => <li key={item.id}><label><input type="checkbox" checked={selected.has(item.id)} onChange={(event) => {
      const next = new Set(selected);
      if (event.target.checked) next.add(item.id); else next.delete(item.id);
      save(key, [...next]);
    }} /><span>{item.label}</span></label></li>)}</ul>
    <p className="guide-checklist-note">{m.checklistNote}</p>
  </section>;
}
