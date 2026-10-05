"""Append-only coverage archive. Mappings are editorial decisions, not SEO scores."""
import datetime
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
def read_json(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))

corpus = read_json('keywords.json')
first = read_json('keywords-priority-20.json')
manifest = read_json('content-topics.json')
evidence = read_json('research/keywords/2026-10-03/evidence.json')
similarweb = read_json('research/keywords/2026-10-03/implementation/similarweb-plan-observations.json')
first_keywords = {q for c in first['categories'] for q in c['keywords']}
published_keywords = [q for c in manifest['categories'] for q in c['keywords']]
published_slugs = {q.removeprefix('aion 2 ').replace(' ', '-') for q in published_keywords}
locales = ['en', 'ja', 'es', 'de']

def mapping(url, priority, status, gap, next_step, planned=None, support=None):
    return dict(destinationUrl=url, priority=priority, currentStatus=status, gap=gap,
                nextStep=next_step, plannedUrl=planned, supportingUrl=support)

# Full original corpus: every decision below was reviewed manually.
MAP = {
 'guide': mapping('/guide','P0','existing_page_updated','社区来源不是当前游戏规则；Bahamut本次直接访问403。','保留官方/社区与Global/KR/TW区分，按GSC具体问题补强。'),
 'leveling': mapping('/leveling','P3','existing_page','TW路线与耗时不保证Global适用。','有当前Global任务截图或用户问题时更新对应步骤。'),
 'gathering': mapping('/gathering','P3','existing_page','地域版采集与材料规则需持续按地区核对。','跟踪Global获取任务，不与Odyle能量公式混用。'),
 'classes': mapping('/classes','P0','existing_page_updated','已有八职业官方图标识别；不证明统一伤害排名。','跟踪职业选择/图标查询表现，维护八职业名称与来源。'),
 'chanter': mapping('/chanter','P0','existing_page_updated','区域角色序盘模拟不等于Global最终配点。','按当前Global技能特性验证起步循环。'),
 'tier list': mapping('/tier-list','P0','existing_page_updated','作者观点不构成测量过的Global职业排序。','按具体活动解释推荐，链接实际起步决策。'),
 'gladiator': mapping('/gladiator','P1','new_page_ready','区域角色示例的精确Global等级/配点与最终坦克能力未独立验证。','取得当前Global技能描述后补精确配置，先维护已有实用起步选择。'),
 'ranger': mapping('/ranger','P1','new_page_ready','Snipe–Deadshot/暴击触发为来源实例；TW/Global盘不同，无通用暴击阈值。','按目标技能验证Global节点与已选特性。'),
 'spiritmaster': mapping('/spiritmaster','P1','new_page_ready','四精灵顺序与冷却优先来自区域序盘例，Global最优顺序/数值/节点未核实。','对照当前Global召唤效果及Daevanion，补经验证的选择。'),
 'brawler': mapping('/classes#brawler-and-regional-guides','P3','partially_covered','Global八职业官方名单未建立Brawler可选状态。','保留KR/TW更新说明；Global确认可选后再立独立页。'),
 'class quiz': mapping(None,'P3','deferred','现有角色筛选不是完整问答测评；核心职业内容优先。','主要职业资料齐全且搜索表现支持后，按已核实特点制作测评。','/class-quiz','/classes'),
 'builds': mapping('/builds','P0','existing_page_updated','起步方法和样例不构成所有职业完整Global配点数据库。','按实际查询补具体例子，保留与三个新职业页互链。'),
 'cleric build': mapping('/cleric-build','P0','existing_page_updated','TW经验与早期Global模拟未覆盖最终配点、所有冷却条件。','用当前Global技能描述核实治疗/减益与触发条件。'),
 'chanter build': mapping('/chanter','P0','merged_existing_page','已有起步技能/Mantra/角色调整；最终Global配点仍有限制。','同页补实际Global构筑，不建重复Chanter build页。'),
 'chanter skills': mapping('/chanter','P0','merged_existing_page','已覆盖起步技能和特性，不是完整数值技能库。','先扩展有证据的关键技能说明，保留同页承接。'),
 'cleric guide': mapping('/cleric-build','P0','merged_existing_page','已覆盖治疗/净化/复活/伤害职责，独立职业宏未完成。','核实具体宏操作后另做实质案例，不复制职业构筑。'),
 'gladiator build': mapping('/gladiator#starter-build','P1','merged_new_page','当前为带来源限制的实用starter，不是最终Global点表。','将当前Global配点证据补入同一职业页。'),
 'macro guide': mapping('/macro-guide','P2','new_page_ready','设置流程来自上线期玩家演示，未在Global游戏会话中独立复现；精确延迟未知。','用当前Global操作验证保存/绑定/停止/优先级；职业案例单独补证。'),
 'ranger macro': mapping(None,'P2','awaiting_global_evidence','通用宏页已完成，但缺当前Global Ranger专属配置/条件/响应验证。','先手动验证Ranger技能前提，再记录实际宏绑定、停止和延迟行为。','/ranger-macro','/macro-guide'),
 'character creation': mapping('/character-creation','P3','existing_page_updated','Global精确名称长度、删除等待和修改消耗未核实。','保留作成/外观流程；删除与重做教程齐证后独立承接。'),
 'presets': mapping('/presets','P3','existing_page','官方样式浏览已证实；初始创建导入/后续应用费用存在限制。','取得当前确认画面后补具体导入与消耗。'),
 'redo character creation': mapping('/character-creation','P2','partially_covered','已有外观规划，Global重做入口/券/价格/适用条件未核实。','补齐Global确认步骤与消耗再发布操作页。','/redo-character-creation'),
 'races': mapping('/races','P1','new_page_ready','独立Global换阵营手段/价格/冷却、种族伤害优势未核实。','维护官方二阵营/配对/同阵营转服条件，等待真实变更规则。'),
 'release': mapping('/steam#access-schedule','P0','merged_existing_page','公告日期会变；不延伸成所有地区统一开放时间。','在正式开放前后复核官方公告，并标示最新检查时间。'),
 'early access': mapping('/steam#access-schedule','P0','merged_existing_page','先行权利与公开免费开放有区别；账号注册不自动提供资格。','在访问阶段切换时更新资格及过期状态。'),
 'global release date': mapping('/steam#access-schedule','P0','merged_existing_page','计划日期不保证服务已运行；维护时段可能调整。','按官方后续公告复核开放日期与时区。'),
 'pre registration': mapping('/steam#global-and-regional-versions','P0','partially_covered','未确认正在开放的Global事前注册活动。','查当前Global公告；有明确活动期限/条件后补问答，不能复用TW旧预约。'),
 'release time': mapping('/steam#access-schedule','P0','merged_existing_page','当前为官方公告UTC时点，不是地区客户端通用时间表。','复核公告并保持UTC/JST转换一致。'),
 'japan release date': mapping('/steam#global-and-regional-versions','P0','merged_existing_page','日语Global站不证明日本独立发行日。','按Global公告提供日本时区换算，独立日期只在官方确认时新增。'),
 'global': mapping('/steam#global-and-regional-versions','P0','merged_existing_page','地域服务区别已说明，不提供跨服务账号/进度共用保证。','随Global官方服务声明更新入口与资格。'),
 'japan': mapping('/steam#global-and-regional-versions','P0','merged_existing_page','有日语Global入口，不构成单独日本服务器/账号规则。','按官方区域服务信息维护。'),
 'taiwan': mapping('/steam#global-and-regional-versions','P0','merged_existing_page','提供官方TW客户端入口与服务区别，不将Global日期当TW日期。','保留TW来源标签，独立查其当前公告。'),
 'steam': mapping('/steam','P0','existing_page_updated','当前平台/日期/兼容标记随商店与公告变动。','维持app3393110身份与地区/账号说明的时效。'),
 'ps5': mapping('/steam#platform-and-controller-support','P0','covered_with_limits','已查Global PC来源未建立PS5发行，不等同断言永久无PS5。','有官方平台公告时更新；不发薄否定页。'),
 'purple': mapping('/download','P0','merged_existing_page','Global安装及地区入口有说明，不保证TW/KR账户同样适用。','复核官方Global安装菜单与地区选择。'),
 'mobile': mapping('/steam#platform-and-controller-support','P0','covered_with_limits','TW有原生移动客户端不证明Global有；PURPLE移动/远程不等于原生游戏。','只按Global官方平台发布信息更新。'),
 'download': mapping('/download','P0','existing_page','Steam/PURPLE来源可变；未对每台硬件/地区复现安装。','遇到新官方错误公告时补具体排查步骤。'),
 'controller': mapping('/steam#platform-and-controller-support','P0','covered_with_limits','捕获Steam分类无完整/部分支持标记；未测试Global控制器，不证明所有映射不可能。','查现行官方兼容与实际菜单后补可复现配置。'),
 'system requirements': mapping('/download','P0','merged_existing_page','规格来自官方Steam；不是保证帧率或实际压缩下载大小。','维护官方规格，避免重复规格专页。'),
 'server': mapping('/server','P0','existing_page_updated','列表/配对是日期快照，非实时人口或创建状态。','公告更新时核对地区/阵营/配对。'),
 'maintenance': mapping('/maintenance','P0','existing_page','使用公告状态与期限，不是实时服务器探针。','按官方最新维护公告更新。'),
 'server transfer': mapping('/server-transfer','P1','new_page_ready','开始计划/初始同阵营及EA限制已证实；菜单/处理时间/冷却等未公告。','实际开放后依据当前Global界面补操作步骤。'),
 'server status': mapping('/maintenance','P0','merged_existing_page','公告快照不能证明此刻全部地区在线。','清晰呈现更新时间与公告；有可靠探针才加入实时状态。'),
 'map': mapping('/map','P0','existing_page','第三方地图筛选经来源检查，不是自有完整坐标数据库。','维护可用工具与操作入口。'),
 'interactive map': mapping('/map','P0','merged_existing_page','已有工具入口/实际筛选方法；地图数据完整性不能保证。','按实际玩家任务补地图使用方法，不复制新地图页。'),
 'pvp': mapping('/pvp','P3','existing_page','地域演示与Global模式公告分开，未统一量化职业强度。','核实新Global模式或规则变更再更新。'),
 'spacetime rift': mapping('/spacetime-rift','P1','existing_page_updated','缺可靠Global重复赛程；现有计时组件保持未知，不套KR/TW冲突周期。','取得Global入口时间/持续期/时区后接有效倒计时。'),
 'code': mapping('/code','P0','existing_page','活动/代码有有效期与资格，不保证所有账号可领。','优先复核过期状态及官方领取条件。'),
 'twitch drops': mapping('/twitch-drops','P0','existing_page','活动期限、账号关联与领取资格需时效检查。','在活动节点复核期限/关联流程。'),
 'monetization': mapping('/monetization','P0','existing_page','地区价格与权益来自日期来源，非永久跨地区价格。','复核免费/先行/礼包变化。'),
 'founders pack': mapping('/monetization','P0','merged_existing_page','已有礼包对照；当地价格与活动截止可能不同。','复核售卖状态/权益，避免重复礼包页。'),
 'g2g': mapping(None,'P3','deferred','品牌导航需求未建立本站可服务的独立攻略任务。','出现可核实的玩家交易问题与点击机会后再判断；不写假评测。'),
 'twitch': mapping('/guide#community-resources','P2','merged_existing_page','官方频道入口与Drops说明已提供，不复制直播列表。','维护频道与活动链接可用性。'),
 'reddit': mapping('/guide#community-resources','P2','merged_existing_page','社区导航已承接，帖子不能证明官方Global规则。','按具体问题引用日期/地区，不建链接薄页。'),
 'discord': mapping('/guide#community-resources','P2','merged_existing_page','官方入口有来源，未把聊天消息当当前规则。','维护官方入口，规则引用回原公告。'),
 'bahamut': mapping('/guide#community-resources','P2','covered_with_limits','已识别TW社区板块；本次直接访问403，未推荐其当前Global步骤。','后续可访问时核实具体帖子/日期/地区。'),
 'steam charts': mapping('/player-count#steamcharts-and-steamdb','P2','merged_new_page','当前SteamCharts app页返回Page Not Found，不能写人数0；已有SteamDB日期快照。','页面可访问后比对app/指标/窗口。'),
 'steamdb': mapping('/player-count','P2','merged_new_page','SteamDB独立来源日期快照，不是全客户端人数或自动实时服务。','复核图表读数并保留读取时间。'),
 'player count': mapping('/player-count','P2','new_page_ready','SteamDB日期快照；直接官方人数API未得到可用JSON，无PURPLE/地区合计。','获得可靠新读数或API后标明来源/时间/口径更新。'),
 'notmeter': mapping('/notmeter','P1','new_page_ready','维护者安装步骤与Npcap依赖已证实；未运行程序、未独立测试Global兼容或确认NC批准。','查当前维护版本/兼容与NC说明，继续明确技术兼容和许可是两回事。'),
 'lagofast': mapping(None,'P3','deferred','品牌导航或广告话术不提供本站实测网络优化价值。','只有独立可复现问题/测试证据时再决定内容。'),
 'review': mapping(None,'P3','deferred','缺足够可核查体验，不冒充第一手评测。','有实际体验/版本/素材后与gameplay合并一篇。','/review'),
 'gameplay': mapping(None,'P3','deferred','类介绍与演示链接不是完整体验评测，缺可核查素材。','与review同页，取得体验证据后制作。','/review'),
}

