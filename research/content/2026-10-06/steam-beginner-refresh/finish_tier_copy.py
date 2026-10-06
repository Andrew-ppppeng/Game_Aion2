import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
copy = {
 'en': ('Launch ratings', 'Spiritmaster keeps a summoned spirit active and reacts to short follow-up opportunities before they expire. Compare managing those spirit attacks with keeping your own ranged attacks active on Ranger.'),
 'ja': ('開始時の評価', 'スピリット マスターは召喚した精霊を維持し、短い追撃の機会を期限内に使います。精霊の攻撃を管理する操作と、レンジャーで自分の遠距離攻撃を継続する操作を比較してください。'),
 'es': ('Valoraciones iniciales', 'Espiritualista mantiene un espíritu invocado y aprovecha las ventanas breves de ataques siguientes antes de que caduquen. Compara gestionar los ataques del espíritu con mantener tus propios ataques a distancia como Arquero.'),
 'de': ('Startbewertungen', 'Beschwörer hält einen Geist aktiv und nutzt kurze Folgeangriffsfenster, bevor sie ablaufen. Vergleiche die Steuerung der Geistangriffe damit, als Waldläufer eigene Fernkampfangriffe aufrechtzuerhalten.'),
}
for locale, (label, paragraph) in copy.items():
 path = ROOT / f'src/content/{locale}/tier-list.mdx'
 body = path.read_text(encoding='utf-8')
 body = re.sub(r'(<h2 id="spiritmaster-and-ranger">[^\n]+</h2>\n\n)[^\n]+', lambda m: m[1] + paragraph, body)
 rows = body.splitlines()
 first_row = next(i for i, row in enumerate(rows) if row.startswith('|'))
 cells = rows[first_row].split('|'); cells[2] = ' ' + label + ' '; rows[first_row] = '|'.join(cells)
 path.write_text('\n'.join(rows) + '\n', encoding='utf-8', newline='\n')
