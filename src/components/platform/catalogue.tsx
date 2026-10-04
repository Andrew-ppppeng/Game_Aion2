'use client';
import {useMemo, useState} from 'react';
import Image from 'next/image';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import type {CatalogueEntry} from '@/lib/aion2/catalogue';
import {regions, type Region} from '@/lib/aion2/types';
import {useStored} from '../tools/local-store';
import {ItemActions, StorageNotice} from './item-actions';
const validRegion = (value: unknown): value is Region => regions.includes(value as Region);
export function Catalogue({entries, locale}: {entries: CatalogueEntry[]; locale: Locale}) {
  const m = platformMessages[locale];
  const [region, setRegion] = useStored('aion2-region-v1', 'nae' as Region, validRegion);
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('');
  const [grade, setGrade] = useState('');
  const [className, setClassName] = useState('');
  const [maxLevel, setMaxLevel] = useState('');
  const [sort, setSort] = useState('name');
  const available = entries.filter((entry) => entry.regions.includes(region));
  const categories = [...new Set(available.map(({item}) => item.categoryName).filter(Boolean))];
  const grades = [...new Set(available.map(({item}) => item.gradeName || item.grade))];
  const classes = [...new Set(available.flatMap(({item}) => item.classNames || []))];
  const filtered = useMemo(() => available.filter(({item}) => (!category || item.categoryName === category) &&
    (!grade || (item.gradeName || item.grade) === grade) && (!className || !item.classNames?.length || item.classNames.includes(className)) &&
    (!maxLevel || item.equipLevel <= Number(maxLevel)) && `${item.name} ${item.id} ${item.categoryName || ''}`.toLocaleLowerCase(locale).includes(query.trim().toLocaleLowerCase(locale)))
    .sort((a, b) => sort === 'level' ? a.item.equipLevel - b.item.equipLevel || a.item.name.localeCompare(b.item.name, locale) : a.item.name.localeCompare(b.item.name, locale)),
  [available, category, grade, className, maxLevel, query, sort, locale]);
  return <section className="game-tool catalogue" aria-label={m.database} data-catalogue>
    <div className="platform-heading"><div><h2>{m.database}</h2><p>{m.catalogueIntro}</p></div><Link className="tool-link" href="/tools/compare">{m.compare} →</Link></div>
    <div className="catalogue-filters">
      <label className="tool-field catalogue-query">{m.search}<input type="search" value={query} onChange={(e) => setQuery(e.target.value)} placeholder={m.searchPlaceholder} /></label>
      <label className="tool-field">{m.region}<select aria-label={m.region} value={region} onChange={(e) => {setRegion(e.target.value as Region); setCategory(''); setGrade(''); setClassName('');}}>{regions.map((r) => <option key={r}>{r}</option>)}</select></label>
      <label className="tool-field">{m.category}<select aria-label={m.category} value={category} onChange={(e) => setCategory(e.target.value)}><option value="">{m.all}</option>{categories.map((c) => <option key={c}>{c}</option>)}</select></label>
      <label className="tool-field">{m.grade}<select aria-label={m.grade} value={grade} onChange={(e) => setGrade(e.target.value)}><option value="">{m.all}</option>{grades.map((g) => <option key={g}>{g}</option>)}</select></label>
      <label className="tool-field">{m.classes}<select aria-label={m.classes} value={className} onChange={(e) => setClassName(e.target.value)}><option value="">{m.all}</option>{classes.map((c) => <option key={c}>{c}</option>)}</select></label>
      <label className="tool-field">{m.maxLevel}<input type="number" min="0" max="999" value={maxLevel} onChange={(e) => setMaxLevel(e.target.value)} /></label>
      <label className="tool-field">{m.sort}<select aria-label={m.sort} value={sort} onChange={(e) => setSort(e.target.value)}><option value="name">{m.name}</option><option value="level">{m.level}</option></select></label>
    </div>
    <div className="tool-actions"><span role="status" aria-live="polite">{filtered.length} / {available.length} {m.results}</span><button className="tool-button" type="button" onClick={() => {setQuery(''); setCategory(''); setGrade(''); setClassName(''); setMaxLevel(''); setSort('name');}}>{m.clear}</button><Link href="/workspace" className="tool-link">{m.workspace} →</Link></div>
    {!available.length ? <p role="status">{m.unavailable}</p> : !filtered.length ? <p role="status">{m.noResults}</p> :
      <div className="catalogue-grid">{filtered.map(({item}) => <article className="catalogue-card" key={item.id} data-catalogue-item={item.id}>
        <Link href={`/database/items/${item.id}?region=${region}`} className="catalogue-item-heading"><Image src={item.icon?.startsWith('https://assets.playnccdn.com/') ? item.icon : '/favicon-32x32.png'} width={48} height={48} alt="" unoptimized /><div><h3>{item.name}</h3><span>{item.gradeName || item.grade} · {item.categoryName}</span></div></Link>
        <p>{m.level}: <strong>{item.equipLevel}</strong>{item.classNames?.length ? ` · ${item.classNames.join(', ')}` : ''}</p>
        <ItemActions item={{id: item.id, region}} locale={locale} />
      </article>)}</div>}
    <StorageNotice locale={locale} />
  </section>;
}
