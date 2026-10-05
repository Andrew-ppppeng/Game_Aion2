'use client';

import {useEffect, useRef, useState, type ComponentProps} from 'react';
import {useLocale} from 'next-intl';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';

export function GuideTable({tierComparison = false, ...props}: ComponentProps<'table'> & {tierComparison?: boolean}) {
  const ref = useRef<HTMLDivElement>(null);
  const [overflow, setOverflow] = useState(false);
  const locale = useLocale() as Locale;
  useEffect(() => {
    const element = ref.current;
    if (!element) return;
    const observer = new ResizeObserver(() => setOverflow(element.scrollWidth > element.clientWidth + 1));
    observer.observe(element);
    return () => observer.disconnect();
  }, []);
  return <div className="guide-table-block">
    <div className="mdx-table-wrap" ref={ref} tabIndex={overflow ? 0 : undefined} aria-label={overflow ? guideMessages[locale].swipe : undefined}><table {...props} data-tier-comparison={tierComparison || undefined} /></div>
    {overflow && <p className="guide-table-hint">↔ {guideMessages[locale].swipe}</p>}
  </div>;
}
