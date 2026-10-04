import {respond} from '@/lib/aion2/http';
import {getBoard} from '@/lib/aion2/server';
export async function GET(request: Request, {params}: {params: Promise<{id: string; board: string}>}) {
  const {id, board} = await params;
  return respond(() => getBoard(id, board, new URL(request.url).searchParams), request);
}
