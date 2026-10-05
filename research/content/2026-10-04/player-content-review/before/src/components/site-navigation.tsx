'use client';

import {useEffect, useRef, useState} from 'react';
import {
  ArrowUpRight, BookOpen, ChevronDown, Coins, Download, Gift, Home, Layers3, ChartNoAxesCombined,
  Map, Menu, Monitor, Server, Sparkles, Swords, Ticket, WandSparkles, X, Flag, Keyboard, UserRound, Calculator, ListChecks,
} from 'lucide-react';
import {useTranslations} from 'next-intl';
import {Link, usePathname} from '@/i18n/navigation';
import type {CategoryId, TopicSlug} from '@/lib/topics';
import {CouponCard} from './coupon-card';

export type NavGroup = {
  id: CategoryId;
  label: string;
  topics: {slug: TopicSlug; title: string; published: boolean}[];
};

const icons = {
  guide: BookOpen,
  classSelection: Layers3,
  maps: Map,
  codes: Ticket,
  characterCustomization: Sparkles,
  pvp: Swords,
  buildsAndSkills: WandSparkles,
  twitchRewards: Gift,
  servers: Server,
  platforms: Monitor,
  installationAndControls: Download,
  monetizationAndTrading: Coins,
  damageMeters: ChartNoAxesCombined,
  playerStatistics: ChartNoAxesCombined,
  factions: Flag,
  macros: Keyboard,
};

function NavigationContent({groups, onNavigate}: {groups: NavGroup[]; onNavigate?: () => void}) {
  const pathname = usePathname();
  const t = useTranslations('ui');
  const complete = groups.every((group) => group.topics.every((topic) => topic.published));
  const publishedCount = groups.reduce((count, group) => count + group.topics.filter((topic) => topic.published).length, 0);

  return (
    <>
      <div className="sidebar-scroll">
        <nav aria-label={t('navLabel')} id={onNavigate ? undefined : 'guides'}>
          <Link className={`nav-home ${pathname === '/' ? 'active' : ''}`} href="/" aria-current={pathname === '/' ? 'page' : undefined} onClick={onNavigate}>
            <Home size={17} aria-hidden="true" />{t('home')}
            <span className="nav-active-dot" aria-hidden="true" />
          </Link>
          <p className="nav-overline">{t('playerTools')}</p>
          <Link className={`nav-single ${pathname === '/tools/character' ? 'active' : ''}`} href="/tools/character" aria-current={pathname === '/tools/character' ? 'page' : undefined} onClick={onNavigate}><UserRound size={16} aria-hidden="true" /><span>{t('characterLookup')}</span></Link>
          <Link className="nav-single" href="/monetization#material-budget" onClick={onNavigate}><Calculator size={16} aria-hidden="true" /><span>{t('materialBudget')}</span></Link>
          <Link className="nav-single" href="/guide#starter-checklist" onClick={onNavigate}><ListChecks size={16} aria-hidden="true" /><span>{t('starterChecklist')}</span></Link>
          <p className="nav-overline">{t('browse')}</p>
          {groups.map((group) => {
            const Icon = icons[group.id];
            const active = group.topics.some((topic) => pathname === `/${topic.slug}`);
            if (group.topics.length === 1) {
              const topic = group.topics[0];
              return (
                <Link key={group.id} href={`/${topic.slug}`} className={`nav-single ${active ? 'active' : ''}`} aria-current={active ? 'page' : undefined} onClick={onNavigate} title={topic.published ? topic.title : `${topic.title} · ${t('comingSoon')}`}>
                  <Icon size={16} aria-hidden="true" /><span>{group.label}</span><ArrowUpRight size={12} aria-hidden="true" />
                </Link>
              );
            }
            return (
              <details className="nav-group" key={group.id} open>
                <summary><Icon size={16} aria-hidden="true" /><span>{group.label}</span><ChevronDown size={13} className="nav-chevron" aria-hidden="true" /></summary>
                <div className="nav-topics">
                  {group.topics.map((topic) => (
                    <Link key={topic.slug} href={`/${topic.slug}`} onClick={onNavigate} className={pathname === `/${topic.slug}` ? 'active' : ''} aria-current={pathname === `/${topic.slug}` ? 'page' : undefined} title={topic.published ? topic.title : t('comingSoon')}>
                      <span>{topic.title}</span><span className="topic-dot" aria-hidden="true" />
                    </Link>
                  ))}
                </div>
              </details>
            );
          })}
        </nav>
      </div>
      <div className="sidebar-bottom">
        <CouponCard />
        <p className="sidebar-status"><span aria-hidden="true" />{complete ? t('contentReady', {count: publishedCount}) : t('contentStatus')}</p>
      </div>
    </>
  );
}

export function SiteNavigation({groups, gameTitle}: {groups: NavGroup[]; gameTitle: string}) {
  const t = useTranslations('ui');
  const dialog = useRef<HTMLDialogElement>(null);
  const [open, setOpen] = useState(false);

  function closeMenu() {
    dialog.current?.close();
  }

  useEffect(() => {
    const media = window.matchMedia('(min-width: 1024px)');
    const closeOnDesktop = () => {if (media.matches) dialog.current?.close();};
    media.addEventListener('change', closeOnDesktop);
    return () => media.removeEventListener('change', closeOnDesktop);
  }, []);

  useEffect(() => {
    if (!open) return;
    const previous = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {document.body.style.overflow = previous;};
  }, [open]);

  return (
    <>
      <button className="mobile-menu-button" type="button" aria-label={t('menu')} aria-expanded={open} aria-controls="mobile-navigation" onClick={() => {dialog.current?.showModal(); setOpen(true);}}>
        <Menu size={20} aria-hidden="true" />
      </button>
      <aside className="desktop-sidebar"><NavigationContent groups={groups} /></aside>
      <dialog id="mobile-navigation" ref={dialog} className="mobile-sidebar" aria-label={t('navLabel')} onClose={() => setOpen(false)} onKeyDown={(event) => {
        if (event.key !== 'Tab') return;
        const focusable = Array.from(event.currentTarget.querySelectorAll<HTMLElement>('a[href], button:not(:disabled), summary, [tabindex="0"]')).filter((element) => element.getClientRects().length > 0);
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last?.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first?.focus();
        }
      }} onClick={(event) => {
        if (event.target !== event.currentTarget) return;
        const bounds = event.currentTarget.getBoundingClientRect();
        if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) closeMenu();
      }}>
        <div className="mobile-sidebar-heading"><span>{gameTitle} <span>WIKI</span></span><button type="button" onClick={closeMenu} aria-label={t('closeMenu')}><X size={21} aria-hidden="true" /></button></div>
        <NavigationContent groups={groups} onNavigate={closeMenu} />
      </dialog>
    </>
  );
}
