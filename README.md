# AION 2 Wiki

四语言 AION 2 攻略站，使用 Next.js App Router、TypeScript、Tailwind CSS、next-intl 和 MDX。已发布主题由 `content-topics.json` 管理，每个主题分别提供英、日、西、德正文；隐私、条款、编辑与纠错说明已提供四语言版本，不收录法律页。

## 本地运行

需要 Node.js 20.9+，本项目使用 Node.js 22 验证。

```sh
npm install
npm run dev
```

打开 http://localhost:3000。英语使用 `/`，其他语言使用 `/ja`、`/es`、`/de`。语言由URL决定；切换时保留当前主题、查询参数和锚点。

## 验证与生产运行

```sh
npm run check
npm run test:content
npm run test:data
npm run build
npm run start
```

在服务运行期间，另一个终端执行：

```sh
npm run test:smoke
npm run test:browser
npm run test:beginner
npm run test:tools
npm run test:review
npm run test:navigation
npm run test:structure
npm run test:analytics
npm run test:share
npm run test:site-info
npm run test:performance
```

浏览器测试默认使用本机 Chrome；未安装时可运行 `npx playwright install chromium`，或者通过 `PLAYWRIGHT_BROWSER_PATH` 指定浏览器可执行文件。桌面与手机截图保存在 `.qa/`。`QA_BASE_URL` 可指定另一个本地端口。性能脚本用手机视口、冷缓存、1.6Mbps 和 4 倍 CPU 降速，采样三次，覆盖首页、攻略、装备页、角色工具、视频中心、新栏目及成长清单。预算默认 LCP 2500ms、CLS 0.1、总传输 700KB、脚本 220KB、实验室交互 200ms；超预算退出失败。结果保存在 `.qa/performance-after.json`，其中交互测量是实验室检查，真实 INP 由匿名访问统计采集。当前 GA4 开启时，总脚本超过 220KB 目标；本次保留该失败结果，并新增站内/第三方脚本拆分记录，没有关闭统计或提高预算。

将 `.env.example` 复制为 `.env.local`，设置 `NEXT_PUBLIC_SITE_URL` 为正式域名，然后重新构建。canonical、语言替代链接、站点地图和分享信息会使用该地址。本地默认域名为 `http://localhost:3000`。

## 内容与维护

2026-10-09 页面结构整理为 Tools、Guides、Classes、Resources。`src/lib/site-structure.ts` 集中管理全部 38 个主题的唯一栏目归属、导航分组及工具入口；`content-topics.json` 继续作为发布清单，文章旧网址及关键词文件保持原样。新增 `/tools`、`/guides`、`/resources` 四语言聚合页，`/classes` 沿用职业总览并连接配装与评级。

`/tools/growth-checklist` 提供全职业通用成长清单：复用新手六项目标，再加入升级/技能三项及装备三项，共十二项。首次打开继承当前浏览器的新手完成项，之后按稳定目标 ID 独立保存于 `aion2-growth-checklist-v1`，包含 schemaVersion、templateRevision、completedIds；更新模板保留历史完成记录。可从任意阶段开始，手动完成、撤销及确认后重置；切换语言与刷新保持进度，浏览器禁止存储时提示临时状态，无 JavaScript 时保留目标和攻略链接。首页显示续做进度，旧新手与日周清单独立保存。

Tools 的第三方工具区域明确显示外部入口及本站教程；桌面采集兼容性未确认的 NotMeter 只链接教程，不展示为已确认可用的本站功能。职业专用成长清单及后续数据验证记录在 [拓展 TODO](docs/AION2-EXPANSION-TODO.md)。`npm run test:structure` 验证新栏目与成长流程；`test:data` 覆盖归属、继承、模板更新与攻略锚点。匿名统计只新增固定 `growth` target，初始化继承不算玩家保存，不上传勾选内容。

