# /races 玩家深度独立复核

日期：2026-10-04（Asia/Shanghai）。范围：只读审查现有 en/ja/es/de 的 races.mdx、races.json、article-data/races.json，复核已有官方 Global 归档和相邻主题资料。没有修改 src、脚本、原始资料或既有日志。官网差异和图片由 world_guides、service_guides 分工研究；本记录不重复下载图片。

## 结论

现有页面准确保留了各阵营独立服务器、PvP 对手配对和同阵营转服限制，但“阵营有什么玩法差别”回答不完整。首张表两条 Useful decision 都以“喜欢世界且适合朋友”循环解释，缺少对比标准；Class 行只有角色数，没有回答两阵营可选范围。创建清单第 3–5 项没有明确检查对象、判断标准和失败分支。四语正文和摘要存在同样缺口。

官方 Global 副本直播已经能够支持跨阵营、跨服的副本组队。上轮审查没有检索已归档的相邻主题官方全文，导致把这条玩家真正需要的确定信息遗漏。此遗漏不是必须保留的不确定事项。

## 基础玩法事实矩阵

| 玩家问题 | 核验结果 | 可用正文边界 | 依据 |
| --- | --- | --- | --- |
| 两阵营是否各有全部 8 职业？ | Global 官方 about API 和角色信息 classes API 都提供同一套 8 职业名单；about 将阵营和职业分开介绍。已读官方材料没有逐字说明每个阵营都能选全部 8 个。多个社区页面主张共享名单，但经读其引用，常以“官方列出同一名单且没写限制”推出结论。 | “Global 的职业名单为 8 个；职业与阵营分别选择”有依据。若要明确写“两阵营都可选全部 8 个”，补一份实际两阵营选择画面或官方明确说明最稳妥；不要把未列限制单独当成完整限制不存在的证明。 | about-en-source.json 的 classes/factions；官方 Global api-global-eu-classes.body。 |
| 是否有阵营专属技能或基础属性？ | 现有官方 Global 素材没有提供两阵营基础角色属性或全技能表的同条件对照，也没有明确声明无种族技能、完全相同属性。搜索官方 Global/KR 域和官方新闻未补到明确声明。 | 不发布“技能和全部属性完全相同”“阵营没有任何强度影响”的绝对结论。不照搬 AION 1 的种族技能。页面可以直接说明已核实的选择维度，而不为没有数据的比较制造强弱榜。 | races/implementation-evidence.md 已明确未抄旧 AION racial skill；about 仅职业身份，未列属性比较。 |
| 跨服副本是否允许跨阵营？ | **允许。** AION 2 Official 的 Global Dungeon Live Gameplay Showcase 在 61:00–61:25 明确讲到 Global launch 的副本可和对立阵营、其它服务器玩家组队，并展示 My Faction Only 选项。 | 可直接补“副本支持跨服、跨阵营组队；只想与同阵营玩家组队时勾选 My Faction Only”。不要扩成跨地区、普通世界共同任务或敌对区域友好。 | 官方视频 https://www.youtube.com/watch?v=S_TjiOh33a4；本地完整自动字幕及 oEmbed 作者核验。 |
| Poeta/Ishalgen 与 Verteron/Altgard 是什么关系？ | about API 的 lore 提及 Poeta 遭 Ishtar 火焰毁坏、Ishalgen 遭 Fafnir 侵袭；elyos/asmodians 的 world 数组则分别介绍 Verteron/Altgard 的多个实际世界地点。这两组在官方页面的职能不同。当前已读 Global 官方文字没有把 Poeta/Ishalgen 明确标作初始教学地图。 | 可准确展示“Elyos 世界地区 Verteron / Asmodian 世界地区 Altgard”，配各自真实场景。不能依据该 lore 把四个名字都称为同一出生地图。若写教学出生地，需要直接任务/开场实机证据并区分教程地图与后续开放世界。 | about-en-source.json：lore、elyos、asmodians；今日重复抓取由 visual-research 保存。 |
| 好友/对手/转服有哪些关键差异？ | 每个 home server 仅一阵营；先选 region、再 faction、再服务器。配对服务器在 Abyss/Spacetime Rifts 提供敌对玩家且会轮换。10 月 14 日开始的转服限定同阵营；初期 EA 角色只能转 EA 服务器。 | 当前正文这些信息可保留。普通世界共同任务选择相同 region/faction/home server，副本组队另述，避免同阵营条件误扩到所有组队。 | Global server-access、matchmaking、transfer 公告。 |

## 已读核心归档

