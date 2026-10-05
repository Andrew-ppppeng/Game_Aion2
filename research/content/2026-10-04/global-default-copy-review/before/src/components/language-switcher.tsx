'use client';

import {useTransition} from 'react';
import {ChevronDown, Globe2} from 'lucide-react';
import {useRouter} from 'next/navigation';
import {useLocale, useTranslations} from 'next-intl';
import {getPathname, usePathname} from '@/i18n/navigation';
import type {Locale} from '@/i18n/routing';

const languages: {locale: Locale; label: string}[] = [
  {locale: 'en', label: 'English'},
  {locale: 'ja', label: '日本語'},
  {locale: 'es', label: 'Español'},
  {locale: 'de', label: 'Deutsch'},
];

export function LanguageSwitcher() {
  const locale = useLocale();
  const t = useTranslations('ui');
  const router = useRouter();
  const pathname = usePathname();
  const [isPending, startTransition] = useTransition();

  return (
    <div className="language-switcher" aria-busy={isPending}>
      <Globe2 size={15} aria-hidden="true" />
      <select
        aria-label={t('chooseLanguage')}
        value={locale}
        disabled={isPending}
        onChange={(event) => {
          const nextLocale = event.target.value as Locale;
          const href = getPathname({locale: nextLocale, href: `${pathname}${window.location.search}${window.location.hash}`});
          startTransition(() => router.replace(href));
        }}
      >
        {languages.map((language) => (
          <option key={language.locale} value={language.locale}>{language.label}</option>
        ))}
      </select>
      <ChevronDown size={13} aria-hidden="true" />
    </div>
  );
}
