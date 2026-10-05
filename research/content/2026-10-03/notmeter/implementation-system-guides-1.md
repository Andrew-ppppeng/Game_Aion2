# NotMeter 实施与证据（2026-10-03）

状态：四语正文及元数据完成，可发布来源、维护者步骤和统计解读页。桌面程序在当前 Global 客户端的实测兼容性、NC 对该工具的明确批准未确认，不能作肯定描述。

## 本轮实读来源

- https://notmeter.com/：维护者自己的主页；初次安装弹窗实际写 Npcap → ZIP → 解压运行 NotMeter.exe；Global 搜索选项只证明网页入口。公开指标 DPS/nDPS、筛选和排名说明为维护者报告。原始 HTML、纯文本、请求元数据在 `../system-guides-run-1/notmeter-site*`。
- https://github.com/Not4You-Dev/NotMeter-Releases/releases：主页确实链接此仓库。GitHub API 当前仅返回 v1.0.246，发布时间 2026-08-29T00:37:48Z，正文为空，资产 NotMeter.exe/NotMeter.zip；不能据此推断当前 Global 捕获正常。旧 NotMeter-Update 仓库返回其他 test 标签，不作为下载推荐。两份原始 API 保留在同一 run 目录。
- https://npcap.com/：Windows 网络捕获项目的原始文档。NotMeter 当前链接 Npcap 1.88，Npcap 页面显示 1.89（2026-09-12）。正文不擅自选择某版为已验证兼容。
- https://www.plaync.com/policy/operation/aion2global/en：Global 官方运营规则，制裁表的 Unauthorized Programs 与正常服务干扰／保护规避有关；没有找到 NotMeter 专项许可，不能将一般条款改写为该程序已被允许或已被明确禁止。

## 制作与验证

- 新建 `src/content/{en,ja,es,de}/notmeter.{mdx,json}` 与 `src/content/article-data/notmeter.json`，未改共享注册表、旧页或原始词库。
- 正文同一事实、来源、锚点、链接、操作示例；四步可视流程明确为编辑比较方法。
- 未下载或运行 NotMeter/Npcap 可执行文件，未修改游戏设置、未登录／发消息给维护者。
- 独立检查通过：四语 JSON 解析、五节 TOC 对齐、正文长度、编码、链接同构、GuideVisual/GuideNext 对齐。整体构建由根代理统一执行。
