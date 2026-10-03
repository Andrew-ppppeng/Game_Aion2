import 'server-only';
import {randomUUID} from 'node:crypto';
import {DataError} from './model.ts';
import type {ApiResult} from './types';

type Entry<T> = {result: ApiResult<T>; expires: number; staleUntil: number};
const memory = new Map<string, Entry<unknown>>();
const pending = new Map<string, Promise<unknown>>();
const quotas = new Map<string, {count: number; until: number}>();
let localQueue: Promise<unknown> = Promise.resolve();
let localNext = 0;
const redisUrl = process.env.UPSTASH_REDIS_REST_URL || process.env.KV_REST_API_URL;
const redisToken = process.env.UPSTASH_REDIS_REST_TOKEN || process.env.KV_REST_API_TOKEN;
const configured = Boolean(redisUrl && redisToken);

async function redis(command: (string | number)[]): Promise<unknown> {
  if (!redisUrl || !redisToken) throw new DataError('cache-unavailable', 503, 30);
  try {
    const response = await fetch(redisUrl, {method: 'POST', headers: {Authorization: `Bearer ${redisToken}`, 'Content-Type': 'application/json'},
      body: JSON.stringify(command), cache: 'no-store', signal: AbortSignal.timeout(3000)});
    const data = await response.json();
    if (!response.ok || data.error) throw new Error('Redis refused the command');
    return data.result;
  } catch {throw new DataError('cache-unavailable', 503, 30);}
}
export async function takeQuota(key: string, max = 30): Promise<void> {
  let count: number;
  if (configured) {
    count = Number(await redis(['EVAL', "local n=redis.call('INCR', KEYS[1]); if n==1 then redis.call('PEXPIRE', KEYS[1], 60000) end; return n", 1, `aion2:v1:quota:${key}`]));
  } else {
    if (process.env.VERCEL) throw new DataError('cache-unavailable', 503, 30);
    const old = quotas.get(key);
    const entry = old && old.until > Date.now() ? old : {count: 0, until: Date.now() + 60000};
    count = ++entry.count;
    if (!quotas.has(key) && quotas.size >= 300) quotas.delete(quotas.keys().next().value as string);
    quotas.set(key, entry);
  }
  if (!Number.isFinite(count) || count > max) throw new DataError('rate-limited', 429, 60);
}
async function read<T>(key: string): Promise<Entry<T> | undefined> {
  if (configured) {
    const value = await redis(['GET', `aion2:v1:${key}`]);
    if (typeof value !== 'string') return undefined;
    try {return JSON.parse(value) as Entry<T>;} catch {return undefined;}
  }
  if (process.env.VERCEL) throw new DataError('cache-unavailable', 503, 30);
  return memory.get(key) as Entry<T> | undefined;
}
async function write<T>(key: string, entry: Entry<T>) {
  if (configured) await redis(['SET', `aion2:v1:${key}`, JSON.stringify(entry), 'PX', Math.max(1000, entry.staleUntil - Date.now())]);
  else {
    if (memory.size >= 300) memory.delete(memory.keys().next().value as string);
    memory.set(key, entry as Entry<unknown>);
  }
}
export async function cached<T>(key: string, ttl: number, stale: number, load: () => Promise<ApiResult<T>>): Promise<ApiResult<T>> {
  const entry = await read<T>(key);
  if (entry && entry.expires > Date.now()) return {...entry.result, meta: entry.result.meta ? {...entry.result.meta, freshness: 'cached'} : null};
  if (pending.has(key)) return pending.get(key) as Promise<ApiResult<T>>;
  const job: Promise<ApiResult<T>> = (async (): Promise<ApiResult<T>> => {
    const lock = `aion2:v1:request-lock:${key}`;
    const token = randomUUID();
    let acquired = false;
    try {
      if (configured) {
        // Coalesce cache misses across separate Vercel instances as well as this process.
        for (let i = 0; i < 70; i++) {
          if (await redis(['SET', lock, token, 'NX', 'PX', 60000]) === 'OK') {acquired = true; break;}
          const shared = await read<T>(key);
          if (shared && shared.expires > Date.now()) return {...shared.result, meta: shared.result.meta ? {...shared.result.meta, freshness: 'cached'} : null};
          await new Promise((resolve) => setTimeout(resolve, 500));
        }
        if (!acquired) throw new DataError('rate-limited', 429, 10);
        const shared = await read<T>(key);
        if (shared && shared.expires > Date.now()) return {...shared.result, meta: shared.result.meta ? {...shared.result.meta, freshness: 'cached'} : null};
      }
      const result = await load();
      await write(key, {result, expires: Date.now() + ttl, staleUntil: Date.now() + ttl + stale});
      return result;
    } catch (error) {
      if (entry && entry.staleUntil > Date.now() && !(error instanceof DataError && [400, 404].includes(error.status))) return {
        ...entry.result, meta: entry.result.meta ? {...entry.result.meta, freshness: 'stale'} : null,
        error: {code: 'using-stale-data'},
      };
      throw error;
    } finally {
      if (acquired) await redis(['EVAL', "if redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('DEL', KEYS[1]) else return 0 end", 1, lock, token]).catch(() => {});
      pending.delete(key);
    }
  })();
  pending.set(key, job);
  return job;
}

export function limited<T>(load: () => Promise<T>): Promise<T> {
  if (!configured) {
    if (process.env.VERCEL) return Promise.reject(new DataError('cache-unavailable', 503, 30));
    const job = localQueue.catch(() => {}).then(async () => {
      const delay = Math.max(0, localNext - Date.now());
      if (delay) await new Promise((resolve) => setTimeout(resolve, delay));
      try {return await load();} finally {localNext = Date.now() + 1000;}
    });
    localQueue = job;
    return job;
  }
  return distributed(load);
}
async function distributed<T>(load: () => Promise<T>): Promise<T> {
  const token = randomUUID();
  const lock = 'aion2:v1:upstream-lock';
  let acquired = false;
  for (let i = 0; i < 20; i++) {
    if (await redis(['SET', lock, token, 'NX', 'PX', 12000]) === 'OK') {acquired = true; break;}
    await new Promise((resolve) => setTimeout(resolve, 500));
  }
  if (!acquired) throw new DataError('rate-limited', 429, 10);
  try {
    if (await redis(['GET', 'aion2:v1:upstream-pause'])) throw new DataError('rate-limited', 429, 60);
    return await load();
  } catch (error) {
    if (error instanceof DataError && error.code === 'upstream-refused') {
      await redis(['SET', 'aion2:v1:upstream-pause', '1', 'EX', Math.max(60, error.retryAfter || 60)]).catch(() => {});
    }
    throw error;
  } finally {
    // Keep the lock for one second after completion. Compare its owner before extending it.
    await redis(['EVAL', "if redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('PEXPIRE', KEYS[1], 1000) else return 0 end", 1, lock, token]).catch(() => {});
  }
}
