import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[3]
evidence = json.loads((ROOT / 'observations.json').read_text(encoding='utf-8'))
observations = []
by_query = {}
for batch in evidence['batches']:
    for row in batch['rows']:
        item = dict(row, mode=batch['mode'], sourceUrl=batch['url'], observedAt=batch['observedAt'])
        observations.append(item)
        by_query.setdefault(row['keyword'], []).append(item)

# 人工判断任务、分类、同义词和承接页面；数值只从本轮 UI 观察读取。
# canonical, representative raw query, other raw variants, category, priority, current/possible path, action, gap
decisions = [
    ('aion 2 max level', 'aion 2 max level', [], 'level cap', 'P1', '/leveling#global-leveling', '维护已有答案', '已有 Global/KR/TW 等级上限说明；优化关键词入口，更新时复核官方版本。'),
    ('aion 2 dps meter', 'aion 2 dps meter', [], 'damage meters', 'P1', '/notmeter', '补充已有页', '已有 NotMeter 安装与 DPS 说明；可加强通用 DPS meter 意图和 Global 兼容说明。'),
    ('aion 2 global changes', 'aion 2 global changes', ['aion 2 global change'], 'regional version differences', 'P1', '/global-changes（计划）', '候选新页', '独立整理 Global 与 KR/TW 差异；逐项补地区、版本与官方证据。'),
    ('aion 2 how to play on taiwan server', 'how to play aion 2 on taiwan server', [], 'regional installation', 'P2', '/download；/taiwan-server-guide（计划）', '候选区域教程', '已有地区入口说明；完整 TW 注册、客户端、语言、地区限制步骤仍需核验。'),
    ('aion 2 private server', 'aion 2 private server', [], 'private servers', 'P3', '/private-server（计划）', '暂缓', '需求存在；须核实是否为 AION 2，避免混入 AION 1 私服和未证实服务。'),
    ('aion 2 global server', 'aion2 global server', [], 'server regions', 'P2', '/server', '维护已有页', '已有 Global 大区和服务器；继续区分 TW/KR 与 Global 服务。'),
    ('aion 2 console release', 'aion 2 console release', [], 'console availability', 'P2', '/steam#platform-and-controller-support', '补充已有 FAQ', '核实主机发行公告；缺少公告不能写成永久不支持。'),
    ('aion 2 how to play', 'aion 2 how to play', ['how to play aion2', 'how to play aion 2', 'aion 2 how tp play'], 'getting started', 'P2', '/guide；/download', '合并到已有页', '统一入门与安装意图；不同原始问法的搜索量和 KD 分别保留，不相加。'),
    ('aion 2 new class', 'aion 2 new class', [], 'class availability', 'P2', '/classes#brawler-and-regional-guides', '维护已有答案', '已有 Brawler 地区区别；Global 新职业开放状态待官方更新。'),
    ('aion 2 eu release date', 'aion2 eu release date', [], 'regional release schedule', 'P2', '/steam#access-schedule', '维护已有答案', '已有 Global 开放时间；按欧洲时区和当前阶段核对。'),
    ('aion 2 class change', 'aion 2 class change', [], 'class switching', 'P1', '/classes（拟补 FAQ）', '补充已有页', '现有职业页没有完整转职答案；先核实是否支持、操作与限制，不推断机制。'),
    ('aion 2 gathering map', 'aion 2 gathering map', [], 'gathering locations', 'P1', '/gathering#gathering-routes；/map', '维护已有答案', '已有地图筛选与采集路线；可增强资源筛选示例和入口。'),
    ('aion 2 talent calculator', 'aion 2 talent calculator', [], 'talent planning tools', 'P1', '/builds；/talent-calculator（计划）', '候选工具', '需核对 Global 天赋数据、节点与点数规则；不能把现有角色查询工具算作天赋计算器。'),
    ('aion 2 what does quna do', 'aion 2 what does quna do', [], 'premium currency uses', 'P2', '/monetization#currency-and-trading', '维护已有答案', '已有 Quna 用途与兑换说明；当前 28 天量低于 50，先做 FAQ。'),
    ('aion 2 how many players per server', 'how many players has an aion 2 server', [], 'server capacity', 'P2', '/server（拟补 FAQ）', '补充已有页', '这是单服容量/人数需求；与全游戏并发不同，缺官方容量数字时不编造。'),
    ('aion 2 eu server location', 'aion 2 eu server location', [], 'server hosting locations', 'P2', '/server（拟补 FAQ）', '补充已有页', '需要欧洲服务器物理部署地点证据；不能从大区名称推出机房城市。'),
    ('aion 2 raid 2026', 'aion 2 raid 2026', [], 'raid access', 'P3', '/raid-guide（计划）', '待核实意图', '需要确认指向哪一地区、版本、团本与入口；低量宽泛词先观察。'),
    ('aion 2 taiwan discord', 'aion 2 taiwan discord', [], 'regional community resources', 'P2', '/guide#community-resources', '补充已有页', '以地区社区导航满足需求；核验邀请链接与官方/社区身份。'),
    ('aion 2 fishing release', 'aion2 fishing release', [], 'fishing availability', 'P3', '/fishing（计划）', '待核实意图', '需要确认真实机制、地区和开放公告；本轮工具词不能证明钓鱼已经开放。'),
    ('aion 2 are maps connected to aion 1', 'are aion 2 maps connected to aion 1', [], 'world map continuity', 'P3', '/map（拟补 FAQ）', '补充已有页', '核实两代地图/世界关系和区域名称；先按简短 FAQ 处理。'),
    ('aion 2 can i use vpn and connect to japan to play', 'can i use vpn and connect to japan to play aion 2?', [], 'regional service access', 'P3', '/download（拟补 FAQ）', '补充已有页', '核实服务地区、账号与平台限制；不把 VPN 当作已实测可用结论。'),
    ('aion 2 how much do i have to p2w in global release', 'how much do i have to p2w in aion 2 global release', [], 'global spending expectations', 'P2', '/monetization', '补充已有页', '已有商业模式；不能仅凭需求给付费强度或最小花费数字，需实际 Global 依据。'),
]

