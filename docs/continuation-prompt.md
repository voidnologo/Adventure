# Continuation Prompt

## Last Session (9) — Rules Review, Ballistic/Martial Armor, Galvanic Weapons, Full UI Redesign
- Caught and fixed inconsistencies from session 8 (Reliability always checked, accumulation timing, wild caster farther-die mechanic, malfunction as roll-under not reverse formula)
- Armor split into **Ballistic** (firearms) and **Martial** (melee) ratings — different armor for different threats
- Galvanic weapons redesigned from generic stat table to 7 named weapons with unique abilities and keywords (Force Blade, Arc Gun, Galvanic Lance, etc.)
- Complete UI redesign: 8-page documentation site with sidebar TOC, per-page themes (Aetheric/Galvanic/split), new design system (deep blue-black, Playfair Display, glassmorphic panels, particles)
- Landing page rewritten narrative-first: world/story before mechanics, scenario cards, inline SVG icons
- Expanded World Between with approved cosmology (Veil/Engine/Baseline, terminology table, Three Theories)

## Current State
- **Website live:** Landing page + 8-page rules reference with new design system
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval. Layout/design only.
- **Playtest-ready documents:** COMBAT_PROCEDURE.md, BASE_MECHANICS.md (with cheat sheets)
- **Complete (first pass):** Magic system, spell compendium (37 spells), weapons (melee + firearms + Galvanic), armor/soak (Ballistic/Martial), malfunction/accumulation, design philosophy, art style guide, writing style guide
- **Accumulation model:** Single sliding scale. Spells push Aetheric (+), Galvanic tech pushes negative (-). Eff. Reliability = Base - (net x 2). Eff. Casting Target = Base + (net x 2). Reliability always checked. Symmetric zones.
- **Not yet designed:** Leveling, factions, zone formation mechanics, Push Timing mechanic, races, archetype names, skill list revision, currency, bestiary

## Immediate Next Task
**Verify rulebook page content**, then **define major factions and Adventuring Societies.**

## Key References
- `web/rules/` — 8-page rules site (index, creating, rolling, getting-hurt, magic, world-between, combat, reference)
- `web/rules/css/styles.css` — Design system
- `web/rules/js/main.js` — Navigation, particles, scroll spy
- `web/index.html` — Landing page
- `docs/requirements/COMBAT_PROCEDURE.md` — Full combat rules with cheat sheet
- `docs/requirements/BASE_MECHANICS.md` — Core mechanics with cheat sheet
- `docs/requirements/PROJECT_SPEC.md` — Setting, stats, weapons, armor, zone descriptions
- `docs/requirements/MAGIC_SYSTEM.md` — Full casting rules, Push It, school access, tie rule
- `docs/requirements/SPELL_COMPENDIUM.md` — All 37 spells with fixed casting times
- `docs/requirements/FIREARMS_EQUIPMENT.md` — Firearms, Galvanic weapons, Aetheric ratings, accumulation, malfunction
- `docs/requirements/DESIGN_PHILOSOPHY.md` — Cosmology (Veil/Engine), literary influences, terminology table
- `docs/requirements/WRITING_STYLE.md` — Player-facing vs internal style, dice roll conventions, terminology guide
- `docs/sessions/session-9-notes.md` — Full record of all decisions and changes
