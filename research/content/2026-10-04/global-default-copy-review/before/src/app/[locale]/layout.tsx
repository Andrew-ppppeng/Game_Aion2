import type {Metadata} from 'next';
import {hasLocale, NextIntlClientProvider} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {routing} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {SiteShell} from '@/components/site-shell';
import {site} from '@/lib/site';
import {SiteAnalytics} from '@/components/site-analytics';
import {GoogleAnalytics} from '@/components/google-analytics';
import '../globals.css';

export async function generateMetadata({params}: {params: Promise<{locale: string}>}): Promise<Metadata> {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  const m = getSiteMessages(locale);
  return {
    metadataBase: new URL(site.url),
    title: {default: m.footer.aboutTitle, template: `%s | ${m.footer.aboutTitle}`},
    applicationName: m.footer.aboutTitle,
    referrer: 'origin',
    icons: {icon: [{url: '/favicon.ico'}, {url: '/favicon-32x32.png', sizes: '32x32', type: 'image/png'}, {url: '/favicon-16x16.png', sizes: '16x16', type: 'image/png'}], apple: [{url: '/apple-touch-icon.png', sizes: '180x180'}]},
    manifest: '/site.webmanifest',
  };
}

export const viewport = {width: 'device-width', initialScale: 1, themeColor: '#0a101b', colorScheme: 'dark'};
export function generateStaticParams() {return routing.locales.map((locale) => ({locale}));}

export default async function LocaleLayout({children, params}: {children: React.ReactNode; params: Promise<{locale: string}>}) {
  const {locale} = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const messages = getSiteMessages(locale);
  return <html lang={locale} className="dark"><body><NextIntlClientProvider locale={locale} messages={{ui: messages.ui}}><SiteShell locale={locale}>{children}</SiteShell><SiteAnalytics locale={locale} /><GoogleAnalytics /></NextIntlClientProvider></body></html>;
}
