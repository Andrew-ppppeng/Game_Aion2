import {getMeta} from '@/lib/aion2/server';
import {respond} from '@/lib/aion2/http';
export async function GET(request: Request) {return respond(() => getMeta(new URL(request.url).searchParams));}