groups = []
for canonical, primary, variants, category, priority, path, action, gap in decisions:
    queries = [primary, *variants]
    metrics = []
    for query in queries:
        rows = by_query[query]
        row = rows[0]
        assert 1 <= int(row['kd']) <= 20
        metrics.append({
            'rawQuery': query,
            'volume28dDisplay': row['volume28d'],
            'averageVolumeDisplay': row['averageVolume'],
            'kd': int(row['kd']),
            'zeroClickDisplay': row['zeroClick'],
            'intentDisplay': row['intent'],
            'cpcDisplay': row['cpc'],
            'observations': [{'mode': r['mode'], 'sourceUrl': r['sourceUrl'], 'observedAt': r['observedAt']} for r in rows],
        })
    groups.append({
        'keyword': canonical,
        'category': category,
        'priority': priority,
        'representativeRawQuery': primary,
        'rawQueries': metrics,
        'currentOrPlannedPath': path,
        'action': action,
        'contentGap': gap,
        'serpCompetition': '本轮未检查 SERP；仅有 Similarweb 工具 KD',
        'gameFactsValidatedThisRun': False,
    })

assert len(groups) == 22
assert len({g['keyword'] for g in groups}) == len(groups)
assert all(g['keyword'].startswith('aion 2 ') for g in groups)
selected_queries = {q['rawQuery'] for g in groups for q in g['rawQueries']}
unique_queries = set(by_query)
library = json.loads((PROJECT / 'keywords.json').read_text(encoding='utf-8'))
library_words = {k for c in library['categories'] for k in c['keywords']}

def strict_aion2(query):
    return bool(re.search(r'\baion\s*2\b', query, re.I))

def non_english(query):
    return bool(re.search(r'[\u3040-\u30ff\u4e00-\u9fff\u0400-\u04ff]', query)) or query in {
        'aion 2 combien de slot characters max',
        'aion 2 quels sont les classes les plus jouées a taiwan',
    }

