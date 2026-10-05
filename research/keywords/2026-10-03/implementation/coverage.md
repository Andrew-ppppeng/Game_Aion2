# AION 2 内容实施覆盖 · 2026-10-03

**已完成28个主题、112篇四语言正文；原63词全部逐项映射。剩余待证主题保留队列，不用薄页填满。**

- 新增8个独立主题：Gladiator、Ranger、Spiritmaster、阵营、转服、Notmeter、玩家人数、通用宏。
- 原20个主词保留；另外43词不等于43张新页，按独立任务和现有答案归并。
- 本档记录本地内容实现，不能据此声称已经部署、收录或获得流量。英文先定事实，日／西／德正文同时齐备。

## 原63词的完整承接表

下表词形仅省略共同前缀 `aion 2`；JSON保留每个原词及来源、国家、窗口、时间、增幅属性、状态、缺口和下一步。

| 原词 | 优先级 | 当前状态 | 承接／计划 |
| --- | --- | --- | --- |
| `guide` | P0 | 旧页增补 | /guide |
| `leveling` | P3 | 既有页 | /leveling |
| `gathering` | P3 | 既有页 | /gathering |
| `classes` | P0 | 旧页增补 | /classes |
| `chanter` | P0 | 旧页增补 | /chanter |
| `tier list` | P0 | 旧页增补 | /tier-list |
| `gladiator` | P1 | 新页完成 | /gladiator |
| `ranger` | P1 | 新页完成 | /ranger |
| `spiritmaster` | P1 | 新页完成 | /spiritmaster |
| `brawler` | P3 | 部分覆盖 | /classes#brawler-and-regional-guides |
| `class quiz` | P3 | 暂缓 | 暂无公开页；计划 /class-quiz |
| `builds` | P0 | 旧页增补 | /builds |
| `cleric build` | P0 | 旧页增补 | /cleric-build |
| `chanter build` | P0 | 旧页合并承接 | /chanter |
| `chanter skills` | P0 | 旧页合并承接 | /chanter |
| `cleric guide` | P0 | 旧页合并承接 | /cleric-build |
| `gladiator build` | P1 | 新页合并承接 | /gladiator#starter-build |
| `macro guide` | P2 | 新页完成 | /macro-guide |
| `ranger macro` | P2 | 待Global证据 | 暂无公开页；计划 /ranger-macro |
| `character creation` | P3 | 旧页增补 | /character-creation |
| `presets` | P3 | 既有页 | /presets |
| `redo character creation` | P2 | 部分覆盖 | /character-creation；计划 /redo-character-creation |
| `races` | P1 | 新页完成 | /races |
| `release` | P0 | 旧页合并承接 | /steam#access-schedule |
| `early access` | P0 | 旧页合并承接 | /steam#access-schedule |
| `global release date` | P0 | 旧页合并承接 | /steam#access-schedule |
| `pre registration` | P0 | 部分覆盖 | /steam#global-and-regional-versions |
| `release time` | P0 | 旧页合并承接 | /steam#access-schedule |
| `japan release date` | P0 | 旧页合并承接 | /steam#global-and-regional-versions |
| `global` | P0 | 旧页合并承接 | /steam#global-and-regional-versions |
| `japan` | P0 | 旧页合并承接 | /steam#global-and-regional-versions |
| `taiwan` | P0 | 旧页合并承接 | /steam#global-and-regional-versions |
| `steam` | P0 | 旧页增补 | /steam |
| `ps5` | P0 | 有限覆盖 | /steam#platform-and-controller-support |
| `purple` | P0 | 旧页合并承接 | /download |
| `mobile` | P0 | 有限覆盖 | /steam#platform-and-controller-support |
| `download` | P0 | 既有页 | /download |
| `controller` | P0 | 有限覆盖 | /steam#platform-and-controller-support |
| `system requirements` | P0 | 旧页合并承接 | /download |
| `server` | P0 | 旧页增补 | /server |
| `maintenance` | P0 | 既有页 | /maintenance |
| `server transfer` | P1 | 新页完成 | /server-transfer |
| `server status` | P0 | 旧页合并承接 | /maintenance |
| `map` | P0 | 既有页 | /map |
| `interactive map` | P0 | 旧页合并承接 | /map |
| `pvp` | P3 | 既有页 | /pvp |
| `spacetime rift` | P1 | 旧页增补 | /spacetime-rift |
| `code` | P0 | 既有页 | /code |
| `twitch drops` | P0 | 既有页 | /twitch-drops |
| `monetization` | P0 | 既有页 | /monetization |
| `founders pack` | P0 | 旧页合并承接 | /monetization |
| `g2g` | P3 | 暂缓 | 暂无公开页 |
| `twitch` | P2 | 旧页合并承接 | /guide#community-resources |
| `reddit` | P2 | 旧页合并承接 | /guide#community-resources |
| `discord` | P2 | 旧页合并承接 | /guide#community-resources |
| `bahamut` | P2 | 有限覆盖 | /guide#community-resources |
| `steam charts` | P2 | 新页合并承接 | /player-count#steamcharts-and-steamdb |
| `steamdb` | P2 | 新页合并承接 | /player-count |
| `player count` | P2 | 新页完成 | /player-count |
| `notmeter` | P1 | 新页完成 | /notmeter |
| `lagofast` | P3 | 暂缓 | 暂无公开页 |
| `review` | P3 | 暂缓 | 暂无公开页；计划 /review |
| `gameplay` | P3 | 暂缓 | 暂无公开页；计划 /review |

