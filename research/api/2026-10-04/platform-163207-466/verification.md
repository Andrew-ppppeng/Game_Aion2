# 官方接口与本地适配链路核验

日期：2026-10-04；Global EU；en-US；gameVersion 未返回。

- 原始装备 +1：`enhancement-1.body` 与 `enhancement-1.meta.json`。官方 URL：`https://aion2.plaync.com/en-us/api/gameconst/item?id=110730048&enchantLevel=1&lang=en-US&region=eu`。200，id/enchantLevel 正确，4 个 mainStats。
- 本地适配链路 `/api/aion2/items/110730048?locale=en&region=eu&enchantLevel=1`：实际访问返回 200、fresh、error=null。
- 本地成长链路 `/api/aion2/characters/[id]/boards/11?serverId=1306&locale=en&region=eu`：使用既有官方公开 EU 角色 ID；实际访问返回 200、225 个经过校验的节点、fresh、error=null。上游 `https://aion2.plaync.com/api/character/daevanion/detail`，角色/服务器/面板/地区/语言参数固定；角色 ID 与原始响应参考 `research/competitive/2026-10-03/raw/api-global-eu-board-detail.meta.json`/`.body`。
- 此核验未补充地图、配方或全量 ID。没有用 TW 数据兜底 Global，没有解析客户端，也没有批量枚举 ID。
- 公开页面不展示本日志、来源分析或 API 来源链接。
