"""Final manual editorial corrections; keep original anchors as aliases."""
from pathlib import Path
import json,re
from author_articles import ROOT,LOCALES

answers = {
 'gathering': [
  'For one starter sword attempt, gather 6 Orichalcum Ore and 2 Odyle, buy 3 Solvent and collect 5 Refining Stones. Specialize in Odyle plus your recipe resource. At Novice 50, Asmodians complete Alzirr’s Ruby promotion in Safe Haven.',
  '初期の剣1回分はOrichalcum Ore 6、Odyle 2を採集、Solvent 3を購入、Refining Stone 5を入手。Odyleと製作資源に特化し、魔族はNovice 50でSafe HavenのAlzirrのRuby昇級を完了します。',
  'Para una espada inicial, recoge 6 Orichalcum Ore y 2 Odyle, compra 3 Solvent y consigue 5 Refining Stones. Especializa Odyle y el recurso de tu receta. En Novice 50, Asmodian completa la promoción Ruby de Alzirr en Safe Haven.',
  'Für ein Startschwert 6 Orichalcum Ore und 2 Odyle sammeln, 3 Solvent kaufen und 5 Refining Stones holen. Odyle und Rezeptmaterial spezialisieren. Asmodier erledigen auf Novice 50 Alzirrs Ruby-Aufstieg in Safe Haven.'],
 'macro-guide': [
  'Bind the ability-macro key under Key Settings → General → Gameplay, select the whole hotbar chain and hold the key. The bottom skill has priority; place filler above conditional attacks. Keep healing, movement and interrupts on direct keys.',
  'Key Settings → General → Gameplayでマクロキーを設定し、ホットバーの連鎖全体を選んで長押し。最下段が優先なので埋め技は条件付き攻撃の上へ。回復・移動・中断は直接キーに残します。',
  'Asigna la tecla en Key Settings → General → Gameplay, selecciona toda la cadena y mantén pulsado. La habilidad inferior tiene prioridad: pon el relleno encima de ataques condicionales. Curación, movimiento e interrupción van separados.',
  'Makrotaste unter Key Settings → General → Gameplay belegen, ganze Hotbar-Kette wählen und Taste halten. Die unterste Fertigkeit hat Vorrang; Füller über bedingten Angriffen anordnen. Heilung, Bewegung und Unterbrechen direkt belegen.']}

for slug in ['settings','gear-progression','daily-weekly-checklist','crafting','guide','leveling','gathering','macro-guide']:
 for i,locale in enumerate(LOCALES):
  p=ROOT/f'src/content/{locale}/{slug}.json';m=json.loads(p.read_text(encoding='utf-8'))
  b=p.with_suffix('.mdx');body=b.read_text(encoding='utf-8')
  # Actual UI figures and task tables replace redundant summary diagrams.
  if slug in ['settings','gear-progression','daily-weekly-checklist','guide','leveling']:
   body=body.replace('\n\n<GuideVisual id="workflow" />','');m['visuals'].pop('workflow',None)
  if slug in answers:m['quickAnswer']=answers[slug][i]
  if slug=='gathering':m['summary']=['Exact starter materials, a gathering allocation and the Asmodian Novice-50 Ruby promotion.','初期素材の数量、採集配分、魔族のNovice 50 Ruby昇級。','Materiales iniciales, puntos de recolección y promoción Ruby Asmodian en Novice 50.','Startmaterialien, Sammelpunkte und Asmodier-Ruby-Aufstieg auf Novice 50.'][i]
  old=json.loads((Path(__file__).parent/f'before/src/content/{locale}/{slug}.json').read_text(encoding='utf-8'))
  ids={x['id'] for x in m['toc']}
  missing=[x['id'] for x in old['toc'] if x['id'] not in ids]
  if missing:
   target={'guide':'skills-and-gear','leveling':'leveling-blockers','gathering':'gathering-routes'}.get(slug,m['toc'][-1]['id'])
   aliases='\n'.join(f'<span id="{id}" />' for id in missing)
   body=body.replace(f'<h2 id="{target}"',aliases+f'\n\n<h2 id="{target}"',1)
  p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');b.write_text(body,encoding='utf-8')
print('Removed redundant diagrams, refined quick answers and retained previous section anchors.')
