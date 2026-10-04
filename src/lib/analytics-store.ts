import 'server-only';
import {redis} from './aion2/cache.ts';
import {counterField, type AnalyticsEvent} from './analytics-model.ts';

const retention = 35 * 86400;
const memory = new Map<string, Record<string, number>>();
const configured = () => Boolean((process.env.UPSTASH_REDIS_REST_URL || process.env.KV_REST_API_URL) && (process.env.UPSTASH_REDIS_REST_TOKEN || process.env.KV_REST_API_TOKEN));
export async function storeEvents(events: AnalyticsEvent[], now = Date.now()) {
  const today = new Date(now).toISOString().slice(0, 10);
  const increments = new Map<string, Map<string, number>>();
  for (const event of events) {
    // Return counts are attached to the original browser cohort, not the return date.
    const date = event.name === 'return_7d' ? event.cohort! : today;
    const fields = increments.get(date) || new Map<string, number>();
    const field = counterField(event);
    fields.set(field, (fields.get(field) || 0) + 1); increments.set(date, fields);
  }
  for (const [date, fields] of increments) {
    if (configured()) {
      const args = [...fields].flatMap(([field, count]) => [field, count]);
      const expiresAt = Math.floor(Date.parse(`${date}T00:00:00Z`) / 1000) + retention;
      await redis(['EVAL', "for i=1,#ARGV-1,2 do redis.call('HINCRBY',KEYS[1],ARGV[i],ARGV[i+1]) end; redis.call('EXPIREAT',KEYS[1],ARGV[#ARGV]); return 1", 1, `aion2:analytics:v1:${date}`, ...args, expiresAt]);
    } else {
      if (process.env.VERCEL) throw new Error('analytics-storage-unavailable');
      const day = memory.get(date) || {};
      for (const [field, count] of fields) day[field] = (day[field] || 0) + count;
      memory.set(date, day);
      for (const key of memory.keys()) if (Date.parse(key) < now - retention * 1000) memory.delete(key);
    }
  }
}
export async function readCounters(date: string): Promise<Record<string, number>> {
  if (!configured()) {
    if (process.env.VERCEL) throw new Error('analytics-storage-unavailable');
    return memory.get(date) || {};
  }
  const rows = await redis(['HGETALL', `aion2:analytics:v1:${date}`]) as string[];
  return Object.fromEntries(Array.from({length: rows.length / 2}, (_, i) => [rows[i * 2], Number(rows[i * 2 + 1])]));
}
