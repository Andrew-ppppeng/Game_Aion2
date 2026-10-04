'use client';

import {useEffect, useRef, useState} from 'react';
import type {Locale} from '@/i18n/routing';
import type {ApiResult, Item} from '@/lib/aion2/types';
import {toolMessages} from '@/i18n/tool-messages';
import {ItemDetails} from './item-details';

export function MoreEquipment({locale, slug, count}: {locale: Locale; slug: string; count: number}) {
  const m = toolMessages[locale];
  const [items, setItems] = useState<ApiResult<Item>[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const controller = useRef<AbortController | null>(null);
  useEffect(() => () => controller.current?.abort(), []);
  async function load() {
    if (items || controller.current) return;
    const abort = new AbortController();
    controller.current = abort;
    setLoading(true); setError(false);
    try {
      const response = await fetch(`/api/aion2/equipment-examples?${new URLSearchParams({locale, slug})}`, {signal: abort.signal});
      if (!response.ok) throw new Error('unavailable');
      const result = await response.json() as {items: ApiResult<Item>[]};
      if (!Array.isArray(result.items) || result.items.some((item) => !item.data)) throw new Error('invalid-data');
      setItems(result.items);
    } catch {if (!abort.signal.aborted) setError(true);}
    finally {if (controller.current === abort) {controller.current = null; setLoading(false);}}
  }
  return <details className="tool-details" data-more-equipment onToggle={(event) => {if (event.currentTarget.open) void load();}}>
    <summary>{m.moreItems} ({count})</summary>
    {loading && <p role="status" className="tool-loading">{m.loading}</p>}
    {error && <div role="alert"><p className="tool-error">{m.unavailable}</p><button type="button" className="tool-button" onClick={() => void load()}>{m.retry}</button></div>}
    {items && <div className="item-grid">{items.map((entry) => <ItemDetails key={entry.data!.id} item={entry.data!} meta={entry.meta} locale={locale} />)}</div>}
  </details>;
}
