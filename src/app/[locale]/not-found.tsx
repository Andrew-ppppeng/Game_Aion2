import {getLocale} from 'next-intl/server';
import {Compass} from 'lucide-react';
import {Link} from '@/i18n/navigation';
import {getSiteMessages} from '@/i18n/messages';
import {routing, type Locale} from '@/i18n/routing';

export default async function NotFound() {
  const current = await getLocale();
  const locale = routing.locales.includes(current as Locale) ? current as Locale : 'en';
  const m = getSiteMessages(locale);
  return <div className="placeholder-page"><div className="placeholder-content"><Compass size={50} strokeWidth={1} aria-hidden="true" /><span className="eyebrow">404</span><h1>{m.ui.notFoundTitle}</h1><p>{m.ui.notFoundDescription}</p><Link href="/" className="button button-primary">{m.ui.backHome}</Link></div></div>;
}
