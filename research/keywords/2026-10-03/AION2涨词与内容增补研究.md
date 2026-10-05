# AION 2 涨词与内容增补研究 · 2026-10-03

**先完善职业图标识别；删角色、Cleric 宏先补 Global 证据；Arcana 集中验证一篇系统指南。**

- 八职业图标已有素材，也已在四语言职业页显示。下一步是放大识别、名称对照和独立定位入口。
- 计划中的涨幅属于 **17:45–18:02 北京时间**的前次观察。本次晚间复核有变化，旧值不能当作当前实测值。
- **本次只新增研究报告与证据档案。** 下文的新路径都是拟议承接页，不代表已写好或已上线。

## 研究口径与证据

目标：AION 2 攻略站的英语、日语、西语、德语增补；市场分别读取 Worldwide、JP、ES、DE。平台沿用项目的 Global PC 内容，KR/TW 只作有地区标记的材料线索。反馈以小规模内容验证为目标，不预测点击或收入。

本次复核时段：**2026-10-03 20:18–20:27，Asia/Shanghai（UTC+8）**。Trends 均为 Search term、Past day、All categories、Web Search。`now 1-d` 是滚动窗口，不能重建前次观察的完整榜单；本次窗口及抽样结果不同，不足以判定前次观察错误。

全部原词、显示值、读取范围和来源 ID 保存于 [evidence.json](evidence.json)。这是相关可见 DOM 字段的人工摘录，不是平台导出的 CSV；未保存账号、Cookie 等私人数据。

