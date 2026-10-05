'use client';

import Image from 'next/image';
import {Children, type ReactNode, useId, useState} from 'react';
import {ArrowDown, Check} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import identities from '@/content/class-identities.json';
import {classMediaMessages} from '@/i18n/class-media-messages';

export function GuideBuildMaps({locale, children}: {locale: Locale; children: ReactNode}) {
  const [selected, setSelected] = useState('gladiator');
  const id = useId();
  return <div className="build-skill-maps" data-build-maps>
    <label htmlFor={id}>{classMediaMessages[locale].classSelect}<select id={id} value={selected} onChange={(event) => setSelected(event.target.value)}>{identities.map((entry) => <option key={entry.id} value={entry.id}>{entry.names[locale]}</option>)}</select></label>
    {Children.map(children, (child, index) => <div hidden={identities[index].id !== selected} data-build-map-panel={identities[index].id}>{child}</div>)}
  </div>;
}

export function GuideSpecializationTree({locale, skillName, title, caption}: {locale: Locale; skillName: string; title: string; caption: string}) {
  const [selected, setSelected] = useState('mobile');
  const m = classMediaMessages[locale];
  const choices = [
    {id: 'speed', label: m.speed, text: m.speedText},
    {id: 'damage', label: m.damage, text: m.damageText},
    {id: 'mobile', label: m.mobile, text: m.mobileText},
  ];
  return <figure className="specialization-tree" data-specialization-tree>
    <figcaption><strong>{title}</strong><p>{caption}</p></figcaption>
    <div className="specialization-root"><Image src="/media/skills/15060000.webp" width={64} height={64} alt="" unoptimized /><strong>{skillName}</strong><span>{m.rank}</span></div>
    <ArrowDown size={30} aria-hidden="true" className="specialization-trunk" />
    <fieldset><legend>{m.option}</legend><div className="specialization-options">{choices.map((choice) => <label key={choice.id} className={selected === choice.id ? 'selected' : ''}>
      <input type="radio" name={`hellfire-${locale}`} value={choice.id} checked={selected === choice.id} onChange={() => setSelected(choice.id)} /><span><strong>{choice.label}</strong><span>{choice.text}</span></span>{selected === choice.id && <Check size={18} aria-hidden="true" />}
    </label>)}</div></fieldset>
    <p className="specialization-result" role="status"><strong>{m.selected}: {choices.find((choice) => choice.id === selected)!.label}.</strong> {m.rankNote}</p>
    <a className="specialization-image-link" href={`/media/guides/specialization-hellfire-${locale}.png`} target="_blank" rel="noopener">{m.fullImage}</a>
  </figure>;
}
