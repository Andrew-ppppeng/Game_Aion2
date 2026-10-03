# AION 2 Wiki

四语言 AION 2 攻略站，使用 Next.js App Router、TypeScript、Tailwind CSS、next-intl 和 MDX。20 个优先主题分别提供英、日、西、德正文，共 80 个攻略页；隐私和条款页面仍为未收录的占位页。

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
npm run build
npm run start
```

在服务运行期间，另一个终端执行：

```sh
npm run test:smoke
npm run test:browser
npm run test:performance
```

浏览器测试默认使用本机 Chrome；未安装时可运行 `npx playwright install chromium`，或者通过 `PLAYWRIGHT_BROWSER_PATH` 指定浏览器可执行文件。桌面与手机截图保存在 `.qa/`。`QA_BASE_URL` 可指定另一个本地端口。性能脚本用手机视口、冷缓存、1.6Mbps 和 4 倍 CPU 降速，采样三次；结果保存在 `.qa/performance-after.json`，只用于本机对比。

将 `.env.example` 复制为 `.env.local`，设置 `NEXT_PUBLIC_SITE_URL` 为正式域名，然后重新构建。canonical、语言替代链接、站点地图和分享信息会使用该地址。本地默认域名为 `http://localhost:3000`。

## 内容与维护

- `home.en.json`：原始英语首页文案，直接作为英语内容源，保留原文件。
- `src/messages/`：首页和导航界面文案；文章公共标签在 `src/i18n/article-messages.ts`。
- `keywords-priority-20.json`：唯一的第一版主题计划。侧栏与攻略路由从此生成，原关键词与分类保持不变。
- [术语核对.md](术语核对.md)：2026-10-02 四语言二代官方名称、职业、阵营与关键词标题核对；两个关键词 JSON 的 `terminologyReview` 指向此表。日语使用 `AION2`，其他语言使用 `AION 2`；待核实译名单独标注。
- `src/content/home.mdx`：首页模块编排，实际经过MDX编译。
- `src/content/{locale}/{slug}.mdx`：四语言独立攻略正文；同名 JSON 保存本地化标题、摘要、描述与目录。
- `src/content/article-data/{slug}.json`：四语言共用的核对日期、修订号、地区、原始来源与相关主题。来源标题保留原文，来源类型标签按页面语言显示。
- `src/lib/articles.ts`：显式文章注册表及服务端加载器。正文、导航状态、metadata 和 sitemap 共用此注册表；不回退到英语正文。
- `src/mdx-components.tsx`：MDX 共享组件。站内 Markdown 链接自动保留当前语言，外部资料在新标签打开；GFM 表格支持横向滚动。
- `src/components/article-page.tsx`：攻略外壳，含快速答案、目录、来源、相关攻略及 Article/BreadcrumbList 结构化数据。
- `src/lib/topics.ts`：稳定的主题ID、slug与分类，后续工具或数据库可复用这些ID。
- `src/lib/coupons.ts`：官方Global兑换码来源和UTC到期时间。页面在浏览器内根据时间更新过期状态；兑换码仅经公告核实，未做游戏内兑换测试。
- `assets.sources.json`：图片和首页事实的来源记录。
- `src/content/guide-assets.json`：内页的 28 条图片来源记录；含原图地址、发布者、核对日期、地区、版本、尺寸和用途。图片在 `public/media/guides/`，保留原图，不伪造游戏界面。
- `src/i18n/guide-messages.ts`：图片放大、目录、筛选、清单和下一篇卡片的四语界面文字。
- `src/lib/reading-paths.ts`：各主题推荐的下一篇攻略；正文卡片、页尾卡片和相关链接会去重。

页面默认使用暗色冰蓝主题。完整攻略页使用 `index, follow`，具有独立 canonical、四语与 `x-default` 替代链接；站点地图包含 4 个首页和 80 个攻略页。法律占位页仍使用 `noindex, follow`。

修改英语事实稿后，须同步日、西、德对应正文和 metadata。四语保持目录 ID、引用链接、数值、地区与适用版本一致；`npm run test:content` 校验覆盖、来源、链接、锚点与编码，事实和翻译语义还需人工审校。正文不放视频时间点，视频证据保存在研究日志。

逐主题补采原文与研究说明在 `research/content/2026-10-02/` 和 `research/content/2026-10-03/`。服务器、活动和维护均为核对日的公告快照，维护页面不提供实时探测。Global 是主体；KR/TW 经验、作者评级和未确认的客户端细节均在正文中说明适用范围。

## 配图与互动组件

每篇 MDX 通过以下组件使用同名 JSON 的本地化数据：

- `<GuideVisual id="topic" />`：`visuals.topic` 提供 `assetId`、本地化 `alt` 和 `caption`；使用来源清单中已登记的图片。
- `<GuideVisual id="workflow" />`：`visuals.workflow` 提供 `title`、`caption` 和至少 3 个 `steps`，每步有 `label` 和 `description`。说明图用于解释操作，不作为游戏实测数据。
- `<GuideChecklist />`：`checklist` 提供标题与稳定的 `items[].id`、本地化 `label`。当前用于新手和下载页；勾选状态按主题保存在浏览器，切换语言后保留，可以重置。存储受限时仍可在当前页面使用。
- `<GuideClasses />`：职业页的八职业官方画像与职责筛选；职业身份在 `src/content/class-identities.json`。
- `<GuideFaction faction="elyos">…</GuideFaction>` / `asmodians`：升级页的阵营章节。
- `<GuideRegion region="eu">…</GuideRegion>`：服务器页的地区章节；其他地区组合外层用 `other`，内层分别用 `naWest`、`naEast`、`latam`、`asia`。
- `<GuideNext slug="leveling" />`：正文中的下一篇卡片；JSON 的 `inlineNext` 同步登记这些 slug，用于页尾去重。

四语使用相同 visual ID、asset ID、清单项 ID、组件顺序和筛选分组。`npm run test:content` 会检查对应关系，`npm run test:browser` 检查 80 页及互动行为。手机目录可展开并高亮当前章节；图片可点击放大，表格可横向滚动；筛选隐藏的章节能通过目录重新展开。无脚本时仍输出完整正文、来源和图片。

本轮未接入统计。停留时间、跳出率和阅读路径的实际变化，须在后续取得访问数据后评估。

原有资料、Discord导出、研究记录、主题文件和favicon原件均保留。主页所展示的维护日期为资料快照，不代表实时服务器状态。
