import {defineRouting} from 'next-intl/routing';

export const routing = defineRouting({
  locales: ['en', 'ja', 'es', 'de'],
  defaultLocale: 'en',
  localePrefix: 'as-needed',
  localeDetection: false,
  localeCookie: false,
});

export type Locale = (typeof routing.locales)[number];
