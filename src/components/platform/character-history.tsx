'use client';
import {useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import type {CharacterData, Region} from '@/lib/aion2/types';
import {StorageNotice, useWorkspace} from './item-actions';
export function CharacterHistory({data, region, locale}: {data: CharacterData; region: Region; locale: Locale}) {
  const m = platformMessages[locale]; const [state, save] = useWorkspace(); const [message, setMessage] = useState('');
  const profile = data.info.profile;
  const history = state.snapshots.filter((s) => s.region === region && s.serverId === profile.serverId && s.characterId === profile.characterId).sort((a, b) => b.capturedAt.localeCompare(a.capturedAt));
  const [latest, previous] = history;
  return <section className="game-tool" data-character-history><h3>{m.snapshots}</h3><p className="tool-note">{m.snapshotNote}</p><button className="tool-button" onClick={() => {
    if (state.snapshots.length >= 40) {setMessage(m.storageLimit); return;}
    const snapshot = {key: crypto.randomUUID(), name: profile.characterName, region, serverId: profile.serverId, characterId: profile.characterId, capturedAt: new Date().toISOString(), power: profile.combatPower,
      stats: (data.info.stat?.statList || []).map((s) => ({id: s.type, name: s.name, value: s.value})), equipment: data.equipment.equipment.equipmentList.map((i) => ({id: i.id, slot: i.slotPos, level: i.enchantLevel}))};
    save({...state, snapshots: [...state.snapshots, snapshot]}); setMessage(m.saved);
  }}>{m.saveSnapshot}</button>{message && <p role="status">{message}</p>}
    {latest && <p>{m.latest}: <time dateTime={latest.capturedAt}>{new Date(latest.capturedAt).toLocaleString(locale)}</time> · {latest.power.toLocaleString(locale)}</p>}
    {latest && previous && <><p>{m.previous}: <time dateTime={previous.capturedAt}>{new Date(previous.capturedAt).toLocaleString(locale)}</time></p><dl className="tool-stats"><div><dt>{m.power}</dt><dd>{new Intl.NumberFormat(locale, {signDisplay: 'exceptZero'}).format(latest.power - previous.power)}</dd></div>{latest.stats.flatMap((s) => {
      const old = previous.stats.find((p) => p.id === s.id); return old && s.value !== old.value ? [<div key={s.id}><dt>{s.name}</dt><dd>{new Intl.NumberFormat(locale, {signDisplay: 'exceptZero', maximumFractionDigits: 3}).format(s.value - old.value)}</dd></div>] : [];
    })}</dl></>}
    <StorageNotice locale={locale} />
  </section>;
}
