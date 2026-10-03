# AION 2 数据接入与维护

核对日期：2026-10-03。适用版本：Global；官网未提供这些数值的游戏版本号，保留 `gameVersion: null`。KR/TW 数据不用于 Global 数值回退。

来源是官方网页使用的公开接口；没有独立开发者 API 或 SLA 的证明。接口结构若变化，停止解析并显示暂不可用，不能靠猜测补齐游戏事实。

## 当前内容

- 22 件装备：20 件高等级角色上的例子，另有公开角色上观察到的入门钉锤和法杖。所有物品均逐一取得英、日、西、德响应；NA East、NA West、EU、LATAM 的数值一致。
- Asia 的装备模板请求 `region=as` 返回 HTTP 200 空响应，不能解析成有效物品。区域验证结果保存为 `valid: false`；工具显示该区域模板未核实。未知区域值会被上游默认为其他区域，禁止使用 `asia` 等猜测别名。
- 五个 Global 区域的服务器、职业和 pcData 元数据；公开角色的职业、等级、战力、军团、装备、属性、技能配置、称号、成长面板、宠物和翅膀，以官方实际返回为准。
- 人工核对的活动记录：10 月 5 日维护、War for Atreia 三轮 Drops、兑换码期限、时空裂缝待核实状态。第二、三轮 Drops 只有日期，没有准确时刻，不能生成倒计时或日历。没有固定 Global 裂缝时间表时保持待核实。
- 角色收藏和素材计划保存在本机浏览器。素材预算由玩家输入数量、已有数量、单价、每次手续费与产出；向上取整计算次数，不设定成功率、保底或市场价格。

装备比较支持同类别的当前模板与候选模板，两侧独立选择强化等级，初始均为 +0。只比较相同属性 ID、可解释单位的主属性；范围值分两端比较，百分比差使用百分点。强化额外值只加一次。随机属性候选池、实际装备随机值和突破属性不会混入这个固定属性差，不预测总战力、DPS 或治疗量。

## 配置与部署

环境变量见 `.env.example`：

```text
NEXT_PUBLIC_SITE_URL=https://aion2wiki.space
UPSTASH_REDIS_REST_URL=...
UPSTASH_REDIS_REST_TOKEN=...
```

Upstash URL/token 仅由服务端读取，不能使用 `NEXT_PUBLIC_` 前缀。Vercel Marketplace 自动注入的 `KV_REST_API_URL` 和 `KV_REST_API_TOKEN` 也受支持，无需复制或重命名密钥。本地未配置 Redis 时允许有容量上限的进程内缓存；Vercel 未配置或 Redis 故障时，动态角色查询返回可理解的暂不可用提示和官方入口，禁止退回各实例无限发请求。静态攻略、装备卡片、计时器和预算继续可用。

现有 Vercel 项目为 `game-aion2`。首次安装 Upstash 时，Vercel CLI 返回 `integration_terms_acceptance_required`，必须由账号持有人接受条款；代码或自动化不能代替这一动作。2026-10-03 用户确认已接受，已创建免费的 `upstash/upstash-kv`，资源名 `aion2-data-cache`，主区域 `iad1`，关闭 `autoUpgrade` 和 `prodPack`，连接 Development/Preview/Production 环境。密钥只保存在平台及已忽略的本地环境文件中，不能进入上传目录。验证和预览后再发布正式版本。

预览环境 robots.txt 禁止整站抓取；正式环境禁止 `/api/` 抓取。工具的纯路径可收录，带角色 ID 等查询参数的结果页使用 noindex，并 canonical 到纯工具路径。API 返回 `private, no-store` 和 `X-Robots-Tag`；避免搜索引擎收录公开玩家结果和参数页。

本机 Vercel CLI 61.1.0 的 archive 模式未按 dry-run 的排除清单打包，因此先生成 `.qa/deploy-inputs.json`，再运行 `python scripts/stage-vercel-preview.py`。只部署输出的隔离目录，核对上传源文件数量，禁止直接从含研究档案和本地凭据的工作区使用 archive 模式。

## API 与缓存

浏览器只访问本站 `/api/aion2/*`；服务端只请求固定官方主机，不接收任意来源 URL。

| 本站路由 | 用途 | 缓存 |
| --- | --- | --- |
| `/api/aion2/meta?region=nae&locale=en` | 服务器、职业、pcData | 24 小时；可用旧数据 14 天，失败用人工快照 |
| `/api/aion2/characters/search?q=…&region=…` | 名称搜索，可加 serverId/class/page | 1 分钟，每页 20，页码最多 500 |
| `/api/aion2/characters/{id}?serverId=…&region=…` | 基础信息和已装装备 | 15 分钟；故障时最多多保留 45 分钟 |
| `/api/aion2/characters/{id}/equipment/{slot}?serverId=…` | 实际实例属性 | 15 分钟；故障时最多多保留 45 分钟 |
| `/api/aion2/items/{id}?enchantLevel=0&region=…` | 固定装备模板 | 24 小时，旧数据再保留 24 小时；已核实 +0 可回退快照 |
| `/api/aion2/events?topic=maintenance` | 人工核对的活动时刻 | 本地内容，随部署更新 |

