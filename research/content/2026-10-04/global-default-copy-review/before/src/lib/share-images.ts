import {createHash} from 'node:crypto';
import type {Locale} from '@/i18n/routing';

/** Content-versioned URLs prevent social caches retaining an old article title. */
export function shareImagePath(locale: Locale, slug: string, title: string, revision = '') {
  const version = createHash('sha256').update(`${title}:${revision}`).digest('hex').slice(0, 12);
  return `/api/share/${locale}/${slug}?v=${version}`;
}
