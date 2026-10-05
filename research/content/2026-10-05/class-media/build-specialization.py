import json
from pathlib import Path
root=Path('src/content')
copy={
 'en': dict(title='Hellfire: one rank threshold, three choices',caption='At skill rank 8, choose one effect for the same specialization slot.',steps=[dict(label='Faster casting',description='Adds 30% skill speed.'),dict(label='Damage over time',description='Adds fire damage over 10 seconds on hit.'),dict(label='Mobile casting',description='Allows movement while casting.')]),
 'ja': dict(title='Hellfire：同じ条件で3種類の選択肢',caption='スキルLv8で、同じ特化枠の効果を1つ選びます。',steps=[dict(label='詠唱を高速化',description='スキル速度が30%上昇。'),dict(label='持続ダメージ',description='命中時に10秒間の火属性持続ダメージ。'),dict(label='移動しながら詠唱',description='詠唱中に移動可能。')]),
 'es': dict(title='Hellfire: un umbral, tres opciones',caption='En rango de habilidad 8, elige un efecto para la misma ranura de especialización.',steps=[dict(label='Lanzamiento más rápido',description='Añade un 30% de velocidad de habilidad.'),dict(label='Daño prolongado',description='Añade daño de fuego durante 10 segundos al acertar.'),dict(label='Lanzamiento en movimiento',description='Permite moverte mientras lanzas.')]),
 'de': dict(title='Hellfire: eine Rangschwelle, drei Optionen',caption='Wähle auf Fertigkeitsrang 8 einen Effekt für denselben Spezialisierungsplatz.',steps=[dict(label='Schnelleres Wirken',description='Erhöht die Fertigkeitsgeschwindigkeit um 30%.'),dict(label='Schaden über Zeit',description='Verursacht bei einem Treffer 10 Sekunden lang Feuerschaden über Zeit.'),dict(label='Wirken in Bewegung',description='Erlaubt Bewegung beim Wirken.')]),
}
for locale in copy:
 path=root/locale/'builds.json'
 data=json.loads(path.read_text(encoding='utf-8'))
 data['visuals']['topic']=dict(specializationTree=True,**copy[locale])
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 path=root/locale/'builds.mdx'
 text=path.read_text(encoding='utf-8').replace('\n\n<GuideSpecializationTree />','')
 path.write_text(text,encoding='utf-8')