EXTRA = {
 'aion 2 class icons': mapping('/classes#class-icons','P0','existing_page_updated','原+70%未复现；图标当前实现依据官方素材与实读联想。','核对八图标名称与可放大原图，按GSC查询维护。'),
 'aion 2 delete character': mapping(None,'P2','awaiting_global_evidence','Global删除入口/等待/取消/名称复用未核实，继承Breakout无原快照。','取得Global官方帮助或非破坏操作证据后制作。','/delete-character','/character-creation'),
 'aion 2 cleric macro': mapping(None,'P2','awaiting_global_evidence','通用宏已写，但Cleric专属顺序/治疗独立键/Global效果未验证，旧+300%未复现。','补Global职业实例与手动/宏对照。','/cleric-macro','/macro-guide'),
 'aion 2 arcana': mapping(None,'P2','awaiting_global_evidence','存在当前需求；Global槽/升级/转化/卡片用途仍缺可发布证据。','一篇系统指南先核实操作；Chanter案例通过后同页展示。','/arcana'),
 'odyle energy aion 2': mapping(None,'P2','awaiting_global_evidence','奖励物品名不能证明Global能量用途/消耗/恢复公式。','区分能量系统、恢复道具、采集材料；先查Global说明。','/odyle-energy'),
 'aion 2 dimensional invasion': mapping(None,'P2','awaiting_global_evidence','Global入口、条件、流程、奖励、日程未核实。','核实官方Global活动后写独立流程并接现有计时。','/dimensional-invasion'),
 'aion 2 training dummy location': mapping(None,'P2','awaiting_global_evidence','缺Global两阵营地点、高度及到达路线。','取得地图/现场来源后制作；无坐标不画假标记。','/training-dummy-location','/map'),
 'aion 2 timer': mapping('/spacetime-rift#check-the-three-timers','P1','partially_covered','已有活动分流与未知赛程说明，尚无可靠Global裂隙有效周期。','验证活动日程后复用现有计时；不为同义timer另做薄页。'),
 'aion 2 rift timer': mapping('/spacetime-rift#check-the-three-timers','P1','partially_covered','Global重复开门时间/时区未证实，不套区域冲突规则。','获取Global当前规则后启用可靠倒计时。'),
 'aion 2 database': mapping(None,'P3','deferred','现有22件装备示例与角色查询不构成完整道具/卡片/掉落库。','先确认具体查找/筛选任务与可维护来源覆盖，再判断数据库。','/database'),
 'アイオン 2 クラス': mapping('/ja/classes','P0','existing_page_updated','本轮JP Rising禁用，Top指数4不是增长率。','维护官方八职业图标与选择指南，不建立重复页。'),
 'aion 2 es gratis?': mapping('/es/monetization','P0','merged_existing_page','原+100%未复现；免费与付费先行依来源区别。','在公开访问转换时复核/es/steam与免费说明。'),
 'aion 2 roadmap': mapping(None,'P3','awaiting_global_evidence','有德国当前Rising但缺可核实官方Global路线图。','出现官方Global后续安排时做有日期与版本的说明。','/roadmap'),
 'aion 2 best solo class': mapping('/classes#solo-party-and-pvp','P0','merged_existing_page','已有按责任/场景选择，无测得的Global统一最强。','用具体玩家任务改善选择；与tier-list保持分工。'),
 'aion 2 ranger leveling build': MAP['ranger'],
 'aion 2 spiritmaster daevanion build': MAP['spiritmaster'],
 'aion 2 steam chart': MAP['steam charts'],
 'aion 2 not meter': MAP['notmeter'],
 'aion 2 dps meter': MAP['notmeter'],
 'steam aion 2': MAP['steam'],
 'aion 2 steam best seller': mapping('/steam','P0','merged_existing_page','查询可映射Steam，但没有核实畅销榜排名/口径。','不因Rising宣称销量或畅销排名；仍维护Steam身份与访问说明。'),
 'questlog aion 2': mapping('/map','P0','merged_existing_page','主要是第三方地图品牌导航，工具数据覆盖不保证。','维护已检查入口与筛选任务，不另建品牌薄页。'),
 'npcap': mapping('/notmeter#maintainer-installation','P1','merged_new_page','维护者已说明依赖；驱动版本与Global兼容尚未独立测试。','保留原查询npcap，不创造aion前缀新词；核实维护者当前安装说明。'),
 'aion 2 как поиграть в россии': mapping('/steam#global-and-regional-versions','P3','out_of_language_scope','本轮站点语言为EN/JA/ES/DE，未核实俄区账号/可用性。','保留俄语市场线索，不自动开俄语页或承诺地区绕过。'),
 'american covid strain': mapping(None,'excluded','excluded_unrelated','与AION2内容无关。','排除，不计作游戏新机会。'),
 'erik brown cave rescue diver': mapping(None,'excluded','excluded_unrelated','与AION2内容无关。','排除，不计作游戏新机会。'),
 'aniimo': mapping(None,'excluded','excluded_unrelated','其他游戏/实体，不是AION2内容需求。','排除，不计作AION2新机会。'),
}

