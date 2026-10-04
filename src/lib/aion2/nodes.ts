import {DataError, plainName} from './model.ts';
export type NodeDetail = {boardId: number; nodeId: number; row: number; col: number; open: number; type: string; grade: string; name: string; effectList: {desc: string}[]};
export type BoardDetail = {nodeList: NodeDetail[]};
export function validateBoard(value: unknown, boardId: number): BoardDetail {
  if (!value || typeof value !== 'object' || !('nodeList' in value) || !Array.isArray(value.nodeList) || !value.nodeList.length || value.nodeList.length > 2000) throw new DataError('invalid-data');
  const ids = new Set<number>();
  const nodeList = value.nodeList.map((raw: unknown) => {
    if (!raw || typeof raw !== 'object') throw new DataError('invalid-data');
    const n = raw as NodeDetail;
    if (n.boardId !== boardId || !Number.isSafeInteger(n.nodeId) || n.nodeId <= 0 || ids.has(n.nodeId) || !Number.isInteger(n.row) || n.row < 0 || n.row > 100 || !Number.isInteger(n.col) || n.col < 0 || n.col > 100 ||
      ![0, 1].includes(n.open) || typeof n.name !== 'string' || typeof n.type !== 'string' || typeof n.grade !== 'string' || !Array.isArray(n.effectList) || n.effectList.length > 50 || n.effectList.some((e) => !e || typeof e.desc !== 'string')) throw new DataError('invalid-data');
    ids.add(n.nodeId);
    return {boardId, nodeId: n.nodeId, row: n.row, col: n.col, open: n.open, name: plainName(n.name), type: n.type, grade: n.grade, effectList: n.effectList.map((e) => ({desc: plainName(e.desc)}))};
  });
  return {nodeList};
}
