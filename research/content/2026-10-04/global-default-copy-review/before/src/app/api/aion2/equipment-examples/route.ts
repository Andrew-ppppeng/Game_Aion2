import {hasLocale} from 'next-intl';
import {routing} from '@/i18n/routing';
import {itemCards} from '@/lib/aion2/data';

export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const locale = params.get('locale');
  const slug = params.get('slug');
  if (!hasLocale(routing.locales, locale) || !slug || !['builds', 'cleric-build', 'chanter'].includes(slug)) {
    return Response.json({error: 'invalid-input'}, {status: 400});
  }
  return Response.json({items: itemCards(locale, slug).slice(2)}, {headers: {
    'Cache-Control': 'public, max-age=3600, s-maxage=86400',
    'X-Robots-Tag': 'noindex, nofollow',
  }});
}