def choose(query):
    if query.startswith('aion 2 ') and query.removeprefix('aion 2 ') in MAP:
        return MAP[query.removeprefix('aion 2 ')].copy()
    if query in EXTRA:
        return EXTRA[query].copy()
    raise AssertionError('Missing editorial mapping: '+query)

def localized_paths(url):
    if not url: return None
    if url.startswith('/ja/') or url.startswith('/es/') or url.startswith('/de/'):
        return {url.split('/')[1]:url}
    return {locale:url if locale=='en' else '/'+locale+url for locale in locales}

def decorate(row):
    url=row['destinationUrl']
    row['localizedDestinationUrls']=localized_paths(url)
    slug=(url.split('#')[0].strip('/').split('/')[-1] if url else None)
    row['destinationLocallyPublished']=bool(slug and slug in published_slugs)
    row['routeAvailability']='local_content_ready' if row['destinationLocallyPublished'] else 'not_published'
    if slug:
        row['contentMetadataFile']='src/content/article-data/'+slug+'.json'
    return row

original = []
for category in corpus['categories']:
    for query in category['keywords']:
        row=dict(originalQuery=query, category=category['category'], historicalPriority20=query in first_keywords,
                 sourceId='K63', sourceFile='keywords.json', sourceUrl=None, country=None, timeWindow=None,
                 observedAt=corpus['terminologyReview']['checkedAt'], growth=None, growthVerified=False,
                 demandVerification='not_individually_requeried', **choose(query))
        original.append(decorate(row))

