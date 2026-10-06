"""Narrow menu claims to checked evidence and keep article introductions short."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
summaries = {
 'settings': {'en': 'Set targeting, potion use, key bindings and visibility, then test the changes in a real encounter.', 'ja': 'ターゲット、ポーション、キー配置、表示を調整し、実際の戦闘で変更を試します。', 'es': 'Ajusta objetivos, pociones, teclas y visibilidad y prueba los cambios en un combate real.', 'de': 'Passe Zielwahl, Tränke, Tasten und Sichtbarkeit an und teste die Änderungen in einem echten Kampf.'},
 'gear-progression': {'en': 'Turn level-45 unlocks and exploration rewards into your next equipment upgrade, keeping gear score and Combat Power separate.', 'ja': '45で開く活動と探索報酬を次の装備更新につなげ、装備スコアと戦闘力を分けて考えます。', 'es': 'Convierte desbloqueos del nivel 45 y exploración en tu próxima mejora, distinguiendo puntuación de equipo y poder de combate.', 'de': 'Nutze Freischaltungen ab Stufe 45 und Erkundungsbelohnungen für das nächste Ausrüstungsupgrade und unterscheide Ausrüstungswert und Kampfkraft.'},
 'daily-weekly-checklist': {'en': 'Plan a short session around Duty, limited activity rewards and event deadlines; check each activity’s own counter.', 'ja': 'Duty、回数制限のある報酬、イベント期限を軸に短いセッションを組み、活動ごとの残り枠を確認します。', 'es': 'Organiza una sesión breve con Duty, recompensas limitadas y plazos de eventos; revisa el contador de cada actividad.', 'de': 'Plane eine kurze Sitzung mit Duty, begrenzten Belohnungen und Eventfristen und prüfe die Zähler jeder Aktivität.'},
 'crafting': {'en': 'Prepare a recipe, match its inputs and binding rules, and compare gathering with purchasing before making your first batch.', 'ja': 'レシピの素材と帰属条件を照合し、採集と購入の費用を比べてから最初の一回を製作します。', 'es': 'Prepara una receta, comprueba materiales y vinculación y compara recolección y compra antes del primer lote.', 'de': 'Bereite ein Rezept vor, gleiche Materialien und Bindungsregeln ab und vergleiche Sammeln und Kaufen vor der ersten Herstellung.'},
}
modes = {
 'en': ('compare the available AION 1 and AION 2 control modes', 'review the available movement and camera controls'),
 'ja': ('AION 1とAION 2の操作モードを比較します', '利用できる移動とカメラの操作設定を確認します'),
 'es': ('compara los modos AION 1 y AION 2', 'revisa los controles disponibles de movimiento y cámara'),
 'de': ('vergleiche AION 1 mit AION 2', 'prüfe die verfügbaren Bewegungs- und Kamerasteuerungen'),
}
upgrade_titles = {'en': 'Preview an equipment upgrade', 'ja': '強化の結果と費用を確認する', 'es': 'Revisa el resultado de la mejora', 'de': 'Vorschau einer Verbesserung prüfen'}
unneeded = {
 'en': ['; it is not a separate game mode', ' This page does not impose an automatic reset or a fixed regional timetable.'],
 'ja': ['で、独立したゲームモードではありません', 'このページでは自動リセットや固定時刻表を設定しません。'],
 'es': ['; no es un modo de juego', ' Esta página no aplica reinicios automáticos ni un horario fijo.'],
 'de': ['; sie ist kein eigener Spielmodus', ' Diese Seite setzt nichts automatisch zurück und gibt keinen festen Zeitplan vor.'],
}
for slug, localized in summaries.items():
 for locale, summary in localized.items():
  body_path = ROOT / f'src/content/{locale}/{slug}.mdx'
  meta_path = ROOT / f'src/content/{locale}/{slug}.json'
  body = body_path.read_text(encoding='utf-8')
  meta = json.loads(meta_path.read_text(encoding='utf-8'))
  meta['summary'] = summary
  if locale == 'en':
   meta['title'] = {'settings': 'AION 2 Settings & Controls', 'gear-progression': 'AION 2 Gear Progression', 'daily-weekly-checklist': 'AION 2 Daily & Weekly Checklist', 'crafting': 'AION 2 Crafting'}[slug]
  if slug == 'settings':
   a, b = modes[locale]
   body = body.replace(a, b)
  if slug == 'gear-progression':
   body = re.sub(r'(<h2 id="growth-and-enhancement">).*?(</h2>)', lambda m: m[1] + upgrade_titles[locale] + m[2], body)
   for section in meta['toc']:
    if section['id'] == 'growth-and-enhancement': section['title'] = upgrade_titles[locale]
  if slug == 'daily-weekly-checklist':
   for text in unneeded[locale]: body = body.replace(text, '')
  body_path.write_text(body, encoding='utf-8', newline='\n')
  meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
