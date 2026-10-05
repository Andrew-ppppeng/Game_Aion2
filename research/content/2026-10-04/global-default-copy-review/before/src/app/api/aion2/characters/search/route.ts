import {searchCharacters} from '@/lib/aion2/server';
import {respond} from '@/lib/aion2/http';
export const maxDuration = 60;
export async function GET(request: Request) {return respond(() => searchCharacters(new URL(request.url).searchParams), request);}
