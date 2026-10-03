import Image from 'next/image';
import {ArrowRight, ArrowUpRight, BookOpen, Clock3, Compass, Feather, Gem, Play, Shield, Swords} from 'lucide-react';
import {getLocale} from 'next-intl/server';
import {Link} from '@/i18n/navigation';
import {getSiteMessages} from '@/i18n/messages';
import type {Locale} from '@/i18n/routing';
import {officialLinks, site} from '@/lib/site';
import {isArticlePublished} from '@/lib/articles';

async function messages() {
  return getSiteMessages(await getLocale() as Locale);
}

export async function Hero() {
  const m = await messages();
  const h = m.home.hero;
  return <>
    <section className="hero" aria-labelledby="hero-title">
      <Image className="hero-image" src="/media/hero.jpg" alt="" fill priority sizes="(min-width: 1024px) calc(100vw - 248px), 100vw" />
      <div className="hero-shade" />
      <div className="hero-content">
        <div className="hero-eyebrow"><span aria-hidden="true" />{h.eyebrow}</div>
        <h1 id="hero-title">{h.title.slice(0, -1)}<span>{h.title.slice(-1)}</span></h1>
        <p className="hero-description">{h.description}</p>
        <div className="hero-buttons">
          <Link href="/guide" className="button button-primary"><BookOpen size={16} aria-hidden="true" />{h.primaryCta}<ArrowRight size={15} aria-hidden="true" /></Link>
          <Link href="/classes" className="button button-secondary">{h.secondaryCta}<ArrowUpRight size={15} aria-hidden="true" /></Link>
        </div>
        <Link href="/code" className="hero-code-link">{h.tertiaryCta}<ArrowRight size={13} aria-hidden="true" /></Link>
        <div className="hero-stats">{h.stats.slice(2).map((stat) => <div key={stat}><strong>{stat.match(/^\d+/)?.[0]}</strong><span>{stat.replace(/^\d+[- ]?/, '')}</span></div>)}</div>
      </div>
      <a className="hero-trailer" href={site.steam} target="_blank" rel="noopener noreferrer"><span className="play-circle"><Play size={17} fill="currentColor" aria-hidden="true" /></span><span>{h.videoLabel}<small>STEAM <ArrowUpRight size={10} aria-hidden="true" /></small></span></a>
      <span className="hero-image-credit" aria-hidden="true">ATREIA · NC</span>
    </section>
    <div className="announcement-strip">
      <a href={site.launchAnnouncement} target="_blank" rel="noopener noreferrer"><span className="announcement-dot" aria-hidden="true" /><span>{m.ui.launchLabel}<strong>{m.home.aboutGame.stats[3].value}</strong></span><ArrowUpRight size={13} aria-hidden="true" /></a>
      <a href={site.maintenanceAnnouncement} target="_blank" rel="noopener noreferrer" title={m.ui.maintenanceLabel}><Clock3 size={15} aria-hidden="true" /><span>{h.stats[1]}</span><ArrowUpRight size={13} aria-hidden="true" /></a>
    </div>
  </>;
}

const journeyRoutes = ['/guide', '/classes', '/leveling', '/pvp'];
const journeyIcons = [Compass, Swords, Gem, Shield];

export async function Journey() {
  const m = await messages();
  const locale = await getLocale() as Locale;
  return <section className="content-section journey-section" id="journey" aria-labelledby="journey-title">
    <div className="section-topline"><span className="eyebrow">{m.home.start.eyebrow}</span><span className="section-index">01 /</span></div>
    <div className="section-heading"><div><h2 id="journey-title">{m.home.start.title}</h2><p>{m.ui.journeyDescription}</p></div><span className="section-decoration" aria-hidden="true">✧</span></div>
    <div className="journey-grid">{m.home.start.cards.map((card, index) => {
      const Icon = journeyIcons[index];
      return <Link key={card.number} href={journeyRoutes[index]} className={`journey-card journey-card-${index + 1}`}>
        <div className="journey-card-top"><span className="journey-icon"><Icon size={22} strokeWidth={1.5} aria-hidden="true" /></span><span className="journey-number" aria-hidden="true">0{card.number}</span></div>
        <h3>{card.title}</h3><p>{card.description}</p>
        <div className="journey-card-bottom"><span>{m.ui.openGuide}<ArrowRight size={14} aria-hidden="true" /></span>{!isArticlePublished(locale, journeyRoutes[index].slice(1)) && <span className="coming-soon-badge">{m.ui.comingSoon}</span>}</div>
      </Link>;
    })}</div>
  </section>;
}

export async function AboutGame() {
  const m = await messages();
  const about = m.home.aboutGame;
  return <section className="content-section about-section" aria-labelledby="about-title">
    <div className="section-topline"><span className="eyebrow">{m.ui.aboutEyebrow}</span><span className="section-index">02 /</span></div>
    <div className="about-grid">
      <div className="about-copy"><h2 id="about-title">{about.title}</h2>{about.paragraphs.map((paragraph) => <p key={paragraph}>{paragraph}</p>)}<Link href="/#journey" className="text-link">{about.cta}<ArrowRight size={15} aria-hidden="true" /></Link></div>
      <div className="game-facts"><h3><Feather size={17} aria-hidden="true" />{m.ui.quickFacts}</h3><dl>{about.stats.map((stat) => <div key={stat.label}><dt>{stat.label}</dt><dd>{stat.value}</dd></div>)}</dl><div className="facts-region-note"><span aria-hidden="true" />{m.ui.globalNotice}</div></div>
    </div>
    <div className="about-visual"><Image src="/media/atreia.jpg" alt="" fill sizes="(min-width: 1024px) calc(100vw - 328px), calc(100vw - 40px)" /><div className="about-visual-shade" /><span>{m.footer.description}</span></div>
  </section>;
}

export async function FinalCta() {
  const locale = await getLocale() as Locale;
  const m = getSiteMessages(locale);
  const cta = m.home.finalCta;
  return <section className="final-cta" aria-labelledby="cta-title"><Feather className="cta-feather" size={180} strokeWidth={0.6} aria-hidden="true" /><div><span className="eyebrow">{m.home.hero.title} · GLOBAL</span><h2 id="cta-title">{cta.title}</h2><p>{cta.description}</p></div><div className="cta-actions"><Link href="/guide" className="button button-primary">{cta.primary}<ArrowRight size={15} aria-hidden="true" /></Link><a href={officialLinks(locale).official} target="_blank" rel="noopener noreferrer" className="cta-official-link">{cta.secondary}<ArrowUpRight size={14} aria-hidden="true" /></a></div></section>;
}
