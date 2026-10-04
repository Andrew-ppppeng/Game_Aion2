import {notFound} from 'next/navigation';
import {platformMessages} from '@/i18n/platform-messages';
import {platformLocale, platformMetadata} from '@/lib/platform-page';
import {catalogue} from '@/lib/aion2/catalogue';
import {gameEvents} from '@/lib/aion2/data';
import {PlatformFrame} from '@/components/platform/page-frame';
import {EquipmentCompare} from '@/components/platform/equipment-compare';
import {BudgetPlanner, EventTimers} from '@/components/guide-interactions';
import {readRegion} from '@/lib/aion2/model';
type Props = {params: Promise<{locale: string; tool: string}>; searchParams: Promise<Record<string, string | string[] | undefined>>};
function toolKey(tool: string) {if (!['compare', 'budget', 'calendar'].includes(tool)) notFound(); return tool === 'compare' ? 'compare' : tool === 'budget' ? 'budget' : 'calendar';}
export async function generateMetadata({params,searchParams}: Props) {const raw = await params; const locale = platformLocale(raw.locale); const key = toolKey(raw.tool); const m = platformMessages[locale]; return platformMetadata(locale, `/tools/${raw.tool}`, m[key], m[key === 'compare' ? 'compareNote' : key === 'budget' ? 'budgetDesc' : 'calendarDesc'], !Object.keys(await searchParams).length);}
export default async function ToolPage({params,searchParams}: Props) {
  const raw = await params; const locale = platformLocale(raw.locale); const key = toolKey(raw.tool); const m = platformMessages[locale]; const query = await searchParams;
  // This server timestamp is the hydration baseline for the client's live clock.
  // eslint-disable-next-line react-hooks/purity
  const initialNow = Date.now();
  let initialRegion;
  try {initialRegion = readRegion(typeof query.region === 'string' ? query.region : null);} catch {notFound();}
  return <PlatformFrame locale={locale} title={m[key]} intro={m[key === 'compare' ? 'compareNote' : key === 'budget' ? 'budgetDesc' : 'calendarDesc']}>
    {key === 'compare' ? <EquipmentCompare locale={locale} entries={catalogue(locale)} initialFirst={Number(query.first)} initialSecond={Number(query.second)} initialRegion={initialRegion} /> : key === 'budget' ? <BudgetPlanner locale={locale} /> : <EventTimers locale={locale} events={gameEvents} initialNow={initialNow} />}
  </PlatformFrame>;
}
