'use client';
import {useEffect, useRef, useState} from 'react';
import {Bookmark, Target} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import {emptyWorkspace, refKey, validWorkspace, withRecent, workspaceKey, type ItemRef} from '@/lib/aion2/workspace';
import {useStored, useStorageFailure} from '../tools/local-store';
export function useWorkspace() {return useStored(workspaceKey, emptyWorkspace, validWorkspace);}
export function StorageNotice({locale, keys = [workspaceKey]}: {locale: Locale; keys?: string[]}) {
  const failed = useStorageFailure(keys);
  return <p className={failed ? 'tool-error' : 'tool-note'} role={failed ? 'status' : undefined}>{platformMessages[locale][failed ? 'session' : 'local']}</p>;
}
export function ItemActions({item, locale, recordRecent = false}: {item: ItemRef; locale: Locale; recordRecent?: boolean}) {
  const m = platformMessages[locale];
  const [workspace, save] = useWorkspace();
  const [message, setMessage] = useState('');
  const recorded = useRef('');
  const key = refKey(item);
  useEffect(() => {
    if (recordRecent && recorded.current !== key) {recorded.current = key; save(withRecent(workspace, item));}
  }, [recordRecent, key, item, workspace, save]);
  const favorite = workspace.favorites.some((i) => refKey(i) === key);
  const goal = workspace.goals.some((i) => refKey(i) === key);
  return <div className="item-actions">
    <button type="button" className="tool-button" aria-pressed={favorite} onClick={() => {
      if (!favorite && workspace.favorites.length >= 200) {setMessage(m.storageLimit); return;}
      save({...workspace, favorites: favorite ? workspace.favorites.filter((i) => refKey(i) !== key) : [...workspace.favorites, item]});
    }}><Bookmark size={15} aria-hidden="true" />{favorite ? m.unfavorite : m.favorite}</button>
    <button type="button" className="tool-button" aria-pressed={goal} onClick={() => {
      if (!goal && workspace.goals.length >= 100) {setMessage(m.storageLimit); return;}
      save({...workspace, goals: goal ? workspace.goals.filter((i) => refKey(i) !== key) : [...workspace.goals, {...item, done: false}]});
    }}><Target size={15} aria-hidden="true" />{m.goal}</button>
    {message && <span role="status">{message}</span>}
  </div>;
}
