'use client';
import {useEffect, useRef, useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import {errorMessage, toolMessages} from '@/i18n/tool-messages';
import type {BoardDetail} from '@/lib/aion2/nodes';
import type {ApiResult, Region} from '@/lib/aion2/types';
import {DataUpdated} from '../tools/item-details';
export function CharacterBoard({id, serverId, board, region, locale}: {id: string; serverId: number; board: {id: number; name: string}; region: Region; locale: Locale}) {
  const m = platformMessages[locale]; const t = toolMessages[locale];
  const [result, setResult] = useState<ApiResult<BoardDetail> | null>(null); const [busy, setBusy] = useState(false); const [error, setError] = useState('');
  const [selected, setSelected] = useState(0); const controller = useRef<AbortController | null>(null);
  useEffect(() => () => controller.current?.abort(), []);
  async function load() {
    controller.current?.abort(); const abort = new AbortController(); controller.current = abort; setBusy(true); setError('');
    try {
      const response = await fetch(`/api/aion2/characters/${encodeURIComponent(id)}/boards/${board.id}?${new URLSearchParams({region, locale, serverId: String(serverId)})}`, {signal: abort.signal});
      const data: ApiResult<BoardDetail> = await response.json(); if (!response.ok || !data.data) throw new Error(data.error?.code || 'upstream-unavailable');
      if (!abort.signal.aborted) {setResult(data); setSelected(0);}
    } catch (e) {if (!abort.signal.aborted) setError(errorMessage(e instanceof Error ? e.message : 'upstream-unavailable', locale));}
    finally {if (!abort.signal.aborted) setBusy(false);}
  }
  const nodes = result?.data?.nodeList.filter((n) => n.type !== 'None' && n.name) || [];
  const active = nodes.find((n) => n.nodeId === selected);
  const cols = Math.max(...nodes.map((n) => n.col), 1);
  return <div className="character-board"><button className="tool-button" type="button" disabled={busy} onClick={load}>{busy ? t.loading : `${board.name} · ${m.nodeDetails}`}</button>{error && <p role="alert">{error}</p>}
    {!!nodes.length && <><div className="node-board-scroll"><div className="node-board" style={{gridTemplateColumns: `repeat(${cols + 1}, 28px)`}} aria-label={board.name}>{nodes.map((n) => <button type="button" key={n.nodeId} style={{gridRow: n.row + 1, gridColumn: n.col + 1}} className={`node-cell ${n.open ? 'unlocked' : ''}`} aria-label={`${n.name} · ${n.open ? m.acquired : m.locked}`} aria-pressed={selected === n.nodeId} onClick={() => setSelected(n.nodeId)}>{n.open ? '●' : '○'}</button>)}</div></div>
      {active && <div className="node-detail" role="status"><strong>{active.name}</strong><p>{active.open ? m.acquired : m.locked}</p><ul>{active.effectList.filter((e) => e.desc).map((e, i) => <li key={i}>{e.desc}</li>)}</ul></div>}{result?.meta && <DataUpdated meta={result.meta} locale={locale} />}{result?.meta?.freshness === 'stale' && <p role="status" className="tool-error">{t.stale}</p>}</>}
  </div>;
}
