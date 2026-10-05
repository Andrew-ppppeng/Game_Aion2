'use client';

import {useEffect, useRef, useState} from 'react';
import {List, ChevronDown} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';

export function ArticleToc({sections, title, locale}: {sections: {id: string; title: string}[]; title: string; locale: Locale}) {
  const [active, setActive] = useState(sections[0]?.id);
  const mobile = useRef<HTMLDetailsElement>(null);
  useEffect(() => {
    let frame = 0;
    function update() {
      frame = 0;
      let next = sections[0]?.id;
      const first = document.getElementById(sections[0]?.id);
      const offset = (parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0) + (first ? parseFloat(getComputedStyle(first).scrollMarginTop) || 0 : 0) + 8;
      for (const section of sections) {
        const element = document.getElementById(section.id);
        if (element && !element.closest('[hidden]') && element.getBoundingClientRect().top <= offset) next = section.id;
      }
      setActive(next);
    }
    const schedule = () => {if (!frame) frame = requestAnimationFrame(update);};
    schedule();
    window.addEventListener('scroll', schedule, {passive: true});
    window.addEventListener('hashchange', schedule);
    window.addEventListener('aion-guide-filter', schedule);
    return () => {cancelAnimationFrame(frame); window.removeEventListener('scroll', schedule); window.removeEventListener('hashchange', schedule); window.removeEventListener('aion-guide-filter', schedule);};
  }, [sections]);
  const links = <ol>{sections.map((section) => <li key={section.id}><a href={`#${section.id}`} aria-current={active === section.id ? 'location' : undefined} onClick={() => {
    setActive(section.id);
    window.dispatchEvent(new CustomEvent('aion-guide-anchor', {detail: section.id}));
    mobile.current?.removeAttribute('open');
  }}>{section.title}</a></li>)}</ol>;
  return <div className="article-toc-container">
    <nav className="article-toc article-toc-desktop" aria-label={title}><h2>{title}</h2>{links}</nav>
    <details className="article-toc article-toc-mobile" ref={mobile}>
      <summary><List size={17} aria-hidden="true" /><span>{guideMessages[locale].contents}</span><small>{sections.find((section) => section.id === active)?.title}</small><ChevronDown size={16} aria-hidden="true" /></summary>
      <nav aria-label={title}>{links}</nav>
    </details>
  </div>;
}
