# AION2 永恒之塔2 公共接口文档 (API Specification)

本文档记录了对接 NCSoft 官方 AION2 台湾服务器的公共数据接口规范。

## 1. 角色查询列表 (Search)

用于通过角色名模糊或精确匹配，获取角色的唯一标识符 `characterId`。

- **请求网址**: `https://tw.ncsoft.com/aion2/api/search/aion2tw/search/v2/character`
- **请求方法**: `GET`
- **请求参数**:
  - `keyword`: 角色名称 (例如: `fofoooooo`)
  - `serverId`: 服务器 ID (例如: `2015`)
  - `race`: 种族代码 (1: 天族, 2: 魔族)
  - `page`: 分页页码
  - `size`: 每页显示数量

### 返回数据示例

```json
{
    "list": [
        {
            "characterId": "chQWw6n1ntmlSG4TAezufiyCeShvn5mCJa-IZ4GG7Hs%3D",
            "name": "fofoooooo",
            "race": 2,
            "level": 45,
            "serverId": 2015,
            "serverName": "簡卡卡",
            "profileImageUrl": "..."
        }
    ]
}
```

---

## 2. 查询角色基本信息 (Profile & Stats)

获取角色的职业、性别、详细属性值、各玩法排名以及称号数据。

- **请求网址**: `https://tw.ncsoft.com/aion2/api/character/info`
- **请求方法**: `GET`
- **请求参数**:
  - `characterId`: 角色加密 ID
  - `serverId`: 服务器 ID
  - `lang`: 语言 (例如: `zh`)

### 核心数据模块

1. **Profile**: 包含职业 (`className`)、等级、性别等基础信息。
2. **Stat**: 包含基础属性 (STR/DEX/INT/CON/AGI/WIS) 及十二主神加成的特殊属性。
3. **Ranking**: 包含深渊、恶梦、竞技场等内容的排名数据。
4. **Title**: 包含已获得和已装备的称号及其属性加成。

---

## 3. 查询角色装备与技能 (Equipment & Skills)

获取角色当前穿着的装备细节、宠物、翅膀以及技能配置。

- **请求网址**: `https://tw.ncsoft.com/aion2/api/character/equipment`
- **请求方法**: `GET`
- **请求参数**: 同上

### 核心数据模块

1. **Skill**: 包含主动 (`Active`)、被动 (`Passive`) 及 DP 技能的等级与装备状态。
2. **Equipment**: 包含所有部位装备的名称、强化等级 (`enchantLevel`)、品质 (`grade`) 及对应图标。
3. **PetWing**: 当前使用的宠物 (`pet`) 信息、翅膀 (`wing`) 及其外形皮肤 (`wingSkin`)。
4. **SkinList**: 角色当前应用的所有时装外形。

---

## 💡 开发说明

- **ID 获取**: 必须先调用 `search` 接口拿到 `characterId`，才能请求后续详情。
- **资源路径**: 文档中返回的图标链接（如 `Icon_WP_ST_...`）均指向 `assets.playnccdn.com`。
- **接口权限**: 该文档基于 NCSoft 官方公开 API，建议在请求头中携带正确的 `User-Agent` 与 `Referer` 以保证请求稳定性。
