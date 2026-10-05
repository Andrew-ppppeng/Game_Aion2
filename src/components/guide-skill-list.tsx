import skills from '@/content/class-skills.json';
import focus from '@/content/class-skill-focus.json';
import type {Locale} from '@/i18n/routing';
import {GuideTable} from './guide-table';

export type ClassId = keyof typeof skills;
const labels = {
  en: {active: 'Active skills', passive: 'Passive skills', stigma: 'Stigma skills', skill: 'Skill', use: 'Use and trigger', level: 'Character level required', note: 'Learning a Stigma skill does not add an equipped slot. Upgrades use their respective skill or Stigma points; select specializations separately after unlocking them.'},
  ja: {active: 'アクティブスキル', passive: 'パッシブスキル', stigma: 'スティグマスキル', skill: 'スキル', use: '用途と発動条件', level: '必要キャラクターレベル', note: 'スティグマを習得しても装備枠は増えません。強化には対応するスキル・スティグマポイントを使い、特化は解放後に別途選択します。'},
  es: {active: 'Habilidades activas', passive: 'Habilidades pasivas', stigma: 'Habilidades de estigma', skill: 'Habilidad', use: 'Uso y condición', level: 'Nivel de personaje requerido', note: 'Aprender un estigma no añade una ranura equipada. Las mejoras usan puntos de habilidad o estigma; selecciona las especializaciones por separado tras desbloquearlas.'},
  de: {active: 'Aktive Fertigkeiten', passive: 'Passive Fertigkeiten', stigma: 'Stigma-Fertigkeiten', skill: 'Fertigkeit', use: 'Nutzen und Auslösung', level: 'Erforderliche Charakterstufe', note: 'Eine erlernte Stigma-Fertigkeit fügt keinen Ausrüstungsplatz hinzu. Verbesserungen benötigen Fertigkeits- oder Stigma-Punkte; Spezialisierungen gesondert auswählen.'},
};

export function GuideSkillFocus({locale, classId}: {locale: Locale; classId: ClassId}) {
  const m = labels[locale];
  return <div className="class-skill-focus" data-skill-focus={classId}><GuideTable><thead><tr><th scope="col">{m.skill}</th><th scope="col">{m.use}</th></tr></thead>
    <tbody>{focus[classId].map((entry) => {
      const skill = skills[classId].find((item) => item.id === entry.id)!;
      return <tr key={entry.id}><th scope="row">{skill.names[locale]}{locale !== 'en' && skill.names[locale] !== skill.names.en && <small lang="en">{skill.names.en}</small>}</th><td>{entry.text[locale]}</td></tr>;
    })}</tbody>
  </GuideTable></div>;
}

export function GuideSkillList({locale, classId}: {locale: Locale; classId: ClassId}) {
  const m = labels[locale];
  return <div className="class-skill-list" data-skill-class={classId}>
    <p>{m.note}</p>
    {(['active', 'passive', 'stigma'] as const).map((kind) => {
      const entries = skills[classId].filter((skill) => skill.kind === kind);
      return <details key={kind} open={kind === 'active'}>
        <summary>{m[kind]} ({entries.length})</summary>
        <GuideTable><thead><tr><th scope="col">{m.skill}</th><th scope="col">{m.level}</th></tr></thead>
          <tbody>{entries.map((skill) => <tr key={skill.id} data-skill-id={skill.id}>
            <th scope="row">{skill.names[locale]}{locale !== 'en' && skill.names[locale] !== skill.names.en && <small lang="en">{skill.names.en}</small>}</th>
            <td>{skill.learnedAt}</td>
          </tr>)}</tbody>
        </GuideTable>
      </details>;
    })}
  </div>;
}
