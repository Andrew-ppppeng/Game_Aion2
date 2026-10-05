# 物品数量与 JS 预算复核

核验时间：2026-10-04，Global EU 与 TW；游戏版本未由响应返回。

## 当前实现范围

`scripts/collect-aion2-data.py` 的 ITEM_IDS 是 22 个固定样本。它只刷新指定物品，没有全量目录发现逻辑。`src/content/game-data/items.json` 和公开目录复用了这些样本。22 不是官方物品数量上限。

本次小量 GET 核验另一个合法且不在样本名单中的 Global ID 110160001，官方接口成功返回 Worn Greatsword。原始响应、精确 URL、时间、地区和哈希见同目录 global-outside-samples.body / .meta.json。

TW 官方词典本次 page=1、size=5 返回 total=11225、limit=10000。仅取第一页五件，未下载完整目录；不能宣称已采集 11225 件，也不能把 TW 数值当 Global 数值。原始响应见 tw-dictionary.body / .meta.json。后续需核验官方支持的目录筛选与分页语义，及候选 ID 在 Global 的实际覆盖率。不得猜测连续 ID、绕过分页限制或跨地区补数值。

## 竞品自述（不是官方覆盖率证据）

- https://aion2.app/db ：2026-10-04 页面列出 Items 9450、Skills 483、Monsters 7545、Dungeons 109、Quests 1314 等；页面标记 Game client 18.09.2026，同时页脚称官方 NCSOFT API 来源。数据渠道表述混合，不能据此断言全部数据由 Global 物品详情接口提供。地区未在该目录页明确。
- https://aion2hub.com/database ：同日页面列出 Global 9450、Korea/Taiwan 3689、All regions 13139。属于该站自己的数量和地区标记，未逐项独立核验，不能把所有竞品的数千物品都解释为仅 KR/TW。
- https://www.aion2kina.com/en/database/ ：同日页面列出 10910，称使用 NC 发布的 Taiwan、Korea 和 en-US 数据，页面资料日期 July 19, 2026。多来源目录不证明数值适用于所有地区。

## GA 大小目标

本项目测试默认 JS 目标 220 KiB（225280 bytes），不是 Google 限制。既有报告站内脚本 200704 bytes、GA 178546 bytes，合计 379250 bytes。GA 开启时 LCP 1080ms、CLS 0、脚本交互 112ms，其对应目标通过，只有总脚本大小目标未通过。这些是有限本地实验数据，不能声称网站被 SEO 处罚或 GA 出错，也不能推断真实用户 INP。报告保存在 .qa/performance-platform-with-ga.json / .qa/performance-platform-no-analytics.json。
