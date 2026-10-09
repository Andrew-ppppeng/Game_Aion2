# AION 2 内容更新与后续优先级

## 当前状态 · 2026-10-09

已发布内容以 `content-topics.json` 为准：38 个主题、152 篇四语文章。以下 10 月 3/4 日的数量与候选状态属于历史记录，不能作为当前剩余待办。

本次首期重组 Tools / Guides / Classes / Resources，保留全部现有文章网址，并增加全职业通用成长清单。`/global-changes` 继续跳转到新手指南，不恢复地区比较页；TW/KR 访问与专用玩法队列不进入公开站点。

后续顺序：维护现有职业与成长内容及奖励窗口 → 职业专用成长清单（先 Cleric、Chanter）→ 制作／购买成本决策 → 有证据的单区域路线。数据库与自动行情分别通过目录、报价数据验证后再启动。职业转换、职业宏、Arcana 等缺口先补证据，成熟后由现有主题承接。完整待办见 [拓展 TODO](AION2-EXPANSION-TODO.md)。

更新日期：2026-10-04。目标：未来 30–90 天最大化可获得的 SEO 流量。当前完整词库 **87 项**（原 63 项保留，新增 24 项），历史第一版优先内容为 20 项；当前发布清单使用 `content-topics.json`。

## 10 月 4 日更新

已实现 3 个新主题（Wings、Database、Global changes）与 11 个既有主题的四语更新，总计 **31 个主题、124 篇攻略**。实际 Google 联想和结果页用于选择内容方向；Classes、Max level、Wings、Database、Specs 均纳入本轮需求。详情与验收见 [本轮实施记录](SEO-CONTENT-UPDATE-2026-10-04.md)。

下一步先补职业转换、单服容量、EU 机房城市等具体证据，以及 TW 境外访问、Global 主机/Brawler 日期等条件；资料成熟后才补相应答案。Private server、Raid 2026、Fishing release、AION 1 地图连接关系与 Japan VPN 继续暂缓。Database 本轮为查询入口指南，完整自建数据库另行评估。

上线后 D+14、D+30 以 GSC 收录、页面/查询/国家曝光与点击调整顺序；未出数据不记零。逐词状态见 `research/keywords/2026-10-04/implementation/keyword-coverage.json`。以下保留 10 月 3 日历史批次和其余证据队列。

## 拓展 TODO（暂缓实施）

- [ ] [游戏站拓展完整方案：成长目标、成本决策、分阶段配装、收藏路线与 Marketplace](AION2-EXPANSION-TODO.md)。2026-10-04 记录；用户明确要求暂时先不做，仅保存方案，不启动开发或行情数据验证。

## 10 月 3 日历史批次

| 内容组 | 承接页 | 实施范围 |
| --- | --- | --- |
| 职业识别与选择 | `/classes` | 八职业官方图标、英语与本地名称对照、90×94 原图放大、职业页直达链接 |
| 职业攻略 | `/gladiator`、`/ranger`、`/spiritmaster` | 新增四语起步指南；Gladiator build、Ranger leveling build、Spiritmaster Daevanion 合并到对应职业页，区域实例与 Global 已确认事实分开 |
| 阵营与转服 | `/races`、`/server-transfer` | 新增四语；转服为 10 月 14 日公告条件与准备指南，未编造开放后的菜单操作 |
| 工具与宏 | `/notmeter`、`/macro-guide` | 新增四语；维护者安装说明、Global 兼容性限制；游戏内宏菜单原图、技能优先次序与测试方法 |
| Steam 与玩家人数 | `/steam`、`/player-count` | 同页补地区、平台、预注册边界；玩家人数合并 SteamCharts/SteamDB 需求，展示带时间的第三方快照 |
| 既有高需求页 | `/chanter`、`/map`、`/maintenance`、`/download`、`/monetization` | 更新标题和说明，明确 build/skills、interactive map、server status、PURPLE/PC requirements、free/founder pack 意图 |
| 社区与计时入口 | `/guide#community-resources`、`/spacetime-rift` | 四社区资源表与地区标注；连接已有代码、Drops、维护计时，不编造 Global 裂隙周期 |

