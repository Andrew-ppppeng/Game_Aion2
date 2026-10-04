'use client';
import {useMemo, useState, useSyncExternalStore} from 'react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import type {CatalogueEntry} from '@/lib/aion2/catalogue';
import {decodeBuild, encodeBuild, mergeWorkspace, refKey, validBuild, type Build, type ItemRef} from '@/lib/aion2/workspace';
import {regions, type Region} from '@/lib/aion2/types';
import {StorageNotice, useWorkspace} from './item-actions';
import {parseBackup, toolKeys, validToolValue, type Backup, type ToolKey} from '@/lib/aion2/backup';
import {readStoredValue, writeStoredValue} from '../tools/local-store';
const subscribeHash = (callback: () => void) => {window.addEventListener('hashchange', callback); return () => window.removeEventListener('hashchange', callback);};
export function WorkspaceView({entries, locale}: {entries: CatalogueEntry[]; locale: Locale}) {
  const m = platformMessages[locale];
  const [state, save] = useWorkspace();
  const [message, setMessage] = useState(''); const [task, setTask] = useState(''); const [name, setName] = useState('');
  const [region, setRegion] = useState<Region>('nae');
  const [selectedBuild, setSelectedBuild] = useState(''); const [selectedItem, setSelectedItem] = useState(entries[0]?.item.id);
  const [slot, setSlot] = useState(''); const [level, setLevel] = useState(0);
  const hash = useSyncExternalStore(subscribeHash, () => location.hash, () => '');
  const validEquipmentPlan = (b: Build) => validBuild(b) && entries.some((e) => e.regions.includes(b.region)) && b.items.every((i) => entries.some((e) => e.item.id === i.itemId && e.regions.includes(b.region) && i.enchantLevel <= (e.item.maxEnchantLevel ?? 0)));
  const shared = useMemo(() => {
    if (!hash.startsWith('#plan=')) return null;
    try {const plan = decodeBuild(hash.slice(6)); return validEquipmentPlan(plan) ? plan : 'invalid';} catch {return 'invalid';}
  // The catalogue is fixed for this page. Validation remains independent of stored plans.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [hash, entries]);
  const activeBuild = state.builds.find((b) => b.id === selectedBuild) || state.builds[0];
  const candidate = entries.find((e) => e.item.id === selectedItem);
  async function importFile(file?: File) {
    if (!file) return;
    try {
      if (file.size > 1_000_000) throw new Error('large');
      const parsed = parseBackup(JSON.parse(await file.text()));
      const merged = mergeWorkspace(state, parsed.workspace);
      if (!merged.builds.every(validEquipmentPlan) || [...merged.favorites, ...merged.goals, ...merged.recent].some((i) => !entries.some((e) => e.item.id === i.id && e.regions.includes(i.region)))) throw new Error('unknown-equipment');
      save(merged);
      for (const [key, value] of Object.entries(parsed.tools)) {
        const existing = readStoredValue(key);
        if (existing === null || !validToolValue(key as ToolKey, existing)) writeStoredValue(key, value);
        else if (Array.isArray(value) && Array.isArray(existing)) {
          const unique = new Map([...value, ...existing].map((v) => [typeof v === 'string' ? v : `${v.region}:${v.serverId}:${v.id}`, v]));
          writeStoredValue(key, [...unique.values()].slice(0, key === 'aion2-characters-v1' ? 30 : 200));
        }
      }
      setMessage(m.imported);
    } catch {setMessage(m.invalidImport);}
  }
  function exportFile() {
    const tools = Object.fromEntries(toolKeys.flatMap((key) => {const value = readStoredValue(key); return value !== null && validToolValue(key, value) ? [[key, value]] : [];}));
    const backup: Backup = {format: 'aion2-backup', version: 1, workspace: state, tools};
    const url = URL.createObjectURL(new Blob([JSON.stringify(backup, null, 2)], {type: 'application/json'}));
    const link = document.createElement('a'); link.href = url; link.download = 'aion2-workspace.json'; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  async function share(plan: Build) {
    const url = `${location.origin}${location.pathname}#plan=${encodeBuild(plan)}`;
    try {await navigator.clipboard.writeText(url); setMessage(m.copied);} catch {setMessage(url);}
  }
  const itemLink = (ref: ItemRef) => {
    const entry = entries.find((e) => e.item.id === ref.id);
    return entry ? <Link href={`/database/items/${ref.id}?region=${ref.region}`}>{entry.item.name} <small>{ref.region.toUpperCase()}</small></Link> : <span>{ref.id} · {m.unavailable}</span>;
  };
  function renderPlan(plan: Build) {return <ul className="workspace-list">{plan.items.map((i) => <li key={i.slot}><span>{i.slot}</span>{itemLink({id: i.itemId, region: plan.region})}<strong>+{i.enchantLevel}</strong>{plan === activeBuild && <button className="tool-button" onClick={() => save({...state, builds: state.builds.map((b) => b.id === plan.id ? {...b, items: b.items.filter((v) => v.slot !== i.slot)} : b)})}>{m.remove}</button>}</li>)}</ul>;}
  return <div data-workspace>
    <section className="game-tool"><StorageNotice locale={locale} /><div className="tool-actions"><button className="tool-button" onClick={exportFile}>{m.export}</button><label className="tool-button file-import">{m.import}<input type="file" accept="application/json,.json" aria-label={m.import} onChange={(e) => {void importFile(e.target.files?.[0]); e.target.value = '';}} /></label></div>{message && <p role="status" className="workspace-message">{message}</p>}</section>
    {shared && <section className="game-tool"><h2>{m.shared}</h2>{shared === 'invalid' ? <p role="alert">{m.invalidPlan}</p> : <><h3>{shared.name} · {shared.region.toUpperCase()}</h3>{renderPlan(shared)}<p className="tool-note">{m.sharedNote}</p><button className="tool-button" onClick={() => {
      if (state.builds.length >= 30) {setMessage(m.storageLimit); return;}
      const copy = {...shared, id: crypto.randomUUID()}; save({...state, builds: [...state.builds, copy]}); setSelectedBuild(copy.id); setMessage(m.saved);
    }}>{m.savePlan}</button></>}</section>}
    <section className="game-tool"><div className="platform-heading"><h2>{m.goals} <small>{state.goals.filter((g) => g.done).length} / {state.goals.length}</small></h2><Link className="tool-link" href="/database">{m.browse} →</Link></div>
      {!state.goals.length ? <p>{m.empty}</p> : <ul className="workspace-list">{state.goals.map((g) => <li key={refKey(g)}><label className="workspace-check"><input type="checkbox" checked={g.done} aria-label={g.done ? m.incomplete : m.complete} onChange={(e) => save({...state, goals: state.goals.map((v) => refKey(v) === refKey(g) ? {...v, done: e.target.checked} : v)})} />{itemLink(g)}</label><button className="tool-button" onClick={() => save({...state, goals: state.goals.filter((v) => refKey(v) !== refKey(g))})}>{m.remove}</button></li>)}</ul>}
    </section>
    <section className="game-tool"><h2>{m.builds}</h2>
      <form className="tool-actions" onSubmit={(e) => {e.preventDefault(); if (state.builds.length >= 30) {setMessage(m.storageLimit); return;} const build = {id: crypto.randomUUID(), name: name.trim(), region, items: []}; if (!validBuild(build)) return; save({...state, builds: [...state.builds, build]}); setSelectedBuild(build.id); setName('');}}>
        <label className="tool-field">{m.buildName}<input required maxLength={80} value={name} onChange={(e) => setName(e.target.value)} /></label><label className="tool-field">{m.region}<select aria-label={m.region} value={region} onChange={(e) => setRegion(e.target.value as Region)}>{regions.map((r) => <option key={r} disabled={!entries.some((e) => e.regions.includes(r))}>{r}</option>)}</select></label><button className="tool-button">{m.create}</button>
      </form>
      {activeBuild && <div className="workspace-plan"><label className="tool-field">{m.builds}<select aria-label={m.builds} value={activeBuild.id} onChange={(e) => {setSelectedBuild(e.target.value); setLevel(0);}}>{state.builds.map((b) => <option key={b.id} value={b.id}>{b.name} · {b.region.toUpperCase()}</option>)}</select></label>{renderPlan(activeBuild)}
        <form className="tool-actions" onSubmit={(e) => {e.preventDefault(); if (!candidate || !candidate.regions.includes(activeBuild.region)) return;
          const label = slot.trim() || candidate.item.categoryName || candidate.item.name;
          const next = {...activeBuild, items: [...activeBuild.items.filter((i) => i.slot !== label), {slot: label, itemId: selectedItem, enchantLevel: level}]};
          if (!validEquipmentPlan(next)) {setMessage(m.invalidPlan); return;} save({...state, builds: state.builds.map((b) => b.id === next.id ? next : b)}); setSlot('');
        }}><label className="tool-field">{m.items}<select aria-label={m.items} value={selectedItem} onChange={(e) => {setSelectedItem(Number(e.target.value)); setLevel(0);}}>{entries.filter((v) => v.regions.includes(activeBuild.region)).map(({item}) => <option key={item.id} value={item.id}>{item.name}</option>)}</select></label>
          <label className="tool-field">{m.slot}<input value={slot} maxLength={80} placeholder={candidate?.item.categoryName} onChange={(e) => setSlot(e.target.value)} /></label><label className="tool-field">{m.enhance}<select aria-label={m.enhance} value={level} onChange={(e) => setLevel(Number(e.target.value))}>{Array.from({length: (candidate?.item.maxEnchantLevel ?? 0) + 1}, (_, n) => <option key={n} value={n}>+{n}</option>)}</select></label><button className="tool-button" disabled={!candidate?.regions.includes(activeBuild.region)}>{m.addItem}</button>
        </form><div className="tool-actions"><button className="tool-button" onClick={() => void share(activeBuild)}>{m.share}</button><button className="tool-button" onClick={() => save({...state, builds: state.builds.filter((b) => b.id !== activeBuild.id)})}>{m.delete}</button></div><p className="tool-note">{m.sharedNote}</p>
      </div>}
    </section>
    <section className="game-tool"><h2>{m.tasks}</h2><form className="tool-actions" onSubmit={(e) => {e.preventDefault(); if (!task.trim()) return; if (state.tasks.length >= 100) {setMessage(m.storageLimit); return;} save({...state, tasks: [...state.tasks, {id: crypto.randomUUID(), text: task.trim(), done: false}]}); setTask('');}}><label className="tool-field">{m.task}<input maxLength={160} required value={task} onChange={(e) => setTask(e.target.value)} /></label><button className="tool-button">{m.add}</button></form>
      <ul className="workspace-list">{state.tasks.map((t) => <li key={t.id}><label className="workspace-check"><input type="checkbox" checked={t.done} onChange={(e) => save({...state, tasks: state.tasks.map((v) => v.id === t.id ? {...v, done: e.target.checked} : v)})} /><span>{t.text}</span></label><button className="tool-button" onClick={() => save({...state, tasks: state.tasks.filter((v) => v.id !== t.id)})}>{m.remove}</button></li>)}</ul>
    </section>
    <div className="workspace-columns">{(['favorites', 'recent'] as const).map((key) => <section className="game-tool" key={key}><h2>{m[key]}</h2>{!state[key].length ? <p>{m.empty}</p> : <ul className="workspace-list">{state[key].map((i) => <li key={refKey(i)}>{itemLink(i)}<button className="tool-button" onClick={() => save({...state, [key]: state[key].filter((v) => refKey(v) !== refKey(i))})}>{m.remove}</button></li>)}</ul>}</section>)}</div>
    <section className="game-tool"><h2>{m.snapshots}</h2>{!state.snapshots.length ? <p>{m.empty} <Link href="/tools/character">{m.character} →</Link></p> : <ul className="workspace-list">{state.snapshots.map((s) => <li key={s.key}><div><strong>{s.name} · {s.region.toUpperCase()}</strong><p><time dateTime={s.capturedAt}>{new Date(s.capturedAt).toLocaleString(locale)}</time> · {m.power}: {s.power.toLocaleString(locale)}</p><Link href={`/tools/character?${new URLSearchParams({cid: s.characterId, serverId: String(s.serverId), region: s.region})}`}>{m.viewCharacter} →</Link></div><button className="tool-button" onClick={() => save({...state, snapshots: state.snapshots.filter((v) => v.key !== s.key)})}>{m.remove}</button></li>)}</ul>}</section>
    <div className="tool-actions"><Link className="tool-link" href="/tools/budget">{m.budget} →</Link><Link className="tool-link" href="/tools/calendar">{m.calendar} →</Link></div>
  </div>;
}
