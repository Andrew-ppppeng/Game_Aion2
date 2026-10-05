# 新主题资料审核 — 2026-10-04

范围：英语 Google 关键词方向由 root 的实际搜索框联想记录提供；本站页面以 Global 为主，四语正文独立翻译。观察日期为 2026-10-04，Asia/Shanghai。源码、HTML/JSON 及图片只追加，不覆盖 2026-10-02/03 原件。`capture*.py` 中 URL 均为公共网页或官方公共内容接口。

## 发布结论

- **Database 可发布**：已打开至少两套实际目录与详情，保留 Global/区域快照限制；不是本站自建全量数据库。
- **Wings 可发布限定范围**：早期主线获取、装备/所有/外观区别、飞行操作有材料；不发布全翼数值表、PvE排行、概率、成本或强化面板指引。
- **Global changes 可发布限定范围**：明确比较 Global launch 与 KR/TW Chapter 1 的内容阶段，不声称是两地区最新补丁的完整差异清单。

## Database：实际使用与可用性

1. https://aion2.gaming.tools/items — web 工具实际打开 Global 列表，显示搜索、Faction/Tier/Grade。随后点击实际奖励箱记录 https://aion2.gaming.tools/items/533700175 ，打开选择内容和关联装备。列表标 Global 1.0.21.0、9/30；该详情仍标 Global Playtest 1.0.21.0、9/26。正文要求检查具体页版本，不冒称所有条目都是当前已开放内容。
2. https://aion2.gaming.tools/skills 与 /quests — web 实际打开；技能 Class/Type、任务 Faction/Region/Type 列表存在。Root 另外完成 build-planner 实际点选、加点、详情与刷新保留检查，本文不重复开发工具。
3. https://aion2hub.com/database — 保存 200 HTML。检查真实 form 的 action=/database、query=q；实际请求 https://aion2hub.com/database?q=Ludra 成功，返回 Ludra 武器记录。打开 https://aion2hub.com/database/items/110120003 ，基础/随机/升级/How to Obtain/Regional Comparison 可见。
4. Hub 的真实 Korea/Taiwan 链接为 /database?region=kr，已请求成功。示例装备详情标 **Global Launch Scale Test 2026-09-19 与 KR/TW v110 2026-09-09**，仅用于说明读字段及比较，不把其具体数值或来源可玩性搬成当前 Global 确定事实。
5. https://metabot.gg/en/aion-2 — home/items HTML 200；web 打开方法页、翼详情与两个主线任务页。其方法页声明 Global client build 0.0.4387.0；并非我们独立验证的最新零售构建。本文介绍数据库用途，不复制其“所有资料/掉率都匹配当前Global”的推广保证或完整数量。
6. https://shugo.gg/ 与 /faq — 当前首页有 Global/KR/TW 角色选项，API degraded/offline。FAQ 明确物品字典来自 KR/TW，Global item entry 暂时 disabled；部分 launch 时间和“只能选KR/TW”旧段落与首页冲突。正文只介绍实际搜索入口及 API/区域条件，不承诺已取得成功的 Global 角色详情。
7. https://steamdb.info/app/3393110/ — HTTP 403；不将此链接交付为本轮已核验可用资料入口。保留 SteamDB 是产品档案而非游戏掉落数据库的用途区别，转链现有 `/steam`。App ID3393110与官方Steam既有资料一致。

## Wings：事实与版本门槛

