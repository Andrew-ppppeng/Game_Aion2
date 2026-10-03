import assert from 'node:assert/strict';
import {test} from 'node:test';
import {DataError} from '../src/lib/aion2/model.ts';
import type {ApiResult} from '../src/lib/aion2/types.ts';

const result: ApiResult<number> = {data: 42, meta: {service: 'Global', region: 'nae', locale: 'en', sourceUrl: 'https://aion2.plaync.com/api/character/info', fetchedAt: '2026-10-03T06:00:00Z', gameVersion: null, freshness: 'fresh'}, error: null};

test('local cache deduplicates requests and returns a marked stale value only for transient failures', async () => {
  delete process.env.UPSTASH_REDIS_REST_URL;
  delete process.env.UPSTASH_REDIS_REST_TOKEN;
  delete process.env.KV_REST_API_URL;
  delete process.env.KV_REST_API_TOKEN;
  delete process.env.VERCEL;
  const {cached, takeQuota} = await import('../src/lib/aion2/cache.ts');
  let calls = 0;
  const load = async () => {calls++; await new Promise((resolve) => setTimeout(resolve, 20)); return result;};
  await Promise.all(Array.from({length: 10}, () => cached('dedupe', 1000, 1000, load)));
  assert.equal(calls, 1);
  assert.equal((await cached('dedupe', 1000, 1000, load)).meta?.freshness, 'cached');
  await cached('stale', 0, 1000, load);
  const old = await cached('stale', 0, 1000, async () => {throw new DataError('upstream-unavailable');});
  assert.equal(old.data, 42);
  assert.equal(old.meta?.freshness, 'stale');
  assert.equal(old.error?.code, 'using-stale-data');
  await assert.rejects(cached('stale', 0, 1000, async () => {throw new DataError('character-unavailable', 404);}), /character-unavailable/);
  for (let i = 0; i < 3; i++) await takeQuota('test', 3);
  await assert.rejects(takeQuota('test', 3), /rate-limited/);
  process.env.VERCEL = '1';
  await assert.rejects(cached('missing-redis', 1000, 1000, load), /cache-unavailable/);
  delete process.env.VERCEL;
});

test('Redis locks deduplicate across server instances and Redis failure never bypasses shared limits', async () => {
  const originalFetch = globalThis.fetch;
  const values = new Map<string, string>();
  let fail = false;
  let pauseWrites = 0;
  process.env.UPSTASH_REDIS_REST_URL = 'https://redis.example.invalid';
  process.env.UPSTASH_REDIS_REST_TOKEN = 'offline-test-token';
  globalThis.fetch = async (_input, init) => {
    if (fail) throw new Error('Offline Redis failure');
    const [command, k, value, option] = JSON.parse(String(init?.body));
    let output: unknown = null;
    if (command === 'GET') output = values.get(k) ?? null;
    if (command === 'SET') {
      if (k === 'aion2:v1:upstream-pause') pauseWrites++;
      if (option !== 'NX' || !values.has(k)) {values.set(k, value); output = 'OK';}
    }
    if (command === 'EVAL') {values.delete(option); output = 1;}
    return Response.json({result: output});
  };
  try {
    const firstUrl = new URL('../src/lib/aion2/cache.ts?instance=one', import.meta.url).href;
    const secondUrl = new URL('../src/lib/aion2/cache.ts?instance=two', import.meta.url).href;
    const one = await import(firstUrl);
    const two = await import(secondUrl);
    let calls = 0;
    const load = async () => {calls++; await new Promise((resolve) => setTimeout(resolve, 40)); return result;};
    const [a, b] = await Promise.all([one.cached('shared-key', 1000, 1000, load), two.cached('shared-key', 1000, 1000, load)]);
    assert.equal(a.data, 42); assert.equal(b.data, 42); assert.equal(calls, 1);
    await assert.rejects(one.limited(async () => {throw new DataError('upstream-refused', 503, 60);}), /upstream-refused/);
    await assert.rejects(two.limited(load), /rate-limited/);
    assert.equal(pauseWrites, 1, 'Requests during the pause must not extend it indefinitely');
    fail = true;
    await assert.rejects(one.cached('fail-closed', 1000, 1000, load), /cache-unavailable/);
    assert.equal(calls, 1);
  } finally {
    globalThis.fetch = originalFetch;
    delete process.env.UPSTASH_REDIS_REST_URL;
    delete process.env.UPSTASH_REDIS_REST_TOKEN;
  }
});