新增 **8 个主题、32 篇本地化页面**，总计 **28 个主题、112 篇攻略**。英语、日语、西语、德语均有完整正文、目录、来源与导航。SEO 验收按意图覆盖和索引页面统计；同义词不重复计算新增页面。

## 下一批的执行顺序

| 优先级 | 需求与承接方案 | 制作前必须补足的证据 |
| --- | --- | --- |
| P0 持续 | 维护 `/steam`、`/code`、`/twitch-drops`、`/maintenance` 的开放与奖励窗口 | 最新 Global 通知、时区与明确截止时间；新窗口不能沿用旧倒计时 |
| P1 待证据 | 删除角色独立教程、重做外观独立教程 | Global 菜单实图、等待/取消、名称重用；外观券具体用途与确认流程。现有奖励券只能证明道具存在 |
| P1 待证据 | 职业宏：先 Cleric，再 Ranger | 可复现 Global 技能、延迟、治疗/应急按键；通用宏页不能充当已测职业模板 |
| P1 待证据 | Arcana 一篇系统指南，先验证 Chanter 案例 | Global 装备槽、用途、升级、转化及案例。现有 Season 2/3 韩服资料不能直接移植 |
| P1 待证据 | `/spacetime-rift` 增加有效 Global 倒计时 | 具体地区、时区、开门周期与两次以上客户端观察；当前玩家资料冲突未解决 |
| P2 待证据 | Odyle Energy、Dimensional Invasion、training dummy、Global roadmap | 分别补用途/消耗/恢复，活动入口/流程/赛程，两阵营木桩地点/路线，正式 Global 路线公告 |
| P2 条件性 | Class quiz、Brawler、完整数据库 | Quiz 要有可解释角色选择逻辑；Brawler 要有 Global 开放证据；数据库要有完整、可维护的数据覆盖 |
| P3 暂缓 | Review/gameplay、G2G/Lagofast 独立页 | 前者需真实当前体验，后者以品牌导航为主；没有独有答案时先避免重复薄页 |

顺序综合现有覆盖、需求体量、增长、搜索意图、答案竞争、证据成熟度和制作/维护成本。Rising 的相对增幅不能当绝对体量；Breakout 不能直接推断高流量。Similarweb 是截至 9 月 30 日的全球近 28 天辅助数据，未逐词查完 63 项，也未按国家分量；不汇总重叠同义词体量。

详细逐词状态见 `research/keywords/2026-10-03/implementation/keyword-coverage.json` 与 `coverage.md`。来源缺口审计见 `research/content/2026-10-03/seo-expansion-implementation/global-gates-reviewed.md`。历史调研、原始字幕和 Discord 资料只追加、不覆盖。

## 验收与复查

- 发布必须四语正文、来源、目录、素材一致；登记后进入导航、路由、sitemap、hreflang 与动态文章计数。历史 20 项文件不再承担当前发布状态。
- 每次发布执行 `npm run check`、`npm run test:content`、`npm run build`，在新构建上运行 smoke/browser。重点检查 canonical、索引状态、链接本地化、手机溢出、图标键盘放大与未知/过期计时。
- GSC 正式属性为 `aion2wiki.space`。本轮近 28 天报告仍为 Processing data，点击、曝光、CTR、位置记未知；不能把未出报告写成 0。
- 以实际上线日期为 D0，D+14、30、60、90 人工读取 GSC 的页面/查询/国家指标。先处理已获曝光但标题意图不匹配的页面，再用来源已成熟的新主题承接缺口。对未出数据或未索引页先核查原因，避免凭空判断内容失败。
- 复查同时记录收录状态、页面点击/曝光、目标查询覆盖和成本；结合收录、意图和来源判断下一轮更新，避免仅凭零点击单项删除内容。
