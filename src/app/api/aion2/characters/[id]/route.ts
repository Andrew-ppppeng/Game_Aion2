import {getCharacter} from '@/lib/aion2/server';
import {respond} from '@/lib/aion2/http';
export const maxDuration = 60;
export async function GET(request: Request, {params}: {params: Promise<{id: string}>}) {
  const {id} = await params;
  return respond(() => getCharacter(id, new URL(request.url).searchParams), request);
}
