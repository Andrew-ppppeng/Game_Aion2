import {createHash} from 'node:crypto';
import type {Locale} from '@/i18n/routing';

/** Versioned URLs refresh social caches when the title or card layout changes. */
export function shareImagePath(locale: Locale, slug: string, title: string, revision = '') {
  const version = createHash('sha256').update(`2:${title}:${revision}`).digest('hex').slice(0, 12);
  return `/api/share/${locale}/${slug}?v=${version}`;
}