| ID | 实读来源 | 读取范围与限制 |
| --- | --- | --- |
| G1 | [全球 Trends](https://trends.google.com/trends/explore?date=now%201-d&q=aion%202&hl=en) | Rising 全部 10 条，两页；Worldwide 不等于仅英语 |
| G2 | [德国 Trends](https://trends.google.com/trends/explore?date=now%201-d&geo=DE&q=aion%202&hl=en) | Rising 全部 12 条，三页；英文查询仍归英语，市场是 DE |
| G3 | [日本 Trends](https://trends.google.com/trends/explore?date=now%201-d&geo=JP&q=%E3%82%A2%E3%82%A4%E3%82%AA%E3%83%B32&hl=en) | Related queries 的 Rising 选项禁用；只读 Top 前 5/6 条，不能赋增长率 |
| G4 | [西班牙 Trends](https://trends.google.com/trends/explore?date=now%201-d&geo=ES&q=aion%202&hl=en) | Rising 显示全部 5 条，无分页；英文查询不改称西语关键词 |
| S1 | Similarweb 已登录的 Keyword Generator，`aion 2` + 包含 `arcana` | Worldwide / Google / All traffic / Last 28 days / As of Sep 30；完整地址与七行原值在证据档案 |
| A1 | [英语 Arcana 联想入口](https://www.google.com/search?q=aion+2+arcana&hl=en&gl=US) | 输入 `aion 2 arcana ` 后实读 10 个下拉词；无增长率 |
| A2 | [德语职业联想入口](https://www.google.com/search?q=aion+2+klassen&hl=de&gl=DE) | 输入 `aion 2 klassen ` 后实读 10 个下拉词；无增长率 |
| A3 | [日语职业联想入口](https://www.google.com/search?q=%E3%82%A2%E3%82%A4%E3%82%AA%E3%83%B32+%E3%82%AF%E3%83%A9%E3%82%B9&hl=ja&gl=JP) | 输入 `アイオン2 クラス ` 后实读 10 个下拉词；原词实际使用 `aion2` |

联想在现有登录浏览器中读取，搜索页面显示个性化结果。`hl` / `gl` 记录的是请求设置，未独立验证实际国家定位；它们支持词形线索，不构成无个性化的当地全市场调查。没有把搜索结果摘要当作游戏事实或精确排名。

**覆盖：**本地词库 63 个、优先清单 20 个；未逐一重查 63 个关键词。本次归档 27 条当前 Rising 记录。原计划 13 条带增幅的观察中，4 条查询在本次 Rising 复现，9 条未复现或当前不可读取；不据此推断它们需求为零。

## 原计划机会与复核结果

前次数字仅来自用户提供的计划，未找到其原始截图或导出；在证据档案标记 `rawSnapshotAvailable: false`、`verifiedInThisRun: false`。下表保留其原始表述，并单独列出当前直接读取值。

| 原词／市场 | 前次计划记录 | 本次实读证据 | 覆盖状态与承接 |
| --- | --- | --- | --- |
| `aion 2 class icons` · Worldwide | +70% | G1 当前未出现；A2/A3 复现职业图标联想，不能替代 +70% 证据 | `/classes`、`/ja/classes`、`/de/classes` 已有小图；更新识别区 |
| `aion 2 delete character` · DE | Breakout | G2 当前未出现；前次值待复核 | 创建页仅说明删除等待未核实；拟新增 `/delete-character` |
| `aion 2 cleric macro` · DE | +300% | G2 当前未出现；前次值待复核 | `/cleric-build` 有手动顺序，无宏设置教程；拟新增 `/cleric-macro` |
| `aion 2 arcana` · Worldwide | +70% | G1 第 7 条 **+50%**；G2 第 1 条为 Breakout；S1 28 天体量 300 | 无独立系统指南；拟新增 `/arcana`，先做一篇 |
| `odyle energy aion 2` · DE | +180% | G2 当前未出现；前次值待复核 | `/code`、`/twitch-drops` 只提及奖励物品；拟新增 `/odyle-energy` |
| `aion 2 dimensional invasion` · DE | +200% | G2 当前未出现；前次值待复核 | 无专页或已核实赛程；拟新增 `/dimensional-invasion` |
| `aion 2 training dummy location` · Worldwide | +40% | G1 当前未出现；前次值待复核 | `/map` 有地图使用方法，没有木桩位置；拟新增 `/training-dummy-location` |
| `aion 2 timer` · Worldwide | +50% | G1 第 9 条 **+40%**；G2 第 10 条 +90% | 已有活动计时组件；优先按实际活动承接，是否需要统一入口待验证 |
| `aion 2 rift timer` · Worldwide | +40% | G1 第 10 条 **+40%** | `/spacetime-rift` 已有组件和待核实状态；取得 Global 赛程后更新 |
| `aion 2 database` · DE | +170% | G2 当前未出现；前次值待复核 | 只有装备示例、比较与角色查询；拟 `/database`，观察阶段 |
| `アイオン 2 クラス` · JP | +40% | G3 Top 第 4 条指数 **4**，Rising 不可选；4 不是增幅 | 更新 `/ja/classes`，不据此生成重复职业页 |
| `aion 2 es gratis?` · ES | +100% | G4 当前未出现；前次值待复核 | `/es/monetization` 和 `/es/steam` 已有免费／提前访问说明，先检查问答是否直达 |
| `aion 2 interactive map` · ES | +90% | G4 第 3 条 **+80%** | `/es/map` 已有互动地图入口和筛选示例，更新入口表达与易用性 |

英语词序规范化只做允许的整理：`odyle energy aion 2` → `aion 2 odyle energy`，原词保留。类别由意图人工判断：职业识别、角色管理、构筑与技能、Arcana 成长、能量资源、限时活动、练习地点、事件计时、道具数据库；不创建 `general` 或 `gameplay` 等空泛分类。

## 高优先级：职业图标识别

**动作：更新现有职业页，复用八张官方图标。** 八职业、名称和图标顺序已有来源记录，四语言同用 [class-identities.json](../../../src/content/class-identities.json) 与 [guide-assets.json](../../../src/content/guide-assets.json)。[ClassFinder](../../../src/components/class-finder.tsx) 目前将图标显示为 28×29，点击放大针对职业画像；尚无专门的图标放大入口或图标总表。

八张 `emblem-{class}.webp` 均存在于 `public/media/guides/`，原尺寸 90×94。[素材核验记录](../../assets/2026-10-03/source-notes.md)注明来自官方 Global CDN `aion2-global/1.0.0`；这是素材版本，不是游戏补丁号。来源入口为 [官方 Global 职业介绍](https://aion2.plaync.com/en-us/about/index)，本次文本工具只能取得空壳，职业事实沿用已保存的官方快照，不宣称本次重新读到完整正文。

下一轮制作应提供八职业图标／英语名／当前语言名称对照、可定位的识别章节和清楚的图片标签。用原图支持放大查看，不伪称高清重绘，也不将画像当图标。先英语，再日语、德语；共用组件变化需同时验证西语。不得因 KR/TW 有九职业素材而补进 Global 八职业表。

验收：八个图标与职业 ID 一一对应；四语言名称一致；键盘和手机可打开／关闭识别大图；现有画像与角色筛选仍可用。估计编辑及组件工作 2–4 小时，属于工时判断，不是承诺。

## 高优先级：删除角色

**动作：先核实 Global 客户端，再写 `/delete-character`。** [现有创建页](../../../src/content/en/character-creation.mdx)只明确删除等待等限制未独立核实，不能当作删除教程。

待取得的证据：角色选择画面的删除入口与确认提示、适用角色条件、等待时长、倒计时状态、取消入口与截止条件、删除完成后的名称可用性。每项记录 Global 区域／服务器、观察日期和实际客户端版本；没有补丁号就保持未知。名称释放是否即时、跨服务器或仅同服务器，均不能由其他游戏或 KR/TW 规则推断。

截图优先使用可公开核验的官方帮助或 Global 客户端操作记录；本轮官网索引检索未取得直接说明，不等于官方不存在文档。不为了搜集素材删除玩家角色。步骤写作在证据齐全后约 2–4 小时，等待规则和名称重用的验证时间另计。

验收：读者能找到入口、理解等待、取消操作和名称限制；数字逐项有同地区来源；与 `/character-creation`、`/presets` 互链。当前状态为选题与证据清单，尚无可发布教程。

## 高优先级：Cleric 宏

**动作：新增操作教程，与 `/cleric-build` 互链，避免复制整篇构筑。** [现有正文](../../../src/content/en/cleric-build.mdx)已有减益／伤害顺序及治疗、净化、复活的独立按键建议，但不含宏菜单、设置或延迟验证。

可复用线索：[BoredAF 视频](https://www.youtube.com/watch?v=J3nPw7cuDjY)的[已保存字幕](../../youtube/J3nPw7cuDjY.txt)在 03:17–03:27 提及 Judgment／普攻与游戏内宏，04:10–04:20 区分其游戏内设置与第三方程序；作者同时谈及 TW。03:46–04:20 的恢复讨论可作为治疗按键安排线索。字幕不是 Global 当前菜单、宏命令语法或精确延迟的证据。已有[构筑核验日志](../../content/2026-10-03/cleric-build/upgrade-review.md)保留地区差异和技能名冲突。

必须补齐：Global 宏入口及菜单截图、支持的动作／技能数、保存与绑定方法、执行方式、冷却未就绪时的行为、连锁技能处理、延迟单位与实际效果、停止／打断方式。先手动验证技能顺序，再测试宏；治疗、净化、复活能否及时独立使用也要验证。不提供未证实的循环或毫秒值。

验收：读者能按图创建、绑定、修改并停止宏；技能名与当前客户端相符；低等级／不同冷却条件有明确适用范围。时间点只留研究日志。证据齐全后单语言教程及截图整理约 3–5 小时，客户端验证另计。

## 中优先级：Arcana 一篇系统指南

**动作：先验证 `/arcana`，暂不拆 guide、cards、transmute 和职业搭配页。** A1 下拉直接出现 `aion 2 arcana guide`、`aion 2 arcana cards`、`aion 2 arcana transmute`，以及 Gladiator、Ranger、Chanter、Cleric、Sorcerer 搭配查询。它们是联想证据，没有增长率。

S1 当前七条中，`aion 2 arcana` 的 **28 天体量是 300**，`aion 2 chanter arcana` 为 **510**。`aion 2 arcana guide` 和 `aion 2 arcana transmute` 为 `< 50`；不改写为零或具体整数。数据截至 9 月 30 日，不能用来证明 10 月 3 日当天搜索量，也不能加总成预计网站流量。平均体量与近 28 天体量分别保留。

素材起点：[TW 新手视频](https://www.youtube.com/watch?v=C73KG9MvqUk)的[保存字幕](../../youtube/C73KG9MvqUk.txt)05:59–06:43 将 Arcana 作为成长系统，提及属性、技能等级和套装效果；这只支持主题线索。[Chanter 材料日志](../../content/2026-10-02/chanter/research.md)和[字幕](../../youtube/EsxGbxt0k-4.txt)11:19、16:28 的附近段落涉及 Arcana 与技能，尚不足以产生固定职业配卡结论。

先用 Global 证据核实装备槽与类型、卡片用途／来源、升级材料与效果、转化入口／消耗／结果、套装触发；每个数值保存来源、日期、服务器和版本。KR/TW 后续系统与 Global 初期规则分开。Chanter 先验证一个具体案例：现有技能、卡片等级、预期效果与实际观察相符后，作为同一篇中的搭配示例，不能由“510”推导它是最强构筑。

可见搜索样本已存在媒体、Wiki 与视频答案，不能认定低竞争；本轮未完整检查这些页面或测量 KD。单篇增量应是可核查的 Global 操作图与版本对照。资料和客户端证据足够后约 4–8 小时。若主要规则仍只能找到 KR/TW，保留选题；若后续曝光和查询仅集中于系统入门，继续维护一篇。

## 其余机会：范围与证据门槛

| 主题／优先级 | 拟承接与核心增量 | 缺少的证据、更新触发 |
| --- | --- | --- |
| Odyle Energy · 中 | `/odyle-energy`：用途、消耗、恢复、获取；与 `/gathering` 采集资源分开 | 现有 `/code` 和 `/twitch-drops` 的奖励物品名称不能证明能量系统公式。核实“能量资源”与“补充能量的物品”的关系，勿混用同名采集材料 |
| Dimensional Invasion · 中 | `/dimensional-invasion`：入口、流程、奖励；取得赛程后接现有计时器 | Global 是否存在、解锁条件、地区赛程／时区、奖励均待核；不得套用裂隙活动规则 |
| Training dummy · 中 | `/training-dummy-location`：分阵营的地图、地点高度、路线与现场图；链接 `/map` | 缺两阵营 Global 地点证据；无坐标或路线时保留选题，不画假标记 |
| Timer／Rift timer · 中 | 复用活动计时组件；裂隙查询由 `/spacetime-rift` 承接，其他计时按活动分流 | [现有事件记录](../../../src/content/game-data/events.json)的裂隙时间为 `null`。[研究日志](../../content/2026-10-03/spacetime-rift/upgrade-review.md)保留 KR 四小时与另一报告三小时的冲突；不能拼成 Global 周期 |
| Database · 观察 | 先核实用户想查的道具类型和筛选任务，再决定 `/database` | [数据接入记录](../../../docs/AION2-DATA.md)只有 22 件装备示例及角色查询等数据；不覆盖所有物品、卡片或掉落。来源覆盖和维护能力达到要求后才立项 |

## 四语言与去重安排

| 语言 | 本轮承接 | 证据性质与限制 |
| --- | --- | --- |
| 英语 | 职业识别更新；独立删角色与宏选题；一篇 Arcana 系统指南 | A1 实际下拉词与 G1/G2 当前查询分开；英文前缀统一 `aion 2`，只做纠错、词序统一与同义合并 |
| 日语 | 更新 `/ja/classes` 的图标与推荐选择入口 | A3 实际词是 `aion2 クラス アイコン`、`aion2 クラス おすすめ`；显示标题沿用项目 AION2 术语规范；原计划 `アイオン 2 クラス +40%` 尚未复现 |
| 西语 | 优先检查 `/es/monetization`、`/es/steam` 的免费／提前访问问答，再改善 `/es/map` 的地图入口 | `aion 2 es gratis?` 前次 +100% 待复核；G4 的英文 interactive map 当前 +80% 是 ES 市场信号，不是西语词形 |
| 德语 | 更新 `/de/classes` 的职业符号对照；新问题页保留原始查询与德国市场证据 | A2 确认 `aion 2 klassen icons`、`aion 2 klassen symbole`；G2 的英文删除／宏历史查询不能称为德语词 |

制作新页前仍需遵守项目四语言一致性要求；本轮不扩写未观察到的日／西／德关键词，也不将英语翻译自动计为新需求。

| 原词或前次片段 | 归并主题 | 页面覆盖情况 |
| --- | --- | --- |
| `steam aion 2` | `aion 2 steam` | 已有 `/steam`，无须为词序再建页 |
| `aion 2 not meter` | `aion 2 notmeter` | 已在完整词库“damage meters”分类；不在优先 20 页中，尚无专页。归并不等于内容已覆盖 |
| 前次仅给片段 `build guides` | `aion 2 builds` | 已有 `/builds`；不补造未保存的完整原查询 |
| Arcana guide／cards／transmute／职业搭配 | Arcana 系统主题与案例 | 先一篇 `/arcana`；符合独立任务和证据门槛后再考虑拆分 |
| `aion 2 timer`／`aion 2 rift timer` | 按实际活动映射；裂隙主题统一 | 已有 `/spacetime-rift` 及其他活动组件；不因两个词自动生成两套时间表 |

当前榜单还出现 Spiritmaster Daevanion、Ranger leveling build、roadmap、player count 等查询。已逐条保存于证据档案，**仅作为复核快照，不自动加入本轮内容清单或词库**。`american covid strain`、`erik brown cave rescue diver` 和 `aniimo` 不计为 AION 2 内容机会；`npcap` 的 AION 关联未核实，也不单独立项。

## 指标解释、验收与后续验证

Rising 的增幅比较前一时段；**Breakout 表示超过 5000%，不提供绝对搜索量**。[Google 官方说明](https://support.google.com/trends/answer/4355000?hl=en)。Similarweb 可选月份或近 28 天并区分设备／国家与 Volume／Clicks；本报告沿用实际 UI 列名，未混用体量和点击。[Similarweb 官方说明](https://support.similarweb.com/hc/en-us/articles/20388328460061-Using-Keyword-Overview)。原计划称国家筛选受套餐限制，本次只读现有全球视图，未重测套餐权限，也未购买或升级。

交付检查：

- 原计划 13 条观察均有来源、国家、窗口、前次显示值、当前复核状态与承接安排；旧值未冒充本次已证实数据。
- 当前 27 条 Rising 逐条保留原查询、显示增幅与来源；日本 Top 和下拉联想分别记录，不赋增长率。
- 词库 63／优先 20 数量核对；声明未完成逐词查询；现有页面、素材和内部引用均检查。
- 原始材料、词库与页面保留；新增文件仅在本日期研究目录。`research/` 沿用项目的本地忽略规则，不调整部署或发布。

实际验证通过：证据 JSON 可解析，13 条机会映射完整，27 条 Rising 的序号／原词／显示值有效，4 条复现查询与当前源记录逐项一致，Similarweb 七行与原始列对齐，15 个本地文件链接存在。328 个原有文件 SHA-256 前后相同，Git 工作区状态与本轮开始时一致。本轮没有应用代码变更，验证针对研究档案与引用完整性；没有运行应用构建或浏览器功能测试。

下一次复核建议为 24–48 小时后，按同样市场／种子／窗口保存新快照，重点看职业图标、删除、宏、Arcana 是否再现。内容完成并可索引后，再按语言、国家、查询和承接页检查实际曝光／点击；本次未读取 GSC，不设虚构基线或收益指标。以上是复核建议，未创建自动任务。
