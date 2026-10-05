import {getEquipped} from '@/lib/aion2/server';
import {respond} from '@/lib/aion2/http';
export const maxDuration = 60;
export async function GET(request: Request, {params}: {params: Promise<{id: string; slot: string}>}) {
  const {id, slot} = await params;
  return respond(() => getEquipped(id, slot, new URL(request.url).searchParams), request);
}
