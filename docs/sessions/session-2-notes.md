# Session 2: Magic System Design

**Date:** 2026-03-29
**Goal:** Continue design interview — define schools of magic, casting mechanics, spell lists, scholarly/wild caster paths, backlash, and core spell templates.

## Overview

Deep-dive session on the magic system. Established the tiered casting mechanic (inspired by DCC's variable spell results mapped onto the existing d100 percentile system), defined six schools of magic with 37 total spells, designed the scholarly vs. wild caster paths with meaningful mechanical differences, and worked out the relationship between misfire, backlash, exhaustion, tier selection, and the "push it" mechanic.

Key design breakthroughs:
- Spells are concept-based tools with tiered results, not D&D-style fixed effects
- Wild casters roll 2d100-take-extreme with +10 casting bonus (probability-verified)
- Backlash uses a d10 Wild Effect Table with 3-tier escalation (base → escalated → permanent)
- Wild caster tier suppression scales with skill brackets (mirroring crit range mechanic)
- Exhaustion overflow converts to physical damage at half rate
- Opposed checks established as a core system mechanic (not just magic-specific)
- Six template spells designed across all schools to validate the cost formula

---

## Changes Made

- [x] Defined 6 schools of magic with thematic identities
- [x] Created 37 spells across all schools (5-7 per school)
- [x] Designed tiered casting mechanic (Misfire/Weak/Standard/Strong/Spectacular)
- [x] Established hard caps based on casting target number
- [x] Designed scholarly vs wild caster mechanical differentiation
- [x] Wild caster variance: 2d100 take farther from target, +10 casting bonus (probability verified)
- [x] Wild caster tier suppression: 0/1/2/3 tiers based on 25% skill brackets
- [x] Backlash: 1d4 flat damage + 25% chance of Wild Effect (d10 table, 3-tier escalation)
- [x] Exhaustion overflow: spell fires, excess converts to physical HP damage at half rate
- [x] Casting interruption: noted as open design question with timing track interaction
- [x] Opposed check mechanic: added to core rules (PROJECT_SPEC.md §3.1b)
- [x] Six template spells designed: Force, Mend, Shield, Reveal, Reshape, Sever
- [x] Hidden cost formula validated across Complexity 1-4
- [x] Removed Harden (redundant with Alter Property) and Animate (poor fit)
- [x] Added Transmute as Transmutation school's crown jewel

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/MAGIC_SYSTEM.md` | **NEW** — Full magic system design: philosophy, paths, casting mechanics, 6 schools, 37 spells, backlash table, 6 template spell tier tables, design guidelines |
| `docs/requirements/PROJECT_SPEC.md` | Updated magic section to summary + reference, added opposed check mechanic (§3.1b), updated open questions |
| `docs/sessions/session-2-notes.md` | **NEW** — This file |
| `docs/pending-tasks.md` | Updated to reflect completed magic work |

## Key Design Decisions

1. **DCC-inspired tiered casting on d100** — Roll determines tier available (Weak/Standard/Strong/Spectacular). Not just pass/fail.
2. **Hard caps from stats** — A target of 30 can NEVER achieve Strong. Power ceiling is built into ability, not luck.
3. **Scholarly vs Wild** — Scholarly: spellbook, choose tier freely, lower backlash. Wild: entire domain, 2d100 extreme variance, +10 bonus, limited tier suppression.
4. **Wild caster tier suppression** — Can step down 0/1/2/3 tiers based on 25% skill brackets. Novices are chaotic, masters learn control. Mirrors crit range mechanic.
5. **Concept-based spells** — "Elemental Manipulation" covers fire through lightning. GM and player interpret specifics within tier guidelines.
6. **Misfire ≠ Backlash** — Misfire is spell-specific (healing drains instead). Backlash is raw energy burn (1d4 + wild effect chance).
7. **Backlash escalation** — Wild effects escalate per-effect if same number rolled while active. Third instance = permanent stat reduction. Fear of escalation naturally limits casting.
8. **Exhaustion overflow** — Spell fires even if you can't pay the full cost. Overflow → physical HP damage at half rate. Enables heroic sacrifice moments.
9. **Costs scale with complexity** — Hidden formula: Complexity 1 (Force) through Complexity 4 (Sever). Players see final numbers, designers use consistent formula.
10. **Opposed checks** — Core mechanic added to PROJECT_SPEC. Both sides roll d100 vs relevant target, larger margin wins. Used for Sever resistance, arm wrestling, chases, stealth vs observation, etc.
11. **No spirits/elementals as routine magic** — Supernatural entities are rare, alien, Cthulhu-esque. Not summonable.
12. **Shield absorbs all damage equally** — No separate "magical damage" type. Mechanical consistency.

## Open Issues

- Push It mechanic needs exact costs/risks
- Remaining 31 spell tier tables (6 templates done, 31 to go)
- Wild vs Scholarly exact backlash rate modifier
- Scholarly bonus to school count
- Casting interruption/concentration check mechanics
- Spell interaction with magic/tech zones
- Mid-campaign spell learning for scholarly casters
- Weapon timing table may need rebalancing relative to casting times

## Next Session

Continue design interview:
1. Remaining spell tier tables (batch by school)
2. Firearms and steampunk equipment tables
3. Leveling/progression mechanics
4. Faction design
5. Magic/tech zone interference rules
