'use client';

import {useState} from 'react';
import Image from 'next/image';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';
import type {GuideAsset} from '@/lib/article-types';
import identities from '@/content/class-identities.json';
import {GuideImage} from './guide-image';
import {GuideTable} from './guide-table';

type Role = 'all' | 'frontline' | 'melee' | 'ranged' | 'healing' | 'support';
type ClassAsset = Pick<GuideAsset, 'id' | 'src' | 'width' | 'height'>;

export function ClassIconTable({locale, assets}: {locale: Locale; assets: ClassAsset[]}) {
  const m = guideMessages[locale];
  return <section className="class-icon-reference" aria-label={m.iconTable}>
    <p>{m.iconNote}</p>
    <GuideTable><thead><tr><th scope="col">{m.classIcon}</th><th scope="col">{m.englishName}</th><th scope="col">{m.localName}</th></tr></thead>
      <tbody>{identities.map((entry) => {
        const emblem = assets.find((asset) => asset.id === `emblem-${entry.id}`);
        if (!emblem) throw new Error(`Missing class emblem: ${entry.id}`);
        return <tr key={entry.id} data-class-icon={entry.id}>
          <td><div className="class-icon-preview"><GuideImage src={emblem.src} width={emblem.width} height={emblem.height} alt={`${entry.names[locale]} — ${m.classIcon}`} locale={locale} /></div></td>
          <td lang="en">{entry.names.en}</td><td>{entry.names[locale]}</td>
        </tr>;
      })}</tbody>
    </GuideTable>
  </section>;
}

export function ClassFinder({locale, assets}: {locale: Locale; assets: ClassAsset[]}) {
  const [role, setRole] = useState<Role>('all');
  const m = guideMessages[locale];
  const visible = identities.filter((entry) => role === 'all' || entry.roles.includes(role));
  return <section className="class-finder" aria-label={m.roster}>
    <p className="class-finder-note">{m.classNote}</p>
    <fieldset><legend>{m.filter}</legend><div>{(['all', 'frontline', 'melee', 'ranged', 'healing', 'support'] as const).map((value) => <button key={value} type="button" aria-pressed={role === value} onClick={() => setRole(value)}>{m[value]}</button>)}</div></fieldset>
    <div className="class-card-grid" aria-live="polite">{visible.map((entry) => {
      const asset = assets.find((item) => item.id === `class-${entry.id}`)!;
      const emblem = assets.find((item) => item.id === `emblem-${entry.id}`)!;
      return <div className="class-guide-card" key={entry.id} data-class={entry.id}>
        <GuideImage src={asset.src} width={asset.width} height={asset.height} alt={entry.names[locale]} locale={locale} portrait />
        <h3><Image src={emblem.src} width={28} height={29} alt="" />{entry.names[locale]}</h3>
        <p>{entry.roles.map((value) => m[value as Exclude<Role, 'all'>]).join(' · ')}</p>
        {entry.href.startsWith('/') ? <Link href={entry.href}>{m.next} →</Link> : <a href={entry.href}>{m.inspect} ↓</a>}
      </div>;
    })}</div>
  </section>;
}
