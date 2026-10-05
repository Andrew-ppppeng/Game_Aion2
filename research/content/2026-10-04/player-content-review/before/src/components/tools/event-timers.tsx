'use client';
import {useState, useSyncExternalStore} from 'react';
import type {Locale} from '@/i18n/routing';
import {toolMessages} from '@/i18n/tool-messages';
import {calendarFile, eventStatus} from '@/lib/aion2/model';
import type {EventRecord} from '@/lib/aion2/types';
import {useClock, useStored} from './local-store';

const noop = () => () => {};
const isIds = (value: unknown): value is string[] => Array.isArray(value) && value.every((v) => typeof v === 'string');
const emptyIds: string[] = [];
const isZone = (value: unknown): value is string => typeof value === 'string' && ['local', 'UTC', 'America/New_York', 'America/Los_Angeles', 'Europe/Berlin', 'America/Sao_Paulo', 'Asia/Tokyo', 'Asia/Shanghai'].includes(value);

export function EventTimers({events, locale, initialNow}: {events: EventRecord[]; locale: Locale; initialNow: number}) {
  const m = toolMessages[locale];
  const now = useClock(initialNow);
  const mounted = useSyncExternalStore(noop, () => true, () => false);
  const [selection, setSelection] = useStored('aion2-timezone-v1', 'local', isZone);
  const [claimed, setClaimed] = useStored('aion2-event-reminders-v1', emptyIds, isIds);
  const [error, setError] = useState('');
  const zone = selection === 'local' ? (mounted ? Intl.DateTimeFormat().resolvedOptions().timeZone : 'UTC') : selection;
  const format = (date: string) => new Intl.DateTimeFormat(locale, {dateStyle: 'medium', timeStyle: 'short', timeZone: zone}).format(new Date(date));
  const remaining = (date: string) => {const seconds = Math.max(0, Math.floor((Date.parse(date) - now) / 1000)); return `${Math.floor(seconds / 86400)}d ${String(Math.floor(seconds / 3600) % 24).padStart(2, '0')}:${String(Math.floor(seconds / 60) % 60).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}`;};
  function download(event: EventRecord) {
    const contents = calendarFile(event, event.titles[locale]);
    if (!contents) return;
    try {
      const url = URL.createObjectURL(new Blob([contents], {type: 'text/calendar;charset=utf-8'}));
      const anchor = document.createElement('a'); anchor.href = url; anchor.download = `${event.id}.ics`; anchor.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    } catch {setError(m.calendarError);}
  }
  return <section className="game-tool" data-event-timers>
    <h3>{m.timerTitle}</h3><p className="tool-note">{m.timerNote}</p>
    <label className="tool-field">{m.timezone}<select value={selection} onChange={(e) => setSelection(e.target.value)}>
      <option value="local">{m.localTimezone}</option>{['UTC', 'America/New_York', 'America/Los_Angeles', 'Europe/Berlin', 'America/Sao_Paulo', 'Asia/Tokyo', 'Asia/Shanghai'].map((tz) => <option key={tz}>{tz}</option>)}
    </select></label><p className="tool-note">{zone}</p>
    {events.map((event) => {
      const status = eventStatus(event, now);
      return <article className="event-card" key={event.id} data-event={event.id} data-event-status={status}>
        <div className="event-heading"><h4>{event.titles[locale]}</h4><span className={`tool-badge ${status}`}>{m[status]}</span></div>
        {event.startAt && <p>{m.start}: <time dateTime={event.startAt}>{format(event.startAt)}</time></p>}
        {event.endAt && <p>{m.end}: <time dateTime={event.endAt}>{format(event.endAt)}</time></p>}
        {status !== 'unconfirmed' && status !== 'ended' && <p className="event-countdown">{m.countdown}: <span>{remaining((status === 'upcoming' && !event.deadlineOnly ? event.startAt : event.endAt)!)}</span></p>}
        {event.dateRange && <p>{m.confirmedDates}: {event.dateRange}</p>}
        {(event.startAt || event.endAt) && <details><summary>{m.originalTime}</summary><p className="tool-note">{event.sourceTime}</p></details>}
        <p className="tool-source">Global · {m.checkedAt}: {event.checkedAt} · <a href={event.sourceUrl} target="_blank" rel="noopener noreferrer">{m.source} ↗</a></p>
        {event.startAt && event.endAt || event.deadlineOnly ? <button type="button" className="tool-button" onClick={() => download(event)}>{m.calendar}</button> : null}
        {event.topics.includes('twitch-drops') && <label className="tool-check"><input type="checkbox" checked={claimed.includes(event.id)} onChange={(e) => setClaimed(e.target.checked ? [...claimed.filter((id) => id !== event.id), event.id] : claimed.filter((id) => id !== event.id))} />{m.claimed}</label>}
      </article>;
    })}
    {events.some((e) => e.topics.includes('twitch-drops')) && <p className="tool-note">{m.claimNote}</p>}
    {error && <p role="alert">{error}</p>}
  </section>;
}
