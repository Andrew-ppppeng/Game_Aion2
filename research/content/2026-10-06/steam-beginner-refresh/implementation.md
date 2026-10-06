# 2026-10-06 Steam 新手内容更新

本次执行用户确认的站点修改方案。公开页面服务 Steam AION 2 Global 玩家；KR/TW 专用规则、跨服比较和对应视频不公开。原始 YouTube 资料目录未修改。未执行部署、提交或推送。

## 发布内容

| 路径 | 玩家任务 | 实施范围 |
| --- | --- | --- |
| `/settings` | 调整目标、追击、药水、按键、HUD 和拥挤战斗显示 | 英、日、西、德完整正文、快速答案、目录、流程图、相关阅读及视频 |
| `/gear-progression` | 到 45 后找到下一项装备目标 | 区分等级、装备分数、战斗力；探索、强化预览、腰带/护符输入、镶嵌和物品权限 |
| `/daily-weekly-checklist` | 在短时间内安排有用活动 | Duty、活动入场与奖励领取、界面计数器、一次性奖励、活动期限；没有新增游戏系统或自动重置功能 |
| `/crafting` | 为一个具体配方准备材料并完成首次制作 | 区分采集、装备抽取和 Substance Morph；材料数量、Bound 变体、市场条件与配方阻塞 |
| `/beginner-videos` | 按入门或 45 后成长阶段选择教程 | 四语言页面、阶段筛选、两张推荐卡、发布时间/时长/语言/理由、CollectionPage + ItemList |

原有 35 个主题，停用 `global-changes`，新增 4 个主题后为 **38 个主题、152 篇攻略**。旧路径及 `/en`、`/ja`、`/es`、`/de` 变体返回 308，跳转到同语言 `/guide`。

首页新增视频推荐，相关攻略最多显示两支；侧栏增加视频中心，sitemap 加入四语言中心。视频采用本地封面与直接 YouTube 外链，`noopener noreferrer`；不嵌入播放器，点击前没有 YouTube/ytimg/googlevideo 请求，无脚本仍可打开全部推荐。

英语新增关键词仅使用用户授权的 `aion 2 settings`、`aion 2 gear progression`、`aion 2 daily weekly checklist`、`aion 2 crafting`。历史关键词库和首批优先词清单保留；公开主题清单、显式文章注册、四语言导航、相关阅读、canonical 与 hreflang 同步更新。

## 已有页面调整

本次调整了 `guide`、`leveling`、`gathering`、`classes`、`tier-list`、`ranger`、`builds`、`code`、`database`、`download`、`maintenance`、`map`、`monetization`、`notmeter`、`presets`、`server`、`steam`、`twitch-drops` 的公开正文或 metadata，并同步四语言。

- 新手、升级、采集页连接设置、装备、清单和制作内容。等级 45 上限沿用已归档的官方展示；不把旧地区服数字路线改名发布。
- 安装、Steam、服务器、付费入口使用已经开放的正式服务措辞；先行访问仅作为历史或仍影响账号条件的说明。保留 Steam/PURPLE 账号互通、实际支持语言和服务器地区等操作限制。Steam 的韩语语言支持保留，它不是韩国地区服攻略。
- 维护页区分过去的 10 月 5 日上线维护与当前状态查询，加入 Duty 访问修复；不把历史维护窗口写成下一次停服。
- 奖励页删除已过期的先行访问邮件领取提示，加入 Pet/Wishlist 邮件礼物的资格和期限，以及 Customization Voucher 的 ESC → Closet 使用入口。
- Tier 页去掉另一地区服的比较列和残留的“B 对 S”标题；保留原有首发评级及其适用范围，快速答案重新回答评级问题。Spiritmaster/Ranger 描述使用已有职业玩法事实，不把新采集视频里的混合地区数字或等级阈值当成游戏规则。
- 首页、页脚、政策页和反馈模板同步公共范围；来源说明只保存在内部记录。

仅这 18 个有实际内容修改的主题更新核对日期与修订号。未修改的其他 16 个存量主题恢复原核对日期，避免声称本次重新验证了全站所有机制。原始内部来源中的地区、版本、网址与未核实说明均保留。

## 来源与取舍

官方快照：[steam-official-news.json](steam-official-news.json)，通过官方 `ISteamNews/GetNewsForApp` 读取 `appid=3393110`、`steam_community_announcements`。Steam 新闻 API 的 `gid` 是外部新闻编号，与最终 community announcement ID 不同；维护时按标题及正文匹配，不直接拼接该 `gid`。

