export const eventNames = ['page_view', 'new_browser', 'session_start', 'return_7d', 'next_guide_click', 'video_click', 'tool_use', 'bookmark_save', 'budget_save', 'checklist_save', 'web_vital'] as const;
export type AnalyticsEvent = {
  name: typeof eventNames[number]; path: string; locale: 'en' | 'ja' | 'es' | 'de';
  target?: 'character' | 'budget' | 'checklist' | 'calendar' | 'equipment' | 'classes' | 'videos';
  metric?: 'LCP' | 'INP' | 'CLS'; value?: number; cohort?: string;
};
const allowedKeys = new Set(['name', 'path', 'locale', 'target', 'metric', 'value', 'cohort']);
const targets = ['character', 'budget', 'checklist', 'calendar', 'equipment', 'classes', 'videos'];
export function isIsoDate(value: string) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const timestamp = Date.parse(`${value}T00:00:00Z`);
  return Number.isFinite(timestamp) && new Date(timestamp).toISOString().slice(0, 10) === value;
}
export function validateEvents(input: unknown, pages: Set<string>, now = Date.now()): AnalyticsEvent[] | null {
  if (!Array.isArray(input) || !input.length || input.length > 12) return null;
  for (const item of input) {
    if (!item || typeof item !== 'object' || Object.keys(item).some((key) => !allowedKeys.has(key))) return null;
    if (!eventNames.includes(item.name) || !pages.has(item.path) || !['en', 'ja', 'es', 'de'].includes(item.locale)) return null;
    if (item.target !== undefined && !targets.includes(item.target)) return null;
    if (item.name === 'web_vital') {
      if (!['LCP', 'INP', 'CLS'].includes(item.metric) || typeof item.value !== 'number' || !Number.isFinite(item.value) || item.value < 0 || item.value > (item.metric === 'CLS' ? 10 : 60000)) return null;
    } else if (item.metric !== undefined || item.value !== undefined) return null;
    if (item.name === 'return_7d') {
      if (typeof item.cohort !== 'string' || !isIsoDate(item.cohort)) return null;
      const age = now - Date.parse(`${item.cohort}T00:00:00Z`);
      if (!Number.isFinite(age) || age < 0 || age > 8 * 86400000) return null;
    } else if (item.cohort !== undefined) return null;
  }
  return input as AnalyticsEvent[];
}
export function counterField(event: AnalyticsEvent) {
  const prefix = `${event.locale}|${event.path}|${event.name}`;
  if (event.name === 'web_vital') {
    const step = event.metric === 'CLS' ? .01 : 100;
    return `${prefix}|${event.metric}|${Math.min(600, Math.floor(event.value! / step))}`;
  }
  return event.target ? `${prefix}|${event.target}` : prefix;
}
export function returningVisit(state: {firstAt: number; lastAt: number; returned: boolean}, now: number) {
  const age = now - state.firstAt;
  return !state.returned && now - state.lastAt >= 1800000 && age >= 86400000 && age <= 7 * 86400000;
}