unselected = []
for query in sorted(unique_queries - selected_queries):
    row = by_query[query][0]
    if query in {'aion2chapterone', 'aeon 2 release date', 'is iaon 2 already released in some places', 'recent aion 2 chances'}:
        reason = '主题或拼写存在歧义，保留原词待核实；不擅自纠正为新需求。'
    elif not strict_aion2(query):
        reason = '未确认属于 AION 2：同名商品、其他游戏或无关查询，排除英语长尾主清单。'
    elif non_english(query):
        reason = '非英语观察；保留原词和原指标，不能直接当成英语搜索量。'
    else:
        reason = '核心短词、导航词或模糊需求；保留低 KD 观察，不计入精选长尾组。'
    unselected.append({'rawQuery': query, 'volume28dDisplay': row['volume28d'], 'averageVolumeDisplay': row['averageVolume'], 'kd': int(row['kd']), 'reason': reason})

summary = {
    'observations': len(observations),
    'uniqueRawQueries': len(unique_queries),
    'readTableCounts': {b['mode']: len(b['rows']) for b in evidence['batches']},
    'selectedEnglishRawQueries': len(selected_queries),
    'selectedEnglishIntentGroups': len(groups),
    'groupsWithRepresentativeKDAtMost10': sum(g['rawQueries'][0]['kd'] <= 10 for g in groups),
    'groupsWithRepresentative28dVolumeAtLeast50': sum(not g['rawQueries'][0]['volume28dDisplay'].startswith('<') for g in groups),
    'groupsWithRepresentative28dVolumeBelow50': sum(g['rawQueries'][0]['volume28dDisplay'].startswith('<') for g in groups),
    'priorities': dict(Counter(g['priority'] for g in groups)),
    'exactCanonicalQueriesAlreadyIn63WordLibrary': sum(g['keyword'] in library_words for g in groups),
    'unselectedUniqueQueries': len(unselected),
}
result = {
    'schemaVersion': 1,
    'source': 'Similarweb browser UI',
    'market': evidence['market'],
    'searchEngine': evidence['searchEngine'],
    'device': evidence['device'],
    'dataAsOf': evidence['dataAsOf'],
    'timeWindow': evidence['timeWindow'],
    'collectedAt': evidence['collectedAt'],
    'timezone': 'Asia/Shanghai',
    'summary': summary,
    'selectionPolicy': [
        '人工选取更具体的玩家任务、条件或工具查询，合并同一答案的词序/拼写变体。',
        '代表词统一 aion 2 前缀；只纠错、重排已有词和统一主题，不拼接未出现的长尾词。',
        '精选组均有实际读取的 KD 1–20；优先 KD ≤10。',
        '同义词各自指标保留，不相加、不跨词形转移 KD。',
        '同一承接页的不同问题仍可分组；22 组不等于 22 张新页。',
        '低 KD 不是实战 SERP 竞争结论；本轮不验证游戏机制、不实施内页。',
        '保留 <50 和缺失标记；28 天体量与平均体量分列。',
    ],
    'groups': groups,
    'unselectedQueries': unselected,
}

