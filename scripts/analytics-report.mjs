import {resolve} from 'node:path';
import {fileURLToPath} from 'node:url';

const dayMs = 86400000;
const metrics = ['LCP', 'INP', 'CLS'];
const eventNames = new Set(['page_view', 'new_browser', 'session_start', 'return_7d', 'next_guide_click', 'video_click', 'tool_use', 'bookmark_save', 'budget_save', 'checklist_save', 'web_vital']);
const targets = new Set(['character', 'budget', 'checklist', 'calendar', 'equipment', 'classes', 'videos', 'growth']);

/** @param {string} date */
function dateTime(date) {
  const value = Date.parse(`${date}T00:00:00Z`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !Number.isFinite(value) || new Date(value).toISOString().slice(0, 10) !== date) throw new Error('Dates must be valid YYYY-MM-DD UTC dates.');
  return value;
}

/** @param {string[]} args @param {number} [now] */
export function reportDates(args, now = Date.now()) {
  let from;
  let to;
  if (!args.length) from = to = new Date(now).toISOString().slice(0, 10);
  else if (args.length === 1 && !args[0].startsWith('--')) from = to = args[0];
  else {
    const values = new Map();
    for (let i = 0; i < args.length; i += 2) {
      if (!['--from', '--to'].includes(args[i]) || !args[i + 1] || values.has(args[i])) throw new Error('Usage: analytics-report.mjs [YYYY-MM-DD] or --from YYYY-MM-DD --to YYYY-MM-DD');
      values.set(args[i], args[i + 1]);
    }
    from = values.get('--from'); to = values.get('--to');
    if (!from || !to) throw new Error('Both --from and --to are required.');
  }
  const start = dateTime(from);
  const end = dateTime(to);
  if (start > end || end > now || now - start > 35 * dayMs || (end - start) / dayMs >= 35) throw new Error('Choose an ordered range of up to 35 days within available storage, with no future dates.');
  return Array.from({length: (end - start) / dayMs + 1}, (_, i) => new Date(start + i * dayMs).toISOString().slice(0, 10));
}

/** @param {Map<number, number>} bins @param {string} metric */
function histogram(bins, metric) {
  const count = [...bins.values()].reduce((a, b) => a + b, 0);
  if (!count) return {samples: 0, p75: null, availability: metric === 'INP' ? 'Unavailable: no eligible interaction samples.' : 'Unavailable: no samples.'};
  const rank = Math.ceil(count * .75);
  let cumulative = 0;
  let selected = 0;
  for (const [bin, frequency] of [...bins].sort((a, b) => a[0] - b[0])) {
    cumulative += frequency;
    if (cumulative >= rank) {selected = bin; break;}
  }
  const step = metric === 'CLS' ? .01 : 100;
  const lower = Number((selected * step).toFixed(metric === 'CLS' ? 2 : 0));
  const upper = selected === 600 ? (metric === 'CLS' ? 10 : 60000) : Number(((selected + 1) * step).toFixed(metric === 'CLS' ? 2 : 0));
  return {samples: count, p75: {lowerInclusive: lower, upper, upperInclusive: selected === 600, unit: metric === 'CLS' ? 'score' : 'ms'}, availability: 'Available', smallSample: count < 30};
}

