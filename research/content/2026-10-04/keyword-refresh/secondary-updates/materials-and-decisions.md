# 第二组内页更新：素材与决策

- 核对时间：2026-10-04，UTC 原始请求时间见各 `*-request.json`；主要请求为 06:23 UTC。
- 页面语言：英语、日语、西语、德语；玩家内容优先 Global。
- 搜索方向：root 实际 Google 搜索框观察，英语 UI、当前会话 Hong Kong 页脚。联想不表示全球排名或搜索量；详细记录由 root 保存在 `research/keywords/2026-10-04/google-autocomplete-refresh/`。
- 词形只合并、纠错、统一主题；未把自行组织的小标题加入词库。
- 内部来源保留在 article-data 和本目录；正文只保留玩家实际需要打开的工具、下载、支持入口。

## aion 2 gathering map

- 承接：`/map#gathering-map-filters` 和 `/gathering#gathering-routes`。
- Google 方向：resource map；其余许多联想/结果指向 AION 1，排除。
- 当前工具原件：[Aion2T](https://aion2t.com/map)，`map-aion2t.html/-text.txt/-request.json`；[Aion2Maps](https://www.aion2maps.com)，`map-voxel.html/-text.txt/-request.json`。
- Aion2T 当前 UI 提供 Hide All、Gems/Ore/Herbs/Vegetables/Logs 层。旧 Global → Verteron → Aria 交互例保留 2026-10-03 的实际浏览器日志和截图，未把分类总数当 Global 节点总数。
- Aion2Maps 当前 UI：Enter 搜索、Alt 透视、Floor slice / PgUp/PgDn、F 完成、Settings → Your progress → Export progress / Import…。替换过时的同步码说明。
- 地区：工具含 Global 与 TW 地图；晚期地图卡片标 not open at launch，不作为 Global 已开放区域。
- 操作限制：工具地点不是当前在线节点；未验证实时刷新或复活时间，未填具体再生间隔。Export/Import 控件确实存在，导入往返和恢复未实际提交，不承诺账号云同步。
- 分工：map 教筛选、查高度、保存；gathering 教节点要求、失败判断、短路线有用产量，避免复制整篇工具说明。

## aion 2 gathering

- 承接：`/gathering#route-results`，保留既有熟练度、技能及昇阶章节。
- 2026-01-28 [NC anti-bot 公告](https://about.ncsoft.com/en/news/article/aion2_update_260128)：KR 采集解锁提升到等级45；本轮保存 `kr-antibot.html/-text.txt/-request.json`。
- Global 早期采集与 Asmodian Novice50 昇阶资料沿用历史核对，不将 KR 45 条件混入 Global。原始视频字幕及 Global 玩家记录不覆盖。
- 本轮新增的十分钟比较、材料/产量/分钟/失败记录属于操作建议，不写成测得最佳路线、时薪或固定收益。
- 缺口：没有新的官方 Global 节点坐标、再生秒数或“全职业最佳”路线证据。

## aion 2 global server

- 承接：`/server#global-server-regions`。
- Google 方向：locations/list/names/release date/region/sea server/discord server。
- 官方地区与启动器规则：[Launch FAQ](https://store.steampowered.com/news/app/3393110?emclan=103582791475596239&emgid=680761758839734961)，2026-10-01；本轮读 Steam ISteamNews 官方 feed，`steam-global-news.json` 内 title=Launch FAQ、gid=1845383656377634。
- 官方直接确认 NA/SA/Europe/Japan locations；客户端地区有 NA West/NA East/Europe/South America/Asia。将 Asia 说明为 Global 日本主机地区，未添加独立 SEA 服务名称或预估延迟数。
- Steam/PURPLE 同内容同服；Steam独立游玩不需PURPLE绑定，同角色跨启动器才需绑定；TW/KR进度不转Global。
- 初始服务器名单与配对重新读取 `global-access-servers.json`、`global-matchmaking.json`，10/2 更新版本。新增EU Hithanya/Nemon已在现表，保存 `global-new-eu-servers.json/-text.txt`，没有另加重复行。
- 一般地区指导放在 EU-only GuideRegion 组件之外，避免非EU读者看不到。

## aion 2 how many players per server

- 承接：`/server#queues-and-population`；**准确容量数和当前单服在线数仍不覆盖**。
- 官方没有在本轮可读公告给单服容量。Steam总并发既不能分解为某服人数，也不含PURPLE，禁止推算。
- 有用已知条件：[Launch Scale Test Comes to a Close: What's Next?](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010496396)，2026-09-19。当前官方feed有会员优先队列，空位出现才前进；优先并不保证立即登录，违规可失去优先。
- 正文解释队列与并发口径，不用空洞FAQ制造一个虚构容量答案。

## aion 2 eu server location

- 承接：`/server#queues-and-population`；**物理机房城市仍不覆盖**。
- 官方 Launch FAQ 只给 Europe 地区，没有 Frankfurt/Amsterdam 等具体城市；不从服务器名或第三方测试推断。
- 正文给 Europe 选择与在自己的常用时段比较连接的操作，保留地理细节缺口在内部。

## aion 2 eu release date

- 承接：`/steam#europe-launch-time`，保留原 `access-schedule` 锚点。
- Google 方向：European release date / EU server release date / Europe launch date，合并同意图。
- [Advanced Access Servers](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab85cc646be804931c31335)：公开开启 2026-10-05 13:00 UTC；EA到05:00 UTC，维护05:00–13:00 UTC。
- 日期：9/29发布、10/2更新、10/4重新读取 `global-access-servers.json`。
- BST14:00 / CEST15:00 / EEST16:00 是从 UTC 推算的10月5日当日民用时区转换；不是三个地区另有公告时刻。维护会变化，保留该条件。

## aion 2 console release

- 承接：`/steam#platform-and-controller-support`。
- Google 方向：console release date/version/global release date console。
- 10/1 官方 Launch FAQ：目前仅 Windows PC Steam/PURPLE 受官方支持；控制器可用但非官方支持，Linux/Steam Deck没有官方支持；Global移动端问题只给Steam/PURPLE。
- 本轮未发现 PlayStation/Xbox 发售日期，不编造日期，也不声称永远不会出。正文保留“没有确认的主机日期”的重要平台限制。
- 原文旧“控制器检查状态未确认”的缺口现在已有 Launch FAQ 官方答案。

## aion 2 how to play

- 承接：`/guide#how-to-play-by-region`，台湾安装步骤由另一个 agent 在 `/download#taiwan-client` 实现。
- Google 方向：in US/on Taiwan/in Europe/Taiwan server/now/with friends/in NA；Spiritmaster玩法交给职业页，不复制职业全文。
- 新增NA/EU/TW服务入口表，突出当前EA权益与免费开放、同区同族同服、Steam/PURPLE共同游玩，不把启动器绑定当成找朋友的前置条件。
- TW官方入口本轮已读：[Taiwan download](https://tw.ncsoft.com/aion2/download/index)，`tw-download.html/-text.txt/-request.json`。提供PurpleInstaller → PURPLE STORE → AION2 → 安装游戏步骤。
- 缺口：该下载页不提供境外认证、支付、账号合规和VPN进入条件，不能声称任何国家安装后必定可玩；未执行注册或购买。

## aion 2 taiwan discord

- 承接：`/guide#community-resources`。
- 原词保留，联想多为AION 1噪声，不造新词。
- 10/4 Discord公开invite解析：`aion2official` → guild1433227540184567928 AION 2 Global (Official)；`AION2` → guild1377004046832894095 AION 2 Community，保存对应json/request。两个服务不会混标。
- [社区管理者2025-09-17说明](https://www.reddit.com/r/Aion2Hub/comments/1njbn8v/)历史指出TW交流及TW公告合作，但**不据此声称台湾官方运营Discord**，未声称当前具体频道已逐个确认。
- 只增一个实效社区邀请，明确community-run及Global/KR/TW范围，继续保留Bahamut及Global官方邀请。

## aion 2 what does quna do

- 承接：`/monetization#quna-use-and-budget`，保留 `currency-and-trading`。
- Google 方向：price/exchange/buy/shop/how to get quna；语义不清的kina-to-kina不收。
- [Team Update](https://aion2.plaync.com/en-us/board/notice/view?articleId=6a4d7d47a729ca5877f5e1ef)，7/8发布、7/17更新；正文是图片，本轮抓JSON及图片并人工查看 `global-team-update-image-1.png`，避免把没有文本当成无信息。
- Quna用于商店、Battle Pass与Exchange买Kina；也能出售Kina获得Quna；会员Market+Exchange；玩家驱动汇率不等于现金Quna包价格。
- US会员$15/月是公告参考价，仍要求看当地结算货币和税；未推测具体Quna充值比例或礼包档位。
- Steam Founder三个美元价格在本轮 `steam-founder-us.json` package_groups核对：24.99/49.99/99.99，保留US限定。

## aion 2 how much do i have to p2w in global release

- 承接：`/monetization#quna-use-and-budget` 和 `founder-cosmetic-access`。
- 免费基础入场、会员取交易权限、pass给成长资源、外观无战斗数值分开；不存在资料支持的“最低获胜花费”，不编造。
- 新事实：[10/3 Founder Cosmetics](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac1229d5657e135c2f5ef65)，更新18:18 UTC，本轮 `global-founder-cosmetics.json/-text.txt`。全账号全服务器外观共享**尚待实施、EA后完成**；会员与Supply/StylingChest仍一次性。Steam降档退款操作流程仍待跟进，避免不加条件建议玩家重复购买。
- 购买故障的现有操作和support链接保留；未执行任何支付或联系支持。

## aion 2 talent calculator

- 承接：`/builds#talent-calculator`，保留现有 `save-and-improve-your-build`。
- Google方向：skill calculator，排除Classic计算器。
- root实际CUA打开 [Global Build Planner](https://aion2.gaming.tools/build-planner)，Global 1.0.21.0、Oct1更新；完整交互记录在统一Google日志目录 `planner-ui-check.md`。
- 浏览器实测：Gladiator Lv45、Skills初始0/203；Raise KeenStrike 1→2后1/203；刷新保存，Lower恢复0。预算是工具显示，不表示逐项验证服务端所有点数来源。
- 文中讲Raise/Lower及预算、Active/Passive/Stigma、浏览器持久化、Save to My Builds账户条件；未注册、未保存账号build、未声称分享和跨设备恢复已实际测试。
- 本agent的直接HTTP请求403只说明该请求受限，不能称该工具失效；另DBAion页面原件保留，但不堆砌未交互验证工具。
- Codex旧guest链接只有SSR外壳且未验证保存，替换为本轮实际操作工具；Aion2Hub Cleric目录继续保留，并补其明确Global test / KR-TW v110差异。

## 验收

- 28篇MDX/metadata及7组article-data完成；已有图片、工具组件、内链和原锚点保留。
- 本agent检查28篇JSON解析、TOC存在、ID不重复、GuideRegion标签平衡及无明显英语研究过程残留通过。
- 全站check/content/build/smoke由root统一执行，避免并行构建冲突。

## 交叉审核修订

- 按 primary/root 的P2建议，四语删除服务器幻想名与机房城市的举证式说明，直接保留Europe选择、常用时段延迟比较及转服条件。机房城市仍是内部缺口。
- 四语Linux/Steam Deck行简化为无官方支持，删除“成功启动不能证明兼容/反作弊”重复说明，保留controller实用测试与键鼠准备。
- `/guide`台湾安装链接采用文件owner已实现的`/download#taiwan-client`，四语一致。
