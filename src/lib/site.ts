import type {Locale} from '@/i18n/routing';
import {routing} from '@/i18n/routing';

export const site = {
  name: 'AION 2 Wiki',
  url: (process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000').replace(/\/$/, ''),
  official: 'https://aion2.plaync.com/en-us/',
  steam: 'https://store.steampowered.com/app/3393110/AION_2/',
  discord: 'https://discord.gg/aion2official',
  youtube: 'https://www.youtube.com/@Aion2Official',
  characters: 'https://aion2.plaync.com/en-us/characters/index',
  launchAnnouncement: 'https://about.ncsoft.com/news/article/A2_update_20261001',
  maintenanceAnnouncement: 'https://aion2.plaync.com/en-us/board/notice',
};

const officialLocales: Record<Locale, string> = {en: 'en-us', ja: 'ja-jp', es: 'es-es', de: 'de-de'};

export function officialLinks(locale: Locale) {
  const official = `https://aion2.plaync.com/${officialLocales[locale]}/`;
  return {official, characters: `${official}characters/index`};
}

export function localePath(locale: Locale, pathname = '/') {
  const suffix = pathname === '/' ? '' : pathname;
  return locale === 'en' ? suffix || '/' : `/${locale}${suffix}`;
}

export function languageAlternates(pathname = '/') {
  return Object.fromEntries([
    ...routing.locales.map((locale) => [locale, `${site.url}${localePath(locale, pathname)}`]),
    ['x-default', `${site.url}${localePath('en', pathname)}`],
  ]);
}
