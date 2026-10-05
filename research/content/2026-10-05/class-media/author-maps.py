import json
from pathlib import Path

root = Path(__file__).parent
out = Path('src/content')
def tr(en,ja,es,de): return dict(en=en,ja=ja,es=es,de=de)
def row(sources,targets,kind,caption): return dict(sources=sources,targets=targets,kind=kind,caption=caption)
def state(labels): return dict(label=labels)
crit=state(tr('Critical hit','クリティカルヒット','Golpe crítico','Kritischer Treffer'))
stagger=state(tr('Staggered target','対象がグロッギー','Objetivo en Stagger','Ziel in Stagger'))
maps={
 'gladiator':[
  row(['11020000'],['11100000'],'specialization',tr('Skill rank 12 • select cooldown reduction • land a hit','スキルLv12・クールタイム短縮を選択・攻撃を命中させる','Rango 12 • selecciona reducción de enfriamiento • acierta','Fertigkeitsrang 12 • Abklingzeitverkürzung wählen • treffen')),
  row(['11290000'],['11170000'],'trigger',tr('Knockdown opens the follow-up; immune targets use their proc','ノックダウンで追撃可能。無効な対象には専用の発動条件','Derribo activa el seguimiento; los inmunes usan su activación','Niederschlag ermöglicht den Folgeangriff; immune Ziele nutzen ihren Auslöser')),
  row([stagger],['11280000'],'trigger',tr('Use during the target’s Stagger window','対象のグロッギー中に使用','Usa durante la ventana de Stagger','Während des Stagger-Fensters einsetzen')),
 ],
 'templar':[
  row(['12100000','12350000'],['12240000'],'trigger',tr('Either shield attack → Judgment within 2 seconds','どちらかの盾攻撃 → 2秒以内に追撃','Cualquiera de los dos ataques → Judgment en 2 segundos','Einer der Schildangriffe → Judgment innerhalb von 2 Sekunden')),
  row(['12040000'],['12090000'],'specialization',tr('Skill rank 12 • select cooldown reduction • land a hit','スキルLv12・クールタイム短縮を選択・攻撃を命中させる','Rango 12 • selecciona reducción de enfriamiento • acierta','Fertigkeitsrang 12 • Abklingzeitverkürzung wählen • treffen')),
  row([state(tr('Successful block','ブロック成功','Bloqueo exitoso','Erfolgreicher Block'))],['12270000'],'trigger',tr('Block opens the defense-reducing follow-up','ブロック後に防御低下の追撃が可能','El bloqueo activa el seguimiento que reduce defensa','Block ermöglicht den Folgeangriff mit Verteidigungssenkung')),
 ],
 'assassin':[
  row(['13100000'],['13130000'],'trigger',tr('Build Insignia on the same target • up to 5 stacks','同じ対象に刻印を蓄積・最大5スタック','Acumula Insignia en el mismo objetivo • hasta 5 cargas','Insignia auf demselben Ziel aufbauen • bis zu 5 Stapel')),
  row([crit],['13350000'],'trigger',tr('React to the critical-hit opportunity','クリティカル発生時の追撃機会に反応','Reacciona a la oportunidad tras un crítico','Auf die Gelegenheit nach einem kritischen Treffer reagieren')),
  row(['13010000'],['13130000'],'specialization',tr('Skill rank 12 • select cooldown reduction • land a hit','スキルLv12・クールタイム短縮を選択・攻撃を命中させる','Rango 12 • selecciona reducción de enfriamiento • acierta','Fertigkeitsrang 12 • Abklingzeitverkürzung wählen • treffen')),
 ],
 'ranger':[
  row(['14090000'],['14070000','14010000'],'trigger',tr('Precision enables Suppressing Arrow and boosts Deadshot','精密で制圧矢が使用可能・狙撃の威力上昇','Precision activa Suppressing Arrow y mejora Deadshot','Precision ermöglicht Suppressing Arrow und verstärkt Deadshot')),
  row(['14130000'],['14080000'],'trigger',tr('Slow or Root must be active on the target','対象がスロウまたはルート状態であること','El objetivo debe tener ralentización o inmovilización','Verlangsamung oder Wurzel muss auf dem Ziel aktiv sein')),
  row([crit],['14050000'],'trigger',tr('A critical hit opens Drill Dart; its own crit restores MP','クリティカルで発動。自身もクリティカルならMP回復','Un crítico activa Drill Dart; su propio crítico recupera MP','Kritischer Treffer ermöglicht Drill Dart; sein eigener kritischer Treffer stellt MP her')),
 ],
 'chanter':[
  row(['18060000','18290000'],['18100000'],'trigger',tr('Either attack → Dark Crush within 2 seconds','どちらかの攻撃 → 2秒以内に追撃','Cualquiera de los dos ataques → Dark Crush en 2 segundos','Einer der Angriffe → Dark Crush innerhalb von 2 Sekunden')),
  row(['18010000'],['18290000'],'specialization',tr('Skill rank 12 • select cooldown reduction • land a hit','スキルLv12・クールタイム短縮を選択・攻撃を命中させる','Rango 12 • selecciona reducción de enfriamiento • acierta','Fertigkeitsrang 12 • Abklingzeitverkürzung wählen • treffen')),
  row([state(tr('Successful parry','パリィ成功','Desvío exitoso','Erfolgreiche Parade'))],['18150000'],'trigger',tr('Parry opens the follow-up; a selected Rushing Smash option also triggers it','パリィ後に追撃可能。接近技の発動特化を選んだ場合も使用可能','El desvío activa el seguimiento; una opción elegida de Rushing Smash también lo activa','Parade ermöglicht den Folgeangriff; eine gewählte Rushing-Smash-Option löst ihn ebenfalls aus')),
 ],
 'cleric':[
  row(['17070000'],['17350000'],'trigger',tr('Chain of Torment must be active on this target','同じ対象に苦痛の連鎖が付与されていること','Chain of Torment debe estar activo en este objetivo','Chain of Torment muss auf diesem Ziel aktiv sein')),
  row([crit],['17350000'],'specialization',tr('Condemnation crit • selected rank-12 reset • keep Chain of Torment active','追撃のクリティカル・Lv12のリセット特化を選択・苦痛の連鎖を維持','Crítico de Condemnation • reinicio de rango 12 elegido • mantén Chain of Torment','Condemnation-Krit • gewählter Reset auf Rang 12 • Chain of Torment aufrechterhalten')),
  row([state(tr('Party takes damage + a removable debuff','味方の被ダメージ＋解除可能なデバフ','Daño de grupo + perjuicio eliminable','Gruppenschaden + entfernbarer Debuff'))],['17120000'],'response',tr('Heal the party and remove one debuff with the base skill','基本効果でパーティーを回復し、デバフを1個解除','La habilidad base cura al grupo y elimina un perjuicio','Die Grundfertigkeit heilt die Gruppe und entfernt einen Debuff')),
 ],
 'sorcerer':[
  row(['15210000','15710000'],['15050000'],'trigger',tr('Flame Arrow applies Fire Mark through the passive → Blaze','パッシブにより火矢で火の印を付与 → 追撃','Flame Arrow aplica Fire Mark mediante la pasiva → Blaze','Flame Arrow setzt durch die passive Fertigkeit Fire Mark → Blaze')),
  row(['15040000'],['15060000'],'specialization',tr('Skill rank 12 • select cooldown reduction • land a hit','スキルLv12・クールタイム短縮を選択・攻撃を命中させる','Rango 12 • selecciona reducción de enfriamiento • acierta','Fertigkeitsrang 12 • Abklingzeitverkürzung wählen • treffen')),
  row(['15150000'],['15220000'],'trigger',tr('Frost enables the follow-up; immune targets use their proc','凍結で追撃可能。無効な対象には専用の発動条件','Frost activa el seguimiento; los inmunes usan su activación','Frost ermöglicht den Folgeangriff; immune Ziele nutzen ihren Auslöser')),
 ],
 'spiritmaster':[
  row([state(tr('4 spirit-skill activations','精霊スキルを4回使用','4 activaciones de habilidades de espíritu','4 Anwendungen von Geisterfertigkeiten'))],['16300000'],'trigger',tr('Four Elements → spend Fusion before gaining more stacks','四元素 → 融合を使用してから次のスタックを獲得','Four Elements → usa Fusion antes de acumular más cargas','Four Elements → Fusion einsetzen, bevor weitere Stapel gesammelt werden')),
  row(['16100000','16110000','16120000','16130000'],['16330000'],'trigger',tr('A summon or spirit-skill action opens a brief window','召喚または精霊スキル後の短い発動ウィンドウ','Una invocación o acción del espíritu abre una ventana breve','Beschwörung oder Geisteraktion öffnet ein kurzes Fenster')),
  row(['16110000'],[state(tr('MP recovery','MP回復','Recuperación de MP','MP-Regeneration'))],'resource',tr('Water Spirit restores your MP when its attacks land','水の精霊の攻撃命中で本人のMPが回復','Water Spirit recupera tus MP cuando acierta sus ataques','Treffer des Wassergeists stellen deine MP wieder her')),
 ],
}
(out/'class-skill-maps.json').write_text(json.dumps(maps,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
