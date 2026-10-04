'use client';
import {useEffect, useRef, useState} from 'react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {errorMessage, toolMessages} from '@/i18n/tool-messages';
import {guideMessages} from '@/i18n/guide-messages';
import identities from '@/content/class-identities.json';
import {compareStats} from '@/lib/aion2/model';
import {regions} from '@/lib/aion2/types';
import type {ApiResult, CharacterData, CharacterMatch, EquippedItem, Item, MetaData, Region, SearchData} from '@/lib/aion2/types';
import {ItemDetails, DataUpdated} from './item-details';
import {CharacterHistory} from '../platform/character-history';
import {CharacterBoard} from '../platform/character-board';
import {StorageNotice} from '../platform/item-actions';
import {useStored} from './local-store';

type Bookmark = {id: string; name: string; region: Region; serverId: number};
const noBookmarks: Bookmark[] = [];
const isBookmarks = (v: unknown): v is Bookmark[] => Array.isArray(v) && v.length <= 30 && v.every((b) => b && typeof b.id === 'string' && typeof b.name === 'string' && regions.includes(b.region) && Number.isInteger(b.serverId));
const isRegion = (v: unknown): v is Region => regions.includes(v as Region);
const regionKeys = {nae: 'naEast', naw: 'naWest', eu: 'eu', la: 'latam', as: 'asia'} as const;
const query = (values: Record<string, string | number>) => new URLSearchParams(Object.fromEntries(Object.entries(values).map(([k, v]) => [k, String(v)]))).toString();

