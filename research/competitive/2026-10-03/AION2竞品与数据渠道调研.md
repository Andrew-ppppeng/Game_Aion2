# AION 2 竞品与数据渠道调研

调研日期：**2026-10-03（Asia/Shanghai）**。覆盖 19 个网站/平台入口；保存 132 次原始来源捕获，其中 32 次官网接口请求。接口快照对应当日线上服务；接口没有返回统一客户端版本号，不能给所有响应强行标同一个版本。

## 先看结论

1. **值得继续做，但“攻略 + 大而全数据库 + 地图”已经有充分竞争。** 优先跟踪 Questlog、Shugo、AION2 Hub、Aion2.app、DBAion2、aion2.tools；Atool 是数值与成长分析的区域标杆。
2. **可以用官网 JSON 接口丰富本站。** 本轮实际读到了 Global EU 与 TW 的角色、装备、物品模板、部分技能信息和 Daevanion 节点。英语/日语/西语/德语的同一件 Global 物品也全部验证成功。
3. **目前没有核到面向 AION2、有完整文档和服务承诺的官方开发者 Open API。** 官网前端能访问的 JSON，是可用的数据渠道；稳定性、批量使用额度和再分发授权仍未确认。
4. **流量不能乱报。** Questlog 的 159 万/月是多游戏平台整站估算；AION2 分区流量未知。多数独立新站没有取得可靠公开当期估算，不能写成 0，也不能按内容数量猜访问量。
5. **本站建议定位：帮助英语 Global 玩家做具体成长选择，再复用官方术语扩展 JA/ES/DE。** 将经过核验的数值放进现有攻略，解释适用阶段、选择条件和替换理由。这是策略判断，尚不是已验证的市场空白。

完整可筛选表：[competitors.csv](competitors.csv)。接口细节：[API核验与接入建议.md](API核验与接入建议.md)。

## 一、统计口径：建站时间和访问量怎么看

### 建站时间

- **域名注册日**：来自 RDAP 的 registration 事件，以下表格统一使用 UTC 日期。它证明域名何时注册，不能证明网站何时上线。
- **公开运营证据**：开发者介绍帖、明确的站内开站公告、当前可见更新日志。只能证明“该日已存在”；普通文章日期也不能直接当开站日。
- 多游戏平台的注册日不能当 AION2 分区成立日；迁移后的新域名注册日不能当原项目年龄。
- 本轮 Wayback 查询出现错误或超时，**没有取得足够的首个历史快照证据**。失败日志已保留，不据此断言网站没有历史。
- .gg 的 RDAP 查询未成功取得注册信息，因此 Questlog、Shugo 的注册时间保留未知；没有用猜测补齐。

### 访问量

以下数字是第三方 **visits（访问次数）估算**，不是独立用户、玩家数、在线人数或网站后台实测。当前能比对的公开月份是 2026-08，不是 2026-10。不同数据商、不同设备范围、整站与子目录不能混算。