## 本轮调研证据如何计入

- 27条当前Rising按原国家、近一天滚动窗口、20:18–20:27北京时间保存；3条明显无关词仍保留原值但排除。德国/西班牙中的英语查询仍是英语查询。
- 13条继承观察仅保留 `claimedGrowth`，不当作新证实的增长。4个查询在后次Rising复现，9个未复现或不可读；未复现不等于需求为零。
- 30条实际下拉联想单独记录，无增长率；请求hl/gl、个性化与实际国家未核实限制保留。前次只有片段的联想不补造完整查询。
- `npcap` 已由Notmeter维护者安装说明确认关联，归并 `/notmeter`；不创造 `aion 2 npcap`。
- Similarweb Arcana7行作为辅助保留截至9月30日的近28天估计值，`<50`不改为0；不估算流量、不累加同义词体量。

优先级同时参考前次Similarweb实际界面读取的29条选样：职业 `classes` 142.4K、KD3，Gladiator 8K及其build 6.1K、阵营6.5K支持职业内容优先；`release date` 199.8K支持维护Steam访问时间，`steamcharts` 22.4K支持有日期的人数页。社区查询多为导航需求，集中放入攻略入口资源区。仅引用相同原词的估计值，各词不相加。

上述Similarweb窗口为Worldwide／Google／All traffic、近28天、截至9月30日；精确采集时刻未保留，本轮未重查，与Trends近一天涨幅分开。原选样见 [similarweb-plan-observations.json](similarweb-plan-observations.json)。

## 已完成内容的事实边界

- **职业3页：** 起步实例来自有字幕与时间日志的区域角色示范；未发布Global最优配点、节点坐标或统一伤害排序。
- **阵营／转服：** 官方确认二阵营、临时配对、10月14日开始计划、同阵营与初始EA限制；没有补造换阵营、菜单或冷却规则。
- **Notmeter：** 维护者来源、安装说明与Npcap依赖已核；程序未运行，Global兼容及NC批准未独立确认。
- **人数：** SteamDB日期快照，非全客户端总量；SteamCharts当前查无页，官方人数API无可用JSON均不写成0。
- **宏：** 通用菜单来自上线期玩家演示，未声明游戏内独立实测；Ranger/Cleric专属模板和固定延迟仍待证。
- **Steam：** Global与日本时区/TW服务区分；未查到的PS5、原生Global手机、控制器支持不写成永久不支持。社区入口另标官方/社区和地区。

## 下一批顺序与验收

1. P0维护：访问阶段、活动截止、价格、维护公告与来源入口的时效。
2. P1补证：Global裂隙日程；转服实际开放后补界面与条件；职业技能与工具兼容按明确证据更新。
3. P2小批：Ranger/Cleric职业宏、重做/删除、Arcana、Odyle、Dimensional Invasion、木桩地点，证据不足则推进下一主题。
4. P3保留：Brawler Global可选状态、测评、实际体验评测、品牌导航、官方roadmap和完整database；不以旧涨幅强行发布。

结构验收：63个原词、20个历史主词、43个余词、27条当前Rising、13条继承观察、30条联想数量与原词一致；已有承接URL的四语正文和锚点存在。原词库与旧研究SHA-256保留在JSON。

上线后第14／30／60／90天按页面、查询、语言、国家复盘。以真实曝光与内容缺口决定下一批；收录异常先排查，不虚构排名、收益或点击预测。

机器可读档：[keyword-coverage.json](keyword-coverage.json)。原证据：[../evidence.json](../evidence.json)。
