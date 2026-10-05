import Image from 'next/image';
import {ArrowUpRight, ExternalLink} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {topicGroups} from '@/lib/topics';
import {isArticlePublished} from '@/lib/articles';
import {officialLinks, site} from '@/lib/site';
import {LanguageSwitcher} from './language-switcher';
import {SiteNavigation} from './site-navigation';

export function SiteShell({locale, children}: {locale: Locale; children: React.ReactNode}) {
  const m = getSiteMessages(locale);
  const official = officialLinks(locale);
  const groups = topicGroups.map((group) => ({
    id: group.id,
    label: m.categories[group.id],
    topics: group.topics.map((topic) => ({slug: topic.slug, title: m.topics[topic.slug], published: isArticlePublished(locale, topic.slug)})),
  }));

  return (
    <>
      <a className="skip-link" href="#main-content">{m.ui.skipContent}</a>
      <header className="site-header">
        <Link href="/" className="brand" aria-label={m.footer.aboutTitle}>
          <Image src="/android-chrome-192x192.png" width={40} height={40} alt="" priority />
          <span className="brand-wordmark">{m.home.hero.title.slice(0, -1)}<span>{m.home.hero.title.slice(-1)}</span><small>WIKI</small></span>
        </Link>
        <div className="header-tagline"><span className="header-divider" />{m.ui.community}</div>
        <div className="header-actions">
          <span className="edition-label"><span aria-hidden="true" />{m.ui.edition}</span>
          <LanguageSwitcher />
          <a href={site.steam} className="header-game-link" target="_blank" rel="noopener noreferrer">{m.footer.playGame}<ArrowUpRight size={15} aria-hidden="true" /></a>
        </div>
      </header>
      <SiteNavigation groups={groups} gameTitle={m.home.hero.title} />
      <div className="main-column">
        <main id="main-content" tabIndex={-1}>{children}</main>
        <footer className="site-footer">
          <div className="footer-grid">
            <div className="footer-about"><Link href="/" className="footer-brand">{m.home.hero.title} <span>WIKI</span></Link><p>{m.footer.about}</p></div>
            <div><h2>{m.ui.allGuides}</h2><Link href="/guide">{m.topics.guide}</Link><Link href="/classes">{m.topics.classes}</Link><Link href="/leveling">{m.topics.leveling}</Link><Link href="/pvp">{m.topics.pvp}</Link></div>
            <div><h2>{m.ui.resources}</h2>{[
              [m.footer.playGame, site.steam], [m.footer.officialDiscord, site.discord],
              [m.footer.officialYoutube, site.youtube], [m.ui.characterLookup, official.characters],
            ].map(([label, href]) => <a href={href} key={href} target="_blank" rel="noopener noreferrer">{label}<ExternalLink size={11} aria-hidden="true" /></a>)}</div>
          </div>
          <div className="footer-bottom"><span>© {new Date().getUTCFullYear()} {m.footer.aboutTitle} · {m.ui.fanSite}</span><div><Link href="/privacy-policy">{m.footer.privacyPolicy}</Link><Link href="/terms-of-service">{m.footer.termsOfService}</Link></div></div>
        </footer>
      </div>
    </>
  );
}
