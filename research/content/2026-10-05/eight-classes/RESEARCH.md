# 八职业与 Builds 素材和内容验收

收集日期：2026-10-05。默认内容服务 Global；地区比较单独限定。原始素材未删除或覆盖。

## 审查前的玩家问题

1. 我适合哪种操作方式？近战、盾、防御、远程、施法、召唤、主要治疗还是混合支援？
2. 每个职业到底有哪些技能，几级可学？哪些是常用攻击，哪些需要暴击、控制、闪避、资源或 Stagger？
3. 哪个普通攻击恢复 MP？技能为何亮不起来、无法重置或伤害下降？
4. 低进度先投什么？技能等级与角色等级有什么区别？特化解锁后是否必须选择？
5. Stigma 怎样按输出、坦克、治疗、单刷和对战交换？学会是否等于有装备槽？
6. 如何手动起手、填充等待并应对移动？哪些按钮必须独立操作？
7. 命中、暴击、资源、速度、生存和 Daevanion 应怎样解决具体问题？
8. 同队职业哪些增益重叠？复制旧版本或高进度配置会在哪些条件上失败？
9. Builds 能否直接找到全部八职业，预算点数并保存、比较实际配置？

## 原始来源和范围

- 官网：<https://aion2.plaync.com/en-us/about/index>；实际接口 `https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en`；`official-about.json`。Global 的八职业名称、定位与武器介绍。不能据此推导全套技能与最佳配点。
- Global 客户端技能资料：<https://aion2.gaming.tools/skills>、<https://aion2.gaming.tools/build-planner>。站点标记客户端 1.0.21.0、更新 2026-09-30。公开 CDN `https://cdn-hosted.gaming.tools/aion2/data/en/build-planner.d.json?version=1791128411844`，ja/es/de 同路径。已保存四语解码后的 `planner-data-{locale}.json`、HTML、devalue 脚本、技能索引及单技能详情。
- 单技能详情：`https://aion2.gaming.tools/skills/{id}`，公开数据 `https://cdn-hosted.gaming.tools/aion2/data/en/skills/{id}.d.json?version=1791128411844`。`client-records/{id}.json` 共 280 个完整响应；`client-record-errors.json` 为零失败。每职业 12 个主动、10 个被动、13 个 Stigma。记录包含学习条件、成本、升级效果、使用条件、特化、范围等字段。**数据是工具提供的客户端抽取，未自行拆包、未进行游戏内实测。**
- 独立客户端抽取对照：<https://metabot.gg/en/aion-2/skills>；标记 build 0.0.4387.0。209 页成功，71 页失败，失败保留在 `client-skill-failures.json`；不将此批误报为 280 页成功。`client-skill-records.json` 与 `raw-skills/` 保存全文及 gzip 原始 HTML。仅用名称、实际说明和特化交叉检查；不采用站点自动生成的泛用 FAQ、排行榜使用率或错误百分比渲染。
- 官网优先用于身份；YouTube 用全文字幕及时间点说明手动操作；技能细节采用 Global 客户端资料交叉对照。没有复制 KR/TW 的数值、最终 Daevanion 路线、装备毕业标准或赛季排名。
- 页面 <https://aion2wiki.space/builds> 的 web 抓取不可达；本地同路由 MDX 是实际修改对象。Build Planner HTML 已用网络请求归档；web 工具因 >4MB 无法打开该页。公开攻略保留实际工具入口，不展示抓取过程。

## 视频字幕时间点

完整字幕已读。下列时间点用于定位，不在公开页面展示，自动字幕名称有误时以客户端名称校正。

| 职业 | 完整视频 | 重点时间点 | 区域与限制 |
| --- | --- | --- | --- |
| Templar | <https://www.youtube.com/watch?v=f3gxUdec82U>，37:52；另有 RsAWWG741MA | 03:05–03:51 Warding Strike 与 Judgment 的短追击窗口；后续主动、被动、Stigma、板、控制均保留全文 | Mixed；教学实际补丁不明确，只采用 Global 资料一致的交互 |
| Assassin | <https://www.youtube.com/watch?v=DNfd1lZtQkI>，34:08；另有 YPqMG7Z5TD4 | 07:18、11:29 标记资源；28:14、32:04 Illusive Clone 与连招 | Mixed；不复制玩家暴击阈值或宏的固定间隔 |
| Sorcerer | <https://www.youtube.com/watch?v=C6-9zLLRiDE>，35:52；另有 s-pYR_fmMDk | 02:49 Firestorm → Hellfire；05:58–06:05 MP 与成本选择 | Mixed；技能名由客户端校正 |
| Spiritmaster | <https://www.youtube.com/watch?v=v9MYphrcvic>，42:34 | 04:36–04:40、06:20–06:23 Water Spirit 与资源；后续精灵与融合保留全文 | Mixed；不把一种召唤顺序写成 Fusion 的必要条件 |
| Gladiator | <https://www.youtube.com/watch?v=WlxLOTs62dM>，32:06 | 12:22 Blood Absorption；主动与 Stigma 全文用于检查输出、防御交换 | Mixed；恢复条件以客户端说明为准 |
| Ranger | <https://www.youtube.com/watch?v=UOuiJT9E1xA>，28:44 | 02:47–03:18 Snipe 与 Deadshot 冷却关系 | Mixed；不照搬 TW 板路径 |
| Cleric | <https://www.youtube.com/watch?v=A3pZDSt4ceU>，33:58 | 09:59–11:35 Condemnation；12:10 Radiant Recovery | Mixed；基础解除与技能数值按客户端纠错 |
| Chanter | <https://www.youtube.com/watch?v=bdJOwmhdpQ8>，13:56；主教学 `research/youtube/EsxGbxt0k-4.txt` | 00:36–00:51 Dark Crush 的远程触发与再使用；原有 EsxGbxt0k-4 完整字幕仍保留 | Mixed；不复制已经达到后期特化的连续输入到低等级 |