| 网站 | 2026-08 月 visits 估算 | 覆盖范围 | 近三个月 | 来源 / 更新日 |
|---|---:|---|---|---|
| Questlog | **1.59M，约 159 万** | questlog.gg 全站，多游戏 | Jun 1.83M → Jul 1.99M → Aug 1.59M | [Semrush](https://www.semrush.com/website/questlog.gg/overview/)，2026-09-18 |
| Fextralife | **42.8M，约 4,280 万** | fextralife.com 全站，多游戏 | Jun 44.72M → Jul 44.74M → Aug 42.8M | [Semrush](https://www.semrush.com/website/fextralife.com/overview/)，2026-09-17 |
| Inven | **53.98M，约 5,398 万** | inven.co.kr 全站，多游戏 | Jun 52.29M → Jul 55.59M → Aug 53.98M | [Semrush](https://www.semrush.com/website/inven.co.kr/overview/)，2026-09-17 |
| 其余本轮独立站 / Timesaver | **未知** | 不使用其他站或集团流量代替 | 公开查询未取得可靠当期数字 | 各次查询见 [source-index.csv](source-index.csv) |

补充历史线索：Atool 的 [HypeStat 页面](https://hypestat.com/info/aion2tool.com)显示约 **2,058,037 月 visits**，但同页标注上次更新已过去 254 天，三个月图只有 OCT/NOV/DEC，年份不清楚，且嵌入的 Semrush/SimilarWeb 数字不同。**只保留为陈旧线索，不能当作其当前月流量。** 页面给出的“广告收入估算”也不是其真实营收，本报告不采用。

Questlog 的整站体验指标为 4.63 页/访问、平均 07:13；其 Desktop Traffic Journey 显示 Direct 74.64%、Google organic 15.61%。这支持“工具可能产生回访”的假设，但不能证明 AION2 分区表现，也不能把桌面口径当全部设备渠道占比。对应原始页：[questlog-gg-semrush.txt](raw/questlog-gg-semrush.txt)。

检索工具曾返回 Questlog 较旧的 July 缓存；上表采用本轮直接抓取的 August 页面。**本轮没有完成地区化 Google 排名追踪，也没有取得任何竞品 GA/GSC 后台数据。**

## 二、竞品全表

“流量未知”表示本轮未取得可靠当期公开估算。工具是否有入口、开发者是否声称具备功能，与每个功能是否准确可用，是不同验证层级。

### A. 综合工具、数据库与区域标杆（13 个）

| 网站 | 域名注册日（UTC） | 公开运营时间证据 | 主要特点 / 地区 | 流量与商业化 |
|---|---|---|---|---|
| [Questlog](https://questlog.gg/aion-2/en) | 未取得 | [2026-01-10 开发者介绍 AION2 分区](https://www.reddit.com/r/Aion2/comments/1q9aikc/weve_developed_a_aion_2_companion_website_with/) | 配装/技能、Armory、地图、节点、清单、3D外观；多语言；多游戏平台 | 整站 159 万/月，AION2 未知；实见 Premium / Remove Ads |
| [Shugo](https://shugo.gg/) | 未取得 | [2025-12-09 开发者介绍](https://www.reddit.com/r/Aion2/comments/1pi2bxn/just_created_shugogg_check_your_profile_in_english/) | KR/TW 起步；现称覆盖 Global 5 区；角色、装备、数据库、地图、计时器、样本战力榜 | 当期未知；开发者称免费，具体商业收入未核 |
| [AION2 Hub .com](https://aion2hub.com/) | [2025-09-06](https://rdap.org/domain/aion2hub.com) | 有开发者 Summer Game Fest 介绍帖；绝对发布日期未核准 | 英语 Global；客户端数据库、配装、强化、制作、地图、活动；链接 AionFlex | 当期未知；实见 Creator Spotlight，收费合作条款未核 |
| [Aion2.app](https://aion2.app/) | [2025-12-26](https://rdap.org/domain/aion2.app) | [2026-02-22 开发者介绍](https://www.reddit.com/r/Aion2/comments/1rbilp3/aion2app/) | 制作/技能/节点/地图/数据库；版本拆解内容；KR/TW 与 Global 内容并存 | 当期未知；收费未核；主页工具链接到 aion2t.com |
| [DBAion2](https://www.dbaion2.online/en/) | [2026-09-22，.online 镜像](https://rdap.org/domain/dbaion2.online) | [日志明确宣布 2026-09-22 dbaion2.ru 开放](https://www.dbaion2.online/en/site-news/)；09-23 上英语 | RU/EN；Global 客户端数据库、配装、制作、分享/嵌入卡、Tracker | 当期未知；明确 PRO 订阅，DPS 部分免费，主播合作计划 |
| [aion2.tools](https://aion2.tools/) | [2026-08-07](https://rdap.org/domain/aion2.tools) | 本轮主页可见 2026-09-21/23 攻略；不是开站确证 | 英语；明确 TW 物品 / KR 强化；装备对比、强化预算、技能叠加解释 | 当期未知；有 Account，收费未核 |
| [Atool](https://www.aion2tool.com/) | [2025-11-21](https://rdap.org/domain/aion2tool.com) | 当前主页更新日志可见至 2026-04-01；可能更早上线 | 韩语为主；角色统计、成长模拟、节点、Arcana、魔石、样本服务器比较 | 当期未知；历史约 206 万估算已陈旧；商业化未核 |
| [Gamers4 / InteractiveMap](https://gamers4.life/aion-2/database/en/tools/) | [2023-08-25，多游戏平台](https://rdap.org/domain/gamers4.life) | AION2 分区成立时间未核到 | 自报 33 工具；配装/成长/制作；配套地图、社区路线、Discord bot | 当期未知；Support Me/账号；开发者称工具免费 |
| [Aion2Atlas](https://aion2atlas.com/) | [2025-11-23](https://rdap.org/domain/aion2atlas.com) | [2025-11-29 已有事件计时器](https://www.reddit.com/r/Aion2/comments/1p9epc1/rift_schedule_event_timer_for_aion_2/) | 地图、计时器、外观数据库；KR/TW 时期起步；当前完整交互未测 | 当期未知；商业化未核 |
| [Aion2GG](https://aion2gg.com/) | [2026-07-23](https://rdap.org/domain/aion2gg.com) | 首次上线日期未取得 | 韩语为主；角色查询、强化/突破模拟、节点优化、副本机制辅助 | 当期未知；商业化未核 |
| [Aion2Timers](https://aion2timers.com/) | [2026-09-21](https://rdap.org/domain/aion2timers.com) | [09-24 开发者称迁移完成](https://www.reddit.com/r/Aion2/comments/1wp1avo/aion_2_timers_update_9242026/)，旧项目更早 | 时区事件/Rift计时、日周清单、弹出窗口、主播显示、Boss beta | 当期未知；捐助；目前无订阅/付费墙，广告是未来计划 |
| [AION2HUB .me](https://aion2hub.me/en) | [2026-09-06](https://rdap.identitydigital.services/rdap/domain/aion2hub.me) | 首次上线未核；转载旧新闻不能当本站年龄 | 数据库、配装、社区 build、地图、计时；自报 13,018 物品和 48,849 标记 | 当期未知；商业化未核 |
| [Elysion](https://www.elysion.quest/) | [2026-05-12](https://rdap.org/domain/elysion.quest) | 首次上线未核 | Wiki/tools 搜索摘要可见；当前 JS 页具体功能未完整验证 | 当期未知；商业化未核，低置信度待补 |

**身份与规模注意：**

- AION2 Hub 的 **.com 与 .me 是两个分别核查的域名**，没有证据证明同一运营者。
- Gamers4 与 interactivemap.app 的[开发者说明](https://www.reddit.com/r/Aion2/comments/1wh1y5x/aion_2_interactive_map_database_full_rundown/)提到共享账号与配套数据库，因此按同一产品生态分析，避免重复算成独立竞争力量。
- Aion2.app 链出的 aion2t 工具页不再额外当一个竞争站计数；集团所有权没有另作确证。
- 数据库记录数量、地图标记数量、被查询角色数量，**全部不是网站访问量或游戏在线人数**。
- 初始搜索误命中的 atool.kr 是无关网站，已排除。AION2 的 Atool 正确域名是 aion2tool.com。

### B. 内容站与平台入口（6 个）

| 网站 | 注册 / 时间证据 | 内容与语言 | 可见特点 / 局限 | 流量 |
|---|---|---|---|---|
| [AION2 Guide](https://aion2guide.org/) | [注册 2026-09-21](https://rdap.org/domain/aion2guide.org)；开站日未知 | 英语；职业/代码/开服/系统/副本 | Pagefind、最后核验日期；与本站优先内容重叠高；所有攻略数值未逐页验证 | 未知 |
| [aion2game.wiki](https://aion2game.wiki/) | [注册 2026-09-17](https://rdap.org/domain/aion2game.wiki)；开站日未知 | EN/JA/ES/DE 等 8 种语言入口 | 来源和未核信息提示；部分主页说法仍停留在 09-18，需注意更新；实见广告占位 | 未知 |
| [aion-two.wiki](https://aion-two.wiki/) | [注册 2026-09-20](https://rdap.org/domain/aion-two.wiki)；主页 Last reviewed 09-20 | 英语；发行/职业/新手/PC条件 | 结构清楚；部分抢先体验信息落后；实见广告网络链接 | 未知 |
| [Fextralife AION2](https://aion2.wiki.fextralife.com/) | AION2 分区成立日未知 | 英语 Wiki；职业/任务/战斗/区域 | 借平台内容体系；本轮主页仍将 Global 写为 mid-2026，时效性明显不足 | 全平台 4,280 万/月；分区未知 |
| [Inven AION2](https://aion2.inven.co.kr/) | AION2 分区成立日未知 | 韩语新闻、攻略、玩家论坛 | 社区/职业专区是重要情报入口；KR 结论不能直接搬到 Global | 全平台 5,398 万/月；分区未知 |
| [Timesaver AION2](https://timesaver.gg/blog/aion-2-release-date) | 本轮文章标记 2026-09-01；整站自述创立于 2024 | 英语内容集群；发行/职业/成长/会员/服务器 | 主站是多游戏商业服务商城；AION2 文章参与内容竞争，未证 AION2 服务已开放 | 未知 |

商业模式依据分别来自站内可见入口、公告或[Timesaver 主站](https://timesaver.gg/)。**功能/文案观察不等于收入或效果证明**。没有下载或运行任何竞品 Tracker/DPS 程序。

## 三、最值得研究的 7 个对象

以下优先级是对本站的相关性判断，不是流量排名。

### 1. Questlog：平台化工具与回访

实见配装、Armory、清单、地图、Daevanion、服务器状态、3D Dressing Room，以及去广告/会员入口。语言选择已经覆盖 EN/DE/ES/JA 等，所以“有多语言”本身不构成独特优势。[产品入口](https://questlog.gg/aion-2/en)

借鉴：将攻略中的选择保存成 build/清单，让读者下次回来继续。直接追齐整个平台会明显扩大工作量。主页同时呈现多个地区的更新内容，本站需要在每张数值卡上单独标版本与地区。

### 2. Shugo：角色查询带动分享与样本数据

开发者现称已覆盖 Global 五区，角色页可分享、收藏；战力榜来自站内被查过的角色。[当前开发者说明](https://www.reddit.com/r/Aion2/comments/1wvo1t1/aion_2_armory_profile_character_database/)

借鉴：角色导入、装备解释、可分享链接。它已经具备基本 Armory，本站更适合在导入后解释“这个阶段先补哪种属性”，并展示依据。查询样本不能叫全服人口，也不能自动等同最优打法。

### 3. AION2 Hub .com：数值工具与攻略组合

当前主页强调 Global 客户端数据库，配装、强化、制作、地图与成长攻略同时提供，还连接 DPS 生态和主播展示。[主页](https://aion2hub.com/)

借鉴：将物品与制作链直接链接进攻略。数据库“完整”、掉落率和公式是站方说法，本轮没有逐项复算，不能把其结果直接当官方答案。

### 4. DBAion2：新站也能快速形成分发和付费产品

站内公告明确记录 09-22 开站、09-23 英语版、09-27 嵌入卡与分享、09-29 PRO Tracker；10-02 又记录角色接口迁移后修复。这说明更新维护也是产品成本。[更新日志](https://www.dbaion2.online/en/site-news/)

借鉴：物品引用卡、分享预览、作者署名 build、主播合作。数据展示免费，便利功能付费是已存在的模式；注册只有十余天并不代表功能少，也不代表流量已经大。

### 5. Atool：有样本定义的成长分析

站内统计明确限定近期在 Atool 被查询的角色，部分比较只取高战力样本；成长模拟标明使用反推估算。因此其价值是样本分析与解释，不是取得了全服真实人口和完整官方伤害公式。[主页](https://www.aion2tool.com/)

借鉴：按职业/成长阶段展示分布、样本数、统计窗口，解释常见选择。本站如做群体统计，先获得足够 Global 样本再上线，不把“热门”写成“最强”。

### 6. aion2.tools：窄问题、清楚地区、具体数字

主页把 Taiwan 物品与 Korea 强化分开，文章围绕装备差异、预算和技能叠加等实际选择展开。[主页](https://aion2.tools/)

借鉴：一篇攻略解决一个具体决定。本站可采用这个内容深度，但优先补当前 Global 数据，不能把其区域计算结果换个标题后直接使用。

### 7. Gamers4 / InteractiveMap：社区参与增加留存

开发者介绍了路线草稿、发布、复制、进度保存、评论与投票，以及配套 build 和 Discord bot。[开发者说明](https://www.reddit.com/r/Aion2/comments/1wh1y5x/aion_2_interactive_map_database_full_rundown/)

借鉴：玩家自己的路线与进度，比只堆地图标记更有回访理由。完整地图与客户端数据维护量大，本站可先在现有地图攻略中添加经过核验的小范围路线。

## 四、API / 数值渠道：确认结果

### 4.1 能用的是什么

[NC 开发者门户](https://developers.plaync.com/apis/l2m/search)本轮 Documentation 界面只见 Lineage 2M。没有核到 AION2 的公开开发者文档、Key 申请、配额和 SLA。与之不同，**AION2 官网前端的公开 JSON 数据实际可读**。

社区 [nuriland/aion2-api](https://github.com/nuriland/aion2-api)提供 Go 封装，注明是非官方客户端。本轮读过源代码并以小量 GET 请求验证，未使用游戏账号、API Key 或绕过措施。

| 数据 | Global EU 实测 | TW 实测 | 对本站的用途 / 边界 |
|---|---|---|---|
| 服务器、职业目录 | JSON 成功：18 个服务器条目、8 职业 | 36 个服务器条目、9 职业 | 当前目录卡；不是人数、在线状态或拥挤程度 |
| 角色搜索、资料 | 成功 | 成功 | 等级/职业/战力/属性字段；本轮 Global 新角色部分属性为 0，须做质量判断 |
| 装备、单件装备详情 | 成功 | 成功；另一个模板请求超时 | 展示在穿物品、强化和具体词条；没有完整高阶随机装备覆盖测试 |
| 已知 ID 的物品模板 | 成功，真实物品 ID 110160001 | 成功，样例 ID 110120001 | 等级、品质、属性、词条范围、强化上限等；不同地区 ID 不保证可通用 |
| 技能 | 角色装备接口有名称/ID/等级/类别 | 同类字段成功 | 技能配置卡；**不等于全技能倍率、冷却与伤害公式库** |
| Daevanion | 返回 225 网格条目，含空位与部分效果 | 返回 225 网格条目，含空位 | 节点展示/已解锁状态；不是 225 个可加点节点或全板效果验证 |
| 全量物品目录 | 未验证可用的 Global 目录 | 搜索页成功，返回 total 11,225、limit 10,000 | TW 可作地区资料；没有遍历全量，也不能当 Global 清单 |
| 排行榜 | 本轮参数 HTTP 200，但空列表、无 season | 同样为空 | **当前不能据此上线“官方实时排行榜”**；未遍历其他模式 |
| 官方物品多语言 | EN/DE/ES/JA 四种成功，数值一致 | 本轮未做四语言比较 | 可直接解决本站四语言物品/属性术语 |

KR 两个测试地址返回 HTTP 200 的“找不到页面”HTML，**不是 JSON 成功**。没有通过切换网络或地区继续探测。因此“有 KR 代码支持”不能代替本环境的可用性证明。

更多 URL、参数、字段和失败记录见 [API核验与接入建议.md](API核验与接入建议.md)、[api-verification.csv](api-verification.csv)。

### 4.2 一个实际拿到的 Global 数值例子

[官网物品接口](https://aion2.plaync.com/en-us/api/gameconst/item?id=110160001&enchantLevel=0&lang=en-US)在本轮返回：

| 字段 | 实际值 |
|---|---|
| 物品 | Worn Greatsword |
| equipLevel / maxEnchantLevel | 1 / 5 |
| Attack | 4–6，是范围，不是固定 6 |
| Accuracy / Critical Hit / Block | 100 / 150 / 150 |
| 同 ID 官方名称 | DE：Altes Großschwert；ES：Espadón viejo；JA：古びたグレートソード |

这证明“可以取得真实数值”，没有证明整个数据库都已齐备。实测 TW 的另一物品 ID 在 Global 返回 id=0 的空模板，因此必须同时检查内容有效性，不能只看 HTTP 200。

### 4.3 本轮没有确认可用的数值

| 需求 | 当前判断 | 可行替代 |
|---|---|---|
| 实时拍卖价、完整挂单 | 未核到可用 Global 市场接口 | 用户输入价格；经同意提交截图与时间戳 |
| 全服人口 / 实时在线人数 | 服务器目录没有这类字段 | 只报告站内查询样本，并说明偏差；Steam 指标也不覆盖 PURPLE/跨地区全部玩家 |
| 全技能系数、CD、最终伤害公式 | 角色技能列表不够 | 版本对应的客户端资料、游戏内实测、截图和可复核实验 |
| 精确掉率 | 未找到足够官方接口证明 | 显示可核实的获取来源；社区记录附样本量，不把权重当概率 |
| 可变世界 Boss 的真实刷新 | 固定事件计时与 Boss 死亡状态不同 | 玩家上报死亡时间，标可信度与误差；未知时不显示假精确倒计时 |
| 未开放内容是否已实装 | 静态目录不能证明 | 官网公告 + 当区游戏验证；不按目录记录数宣称可玩副本数 |

## 五、其他数据渠道与玩法

| 渠道 | 获取内容 | 更新/准确性特点 | 建议用途 |
|---|---|---|---|
| Global/KR/TW 官网公告与补丁 | 变更、活动、维护、条件、已公布数值 | 官方优先；三地区分别保存，不用 KR 补丁覆盖 Global | 页面更新提示、版本变化记录、活动与维护汇总 |
| 官网物品/角色 JSON | 装备模板、角色配置、部分节点 | 当前可用但地址可能变化；缓存与有效性检测必需 | 攻略数值卡、官方多语言名称、角色装备解释 |
| 客户端静态表与文本 | 物品/配方/技能说明/坐标/素材 | 多家竞品自述采用；本轮没有提取或验证一套完整客户端数据 | 后续补充 Global 数据；先确认获取与使用条件、版本和字段语义 |
| 游戏内截图 / 人工记录 | 属性、强化成本、配方、实际条件 | 工作量较高，但可小量验证；OCR 结果必须人工复核 | 先做常用装备与关键选择的高质量资料 |
| 官方 Discord / 经许可社区资料 | 公告、纠错、玩家测试与地区差异 | 官方身份、原帖时间、许可、版本需要记录；传闻独立标注 | 提炼高频问题、补攻略缺口、验证地区冲突 |
| YouTube / 创作者 | 操作、路径、Boss机制、配置 | 使用字幕与时间点留日志；一段视频不能证明通用数值公式 | 攻略步骤、路线证据、作者署名示例 |
| 用户主动提交配置/测试日志 | 常见 build、成长样本、战斗观察 | 有样本偏差；工具依赖与维护较重 | 后期做配置分布与社区 build；不优先开发独立 DPS 程序 |
| Steam 官方页面/新闻/公开指标 | 平台信息、公告、Steam维度数据 | 可补平台资料，不能提供完整游戏属性或全平台人口 | 对应本站 steam/download 页面 |

产品与获客建议（属于本次推导，效果尚待验证）：

1. **攻略内数值卡**：读者看到推荐装备时，直接查看当前 Global 属性、适用职业和取得来源；返回原攻略继续阅读。
2. **角色导入后的选择解释**：比较物品的可确认属性差异，再给阶段性建议。伤害公式未核清前，避免承诺精确 DPS 提升。
3. **时区计时 + 日周清单**：固定时刻取官方计划，进度先存在本地；只显示已经核到的活动。
4. **制作 / 强化预算**：成本资料核验后再上线；价格让玩家填写，分别展示期望成本与更保守预算。
5. **带作者的 build 与路线**：支持链接分享和引用卡，与创作者合作；本轮没有联系任何作者，也没有获得其内容授权。
6. **版本差异与更新提醒**：每个数值附地区、采集时间与版本状态；数值变更后更新已引用它的攻略。
7. **商业化顺序**：先验证回访与工具使用，再考虑去广告、跨设备保存、更多保存方案等便利功能。竞品已证明这些模式存在，未证明本站能赚多少。

## 六、本站怎么落地：沿用现有 20 个优先词

这里没有新增、合并或修改词库，只把功能建议映射到现有内容。内部数据表不必全部变成可索引薄页。

| 优先级 | 已有关键词 | 建议增强 | 上线前必要证据 |
|---|---|---|---|
| P0 | aion 2 builds / aion 2 cleric build / aion 2 chanter | Global 装备/技能配置卡、物品差异、适用阶段 | 有效 Global 物品；技能只展示已核字段；推荐理由需玩家实测 |
| P0 | aion 2 classes / aion 2 tier list | 当前职业目录；角色定位与选择条件；样本统计后置 | 当前 Global 8 职业；不能从战力样本推出绝对强弱 |
| P1 | aion 2 server / aion 2 maintenance | 官方服务器目录、公告时间线、地区筛选 | 目录不代表人口；维护来源与时区核验 |
| P1 | aion 2 spacetime rift / aion 2 pvp | 当前地区时区计时、准备清单 | 官方活动计划；不假装取得世界状态 |
| P1 | aion 2 map / aion 2 gathering / aion 2 leveling | 小范围路线、已核地点与个人进度 | 坐标/掉落/路线需额外来源；角色接口不能提供完整地图 |
| P1 | aion 2 code / aion 2 twitch drops | 奖励、条件、结束时间与来源卡 | 官方公告核实；不靠物品目录推断可领活动 |
| P2 | aion 2 character creation / aion 2 presets | 作者署名示例与版本对应说明 | 用户许可与实际可导入性；Global 外观分享接口未实测成功 |
| P2 | aion 2 steam / aion 2 download / aion 2 monetization / aion 2 guide | 当前官方条件与重点决策卡 | 以 Global 官方来源更新，金额/条件不搬用 KR/TW |

**建议第一步：取 20–50 个真正出现在本站 build 攻略中的 Global 物品，做版本化数据卡，先验证 2–3 篇攻略的帮助程度。** 下一步再做角色导入和小规模装备对比。暂缓全量数据库、实时市场、全服排行榜和独立 DPS 采集器，原因是数据或维护条件尚未齐备。

衡量效果时看：攻略到工具的点击、使用后返回攻略、保存/分享、7 日回访、搜索点击和页面是否过期。数值规模大、收录页多，并不能单独证明用户满意或可盈利。

## 七、证据与仍待补充的部分

- [competitors.csv](competitors.csv)：19 个竞品，注册时间、公开时间证据、特点、地区、商业化和流量口径。
- [source-index.csv](source-index.csv) / [source-index.json](source-index.json)：132 条抓取元数据，URL、UTC 时间、HTTP 状态、哈希与文件路径。
- [api-verification.csv](api-verification.csv)：32 条官网接口核验，含非 JSON、空模板、空榜和超时。
- [browser-observations.md](browser-observations.md)：Questlog 与开发者门户的实际 UI 观察。
- raw/：原始 HTTP 响应与文本；web/：检索、网页读取及开发者声明日志。原文件保留，错误记录也保留。

待补充而非编造：多数独立站的真实当期流量、.gg 注册日期、平台 AION2 子目录流量、部分站首个上线日期、每个工具的算法准确性、移动端完整流程、Global 非 EU 四区实际接口请求、全套高阶装备/技能覆盖、数据再分发条款与正式开发者支持。

本报告依据公开来源与本轮有限验证，不把竞品自己的“完整/实时/精确”宣传当作已独立核实的事实。日期、地区和版本状态要跟随每条资料，而不是跟随整站名称。
