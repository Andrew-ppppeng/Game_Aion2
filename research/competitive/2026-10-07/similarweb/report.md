# AION 2 竞品流量与下一步建议

**结论：集中运营已有的 classes、tier-list、builds 三个入口；下一项工具优先验证并实现裂缝日程。** 地图采集路线和可使用的捏脸案例放在第二批。你已经有职业技能、起手循环、角色收藏、材料预算和新手清单；本次证据支持集中改进这些入口与传播，而不是扩大页面数量。

采集：2026-10-07，通过 Computer Use 操作 Edge 中的 Similarweb。名单来自 `research/competitive/2026-10-03/competitors.json`（19 站），额外补查关联站 aion2t.com，共 20 个域名。

## 先读统计口径

- **整站 Visits**：Worldwide / All Traffic / Include Subdomains / **Last 28 days (As of Oct 04)**。它是估算的访问次数，不是人数、PV，也不是自然月流量。
- **页面排名**：Organic Landing Pages 的自然搜索点击估算。**Website Content 被当前套餐锁定，全渠道热门页面没有获得。** 本报告不把 SEO 点击写成页面总访问量。
- **品牌搜索**：网站表现页面的品牌 / 非品牌卡片实际显示 **2026 年 9 月**，与所选 28 天不同。
- Questlog、Timesaver、Fextralife、Inven、Gamers4 是多游戏平台，表中总量不能当作 AION 2 流量；分区全渠道流量未知。
- 小站结果仅作显示值记录。aion2guide.org 的 Visits 为 607，而自然落地页估算明显更高，两模块不一致；不能反推真实访问量。N/A 也不等于零。
- 本期截至 10 月 4 日，不能据此判断 10 月 5 日之后的实际走势；不能直接与旧报告的 8 月自然月数字计算涨跌。

## 20 个域名分别有多少流量

下表页面括号内是 **自然搜索点击**，不是 Visits。完整来源 URL 与更多落地页见 data.json / CSV。

### 专门的 AION 2 站点

