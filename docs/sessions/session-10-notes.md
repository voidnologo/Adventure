# Session 10: Skills, Progression & Rulebook Restructure

**Date:** 2026-04-03
**Goal:** Design complete skills list and progression system, then restructure the web rulebook into focused chapters

## Overview

Session began with designing the full skills list and XP/progression system, then expanded into a major rulebook restructure. The skill list was consolidated from 34 unfocused skills to 27 setting-appropriate ones, categorized by all 6 attributes (PW joined the Mental group). The progression system uses session-based XP with no combat incentive — 1 XP automatic per session plus table vote bonus, skills cost N XP to reach level N, attributes cost 10 XP per point.

The second half restructured the 8-page web rulebook into 12 chapters, splitting reference content from rules/mechanics. The grimoire was expanded with full tier-by-tier spell descriptions for all 37 spells. The equipment chapter gained Galvanic Oddities (6 template devices) and a vehicles section. "Aetheric rating" was renamed to "Galvanic rating" for Galvanic devices/weapons.

---

## Changes Made

### Skills List (27 Skills)
- Consolidated from 34 to 27 skills across all 6 attributes
- Added: Firearms (PC), Piloting (PC), Investigation (AW), Occult Lore (IN), Sleight of Hand (PC), Streetwise (SP), Deception (SP), Resolve (PW)
- Removed/consolidated: Running, Swimming, Climbing → Athletics; Metalworking, Woodworking, Repair → Craft; Acting, Disguise, Forgery → Deception; Hunting → Survival; Security → Sleight of Hand; Gambling, Business, Interrogation → removed
- Intimidation is flex-stat (PP physical menace or SP social pressure)
- PW added to Mental group (Mental = IN + AW + PW)

### Progression System
- 1 XP per session (automatic) + bonus XP from table vote at session end
- Skill advancement: cost to reach level N = N XP (creation cap 3, gameplay max 5)
- Attribute advancement: 10 XP per +1 (cap +3)
- Post-creation XP is universal currency, not limited by group pools
- No XP for kills, loot, or combat — strongest anti-murderhobo signal possible

### Rulebook Restructure (8 → 12 Chapters)
- Ch 05 Skills (NEW) — full skill descriptions by attribute
- Ch 07 The Grimoire (NEW) — spell school overviews + alphabetical spell reference dictionary with full tier tables for all 37 spells
- Ch 10 Arms & Equipment (NEW) — weapons, armor, Galvanic oddities, vehicles (extracted from combat chapter)
- Ch 12 Table Index (NEW) — every table in the rulebook, organized by frequency of use with direct links
- Magic chapter (now Ch 06) slimmed to casting mechanics only, spell listings moved to grimoire
- Combat chapter (now Ch 09) slimmed to mechanics only, equipment moved to arms chapter
- All navigation, chapter numbers, and sidebar updated across all pages

### Grimoire Expansion
- All 37 spells expanded with full Weak/Standard/Strong/Spectacular/Misfire tier tables from SPELL_COMPENDIUM.md
- Page structure: school overviews with linked summary tables → exhaustion/casting time reference → alphabetical spell reference dictionary
- Each spell entry shows its school in a subdued label
- spell-title CSS class for visual prominence, school-title class with accent underline

### Equipment Expansion
- Galvanic Oddities section: 6 template devices (Aetheric Compass, Force Generator, Resonance Damper, Voltaic Lantern, Galvanic Brace, Signal Caster) with "Creating Your Own" framework
- Vehicles & Conveyance: 10 narrative categories with Aetheric vulnerability notes
- Terminology fix: "Aetheric rating" renamed to "Galvanic rating" throughout (devices channel Engine force)

### Design Doc Updates
- Created SKILLS_PROGRESSION.md — authoritative reference for all 27 skills and progression rules
- Expanded FIREARMS_EQUIPMENT.md §6-8 with full Galvanic Oddities design, vehicle categories, general equipment
- Updated PROJECT_SPEC.md §3.3 (skills) and §7 (progression)
- Updated BASE_MECHANICS.md §4 (skills) and added §4.4 (progression)

### UI/UX Fixes
- Sidebar TOC: added data-toc attribute support for short labels (school names instead of full subtitles)
- Scroll-spy: added 60vh bottom padding so last page sections can scroll to top
- h3 bumped to 1.4rem for proper hierarchy over spell titles
- school-title class: accent color with underline border
- spell-title class: Playfair Display, accent color, left border
- Removed spell counts from school headings (maintenance burden, no user value)

