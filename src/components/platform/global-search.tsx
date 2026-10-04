'use client';
import {useEffect, useRef, useState} from 'react';
import {Search, X} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import type {SearchEntry} from '@/lib/aion2/catalogue';
import {platformMessages} from '@/i18n/platform-messages';
export function GlobalSearch({entries, locale}: {entries: SearchEntry[]; locale: Locale}) {
  const m = platformMessages[locale];
  const dialog = useRef<HTMLDialogElement>(null);
  const input = useRef<HTMLInputElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);
  const [query, setQuery] = useState('');
  const [kind, setKind] = useState('all');
  function open() {dialog.current?.showModal(); input.current?.focus();}
  useEffect(() => {
    const keyboard = (event: KeyboardEvent) => {if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {event.preventDefault(); open();}};
    window.addEventListener('keydown', keyboard); return () => window.removeEventListener('keydown', keyboard);
  }, []);
  const matches = entries.filter((entry) => (kind === 'all' || kind === entry.kind) && `${entry.title} ${entry.text} ${entry.id}`.toLocaleLowerCase(locale).includes(query.trim().toLocaleLowerCase(locale))).slice(0, 30);
  return <><button type="button" ref={trigger} className="search-launcher" onClick={open} aria-label={m.search}><Search size={18} aria-hidden="true" /><span>{m.search}</span><kbd>⌘ K</kbd></button>
    <dialog ref={dialog} className="search-dialog" aria-labelledby="global-search-title" onClose={() => trigger.current?.focus()} onKeyDown={(e) => {if (e.key === 'Escape') {e.preventDefault(); dialog.current?.close();}}} onClick={(e) => {if (e.target === dialog.current) dialog.current.close();}}>
      <div className="platform-heading"><h2 id="global-search-title">{m.search}</h2><button className="tool-button" aria-label={m.close} onClick={() => dialog.current?.close()}><X size={18} /></button></div>
      <label className="tool-field"><span className="sr-only">{m.search}</span><input type="search" ref={input} value={query} onChange={(e) => setQuery(e.target.value)} placeholder={m.searchPlaceholder} /></label>
      <div className="search-tabs" role="group" aria-label={m.category}>{[['all', m.all], ['guide', m.guides], ['item', m.items], ['class', m.classes]].map(([id, label]) => <button type="button" className="tool-button" aria-pressed={kind === id} key={id} onClick={() => setKind(id)}>{label}</button>)}</div>
      <ul className="search-results">{matches.map((entry) => <li key={`${entry.kind}:${entry.id}`}><Link href={entry.href} prefetch={false} onClick={() => dialog.current?.close()}><strong>{entry.title}</strong><small>{m[entry.kind === 'guide' ? 'guides' : entry.kind === 'item' ? 'items' : 'classes']}</small></Link></li>)}</ul>
      {!matches.length && <p role="status">{m.noResults}</p>}
    </dialog></>;
}
