# 宏菜单截图公开接入（2026-10-03）

依根代理后续任务，将已核查的两张原始 JPG 复制至 `public/media/guides/macro-global-keybind.jpg` 与 `macro-global-editor.jpg`。未裁切、修改标记、重编码或覆盖研究原图；复制后 SHA256 与原始文件完全一致。

`guide-assets.json` 仅追加两项：原始文章与图片 URL、Karsten Scholz / MeinMMO 作者、2026-09-30 发表日期、Global 德语界面、尺寸、用途与复核日。许可字段如实记录没有核实到开放再分发许可，原有 NC/MeinMMO 权利保留，不声明 CC 或开放授权。

四语 `/macro-guide` 新增相同位置的两个 GuideVisual，分别解释设置中的起动键行与技能页编辑入口。说明和 alt 完整翻译，截图本身维持德语原图并注明其语言／日期／作者，未将图片解释为职业宏或 DPS 实测证据。

首次元数据追加经 PowerShell 默认管道编码，导致新增 ja/es/de 字段出现问号；内容检查发现后立即用 UTF-8 apply_patch 修正全部新增字段。再次完整 `npm run test:content` 通过：112 篇本地化文章、30 个素材，关键词、来源、视觉、目录、链接和编码均通过。

已通知 published_registry 与根代理继续统一构建和浏览器验证。
