# 平台首版验收记录

日期：2026-10-04。本次为本地生产构建验收，未部署生产站。

| 检查 | 结果 |
| --- | --- |
| `npm run check` | ESLint 与 TypeScript 通过 |
| `npm run build` | 生产构建通过 |
| `npm run test:content` | 124 篇四语言攻略、32 个素材及关键词/锚点/来源记录通过 |
| `npm run test:data` | 34 项测试通过，包括 Unicode 分享、无效导入、地区隔离、存储上限和真实强化/节点响应 |
| `npm run test:platform` | 四语言手机/桌面、收藏/目标/计划/清单、完整备份导入与旧预算恢复、分享隐私、失效请求、节点/快照、存储拒绝及 SEO 通过 |
| `npm run test:tools` | 原有装备、角色、时区、日历、预算和 320/390/1440px 流程通过 |
| `npm run test:navigation` | 四语言导航、Tab/Escape/焦点、312px 布局、语言查询参数和锚点保留通过 |
| `npm run test:browser` | 124 篇攻略交互、图片/目录/过滤/清单/缩放/语言/优惠码通过，无运行时错误 |
| `node --env-file=.env.local scripts/smoke.mjs` | 144 页检查、236 条 sitemap、多语言 canonical/alternate、404、政策和素材通过 |
| 本地装备 API → 官方接口 | EU、110730048、+1：200，正确 ID/强化等级，fresh，error=null |
| 本地成长节点 API → 官方接口 | EU、serverId=1306、boardId=11：200，225 节点，fresh，error=null |

浏览器回归用真实归档响应。实际官方请求仅作有限手动核验，不把实时上游作为批量 UI 测试依赖。截图与机器结果保存在 `.qa/platform/`；原始装备 +1 响应在 `research/api/2026-10-04/platform-163207-466/`。

## 性能结果与保留的问题

这里的 JS 预算是本项目测试脚本设定的大小目标（220 KiB），不是 Google 的限制、GA 错误或 SEO 处罚条件。应分别报告脚本大小与实际加载/交互测量结果，不能把大小目标未通过表述为网站性能整体未通过。

390×844、冷缓存、150ms 延迟、200KB/s、CPU 4 倍降速、每个场景三次取中位数：

- 开启现有 GA：LCP 1080ms，CLS 0，脚本交互 112ms。站内 JS 200,704 bytes，GA JS 178,546 bytes，总 JS 379,250 bytes，超过原 225,280-byte 总脚本预算。LCP/CLS/总资源/交互预算通过，总脚本预算未通过。
- 通过站点已有隐私设置停用统计后的对照：LCP 1056ms，CLS 0，脚本交互 104ms，总 JS 200,704 bytes，五项预算通过。
- 保留 GA 现有配置；没有放宽默认预算或把对照结果报告为开启 GA 时通过。性能脚本补充站内/第三方脚本分解和明确的统计开关测试条件，便于后续优化。
- 对应机器报告：`.qa/performance-platform-with-ga.json` 与 `.qa/performance-platform-no-analytics.json`。这两份抽样在首版核心实现完成后、最终少量字段和统计路由补齐前生成；不代表生产真实用户 INP。

## 发布范围

本次接入仅完成已收录装备、角色与成长节点等模块。22 件装备来自采集脚本的固定样本名单，并非官方接口的物品数量上限；未完成全量目录发现和采集，因此不能把这次交付称为完整数据库。Global 全量目录、交互世界地图、技能数值、配方、掉落和行情仍按 [平台路线图](AION2-PLATFORM-ROADMAP.md) 的数据条件推进。客户端解析保持 TODO，未执行。原有用户改动、关键词与 research 原始文件未覆盖。