- `home.en.json`：原始英语首页文案，直接作为英语内容源，保留原文件。
- `src/messages/`：首页和导航界面文案；文章公共标签在 `src/i18n/article-messages.ts`。
- `keywords-priority-20.json`：保留首批 20 词的历史计划，原关键词与分类保持不变。
- `content-topics.json`：已发布主题的唯一清单。侧栏、攻略路由、sitemap 和检查数量从此生成；研究队列和未完成的翻译不加入此文件。
- [术语核对.md](术语核对.md)：2026-10-02 四语言二代官方名称、职业、阵营与关键词标题核对；两个关键词 JSON 的 `terminologyReview` 指向此表。日语使用 `AION2`，其他语言使用 `AION 2`；待核实译名单独标注。
- `src/content/home.mdx`：首页模块编排，实际经过MDX编译。
- `src/content/{locale}/{slug}.mdx`：四语言独立攻略正文；同名 JSON 保存本地化标题、摘要、描述与目录。
- `src/content/article-data/{slug}.json`：四语言共用的核对日期、修订号、地区、内部来源记录与相关主题。`edition` 指定页头与分享图的配置地区（缺省 Global），与正文范围一致；改变范围时同步修订号，避免旧分享图缓存。来源标题、日期、地区、版本和核实范围保留原文，不在攻略页展示。
- `src/lib/articles.ts`：显式文章注册表及服务端加载器。正文、导航状态、metadata 和 sitemap 共用此注册表；不回退到英语正文。
- `src/mdx-components.tsx`：MDX 共享组件。站内 Markdown 链接自动保留当前语言，外部资料在新标签打开；GFM 表格支持横向滚动。
- `src/components/article-page.tsx`：攻略外壳，含快速答案、目录、相关攻略及 Article/BreadcrumbList 结构化数据。来源列表和核实过程仅供内部维护。
- `src/lib/topics.ts`：稳定的主题ID、slug与分类，后续工具或数据库可复用这些ID。
- `src/lib/coupons.ts`：官方Global兑换码来源和UTC到期时间。页面在浏览器内根据时间更新过期状态；兑换码仅经公告核实，未做游戏内兑换测试。
- `assets.sources.json`：图片和首页事实的来源记录。
- `src/content/guide-assets.json`：内页图片来源记录；含原图地址、发布者、核对日期、地区、版本、尺寸和用途。图片在 `public/media/guides/`，保留原图，不伪造游戏界面。
- `src/i18n/guide-messages.ts`：图片放大、目录、筛选、清单和下一篇卡片的四语界面文字。
- `src/lib/reading-paths.ts`：各主题推荐的下一篇攻略；正文卡片、页尾卡片和相关链接会去重。

页面默认使用暗色冰蓝主题。完整攻略页使用 `index, follow`，具有独立 canonical、四语与 `x-default` 替代链接；站点地图包含四语言首页、清单中每个主题的四语言攻略页和四语言角色工具页。法律页和带查询参数的角色页不收录。攻略 JSON 的 `quickAnswer` 单独保存直接答案，与介绍摘要分开；分享信息使用带语言与标题的版本化 PNG 卡片。攻略标明负责维护的编辑团队并链接编辑说明。

新增主题须先完成四语言 MDX、metadata、共用来源数据及界面标题，再同步 `src/lib/articles.ts` 的显式导入/加载器、`src/lib/reading-paths.ts` 的推荐路径及发布清单；有新分类时同步导航图标和四语言分类名。保留现有 URL，不把同义词建成重复页。构建会拒绝清单中缺失注册或来源不匹配的主题。

修改英语事实稿后，须同步日、西、德对应正文和 metadata。四语保持目录 ID、操作链接、数值、地区与适用版本一致；`npm run test:content` 校验覆盖、内部来源、链接、锚点与编码，事实和翻译语义还需人工审校。正文直接描述机制和操作，图片说明只描述画面；来源分析、视频时间点、核对过程与无关的证据边界保存在研究日志。影响付费、过期时间、兼容性或玩法选择的实质限制应简洁说明，不把未经核实的猜测写成事实。

逐主题补采原文与研究说明在 `research/content/2026-10-02/` 和 `research/content/2026-10-03/`。玩家视角内容审查、修改前全文和逐组记录在 `research/content/2026-10-04/player-content-review/`。公开页面只服务 Steam AION 2 Global 玩家；其他地区服资料和原始评级保留在内部研究库。

2026-10-06 更新新增 `settings`、`gear-progression`、`daily-weekly-checklist`、`crafting` 四个完整四语言主题，当前共 38 个主题、152 篇攻略。旧 `global-changes` 页面永久跳转到同语言新手指南。修改前全文、官方公告快照、字幕核对和实施记录在 [本次更新记录](research/content/2026-10-06/steam-beginner-refresh/implementation.md)。一次性迁移脚本只供审计，不应重复执行。

`/beginner-videos` 提供四语言视频中心，收录 17 支教程，首页推荐 6 支，相关攻略最多推荐 3 支。支持主题筛选、标题/作者搜索、隐藏职业补充视频和章节跳转。`src/content/beginner-videos.json` 是公开推荐清单，`src/i18n/video-messages.ts` 保存四语言界面文字。卡片使用本地封面并直接链接 YouTube，不嵌入播放器；无脚本时仍可打开全部视频。添加推荐时核对资料、适用版本、过时操作与章节字幕，保留内部记录，再填写四语言标题、推荐理由、关联主题和时间点。

后续重写了 8 个主题的 32 篇四语言攻略，补充具体配方、装备路线、日常额度和宏操作，新增 3 张实际操作界面图。20 支视频的取舍、事实核对和验收记录在 [内容深化记录](research/content/2026-10-06/beginner-depth/completion.json)。原始视频大文件保留本地，Git 提交包含可复核的来源、字幕和研究记录。

## 配图与互动组件

每篇 MDX 通过以下组件使用同名 JSON 的本地化数据：