- `research/content/2026-10-03/class-launch-sources/about-en-source.json`：原 URL https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en；fetchedAt `2026-10-03T15:45:41.202279+00:00`，HTTP 200，Global。解码 response 中 jsonData，完整读取 classes、factions、lore、elyos、asmodians、dungeons。
- `research/content/2026-10-03/class-launch-sources/matchmaking-source.json`：https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939；发布日期 2026-09-29。读取独立阵营服务器、对手配对、周期轮换全文。
- `research/content/2026-10-03/class-launch-sources/transfer-source.json`：https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2；发布日期 2026-09-30。公告仅说 cross-server instances；**跨阵营结论来自下面官方视频，而非这句跨服公告。**
- `research/content/2026-10-02/leveling/S_TjiOh33a4-transcript.txt` 与 `S_TjiOh33a4-oembed.json`：视频标题 `[AION 2] Dungeon Live Gameplay Showcase`，作者 `AION 2 Official`，author_url `https://www.youtube.com/@AION2Official`。61:00–61:25 为本次关键机制段；自动字幕把 spoken “for dungeons”写成“four dungeons”，不据此生成副本数量事实。此段明确说 Global launch。相关清单条件在视频里是 My Faction Only，不是现有页面自己推测的创建限制。
- 发布日期具体证据：`research/discord/aion2_socials.json` 的 message ID `1545478600248266804`，NotifyMe 的官方频道 live 通知直接链接该视频，显示当地时间 `09/05/2026 1:00 AM`；由 Discord snowflake 计算 UTC 为 `2026-09-04T17:00:11.903000+00:00`，对应直播日期 2026-09-04 UTC。这证明官方频道该日正在直播该视频；不是本次重新抓得 YouTube publishDate。完整身份、日期路径、精确秒点及访问失败说明另存 `global-dungeon-party-evidence.json`。
- `research/competitive/2026-10-03/raw/api-global-eu-classes.body`：单一 classList 共 8 项。API 内 Elementalist 的显示文字是 Spiritmaster，不能产生第九职业。
- `research/content/2026-10-03/races/implementation-evidence.md`、`research/content/2026-10-04/player-content-review/world-guides.md`、`review.md` 与 races 编辑前备份。前一份日志明确未建立跨阵营合作；后一次使用原证据集合，没有进行此玩家问题的增量证据检索。
- 今日官方世界 API 和图片已由 service_guides 保存于 `research/content/2026-10-04/races-player-depth/visual-research/`。两阵营各 5 个场景标题与描述，可让玩家实际比较世界氛围。

## 官方 web 补查记录

检索时间 2026-10-04。第一组官方 Global 域的 faction/classes/skills/dungeons 组合无搜索结果。第二组使用韩文和 NC 新闻域；以下有用结果只适用于对应范围：

- https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%9B%90%EC%A0%95 ：官方 KR 远征指南。搜索索引完整显示两阵营可同一 party、房间“全体公开 / 同族公开”；同文档含最大 5 人且更新时间 2026-09-23，为当前 KR 内容，不能直接当 Global launch 的规则。实际 web open 返回 JS shell。该线索已共享 world_guides；随后本地官方 Global 字幕提供了独立 Global 证据。
- https://about.ncsoft.com/news/article/aion2_update_250530_2 ：2025-05-30 官方开发阶段新闻，完整打开。确认两阵营从各自独立区域开始、8 职业、独立阵营服务器的设计，但没有给 Global 教程区域名或无种族技能的明确声明；其中当时 4/8 人副本和当前 KR 5/10 人不能混用。
- https://www.youtube.com/watch?v=S_TjiOh33a4 ：今日 web open 被 throttled；保留失败，采用原已归档完整字幕和官方作者 oEmbed，不报告重新在线播放成功。
- 广泛英语搜索返回多个第三方 faction 指南，存在“同属性”“出生区未知”“同服可建两阵营”等互不一致断言；未将其作为新增确定机制依据。

## 前一轮漏掉的步骤与 5 条可执行修正规则

1. **先建立玩家问题清单，再做措辞删除。** 上轮确认了没有研究口吻，却没有逐项验收“哪些相同、哪些不同、如何和朋友玩”。每个选择类主题先列职业可选范围、实际外观/世界、基础能力、队伍兼容、对手与可逆性 6 个问题；标明已回答、待补证、无需写。发布结论必须针对具体缺口，不能用语言整洁和没有高风险数值代替内容完整。
2. **逐个对比维度填写两边的具体值。** Useful decision 两行没有新增信息；Class 是职业概念而非阵营对比。将表格改成 `Aspect / Elyos / Asmodians`，每行只比较同一维度：世界地区、任务/故事、共享职业名单（补证后）、副本组队、PvP 阵营。没有值的“喜欢它就选它”整列删除；图片使用真实对应场景，让“世界偏好”有具体对象。
3. **逐条检查操作项是否包含对象、通过标准和失败分支。** 上轮“预览世界”“选喜欢的责任”“读限制”没有通过此检查。保留能执行的完整 region/faction/server 字符串、客户端 creation 是否开放、受阻时全组换同阵营备用服务器；外观项要指出当前可看到的具体预览/截图，角色责任链接去职业页；没有已知检查对象的项目删除，不凑五步。
4. **对缺失答案做相邻官方全文检索，并分清正面与负面证明。** 上轮只复核 races 的 3 条 sources，未查 leveling 归档官方直播 61 分钟的组队回答。已归档的官方全文要按问题检索并读上下文，再记录 region、版本和字幕时间；“没有写差异”不能升级为“无任何差异”，“跨服”不能自行升级为“跨阵营”，“KR 已有”不能升级为“Global 已有”。这次跨阵营已找到 Global 正面证据，应补确定答案。
5. **做实际决策任务验收，结构测试只检查结构。** 上轮正文字符数、H2、四语锚点和响应式通过，却没有验证玩家能在第一页选阵营或安排朋友组队。人工用“朋友选另一阵营还可一起打副本吗”“Poeta 与 Verteron 为什么同时出现”“选阵营会漏掉职业吗”逐问阅读；答案须指出机制与适用范围。快速答案、对比表、FAQ 及四语译文要覆盖同一结论，删除重复服务器协同话术和无对象检查项。

本次没有运行测试，也没有修改页面；结构测试本身无法证明事实齐全。本记录中的未证实项是内部审查缺口，不建议批量变成玩家页的研究免责声明。