物品 ID 必须属于人工物品库，或当前正在查看的公开角色的实际装备；不开放任意 ID 枚举。地区仅接受 `nae,naw,eu,la,as`，语言仅接受 `en,ja,es,de`。角色 ID、服务器、名称长度、物品与强化参数均在服务端校验，官方返回也校验结构后才进入页面。

同进程 Promise 与 Redis 每键锁合并重复请求；跨实例共用上游锁，每次完成后至少隔一秒再请求。超时 8 秒，上游 403/429 触发至少 60 秒全站暂停；失败不循环请求。角色、实例、模板端点共用每个 IP 每分钟 30 次请求限额。IP 只用于散列缓存键，不写入日志。日志只有成功/错误类型和耗时，无玩家名、ID 或 token。

免费 Redis 有容量和命令配额。查询缓存、锁、限额检查都会消耗命令，不能将命令配额等同于玩家访问次数。关闭自动付费升级；后续根据真实日志和 Upstash 配额面板调整 TTL/流量策略。

实时数据 API 的 `meta` 保存 Global 地区、语言、官方来源、实际取得时间、版本与新鲜度。取得时间不是游戏内同步时间。人工活动 API 使用 checkedAt 核对日，每条活动带独立来源。旧数据标注为 stale，404/参数错误不回退旧角色数据。

## 采集与更新

```sh
python scripts/collect-aion2-data.py
```

采集器只查询明列的 22 个已观察物品，5 区域 × 4 语言，同时采集元数据和活动原文。每次建立新的 `research/api/YYYY-MM-DD/run-*` 目录，保存响应 body、URL、HTTP 状态、取得时间、内容类型和 SHA-256。原始文件不会覆盖。全部采集及数值冲突检查通过后才原子更新发布快照；Asia 空响应保留为未核实。

`events.json` 是人工维护的 UTC 记录，不由公告文本自动猜测时刻。新增/修改时：核对原文日期和时区，归档正文，记录 checkedAt、来源和适用区域；未给准确时间时使用 null。时区显示使用浏览器 IANA 时区数据库，日历使用 UTC，收藏/领取提醒不读取游戏账户。

首次模板采集证据在 `research/api/2026-10-03/run-061041-335900/`；两件入门武器和真实公开角色测试响应在 `run-064112-135367/`。`tests/fixtures/` 保存离线 UI 验证所需的公开响应，不能作为实时角色资料。

新角色未装备称号、宠物或翅膀时，官方会在对应槽位返回 null；这是合法空槽位，不能将整个角色判为无效。亚洲区新角色的原文证据保存在 `research/api/2026-10-03/run-141318-448617/`，回归样本在 `tests/fixtures/asia-new-character-*`。五地区公开角色基础资料与装备列表、四语言角色资料、真实装备详情和强化模板已做线上实测；亚洲模板空响应的限制仍单独保留。

## 验证

```sh
npm run check
npm run test:content
npm run test:data
npm run build
npm run start
# 在另一个终端中
npm run test:smoke
npm run test:browser
npm run test:tools
npm run test:api
```

Node.js 22.17+ 支持数据测试使用的 TypeScript 类型擦除；部署项目使用 Node 24。`test:data` 检查源数值、结构异常、比较单位、UTC 边界、日历、预算、重复请求合并和 Redis 故障。`test:tools` 使用归档公开响应验证四语言、手机/桌面、地区/职业过滤、收藏、默认比较、日历、待核实时刻、本地存储受限时仍可预算。`test:api` 是人工触发的有限官方联通检查，验证五区域搜索、实际装备、+0/+1 与缓存；不用于频繁 CI 轮询。

真实共享缓存检查：`node --conditions=react-server --experimental-strip-types --env-file=.env.development.local scripts/cache-live-check.mjs`。验证跨实例请求合并、原子请求限额和全站请求间隔，测试键 60 秒内过期。

保护中的 Vercel 预览 API 检查：设置 `QA_VERCEL_DEPLOYMENT` 为部署 URL 后执行 `npm run test:api`。脚本使用已登录的 Vercel CLI 请求，自动验证四语言公开角色、五区域搜索、来源时间复用、实际装备、强化模板和错误状态；不打印凭据。Windows 默认查找全局安装的 CLI，其他安装位置可指定 `VERCEL_CLI_PATH`。