- **官方 Global 总体飞行**：https://aion2.plaync.com/en-us/about/index 的公开 about-en JSON 已重抓。Flight 表述支持自由探索，未据此推断无限飞行时间或所有区域无条件飞行。
- **部分副本也可飞行**：官方视频 https://www.youtube.com/watch?v=S_TjiOh33a4 ，既有原字幕 `research/content/2026-10-02/leveling/S_TjiOh33a4-transcript.txt`。**25:42–25:59** 明确谈到在部分副本区域展开翼并飞行。本文没有写“副本一律禁飞”，也没有推断所有副本能飞。
- **初期主线/解锁**：Kevin Link 的 https://space4games.com/en/games-en/aion-2-beginner-guide/ 为本人 Global LST 体验，日期9/28，Level Guide 推荐 First Ascension/Wings 5级。本文写 recommended around5/完成主线，未把达到等级本身写成硬解锁条件。
- **两阵营具体入门奖励**：web 实际打开 https://metabot.gg/en/aion-2/quests/the-power-in-the-lake 和 https://metabot.gg/en/aion-2/quests/the-being-beneath-the-lake 。Elyos：Daminu/Poeta、Lesser Daeva Wings、下一步 Fledgling Wings；Asmodian：Elvida/Ishalgen、Lesser Daeva Wings、下一步 Spread Your Wings。页面自标 Global client0.0.4387.0。Elyos 原件请求200；Asmodian 请求timeout但本轮 web 成功读取完整页面。保留失败记录，不假称所有原件下载成功。
- **装备/所有两栏**：本轮 web 打开 https://metabot.gg/en/aion-2/wings/lesser-daeva-wings ，见 Stats when equipped / Owned effect 两个面板、注册持有后即使换翼仍适用、Elyos/Asmodian两个starter版本相同装戴属性。原HTML请求先后timeout，实际web页面审核成功。本文未抄数值或全部翼效果。
- **键位**：https://space4games.com/en/games-en/aion-2-best-settings-guide/ 实际 web 打开并重新抓200。本人 Global LST 菜单截图列 V / Shift / Space / Ctrl+R / Ctrl+F / Alt+C；初始拼错 settings URL 的404记录保留。本文同时说明自定义键位优先、可在Key Settings确认；不把其测试版UI缺失/图形项原封扩入当前攻略。
- **Founder与商店翼外观**：官方 Business Model 图片来源在 https://aion2.plaync.com/en-us/board/notice/view?articleId=6a4d7d47a729ca5877f5e1ef 。已另存 `founder-business-model.png` 并以原分辨率视觉检查：第6节 In-Game Shop 的 Cosmetics 列明 Wings，写纯外观/no gameplay or combat advantage。最终素材URL及原API都保留。本篇没有把付费 Blazing Sun 的客户端占位属性写成力量收益。
- **Blazing Sun资格与共享待实施**：https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac1229d5657e135c2f5ef65 的10/3公告已抓200完整正文。Ultimate 包含BlazingSun；全账号全服务器共享仍在实施，完成时间在EA结束后；membership、SupplyChest、StylingChest排除且仍one-time。四语明确 pending，不承诺玩家此刻所有角色可领取。

### 强化冲突：删除相关指引

MetaBot翼表有 up-to+10、升级成本以及“owned效果增长”的字段，但对LesserDaeva所列各级值完全相同，且Special翼会混入商业外观条目。https://aion2maps.com/guides/wings/ 的Global客户端解读指出Global没有翼强化、所有效果固定，与前述表格冲突。没有当前Global强化操作界面实证。

因此四语均删除：owned效果随等级变化、Global翼强化面板、翼强化费用与材料建议。也没有把社区“不能强化”直接升级为官方确定事实。Wing获取、装备、收藏、外观、操作仍可独立回答需求。`finalize-copy.py` 记录这一改动；原始草稿留研究内。

## Global changes：已确认范围

- Global roster：上述官方 about-en API 8职业及Verteron/Altgard地图介绍。
- Global level45：官方9/4 Dungeon Showcase的既有字幕/leveling资料；另有 Global LST 本人体验与当前Global公开资料交叉支持。未写新的更高级上限。
- KR/TW Chapter1：https://about.ncsoft.com/en/news/article/aion2_update_260706 已重新抓200、全文检查。7/6新闻确认cap50、Brawler、Eltnen/Morheim以及两个lv50/3500新副本。本文明确Chapter1内容阶段，未将旧公告冒称KR/TW当天全部最新机制。
- Global访问时间与地区：既有官方server-access公告，root/secondary此次同步重查；日期仍按9/30 AA与10/5 13:00UTC区分。
- Founder最近改变：10/3新公告如上，是宣布后的实施状态。quickAnswer采用 awaiting implementation，不暗示已经部分发放。
- 不纳入：LST与当前Global全面装备倍率/交易/掉率/强化削弱比较、未来追版本时间表、服务器物理位置、无当前证据的P2W具体金额。

## 输出与校验

生成：3主题 × 4语言 MDX/metadata，共24个文件，另3个article-data内部证据文件；现有原件保持。

局部检查 `check-new-pages.py` 已通过：12篇正文长度达标、6个目录锚点、4步可视流程、GuideNext一致、四语链接/表格/交互位置一致、无来源footer/研究口吻/乱码占位、内部sources与related可用。正式项目注册、全局内容检查、构建、浏览器检查由root统一完成。