rising=[]
for source in evidence['sources']:
    if source.get('kind')=='google_trends_related_queries' and source.get('view')=='Rising':
        for raw in source['rows']:
            displayed=raw['displayedValue']
            growth={'displayedValue':displayed,'kind':'breakout' if displayed=='Breakout' else 'percent',
                    'percent':None if displayed=='Breakout' else int(re.sub(r'[^0-9]','',displayed)),
                    'lowerBoundPercentExclusive':5000 if displayed=='Breakout' else None}
            row=dict(originalQuery=raw['query'],sourceId=source['id'],sourceFile='research/keywords/2026-10-03/evidence.json',
                     sourceUrl=source['url'],country=source['country'],timeWindow=source['timeWindow'],
                     observedAt=source['observedAt'],rank=raw['rank'],growth=growth,growthVerified=True,
                     **choose(raw['query']))
            rising.append(decorate(row))

inherited=[]
for raw in evidence['inheritedObservations']:
    past=raw['original']
    row=dict(originalQuery=raw['query'],normalizedKeyword=raw['normalizedKeyword'],sourceId='predecessor-plan',
             sourceFile='research/keywords/2026-10-03/evidence.json',sourceUrl=past['sourceUrl'],country=raw['country'],
             timeWindow=past['timeWindow'],observedAt=past['observedAt'],growth=None,growthVerified=False,
             claimedGrowth=past['claimedValue'],rawSnapshotAvailable=past['rawSnapshotAvailable'],
             currentRecheck=raw['verification'],**choose(raw['query']))
    inherited.append(decorate(row))

