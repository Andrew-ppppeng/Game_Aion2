'use client';

import {useSyncExternalStore} from 'react';
import type {Locale} from '@/i18n/routing';
import {optOutKey} from './site-analytics';

const copy = {
  en: {title: 'Usage statistics', label: 'Allow usage statistics and Google Analytics in this browser', note: 'Do Not Track and Global Privacy Control take precedence. Your saved character and budget tools work with statistics turned off.'},
  ja: {title: '利用統計', label: 'このブラウザーで利用統計とGoogle Analyticsを許可する', note: 'Do Not TrackとGlobal Privacy Controlの設定を優先します。統計をオフにしてもキャラクターや予算の保存は利用できます。'},
  es: {title: 'Estadísticas de uso', label: 'Permitir estadísticas de uso y Google Analytics en este navegador', note: 'Do Not Track y Global Privacy Control tienen prioridad. Los personajes y presupuestos guardados funcionan con las estadísticas desactivadas.'},
  de: {title: 'Nutzungsstatistik', label: 'Nutzungsstatistik und Google Analytics in diesem Browser erlauben', note: 'Do Not Track und Global Privacy Control haben Vorrang. Gespeicherte Charaktere und Budgets funktionieren auch ohne Statistik.'},
};
function subscribe(callback: () => void) {
  window.addEventListener('storage', callback); window.addEventListener('aion2-analytics-preference', callback);
  return () => {window.removeEventListener('storage', callback); window.removeEventListener('aion2-analytics-preference', callback);};
}
function enabled() {try {return localStorage.getItem(optOutKey) !== 'true';} catch {return false;}}
export function AnalyticsPreference({locale}: {locale: Locale}) {
  const value = useSyncExternalStore(subscribe, enabled, () => false);
  const m = copy[locale];
  return <section className="analytics-preference" aria-labelledby="analytics-preference-title">
    <h2 id="analytics-preference-title">{m.title}</h2>
    <label><input type="checkbox" checked={value} onChange={(event) => {
      try {
        localStorage.setItem(optOutKey, String(!event.target.checked));
        if (!event.target.checked) localStorage.removeItem('aion2-visit-state-v1');
      } catch { /* A restricted browser keeps statistics off. */ }
      window.dispatchEvent(new Event('aion2-analytics-preference'));
    }} /><span>{m.label}</span></label><p>{m.note}</p>
  </section>;
}
