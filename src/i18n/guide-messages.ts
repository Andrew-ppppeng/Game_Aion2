import type {Locale} from './routing';

const en = {
  enlarge: 'Enlarge image', close: 'Close image', illustration: 'Guide diagram', next: 'Your next step',
  contents: 'Contents', reset: 'Reset checklist', complete: 'completed',
  checklistNote: 'Your checklist is saved in this browser.',
  swipe: 'Swipe or scroll sideways to see the full table', filter: 'Choose your main role',
  classNote: 'Choose a role you enjoy. Classes can fulfil more than one role.',
  all: 'Show all', frontline: 'Frontline', melee: 'Melee damage', ranged: 'Ranged damage', healing: 'Healing & recovery', support: 'Melee support',
  faction: 'Choose a faction route', elyos: 'Elyos', asmodians: 'Asmodians', region: 'Filter server region',
  eu: 'Europe', naWest: 'NA West', naEast: 'NA East', latam: 'South America', asia: 'Asia',
  roster: 'Official class portraits', inspect: 'Compare roles below',
  iconTable: 'Eight Global class icons', classIcon: 'Class icon', englishName: 'English name', localName: 'Class name',
  iconNote: 'Match each class to its emblem. Select an icon to enlarge it.',
};
type GuideMessages = {[K in keyof typeof en]: string};

export const guideMessages = {
  en,
  ja: {
    enlarge: '画像を拡大', close: '画像を閉じる', illustration: 'ガイドの説明図', next: '次のステップ',
    contents: '目次', reset: 'チェックをリセット', complete: '完了',
    checklistNote: 'チェック内容はこのブラウザーに保存されます。',
    swipe: '左右にスクロールすると表全体を確認できます', filter: '主に担当したい役割を選ぶ',
    classNote: '好きな役割を基準に選びましょう。複数の役割をこなせるクラスもあります。',
    all: 'すべて表示', frontline: '前衛', melee: '近接攻撃', ranged: '遠距離攻撃', healing: '回復・蘇生', support: '近接サポート',
    faction: '種族の育成ルートを選ぶ', elyos: '天族', asmodians: '魔族', region: 'サーバー地域で絞り込む',
    eu: 'ヨーロッパ', naWest: '北米西部', naEast: '北米東部', latam: '南米', asia: 'アジア',
    roster: '公式クラスイラスト', inspect: '本文で役割を比較する',
    iconTable: 'Global版の8クラスのアイコン', classIcon: 'クラスアイコン', englishName: '英語名', localName: '日本語名',
    iconNote: 'クラス名と紋章を照合できます。アイコンを選ぶと拡大表示されます。',
  },
  es: {
    enlarge: 'Ampliar imagen', close: 'Cerrar imagen', illustration: 'Diagrama de la guía', next: 'Tu siguiente paso',
    contents: 'Índice', reset: 'Reiniciar lista', complete: 'completados',
    checklistNote: 'La lista se guarda en este navegador.',
    swipe: 'Desliza o desplázate horizontalmente para ver toda la tabla', filter: 'Elige tu función principal',
    classNote: 'Elige una función que disfrutes. Una clase puede cumplir varias funciones.',
    all: 'Mostrar todo', frontline: 'Primera línea', melee: 'Daño cuerpo a cuerpo', ranged: 'Daño a distancia', healing: 'Curación y recuperación', support: 'Apoyo cuerpo a cuerpo',
    faction: 'Elige la ruta de tu facción', elyos: 'Elios', asmodians: 'Asmodianos', region: 'Filtrar región del servidor',
    eu: 'Europa', naWest: 'Norteamérica oeste', naEast: 'Norteamérica este', latam: 'Sudamérica', asia: 'Asia',
    roster: 'Ilustraciones oficiales de las clases', inspect: 'Compara las funciones en la guía',
    iconTable: 'Iconos de las ocho clases de Global', classIcon: 'Icono de clase', englishName: 'Nombre en inglés', localName: 'Nombre en español',
    iconNote: 'Relaciona cada clase con su emblema. Selecciona un icono para ampliarlo.',
  },
  de: {
    enlarge: 'Bild vergrößern', close: 'Bild schließen', illustration: 'Schaubild zum Guide', next: 'Dein nächster Schritt',
    contents: 'Inhalt', reset: 'Checkliste zurücksetzen', complete: 'erledigt',
    checklistNote: 'Die Checkliste wird in diesem Browser gespeichert.',
    swipe: 'Seitlich wischen oder scrollen, um die ganze Tabelle zu sehen', filter: 'Wähle deine bevorzugte Hauptrolle',
    classNote: 'Wähle eine Rolle, die dir Spaß macht. Klassen können mehrere Rollen übernehmen.',
    all: 'Alle anzeigen', frontline: 'Frontlinie', melee: 'Nahkampfschaden', ranged: 'Fernkampfschaden', healing: 'Heilung und Erholung', support: 'Nahkampfunterstützung',
    faction: 'Wähle den Levelweg deiner Fraktion', elyos: 'Elyos', asmodians: 'Asmodier', region: 'Serverregion filtern',
    eu: 'Europa', naWest: 'NA West', naEast: 'NA Ost', latam: 'Südamerika', asia: 'Asien',
    roster: 'Offizielle Klassenillustrationen', inspect: 'Rollen im Guide vergleichen',
    iconTable: 'Symbole der acht Global-Klassen', classIcon: 'Klassensymbol', englishName: 'Englischer Name', localName: 'Deutscher Name',
    iconNote: 'Ordne jeder Klasse ihr Symbol zu. Wähle ein Symbol aus, um es zu vergrößern.',
  },
} satisfies Record<Locale, GuideMessages>;
