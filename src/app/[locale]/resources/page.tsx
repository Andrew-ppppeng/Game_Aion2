import {hasLocale} from 'next-intl';
import {setRequestLocale} from 'next-intl/server';
import {notFound} from 'next/navigation';
import {routing} from '@/i18n/routing';
import {sectionMetadata} from '@/lib/section-metadata';
import {SectionPage} from '@/components/section-page';
type Props = {params: Promise<{locale: string}>};
export async function generateMetadata({params}: Props) {const {locale} = await params; if (!hasLocale(routing.locales, locale)) notFound(); return sectionMetadata(locale, 'resources');}
export default async function Page({params}: Props) {const {locale} = await params; if (!hasLocale(routing.locales, locale)) notFound(); setRequestLocale(locale); return <SectionPage locale={locale} section="resources" />;}