- `<GuideVisual id="topic" />`：`visuals.topic` 提供 `assetId`、本地化 `alt` 和 `caption`；使用来源清单中已登记的图片。
- `<GuideVisual id="workflow" />`：`visuals.workflow` 提供 `title`、`caption` 和至少 3 个 `steps`，每步有 `label` 和 `description`。说明图用于解释操作，不作为游戏实测数据。
- `<GuideChecklist />`：`checklist` 提供标题与稳定的 `items[].id`、本地化 `label`。当前用于新手和下载页；勾选状态按主题保存在浏览器，切换语言后保留，可以重置。存储受限时仍可在当前页面使用。
- `<GuideClasses />`：职业页的八职业官方画像与职责筛选；职业身份在 `src/content/class-identities.json`。
- `<GuideFaction faction="elyos">…</GuideFaction>` / `asmodians`：升级页的阵营章节。
- `<GuideRegion region="eu">…</GuideRegion>`：服务器页的地区章节；其他地区组合外层用 `other`，内层分别用 `naWest`、`naEast`、`latam`、`asia`。
- `<GuideNext slug="leveling" />`：正文中的下一篇卡片；JSON 的 `inlineNext` 同步登记这些 slug，用于页尾去重。

四语使用相同 visual ID、asset ID、清单项 ID、组件顺序和筛选分组。`npm run test:content` 会检查对应关系，`npm run test:browser` 检查清单中的全部四语言攻略及互动行为。手机目录可展开并高亮当前章节；图片可点击放大，表格可横向滚动；筛选隐藏的章节能通过目录重新展开。无脚本时仍输出完整正文和图片；来源列表和图片来源也不输出。

首页和全站导航提供角色查询、素材预算及清单入口；首页显示本浏览器已保存的工具状态。手机导航默认只展开当前文章所属类别，保持键盘循环、Escape 关闭与焦点返回；语言切换保留查询参数和文章锚点。普通攻略按需加载交互组件；装备页首屏仅输出两张卡，其余装备展开时获取，关闭时不请求额外数据，无脚本时保留名称与官方链接。

## GA4、匿名统计与纠错

全站已接入 Google Analytics 4，衡量 ID 为 `G-SHV8K5DLSK`，使用 `next/script` 在页面交互就绪后加载。GA 与站内匿名统计共用 `NEXT_PUBLIC_ANALYTICS_ENABLED`、隐私页开关及 DNT/GPC 设置；生产环境默认开启，开发环境默认关闭。GA 使用自己的 Cookie 和数据保存设置，与下述 Redis 汇总分开。

页面切换由 GA4 增强型衡量自动统计，不额外发送手动 `page_view`。请在 GA 后台「管理 → 数据流 → Web → 增强型衡量 → 网页浏览 → 高级设置」保持「基于浏览器历史记录事件的网页更改」开启，参见 [Next.js 官方说明](https://nextjs.org/docs/app/guides/third-party-libraries#tracking-pageviews)。上线后可在 GA「实时」报告确认访问。

统计复用现有 Redis，按 UTC 日期保存计数与 Web Vitals 直方图，35 天后过期。生产环境默认开启，开发环境需设置 `NEXT_PUBLIC_ANALYTICS_ENABLED=true`；`false` 完全关闭。服务器不保存访问者 ID、角色名/ID、搜索文本、预算内容或查询参数；IP 派生哈希仅用于 1 分钟限流。首访、上次访问和已回访标记只留在浏览器，停用统计会清除这些标记，工具保存状态继续可用。隐私页提供开关，DNT/GPC 优先关闭。Vercel 没有 Redis 凭证时统计返回 503；本地内存仅用于验证，不作为生产持久存储。

设置服务端 `ANALYTICS_READ_TOKEN` 后，可用 `npm run analytics:report` 查看保护接口的汇总，默认显示今日 UTC；指定日期使用 `npm run analytics:report -- YYYY-MM-DD`，范围使用 `--from YYYY-MM-DD --to YYYY-MM-DD`。统计包含页面浏览、下一篇点击、工具使用/保存、LCP/INP/CLS 直方图的 p75 区间估计，以及首访后 1–7 天再次访问的浏览器计数。清除存储、切换设备或禁用统计会影响计数；它不是人数统计。回访率等首访 UTC 日期结束后再满 7 天才纳入报表，INP 需要用户互动，不能把没有样本写成零。

反馈邮箱为 `feedback@aion2wiki.space`，统一配置在 `src/lib/site.ts`；四语政策页显示邮箱及邮件链接，页脚纠错入口和复制模板保留。邮箱修改后重新构建，不依赖额外环境变量。更新日文字段后，可运行 `scripts/update-share-font.py` 维护分享图字体子集（维护脚本需要 fontTools；站点运行不需要 Python）。

原有资料、Discord导出、研究记录、主题文件和favicon原件均保留。主页所展示的维护日期为资料快照，不代表实时服务器状态。

## 游戏数据与工具

已加入 22 件人工选择的装备例子、公开角色查询与固定属性比较、活动时区/倒计时/日历，以及手动素材预算，均提供四语言界面。cleric-build 和 chanter 展示对应职业的装备；计时器在 maintenance、twitch-drops、code、spacetime-rift 中展示；预算在 monetization 中展示，gathering 提供入口。

接入、数据边界、缓存策略和维护方法见 [docs/AION2-DATA.md](docs/AION2-DATA.md)。浏览器测试使用已归档的真实公开角色响应，运行中的真实接口检查可用 `npm run test:api`；该检查会有限查询官方站，不能在未配置共享缓存的 Vercel 环境中通过。