| 网站 | 28 天整站 Visits | 自然搜索占比 | 搜索高点击页（前三） |
| --- | ---: | ---: | --- |
| [aion2hub.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2hub.com) | 642,942 | 69.42% | [/classes (87.9K)；/tools/event-timer (15.4K)；/builds (12.3K)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2hub.com&pageFilter=%5B%7B%22url%22%3A%22aion2hub.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2tool.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2tool.com) | 526,189 | 43.03% | [首页 (113K)；/server-comparison (2.5K)；/statistics/skill (1.7K)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2tool.com&pageFilter=%5B%7B%22url%22%3A%22aion2tool.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [shugo.gg](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=shugo.gg) | 267,402 | 38.15% | [/tierlist (7.1K)；首页 (6.4K)；/leaderboard (4.2K)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=shugo.gg&pageFilter=%5B%7B%22url%22%3A%22shugo.gg%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2t.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2t.com) | 55,368 | 9.78% | [/ru/news/48 (1K)；首页 (330)；/daevanion (220)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2t.com&pageFilter=%5B%7B%22url%22%3A%22aion2t.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2timers.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2timers.com) | 17,027 | 18.81% | [首页 (820)；/community-tools (250)；/calculator (200)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2timers.com&pageFilter=%5B%7B%22url%22%3A%22aion2timers.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2.app](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2.app) | 9,222 | 20.45% | [首页 (1K)；/db/monsters/2600068 (180)；/db/items/610530011 (160)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2.app&pageFilter=%5B%7B%22url%22%3A%22aion2.app%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2atlas.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2atlas.com) | 7,737 | 13.45% | [/skins (300)；/event-timer (220)；/interactive-map?filters=hiddenCubes (120)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2atlas.com&pageFilter=%5B%7B%22url%22%3A%22aion2atlas.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2hub.me](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2hub.me) | 2,410 | 26.35% | [/en/builds/4412ae73-5fd2-4527-9f3b-42d0704d8300 (110)；/en/classes/brawler (100)；/en/db/skills?class=brawler (100)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2hub.me&pageFilter=%5B%7B%22url%22%3A%22aion2hub.me%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2.tools](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2.tools) | 1,219 | 未完整记录 | [首页 (80)；/db/item/tw/radiant-odyle (80)；/db/item/tw/asvata-wood (< 50)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2.tools&pageFilter=%5B%7B%22url%22%3A%22aion2.tools%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2game.wiki](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2game.wiki) | 695 | 45.10% | [/fr (90)；/guide/system-requirements (90)；/ja/guide/beginner-guide (60)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2game.wiki&pageFilter=%5B%7B%22url%22%3A%22aion2game.wiki%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2guide.org](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2guide.org) | 607 | 25.82% | [首页 (350)；/guides/aion-2-pre-registration-rewards (260)；/classes/aion-2-sorcerer-guide (180)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2guide.org&pageFilter=%5B%7B%22url%22%3A%22aion2guide.org%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [dbaion2.online](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=dbaion2.online) | 无数据 | 未完整记录 | [/en/items/533700110 (50)；/en/npcs/2320807 (50)；/en/npcs/2000952 (< 50)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=dbaion2.online&pageFilter=%5B%7B%22url%22%3A%22dbaion2.online%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion2gg.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion2gg.com) | 无数据 | 未完整记录 | [首页 (< 50)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2gg.com&pageFilter=%5B%7B%22url%22%3A%22aion2gg.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [elysion.quest](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=elysion.quest) | 无数据 | 未完整记录 | [/item/535810485 (< 50)；/quest/2302541 (< 50)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=elysion.quest&pageFilter=%5B%7B%22url%22%3A%22elysion.quest%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |
| [aion-two.wiki](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=aion-two.wiki) | 无数据 | 未完整记录 | [无结果](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion-two.wiki&pageFilter=%5B%7B%22url%22%3A%22aion-two.wiki%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |

Atool（aion2tool.com）86.11% 访问来自韩国；9 月品牌搜索占 97%，热门页面也主要承接“아툴”品牌词。它适合参考统计与工具体验，不能据此预期一个英语新工具上线就能复制 52.6 万 Visits。aion2t.com 主要是俄语受众，并与 aion2.app 相互导流，两个域名不应合并成独立用户规模。

### 多游戏平台

| 网站 | 28 天整站 Visits | 自然搜索占比 | 搜索高点击页（前三） |
| --- | ---: | ---: | --- |
| [questlog.gg](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=questlog.gg) | 1.577M | 23.14% | [/aion-2/pt/news/aion-2-class-guide-launch-roster (13.7K)；/aion-2/en/map (9.7K)；/aion-2/en/classes (6.5K)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=questlog.gg&pageFilter=%5B%7B%22url%22%3A%22questlog.gg%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22%2Faion-2%2F%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic) |
| [timesaver.gg](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=timesaver.gg) | 1.679M | 82.37% | [/blog/aion-2-character-creation (5.7K)；/blog/aion-2-server-list (4.1K)；/blog/aion-2-classes (3.3K)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=timesaver.gg&pageFilter=%5B%7B%22url%22%3A%22timesaver.gg%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22aion-2%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic) |
| [fextralife.com](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=fextralife.com) | 14.84M | 70.93% | [/Classes (60.8K)；/Aion_2 (7.3K)；/Interactive_Map (5.9K)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=fextralife.com&pageFilter=%5B%7B%22url%22%3A%22fextralife.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22aion2.wiki.fextralife.com%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic) |
| [inven.co.kr](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=inven.co.kr) | 45.80M | 未完整记录 | [首页 (178.3K)；?vtype=pc (2.5K)；/dataninfo/stream (290)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=inven.co.kr&pageFilter=%5B%7B%22url%22%3A%22inven.co.kr%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22aion2.inven.co.kr%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic) |
| [gamers4.life](https://pro.similarweb.com/#/digitalsuite/websiteanalysis/overview/website-performance/*/999/28d?webSource=Total&key=gamers4.life) | 140,459 | 23.91% | [/aion-2/database/ja/hidden-cubes (560)；/aion-2/database/en/build-calculator (450)；/news/aion-2-interactive-map (380)](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=gamers4.life&pageFilter=%5B%7B%22url%22%3A%22gamers4.life%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic) |

页面筛选范围：Questlog URL 包含 `/aion-2/`；Timesaver 包含 `aion-2`；Fextralife 包含 `aion2.wiki.fextralife.com`；Inven 包含 `aion2.inven.co.kr`。Gamers4 没有加分区筛选，因此它的页面份额分母仍为整站自然落地页报告。Inven 主域 /board 下的 AION 2 论坛 URL 也不被上述子域过滤覆盖。

## 最值得借鉴的高点击页面

| 竞品 | 页面 | 28 天自然搜索点击 | 当前自然落地页报告份额 |
| --- | --- | ---: | ---: |
| AION2 Hub | /classes | 87.9K | 56.30% |
| AION2 Hub | /tools/event-timer | 15.4K | 9.83% |
| AION2 Hub | /builds | 12.3K | 7.88% |
| AION2 Hub | /builds/gladiator | 5.9K | 3.78% |
| Shugo | /tierlist | 7.1K | 30.04% |
| Shugo | /leaderboard | 4.2K | 17.94% |
| Shugo | /timers | 2.6K | 11.21% |
| Questlog | /aion-2/en/map | 9.7K | 7.97%（筛选分区） |
| Questlog | /aion-2/en/classes/ranger | 5.7K | 4.65%（筛选分区） |
| Timesaver | /blog/aion-2-character-creation | 5.7K | 17.90%（筛选分区） |
| Timesaver | /blog/aion-2-server-list | 4.1K | 12.82%（筛选分区） |
| Fextralife | /Classes | 60.8K | 52.70%（筛选子域） |

来源：[AION2 Hub](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=aion2hub.com&pageFilter=%5B%7B%22url%22%3A%22aion2hub.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic)、[Shugo](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=shugo.gg&pageFilter=%5B%7B%22url%22%3A%22shugo.gg%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic)、[Questlog](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=questlog.gg&pageFilter=%5B%7B%22url%22%3A%22questlog.gg%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22%2Faion-2%2F%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic)、[Timesaver](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=timesaver.gg&pageFilter=%5B%7B%22url%22%3A%22timesaver.gg%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22aion-2%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic)、[Fextralife](https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=fextralife.com&pageFilter=%5B%7B%22url%22%3A%22fextralife.com%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&multiIncludeExcludeWebsites=%5B%7B%22type%22%3A%22Include%22%2C%22items%22%3A%5B%7B%22type%22%3A%22website%22%2C%22value%22%3A%22aion2.wiki.fextralife.com%22%7D%5D%2C%22matchType%22%3A%22Phrase%22%7D%5D&selectedPageTab=Organic)。

**职业选择是最明确的内容入口。** AION2 Hub 的职业总览、计时工具、配装总览三页合计占其自然落地页报告约 **74.01%**。Fextralife 的职业页同样占其筛选后的 AION 2 自然点击一半以上。这支持把“选职业 → 看具体职业 → 使用配装 / 工具”当成核心路径，不能把比例外推到全渠道 Visits。

**工具带来反复使用的机会。** Shugo 每次访问 6.11 页、停留 3:52；AION2 Hub 为 4.24 页、2:08。Shugo 直接流量占 45.53%，AION2 Hub 为 18.90%。这些是工具站的参考信号，不能单靠它们证明留存、SEO 或工具之间的因果关系。

**捏脸要提供“能使用的对象”。** Timesaver 的 character-creation 页面承接的首位关键词是 `aion 2 presets`。你的 presets 已有官方 Style Shop 操作步骤，下一阶段应补精选可用样式：清晰预览、真实样式链接、适用条件、下载与应用步骤。优先少量获得许可的案例，不编造滑条数据。

**不按低 KD / 字数单独排工作。** 职业类在多个站点都有估算点击信号；既有低 KD 研究仍可辅助判断零点击与难度，但不能替代你自己页面的曝光、CTR 与实际操作数据。

## 传播渠道的启发

| 网站 | 整站自然搜索 | 整站社交 | 社交流量内的主要来源 |
| --- | ---: | ---: | --- |
| AION2 Hub | 69.42% | 5.61% | YouTube 59.51%；Reddit 39.62% |
| Shugo | 38.15% | 10.30% | YouTube 87.86%；Reddit 12.14% |
| Questlog（多游戏整站） | 23.14% | 19.82% | YouTube 98.72% |
| aion2timers.com（小样本） | 18.81% | 13.27% | Reddit 98.99% |
| aion2atlas.com（小样本） | 13.45% | 52.27% | Reddit 92.97% |

这些社交平台比例的分母是**社交流量**，不是整站。AION2 Hub 的外链渠道为整站 5.19%，其中 steamcommunity.com 占外链流量的 33.37%。数据来源为各站 Website Performance，链接见上表流量记录。

推论：除了 Google，值得用职业比较图、可直接使用的计时工具和具体采集路线争取社区及视频作者引用。先提供完整答案和可用产品，再按社区规则分享。没有证据证明以上流量来自站长主动推广，也没有测量实际传播投入或成本。

## 对照你的网站：已有基础和具体缺口

| 现有内容 / 功能 | 已有基础 | 建议的下一步 |
| --- | --- | --- |
| /classes | 八职业卡片、视频、对照表、独立职业页链接 | 对照表目前在卡片与视频后；让玩家更快看见“角色 / 操作负担 / 单人或组队选择”的具体差异，结合 GSC 判断标题和摘要是否匹配查询 |
| /tier-list | 排行表、选择说明、PvP 与 builds 链接 | 当前一个 launch 列混合单人、组队、Abyss；用一致条件分别呈现 PvE / PvP / Solo。只使用有依据的判断，不为补齐表格编造 S/A/B |
| /builds 与各职业页 | 八职业起手循环、技能等级、特化 / Stigma / Daevanion 条件 | 保留有效细节；挑 Gladiator / Chanter / Cleric 做可复现配置卡，明确点数、购买与加成等级、解锁条件和用途；逐项补查缺失依据 |
| /spacetime-rift | 操作与限制指南，链接外部工具 | 本地尚无已核实的固定裂缝时间表，也未嵌入 GuideTimers；先补查地区 / 服务器 / 时区条件，再决定是否提供倒计时 |
| EventTimers | 时区切换、活动窗口倒计时、ICS 下载；已用于维护、代码、Drops | 可复用格式化与日历能力；周期裂缝需另核对重复规则及状态计算，不能把截止日期组件直接当成现成循环计时器 |
| /map 与 /gathering | 地图入口、攻略、外部地图 | 第二批做一条小范围、可核实的采集路线，补截图、移动方向、入口 / 高度与操作条件 |
| /presets | 官方 Style Shop 操作、应用成本和兼容性提示 | 第二批增加少量授权预览与真实可用样式链接，检验下载到应用的完整路径 |
| 返回工具与埋点 | 角色收藏、材料预算、新手清单；tool_use、保存、return_7d | 优先让现有工具被相关攻略发现，并利用现有埋点衡量使用和回访 |

本地依据：`src/content/en/{classes,tier-list,builds,presets,spacetime-rift,map,gathering}.mdx`、`src/components/tools/event-timers.tsx`、`src/content/game-data/events.json`、`src/components/return-tools.tsx`、`src/components/site-analytics.tsx`。这是内容与代码盘点，未对你的生产站流量、性能或功能进行完整验收。

## 接下来两周，只推进三件事

1. **第 1–4 天：集中优化已有职业入口。** 先取你自己 GSC 最近 28 天的页面 / 查询数据：曝光、点击、CTR、平均排名。优先曝光已有、排名约 8–30 的相关页面；本次未成功取得你站的 GSC 数据，排序暂以竞品信号为依据。重点 /classes、/tier-list、/builds、/gladiator、/chanter、/cleric-build。把比较表提前；拆清 tier 的活动条件；核实并补一两个可照用的配置。现有链接路径已经有基础，检查是否方便从选择职业进入实际配置。受影响的英 / 日 / 西 / 德内容同步保持事实与限制一致。
2. **第 5–10 天：只做一个反复使用的工具。** 首选裂缝日程：核实固定规则后再做下一次时间、本地时区、日历提醒和指南返回入口。现有原始资料仅记录“固定时间表未核实”；若资料无法支持，就先完善已核实活动的计时入口与现有保存工具，不上线猜测的 live 倒计时。完整地图、全物品库和 DPS 软件开发暂不列为本轮第一任务。
3. **第 11–14 天：准备两份可分享的实用成果，再检验数据。** 一份职业选择图 / 具体配置，一份可用日程工具。按社区规则准备 Steam / Reddit 发帖材料，准备给 YouTube 作者使用的简短说明和链接；发布 / 联系由你另行决定。本次没有向任何人发帖或发送消息。随后看 GSC 点击、next_guide_click、tool_use、保存与 return_7d，判断哪条路径值得继续投入。

**第二批候选**：小范围采集路线、捏脸精选样式、服务器实用信息。优先级随你自己的查询曝光与玩家反馈调整。保留现有关键词；竞品的 raw top keywords 只作需求证据，本次未扩写词库或更改页面。

## 文件

- `data.json`：统计范围、限制、20 域名流量与 157 条精选自然落地页转录。
- `traffic.csv`：20 域名整站流量与已记录的渠道 / 互动指标。
- `landing-pages.csv`：每站前 10 行（不足 10 行按实际），来源 URL、URL 筛选与份额分母；不是全部页面导出。
- `browser-log.md`：浏览器操作范围、付费限制、加载状态与小样本冲突记录。

所有新文件写入 `research/competitive/2026-10-07/similarweb/`，未覆盖 10 月 3 日的原始名单与资料。