---

## Files Modified

| File | Change |
|------|--------|
| docs/requirements/SKILLS_PROGRESSION.md | NEW — full skills list (27) with descriptions and progression system |
| docs/requirements/FIREARMS_EQUIPMENT.md | Expanded §6-8: Galvanic oddities, vehicles, equipment categories; renamed Aetheric→Galvanic rating |
| docs/requirements/PROJECT_SPEC.md | Updated §3.3 skills, §7 progression; marked both as DONE in open questions |
| docs/requirements/BASE_MECHANICS.md | Updated skill list/groups, added progression summary, updated cheat sheet |
| docs/pending-tasks.md | Checked off skills revision and progression design |
| web/rules/skills.html | NEW — Chapter 05, full skill descriptions by attribute group |
| web/rules/grimoire.html | NEW — Chapter 07, school overviews + all 37 spells with full tier tables |
| web/rules/equipment.html | NEW — Chapter 10, weapons/armor/oddities/vehicles (extracted from combat) |
| web/rules/tables.html | NEW — Chapter 12, table index organized by frequency of use |
| web/rules/creating.html | Updated skill table, Kael example, added progression section (Step 5), renumbered steps |
| web/rules/magic.html | Chapter 5→6, removed spell listings (→grimoire), updated nav |
| web/rules/combat.html | Chapter 7→9, removed weapons/armor/hinder (→equipment), updated nav |
| web/rules/world-between.html | Chapter 6→8, updated nav links |
| web/rules/getting-hurt.html | Updated nav (next→skills instead of magic) |
| web/rules/reference.html | Chapter 8→11, updated nav (prev→equipment, next→tables) |
| web/rules/js/main.js | Added 4 new pages to PAGES array, data-toc support in getSections() |
| web/rules/css/styles.css | spell-title, school-title, spell-school, spell-meta, section-divider classes; h3 size bump; scroll-spy bottom padding fix |
| docs/sessions/session-10-notes.md | This file |

## Key Design Decisions

1. **PW in Mental group** — keeps the system to 3 groups. Mental's larger pool (3 stats) balances against having the most skills (13). Non-casters who dump PW reduce their Mental pool but may still want Resolve.

2. **No XP for combat** — the progression system literally cannot see whether you fought. Advancement rewards showing up and being memorable. Strongest possible anti-murderhobo design.

3. **Skill cost = next level number** — cheap to try new things (0→1 = 1 XP), expensive to master (4→5 = 5 XP). Scarcity comes from opportunity cost across 15 skills, not raw cost per skill.

4. **Attributes improvable at 10 XP** — expensive but cascading. Raises all skills under that attribute plus derived values. A campaign landmark, not routine.

5. **Rules/reference split** — chapters explain WHY mechanics matter (rules), followed by chapters listing WHAT you use with those mechanics (reference). Combat explains timing track, attacks, defense. Equipment is the catalog you flip to for numbers.

6. **Grimoire structure** — school overviews with linked summary tables for quick scanning, then alphabetical spell dictionary for deep lookup. Players scan by school, then search by name.

7. **Galvanic Oddities as templates** — categories over exhaustive lists. Show GMs how to stat a device (function, Galvanic rating, reliability, power, drawback) so they can create new ones.

8. **Aetheric→Galvanic rating rename** — devices channel Engine force, calling their rating "Aetheric" was confusing. Named for what it IS, not what it interacts with.

9. **Design docs before rules** — established workflow: persist decisions in docs/requirements/ with rationale first, then write polished player-facing version for the rulebook.

## Open Issues

- GM chapter needed: social situations, making devices on the fly, zone tracking, chases, spell effect narration, adjudication philosophy, heavy examples that follow the rules
- "Aetheric rating" → "Galvanic rating" rename needs to propagate to: world-between.html, cheat sheet in reference.html, BASE_MECHANICS.md accumulation section, COMBAT_PROCEDURE.md
- Vehicle chase/travel rules noted in design doc but belong in future GM chapter, not equipment
- Scroll-spy bottom padding (60vh) may need tuning — works but is a blunt instrument
- Table Index page links need verification after all the restructuring
- Mobile sidebar UX still untested on real devices

## Next Session
- Design GM chapter ("Running the Game") — adjudication philosophy, social situations, chases, zone management, narrating spell effects, examples that follow the rules
- Define major factions and Adventuring Societies
- Propagate Galvanic rating terminology across remaining pages