export function CharacterTool({locale, metadata, candidates, initialCharacter}: {
  locale: Locale; metadata: Record<Region, MetaData>; candidates: Item[]; initialCharacter?: {id: string; serverId: number; region: Region};
}) {
  const m = toolMessages[locale];
  const [rememberedRegion, rememberRegion] = useStored<Region>('aion2-region-v1', 'nae', isRegion);
  const [liveMetadata, setLiveMetadata] = useState(metadata);
  const [override, setOverride] = useState<Region | null>(initialCharacter?.region ?? null);
  const region = override ?? rememberedRegion;
  const [bookmarks, saveBookmarks] = useStored('aion2-characters-v1', noBookmarks, isBookmarks);
  const [name, setName] = useState('');
  const [server, setServer] = useState('');
  const [className, setClassName] = useState('');
  const [matches, setMatches] = useState<ApiResult<SearchData> | null>(null);
  const [character, setCharacter] = useState<ApiResult<CharacterData> | null>(null);
  const [selected, setSelected] = useState<Bookmark | null>(null);
  const [slot, setSlot] = useState<EquippedItem | null>(null);
  const [actual, setActual] = useState<ApiResult<Item> | null>(null);
  const [candidate, setCandidate] = useState('');
  const [enhancement, setEnhancement] = useState(0);
  const [targetEnhancement, setTargetEnhancement] = useState(0);
  const [comparison, setComparison] = useState<{current: ApiResult<Item>; next: ApiResult<Item>} | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [saved, setSaved] = useState(false);
  const controller = useRef<AbortController | null>(null);
  const mountedRequest = useRef(false);
  const meta = liveMetadata[region];
  useEffect(() => {
    const abort = new AbortController();
    fetch(`/api/aion2/meta?${query({region, locale})}`, {signal: abort.signal}).then((response) => response.json()).then((result: ApiResult<MetaData>) => {
      if (result.data && !abort.signal.aborted) setLiveMetadata((old) => ({...old, [region]: result.data!}));
    }).catch(() => {});
    return () => abort.abort();
  }, [region, locale]);
  function classLabel(value: string) {return identities.find((i) => i.names.en === value)?.names[locale] ?? value;}
  async function api<T>(path: string, params: Record<string, string | number>, abort: AbortController) {
    const response = await fetch(`${path}?${query({locale, region, ...params})}`, {signal: abort.signal});
    const result = await response.json() as ApiResult<T>;
    if (!response.ok || result.data === null) throw new Error(result.error?.code || 'upstream-unavailable');
    return result;
  }
  async function run(task: (abort: AbortController) => Promise<void>) {
    controller.current?.abort();
    const abort = new AbortController(); controller.current = abort;
    setBusy(true); setError('');
    try {await task(abort);} catch (e) {if (!abort.signal.aborted) setError(errorMessage(e instanceof Error ? e.message : '', locale));}
    finally {if (controller.current === abort) setBusy(false);}
  }
  async function open(bookmark: Bookmark) {
    setOverride(bookmark.region); rememberRegion(bookmark.region);
    setCharacter(null); setSlot(null); setActual(null); setComparison(null); setSelected(bookmark); setSaved(false);
    await run(async (abort) => {
      const result = await api<CharacterData>(`/api/aion2/characters/${encodeURIComponent(bookmark.id)}`, {serverId: bookmark.serverId, region: bookmark.region}, abort);
      if (!abort.signal.aborted) {
        setCharacter(result);
        window.history.replaceState(null, '', `${window.location.pathname}?${query({cid: bookmark.id, serverId: bookmark.serverId, region: bookmark.region})}`);
      }
    });
  }
  useEffect(() => {
    if (initialCharacter && !mountedRequest.current) {
      mountedRequest.current = true;
      Promise.resolve().then(() => open({...initialCharacter, name: initialCharacter.id}));
    }
    return () => controller.current?.abort();
    // A URL lookup runs once on mount. Locale switches mount a new tool and retain the URL.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  function changeRegion(value: Region) {
    controller.current?.abort(); setBusy(false); setError(''); setOverride(value); rememberRegion(value);
    setServer(''); setClassName(''); setMatches(null); setCharacter(null); setSelected(null); setSlot(null); setActual(null); setComparison(null);
    window.history.replaceState(null, '', window.location.pathname);
  }
  async function search(page = 1) {
    await run(async (abort) => {
      const result = await api<SearchData>('/api/aion2/characters/search', {q: name.trim(), page, ...(server ? {serverId: server} : {}), ...(className ? {class: className} : {})}, abort);
      if (!abort.signal.aborted) {setMatches(result); setCharacter(null); setSlot(null); setComparison(null);}
    });
  }
  async function inspect(item: EquippedItem) {
    if (!selected) return;
    setSlot(item); setComparison(null); setActual(null); setCandidate(''); setEnhancement(0); setTargetEnhancement(0);
    await run(async (abort) => {
      const result = await api<Item>(`/api/aion2/characters/${encodeURIComponent(selected.id)}/equipment/${item.slotPos}`, {serverId: selected.serverId}, abort);
      if (!abort.signal.aborted) setActual(result);
    });
  }
  const target = candidates.find((i) => i.id === Number(candidate));
  const profileClass = character?.data?.info.profile.className;
  const canonicalClass = meta.pcData.find((p) => p.id === character?.data?.info.profile.pcId)?.classText;
  const classIdentity = identities.find((i) => i.names.en === canonicalClass || Object.values(i.names).includes(profileClass || ''));
  const allowedClassNames = [profileClass, ...(classIdentity ? Object.values(classIdentity.names) : [])];
  const incompatible = Boolean(target && character?.data && ((target.classNames?.length && !target.classNames.some((n) => allowedClassNames.includes(n))) || target.equipLevel > character.data.info.profile.characterLevel));
  const sameCategory = !actual?.data || !target || target.categoryName === actual.data.categoryName;
  async function compare() {
    if (!slot || !selected || !target || incompatible || !sameCategory) return;
    setComparison(null);
    await run(async (abort) => {
      const params = {characterId: selected.id, serverId: selected.serverId, enchantLevel: enhancement};
      const current = await api<Item>(`/api/aion2/items/${slot.id}`, params, abort);
      const next = await api<Item>(`/api/aion2/items/${target.id}`, {enchantLevel: targetEnhancement}, abort);
      if (!abort.signal.aborted) setComparison({current, next});
    });
  }
  const profile = character?.data?.info.profile;
  const number = new Intl.NumberFormat(locale);
  const bookmark = () => {
    if (!selected || !profile) return;
    const saved = {...selected, name: profile.characterName};
    saveBookmarks([...bookmarks.filter((b) => !(b.id === saved.id && b.region === saved.region && b.serverId === saved.serverId)), saved].slice(-30));
    setSaved(true);
  };
  return <div className="character-tool" data-character-tool>
    <section className="game-tool"><form onSubmit={(e) => {e.preventDefault(); void search();}}>
      <div className="tool-form-grid">
        <label className="tool-field">{m.region}<select value={region} disabled={busy} onChange={(e) => changeRegion(e.target.value as Region)}>{regions.map((r) => <option key={r} value={r}>{guideMessages[locale][regionKeys[r]]}</option>)}</select></label>
        <label className="tool-field">{m.server}<select value={server} disabled={busy} onChange={(e) => {setServer(e.target.value); setMatches(null);}}><option value="">{m.allServers}</option>{meta.servers.map((s) => <option key={s.serverId} value={s.serverId}>{s.serverName} ({s.serverId})</option>)}</select></label>
        <label className="tool-field">{m.class}<select value={className} disabled={busy} onChange={(e) => {setClassName(e.target.value); setMatches(null);}}><option value="">{m.allClasses}</option>{meta.classes.map((c) => <option key={c.id} value={c.name}>{classLabel(c.name)}</option>)}</select></label>
      </div>
      <div className="tool-search"><label className="tool-field">{m.name}<input required maxLength={64} value={name} disabled={busy} onChange={(e) => {setName(e.target.value); setMatches(null);}} /></label><button className="tool-button primary" type="submit" disabled={busy}>{m.search}</button></div>
    </form><p className="tool-note">{m.localNote}</p></section>
    {busy && <p role="status" className="tool-loading">{m.loading}</p>}
    {error && <p role="alert" className="tool-error">{error}</p>}
    {bookmarks.length > 0 && <details className="game-tool"><summary>{m.bookmarks} ({bookmarks.length})</summary>{bookmarks.map((b) => <div className="bookmark-row" key={`${b.region}-${b.serverId}-${b.id}`}><button type="button" className="tool-button" disabled={busy} onClick={() => void open(b)}>{b.name} · {b.region.toUpperCase()} · {b.serverId}</button><button type="button" className="tool-button" onClick={() => saveBookmarks(bookmarks.filter((x) => x !== b))}>{m.remove}</button></div>)}</details>}
    {matches?.data && <section className="game-tool" aria-label={m.search}>
      {!matches.data.list.length && <p role="status">{m.empty}</p>}
      <div className="character-results">{matches.data.list.map((match: CharacterMatch) => <button className="character-match" key={`${match.serverId}-${match.characterId}`} type="button" disabled={busy} onClick={() => void open({id: match.characterId, serverId: match.serverId, name: match.name, region})}>
        <strong>{match.name}</strong><span>{match.serverName} · {m.level} {match.level} · {classLabel(meta.pcData.find((p) => p.id === match.pcId)?.classText || '')}</span><span>{m.select} →</span></button>)}</div>
      <div className="tool-actions"><button type="button" className="tool-button" disabled={busy || matches.data.pagination.page <= 1} onClick={() => void search(matches.data!.pagination.page - 1)}>{m.previous}</button><span>{matches.data.pagination.page} / {matches.data.pagination.endPage}</span><button type="button" className="tool-button" disabled={busy || matches.data.pagination.page >= matches.data.pagination.endPage} onClick={() => void search(matches.data!.pagination.page + 1)}>{m.next}</button></div>
      {matches.meta && <DataUpdated meta={matches.meta} locale={locale} />}
    </section>}
    {profile && character?.data && <>
      <section className="game-tool"><h2>{profile.characterName}</h2><p>{profile.className} · {profile.serverName} · {profile.raceName}</p>
        <dl className="tool-stats"><div><dt>{m.level}</dt><dd>{profile.characterLevel}</dd></div><div><dt>{m.power}</dt><dd>{number.format(profile.combatPower)}</dd></div>{profile.regionName && <div><dt>{m.guild}</dt><dd>{profile.regionName}</dd></div>}</dl>
        <button className="tool-button" type="button" data-analytics="bookmark_save" onClick={bookmark}>{m.saveCharacter}</button>
        {saved && <p className="tool-note" role="status">{m.saved}</p>}
        {character.meta && <DataUpdated meta={character.meta} locale={locale} />}
        {character.meta?.freshness === 'stale' && <p className="tool-error" role="status">{m.stale}</p>}
      </section>
      <section className="game-tool"><h3>{m.equipment}</h3><div className="equipped-grid">{character.data.equipment.equipment.equipmentList.map((i) => <button type="button" className={`equipped-item ${slot?.slotPos === i.slotPos ? 'selected' : ''}`} key={i.slotPos} disabled={busy} aria-pressed={slot?.slotPos === i.slotPos} onClick={() => void inspect(i)}><span>{i.slotPosName} · {i.grade}</span><strong>{i.name} +{i.enchantLevel}</strong><span>{m.inspect} →</span></button>)}</div></section>
      {actual?.data && slot && <section className="game-tool"><ItemDetails item={actual.data} meta={actual.meta} locale={locale} instance />
        <h3>{m.compare}</h3><p className="tool-note">{m.comparisonNote}</p><div className="tool-form-grid">
          <label className="tool-field">{m.candidate}<select value={candidate} disabled={busy} onChange={(e) => {setCandidate(e.target.value); setComparison(null); setTargetEnhancement(0);}}><option value="">—</option>{candidates.filter((i) => i.categoryName === actual.data!.categoryName).map((i) => <option key={i.id} value={i.id}>{i.name}</option>)}</select></label>
          <label className="tool-field">{m.currentTemplate} · {m.enhancement}<select value={enhancement} disabled={busy} onChange={(e) => {setEnhancement(Number(e.target.value)); setComparison(null);}}>{Array.from({length: (actual.data.maxEnchantLevel ?? 0) + 1}, (_, i) => <option key={i} value={i}>+{i}</option>)}</select></label>
          <label className="tool-field">{m.candidateTemplate} · {m.enhancement}<select value={targetEnhancement} disabled={busy || !target} onChange={(e) => {setTargetEnhancement(Number(e.target.value)); setComparison(null);}}>{Array.from({length: (target?.maxEnchantLevel ?? 0) + 1}, (_, i) => <option key={i} value={i}>+{i}</option>)}</select></label>
        </div>{incompatible && <p role="status" className="tool-error">{m.notEligible}</p>}{!sameCategory && <p className="tool-error">{m.sameCategory}</p>}
        <button type="button" className="tool-button primary" disabled={busy || !target || incompatible || !sameCategory} onClick={() => void compare()}>{m.compareAction}</button>
        <p className="tool-note">{m.upgradeCheck} <Link href="/monetization#material-budget">{m.budgetTitle} →</Link></p>
      </section>}
      {comparison && <section className="game-tool" data-item-comparison><h3>{m.fixedDifference}</h3>
        <Difference current={comparison.current.data!} next={comparison.next.data!} locale={locale} />
        <div className="item-grid"><div><h4>{m.currentTemplate}</h4><ItemDetails item={comparison.current.data!} meta={comparison.current.meta} locale={locale} /></div><div><h4>{m.candidateTemplate}</h4><ItemDetails item={comparison.next.data!} meta={comparison.next.meta} locale={locale} /></div></div></section>}
      <section className="game-tool"><h3>{m.progress}</h3>
        {character.data.info.daevanion?.boardList.map((b) => <div key={b.id}><div className="growth-row"><span>{b.name}</span><span>{b.openNodeCount} / {b.totalNodeCount}</span><progress value={b.openNodeCount} max={b.totalNodeCount} aria-label={b.name} /></div><CharacterBoard key={`${region}:${profile.serverId}:${profile.characterId}:${b.id}`} id={profile.characterId} serverId={profile.serverId} board={b} region={region} locale={locale} /></div>)}
        {character.data.info.title && <p>{m.titles}: {character.data.info.title.ownedCount} / {character.data.info.title.totalCount}</p>}
        {character.data.info.title?.titleList.filter((t) => t.name).map((t) => <p key={t.equipCategory}>{t.name}: {t.equipStatList?.map((s) => s.desc).join(', ')}</p>)}
        {character.data.equipment.petwing?.pet?.name && <p>{m.pet}: {character.data.equipment.petwing.pet.name}</p>}
        {character.data.equipment.petwing?.wing?.name && <p>{m.wing}: {character.data.equipment.petwing.wing.name}</p>}
        <p className="tool-note">{m.growthCheck} <Link href="/builds">→</Link></p>
      </section>
      <details className="game-tool"><summary>{m.attributes}</summary><dl className="tool-stats">{character.data.info.stat?.statList.map((s) => <div key={s.type}><dt>{s.name}<small>{s.statSecondList?.join(' · ')}</small></dt><dd>{s.value}</dd></div>)}</dl></details>
      <details className="game-tool"><summary>{m.skills}</summary><ul className="skill-list">{character.data.equipment.skill?.skillList.map((s) => <li key={s.id}><strong>{s.name}</strong><span>{m.level}: {s.skillLevel ?? s.level ?? m.unknown} · {s.category} · {s.acquired === 1 ? m.learned : m.unknown}{s.category === 'Active' && s.acquired === 1 && s.equip === 1 ? ` · ${m.equipped}` : ''}</span></li>)}</ul></details>
      <CharacterHistory data={character.data} region={region} locale={locale} />
    </>}
    <StorageNotice locale={locale} keys={['aion2-characters-v1', 'aion2-region-v1']} />
    <p className="tool-source"><a href="https://aion2.plaync.com/en-us/characters/index" target="_blank" rel="noopener noreferrer">{m.officialCharacter} ↗</a></p>
  </div>;
}
function Difference({current, next, locale}: {current: Item; next: Item; locale: Locale}) {
  const rows = compareStats(current, next);
  const m = toolMessages[locale];
  const format = new Intl.NumberFormat(locale, {maximumFractionDigits: 2, signDisplay: 'exceptZero'});
  return rows.length ? <dl className="tool-stats">{rows.map((r) => <div key={r.id}><dt>{r.name}</dt><dd>{r.min !== r.max ? `${format.format(r.min)} – ` : ''}{format.format(r.max)}{r.unit === 'percent' ? ` ${m.percentagePoints}` : ''}</dd></div>)}</dl> : <p>{m.noComparable}</p>;
}