AUTO_MAP={
 'aion 2 klassen guide':MAP['classes'], 'aion 2 klassen übersicht':MAP['classes'],
 'aion 2 klassen symbole':EXTRA['aion 2 class icons'], 'aion 2 klassen icons':EXTRA['aion 2 class icons'],
 'aion 2 klassen ranking':MAP['tier list'], 'aion 2 klassen deutsch':MAP['classes'],
 'aion 2 klassen und rassen':MAP['races'], 'aion 2 klassen eu':MAP['classes'],
 'aion 2 klassen skills':mapping('/classes','P2','partially_covered','已有职业定位与部分职业技能，非八职业完整技能库。','按Global证据扩已存在职业页，不按联想建重复技能总页。'),
 'aion wiki classes':mapping(None,'excluded','excluded_ambiguous_entity','原词可能指初代AION，不能自动当作AION2查询。','保留原词；确认实体再判断，不添加前缀。'),
 'aion2 クラス おすすめ':EXTRA['aion 2 best solo class'], 'aion2 クラス tier':MAP['tier list'],
 'aion2 クラス アイコン':EXTRA['aion 2 class icons'], 'aion2 クラス 診断':MAP['class quiz'],
 'aion2 クラス 一覧':MAP['classes'], 'aion2 クラス 最強':MAP['tier list'],
 'aion2 クラス 変更':mapping('/classes','P2','awaiting_global_evidence','Global职业更改方法/费用未验证。','查当前Global官方帮助再补明确答复；不从角色外观推断转职。'),
 'aion2 クラス 人口':mapping('/classes','P3','awaiting_global_evidence','无可靠Global逐职业人数，Steam总并发不能替代。','取得合法可信的逐职业口径再回答，不用总人数推算。'),
 'aion2 クラス 性別':mapping('/classes','P2','awaiting_global_evidence','Global各职业性别限制未逐项验证。','读当前创建界面/官方说明后补对应比较。'),
 'aion2 クラス 武器':mapping('/classes','P2','partially_covered','角色风格与官方画像不能替代完整武器规则。','按Global官方装备/技能说明补实际武器条件。'),
}
autocomplete=[]
for source in evidence['sources']:
    if source.get('kind')!='google_autocomplete': continue
    for query in source['queries']:
        target=EXTRA['aion 2 arcana'].copy() if source['id']=='A1' else AUTO_MAP[query].copy()
        if source['queryLanguage']!='en':
            for field in ['destinationUrl','supportingUrl','plannedUrl']:
                if target.get(field):target[field]='/'+source['queryLanguage']+target[field]
        row=dict(originalQuery=query,sourceId=source['id'],sourceFile='research/keywords/2026-10-03/evidence.json',
                 sourceUrl=source['url'],country=source['requestedCountry'],countryIsRequestedNotVerified=True,
                 actualCountryVerified=source['actualCountryVerified'],queryLanguage=source['queryLanguage'],
                 personalized=source['personalized'],timeWindow='Instant autocomplete snapshot; no growth window',
                 observedAt=source['observedAt'],growth=None,growthVerified=False,**target)
        autocomplete.append(decorate(row))

