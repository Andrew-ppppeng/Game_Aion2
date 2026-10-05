import json
import urllib.parse
from collect_public_evidence import capture, RAW
from probe_official_web_api import first_character, summary

def probe(label, origin, path, query):
    meta=capture((label,origin+path+'?'+urllib.parse.urlencode(query),'json'))
    print(json.dumps(summary(meta),ensure_ascii=False),flush=True)
    return meta

for region, origin, lang, shard in [('global-eu','https://aion2.plaync.com','en-US','eu'),('tw','https://tw.ncsoft.com/aion2','en','')]:
    hit=first_character(json.loads((RAW/('api-'+region+'-search-corrected.body')).read_text(encoding='utf-8')))
    character={'characterId':urllib.parse.unquote(hit['characterId']),'serverId':hit['serverId'],'lang':lang}
    if shard: character['region']=shard
    equip=json.loads((RAW/('api-'+region+'-equipment.body')).read_text(encoding='utf-8'))['equipment']['equipmentList'][0]
    prefix='/en-us' if shard else ''
    probe('api-'+region+'-item-from-equipment',origin,prefix+'/api/gameconst/item',{'id':equip['id'],'enchantLevel':0,'lang':lang})
    probe('api-'+region+'-equipped-item-detail',origin,'/api/character/equipment/item',dict(character,id=equip['id'],enchantLevel=equip['enchantLevel'],slotPos=equip['slotPos']))
    profile=json.loads((RAW/('api-'+region+'-info.body')).read_text(encoding='utf-8'))
    board=profile['daevanion']['boardList'][0]
    probe('api-'+region+'-board-detail',origin,'/api/character/daevanion/detail',dict(character,boardId=board['id']))
    probe('api-'+region+'-ranking',origin,'/api/ranking/list',{'rankingContentsType':1,'rankingType':0,'serverId':hit['serverId'],'lang':lang,**({'region':shard} if shard else {})})
    if shard:
        for locale in ['de-DE','es-ES','ja-JP']:
            probe('api-global-item-'+locale.lower(),origin,'/'+locale.lower()+'/api/gameconst/item',{'id':equip['id'],'enchantLevel':0,'lang':locale})
