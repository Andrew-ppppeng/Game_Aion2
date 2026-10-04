'use client';
import {useEffect, useRef, useState} from 'react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import {toolMessages, errorMessage} from '@/i18n/tool-messages';
import type {CatalogueEntry} from '@/lib/aion2/catalogue';
import {regions, type Region, type Item, type ApiResult} from '@/lib/aion2/types';
import {ItemDetails} from '../tools/item-details';
import {ItemActions, StorageNotice} from './item-actions';
export function ItemView({entry, locale, initialRegion = 'nae'}: {entry: CatalogueEntry; locale: Locale; initialRegion?: Region}) {
  const m = platformMessages[locale]; const t = toolMessages[locale];
  const [region, setRegion] = useState<Region>(initialRegion);
  const [level, setLevel] = useState(0);
  const [result, setResult] = useState<ApiResult<Item> | null>(null);
  const [busy, setBusy] = useState(false); const [error, setError] = useState('');
  const controller = useRef<AbortController | null>(null);
  useEffect(() => () => controller.current?.abort(), []);
  function reset() {controller.current?.abort(); setResult(null); setError(''); setBusy(false);}
  const allowed = entry.regions.includes(region);
  async function load() {
    reset(); const abort = new AbortController(); controller.current = abort; setBusy(true);
    try {
      const response = await fetch(`/api/aion2/items/${entry.item.id}?${new URLSearchParams({locale, region, enchantLevel: String(level)})}`, {signal: abort.signal});
      const data: ApiResult<Item> = await response.json();
      if (!response.ok || !data.data) throw new Error(data.error?.code || 'upstream-unavailable');
      if (!abort.signal.aborted) setResult(data);
    } catch (e) {if (!abort.signal.aborted) setError(errorMessage(e instanceof Error ? e.message : 'upstream-unavailable', locale));}
    finally {if (!abort.signal.aborted) setBusy(false);}
  }
  return <section className="game-tool" data-item-view>
    <div className="tool-actions"><label className="tool-field">{m.region}<select aria-label={m.region} value={region} onChange={(e) => {reset(); setRegion(e.target.value as Region); setLevel(0);}}>{regions.map((r) => <option key={r}>{r}</option>)}</select></label>
      <label className="tool-field">{m.enhance}<select aria-label={m.enhance} value={level} onChange={(e) => {reset(); setLevel(Number(e.target.value));}}>{Array.from({length: (entry.item.maxEnchantLevel ?? 0) + 1}, (_, n) => <option key={n} value={n}>+{n}</option>)}</select></label>
      <button className="tool-button" disabled={!allowed || busy} onClick={load}>{busy ? t.loading : t.inspect}</button></div>
    {error && <p role="alert" className="tool-error">{error}</p>}
    {allowed ? <><ItemDetails item={result?.data || entry.item} meta={result?.meta} locale={locale} /><ItemActions item={{id: entry.item.id, region}} locale={locale} recordRecent /></> : <p role="status">{m.unavailable}</p>}
    <div className="tool-actions"><Link className="tool-link" href={`/tools/compare?first=${entry.item.id}&region=${region}`}>{m.compare} →</Link><Link className="tool-link" href="/workspace">{m.workspace} →</Link></div><StorageNotice locale={locale} />
  </section>;
}
