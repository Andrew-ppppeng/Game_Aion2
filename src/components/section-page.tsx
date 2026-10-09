import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {structureMessages} from '@/i18n/structure-messages';
import type {SectionId} from '@/lib/site-structure';
import {SectionDirectory, ToolsDirectory} from './section-directory';

export function SectionPage({locale, section}: {locale: Locale; section: SectionId}) {
  const m = structureMessages[locale].sections[section];
  return <article className="tools-page hub-page" data-section-page={section}>
    <nav className="breadcrumbs" aria-label={getSiteMessages(locale).ui.navLabel}><Link href="/">{getSiteMessages(locale).ui.home}</Link><span aria-hidden="true">/</span><span>{m.title}</span></nav>
    <header className="article-header"><h1>{m.title}</h1><p>{m.description}</p></header>
    {section === 'tools' ? <ToolsDirectory locale={locale} /> : <SectionDirectory locale={locale} section={section} />}
  </article>;
}
