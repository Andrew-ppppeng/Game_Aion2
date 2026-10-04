import Image from 'next/image';
import type {Locale} from '@/i18n/routing';
import {toolMessages} from '@/i18n/tool-messages';
import {formatStat} from '@/lib/aion2/model';
import type {Item, SourceMeta} from '@/lib/aion2/types';
import {itemPropertyMessages, platformMessages} from '@/i18n/platform-messages';

export function DataUpdated({meta, locale}: {meta: SourceMeta; locale: Locale}) {
  const m = toolMessages[locale];
  if (meta.freshness === 'snapshot') return null;
  return <p className="tool-source">{meta.freshness === 'stale' && <strong>{m.stale} · </strong>}Global · {meta.region.toUpperCase()} · {m.readAt}: <time dateTime={meta.fetchedAt}>{new Intl.DateTimeFormat(locale, {dateStyle: 'medium', timeStyle: 'short', timeZone: 'UTC'}).format(new Date(meta.fetchedAt))} UTC</time></p>;
}
export function ItemDetails({item, locale, meta, instance = false}: {item: Item; locale: Locale; meta?: SourceMeta | null; instance?: boolean}) {
  const m = toolMessages[locale];
  const p = itemPropertyMessages[locale];
  const icon = item.icon?.startsWith('https://assets.playnccdn.com/') ? item.icon : '/favicon-32x32.png';
  return <section className="item-card" data-item-id={item.id}>
    <div className="item-card-heading"><Image src={icon} width={42} height={42} unoptimized alt="" /><div><h4>{item.name}{item.enchantLevel > 0 ? ` +${item.enchantLevel}` : ''}</h4><span>{item.gradeName || item.grade} · {item.categoryName}</span></div></div>
    <dl className="item-requirements"><div><dt>{m.requiredLevel}</dt><dd>{item.equipLevel}</dd></div>{item.level !== undefined && <div><dt>{m.itemLevel}</dt><dd>{item.level}</dd></div>}
      {item.maxEnchantLevel !== undefined && <div><dt>{m.maxEnhancement}</dt><dd>+{item.maxEnchantLevel}</dd></div>}</dl>
    {item.classNames?.length ? <p className="tool-note">{m.class}: {item.classNames.join(', ')}</p> : null}
    <dl className="item-requirements">{item.raceName && <div><dt>{p.faction}</dt><dd>{item.raceName === 'All' ? platformMessages[locale].all : item.raceName}</dd></div>}{(['tradable','storable','decomposable'] as const).filter((key) => typeof item[key] === 'boolean').map((key) => <div key={key}><dt>{p[key]}</dt><dd>{item[key] ? p.yes : p.no}</dd></div>)}</dl>
    <h5>{m.baseAttributes}</h5><dl className="tool-stats">{item.mainStats.map((stat) => <div key={stat.id}><dt>{stat.name}</dt><dd>{formatStat(stat)}</dd></div>)}</dl>
    <details className="tool-details"><summary>{m.details}</summary>
      {item.subStats?.length ? <><h5>{instance ? m.rolled : item.subStatRandom ? m.pool : m.fixedSub}</h5>
        {!instance && item.subStatRandom && <p className="tool-note">{m.rolls}: {item.subStatCount ?? m.unknown}</p>}
        <dl className="tool-stats">{item.subStats.map((stat, index) => <div key={`${stat.id}-${index}`}><dt>{stat.name}</dt><dd>{formatStat(stat)}</dd></div>)}</dl></> : null}
      {(item.magicStoneSlotCount !== undefined || item.godStoneSlotCount !== undefined) && <p>{m.sockets}: {item.magicStoneSlotCount ?? m.unknown} / {item.godStoneSlotCount ?? m.unknown}</p>}
      {item.sources?.length ? <p>{m.sources}: {item.sources.join(', ')}</p> : null}
    </details>
    {meta && <DataUpdated meta={meta} locale={locale} />}
  </section>;
}
