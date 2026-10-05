# 默认 Global 文案审查：世界与工具攻略

审查日期：2026-10-04（Asia/Shanghai）。默认读者为 Global 玩家。采用 copy-editing 的清晰度、信息价值和事实范围检查；本轮只优化地区措辞，没有重新测试游戏机制。

## 覆盖与修改

覆盖 `spacetime-rift`、`character-creation`、`presets`、`map`、`gathering`、`guide`、`races`、`macro-guide`、`notmeter`、`wings` 的英语、日语、西语、德语，共 40 篇、80 个 MDX/JSON 文件。检查正文、标题、SEO 描述、摘要、快速答案、FAQ、目录标题、图注/alt、工具步骤。64 个文件实际修改；裂隙正文/metadata，以及 map/wings metadata 已无需要清理的普通 Global 文案，保持原样。

- **角色创建、预设：** 去掉游戏名、创建说明、转服说明和官方 Style Shop 名称旁重复的 Global。KR/TW 外观链接的排错行仍要求使用当前服务的掲載/发布页面或作者手动滑杆值；步骤改为选择自己地区的条目，未承诺跨服务导入。
- **采集：** 标题、快速答案、正文直接说明序盘采集；魔族晋级段保留阵营标签、Novice 50、Safe Haven 的 Alzirr、Calderon Canyon 的 Splendent Ruby (Bound)，以及与 Radiant Ruby Gemstone 的区别。删除与默认服务采集步骤无关的 KR 45 级反机器人旁枝，未把它改写成默认服务的开放等级。
- **新手攻略：** 安装、账号/服务器、公开入场时间、45 级上限、图像 alt 和检查清单去掉重复 Global。保留 KR/TW 角色与进度不转移、台湾客户端入口、EA 权限和迁移维护时间等真实条件。社群普通名称去掉冗余前缀。
- **阵营：** 移除职业名单、跨阵营/跨服副本、同阵营转服以及摘要/快速答案中的重复 Global。地区、剧情、普通世界共同任务与副本组队的范围保持不变。
- **宏与 NotMeter：** NC 运作政策去掉重复地区前缀。宏图像 alt 继续说明德语界面，不把语言当作地区。NotMeter 网站查询与桌面采集功能保持分开，当前桌面兼容性未确认、NC 未确认批准、OCR 操作条件、付费/报告上传条件仍保留。
- **地图、翅膀：** 去掉普通“在 Global 开放/不可用”表达，保留内容开放、阵营、精确奖励和获得路线等操作条件。英文 wings FAQ 同时纠正 `obtain on your region` 为 `obtain in your region`。

## 留下 Global 的具体理由

四语剩余的可见 Global 均在以下三类；没有普通正文、摘要、快速答案、SEO 或图注的重复版本标签：

| 页面 | 保留内容 | 玩家需要它的原因 |
| --- | --- | --- |
| map | `Global/TW` 地图卡标签；`Global → Verteron` 点击路径 | 这是实际工具界面中的选项文字。删除后玩家无法对照选择正确数据集，也容易误用 TW 后期地区。一般的“on Global at launch”已删除。 |
| guide | 社群表地区列中的 `Global`、`Global / KR / TW` | 同表对照台湾社群和跨地区论坛，地区列有实际选择价值。普通 Discord 名称、入门标题、账号、客户端、上限说明不再重复 Global。根代理明确同意保留此对比列。 |
| notmeter | 网站 `KR / TW / Global` 选择；网站搜索支持范围；aion2t `Global (EU)` 与 `TW` 发行路径 | 这些分别是实际服务选择和软件发行/兼容范围，不能把 TW 工具条件变成默认服务兼容承诺。重复的“current Global compatibility”已简化，兼容性限制本身保留。 |

内部标识 `start-global`、`source-and-global-support`、`macro-global-keybind`、`macro-global-editor`、`style-shop-global-filters` 和 URL 中的 `aion2global` 保持原样：它们属于锚点、组件/asset 标识或真实目的地，不是面向玩家的普通版本提示。

## 删除的 KR 采集背景与保留的来源

被删除的信息为：KR 于 2026-01-28 的反机器人更新，将采集开放条件提高到角色等级 45。它属于韩国服务更新，不能作为默认 Global 玩家开始采集的条件。

- 官方链接：[AION 2 Introduced Strengthened Anti-Bot Measures](https://about.ncsoft.com/en/news/article/aion2_update_260128)
- 发表日期：2026-01-28；地区：KR；版本语境：该次韩国服务反机器人更新。
- 原始来源记录仍在 `src/content/article-data/gathering.json`，未修改。
- 先前地区核对说明仍在 `research/content/2026-10-04/player-content-review/world-guides.md`；本轮编辑前四语全文仍在 `before/src/content/{locale}/gathering.mdx`，未覆盖。
- 没有为语气确定新增具体开放等级，也没有删除魔族晋级路线的阵营限制。

其他文章来源数组、原始资料、关键词文件和真实下载/地图/支持链接均未修改。新手页的台湾入口、预设页 KR/TW 链接排错、NotMeter TW 重点版本和工具条件继续明确保留，因此去掉默认标签不改变原有证据地区。

## 检查结果

逐语查看修改后的句子，并比较根代理本轮备份：全部 80 文件可用 UTF-8 读取；40 个 JSON 可解析；目录 ID 与 MDX 标题对应。链接 URL、锚点、Guide 组件顺序/props/ID、JSON 来源字段和标识与备份一致。没有新增数值；唯一移除的数值是四语 KR 旁枝中的 45。未改 `article-data`、共享组件、关键词或原始素材。

剩余 Global 文案已逐项归类为上表三类。本组检查通过；全站内容测试、生产构建和共享 UI 检查由根代理统一执行。
