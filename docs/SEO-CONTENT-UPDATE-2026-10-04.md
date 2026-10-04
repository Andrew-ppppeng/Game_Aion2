# 2026-10-04 内页更新实施记录

本轮实现 **3 个新主题、11 个既有主题更新**，英语、日语、西语、德语同步，共新增 12 篇、更新 44 篇攻略。登记后的内容总量为 **31 个主题、124 篇四语文章**。本文记录本地实现与验收，线上部署状态另行确认。

## 内容变化

| 批次 | 主题 | 更新方向 |
| --- | --- | --- |
| 第一批 | Classes、Leveling、Download、Notmeter | 职业技能与 PvE/PvP 入口；等级上限与满级后步骤；PC 配置自查与 TW 安装；DPS 工具方式、费用、账号和地区条件 |
| 第二批 | Map、Gathering、Server、Steam、Guide、Monetization、Builds | 资源地图筛选与采集路线；Global 地区和队列；欧洲开放时刻与平台支持；NA/EU/TW 入门；Quna 和礼包条件；实际操作过的 Global 技能计算器 |
| 新页 | `/wings`、`/database`、`/global-changes` | 翼与飞行操作、装备/持有效果及外观；物品、技能、掉落、角色查询入口；Global launch 与 KR/TW Chapter 1 的已确认差异 |

Database 是可用资源与查询操作指南；没有搭建或宣称本站拥有全量游戏数据库。Talent calculator 合并到 `/builds`，没有另建重复的工具薄页。旧锚点、职业图标、区域筛选及有效组件保留；新主题接入四语导航、阅读路径、路由、sitemap 和文章计数。

来源、核验时间、地区、版本、冲突和字幕时间点保存在内部材料；玩家页直接说明步骤和重要条件。尤其保留：Steam 独立游玩无需 PURPLE 绑定、同角色跨启动器才需绑定；KR/TW 进度不转 Global；DPS 工具的 “Global” 显示模式不代表国际服兼容；Founder 外观账号共享仍待 EA 后实施。

## 关键词与 Google 方向

**26 组低 KD 候选**来自原 22 组精选与修正后补选的 Classes、Wings、Database、Specs。Max level 原已在榜。词库由 **63 项增至 87 项**：新增 24 项，Classes 已存在，Specs 同义并入 `aion 2 system requirements`。历史 `keywords-priority-20.json` 保持不变。

Google Computer Use 实读 **16 个搜索种子的联想词、8 个实际结果页**。保留 145 条联想观察，人工筛后 103 条研究线索观察；结果页保留 63 条页面标题观察。联想影响文章方向，没有将每个建议词扩写进词库。

搜索会话为英语 UI、个性化结果、页脚 Hong Kong，不能当作 US 或全球排名。Similarweb 指标是 Worldwide / Google / All traffic / Last 28 days，数据截至 2026-09-30；不是平均月量，同义词体量不相加，联想不编造 KD 或体量。

逐词状态、原词指标和来源见 [本轮覆盖记录](../research/keywords/2026-10-04/implementation/coverage.md)及 `keyword-coverage.json`；对应素材已逐词追加到 `关键词素材.md`，旧原件保留。

## 仍需补证据

本轮 26 组中，**14 组按本轮范围已覆盖，4 组有重要限制，3 组关键答案待证据，5 组暂缓**。这是需求状态，不按“词数减页面数”计算剩余工作。

- 有限制：TW 完整境外访问资格、Global 主机日期、Global Brawler 日期、最低“获胜花费”。页面已有相关步骤或消费边界，但不编造答案。
- 关键答案待证据：职业转换流程与成本、单服容量与实时人数、EU 物理机房城市。
- 暂缓：Private server、Raid 2026、Fishing release、AION 1 地图连接关系、Japan VPN 进入资格。

Google 发现的性别锁、技能/采集/Monolith 上限等仍留在研究线索；没有把角色等级上限套给其他系统。Wings 数值排行和强化成本未发布；版本冲突尚未解决。Database 中的测试客户端和 KR/TW 数据明确标注。

原 63 项的历史缺口继续独立保留；本轮不意味着所有旧需求已完成。[网站拓展方案](AION2-EXPANSION-TODO.md)继续按用户要求暂缓，不包含本轮开发。

## 验收

| 检查 | 最终结果 |
| --- | --- |
| `npm run check` | ESLint、TypeScript 通过 |
| `npm run test:content` | 124 篇四语文章、30 个有来源素材通过；元数据、目录、链接、来源与组件一致 |
| `npm run build` | 生产构建通过，生成 148 个静态页面 |
| `npm run test:smoke` | 144 项页面检查、124 篇文章、132 个 sitemap 条目通过；canonical、hreflang、路由与索引标记正常 |
| `npm run test:browser` | 124 篇文章通过；四语切换、桌面/手机布局、筛选、清单、放大、目录、阅读路径和优惠码状态正常；无运行时错误 |
| 新页视觉检查 | 9 组桌面/手机视图、18 张截图；无页面横向溢出或运行错误，英文表格词正常换行 |
| 原件保护 | 上一批基线的 122 个受保护文件哈希一致；完整词库按批准需求更新，原 63 项及更新前快照保留；素材库原字节前缀保留；历史优先 20 项未改 |
| `git diff --check` | 通过 |

最终验收使用相同最终构建的新 production 进程 **http://127.0.0.1:3032**。本地 canonical 为项目默认 `http://localhost:3000`；正式部署沿用真实站点配置。旧 QA 进程 3031 已关闭。Git 提交与推送按用户后续授权执行，线上部署以托管平台状态为准。

检查中修复了新分类图标登记、TW 安装按钮的四语表达、来源地区标记，以及 Database 角色查询链接的语言前缀。文章表格按完整单词换行，手机端保留横向滑动。

首页布局检查改为等待本地化 H1 和可见操作按钮，保留原功能及溢出断言，避免后台预取影响 `networkidle`。旧 QA 进程随后出现 WebP 优化响应超时；同一构建的新进程恢复正常，桌面/手机全部图片就绪断言和完整浏览器检查通过，没有改动图片加载方式。永久框架根因尚未确定，诊断保留在内部日志。

结果详情见 `research/keywords/2026-10-04/implementation/validation.json`；截图位于 `.qa/keyword-refresh-*.png`。研究和 QA 文件沿用项目 `.gitignore` 留在本地。

## 上线后复查

以实际部署日期为 D0，在 **D+14、D+30** 人工查看 GSC `aion2wiki.space` 的收录、页面/查询/国家曝光、点击、CTR 和位置。优先检查新页收录及已有曝光词与标题是否匹配，再调整内容。未出数据记未知，不填 0；本轮没有创建定时任务，也没有推断新增流量。
