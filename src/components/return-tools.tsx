'use client';

import {useMemo, useSyncExternalStore} from 'react';
import {ArrowRight, Calculator, ListChecks, UserRound} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {completedGrowth, growthGoals} from '@/lib/growth-checklist';
import {useGrowthProgress} from './tools/growth-store';

const copy = {
  en: {title: 'Your player tools', note: 'Pick up where you left off. Saved progress stays in this browser.', character: 'Character lookup', budget: 'Material budget', checklist: 'First-session checklist', bookmarks: 'saved characters', saved: 'Saved plan', create: 'Plan your next upgrade', complete: 'complete', lookup: 'Find and bookmark your character'},
  ja: {title: 'プレイヤーツール', note: '前回の続きから。保存した内容はこのブラウザーに残ります。', character: 'キャラクター検索', budget: '素材の予算', checklist: '初回プレイのチェックリスト', bookmarks: '保存したキャラクター', saved: '保存した計画', create: '次の強化を計画', complete: '完了', lookup: 'キャラクターを検索して保存'},
  es: {title: 'Tus herramientas', note: 'Retoma tu progreso. Los datos guardados permanecen en este navegador.', character: 'Buscar personaje', budget: 'Presupuesto de materiales', checklist: 'Lista de la primera sesión', bookmarks: 'personajes guardados', saved: 'Plan guardado', create: 'Planifica tu próxima mejora', complete: 'completado', lookup: 'Busca y guarda tu personaje'},
  de: {title: 'Deine Spielerwerkzeuge', note: 'Mache dort weiter, wo du aufgehört hast. Gespeicherte Daten bleiben in diesem Browser.', character: 'Charaktersuche', budget: 'Materialbudget', checklist: 'Checkliste für die erste Sitzung', bookmarks: 'gespeicherte Charaktere', saved: 'Gespeicherter Plan', create: 'Plane deine nächste Verstärkung', complete: 'abgeschlossen', lookup: 'Finde und speichere deinen Charakter'},
};
function subscribe(callback: () => void) {
  const events = ['storage', 'aion2-tool-storage', 'aion-checklist'];
  events.forEach((name) => window.addEventListener(name, callback));
  return () => events.forEach((name) => window.removeEventListener(name, callback));
}
function stored(key: string) {try {return localStorage.getItem(key) || 'null';} catch {return 'null';}}
function parse(text: string): unknown {try {return JSON.parse(text);} catch {return null;}}

export function ReturnTools({locale, checklistIds}: {locale: Locale; checklistIds: string[]}) {
  const m = copy[locale];
  const growthCopy = {en: {title: 'Continue your growth', tools: 'All tools'}, ja: {title: '成長の続きを進める', tools: 'すべてのツール'}, es: {title: 'Continúa tu progreso', tools: 'Todas las herramientas'}, de: {title: 'Fortschritt fortsetzen', tools: 'Alle Werkzeuge'}}[locale];
  const {progress} = useGrowthProgress(checklistIds);
  const growthIds = [...checklistIds, ...growthGoals.map((goal) => goal.id)];
  const growthComplete = completedGrowth(progress, growthIds).size;
  const bookmarks = useSyncExternalStore(subscribe, () => stored('aion2-characters-v1'), () => 'null');
  const budget = useSyncExternalStore(subscribe, () => stored('aion2-budget-v1'), () => 'null');
  const checklist = useSyncExternalStore(subscribe, () => stored('aion2-checklist-v1:guide'), () => 'null');
  const state = useMemo(() => {
    const characters = parse(bookmarks);
    const plan = parse(budget);
    const selected = parse(checklist);
    return {
      count: Array.isArray(characters) ? characters.filter((c) => c && typeof c.name === 'string' && typeof c.id === 'string').slice(0, 30).length : 0,
      plan: !!plan && typeof plan === 'object' && 'rows' in plan && Array.isArray(plan.rows) && plan.rows.some((r) => r && typeof r.name === 'string' && r.name.trim()),
      completed: Array.isArray(selected) ? new Set(selected.filter((id) => checklistIds.includes(id))).size : 0,
    };
  }, [bookmarks, budget, checklist, checklistIds]);
  return <section className="player-tools" aria-labelledby="player-tools-title" data-return-tools>
    <div><h2 id="player-tools-title">{m.title}</h2><p>{m.note}</p></div>
    <div className="player-tools-grid">
      <Link href="/tools/growth-checklist" data-growth-resume><ListChecks size={20} aria-hidden="true" /><span><strong>{growthCopy.title}</strong><small>{growthComplete} / {growthIds.length} {m.complete}</small></span><ArrowRight size={17} aria-hidden="true" /></Link>
      <Link href="/tools/character"><UserRound size={20} aria-hidden="true" /><span><strong>{m.character}</strong><small>{state.count ? `${state.count} ${m.bookmarks}` : m.lookup}</small></span><ArrowRight size={17} aria-hidden="true" /></Link>
      <Link href="/monetization#material-budget"><Calculator size={20} aria-hidden="true" /><span><strong>{m.budget}</strong><small>{state.plan ? m.saved : m.create}</small></span><ArrowRight size={17} aria-hidden="true" /></Link>
    </div>
    <div className="return-tool-shortcuts"><Link href="/tools">{growthCopy.tools}<ArrowRight size={14} aria-hidden="true" /></Link><Link href="/guide#starter-checklist">{m.checklist}: {state.completed} / {checklistIds.length}</Link></div>
  </section>;
}
