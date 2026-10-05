# /races 三语同步实施

日期：2026-10-04。根代理提供的最终 `src/content/en/races.mdx` 与 `src/content/en/races.json` 为事实基线。

本轮仅修改 6 个内容文件：`src/content/{ja,es,de}/races.mdx`、`races.json`。没有修改英文、资产数据、CSS、来源记录、AGENTS 或其它主题。

## 对应结果

- 原 Useful decision 列、creation checklist 整段及旧 FAQ 全部删除。首张表统一两列；Class 行使用本地化 `/classes` 链接。
- 同步 6 个 H2：elyos-or-asmodians、worlds-and-campaigns、shared-dungeons、choose-with-friends、cross-faction-opponents、changing-faction。每个语言的 TOC 标题与对应正文标题完全一致。
- `faction-world-grid` 含两个 section，依次放 `GuideVisual id="topic"` 和 `GuideVisual id="asmodians"`。JSON 分别绑定 `races-cantas-valley`、`races-moslan-forest`。
- 同步两阵营各 4 个场景描述与阵营历史。缺少已核实当地译名的地名、组织和人物保留英文专名；日语沿用ベルテロン、アルトガルド，西语/德语沿用 Verteron、Altgard。
- Global 副本可跨阵营、跨服同队；`My faction only` 为可选限制。普通世界共同任务仍要求同地区、同阵营、同 home server；没有扩成跨阵营世界任务或跨地区副本。
- 同步同阵营转服及 2026-10-14、初期 EA-to-EA 限制。没有新增阵营技能/属性完全相同或 8 职业两阵营均可选的未证实断言。
- SEO 描述、summary、quickAnswer、图注和 alt 与英文对应；图注只描述对应场景。

## 本地定向检查

仅运行针对 races 三语文件的内联 Python 只读检查，没有运行全站测试。结果：

| 语言 | 正文字符 | 结果 |
| --- | --- | --- |
| ja | 2564 | PASS |
| es | 4968 | PASS |
| de | 4953 | PASS |

检查内容：6 个锚点与英文一致；正文 H2 与本语言 TOC 标题一致；全部链接、表格行列、组件顺序与英文一致；双 section/双图结构、metadata keys、资产 ID 和 GuideNext 一致；保留全部英文专名；原 checklist 锚点不存在；My faction only 保留；没有 U+FFFD、三问号或英文间乱码问号。另人工逐段核对机制与摘要，西语 Balaur servants 使用 `sirvientes` 避免与服务器 `servidores` 混淆。

根代理统一负责构建、浏览器视觉与全站验收。

## 最终信息增量复核同步

根代理更新英文后，仅定向修改 ja/es/de 三个 MDX，metadata 未改。Altamia Canyon 改为“峡谷曾是 Zumion Temple 所在之处，峡谷如今重新浮现，由 Notos Legion 看守”；三语均明确重新浮现的主体是峡谷。

同步删除：表后泛泛的差异概述；世界段中 Verteron 目的地并非 Altgard 目的地的重复句；故事末尾“区别不只是标签”的概括句；shared-dungeons 表后重复说明副本可跨阵营、世界任务需同阵营的整段。实际地点、故事冲突、组队条件表和 My faction only 操作保留。

重新运行 races 定向只读检查：三语正文长度、6 H2、TOC ID、链接、表格列数、组件顺序和编码全部通过，以上字符数为最终版本。未运行全站测试。
