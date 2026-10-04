'use client';
import {useEffect, useRef, useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import {errorMessage, toolMessages} from '@/i18n/tool-messages';
import type {CatalogueEntry} from '@/lib/aion2/catalogue';
import {compareStats} from '@/lib/aion2/model';
import {regions, type Region, type Item, type ApiResult} from '@/lib/aion2/types';
import {ItemDetails} from '../tools/item-details';
import {ItemActions, StorageNotice} from './item-actions';

export function EquipmentCompare({entries, locale, initialFirst, initialSecond, initialRegion = 'nae'}: {entries: CatalogueEntry[]; locale: Locale; initialFirst?: number; initialSecond?: number; initialRegion?: Region}) {
  const m = platformMessages[locale];
  const t = toolMessages[locale];
  const [region, setRegion] = useState<Region>(initialRegion);
  const [first, setFirst] = useState(initialFirst && entries.some((e) => e.item.id === initialFirst) ? initialFirst : entries[0]?.item.id);
  const [second, setSecond] = useState(initialSecond && entries.some((e) => e.item.id === initialSecond) ? initialSecond : entries[1]?.item.id);
  const [firstLevel, setFirstLevel] = useState(0);
  const [secondLevel, setSecondLevel] = useState(0);
  const [result, setResult] = useState<[ApiResult<Item>, ApiResult<Item>] | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const controller = useRef<AbortController | null>(null);
  useEffect(() => () => controller.current?.abort(), []);
  const a = entries.find((e) => e.item.id === first);
  const b = entries.find((e) => e.item.id === second);
  const allowed = a?.regions.includes(region) && b?.regions.includes(region);
  function reset() {controller.current?.abort(); setBusy(false); setResult(null); setError('');}
  async function compare() {
    reset(); const abort = new AbortController(); controller.current = abort; setBusy(true);
    try {
      const load = async (id: number, level: number) => {
        const response = await fetch(`/api/aion2/items/${id}?${new URLSearchParams({locale, region, enchantLevel: String(level)})}`, {signal: abort.signal});
        const data: ApiResult<Item> = await response.json();
        if (!response.ok || !data.data) throw new Error(data.error?.code || 'upstream-unavailable');
        return data;
      };
      const current = await load(first, firstLevel);
      const target = await load(second, secondLevel);
      if (!abort.signal.aborted) setResult([current, target]);
    } catch (e) {if (!abort.signal.aborted) setError(errorMessage(e instanceof Error ? e.message : 'upstream-unavailable', locale));}
    finally {if (!abort.signal.aborted) setBusy(false);}
  }
  const diffs = result ? compareStats(result[0].data!, result[1].data!) : [];
  return <section className="game-tool" data-equipment-compare><h2>{m.compare}</h2><p className="tool-note">{m.compareNote}</p>
    <label className="tool-field">{m.region}<select aria-label={m.region} value={region} onChange={(e) => {reset(); setRegion(e.target.value as Region);}}>{regions.map((r) => <option key={r}>{r}</option>)}</select></label>
    <div className="comparison-selectors">{([[first, setFirst, firstLevel, setFirstLevel, a, m.first], [second, setSecond, secondLevel, setSecondLevel, b, m.second]] as const).map(([id, setId, level, setLevel, entry, label]) => <div key={label}>
      <label className="tool-field">{label}<select aria-label={label} value={id} onChange={(e) => {reset(); setId(Number(e.target.value)); setLevel(0);}}>{entries.filter((e) => e.regions.includes(region)).map(({item}) => <option key={item.id} value={item.id}>{item.name} · {item.categoryName}</option>)}</select></label>
      <label className="tool-field">{m.enhance}<select aria-label={`${m.enhance} · ${label}`} value={level} onChange={(e) => {reset(); setLevel(Number(e.target.value));}}>{Array.from({length: (entry?.item.maxEnchantLevel ?? 0) + 1}, (_, n) => <option value={n} key={n}>+{n}</option>)}</select></label>
    </div>)}</div>
    <button className="tool-button" type="button" onClick={compare} disabled={busy || !allowed}>{busy ? t.loading : m.compareAction}</button>
    {!allowed && <p role="status">{m.unavailable}</p>}{error && <p role="alert" className="tool-error">{error}</p>}
    {result && <><div className="item-grid">{result.map((r, i) => <div key={i}><ItemDetails item={r.data!} locale={locale} meta={r.meta} /><ItemActions item={{id: r.data!.id, region}} locale={locale} /></div>)}</div>
      <h3>{m.difference}</h3>{diffs.length ? <dl className="tool-stats">{diffs.map((d) => <div key={d.id}><dt>{d.name}</dt><dd>{d.min > 0 ? '+' : ''}{d.min}{d.min !== d.max ? ` – ${d.max > 0 ? '+' : ''}${d.max}` : ''}{d.unit === 'percent' ? ` ${t.percentagePoints}` : ''}</dd></div>)}</dl> : <p>{t.noComparable}</p>}</>}
    <StorageNotice locale={locale} />
  </section>;
}
