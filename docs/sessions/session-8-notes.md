# Session 8: Design Document Consistency Audit & Web Rulebook Update

**Date:** 2026-04-02
**Goal:** Review all design documents against session decisions to find and fix discrepancies, then bring the web rulebook fully up to date

## Overview

Two phases: (1) Comprehensive audit of all system documents against session 1-7 decisions. Found 22 discrepancies across MAGIC_SYSTEM.md, PROJECT_SPEC.md, COMBAT_PROCEDURE.md, web rules, and simulation code. All fixed. (2) Major expansion of the web rulebook to include all designed content that was missing — wild caster mechanics, weapon tags, firearms tables, malfunction system, death save details, concentration checks, active defense, range modifiers, hinder, schools of magic, and more.

---

## Changes Made

### MAGIC_SYSTEM.md (13 fixes)
- Wild tier suppression cap: 3 → 2 at 76+ (4 locations: table, examples, casting sequence, open questions)
- Added PW = mental fortitude framing note at top of section 2
- "Spell points" → "spells known" (3 locations: scholarly benefits, wild limitations, comparison table)
- Wild backlash: replaced "TBD/Higher" with working values (+5% flat per tier, actual numbers filled in)
- Mend example in §3.3: removed per-tier casting times, updated to single fixed time format
- Concentration check §3.7: replaced OPEN block with resolved mechanic ((PW+4)×10) and reference table
- All 6 template spell tables (§9): removed per-tier Casting Time columns, added single time to headers
- Both cost comparison tables (§9.3, §9.8): restructured to show fixed casting time separately from per-tier exhaust
- Marked 3 open questions as RESOLVED (spell tier tables, tier suppression cap fix, casting interruption)
- Updated Last Updated date

### PROJECT_SPEC.md (10 fixes)
- Armor degradation: replaced overflow formula with flat 25% / lose 1 soak
- Crushing tag: replaced overflow description with "50% instead of 25%"
- Magic/tech interference: added asymmetric framing (only exotic tech erodes magic back)
- Added §5.2 Exhaustion Points section to Health & Damage (EP as general system mechanic, not magic-only)
- Death saves: replaced TBD with resolved mechanic (d100, >50=fail, 3 fails=death)
- Hinder: replaced "not fully defined" note with actual definition
- Marked 3 open questions as DONE (death saves, spell tier tables, hinder mechanic)
- Exhaustion track in magic section: reframed as reference to §5.2 instead of standalone description
- Updated Last Updated date

### COMBAT_PROCEDURE.md (1 fix)
- Math error in playtest note: PW +2 concentration = "roll under 20" → "roll under 60"

### web/rules/index.html (major rewrite)
Phase 1 fixes:
- Unskilled formula example: ×10 → ×5 (with recalculated numbers for opposed check scenario)
- "magic points" → "exhaustion points" in backlash description
- PW -3 description: "magically dead" → "mentally fragile"
- Kael's PW -2 flavor: "near-dead to magic" → "low mental reserves"

Phase 2 — full content update (sections 4, 5, 7, 8 rewritten):
- **Section 4 (Getting Hurt):** Expanded death saves with d100 mechanic (01=stabilize, 00=instant death), ally intervention rules, exhaustion tier table added
- **Section 5 (Magic):** Complete rewrite — added Scholarly path (1d100, full tier control), Wild path (2d100 farther-from-target, +10 bonus, tier suppression 0-2), dual backlash rate table, concentration check mechanic, spell cancellation, misfire concept with examples, Push It mechanic, all 6 schools with 37 spell names and concepts
- **Section 7 (Combat):** Major expansion — full attack modifier table, expanded active defense (Melee/Brawl/Athletics, Parrying +10%, shields), expanded range bands with movement/cover, complete weapon tables (melee + martial ranged + modern firearms + steampunk exotics), weapon tag tables (melee + firearm + exotic), Hinder mechanic, full armor tables (medieval + modern + shields), malfunction system (severity table, exotic escalation), fixed Kael's Melee 65→66
- **Section 8 (Cheat Sheet):** Fully updated to include all new mechanics

### Simulation code (MP → EP terminology, 3 files)
- config.py: MP_BY_LEVEL → EP_BY_LEVEL, updated comments
- engine.py: mp_before/mp_after/current_mp → ep_before/ep_after/current_ep
- run_analysis.py: all MP references → EP (variable names, strings, report labels)

---

## Files Modified

| File | Change |
|------|--------|
| docs/requirements/MAGIC_SYSTEM.md | Suppress cap, PW framing, spell points terminology, backlash values, template tables, concentration check, open questions |
| docs/requirements/PROJECT_SPEC.md | Armor degradation, crushing tag, magic/tech asymmetry, EP section, death saves, hinder, open questions |
| docs/requirements/COMBAT_PROCEDURE.md | Concentration check math error |
| web/rules/index.html | Full rewrite of sections 4, 5, 7, 8 — all designed content now included |
| simulations/config.py | MP → EP terminology |
| simulations/engine.py | MP → EP terminology |
| simulations/run_analysis.py | MP → EP terminology |

## Key Design Decisions

No new design decisions — this was a consistency audit. All changes reflect decisions already made in sessions 2-7.

## Open Issues

- Wild backlash modifier (+5% flat) is still technically "working value" pending playtesting — but now documented as such rather than "TBD"
- Concentration check ((PW+4)×10) is marked provisional pending playtest tuning
- balance_report.txt still has old MP terminology (will auto-fix when simulation is re-run)

## Next Session