| 证据 | 本次采用的事实 | 限定 |
| --- | --- | --- |
| [Launch Into AION 2 Now!](https://steamcommunity.com/games/3393110/announcements/detail/712288224875119583)，10 月 5 日 | 正式服务开放、Steam 主游戏入口 | 不证明每个玩法数值 |
| [10 月 4/5 日维护](https://steamcommunity.com/games/3393110/announcements/detail/689769594581155933)，10 月 4 日 | 10 月 5 日 05:00–13:00 UTC 窗口、Journal → Duty 访问修复 | 公告修复记录；未做实际账号登录或 Duty 领取测试；不推导日常次数、奖励额度和周重置时间 |
| [Launch Rewards](https://steamcommunity.com/games/3393110/announcements/detail/712288224875118658)，10 月 4 日 | 账号登录与邮件奖励、两个 Advance 箱子 | 表格的 12 月 1 日 23:30 PST 转为 12 月 2 日 07:30 UTC；12 月 8 日 23:30 PST 转为 12 月 9 日 07:30 UTC。没有沿用含糊的正文日期 |
| [Customization Voucher to all players](https://steamcommunity.com/games/3393110/announcements/detail/712288224875120755)，10 月 5 日 | Bound 外观券、ESC → Closet | 未推导公告未给出的领取截止时间 |
| Trunx `Ei17ATvSLGM`，10 月 4 日 | 目标扫描、追击、药水、角色显示、其他玩家效果及入门系统 | 00:09–00:20 明确先行访问与 10 月 5 日入场语境；00:34–01:54 为设置；02:14 起技能/Daevanion；采用操作而非通用最优配置或 FPS 保证 |
| Sywo `J8WVY3FxPQM`，10 月 4 日 | 45 后探索、装备预览、腰带/护符 Morph、材料保留与制作介入 | 00:17–00:24 明确 Global/F2P 语境；00:53、01:51、02:17、11:53、13:19 为主要定位点；不发布作者路线的装备分数门槛、通用强化上限或“最强装备”结论 |

全部 20 支视频的原始字幕、章节和地区说明在用户资料索引中。发布与暂缓决定见 [video-review.json](video-review.json)。六支主要推荐候选中，Trunx 和 Sywo 发布；Savvvo、FRESHY 设置、MistaWigglez 升级、Nova 45 后教程仍缺少足够清楚的当前服务依据，因此暂缓。制作专门教程也暂缓；制作页采用已确认语境的装备教程和已有采集/市场/物品权限材料，范围集中在配方准备与操作。

Grobs 清单视频 12:03 附近明确把周三重置作为 KR/TW 推测，未写入日/周清单。TW 天族/魔族路线不推荐；混合地区的宏、界面和误区视频保留内部研究，不进入公开清单。

视频核对方法为原始描述、完整归档字幕中的相关段落、章节和每支两个静帧样本。`previews/*-0.jpg` 为 Daevanion/Expedition 画面，`*-1.jpg` 为 Essence Extraction/Transcendence 画面。它支持主题匹配和作者目标受众判断，**不是全片逐帧客户端来源鉴定**；精确客户端补丁未独立确认。公开页面未复制整个视频的数值路线。

## 实现与维护

- `src/content/beginner-videos.json`：公开卡片资料；四语言标题/理由，原始身份、时长、阶段、关联主题和本地封面。
- `src/lib/beginner-videos.ts`、`src/components/video-*.tsx`、`src/app/[locale]/beginner-videos/page.tsx`：首页/文章共用卡片及中心筛选。卡片打开 YouTube 页面，不创建播放事件或站内播放状态。
- 增加汇总 `video_click` 事件与固定 `videos` target，只发送规范页面路径和语言；不发送视频 ID、完整网址、查询参数或播放器观看记录。DNT、GPC、站内停用统计仍阻止发送。
- 内容检查增加公开视频数据完整性；新增 `test:beginner` 覆盖筛选、语言、推荐映射、无脚本访问、外链隐私和旧路径跳转。分享图检查纳入四个新主题；日文字体补入“毎”“週”。
- 原来的工具/布局/性能测试仍假定总览 `builds` 展示装备卡，但本次修改前的页面已经没有该组件。把展开卡片验收移动到实际存在组件的 `cleric-build`，保持两张初始、七张展开和延迟请求检查；22 张模板的 API 断言保留。没有为了满足旧测试给玩家增加额外组件。
- `before/` 保存修改前正文、metadata、注册和界面文案、发布清单及字体。此目录中的 Python 脚本是一次性作者/迁移过程记录，**不可作为日常维护命令重复运行**；部分会从备份覆盖正文或追加注册。

## 验收

已通过：ESLint、TypeScript、四语言内容检查（152 篇、32 个存量配图来源、2 支视频）、27 个数据测试、180 个静态页面生产构建；172 项访问/SEO/sitemap 检查、152 篇攻略浏览器检查、20 个本次新手页面检查、192 项四语言布局/放大检查、导航与角色/装备/预算工具检查、8 个政策页检查，以及 11 项匿名统计场景。

统计测试的受保护汇总读取部分需要 `ANALYTICS_READ_TOKEN`，本机未配置，因此该部分跳过；浏览器视频点击、隐私停用和无敏感字段检查已执行。没有替用户设置生产统计凭据或运行真实角色 API 请求。

最终分享图检查通过：36 张四语言 PNG、版本化文章分享链接和无效路由 404；已查看日文每日/每周和装备成长分享图，新增字形正常。桌面/手机视频中心、首页和装备成长页面已查看截图，320px 与 390px 检查无横向溢出。

最终性能采用 390×844、冷缓存、1.6Mbps、4 倍 CPU 降速，每个路径三次采样，共 9 个路径。完整结果见 [performance-with-ga.json](performance-with-ga.json)：

- LCP 中位数 876–1352ms、CLS 为 0、交互事件 24–80ms，总传输均低于 700KiB，四项目标通过。
- 站内脚本为 189420–203803 字节；新视频中心和装备成长页均为 189420 字节，低于 220KiB。
- 第三方脚本为 178917 字节；与 GA4 合并后总脚本 368337–382720 字节，**220KiB 总脚本预算未通过，测试退出码为 1**。已有 [2026-10-04 记录](../../../api/2026-10-04/catalogue-coverage-091156-862911/assessment.md) 记载同类 GA 开启时超标。本次没有关闭 GA、排除其字节或提高预算来制造通过结果。

测试截图留在 `.qa/`，可本地查看。布局和本次新手页面结果分别归档为 `layout-results.json` 与 `beginner-results.json`。本地预览为 `http://localhost:3100`；正式发布仍需按已有项目部署流程进行。
