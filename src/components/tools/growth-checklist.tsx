'use client';

import {useEffect, useMemo, useState, useSyncExternalStore} from 'react';
import {ArrowRight, RotateCcw} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {structureMessages} from '@/i18n/structure-messages';
import {completedGrowth, emptyGrowth, toggleGrowth, type GrowthGoal} from '@/lib/growth-checklist';
import {useGrowthProgress} from './growth-store';

const subscribeReady = () => () => {};

export function GrowthChecklist({locale, goals}: {locale: Locale; goals: GrowthGoal[]}) {
  const m = structureMessages[locale].growth;
  const starterIds = useMemo(() => goals.filter((goal) => goal.stage === 0).map((goal) => goal.id), [goals]);
  const {progress, save, initialize, temporary} = useGrowthProgress(starterIds);
  const [confirming, setConfirming] = useState(false);
  const ready = useSyncExternalStore(subscribeReady, () => true, () => false);
  useEffect(() => {initialize();}, [initialize]);
  const completed = completedGrowth(progress, goals.map((goal) => goal.id));
  const next = goals.find((goal) => !completed.has(goal.id));
  return <div data-growth-checklist>
    <section className="growth-overview" aria-label={m.title}>
      <div className="growth-total" role="status" aria-live="polite"><strong>{completed.size} / {goals.length}</strong><span>{m.complete}</span></div>
      <progress value={completed.size} max={goals.length} aria-label={m.title} />
      {ready && <p className="tool-note" data-growth-storage>{temporary ? m.temporary : m.saved}</p>}
      <div className="growth-next" data-growth-next>{next ? <><span>{m.next}</span><Link href={`#goal-${next.id}`}>{next.label}<ArrowRight size={17} aria-hidden="true" /></Link></> : <p>{m.finished}</p>}</div>
      <div className="growth-reset">
        {!confirming ? <button className="tool-button" type="button" disabled={!ready} onClick={() => setConfirming(true)}><RotateCcw size={15} aria-hidden="true" />{m.reset}</button> : <div role="group" aria-label={m.confirmReset}>
          <p>{m.confirmReset}</p><div className="tool-actions"><button className="tool-button" type="button" onClick={() => {save({...emptyGrowth, completedIds: []}); setConfirming(false);}} data-growth-reset-confirm>{m.confirm}</button><button className="tool-button" type="button" onClick={() => setConfirming(false)} data-growth-reset-cancel>{m.cancel}</button></div>
        </div>}
      </div>
    </section>
    {m.stages.map((title, index) => {
      const stage = goals.filter((goal) => goal.stage === index);
      const count = stage.filter((goal) => completed.has(goal.id)).length;
      return <section className="growth-stage" key={index} aria-labelledby={`growth-stage-${index}`} data-growth-stage={index}>
        <div className="growth-stage-heading"><div><span className="eyebrow">0{index + 1}</span><h2 id={`growth-stage-${index}`}>{title}</h2></div><span>{count} / {stage.length}</span></div>
        <progress value={count} max={stage.length} aria-label={title} />
        <ul>{stage.map((goal) => <li key={goal.id} id={`goal-${goal.id}`} data-growth-goal={goal.id}>
          <label><input type="checkbox" disabled={!ready} checked={completed.has(goal.id)} onChange={(event) => save(toggleGrowth(progress, goal.id, event.target.checked))} /><span>{goal.label}</span></label>
          {goal.condition && <p>{goal.condition}</p>}
          <Link href={goal.href}>{structureMessages[locale].readGuide}<ArrowRight size={14} aria-hidden="true" /></Link>
        </li>)}</ul>
      </section>;
    })}
  </div>;
}
