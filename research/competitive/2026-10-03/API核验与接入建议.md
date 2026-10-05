# AION 2 数值 API 核验与接入建议

核验日：**2026-10-03，Asia/Shanghai**。本轮共 32 个不同官网请求快照，包含成功、参数错误、旧路由失效、空数据和超时。仅小量匿名 GET，没有登录、Key、全量分页、网络限制绕过或竞品程序安装。

## 结论

**可用：官网前端 JSON。尚未确认：AION2 官方开发者 Open API。**

Global EU、TW 的角色与装备链路实际返回 JSON；Global 的 EN/DE/ES/JA 物品名称已实测。先做装备卡、角色装备解释和官方术语对照，技术可行。实时价格、完整伤害计算、全服人口等仍没有充分数据依据。

[NC 开发者门户](https://developers.plaync.com/apis/l2m/search)本轮文档菜单只见 Lineage 2M。公开 JSON 的存在不能推导出正式的使用额度、SLA 或再分发许可。以下地址是**当前官网使用的接口**，不是发布者保证长期不变的开发者合同。

接口发现参考：[nuriland/aion2-api](https://github.com/nuriland/aion2-api)，非官方 Go 客户端，代码许可证为 MIT。MIT 适用于该客户端代码，不能据此判断游戏数据或图像也采用 MIT。源文件保存在 raw/sdk-*.body。

## 一、核验矩阵

全部精确 URL / 请求时间 / HTTP 状态：[api-verification.csv](api-verification.csv)。

| 能力 | Global EU | TW | 保存的主要证据 |
|---|---|---|---|
| Servers / Classes | JSON；18 / 8 条目录 | JSON；36 / 9 条目录 | api-global-eu-servers、classes；api-tw-servers、classes |
| Character search | 正确参数成功，取 3 条 | 加 race 后成功，取 3 条 | api-*-search-corrected |
| Character info | profile/stat/title/ranking/daevanion | 同类模块成功 | api-global-eu-info / api-tw-info |
| Character equipment | equipment/petwing/skill | 同类模块成功 | api-*-equipment |
| Equipped item detail | 真正装备 ID 成功 | 真正装备 ID 成功 | api-*-equipped-item-detail |
| Item template | 110160001 成功；另一 TW ID 空模板 | 110120001 成功；110460008 模板请求超时 | api-global-eu-item-from-equipment / api-tw-item-corrected |
| Item catalog/search | 本轮未确认可用目录 | 3 条样本；total 11225，limit 10000 | api-tw-catalog-localized |
| Daevanion detail | 225 个网格条目；89 条带效果 | 225 个网格条目；153 条带效果 | api-*-board-detail |
| Ranking list | 本轮参数返回 []、season=null | 同样为空 | api-*-ranking |
| Item localization | EN/DE/ES/JA 全成功 | 本轮未做同物品四语言比较 | api-global-item-* |

地区边界：

- **Global**：只实际测试 EU 角色链路。社区客户端列出 NA East、NA West、EU、South America、Asia 选项；本轮不声称其他四区也全部测试通过。
- **TW**：官网域名为 tw.ncsoft.com，单独存储数据，不能替代 Global。
- **KR**：两个测试请求返回 HTTP 200 的韩文找不到页面 HTML，未得到有效 JSON。社区客户端也记录了 KR 跨境可用性变化，错误状态与本环境观测不完全相同，以本轮日志为准。
- 响应没有统一客户端版本号；保存地区、请求日期和可核到的补丁版本。未知版本明确写未知，不能把本站日期自动当游戏版本。
- 本轮排名只测试 rankingContentsType=1、rankingType=0，不能据此断言所有未测试模式都永远为空。

## 二、可复现的静态请求

以下可以直接打开，抓取时间见对应 meta.json；未来变更需要重新核验。

### Global：服务器 / 职业

[EU 服务器目录](https://aion2.plaync.com/en-us/api/gameinfo/servers?lang=en-US&region=eu)

```text
GET https://aion2.plaync.com/en-us/api/gameinfo/servers?lang=en-US&region=eu
GET https://aion2.plaync.com/en-us/api/gameinfo/classes?lang=en-US&region=eu
```

返回 serverList / classList。目录条目数不是服务器在线人数、容量、延迟或实时状态。

### Global：已知 ID 物品

[英语物品模板](https://aion2.plaync.com/en-us/api/gameconst/item?id=110160001&enchantLevel=0&lang=en-US)

```text
GET https://aion2.plaync.com/en-us/api/gameconst/item?id=110160001&enchantLevel=0&lang=en-US
GET https://aion2.plaync.com/de-de/api/gameconst/item?id=110160001&enchantLevel=0&lang=de-DE
GET https://aion2.plaync.com/es-es/api/gameconst/item?id=110160001&enchantLevel=0&lang=es-ES
GET https://aion2.plaync.com/ja-jp/api/gameconst/item?id=110160001&enchantLevel=0&lang=ja-JP
```

本轮验证的同一模板：id=110160001，equipLevel=1，maxEnchantLevel=5，Attack 4–6，其余主属性 100/150/150。四种语言的 mainStats 属性 ID 和数值一致，名称分别本地化。

这是**特定物品 +0 的一次验证**，没有测试所有 ID、所有强化等级与高阶词条。已知 ID 可以来自同区角色装备、官网对应数据或经过验证的同区静态资料；不要靠连续 ID 猜测全量枚举。

### TW：物品与目录样本

[台服物品模板](https://tw.ncsoft.com/aion2/api/gameconst/item?id=110120001&enchantLevel=0&lang=en)

```text
GET https://tw.ncsoft.com/aion2/api/gameconst/item?id=110120001&enchantLevel=0&lang=en
GET https://tw.ncsoft.com/aion2_tw/v2.0/dict/search/item?page=1&size=3&locale=zh-TW
```

模板返回物品名、品质、职业、装备条件、主属性、可选副属性范围、强化上限和来源字段。目录页返回 contents / pagination，total=11225、limit=10000、lastPage=3334。**这不是“已下载完整 11225 物品”的证明**，也不能保证超出 limit 的部分可以遍历。

目录请求漏掉 locale 时，本轮拿到了韩文文本。因此域名在台湾并不自动意味着响应是繁中。

## 三、角色查询链路与参数

### Global EU

```text
1. GET https://api-search.plaync.com/aion2global/search/v2/character
   ?keyword=a&page=1&size=3&localeInfo=en-US&region=eu

2. GET https://aion2.plaync.com/api/character/info
   ?characterId=<ID>&serverId=<serverId>&lang=en-US&region=eu

3. GET https://aion2.plaync.com/api/character/equipment
   ?characterId=<ID>&serverId=<serverId>&lang=en-US&region=eu

4. GET https://aion2.plaync.com/api/character/equipment/item
   ?characterId=<ID>&serverId=<serverId>&lang=en-US&region=eu
   &id=<equipmentItemId>&enchantLevel=<level>&slotPos=<position>

5. GET https://aion2.plaync.com/api/character/daevanion/detail
   ?characterId=<ID>&serverId=<serverId>&lang=en-US&region=eu&boardId=<boardId>
```

这是参数说明，换行不是实际 URL 的一部分。实际成功 URL 保存在 CSV 与对应 meta.json。

**Global 搜索参数叫 localeInfo，不是 lang。** 本轮使用 lang 的初始搜索失败；正确参数后成功。profile/equipment 则使用 lang。

### TW

```text
GET https://tw.ncsoft.com/aion2/api/search/character
?keyword=fofo&race=2&page=1&size=3
```

本轮漏 race 的请求失败，加上 race 成功。后续 info / equipment / equipment/item / daevanion/detail 路径类似，根地址改为 https://tw.ncsoft.com/aion2，带 characterId、serverId、lang=en，无 Global region 参数。

社区旧文档 [go2fofo/aion2-portal](https://github.com/go2fofo/aion2-portal/blob/main/docs/api-specification.md)记录过更长的 TW 搜索路由；本轮那个旧路由返回 404。**接口接入应以当前实测为准，不能只照抄历史文档。**

### characterId 的编码

搜索结果的 ID 可能已经带 %3D。构造后续 URL 时需要规范化一次再进行 URL 编码，避免变成 %253D。复现脚本采用 unquote 后交给 urlencode，实际响应已验证。不同 serverId / region 下不能随意复用一个 ID。

## 四、哪些字段值得用

| 响应模块 | 可用字段示例 | 能做什么 | 不能由它推出什么 |
|---|---|---|---|
| profile | characterLevel、className、combatPower、race/server | 角色头部、职业和阶段筛选 | 完整战斗 DPS、账号总资产 |
| stat.statList | type、name、value、二级列表 | 已公开属性展示；按 type 归一 | 仅凭低级角色的 0 值推断所有高阶属性 |
| equipmentList / 单件详情 | ID、槽位、强化；mainStats/subStats等 | 装备卡、属性对比 | 每条随机词条在所有等级都有一样的范围 |
| item 模板 | grade、equipLevel、maxEnchantLevel、sources、主/副属性 | 推荐装备资料、条件解释 | 实时价格、真实掉落概率 |
| skillList | ID、name、category、needLevel、skillLevel、equip/acquired | 角色当前技能配置 | 全等级倍率/CD/目标数与触发公式 |
| nodeList | boardId/nodeId、row/col、open、type、effectList | 节点位置、效果、已开状态 | 225 条都是可加点的有效节点 |
| petwing | pet、wing、wingSkin | 数据存在时展示配置 | null 时补造名称或属性 |
| rankingList / season | 本轮为空 | 处理暂不可用状态 | 全服官方实时排名 |

数值不全是数字类型。物品字段可能有字符串 "4"、"6"、"5%"，范围由 minValue/value 共同表达。不要直接 parseInt 导致百分比或小数丢失。也不要把 maxEnchantLevel 误写成当前强化等级。

本轮 Global 角色是低级样本，stat 多项为 0；0 本身可能是合法数据，不能统一转成“接口坏了”。输出需区分缺字段、null、0、空数组及不适用。

## 五、几个已观察到的失效方式

| 情况 | 本轮证据 | 处理建议 |
|---|---|---|
| HTTP 200 但非 JSON | KR 两个请求返回错误 HTML | 检查 Content-Type、JSON 解析与结构；不当成功 |
| HTTP 200 但无有效物品 | Global 使用 TW 样例 ID，返回 id=0、空模板 | 要求返回 ID 与请求匹配，名称/关键字段有效 |
| 排名路由有响应但无榜 | Global EU / TW 的本轮参数均 []、season=null | 展示暂不可用；保留旧快照日期，不能叫实时 |
| 请求参数变更 | Global 搜索必须 localeInfo；TW 搜索加 race | 保留地区适配器，单独验证参数 |
| 超时 | TW 真实装备模板请求一次超时 | 有缓存时显示更新时间；不无限重试或填 0 |
| 地址迁移 | DBAion2 10-02 公告称刚修复 Global 搜索 | 接入要有维护预算与监测，页面不直接依赖实时上游 |

[DBAion2 更新日志](https://www.dbaion2.online/en/site-news/)与[开源 Daeva 项目](https://github.com/Othmane-ElAlami/Daeva)也提供了上游变化/榜单不可用的独立线索。Daeva 的缓存/历史快照/明确不可用状态值得参考；本轮没有把它或 Shugo 的内部接口当可自由使用的公共数据服务。

## 六、建议的数据层

这是待实施的设计，不是已经完成的网站接入。

```text
官方来源 / 同区验证资料
        ↓
按 Global / TW / KR 分开的适配器
        ↓
原始快照 + 时间 + 来源 + 哈希
        ↓
内容有效性 / 属性单位 / 地区核验
        ↓
缓存与标准化数据
        ↓
攻略数值卡 / 官方术语 / 装备对比
```

最小记录示例：

```json
{
  "itemId": 110160001,
  "service": "Global",
  "shard": "eu",
  "locale": "en-US",
  "enchantLevel": 0,
  "version": null,
  "fetchedAt": "<实际采集时间>",
  "sourceUrl": "<精确官方请求URL>",
  "state": "live",
  "name": "Worn Greatsword",
  "stats": [
    {
      "statId": "WeaponFixingDamage",
      "unit": "points",
      "min": 4,
      "max": 6,
      "rawMin": "4",
      "rawValue": "6"
    }
  ]
}
```

需要保留 region/itemId/enchantLevel/locale 的组合身份；相同 ID 在不同地区不直接合并。当前版本未知时 version=null，页面写明核验日期。模板、某角色具体穿戴物品与玩家推荐 build 也分别保存，避免随机词条覆盖模板。

建议刷新与节流值属于**本站初始工程选择**，不是官方配额：

- 常规物品/职业目录先缓存约 24 小时；补丁后对实际被攻略引用的少量数据再核验。
- 角色查询按需触发，初始缓存约 15–60 分钟，同一请求去重。
- 初期并发 1，约 0.5–1 请求/秒；遇 429 或失败立即降低/停止，尊重服务返回的指令。
- 社区 Go 客户端默认 5 requests/s **不是官方允许额度**，不要照此推导批量抓取权。
- live/cached/stale/unavailable/invalid 分别显示；离线旧快照不能写“实时”。
- 玩家页面不直接发出几十个上游请求；服务端汇总/缓存，避免首屏依赖上游稳定性。

尚未确认的数据使用与图像再分发条件，需要在批量长期使用前单独核实。本文不把“匿名请求成功”写成“官方已授权任何用途”。

## 七、最小可行产品顺序

1. **20–50 件 Global 常用装备资料**：来自已有攻略，先验证四语言模板与属性显示。
2. **2–3 篇现有 build 攻略内嵌数值卡**：附来源、地区、采集时间、条件与替换理由。
3. **角色导入 + 属性差异比较**：当前实测字段足够做基础版；高阶词条和推荐逻辑仍需实测。
4. **再补节点、制作、强化资料**：先把数据含义核清，尤其概率/保底/价格。
5. **有样本后再做统计**：显示样本量、采集窗口和地区；当前官方空榜不作为启动依赖。

第一版验收：有效 ID；+0 与强化值不混；攻击范围与百分比正确；四语言名称可复核；地区/更新时间可见；上游失败不造数。无需先建出全量公开物品内页。

复现脚本：[probe_official_web_api.py](probe_official_web_api.py)、[probe_item_and_board_details.py](probe_item_and_board_details.py)。脚本保留最初失败请求及修正后的响应；已有 capture 不覆盖，复测用新的标签或新的日期目录。

