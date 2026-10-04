import 'server-only';
import type {Locale} from '@/i18n/routing';
import {getArticle} from '@/lib/articles';
import {topics} from '@/lib/topics';
import {curatedIds, snapshotItem} from './data';
import {regions, type Item, type Region} from './types';
import identities from '@/content/class-identities.json';

export type CatalogueEntry = {item: Item; regions: Region[]};
export type SearchEntry = {id: string; title: string; href: string; kind: 'guide' | 'item' | 'class'; text: string};
export function catalogue(locale: Locale): CatalogueEntry[] {
  return curatedIds.map((id) => ({item: snapshotItem(id, locale).data!, regions: regions.filter((region) => {
    try {return !!snapshotItem(id, locale, region).data;} catch {return false;}
  })}));
}
export function searchIndex(locale: Locale): SearchEntry[] {
  const guides = topics.flatMap((topic): SearchEntry[] => {
    const article = getArticle(locale, topic.slug);
    return article ? [{id: topic.slug, title: article.metadata.title, href: `/${topic.slug}`, kind: 'guide', text: article.metadata.description}] : [];
  });
  const classes = identities.map((c): SearchEntry => ({id: c.id, title: c.names[locale], href: getArticle(locale, c.id) ? `/${c.id}` : '/classes', kind: 'class', text: Object.values(c.names).join(' ')}));
  return [...guides, ...classes, ...catalogue(locale).map(({item}): SearchEntry => ({id: String(item.id), title: item.name,
    href: `/database/items/${item.id}`, kind: 'item', text: [item.categoryName, item.gradeName, ...(item.classNames || [])].filter(Boolean).join(' ')}))];
}
