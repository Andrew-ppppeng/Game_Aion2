import copy
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'research/keywords/2026-10-04/implementation'
DATE = '2026-10-04'
OUT.mkdir(exist_ok=True)

def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def write(path, value):
    (ROOT / path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Explicit editorial decisions after source and page review. These are not generated
# from word length, KD thresholds or the mere existence of a destination page.
decisions = {
    'aion 2 max level': ('covered', '/leveling#global-leveling', 'P1', 'Global 45 与 KR/TW 50 分开；补满级后步骤和耗时因素，未编造升级小时数。', 'primary-updates/max-level.md'),
    'aion 2 dps meter': ('covered', '/notmeter#dps-meter-options', 'P1', '比较 NotMeter、Aletheia、OCR、aion2t 的方式、费用、登录和兼容条件；未安装或运行下载的程序。', 'primary-updates/dps-meter.md'),
    'aion 2 global changes': ('new_page_ready', '/global-changes', 'P1', 'Global launch 与 KR/TW Chapter 1 的已确认差异；不冒称两版最新完整变更表。', 'new-pages/source-review.md'),
    'aion 2 how to play on taiwan server': ('covered_with_limits', '/download#taiwan-client', 'P2', '提供 TW 官方客户端下载路径；境外账号、认证和可进入资格仍有限制，安装不等于获得资格。', 'primary-updates/specs-and-download.md'),
    'aion 2 private server': ('deferred', None, 'P3', '暂缓：缺可靠、可维护的独立攻略范围和当前服务证据。', None),
    'aion 2 global server': ('covered', '/server#global-server-regions', 'P2', '同区同阵营同服选择、Steam/PURPLE同服、进度不可从KR/TW转入Global。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 console release': ('covered_with_limits', '/steam#platform-and-controller-support', 'P2', 'Global 当前官方支持 Windows PC；未公布主机日期；控制器可用但非官方支持。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 how to play': ('covered', '/guide#how-to-play-by-region', 'P2', 'NA/EU/TW入口、资格、启动器与组队选择；台湾细节链接下载页。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 new class': ('covered_with_limits', '/classes#brawler-and-regional-guides', 'P2', 'KR/TW Chapter 1 Brawler 与 Global八职业区分；Global Brawler 日期仍未公告。', 'primary-updates/classes.md'),
    'aion 2 eu release date': ('covered', '/steam#europe-launch-time', 'P2', '公开开启10月5日13:00 UTC及BST/CEST/EEST换算；维护变化条件保留。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 class change': ('awaiting_evidence', '/classes', 'P1', '缺当前Global职业转换入口、费用和角色进度处理规则；没有伪造FAQ答案。', 'primary-updates/classes.md'),
    'aion 2 gathering map': ('covered', '/map#gathering-map-filters', 'P1', '资源筛选、搜索、高度与进度导出；采集路线与失败判断放/gathering。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 talent calculator': ('covered', '/builds#talent-calculator', 'P1', '实测Global工具Raise/Lower、预算变化、刷新持久化；账号保存条件明确，未新造独立计算器薄页。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 what does quna do': ('covered', '/monetization#quna-use-and-budget', 'P2', 'Quna商店、pass、货币交换、获取与当地支付条件。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 how many players per server': ('awaiting_evidence', '/server#queues-and-population', 'P2', '单服容量/实时人数缺官方数字；现页只解释队列与Steam总并发区别。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 eu server location': ('awaiting_evidence', '/server#queues-and-population', 'P2', '已知Europe地区；物理机房城市未公告，不猜测Frankfurt等城市。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 raid 2026': ('deferred', None, 'P3', '暂缓：先核实具体raid、地区、年份意图和现行机制。', None),
    'aion 2 taiwan discord': ('covered', '/guide#community-resources', 'P2', '已核验社区邀请并与Global官方Discord分开；不冒称TW官方运营频道。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 fishing release': ('deferred', None, 'P3', '暂缓：缺当前服务钓鱼系统与明确开放日期。', None),
    'aion 2 are maps connected to aion 1': ('deferred', None, 'P3', '暂缓：历史关系与可通行连接不是同一个答案，缺完整证据。', None),
    'aion 2 can i use vpn and connect to japan to play': ('deferred', None, 'P3', '暂缓：缺服务资格与地区规则；不凭VPN技术可连接推断账号合规或必定可玩。', None),
    'aion 2 how much do i have to p2w in global release': ('covered_with_limits', '/monetization#quna-use-and-budget', 'P2', '有免费入场、会员/角色pass/礼包等消费边界；不存在有证据的最低获胜花费。', 'secondary-updates/materials-and-decisions.md'),
    'aion 2 classes': ('covered', '/classes#class-skills-and-gameplay', 'P1', '八职业、图标、职责、技能与PvE/PvP入口；性别锁仍是内部待核实问题。', 'primary-updates/classes.md'),
    'aion 2 wings': ('new_page_ready', '/wings', 'P1', '解锁、飞行、装备与持有属性、外观和PvE选择；未冒称全量数值/强化成本排行。', 'new-pages/source-review.md'),
    'aion 2 database': ('new_page_ready', '/database', 'P1', '物品/技能/掉落/角色查询入口和版本条件；数据库导航指南，不冒称本站完整数据仓库。', 'new-pages/source-review.md'),
    'aion 2 specs': ('covered', '/download#check-your-specs', 'P1', '同义词并入aion 2 system requirements；Windows自查、最低/推荐表和Global平台条件。', 'primary-updates/specs-and-download.md'),
}

library = read('keywords.json')
canonical_categories = {q: group['category'] for group in library['categories'] for q in group['keywords']}
assert len(canonical_categories) == 87
topics = [q for group in read('content-topics.json')['categories'] for q in group['keywords']]
assert len(topics) == 31
selected = read('research/keywords/2026-10-04/similarweb-low-kd/selected-keywords.json')
observed = read('research/keywords/2026-10-04/similarweb-low-kd/observations.json')
autocomplete = read('research/keywords/2026-10-04/google-autocomplete-refresh/observations.json')
serp = read('research/keywords/2026-10-04/google-autocomplete-refresh/serp-observations.json')
review = read('research/keywords/2026-10-04/google-autocomplete-refresh/direction-review.json')
legacy = read('research/keywords/2026-10-03/implementation/keyword-coverage.json')
by_keyword = {group['keyword']: group for group in selected['groups']}
for q in ['aion 2 classes', 'aion 2 wings', 'aion 2 database', 'aion 2 specs']:
    matches = [(batch, row) for batch in observed['batches'] for row in batch['rows'] if row['keyword'] == q]
    assert matches
    by_keyword[q] = {'keyword': q, 'representativeRawQuery': q, 'rawQueries': [{
        'rawQuery': q, 'volume28dDisplay': matches[0][1]['volume28d'],
        'averageVolumeDisplay': matches[0][1]['averageVolume'], 'kd': int(matches[0][1]['kd']),
        'zeroClickDisplay': matches[0][1]['zeroClick'],
        'observations': [{'mode': b['mode'], 'sourceUrl': b['url'], 'observedAt': b['observedAt']} for b, _ in matches]
    }]}
assert set(by_keyword) == set(decisions) and len(decisions) == 26

candidate_rows = []
for q, (status, route, priority, detail, material) in decisions.items():
    row = copy.deepcopy(by_keyword[q])
    row.update({
        'canonicalQuery': 'aion 2 system requirements' if q == 'aion 2 specs' else q,
        'currentStatus': status, 'destinationUrl': route, 'implementationPriority': priority,
        'coverageDetail': detail,
        'materialFile': 'research/content/2026-10-04/keyword-refresh/' + material if material else None,
        'routePublished': bool(route), 'completeAnswer': status in {'covered', 'new_page_ready'},
        'regions': ['Global', 'KR', 'TW'] if q in {'aion 2 max level', 'aion 2 classes', 'aion 2 new class', 'aion 2 wings', 'aion 2 database', 'aion 2 global changes'} else ['TW'] if q == 'aion 2 how to play on taiwan server' else ['Global'],
        'localizedDestinationUrls': {locale: ('/' + locale + route if locale != 'en' else route) for locale in ['en','ja','es','de']} if route else {},
        'volumePolicy': 'Raw-query 28-day and average metrics are separate; aliases are not summed and inherit no new metric.',
    })
    candidate_rows.append(row)

refresh_slugs = {'classes','leveling','download','notmeter','map','gathering','server','steam','guide','monetization','builds'}
canonical_rows = []
for old in legacy['originalKeywords']:
    row = copy.deepcopy(old)
    q = row['originalQuery']
    row['canonicalQuery'] = q
    row['category'] = canonical_categories[q]
    row['previousCoverageFile'] = 'research/keywords/2026-10-03/implementation/keyword-coverage.json'
    route = row.get('destinationUrl')
    row['refreshedOn'] = DATE if route and route.split('#')[0].lstrip('/') in refresh_slugs else None
    row['previousGap'] = row.get('gap')
    if q == 'aion 2 controller':
        row['gap'] = '官方Launch FAQ确认控制器可用但非官方支持；未逐手柄独立测试。'
    elif q == 'aion 2 notmeter':
        row['gap'] = '比较四种DPS工具；NotMeter及OCR等未安装运行，不把Aletheia的Global显示模式当国际服兼容。'
    elif q == 'aion 2 founders pack':
        row['gap'] = '10/3公告外观全账号/服务器共享待EA后实施；30天会员及两个箱子仍一次性。'
    elif q == 'aion 2 system requirements':
        row['gap'] = '当前Steam配置与Windows自查步骤；不保证帧率、跨区域账户资格或移动端支持。'
    if q in decisions:
        row['latestDemandRefresh'] = {'status': decisions[q][0], 'detail': decisions[q][3]}
    canonical_rows.append(row)
existing = {row['canonicalQuery'] for row in canonical_rows}
for row in candidate_rows:
    q = row['canonicalQuery']
    if q not in existing:
        canonical_rows.append({**copy.deepcopy(row), 'category': canonical_categories[q], 'addedOn': DATE})
        existing.add(q)
assert existing == set(canonical_categories) and len(canonical_rows) == 87

status_counts = dict(Counter(row['currentStatus'] for row in candidate_rows))
summary = {
    'canonicalKeywords': 87, 'originalKeywords': 63, 'addedCanonicalKeywords': 24,
    'approvedIntentCandidates': 26, 'historicalPriority20': 20,
    'publishedTopics': 31, 'publishedLocalizedArticles': 124,
    'updatedExistingTopics': sorted(refresh_slugs), 'updatedLocalizedArticles': 44,
    'newTopics': ['wings', 'database', 'global-changes'], 'newLocalizedArticles': 12,
    'candidateStatusCounts': status_counts,
    'completeCandidateAnswers': sum(row['completeAnswer'] for row in candidate_rows),
    'candidateAnswersWithLimits': status_counts.get('covered_with_limits',0),
    'candidateAwaitingEvidence': status_counts.get('awaiting_evidence',0),
    'candidateDeferred': status_counts.get('deferred',0),
    'autocompleteSeeds': autocomplete['seedCount'],
    'autocompleteObservationCount': autocomplete['suggestionObservations'],
    'reviewedQueryLeadObservations': sum(len(row['keptAsQueryLeads']) for row in review['decisions']),
    'actualSerpSeeds': len(serp['observations']),
    'renderedResultHeadingObservations': sum(len(row['results']) for row in serp['observations']),
    'legacyCoverageStatusCounts': dict(Counter(row['currentStatus'] for row in legacy['originalKeywords'])),
    'legacyScopeCaution': 'Original 63 statuses are carried forward with refreshed details. Page updates do not resolve every historical evidence gap; do not calculate backlog as keyword count minus topic count.',
}
coverage = {
    'schemaVersion': 2, 'createdAt': datetime.now(timezone.utc).isoformat(), 'reportDate': DATE,
    'timezone': 'Asia/Shanghai', 'scope': 'Local implementation; not deployment, indexed-page confirmation, live ranking or traffic growth.',
    'summary': summary,
    'statusDefinitions': {'covered': 'Approved player question answered within defined scope.', 'new_page_ready': 'Four-locale new topic registered and locally ready; deployment is separate.', 'covered_with_limits': 'Useful answer exists but important availability, access or spending condition remains.', 'awaiting_evidence': 'Destination helps with adjacent information, but the requested critical fact is still unanswered.', 'deferred': 'No new page or unsupported answer published for this candidate.'},
    'sources': {
        'similarweb': {'file': 'research/keywords/2026-10-04/similarweb-low-kd/observations.json', 'market': 'Worldwide', 'searchEngine': 'Google', 'device': 'All traffic', 'timeWindow': 'Last 28 days', 'dataAsOf': '2026-09-30', 'filter': 'KD 1–20 inclusive; no minimum volume', 'originalSelectionFile': 'research/keywords/2026-10-04/similarweb-low-kd/selected-keywords.json', 'selectionCorrectionFile': 'research/keywords/2026-10-04/similarweb-low-kd/selection-review.md'},
        'google': {'autocompleteFile': 'research/keywords/2026-10-04/google-autocomplete-refresh/observations.json', 'serpFile': 'research/keywords/2026-10-04/google-autocomplete-refresh/serp-observations.json', 'directionFile': 'research/keywords/2026-10-04/google-autocomplete-refresh/direction-review.json', 'language': 'English UI', 'displayedRegion': 'Hong Kong footer; personalized session', 'metrics': 'KD and volume null; no third-party SERP-extension metrics copied'},
        'facts': {'checkedAt': DATE, 'rawMaterialsRoot': 'research/content/2026-10-04/keyword-refresh', 'regions': ['Global','KR','TW'], 'versionPolicy': 'Regional and test-client data are explicitly scoped; no old-client data is silently treated as current Global.'},
    },
    'canonicalKeywords': canonical_rows, 'approvedCandidates': candidate_rows,
    'validationFile': 'research/keywords/2026-10-04/implementation/validation.json',
    'followUp': {'trigger': 'Actual deployment date D0', 'gscProperty': 'aion2wiki.space', 'daysAfterDeployment': [14,30], 'metrics': ['index status','page and query impressions','clicks','CTR','position','country'], 'missingMetricPolicy': 'Unknown/pending is null, not zero.', 'scheduleCreated': False},
}
write(str((OUT/'keyword-coverage.json').relative_to(ROOT)), coverage)

table_header = '| 需求 | 近28天体量 | KD | 本轮状态 | 承接 |\n| --- | ---: | ---: | --- | --- |\n'
status_labels = {'covered':'已覆盖','new_page_ready':'新页就绪','covered_with_limits':'有答案，保留限制','awaiting_evidence':'关键答案待证据','deferred':'暂缓'}
rows = []
for row in candidate_rows:
    metric = next(raw for raw in row['rawQueries'] if raw['rawQuery'] == row['representativeRawQuery'])
    rows.append(f"| {row['keyword']} | {metric['volume28dDisplay']} | {metric['kd']} | {status_labels[row['currentStatus']]} | {row['destinationUrl'] or '未发布'} |")
coverage_md = '# 本轮逐词实施覆盖 · 2026-10-04\n\n'
coverage_md += f"26组候选：**{summary['completeCandidateAnswers']}组按本轮范围已覆盖，4组有重要限制，3组关键答案待证据，5组暂缓**。3个新主题、11个既有主题更新；词库87项、发布31主题/124篇四语文章。页面数量与需求数量不做减法。\n\n"
coverage_md += table_header + '\n'.join(rows) + '\n\n'
coverage_md += 'Similarweb口径：Worldwide / Google / All traffic / Last28days / 数据截至2026-09-30；不是月均量。<50保留原显示，同义词不相加。逐原词平均量、KD、链接与观察时间见keyword-coverage.json。原22组精选及本次4组补选来源均保留。\n\n'
coverage_md += 'Google实读16种子、145条联想观察，人工保留103条研究线索观察；8个实际结果页、63条页面标题观察。英语UI、当前个性化会话页脚Hong Kong，不代表US或全球排名。联想未批量扩写入词库。\n\n'
coverage_md += '原63项的历史状态独立保留：50项已承接，7项存在内容或证据限制，6项尚未实施；本轮不是全部历史缺口清零。详见JSON中的canonicalKeywords和previousCoverageFile。\n'
(OUT/'coverage.md').write_text(coverage_md, encoding='utf-8')

material_path = ROOT/'关键词素材.md'
original_material = material_path.read_bytes()
marker = '## 2026-10-04 低 KD 内页更新素材补充'
assert marker not in original_material.decode('utf-8')
append = '\n\n' + marker + '\n\n'
append += '本轮26组候选逐词留档。Similarweb为Worldwide/Google/Alltraffic，数据截至9月30日近28天；Google为10月4日实际个性化英语搜索会话，页脚Hong Kong。旧资料保留，指标不跨同义词相加。玩家页不展示研究来源讨论，内部原件和版本条件见链接。\n'
for row in candidate_rows:
    metric = next(raw for raw in row['rawQueries'] if raw['rawQuery'] == row['representativeRawQuery'])
    append += f"\n### {row['keyword']} · 2026-10-04\n\n"
    append += f"- 指标：近28天 {metric['volume28dDisplay']}；平均体量 {metric['averageVolumeDisplay']}；KD {metric['kd']}。保留原词 `{metric['rawQuery']}`，不是月均量。\n"
    append += f"- 状态：{status_labels[row['currentStatus']]}；承接：`{row['destinationUrl'] or '未发布'}`；优先级：{row['implementationPriority']}。\n"
    append += f"- 范围与条件：{row['coverageDetail']}\n"
    if row['materialFile']:
        append += f"- 单独素材：[来源、地区、版本与缺口]({row['materialFile']})。\n"
    append += '- 搜索证据：[Similarweb原观察](research/keywords/2026-10-04/similarweb-low-kd/observations.json)；[Google联想方向](research/keywords/2026-10-04/google-autocomplete-refresh/direction-review.json)。\n'
    if row['canonicalQuery'] != row['keyword']:
        append += f"- 同义归并：`{row['canonicalQuery']}`，不重复建页，不转移原词指标。\n"
material_path.write_bytes(original_material + append.encode('utf-8'))
after = material_path.read_bytes()
assert after[:len(original_material)] == original_material
priority_path = ROOT/'keywords-priority-20.json'
write(str((OUT/'preservation.json').relative_to(ROOT)), {'materialsOriginalByteCount': len(original_material), 'materialsOriginalSha256': hashlib.sha256(original_material).hexdigest(), 'originalPrefixPreserved': True, 'historicalPriority20Sha256': hashlib.sha256(priority_path.read_bytes()).hexdigest(), 'previousCoverageUnmodifiedSha256': hashlib.sha256((ROOT/'research/keywords/2026-10-03/implementation/keyword-coverage.json').read_bytes()).hexdigest()})
print(json.dumps(summary, ensure_ascii=False))
