'use client';

import {memo, useCallback, useEffect, useRef, useState} from 'react';
import {BookOpen, ChevronDown, Home, Layers3, Menu, Wrench, Library, X} from 'lucide-react';
import {useTranslations} from 'next-intl';
import {Link, usePathname} from '@/i18n/navigation';
import {sectionForPath, type SectionId} from '@/lib/site-structure';
import {CouponCard} from './coupon-card';

export type NavSection = {
  id: SectionId; label: string; href: string; overview: string;
  groups: {id: string; label: string; links: {href: string; title: string}[]}[];
};

const icons = {tools: Wrench, guides: BookOpen, classes: Layers3, resources: Library};

export function PrimaryNavigation({sections}: {sections: NavSection[]}) {
  const pathname = usePathname();
  const current = sectionForPath(pathname);
  const t = useTranslations('ui');
  return <nav className="primary-navigation" aria-label={t('navLabel')} data-primary-navigation>{sections.map((section) => <Link key={section.id} href={section.href} aria-current={current === section.id ? (pathname === section.href ? 'page' : 'true') : undefined}>{section.label}</Link>)}</nav>;
}

const NavigationContent = memo(function NavigationContent({sections, onNavigate}: {sections: NavSection[]; onNavigate?: () => void}) {
  const pathname = usePathname();
  const t = useTranslations('ui');
  const current = sectionForPath(pathname);
  const visible = onNavigate ? sections : sections.filter((section) => section.id === (current ?? 'guides'));
  return (
    <>
      <div className="sidebar-scroll">
        <nav aria-label={t('navLabel')} id={onNavigate ? undefined : 'guides'}>
          <Link className={`nav-home ${pathname === '/' ? 'active' : ''}`} href="/" aria-current={pathname === '/' ? 'page' : undefined} onClick={onNavigate}>
            <Home size={17} aria-hidden="true" />{t('home')}
            <span className="nav-active-dot" aria-hidden="true" />
          </Link>
          {!onNavigate && <div className="sidebar-sections">{sections.map((section) => {const Icon = icons[section.id]; return <Link className={`nav-single${current === section.id ? ' active' : ''}`} key={section.id} href={section.href} aria-current={current === section.id ? (pathname === section.href ? 'page' : 'true') : undefined}><Icon size={16} aria-hidden="true" /><span>{section.label}</span></Link>;})}</div>}
          {visible.map((section) => {const Icon = icons[section.id]; return <details className="nav-group" key={`${section.id}:${pathname}`} open={!onNavigate || current === section.id} data-nav-section={section.id}>
            <summary><Icon size={16} aria-hidden="true" /><span>{section.label}</span><ChevronDown size={13} className="nav-chevron" aria-hidden="true" /></summary>
            <div className="nav-topics">{onNavigate && <Link href={section.href} onClick={onNavigate} aria-current={pathname === section.href ? 'page' : undefined}>{section.overview}</Link>}
              {section.groups.map((group) => <div key={group.id}><p className="nav-subheading">{group.label}</p>{group.links.map((link) => <Link key={link.href} href={link.href} onClick={onNavigate} className={pathname === link.href ? 'active' : ''} aria-current={pathname === link.href ? 'page' : undefined}><span>{link.title}</span><span className="topic-dot" aria-hidden="true" /></Link>)}</div>)}
            </div>
          </details>;})}
        </nav>
      </div>
      <div className="sidebar-bottom">
        <CouponCard />
      </div>
    </>
  );
});

export function SiteNavigation({sections, gameTitle}: {sections: NavSection[]; gameTitle: string}) {
  const t = useTranslations('ui');
  const dialog = useRef<HTMLDialogElement>(null);
  const [open, setOpen] = useState(false);

  const closeMenu = useCallback(() => {
    dialog.current?.close();
  }, []);

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
      <aside className="desktop-sidebar"><NavigationContent sections={sections} /></aside>
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
        <NavigationContent sections={sections} onNavigate={closeMenu} />
      </dialog>
    </>
  );
}
