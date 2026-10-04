import {platformMessages} from '@/i18n/platform-messages';
import {platformLocale, platformMetadata} from '@/lib/platform-page';
import {catalogue} from '@/lib/aion2/catalogue';
import {PlatformFrame} from '@/components/platform/page-frame';
import {WorkspaceView} from '@/components/platform/workspace';
type Props = {params: Promise<{locale: string}>};
export async function generateMetadata({params}: Props) {const locale = platformLocale((await params).locale); const m = platformMessages[locale]; return platformMetadata(locale, '/workspace', m.workspace, m.workspaceDesc, false);}
export default async function WorkspacePage({params}: Props) {const locale = platformLocale((await params).locale); const m = platformMessages[locale]; return <PlatformFrame locale={locale} title={m.workspace} intro={m.workspaceDesc}><WorkspaceView entries={catalogue(locale)} locale={locale} /></PlatformFrame>;}
