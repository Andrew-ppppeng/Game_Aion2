# 玩家视角内容审查记录

审查日期：2026-10-04。状态：本地修改与验收完成，未提交、未部署。

## 覆盖范围

全部 28 个攻略主题，en、ja、es、de 四语共 112 篇；同步审查正文、SEO 描述、快速答案、目录标题、图注、FAQ 和共享展示组件。首页、兑换码、活动时间、装备与角色工具的公共说明一并调整。

| 审查组 | 主题 |
| --- | --- |
| 职业与战斗 | tier-list、classes、builds、chanter、cleric-build、gladiator、ranger、spiritmaster、pvp、leveling |
| 世界与角色 | spacetime-rift、character-creation、presets、map、gathering、guide、races、macro-guide、notmeter |
| 服务与活动 | code、download、maintenance、monetization、player-count、server、server-transfer、steam、twitch-drops |

## 采用的编辑原则

- 玩家正文直接讲机制、条件、操作和结果。
- 删除来源比较、核实过程、演示举证、图片不证明什么、一般性的待审查提醒。
- 所有攻略不再渲染 Sources、来源目录项、来源版本详情或 Image source；图注只描述图片内容。
- 删除无实用价值的不确定信息，不把未核实细节改成确定事实。
- 保留会影响玩家选择的地区、账号、兼容性、付费、奖励期限和兑换条件，采用短标签或直接说明。
- 外部下载入口、官方操作入口和玩家可用工具链接继续保留。

## 重点结果

- tier-list 删除作者之间分歧的审慎论述；表头采用 Global launch / KR/TW PvE，保留原有八职业评级与玩法范围。图片说明仅描述职业美术。
- spacetime-rift 删除 Global 固定时间未核实、图片不证明入口位置、页面不编造坐标等说明；保留进入、阵营、PvP 状态、守卫和复活目的地的玩家操作。
- character-creation 删除网站英文展示日期及对初始编辑器、创建前导入的举证说明；保留角色创建、外观分享与导入的实际步骤。
- Ranger、Chanter、Cleric 的区域服技能例子采用简短 TW 标签；PvP 兑换说明按实际费用和目标奖励表达。
- 玩家数保留 Steam 的统计范围和一次数据时刻；未扩展为全部平台人数。未经确认的平台支持列表与无依据的转服细节已删除。
- 独立事实复核覆盖 28 篇英语正文；最终未发现需进一步修改的高风险数字、日期、账号或付费限制问题。
- 视觉复核发现 tier-list 普通两列表误用评级格式，已限定评级样式的适用表格；四语桌面和手机表高恢复 270–413px，正常换行。

## 来源与原始资料

- 修改前的当前工作区内容保存在 before/，没有用 Git 基线覆盖用户已有修改。
- 28 个 src/content/article-data/*.json 的 sources 和 keyword 字段与备份逐项一致；更新的仅为本轮文章更新时间与修订标识。
- src/content/guide-assets.json 与备份一致，图片来源信息仍保留。
- 原始资料继续保存在 discord/、research/，没有覆盖或删除。
- 分组记录：[职业与战斗](class-guides.md)、[世界与角色](world-guides.md)、[服务与活动](service-guides.md)、[公共展示层](shared-ui.md)。
- 线上三个示例 URL 在本次 web 读取中不可访问；本轮依据本地对应文章与既有内部资料完成审查。

## 验收结果

- npm run test:content：112 篇本地化攻略、30 个资产、编码、锚点、目录、链接与内容结构通过。
- npm run check：ESLint 与 TypeScript 通过。
- npm run build：最终独立生产目录 .qa/player-content-final，136 个静态页面生成成功。
- npm run test:smoke：最终构建 132 项页面检查、112 篇攻略、120 项站点地图、语言链接、404、robots 与资产通过。
- npm run test:browser：最终构建全部 112 篇攻略的快速答案、图注、来源隐藏、响应式页面及互动通过；新增四语桌面/手机正文表的列宽、换行与高度回归检查。
- npm run test:tools：上一轮相同工具实现的四语装备/角色、收藏、比较、时区、日历与本地保存检查通过；后续改动仅涉及评级表样式、四语表头及尾随空格。
- 三个用户示例页面另做桌面与手机视觉复核；四语 tier-list 第二表修复后复核通过。
- git diff --check：考虑 Windows CRLF 后通过。
- build-inputs.json 保存 297 项构建输入 SHA-256，最终构建后逐项验证一致。

最终预览：http://127.0.0.1:3109。截图和几何记录在 .qa/player-content-review/，包括 tier-list-1440-content-table-fixed.png、tier-list-390-content-table-fixed.png 和 final-three-results.json。
