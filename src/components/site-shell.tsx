import Image from 'next/image';
import {ArrowUpRight, ExternalLink} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {sectionIds, sectionGroups, sectionPaths, playerToolLinks} from '@/lib/site-structure';
import {structureMessages} from '@/i18n/structure-messages';
import {isArticlePublished} from '@/lib/articles';
import {officialLinks, site} from '@/lib/site';
import {LanguageSwitcher} from './language-switcher';
import {PrimaryNavigation, SiteNavigation, type NavSection} from './site-navigation';

export function SiteShell({locale, children}: {locale: Locale; children: React.ReactNode}) {
  const m = getSiteMessages(locale);
  const official = officialLinks(locale);
  const editorialLabels = {en: ['Editorial policy', 'Corrections'], ja: ['編集方針', '訂正・連絡'], es: ['Política editorial', 'Correcciones'], de: ['Redaktionsrichtlinien', 'Korrekturen']}[locale];
  const structure = structureMessages[locale];
  const sections: NavSection[] = sectionIds.map((id) => ({id, label: structure.sections[id].title, href: sectionPaths[id], overview: structure.allTopics,
    groups: [
      ...(id === 'tools' ? [{id: 'playerTools', label: structure.ownTools, links: playerToolLinks.map((tool) => ({href: tool.href, title: structure.tools[tool.id].title}))}] : []),
      ...sectionGroups[id].map((group) => ({id: group.id, label: structure.groups[group.id], links: group.topics.filter((slug) => isArticlePublished(locale, slug) && slug !== 'classes').map((slug) => ({href: `/${slug}`, title: m.topics[slug]}))})),
      ...(id === 'resources' ? [{id: 'videos', label: m.ui.beginnerVideos, links: [{href: '/beginner-videos', title: m.ui.beginnerVideos}]}] : []),
    ],
  }));

  return (
    <>
      <a className="skip-link" href="#main-content">{m.ui.skipContent}</a>
      <header className="site-header">
        <Link href="/" className="brand" aria-label={m.footer.aboutTitle}>
          <Image src="/android-chrome-192x192.png" width={40} height={40} alt="" priority />
          <span className="brand-wordmark">{m.home.hero.title.slice(0, -1)}<span>{m.home.hero.title.slice(-1)}</span><small>WIKI</small></span>
        </Link>
        <PrimaryNavigation sections={sections} />
        <div className="header-actions">
          <LanguageSwitcher />
          <a href={site.steam} className="header-game-link" target="_blank" rel="noopener noreferrer">{m.footer.playGame}<ArrowUpRight size={15} aria-hidden="true" /></a>
        </div>
      </header>
      <SiteNavigation sections={sections} gameTitle={m.home.hero.title} />
      <div className="main-column">
        <main id="main-content" tabIndex={-1}>{children}</main>
        <footer className="site-footer">
          <div className="footer-grid">
            <div className="footer-about"><Link href="/" className="footer-brand">{m.home.hero.title} <span>WIKI</span></Link><p>{m.footer.about}</p></div>
            <div><h2>{m.ui.browse}</h2>{sections.map((section) => <Link key={section.id} href={section.href}>{section.label}</Link>)}</div>
            <div><h2>{m.ui.resources}</h2>{[
              [m.footer.playGame, site.steam], [m.footer.officialDiscord, site.discord],
              [m.footer.officialYoutube, site.youtube], [m.ui.characterLookup, official.characters],
            ].map(([label, href]) => <a href={href} key={href} target="_blank" rel="noopener noreferrer">{label}<ExternalLink size={11} aria-hidden="true" /></a>)}</div>
          </div>
          <div className="footer-bottom"><span>© {new Date().getUTCFullYear()} {m.footer.aboutTitle} · {m.ui.fanSite}</span><div><Link href="/privacy-policy">{m.footer.privacyPolicy}</Link><Link href="/terms-of-service">{m.footer.termsOfService}</Link><Link href="/terms-of-service#editorial-policy">{editorialLabels[0]}</Link><Link href="/terms-of-service#corrections">{editorialLabels[1]}</Link></div></div>
        </footer>
      </div>
    </>
  );
}
