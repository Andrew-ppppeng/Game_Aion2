'use client';
import {useState} from 'react';
import type {Locale} from '@/i18n/routing';
import {toolMessages} from '@/i18n/tool-messages';
import {budget} from '@/lib/aion2/model';
import {useStored} from './local-store';
import {StorageNotice} from '../platform/item-actions';

type Row = {name: string; quantity: string; owned: string; price: string};
type Plan = {mode: 'craft' | 'enhance'; goal: string; yield: string; fee: string; rows: Row[]};
const emptyRow: Row = {name: '', quantity: '', owned: '', price: ''};
const initial: Plan = {mode: 'craft', goal: '', yield: '', fee: '', rows: [{...emptyRow}]};
function valid(value: unknown): value is Plan {
  if (!value || typeof value !== 'object') return false;
  const p = value as Plan;
  return ['craft', 'enhance'].includes(p.mode) && ['goal', 'yield', 'fee'].every((k) => typeof p[k as 'goal'] === 'string') && Array.isArray(p.rows) && p.rows.length > 0 && p.rows.length <= 20
    && p.rows.every((r) => r && ['name', 'quantity', 'owned', 'price'].every((k) => typeof r[k as keyof Row] === 'string'));
}
export function BudgetPlanner({locale}: {locale: Locale}) {
  const m = toolMessages[locale];
  const [plan, save] = useStored('aion2-budget-v1', initial, valid);
  const [submitted, setSubmitted] = useState(false);
  const format = new Intl.NumberFormat(locale, {maximumFractionDigits: 2});
  let result: ReturnType<typeof budget> | null = null;
  try {
    const fields = [plan.goal, plan.fee, ...(plan.mode === 'craft' ? [plan.yield] : []), ...plan.rows.flatMap((r) => [r.quantity, r.owned, r.price])];
    if (fields.some((s) => !s.trim() || !/^\d+(?:\.\d+)?$/.test(s)) || plan.rows.some((r) => !r.name.trim()) ||
      ![Number(plan.goal), ...(plan.mode === 'craft' ? [Number(plan.yield)] : []), ...plan.rows.flatMap((r) => [Number(r.quantity), Number(r.owned)])].every(Number.isSafeInteger)) throw new Error();
    result = budget(Number(plan.goal), plan.mode === 'craft' ? Number(plan.yield) : 1, Number(plan.fee), plan.rows.map((r) => ({quantity: Number(r.quantity), owned: Number(r.owned), price: Number(r.price)})));
  } catch {result = null;}
  function row(index: number, field: keyof Row, value: string) {save({...plan, rows: plan.rows.map((r, i) => i === index ? {...r, [field]: value} : r)});}
  return <section className="game-tool" id="material-budget" data-budget-planner>
    <h3>{m.budgetTitle}</h3><p className="tool-note">{m.budgetNote}</p>
    <form onSubmit={(e) => {e.preventDefault(); setSubmitted(true);}}>
      <div className="tool-tabs" role="group" aria-label={m.budgetTitle}>
        <button className="tool-button" type="button" aria-pressed={plan.mode === 'craft'} onClick={() => {save({...plan, mode: 'craft'}); setSubmitted(false);}}>{m.craft}</button>
        <button className="tool-button" type="button" aria-pressed={plan.mode === 'enhance'} onClick={() => {save({...plan, mode: 'enhance'}); setSubmitted(false);}}>{m.enhance}</button>
      </div>
      <div className="tool-form-grid">
        <label className="tool-field">{plan.mode === 'craft' ? m.goal : m.attempts}<input type="number" min="1" max="1000000000" step="1" required value={plan.goal} onChange={(e) => save({...plan, goal: e.target.value})} /></label>
        {plan.mode === 'craft' && <label className="tool-field">{m.yield}<input type="number" min="1" max="1000000000" step="1" required value={plan.yield} onChange={(e) => save({...plan, yield: e.target.value})} /></label>}
        <label className="tool-field">{m.fee}<input type="number" min="0" max="1000000000" step="any" required value={plan.fee} onChange={(e) => save({...plan, fee: e.target.value})} /></label>
      </div>
      {plan.rows.map((r, index) => <fieldset className="budget-row" key={index}><legend>{m.material} {index + 1}</legend>
        <label className="tool-field">{m.material}<input maxLength={80} required value={r.name} onChange={(e) => row(index, 'name', e.target.value)} /></label>
        {(['quantity', 'owned', 'price'] as const).map((field) => <label key={field} className="tool-field">{m[field]}<input type="number" min="0" max="1000000000" step={field === 'price' ? 'any' : '1'} required value={r[field]} onChange={(e) => row(index, field, e.target.value)} /></label>)}
        {plan.rows.length > 1 && <button className="tool-button" type="button" onClick={() => save({...plan, rows: plan.rows.filter((_, i) => i !== index)})}>{m.remove}</button>}
      </fieldset>)}
      <div className="tool-actions"><button type="button" className="tool-button" disabled={plan.rows.length >= 20} onClick={() => save({...plan, rows: [...plan.rows, {...emptyRow}]})}>{m.addMaterial}</button>
        <button type="submit" className="tool-button primary">{m.calculate}</button><button type="button" className="tool-button" onClick={() => {save(initial); setSubmitted(false);}}>{m.clear}</button></div>
    </form>
    {submitted && !result && <p role="alert" className="tool-error">{m.budgetInvalid}</p>}
    {submitted && result && <div className="budget-result" role="status"><p><strong>{m.attempts}: {format.format(result.attempts)}</strong></p>
      <div className="tool-table-scroll"><table><thead><tr><th>{m.material}</th><th>{m.required}</th><th>{m.missing}</th><th>Kina</th></tr></thead>
        <tbody>{result.rows.map((r, i) => <tr key={i}><td>{plan.rows[i].name}</td><td>{format.format(r.required)}</td><td>{format.format(r.missing)}</td><td>{format.format(r.cost)}</td></tr>)}</tbody></table></div>
      <p className="budget-total">{m.total}: <strong>{format.format(result.total)}</strong></p></div>}
    <StorageNotice locale={locale} keys={['aion2-budget-v1']} />
  </section>;
}
