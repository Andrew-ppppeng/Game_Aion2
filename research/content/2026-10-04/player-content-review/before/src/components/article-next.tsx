import {ArrowRight} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';
import {getArticle} from '@/lib/articles';

export function ArticleNext({locale, slug, inline = false}: {locale: Locale; slug: string; inline?: boolean}) {
  const next = getArticle(locale, slug);
  if (!next) throw new Error(`Unknown next guide: ${slug}`);
  return <aside className={`article-next-card${inline ? ' inline-next' : ''}`} data-next-guide={slug}>
    <span>{guideMessages[locale].next}</span>
    <Link href={`/${slug}`}><strong>{next.metadata.title}</strong><ArrowRight size={18} aria-hidden="true" /></Link>
    <p>{next.metadata.summary}</p>
  </aside>;
}