sources=[]
for source in evidence['sources']:
    keep={k:v for k,v in source.items() if k not in ['rows','queries','rawColumns']}
    sources.append(keep)

counts=Counter(x['currentStatus'] for x in original)
payload={
 'schemaVersion':1,'createdAt':NOW,'reportDate':'2026-10-03','timezone':'Asia/Shanghai',
 'scope':'Local implementation coverage after authorized SEO content expansion; not deployment, live traffic or rank verification.',
 'goal':'Maximize obtainable SEO clicks over the next 30–90 days; avoid duplicate thin pages and unsupported Global facts.',
 'urlConvention':'Paths are site-relative. English has no locale prefix; JA/ES/DE have explicit prefixes. Planned URLs are not published navigation targets.',
 'growthPolicy':'Only directly read current Rising rows carry verified growth. Inherited claimedGrowth is preserved separately; autocomplete and original-library rows have null growth. Null means unknown/not applicable, never zero.',
 'sourcePolicy':'German/Spanish country evidence does not make an English query German/Spanish. Autocomplete hl/gl is requested locale and country, personalized, with actual location unverified. No keyword expansion or expected traffic estimate.',
 'priorityDefinitions':{'P0':'Fast updates and time-sensitive facts; mostly strengthen current pages','P1':'Core class/utility coverage or obtain Global Rift schedule','P2':'Small validated tutorial/resource batch','P3':'Maintain, defer or evidence-gated later candidate','excluded':'Unrelated or entity-ambiguous signal'},
 'summary':{'originalKeywords':len(original),'historicalPriority20':len(first_keywords),'originalOutsidePriority20':len(original)-len(first_keywords),
            'publishedTopics':len(published_slugs),'publishedLocaleArticles':len(published_slugs)*len(locales),
            'currentRisingRows':len(rising),'inheritedRisingRows':len(inherited),'autocompleteRows':len(autocomplete),
            'originalKeywordStatusCounts':dict(counts),'newIndependentPages':['gladiator','ranger','spiritmaster','races','server-transfer','notmeter','player-count','macro-guide']},
 'sources':[{'id':'K63','kind':'original_keyword_library','file':'keywords.json','country':None,'timeWindow':None,'observedAt':corpus['terminologyReview']['checkedAt'],'note':'All63 read; not a per-keyword demand recheck.'}]+sources,
 'originalKeywords':original,'currentRising':rising,'inheritedRising':inherited,'autocomplete':autocomplete,
 'inheritedAutocompleteFragments':evidence['inheritedAutocompleteFragments'],
 'auxiliaryVolumeEvidence':next(s for s in evidence['sources'] if s['id']=='S1'),
 'planningVolumeEvidence':{'file':'research/keywords/2026-10-03/implementation/similarweb-plan-observations.json','observation':similarweb,'usage':'29 selected UI observations from prior planning, not rechecked during implementation; exact-query metrics only, no synonym sums or missing-query estimates.'},
 'regionalLimits':{
   'gladiator':MAP['gladiator']['gap'],'ranger':MAP['ranger']['gap'],'spiritmaster':MAP['spiritmaster']['gap'],'races':MAP['races']['gap'],
   'notmeter':MAP['notmeter']['gap'],'player-count':MAP['player count']['gap'],'macro-guide':MAP['macro guide']['gap'],'server-transfer':MAP['server transfer']['gap']},
 'monitoring':{'baseline':'No traffic baseline is invented in this artifact; use root implementation GSC evidence when available.',
               'reviewDaysAfterPublication':[14,30,60,90],'dimensions':['page','query','language','country'],
               'decision':'Prioritize pages with real impressions and answer gaps; investigate indexing before adding same-topic pages.'},
 'preservedSourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['keywords.json','keywords-priority-20.json','research/keywords/2026-10-03/evidence.json']},
 'limitations':['Original 63 keywords were all mapped, not all re-queried in Trends or a volume tool.','Twenty-eight topics mean112local MDX pages; four translations are not four independent keyword discoveries.','Search volumes, query variants and growth rates are not added or multiplied into predicted site traffic.','Current Rising contains unrelated rows that remain archived but excluded from game opportunity totals.','No GSC indexing or deployment is performed by this archive task.']
}