with (ROOT / 'selected-keywords.json').open('x', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')

with (ROOT / 'long-tail.csv').open('x', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['keyword', 'raw_query', 'category', 'priority', 'volume_28d_display', 'average_volume_display', 'kd', 'zero_click_display', 'action', 'current_or_planned_path', 'gap', 'source_url', 'observed_at_utc'])
    for g in groups:
        for q in g['rawQueries']:
            source = q['observations'][0]
            writer.writerow([g['keyword'], q['rawQuery'], g['category'], g['priority'], q['volume28dDisplay'], q['averageVolumeDisplay'], q['kd'], q['zeroClickDisplay'], g['action'], g['currentOrPlannedPath'], g['contentGap'], source['sourceUrl'], source['observedAt']])

lines = [
    '# AION 2 · Similarweb 低 KD 长尾词收集',
    '',
    f"**收集 {summary['selectedEnglishRawQueries']} 个英语原始长尾查询，合并为 22 组需求；其中 {summary['groupsWithRepresentativeKDAtMost10']} 组代表查询 KD ≤10。**",
    '',
    '- 采集：2026-10-04，北京时间 10:45–10:47。通过 browser computer-use 实际读取已登录 Similarweb。',
    '- 口径：Worldwide / Google / All traffic / Last 28 days；页面标注 As of Sep 30，即数据截至 2026-09-30。',
    '- 筛选：KD 1–20，无搜索量下限。UI 标签为 <20，但结果中实际包含 KD 20，按读到的值记录。',
    '- 完整读取：语句匹配 98 条、相关词 72 条、问题词 10 条，三表均只有一页；共 180 条观察。热门词表和其他种子不在本次范围。',
    f"- 原始查询去重 {summary['uniqueRawQueries']} 个；其他词及排除原因保留在 selected-keywords.json。", 
    f"- 精选代表查询中，{summary['groupsWithRepresentative28dVolumeAtLeast50']} 组近期体量 ≥50，{summary['groupsWithRepresentative28dVolumeBelow50']} 组显示 <50。", 
    '- 搜索量与 KD 均为 Similarweb 工具估计。低 KD 不保证能排名；本轮没有核验真实 Google SERP。',
    '- 本轮只收集数据、人工分组和提出承接方案；游戏机制、菜单、工具兼容等仍须按 Global/KR/TW 补来源。',
    '- 同一答案的词形合并；不同问题可在同页补 FAQ，因此 22 组不等于 22 张新页。',
    '',
    '## 先看这 6 组',
    '',
    '| 英语关键词 | 最近 28 天体量 | 平均体量 | KD | 零点击 | 处理方式 |',
    '| --- | ---: | ---: | ---: | ---: | --- |',
]
for g in groups:
    if g['priority'] == 'P1':
        q = g['rawQueries'][0]
        lines.append(f"| `{g['keyword']}` | {q['volume28dDisplay']} | {q['averageVolumeDisplay']} | {q['kd']} | {q['zeroClickDisplay']} | {g['action']}：{g['currentOrPlannedPath']} |")
lines.extend(['', 'P1 是本轮调查/维护顺序，不代表都已具备制作证据。Global changes、class change 和 talent calculator 先补事实或数据。', '', '## 全部精选组', '', '| 优先级 | 规范关键词 | 代表原始查询 | 28 天体量 | 平均体量 | KD | 承接/计划 |', '| --- | --- | --- | ---: | ---: | ---: | --- |'])
for g in groups:
    q = g['rawQueries'][0]
    lines.append(f"| {g['priority']} | `{g['keyword']}` | `{q['rawQuery']}` | {q['volume28dDisplay']} | {q['averageVolumeDisplay']} | {q['kd']} | {g['currentOrPlannedPath']} |")
lines.extend(['', '## 同义词指标不能互相替换', '', '| 规范组 | 实际读取原词 | 28 天体量 | 平均体量 | KD |', '| --- | --- | ---: | ---: | ---: |'])
for g in groups:
    if len(g['rawQueries']) > 1:
        for q in g['rawQueries']:
            lines.append(f"| `{g['keyword']}` | `{q['rawQuery']}` | {q['volume28dDisplay']} | {q['averageVolumeDisplay']} | {q['kd']} |")
lines.extend(['', '例如 `aion 2 how to play` 为 420 / KD13，而 `how to play aion 2` 为 <50 / KD6；不能组合成 420 / KD6。', '', '## 每组内容缺口', ''])
for g in groups:
    lines.append(f"- **{g['keyword']}**：{g['contentGap']}")
lines.extend(['', '## 保存文件', '', '- [原始 UI 观察](observations.json)：180 条，保留词形、指标、来源 URL、采集时间。', '- [人工精选与排除记录](selected-keywords.json)：22 组、原词变体、页面映射、优先级和缺口。', '- [可筛选 CSV](long-tail.csv)：每个原词单独一行，供后续排序。', '', '原 63 词库与 28 个发布主题保持当前记录；新增查询作为本次研究候选保存。后续只有在确认内容价值及事实证据后才决定更新或新增页面。', '', '来源页面：[Similarweb 语句匹配](https://pro.similarweb.com/#/digitalsuite/acquisition/findkeywords/keyword-generator-tool/999/28d?searchEngine=google&keyword=aion%202&webSource=Total&isWWW=*&tab=phraseMatch&difficultyFromValue=1&difficultyToValue=20&multiIncludeExcludeKeywords=%5B%5D)。'])
with (ROOT / 'report.md').open('x', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
