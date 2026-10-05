import {gameEvents} from '@/lib/aion2/data';
export async function GET(request: Request) {
  const topic = new URL(request.url).searchParams.get('topic');
  if (topic && !['maintenance', 'twitch-drops', 'code', 'spacetime-rift'].includes(topic)) return Response.json({data: null, meta: null, error: {code: 'invalid-input'}}, {status: 400, headers: {'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow'}});
  return Response.json({data: topic ? gameEvents.filter((e) => e.topics.includes(topic)) : gameEvents, meta: {service: 'Global', freshness: 'snapshot', gameVersion: null, checkedAt: '2026-10-03'}, error: null},
    {headers: {'Cache-Control': 'public, max-age=3600', 'X-Robots-Tag': 'noindex, nofollow'}});
}
