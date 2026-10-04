# AION 2 SEO 内容更新实施记录

**最新状态（2026-10-04）：** 新增 Wings、Database、Global changes，更新 11 个既有主题的四语内容，总计 31 个主题、124 篇文章；词库 87 项。最新改动、缺口与验收见 [10 月 4 日实施记录](SEO-CONTENT-UPDATE-2026-10-04.md)。以下为上一批的历史验收，不代表本轮已经部署。

本轮已在本地项目实现 **8 个新主题、32 篇四语文章**，发布内容从 20 个主题扩展到 **28 个主题、112 篇文章**。英语、日语、西语、德语均包含正文、目录、来源、元数据和导航。

执行跨度：2026-10-03 至 2026-10-04（北京时间）。本记录不声称已经部署或获得新增搜索流量。

## 已完成

- 新页：`/gladiator`、`/ranger`、`/spiritmaster`、`/races`、`/server-transfer`、`/notmeter`、`/macro-guide`、`/player-count`。
- 职业页补八职业官方图标、英语/本地名称对照、原始 90×94 图片放大；已完成职业页链接可直接进入对应攻略。
- Steam 页补 Global/日本/台湾服务区别与平台问题。台湾旧预约入口改为当前官方下载页，并补充地区来源。
- Chanter、地图、服务器状态、下载、免费模式/Founder’s Pack、裂隙页的标题和说明覆盖对应搜索意图；既有目录与事实边界保留。
- 新旧页内链接通；入门指南新增 Discord、Twitch、Reddit、Bahamut 资源表，标明官方/社区及地区。Bahamut 直接访问 403 的限制有记录。
- 裂隙页连接现有代码、Drops 和维护窗口。没有把相互冲突的 KR/TW 周期合成 Global 倒计时。
- 游戏内宏页接入两张原始 Global 德语菜单截图，具备放大、来源和作者说明。截图与研究原图哈希一致。
- 新建 `content-topics.json` 为当前发布清单；登记、路由、导航、推荐路径、sitemap、四语计数及内容检查使用当前内容，历史 `keywords-priority-20.json` 保留。

## 验证结果

| 检查 | 结果 |
| --- | --- |
| `npm run check` | ESLint、TypeScript 通过 |
| `npm run test:content` | 112 篇四语文章、30 个有来源素材通过；目录、表格、链接、组件与元数据一致 |
| `npm run build` | 生产构建通过，生成 135 个静态页面（包括攻略以外页面） |
| 新构建 smoke | 132 项页面检查、112 篇攻略、120 个 sitemap 条目通过 |
| 新构建 browser | 112 篇攻略检查通过；四语切换、手机布局、原图/键盘/焦点、筛选、清单、代码和计时状态正常；无运行时、控制台或本地资源错误 |
| 计时专项 | 维护 Upcoming→Ongoing→Ended 边界、结束后移除倒计时、UTC/JST 与 ICS 一致；四语待确认 Drops 和未知裂隙不显示虚构倒计时、开门时刻或日历按钮 |
| 视觉读图 | 390/1440 视口的职业图标表与宏菜单截图正常；手机表格横向滑动提示可见 |
| 原始资料保护 | 123 个受保护文件哈希一致；两份原关键词文件未改动 |
| `git diff --check` | 通过 |

验收针对新的 production 服务 **http://127.0.0.1:3027**，没有使用或停止旧 3000 服务。该本地构建使用默认 canonical `http://localhost:3000`；部署时沿用项目的真实 `NEXT_PUBLIC_SITE_URL` 配置。

局部截图保存在 `.qa/seo-classes-icons-{390,1440}.png` 和 `.qa/seo-macro-menu-{390,1440}.png`。研究和 QA 文件按现有 `.gitignore` 留在本地；源码、公开素材、发布清单及本文可随项目版本管理。

## 有证据限制的内容

职业构筑是标明地区的起步参考，不宣称实测 Global 最优配点。转服页只承接已公告的准备规则；实际转服菜单与未公布限制需要开放后复核。Notmeter 安装取自维护者资料，当前 Global 抓取兼容性和 NC 授权未被本轮验证。玩家人数是带读页时间的 SteamDB 快照，不是本站实时数据或 Global 全渠道总人数。

Arcana、职业专用宏、删角色、重做外观、Odyle 完整资源机制、Dimensional Invasion、两阵营木桩位置、Global 裂隙周期与 roadmap 仍在来源队列。没有把缺少完整答案的研究草稿加入发布清单。具体解锁条件保存在追加的研究日志。

GSC 正式属性 `aion2wiki.space` 的近 28 天报告仍显示 Processing data，点击/曝光/CTR/位置均为未知，未填零。以实际上线日期为 D0，按 D+14/30/60/90 复查流量与查询覆盖，不能从本轮本地验收推断 SEO 已增长。

后续顺序见 [内容路线图](SEO-CONTENT-ROADMAP.md)。完整原词与涨词映射见 `research/keywords/2026-10-03/implementation/keyword-coverage.json` 和 `coverage.md`；事实缺口见 `research/content/2026-10-03/seo-expansion-implementation/global-gates-reviewed.md`。各类来源保留国家、时间窗、地区/版本和实际核验状态，旧观察的增幅与本轮实读分开。