## 关键纠错和冲突

- Radiant Recovery 基础是 40m 内本人及队友治疗并解除 1 个减益，不需要先选解除特化；rank 8 的解除、额外使用、短冷却是选择项。Recuperation 基础同样有 1 个解除。
- Healing Light 基础选择范围内 HP 最低的队员，不当成自由指定单人的技能。
- Condemnation 需要目标 Chain of Torment，暴击重置选项在 12；不能把升级当成已选择或把暴击重置当成必然发生。
- Hellfire 移动施法在 rank 8；Punishment 的移动特化在 rank 12。
- Drill Dart 必须先发生暴击，其自身暴击才给予说明中的 MP 恢复。Suppressing Arrow 需要 Precision；Burst Arrow 需要 Slow/Root。
- Ankle Slice 与 Heat Wave Blow 条件字段写 Parry，说明出现 Block。公开说明用 Parry，保留通过对应接近技**已选特化**的触发。Debilitating Smash 通过 Block 或 Shield Smite 的触发特化；Whirlwind Slice 通过 Evasion 或 Ambush 特化。
- Elemental Fusion 普通条件为 4 次精灵技能得到的元素层数，非强制 4 个不同属性；Four Elements 状态下不可继续积累，使用 Fusion 后消费。Ancient Spirit 每次使用精灵技能直接给予 Four Elements。
- Dimensional Control 条件写召唤精灵，描述写每次精灵使用技能短暂触发。公开用“召唤或精灵技能后出现的短窗口”，不编造精确触发计时。
- Water Spirit 默认命中恢复 MP，Wind 默认恢复本人 HP；不用特化才能实现这个基础功能的旧说法已删除。
- Blood Absorption 触发是攻击命中与低 HP 紧急恢复，没有正面条件；Experienced Counterstrike 才含正面加成。
- Undefeated Mantra 与 Light of Protection 的伤害增益不叠加；高级别优先，同级 Mantra。Fury 与 Experienced Counterstrike 的队伍伤害增益不叠加。Earth's Promise 与 Chain of Torment 的耐性降低不同时应用。
- 工具的通用 `specializationSlots` 第三项显示 20，而各具体技能 `requiredParentLevel` 显示 16。独立客户端抽取也列具体第三项 16，视频说明后期无冷却循环。公开只描述**具体特化本身的等级条件并要求已解锁、已选择**，不将通用槽字段当成所有技能的统一门槛；完整最终槽解锁规则不作为已核实结论。
- MetaBot 的自动文本有 `70,70% HP`、`22,400% Attack` 等格式错误。没有采用这些百分比。客户端 damage 模板有未完成占位符，公开不输出基础伤害、理论 DPS、模拟结果或声称最高等级 40 可直接购买。
- 当前页面是可操作的起步与机制指南。尚未建立“最优毕业加点、装备毕业阈值、赛季 PvP 强度、实测 DPS 排名”，不编造固定最强配装。

## 逐职业覆盖与产物

八个职业均提供：定位和选择取舍、全部 35 个名称及角色等级条件、12 个主动技能用途与触发、主要被动、按目的选择的 Stigma、手动起手、资源与装备/Daevanion、条件失败、solo/party/PvP 调整。en/ja/es/de 同步，技能名称来自对应客户端语言，非英语页保留英文技能别名。

新增 `/templar`、`/assassin`、`/sorcerer`、`/cleric`；强化 `/gladiator`、`/ranger`、`/spiritmaster`、`/chanter`。`/cleric-build` 保留独立恢复、配装及交换任务，与 `/cleric` 的完整机制介绍互链。

`/builds`：8 个职业及具体核心技能；角色等级和技能等级区别；特化、Stigma、被动、Daevanion、Arcana 的分工；8 个手动连招与限制；真实 planner 操作和登录保存条件；按失败类型调整；保留 7 个原有锚点。

`/classes`：图标与双语名称并入职业卡，8 个入口全部进入真实详情。旧 `class-icons` 锚点保留为 span，重复章节与独立图标表删除。比较表也链接八职业。

用户明确要求补齐职业页面，因此扩展 `content-topics.json` 的公开页面注册。`keywords.json`、`keywords-priority-20.json` 原词库不扩写、不变更。

## 验收记录

- 静态内容检查：140 个四语内页通过；280 个唯一技能，分组完整、96 个主动说明四语覆盖、8 个真实页面目标、重复图标章节删除、锚点与翻译结构通过。
- 首次 TypeScript 检查发现 `.next/types/validator.ts` 引用旧工作区已不存在的路由；`next typegen` 重建后 typecheck 通过。未修改用户已有 tsconfig。
- Next.js production build 已通过，最终浏览器检查与截图见同目录最终验收记录。