/** @typedef {{date: string, counters: Record<string, number>}} CounterDay */
/** @param {CounterDay[]} days @param {number} [now] */
export function summarizeAnalytics(days, now = Date.now()) {
  const totals = Object.fromEntries([...eventNames].map((name) => [name, 0]));
  const toolCounts = Object.fromEntries([...targets].map((target) => [target, 0]));
  /** @type {Map<string, {pageViews: number, nextGuideClicks: number, toolUses: number}>} */
  const pages = new Map();
  /** @type {Map<string, Map<number, number>>} */
  const bins = new Map(metrics.map((metric) => [metric, new Map()]));
  const cohorts = [];
  for (const {date, counters} of days) {
    const cohort = {date, mature: dateTime(date) + 8 * dayMs <= now, newBrowsers: 0, returnedBrowsers: 0};
    for (const [field, count] of Object.entries(counters)) {
      const [locale, path, name, detail, bin, ...extra] = field.split('|');
      if (!Number.isSafeInteger(count) || count <= 0 || extra.length || !['en', 'ja', 'es', 'de'].includes(locale) || !/^\/(?:[a-z0-9-]+(?:\/[a-z0-9-]+)*)?$/.test(path) || !eventNames.has(name)) throw new Error('Unexpected aggregate counter format.');
      if (name === 'web_vital') {
        if (!metrics.includes(detail) || !/^\d+$/.test(bin || '') || Number(bin) > 600) throw new Error('Unexpected metric histogram format.');
        const histogram = bins.get(detail);
        histogram.set(Number(bin), (histogram.get(Number(bin)) || 0) + count);
      } else {
        if (bin !== undefined || (detail !== undefined && !targets.has(detail))) throw new Error('Unexpected tool counter format.');
      }
      totals[name] += count;
      const pageKey = `${locale}|${path}`;
      const page = pages.get(pageKey) || {pageViews: 0, nextGuideClicks: 0, toolUses: 0};
      if (name === 'page_view') page.pageViews += count;
      if (name === 'next_guide_click') page.nextGuideClicks += count;
      if (name === 'tool_use') {page.toolUses += count; if (detail) toolCounts[detail] += count;}
      pages.set(pageKey, page);
      if (name === 'new_browser') cohort.newBrowsers += count;
      if (name === 'return_7d') cohort.returnedBrowsers += count;
    }
    cohorts.push({...cohort, returnRatePercent: cohort.mature && cohort.newBrowsers ? cohort.returnedBrowsers / cohort.newBrowsers * 100 : null, inconsistent: cohort.returnedBrowsers > cohort.newBrowsers});
  }
  const mature = cohorts.filter((cohort) => cohort.mature);
  const denominator = mature.reduce((sum, cohort) => sum + cohort.newBrowsers, 0);
  const numerator = mature.reduce((sum, cohort) => sum + cohort.returnedBrowsers, 0);
  return {
    dates: days.map(({date}) => date),
    currentUtcDatePartial: days.some(({date}) => date === new Date(now).toISOString().slice(0, 10)),
    totals,
    retention: {definition: 'Browsers first observed on a cohort date that return after 1–7 elapsed days and at least 30 minutes since the previous recorded page visit, counted once locally. Mature cohorts only; a full cohort day plus seven days must have elapsed.', newBrowsers: denominator, returnedBrowsers: numerator, returnRatePercent: denominator ? numerator / denominator * 100 : null, smallSample: denominator < 30, inconsistent: numerator > denominator, cohorts},
    vitals: Object.fromEntries(metrics.map((metric) => [metric, histogram(bins.get(metric), metric)])),
    interactions: {
      denominator: 'Page-view events in the same selected dates; event counts per 100 page views, not unique-browser conversion rates.',
      pageViews: totals.page_view,
      nextGuideClicks: totals.next_guide_click,
      nextGuideClicksPer100PageViews: totals.page_view ? totals.next_guide_click / totals.page_view * 100 : null,
      toolUses: totals.tool_use,
      toolUsesPer100PageViews: totals.page_view ? totals.tool_use / totals.page_view * 100 : null,
      tools: toolCounts,
      byPage: Object.fromEntries([...pages].filter(([, page]) => page.pageViews || page.nextGuideClicks || page.toolUses).map(([key, page]) => [key, {...page, nextGuideClicksPer100PageViews: page.pageViews ? page.nextGuideClicks / page.pageViews * 100 : null, toolUsesPer100PageViews: page.pageViews ? page.toolUses / page.pageViews * 100 : null}])),
    },
    notes: ['Counts describe browsers with local storage and statistics enabled, not unique people. Clearing storage or changing browsers creates a new browser cohort.', 'DNT, GPC, opt-outs, blockers, failed network requests and sampling availability reduce coverage.', 'p75 is a histogram interval estimate, not an exact raw percentile. Small samples are flagged below 30 observations.', 'Retention return events are stored on the original cohort date; totals.return_7d is not the number of returns occurring during the selected dates.'],
  };
}

async function main() {
  const token = process.env.ANALYTICS_READ_TOKEN;
  if (!token) throw new Error('Set ANALYTICS_READ_TOKEN in the environment.');
  const base = new URL(process.env.QA_BASE_URL || 'http://127.0.0.1:3000');
  if (!['http:', 'https:'].includes(base.protocol) || base.username || base.password) throw new Error('QA_BASE_URL must be an HTTP(S) URL without credentials.');
  const dates = reportDates(process.argv.slice(2));
  const days = [];
  for (const date of dates) {
    const url = new URL('/api/analytics', base); url.searchParams.set('date', date);
    const response = await fetch(url, {headers: {Authorization: `Bearer ${token}`}, signal: AbortSignal.timeout(10000), redirect: 'error'});
    if (!response.ok) throw new Error(`Analytics read failed (${response.status}) for ${date}.`);
    const result = await response.json();
    if (result.date !== date || !result.counters || typeof result.counters !== 'object' || Array.isArray(result.counters)) throw new Error('Unexpected analytics read response.');
    days.push(result);
  }
  process.stdout.write(`${JSON.stringify(summarizeAnalytics(days), null, 2)}\n`);
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(() => {process.stderr.write('Analytics report failed. Check dates, QA_BASE_URL, read-token authorization and server availability.\n'); process.exitCode = 1;});
}
