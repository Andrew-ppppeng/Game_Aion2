'use client';

import {useCallback, useEffect, useRef} from 'react';
import {usePathname} from 'next/navigation';
import {useReportWebVitals} from 'next/web-vitals';
import type {Locale} from '@/i18n/routing';
import {returningVisit, type AnalyticsEvent} from '@/lib/analytics-model';

export const optOutKey = 'aion2-analytics-opt-out-v1';
export function analyticsAllowed() {
  if (process.env.NEXT_PUBLIC_ANALYTICS_ENABLED === 'false' || (process.env.NODE_ENV !== 'production' && process.env.NEXT_PUBLIC_ANALYTICS_ENABLED !== 'true')) return false;
  if (navigator.doNotTrack === '1' || (navigator as Navigator & {globalPrivacyControl?: boolean}).globalPrivacyControl) return false;
  try {return localStorage.getItem(optOutKey) !== 'true';} catch {return false;}
}
function pagePath(path: string) {return path.replace(/^\/(?:en|ja|es|de)(?=\/|$)/, '') || '/';}
const queue: AnalyticsEvent[] = [];
let timer: ReturnType<typeof setTimeout> | undefined;
function flush() {
  clearTimeout(timer); timer = undefined;
  if (!analyticsAllowed()) {queue.length = 0; return;}
  if (!queue.length) return;
  const body = JSON.stringify(queue.splice(0, 12));
  const blob = new Blob([body], {type: 'application/json'});
  if (!navigator.sendBeacon?.('/api/analytics', blob)) void fetch('/api/analytics', {method: 'POST', body, headers: {'Content-Type': 'application/json'}, keepalive: true, referrerPolicy: 'no-referrer'}).catch(() => {});
  if (queue.length) timer = setTimeout(flush, 2000);
}
function report(event: AnalyticsEvent) {
  if (!analyticsAllowed()) return;
  // Save mutations are debounced; never inspect or send the saved values.
  if (queue.some((old) => old.name === event.name && old.path === event.path && old.target === event.target && old.metric === event.metric && old.cohort === event.cohort)) return;
  queue.push(event);
  if (!timer) timer = setTimeout(flush, 2000);
}

export function SiteAnalytics({locale}: {locale: Locale}) {
  const pathname = usePathname();
  const initial = useRef({path: pagePath(pathname), locale});
  const reportMetric = useCallback((metric: {name: string; value: number}) => {
    if (metric.name === 'LCP' || metric.name === 'INP' || metric.name === 'CLS') report({name: 'web_vital', ...initial.current, metric: metric.name, value: metric.value});
  }, []);
  useReportWebVitals(reportMetric);
  useEffect(() => {
    const path = pagePath(pathname);
    const base = {path, locale};
    report({name: 'page_view', ...base});
    if (analyticsAllowed()) {
      try {
        const now = Date.now();
        const raw = JSON.parse(localStorage.getItem('aion2-visit-state-v1') || 'null');
        const valid = raw && Number.isFinite(raw.firstAt) && Number.isFinite(raw.lastAt) && raw.firstAt <= raw.lastAt && raw.lastAt <= now && typeof raw.returned === 'boolean' && ['en', 'ja', 'es', 'de'].includes(raw.locale) && typeof raw.path === 'string';
        const state = valid ? raw : {firstAt: now, lastAt: now, returned: false, ...base};
        if (!valid) {report({name: 'new_browser', ...base}); report({name: 'session_start', ...base});}
        else {
          if (now - state.lastAt >= 1800000) report({name: 'session_start', ...base});
          if (returningVisit(state, now)) {report({name: 'return_7d', path: state.path, locale: state.locale, cohort: new Date(state.firstAt).toISOString().slice(0, 10)}); state.returned = true;}
        }
        state.lastAt = now;
        localStorage.setItem('aion2-visit-state-v1', JSON.stringify(state));
      } catch { /* Storage restrictions leave page counting independent of retention. */ }
    }
    const send = (name: AnalyticsEvent['name'], target?: AnalyticsEvent['target']) => report({name, ...base, ...(target ? {target} : {})});
    function click(event: MouseEvent) {
      const element = event.target instanceof Element ? event.target : null;
      if (!element) return;
      if (element.closest('.article-next-card a, .article-related a')) send('next_guide_click');
      const action = element.closest('[data-analytics]')?.getAttribute('data-analytics');
      if (action === 'bookmark_save') send('bookmark_save', 'character');
      if (action === 'calendar') send('tool_use', 'calendar');
      if (element.closest('[data-more-equipment] > summary')) send('tool_use', 'equipment');
      const link = element.closest('a[href]');
      if (link) {
        const destination = new URL(link.getAttribute('href')!, location.origin);
        if (destination.origin === location.origin) {
          if (destination.pathname.endsWith('/tools/character')) send('tool_use', 'character');
          if (destination.hash === '#material-budget') send('tool_use', 'budget');
          if (destination.hash === '#starter-checklist') send('tool_use', 'checklist');
        }
      }
    }
    function submit(event: SubmitEvent) {
      const form = event.target instanceof Element ? event.target : null;
      if (form?.closest('[data-character-tool]')) send('tool_use', 'character');
      if (form?.closest('[data-budget-planner]')) send('tool_use', 'budget');
    }
    function changed(event: Event) {
      if ((event as CustomEvent<{key?: string}>).detail?.key === 'aion2-budget-v1') send('budget_save', 'budget');
    }
    const checklist = () => send('checklist_save', 'checklist');
    const hide = () => {if (document.visibilityState === 'hidden') flush();};
    document.addEventListener('click', click); document.addEventListener('submit', submit);
    document.addEventListener('visibilitychange', hide); window.addEventListener('pagehide', flush);
    window.addEventListener('aion2-tool-storage', changed); window.addEventListener('aion-checklist', checklist);
    return () => {
      document.removeEventListener('click', click); document.removeEventListener('submit', submit);
      document.removeEventListener('visibilitychange', hide); window.removeEventListener('pagehide', flush);
      window.removeEventListener('aion2-tool-storage', changed); window.removeEventListener('aion-checklist', checklist);
    };
  }, [pathname, locale]);
  return null;
}
