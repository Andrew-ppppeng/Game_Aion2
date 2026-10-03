import 'server-only';
import {createHash} from 'node:crypto';
import {takeQuota} from './cache';
import {DataError} from './model';
import type {ApiResult} from './types';

export async function respond<T>(load: () => Promise<ApiResult<T>>, request?: Request): Promise<Response> {
  try {
    if (request) {
      const ip = request.headers.get('x-forwarded-for')?.split(',')[0]?.trim() || 'local';
      await takeQuota(createHash('sha256').update(ip).digest('hex'));
    }
    return Response.json(await load(), {headers: {'Cache-Control': 'private, no-store', 'X-Robots-Tag': 'noindex, nofollow'}});
  } catch (error) {
    const known = error instanceof DataError ? error : new DataError('upstream-unavailable');
    return Response.json({data: null, meta: null, error: {code: known.code, ...(known.retryAfter ? {retryAfter: known.retryAfter} : {})}},
      {status: known.status, headers: {'Cache-Control': 'private, no-store', 'X-Robots-Tag': 'noindex, nofollow', ...(known.retryAfter ? {'Retry-After': String(known.retryAfter)} : {})}});
  }
}
