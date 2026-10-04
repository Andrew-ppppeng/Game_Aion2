import {timingSafeEqual, createHash} from 'node:crypto';
import {topics, legalSlugs} from '@/lib/topics';
import {validateEvents, isIsoDate} from '@/lib/analytics-model';
import {storeEvents, readCounters} from '@/lib/analytics-store';
import {takeQuota} from '@/lib/aion2/cache';
import {DataError} from '@/lib/aion2/model';

export const dynamic = 'force-dynamic';
const headers = {'Cache-Control': 'private, no-store', 'X-Robots-Tag': 'noindex, nofollow'};
const pages = new Set(['/', '/tools/character', ...legalSlugs.map((slug) => `/${slug}`), ...topics.map(({slug}) => `/${slug}`)]);
function sameOrigin(request: Request) {
  // Next can normalize request.url to localhost behind the local server or a
  // proxy. The Host authority is the address actually used by the browser.
  const url = new URL(request.url);
  const host = request.headers.get('host') || url.host;
  if (!/^(?:[a-z0-9.-]+|\[[a-f0-9:]+\])(?::\d{1,5})?$/i.test(host)) return false;
  const forwarded = request.headers.get('x-forwarded-proto');
  const protocol = forwarded === 'https' ? 'https:' : url.protocol;
  return request.headers.get('origin') === new URL(`${protocol}//${host}`).origin;
}
export async function POST(request: Request) {
  if (process.env.NEXT_PUBLIC_ANALYTICS_ENABLED === 'false') return new Response(null, {status: 204, headers});
  if (!sameOrigin(request)) return new Response(null, {status: 403, headers});
  if (Number(request.headers.get('content-length')) > 8192) return new Response(null, {status: 413, headers});
  const text = await request.text();
  if (text.length > 8192) return new Response(null, {status: 413, headers});
  let input: unknown;
  try {input = JSON.parse(text);} catch {return new Response(null, {status: 400, headers});}
  const events = validateEvents(input, pages);
  if (!events) return new Response(null, {status: 400, headers});
  try {
    const ip = request.headers.get('x-forwarded-for')?.split(',')[0]?.trim() || 'local';
    await takeQuota(`analytics:${createHash('sha256').update(ip).digest('hex')}`, 120);
    await storeEvents(events);
    return new Response(null, {status: 204, headers});
  } catch (error) {return new Response(null, {status: error instanceof DataError ? error.status : 503, headers});}
}
export async function GET(request: Request) {
  const expected = process.env.ANALYTICS_READ_TOKEN;
  const received = request.headers.get('authorization')?.replace(/^Bearer /, '');
  if (!expected || !received || !timingSafeEqual(createHash('sha256').update(expected).digest(), createHash('sha256').update(received).digest())) return new Response(null, {status: 401, headers});
  const date = new URL(request.url).searchParams.get('date') || new Date().toISOString().slice(0, 10);
  const age = Date.now() - Date.parse(`${date}T00:00:00Z`);
  if (!isIsoDate(date) || !Number.isFinite(age) || age < 0 || age > 35 * 86400000) return new Response(null, {status: 400, headers});
  try {return Response.json({date, counters: await readCounters(date)}, {headers});}
  catch {return new Response(null, {status: 503, headers});}
}
