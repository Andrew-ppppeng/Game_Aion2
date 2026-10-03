import assert from 'node:assert/strict';
import {randomUUID} from 'node:crypto';

// Run with --conditions=react-server --experimental-strip-types and a private env file.
const {cached, limited, takeQuota} = await import('../src/lib/aion2/cache.ts');
const other = await import(new URL('../src/lib/aion2/cache.ts?instance=live-verification', import.meta.url).href);
assert.ok((process.env.UPSTASH_REDIS_REST_URL || process.env.KV_REST_API_URL) && (process.env.UPSTASH_REDIS_REST_TOKEN || process.env.KV_REST_API_TOKEN), 'Shared Redis credentials must be present');
const prefix = `verification:${randomUUID()}`;
let reads = 0;
const load = async () => {reads++; await new Promise((resolve) => setTimeout(resolve, 150)); return {data: {verification: true}, meta: null, error: null};};
const results = await Promise.all([cached(`${prefix}:dedupe`, 60000, 0, load), other.cached(`${prefix}:dedupe`, 60000, 0, load)]);
assert.equal(reads, 1, 'Separate module instances share one Redis request lock');
assert.ok(results.every((r) => r.data.verification));
await other.cached(`${prefix}:dedupe`, 60000, 0, load);
assert.equal(reads, 1);
await takeQuota(`${prefix}:quota`, 2);
await other.takeQuota(`${prefix}:quota`, 2);
await assert.rejects(takeQuota(`${prefix}:quota`, 2), /rate-limited/);
const starts = await Promise.all([limited(async () => Date.now()), other.limited(async () => Date.now())]);
assert.ok(Math.abs(starts[1] - starts[0]) >= 900, 'Separate instances respect the global request interval');
console.log('PASS: live shared Redis, cross-instance deduplication, cached reads, atomic quota and global request spacing. Verification keys expire within 60 seconds.');
