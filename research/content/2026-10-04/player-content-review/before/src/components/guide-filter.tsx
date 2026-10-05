'use client';

import {useEffect, useId, useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';

export function GuideFilter({kind, locale}: {kind: 'faction' | 'region'; locale: Locale}) {
  const [value, setValue] = useState('all');
  const id = useId();
  const m = guideMessages[locale];
  const options = kind === 'faction' ? ['all', 'elyos', 'asmodians'] as const : ['all', 'eu', 'naWest', 'naEast', 'latam', 'asia'] as const;
  const selector = kind === 'faction' ? '[data-faction-section]' : '[data-region-section]';
  const dataKey = kind === 'faction' ? 'factionSection' : 'regionSection';
  function change(next: string) {
    setValue(next);
    for (const element of document.querySelectorAll<HTMLElement>(`.article-body ${selector}`)) {
      const group = element.dataset[dataKey];
      element.hidden = group === 'other' ? next === 'eu' : next !== 'all' && group !== next;
    }
    window.dispatchEvent(new Event('aion-guide-filter'));
  }
  useEffect(() => {
    function reveal(hashValue: string) {
      let hash: string;
      try {hash = decodeURIComponent(hashValue);} catch {return;}
      const target = document.getElementById(hash);
      const group = target?.closest<HTMLElement>(selector);
      if (!group || (!group.hidden && !group.querySelector('[hidden]'))) return;
      for (const element of document.querySelectorAll<HTMLElement>(`.article-body ${selector}`)) element.hidden = false;
      setValue('all');
      window.dispatchEvent(new Event('aion-guide-filter'));
      target?.scrollIntoView({block: 'start'});
    }
    const revealHash = () => reveal(location.hash.slice(1));
    const revealAnchor = (event: Event) => reveal((event as CustomEvent<string>).detail);
    window.addEventListener('hashchange', revealHash);
    window.addEventListener('aion-guide-anchor', revealAnchor);
    return () => {window.removeEventListener('hashchange', revealHash); window.removeEventListener('aion-guide-anchor', revealAnchor);};
  }, [selector]);
  return <div className="guide-filter" data-guide-filter={kind}><label htmlFor={id}>{m[kind]}</label><select id={id} value={value} onChange={(event) => change(event.target.value)}>{options.map((option) => <option key={option} value={option}>{m[option]}</option>)}</select></div>;
}