assert len(original)==63 and len(first_keywords)==20 and len(published_slugs)==28
assert len(rising)==27 and len(inherited)==13 and len(autocomplete)==30
assert len({x['originalQuery'] for x in original})==63
for section in [original,rising,inherited,autocomplete]:
    for row in section:
        for field in ['originalQuery','sourceId','sourceUrl','country','timeWindow','observedAt','growth','priority','currentStatus','gap','nextStep','destinationUrl']:
            assert field in row,(row['originalQuery'],field)
        if row['destinationUrl']:
            base,_,anchor=row['destinationUrl'].partition('#')
            parts=base.strip('/').split('/')
            locale=parts[0] if len(parts)>1 else 'en'
            slug=parts[-1]
            assert slug in published_slugs,(row['originalQuery'],'missing page',slug)
            for check_locale in (['en','ja','es','de'] if locale=='en' else [locale]):
                path=ROOT/'src/content'/check_locale/(slug+'.mdx')
                assert path.exists(),str(path)
                if anchor: assert f'id="{anchor}"' in path.read_text(encoding='utf-8'),(row['originalQuery'],check_locale,anchor)
assert all(r['growth'] is None and r['growthVerified'] is False for r in inherited+autocomplete+original)
assert all(r['growthVerified'] and r['growth']['displayedValue'] for r in rising)

json_target=OUT/'keyword-coverage.json'
if json_target.exists(): raise RuntimeError('Refusing to replace '+str(json_target))
json_target.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

status_cn={'existing_page':'既有页','existing_page_updated':'旧页增补','new_page_ready':'新页完成','merged_existing_page':'旧页合并承接','merged_new_page':'新页合并承接','covered_with_limits':'有限覆盖','partially_covered':'部分覆盖','awaiting_global_evidence':'待Global证据','deferred':'暂缓'}
ready=sum(1 for x in original if x['destinationLocallyPublished'])
md=f'''# AION 2 内容实施覆盖 · 2026-10-03

**已完成28个主题、112篇四语言正文；原63词全部逐项映射。剩余待证主题保留队列，不用薄页填满。**

- 新增8个独立主题：Gladiator、Ranger、Spiritmaster、阵营、转服、Notmeter、玩家人数、通用宏。
- 原20个主词保留；另外43词不等于43张新页，按独立任务和现有答案归并。
- 本档记录本地内容实现，不能据此声称已经部署、收录或获得流量。英文先定事实，日／西／德正文同时齐备。

## 原63词的完整承接表

下表词形仅省略共同前缀 `aion 2`；JSON保留每个原词及来源、国家、窗口、时间、增幅属性、状态、缺口和下一步。

| 原词 | 优先级 | 当前状态 | 承接／计划 |
| --- | --- | --- | --- |
'''
for row in original:
    short=row['originalQuery'].removeprefix('aion 2 ')
    dest=row['destinationUrl'] or '暂无公开页'
    if row['plannedUrl']:dest+='；计划 '+row['plannedUrl']
    md+=f"| `{short}` | {row['priority']} | {status_cn[row['currentStatus']]} | {dest} |\n"
