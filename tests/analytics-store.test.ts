import assert from 'node:assert/strict';
import {test} from 'node:test';
import type {AnalyticsEvent} from '../src/lib/analytics-model.ts';

test('analytics aggregate storage uses original cohorts, fixed expiry and no production memory fallback', async (t) => {
  const keys = ['UPSTASH_REDIS_REST_URL', 'UPSTASH_REDIS_REST_TOKEN', 'KV_REST_API_URL', 'KV_REST_API_TOKEN', 'VERCEL'];
  const originalEnv = new Map(keys.map((key) => [key, process.env[key]]));
  const originalFetch = globalThis.fetch;
  const commands: (string | number)[][] = [];
  const redisValues = new Map<string, Map<string, number>>();
  let unavailable = false;
  for (const key of keys) delete process.env[key];
  process.env.UPSTASH_REDIS_REST_URL = 'https://redis.example.invalid';
  process.env.UPSTASH_REDIS_REST_TOKEN = 'offline-analytics-test-token';
  globalThis.fetch = async (_url, init) => {
    if (unavailable) throw new Error('Offline');
    const command = JSON.parse(String(init?.body)) as (string | number)[];
    commands.push(command);
    if (command[0] === 'EVAL') {
      const hash = redisValues.get(String(command[3])) || new Map<string, number>();
      for (let i = 4; i < command.length - 1; i += 2) hash.set(String(command[i]), (hash.get(String(command[i])) || 0) + Number(command[i + 1]));
      redisValues.set(String(command[3]), hash);
      return Response.json({result: 1});
    }
    if (command[0] === 'HGETALL') return Response.json({result: [...(redisValues.get(String(command[1])) || new Map())].flatMap(([field, count]) => [field, String(count)])});
    throw new Error('Unexpected Redis command');
  };
  try {
    const {readCounters, storeEvents} = await import('../src/lib/analytics-store.ts');
    const now = Date.parse('2026-10-04T12:00:00Z');
    const view: AnalyticsEvent = {name: 'page_view', path: '/guide', locale: 'en'};
    const returning: AnalyticsEvent = {name: 'return_7d', path: '/guide', locale: 'en', cohort: '2026-10-02'};
    await t.test('Redis writes aggregated counters once per date, attaches returns to original cohort and fixes expiry to cohort date', async () => {
      await storeEvents([view, view, returning], now);
      assert.equal((await readCounters('2026-10-04'))['en|/guide|page_view'], 2);
      assert.equal((await readCounters('2026-10-04'))['en|/guide|return_7d'], undefined);
      assert.equal((await readCounters('2026-10-02'))['en|/guide|return_7d'], 1);
      const writes = commands.filter((command) => command[0] === 'EVAL');
      assert.equal(writes.length, 2);
      assert.match(String(writes[1][1]), /EXPIREAT/);
      assert.equal(writes[1].at(-1), Date.parse('2026-10-02T00:00:00Z') / 1000 + 35 * 86400);
      await storeEvents([returning], now + 86400000);
      assert.equal(commands.filter((command) => command[0] === 'EVAL').at(-1)?.at(-1), writes[1].at(-1), 'A later return must not extend cohort storage lifetime');
    });
    await t.test('Redis failure fails closed rather than creating incomplete local counts', async () => {
      unavailable = true;
      await assert.rejects(storeEvents([view], now), /cache-unavailable/);
      await assert.rejects(readCounters('2026-10-04'), /cache-unavailable/);
      unavailable = false;
    });
    await t.test('local development keeps only aggregate counters and expires old days on writes', async () => {
      for (const key of keys) delete process.env[key];
      await storeEvents([view, returning], now);
      assert.deepEqual(await readCounters('2026-10-04'), {'en|/guide|page_view': 1});
      assert.deepEqual(await readCounters('2026-10-02'), {'en|/guide|return_7d': 1});
      await storeEvents([view], now + 36 * 86400000);
      assert.deepEqual(await readCounters('2026-10-04'), {});
    });
    await t.test('production without shared storage rejects reads and writes', async () => {
      process.env.VERCEL = '1';
      await assert.rejects(storeEvents([view], now), /analytics-storage-unavailable/);
      await assert.rejects(readCounters('2026-10-04'), /analytics-storage-unavailable/);
    });
  } finally {
    globalThis.fetch = originalFetch;
    for (const [key, value] of originalEnv) {if (value === undefined) delete process.env[key]; else process.env[key] = value;}
  }
});
