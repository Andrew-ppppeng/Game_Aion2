import {Link} from '@/i18n/navigation';
import {Database, UserRound, Calculator, CalendarDays, LayoutDashboard, ArrowRight, Swords} from 'lucide-react';
import {platformMessages} from '@/i18n/platform-messages';
import {platformLocale, platformMetadata} from '@/lib/platform-page';
import {PlatformFrame} from '@/components/platform/page-frame';
type Props = {params: Promise<{locale: string}>};
export async function generateMetadata({params}: Props) {const locale = platformLocale((await params).locale); const m = platformMessages[locale]; return platformMetadata(locale, '/tools', m.tools, m.toolsIntro);}
export default async function ToolsPage({params}: Props) {
  const locale = platformLocale((await params).locale); const m = platformMessages[locale];
  const tools = [{href:'/database', title:m.database, description:m.catalogueIntro, icon:Database}, {href:'/tools/compare',title:m.compare,description:m.compareNote,icon:Swords}, {href:'/tools/character',title:m.character,description:m.characterDesc,icon:UserRound}, {href:'/workspace',title:m.workspace,description:m.workspaceDesc,icon:LayoutDashboard}, {href:'/tools/budget',title:m.budget,description:m.budgetDesc,icon:Calculator}, {href:'/tools/calendar',title:m.calendar,description:m.calendarDesc,icon:CalendarDays}];
  return <PlatformFrame locale={locale} title={m.tools} intro={m.toolsIntro}><div className="tool-hub-grid">{tools.map(({href,title,description,icon:Icon}) => <Link href={href} className="tool-hub-card" key={href}><Icon size={24} aria-hidden="true" /><h2>{title}</h2><p>{description}</p><ArrowRight size={18} aria-hidden="true" /></Link>)}</div></PlatformFrame>;
}
