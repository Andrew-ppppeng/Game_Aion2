import {notFound} from 'next/navigation';
import {Link} from '@/i18n/navigation';
import {routing} from '@/i18n/routing';
import {platformMessages} from '@/i18n/platform-messages';
import {catalogue} from '@/lib/aion2/catalogue';
import {curatedIds} from '@/lib/aion2/data';
import {platformLocale, platformMetadata} from '@/lib/platform-page';
import {PlatformFrame} from '@/components/platform/page-frame';
import {ItemView} from '@/components/platform/item-view';
import {readRegion} from '@/lib/aion2/model';
type Props = {params: Promise<{locale: string; id: string}>; searchParams: Promise<Record<string, unknown>>};
export function generateStaticParams() {return routing.locales.flatMap((locale) => curatedIds.map((id) => ({locale, id: String(id)})));}
export async function generateMetadata({params, searchParams}: Props) {
  const raw = await params; const locale = platformLocale(raw.locale); const entry = catalogue(locale).find((e) => String(e.item.id) === raw.id); if (!entry) notFound();
  return platformMetadata(locale, `/database/items/${raw.id}`, `${entry.item.name} · AION 2`, platformMessages[locale].detailIntro, !Object.keys(await searchParams).length);
}
export default async function ItemPage({params, searchParams}: Props) {
  const raw = await params; const locale = platformLocale(raw.locale); const entry = catalogue(locale).find((e) => String(e.item.id) === raw.id); if (!entry) notFound();
  const m = platformMessages[locale];
  const query = await searchParams;
  let initialRegion;
  try {initialRegion = readRegion(typeof query.region === 'string' ? query.region : null);} catch {notFound();}
  return <PlatformFrame locale={locale} title={entry.item.name} intro={m.detailIntro}><Link href="/database" className="tool-link">← {m.database}</Link><ItemView entry={entry} locale={locale} initialRegion={initialRegion} /></PlatformFrame>;
}
