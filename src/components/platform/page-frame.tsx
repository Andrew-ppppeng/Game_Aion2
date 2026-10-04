import type {ReactNode} from 'react';
import {Link} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';
import {getSiteMessages} from '@/i18n/messages';
import {platformMessages} from '@/i18n/platform-messages';
export function PlatformFrame({locale, title, intro, children}: {locale: Locale; title: string; intro: string; children: ReactNode}) {
  const m = platformMessages[locale];
  return <div className="tools-page"><nav className="breadcrumbs"><Link href="/">{getSiteMessages(locale).ui.home}</Link><span>/</span><Link href="/tools">{m.tools}</Link><span>/</span><span>{title}</span></nav><header className="article-header"><h1>{title}</h1><p>{intro}</p></header>{children}</div>;
}
