import source from '../../home.en.json';
import en from '@/messages/en.json';
import ja from '@/messages/ja.json';
import es from '@/messages/es.json';
import de from '@/messages/de.json';
import type {Locale} from './routing';

const english = {...source, ...en};
export type SiteMessages = typeof english;

const messages = {
  en: english,
  ja: {...source, ...ja},
  es: {...source, ...es},
  de: {...source, ...de},
} satisfies Record<Locale, SiteMessages>;

export function getSiteMessages(locale: Locale): SiteMessages {
  return messages[locale];
}
