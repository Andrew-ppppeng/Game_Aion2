# AION 2 Wiki

四语言首页，使用 Next.js App Router、TypeScript、Tailwind CSS、next-intl 和 MDX。20个攻略主题与隐私、条款页面目前只显示占位内容。

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
npm run build
npm run start
```

在服务运行期间，另一个终端执行：

```sh
npm run test:smoke
npm run test:browser
```

浏览器测试默认使用本机 Chrome；未安装时可运行 `npx playwright install chromium`，或者通过 `PLAYWRIGHT_BROWSER_PATH` 指定浏览器可执行文件。桌面与手机截图保存在 `.qa/`。

将 `.env.example` 复制为 `.env.local`，设置 `NEXT_PUBLIC_SITE_URL` 为正式域名，然后重新构建。canonical、语言替代链接、站点地图和分享信息会使用该地址。本地默认域名为 `http://localhost:3000`。

## 内容与维护

- `home.en.json`：原始英语首页文案，直接作为英语内容源，保留原文件。
- `src/messages/`：界面文案及日语、西语、德语完整翻译。
- `keywords-priority-20.json`：唯一的第一版主题计划。侧栏和占位路由从此生成，原关键词与分类保持不变。
- [术语核对.md](术语核对.md)：2026-10-02 四语言二代官方名称、职业、阵营与关键词标题核对；两个关键词 JSON 的 `terminologyReview` 指向此表。日语使用 `AION2`，其他语言使用 `AION 2`；待核实译名单独标注。
- `src/content/home.mdx`：首页模块编排，实际经过MDX编译。
- `src/mdx-components.tsx`：MDX共享组件；后续文章可放在 `src/content/{locale}/{slug}.mdx`。当前未编写或发布任何攻略正文，添加MDX文件不会自动发布。
- `src/lib/topics.ts`：稳定的主题ID、slug与分类，后续工具或数据库可复用这些ID。
- `src/lib/coupons.ts`：官方Global兑换码来源和UTC到期时间。页面在浏览器内根据时间更新过期状态；兑换码仅经公告核实，未做游戏内兑换测试。
- `assets.sources.json`：图片和首页事实的来源记录。

页面默认使用暗色冰蓝主题。所有占位页面均设置 `noindex, follow`；站点地图只包含四个首页。正式内容发布时，需同时接入文章加载、更新主题状态和metadata、将实际发布的页面加入站点地图。

原有资料、Discord导出、研究记录、主题文件和favicon原件均保留。主页所展示的维护日期为资料快照，不代表实时服务器状态。

GitHub 首次提交包含四语言首页、占位路由、运行配置、页面资源和维护文档。`research/`、`discord/`、关键词 CSV、原始 favicon 文件和本地工具留在本地；文档中指向这些目录的链接需要本地资料。网页运行使用的图片与图标已包含在 `public/`。