md+='''
## 本轮调研证据如何计入

- 27条当前Rising按原国家、近一天滚动窗口、20:18–20:27北京时间保存；3条明显无关词仍保留原值但排除。德国/西班牙中的英语查询仍是英语查询。
- 13条继承观察仅保留 `claimedGrowth`，不当作新证实的增长。4个查询在后次Rising复现，9个未复现或不可读；未复现不等于需求为零。
- 30条实际下拉联想单独记录，无增长率；请求hl/gl、个性化与实际国家未核实限制保留。前次只有片段的联想不补造完整查询。
- `npcap` 已由Notmeter维护者安装说明确认关联，归并 `/notmeter`；不创造 `aion 2 npcap`。
- Similarweb Arcana7行作为辅助保留截至9月30日的近28天估计值，`<50`不改为0；不估算流量、不累加同义词体量。

优先级同时参考前次Similarweb实际界面读取的29条选样：职业 `classes` 142.4K、KD3，Gladiator 8K及其build 6.1K、阵营6.5K支持职业内容优先；`release date` 199.8K支持维护Steam访问时间，`steamcharts` 22.4K支持有日期的人数页。社区查询多为导航需求，集中放入攻略入口资源区。仅引用相同原词的估计值，各词不相加。

上述Similarweb窗口为Worldwide／Google／All traffic、近28天、截至9月30日；精确采集时刻未保留，本轮未重查，与Trends近一天涨幅分开。原选样见 [similarweb-plan-observations.json](similarweb-plan-observations.json)。

## 已完成内容的事实边界

- **职业3页：** 起步实例来自有字幕与时间日志的区域角色示范；未发布Global最优配点、节点坐标或统一伤害排序。
- **阵营／转服：** 官方确认二阵营、临时配对、10月14日开始计划、同阵营与初始EA限制；没有补造换阵营、菜单或冷却规则。
- **Notmeter：** 维护者来源、安装说明与Npcap依赖已核；程序未运行，Global兼容及NC批准未独立确认。
- **人数：** SteamDB日期快照，非全客户端总量；SteamCharts当前查无页，官方人数API无可用JSON均不写成0。
- **宏：** 通用菜单来自上线期玩家演示，未声明游戏内独立实测；Ranger/Cleric专属模板和固定延迟仍待证。
- **Steam：** Global与日本时区/TW服务区分；未查到的PS5、原生Global手机、控制器支持不写成永久不支持。社区入口另标官方/社区和地区。

## 下一批顺序与验收

1. P0维护：访问阶段、活动截止、价格、维护公告与来源入口的时效。
2. P1补证：Global裂隙日程；转服实际开放后补界面与条件；职业技能与工具兼容按明确证据更新。
3. P2小批：Ranger/Cleric职业宏、重做/删除、Arcana、Odyle、Dimensional Invasion、木桩地点，证据不足则推进下一主题。
4. P3保留：Brawler Global可选状态、测评、实际体验评测、品牌导航、官方roadmap和完整database；不以旧涨幅强行发布。

结构验收：63个原词、20个历史主词、43个余词、27条当前Rising、13条继承观察、30条联想数量与原词一致；已有承接URL的四语正文和锚点存在。原词库与旧研究SHA-256保留在JSON。

上线后第14／30／60／90天按页面、查询、语言、国家复盘。以真实曝光与内容缺口决定下一批；收录异常先排查，不虚构排名、收益或点击预测。

机器可读档：[keyword-coverage.json](keyword-coverage.json)。原证据：[../evidence.json](../evidence.json)。
'''
md_target=OUT/'coverage.md'
if md_target.exists(): raise RuntimeError('Refusing to replace '+str(md_target))
md_target.write_text(md,encoding='utf-8')
print(json.dumps({'summary':payload['summary'],'mappedExistingDestinations':ready,'files':[str(json_target.relative_to(ROOT)),str(md_target.relative_to(ROOT))]},ensure_ascii=False))
