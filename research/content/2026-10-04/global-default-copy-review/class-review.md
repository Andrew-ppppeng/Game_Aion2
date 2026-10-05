# 职业与战斗组：默认服区文案审查

日期：2026-10-04。本轮以站点默认服务为 Global；普通机制、操作步骤和职业介绍不反复附加 Global。审查只处理已存在的内容，没有新增关键词、改动原始素材或改变技能/数值。

## 覆盖与改动

逐项检查 `src/content/{en,ja,es,de}/` 下 tier-list、classes、builds、chanter、cleric-build、gladiator、ranger、spiritmaster、pvp、leveling 的 MDX 和 locale JSON，共 40 篇、80 文件。检查范围包括标题、SEO 描述、快速答案、目录、正文、FAQ、表格、图注与 alt。

25 个文件实际变更：

- tier-list：四语 MDX。
- classes：四语 MDX 和 JSON。
- builds：四语 MDX 和 JSON。
- leveling：四语 MDX。
- gladiator：英文 MDX；其它语言对应句原已不重复 Global。

其余 55 文件检查后没有需要删除的普通服区限定，或仅含有必要的对比；保留原内容。

主要删除或改写：

- 职业总数、职业图标解释和对应 SEO/summary/TOC 中的普通 Global 限定。
- builds 的普通职业行、计算机标题、工具可见名称、SEO/summary/quickAnswer 中的重复 Global；工具名称显示为 Build Planner，URL 和操作步骤保持。
- `/global-changes` 操作链接显示为地区间成长差异，URL 保持原样。
- 升级路线里的 On Global、表头“如何用于 Global”、普通主线目标和 Exploration 节点中的默认服区称呼。
- tier-list 的方法段改用 launch column / 对应译文；首张地区对比表仍明确区分两套评级。
- Gladiator 普通复查句采用 balance update，不再枚举 regional or Global。
- Brawler 可用范围改成 KR/TW Chapter 1 且不在启动职业名单中，不再讨论尚未宣布的日期。

## 保留地区表述的理由

| 位置 | 保留的内容 | 理由 |
| --- | --- | --- |
| tier-list 的地区评级表、对应 metadata | Global launch 与 KR/TW PvE | 两套评级属于不同服务/玩法范围，不能合并为同一服区的统一强度结论。八职业两列评级全部保持原值。 |
| classes 的 Brawler 对比段 | KR/TW Chapter 1、Global launch | 明确区分九职业区域内容与默认八职业名单，影响玩家职业选择；没有扩大为默认服务可用。 |
| builds 的目录例子 | Global Launch Scale Test 与 KR/TW、对应装备/数值/评分不可直接套用 | 目录确实混有两类例子，测试客户端与区域服并不是当前角色构筑的同一依据，保留能防止错误复制。 |
| ranger 技能范围 | TW starter、Global/TW Daevanion 布局与数值差异 | 区域服技能联动与 board 不可默认视为本服已确认配置。 |
| leveling 上限对比及 metadata | Global launch 45、KR/TW Chapter 1 50 | 数字直接不同，保留地区比较避免玩家误以为默认上限已经 50。TW 路线 checkpoint 标签保持。 |
| 各职业攻略的技能例子 | TW / KR/TW starter 标签 | 用户明确要求保留参考构筑真实范围，不能因删默认标签将这些技能和数值变为默认服务事实。 |

builds 中 Chanter 和 Cleric 的具体技能例子此前未短标地区，现依根代理授权在对应段落与表行补上 TW starter / 对应译文。现有 Chanter、Cleric 独立技能页已采用同样 TW 范围，未改技能、触发、数值或来源。Assassin 的例子保持一般资源生成/消耗说明，没有把它改为 TW 技能例子。没有新增泛泛版本免责声明。

## 保持项与注意事项

- `article-data`、sources、keyword、原始研究素材和资产数据没有由本代理编辑。
- Markdown 链接 URL、H2 IDs（包括 `global-leveling`）、组件 IDs、组件顺序、GuideNext 与图片资产 IDs 全部保持。
- 服区对比仍可在 title/description/summary/quickAnswer 中出现；这些是在区分确实不同的评级/上限，不是给普通机制重复加默认标签。
- 当前工作区有其它会话改动。本轮依据指定 `before/src/content/` 快照定向比对，没有用 Git 基线覆盖文件。

## 验证

针对全部 40 篇、80 文件执行只读内联 Python 检查，全部通过：H2 与 TOC 对应、四语锚点/链接/表格行列/组件顺序一致；URL、资产 IDs、inlineNext 与本轮 before 相同；正文长度达标；现有职业 TW/KR-TW 技能范围保持；JSON 有效；没有 U+FFFD、三问号或英文夹杂乱码问号。

公开文字中的 Global/グローバル 出现次数从 153 降为 64，统计排除了 URL 和稳定 ID。剩余均已按上表人工审查。本轮没有运行全站测试；根代理统一检查与构建。
