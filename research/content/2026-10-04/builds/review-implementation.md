# AION 2 starter build cards review implementation

Review date: 2026-10-04. Primary audience: early Global party PvE. Existing raw captions and prior research are preserved.

## Cleric

- Source: https://www.youtube.com/watch?v=J3nPw7cuDjY ; BoredAF self-reports TW experience and proposes early Global choices. Existing saved captions: `research/youtube/J3nPw7cuDjY.txt` and `.json`.
- 01:36-02:43: four-role Stigma model, protection, resurrection, Earth's Punishment, Noble Aura; Prayer of Amplification as a to-test alternative, Absolution/Benevolence for healing.
- 02:44-03:44: Debilitating Mark -> Chains of Torment -> Earth's Punishment -> available Condemnation and ordinary attacks; later critical/reset interaction remains conditional on matching client options.
- 03:46-04:20: later Healing Light skill-level-16 goal, Radiant Recovery cleanse choice, Light of Regen movement-speed choice, built-in controls.
- Source: https://www.youtube.com/watch?v=UPjsUVC0DtA ; aLuckyRO models a new character in an existing regional client. Existing saved captions: `research/youtube/UPjsUVC0DtA.txt` and `.json`.
- 11:23-14:43: adjust protection with Chanter coverage, unlock and equip resurrection early, healing alternatives; 19:43-22:38: lower-level cooldown and recovery access.
- Added a skill/options card and manual loop. Reduced duplicated simulation disclaimers and party examples; retained local exceptions for uncertain protection name, cleanse option and reset support.

## Chanter

- Source: https://www.youtube.com/watch?v=EsxGbxt0k-4 ; aLuckyRO uses a lower-level TW character to simulate early Global. TW channel context also appears at 36:25-36:34. Existing saved captions: `research/youtube/EsxGbxt0k-4.txt` and `.json`.
- 02:43-03:21: manual specialization selection, demonstrated skill-level-8/12 options. These are skill levels, not a proven Global character-level range.
- 07:40-08:43: Rushing Smash on-kill reset option. 10:50-12:25: Impactful Crush triggers Dark Crush, shown Dark Crush skill level 14 and critical choice; level-16 cooldown-removal goal.
- 13:33-14:18: Recuperation percentage-HP recovery selection. 15:22-15:51: Spinning Strike cooldown reduction and single-target damage selection. Published no healing percentages or damage/cooldown coefficients as Global facts.
- 26:23-27:19 and 30:01-30:20: party-dependent protective shield and Healing Touch substitutions. 27:55-29:14: Undefeated Mantra investment priority, lower early Sprint Mantra investment and two ranged Stigma Dark Crush triggers.
- Sprint Mantra is retained from existing terminology review; its automatic caption says "spirit". Exact English names of the two ranged trigger Stigmas are not reliable in captions, so the card identifies their effects without inventing official names.
- 32:30-35:17: Rushing Smash -> Spinning Strike -> available Dark Crush; wait for cooldown -> Impactful Crush -> available Dark Crush; equipped ranged Stigma opens a later window. Kept recovery separate.

## Scope and assets

- Numeric current Global character-level ranges, complete point tables and tooltip parity remain unverified. No universal point allocation, mandatory slot count, damage formula or new keyword was added.
- Build index links to the class skill/options cards with existing section anchors. Existing user-added links to Gladiator, Ranger, Spiritmaster, macros and Notmeter remain intact.
- No registered real Cleric/Chanter skill UI screenshot was found. Existing official class art stays labeled illustration; diagrams remain editorial workflows. No generated or recreated game UI is presented as evidence.
- Changes translated across all four existing locales; H2 IDs preserved except the new Twitch campaign section.
