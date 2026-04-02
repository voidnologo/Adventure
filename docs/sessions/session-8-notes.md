# Session 8: Design Audit, Web Rulebook Overhaul, and Major Mechanical Revisions

**Date:** 2026-04-02
**Goal:** Audit all design docs for consistency, bring web rulebook fully up to date, and resolve multiple open design questions

## Overview

This was the largest session to date. Started as a consistency audit (22 discrepancies found and fixed across all design docs), then expanded into a complete web rulebook overhaul (from ~1400 to ~2400 lines), followed by a series of significant design decisions that reshaped the magic/technology interference system, established setting terminology, and resolved several long-standing open questions.

The session had three major phases: (1) audit and fix all docs against session 1-7 decisions, (2) expand the web rulebook to include all designed content, (3) design-level revisions to the accumulation system, setting terminology, weapon stats, and the Push It mechanic.

---

## Changes Made

### Phase 1: Design Document Consistency Audit

Found and fixed 22 discrepancies across all design docs:

**MAGIC_SYSTEM.md (13 fixes):**
- Wild tier suppression cap: 3 → 2 at 76+ (4 locations)
- Added PW = mental fortitude framing note
- "Spell points" → "spells known" (3 locations)
- Wild backlash: "TBD/Higher" → +5% flat per tier with actual numbers
- Mend example: removed per-tier casting times, updated to single fixed time
- Concentration check §3.7: replaced OPEN with resolved mechanic ((PW+4)×10)
- All 6 template spell tables (§9): removed per-tier Casting Time columns
- Both cost comparison tables restructured
- 3 open questions marked RESOLVED
- Force casting time: corrected to 2ct (was 3ct in worked examples)
- Mend casting time: corrected to 5ct per SPELL_COMPENDIUM (was 4ct in template)

**PROJECT_SPEC.md (10 fixes):**
- Armor degradation: overflow formula → flat 25% / lose 1 soak
- Crushing tag: overflow → "50% instead of 25%"
- Magic/tech interference: added asymmetric framing
- Added §5.2 Exhaustion Points to Health section
- Death saves: TBD → full mechanic
- Hinder: "not fully defined" → full definition
- 3 open questions marked DONE

**COMBAT_PROCEDURE.md:** Math error (PW +2 concentration = "20" → "60")

**Simulation code (3 files):** MP → EP terminology throughout

**Web rulebook phase 1:** Unskilled ×10→×5, "magic points"→"exhaustion points", PW descriptions

### Phase 2: Web Rulebook Major Expansion

Expanded web/rules/index.html from ~1400 to ~2400 lines:

- **Section 3 (Rolling the Dice):** Added timing track introduction so readers understand "counts" before sections 4-5 reference them
- **Section 4 (Getting Hurt):** Expanded death saves (d100 mechanic, 01/00 specials, ally intervention), added exhaustion tier table, clarified death saves are HP-track only with exhaustion overflow explained
- **Section 5 (Magic):** Complete rewrite — Scholarly path (1d100, full tier control, all 6 schools, learned spells), Wild path (2d100 farther-from-target, +10 bonus, tier suppression 0-2, PW modifier schools, all spells in school), dual backlash rates, concentration checks, spell cancellation, misfire concept with examples, Push It with full mechanics, ritual spells, all 6 schools with 37 spell names
- **Section 6 (The World Between):** Rewritten with Veil/Engine cosmology, unified number line model, Aetheric/Galvanic terminology, zone gradient and forensic investigation flavor
- **Section 7 (Combat):** Major expansion — attack modifiers, expanded active defense, range bands with movement/cover, complete weapon tables (melee + martial + firearms + exotics with Aetheric ratings), all weapon tags, Hinder mechanic, full armor tables, malfunction system. Sections reordered: weapons → tags → malfunction grouped together; armor → hinder grouped together
- **Section 8 (Cheat Sheet):** Fully updated

### Phase 3: Design Decisions and Revisions

#### 1. Scholarly vs Wild School Access (NEW DECISION)
- **Scholarly casters:** Access to ALL 6 schools. Must learn specific spells (7+PW base, buy more at 3 skill points). Breadth.
- **Wild casters:** Access to PW modifier schools (min 1). Can cast EVERY spell in those schools. Depth.
- **Rationale:** Clean trade-off. Scholarly = breadth + control. Wild = depth + power. Resolved open question from session 2.

#### 2. Push It Mechanic (RESOLVED)
- Push one tier up from qualified result
- **Exhaustion:** Half the qualified tier's cost + full pushed tier's cost
- **Backlash:** Double the pushed tier's rate
- Hard cap applies. One push per cast.
- **Rationale:** Half+full is less punishing than double but still a meaningful sacrifice. Doubled backlash makes it genuinely scary. The Mend Standard→Strong push at 16 EP is heroic sacrifice territory.

#### 3. Unified Accumulation Number Line (NEW MODEL)
- **Old model:** Two separate pools (Magic Accumulation and Tech Accumulation) that independently penalized each side
- **New model:** Single sliding scale. Spells push positive (Aetheric), exotic tech pushes negative (Galvanic). Net balance determines effects.
- **Rationale:** Simpler to track, creates a tug-of-war dynamic, makes party composition tactically interesting

#### 4. Setting Terminology (NEW)
- **The Veil:** Cosmological source of magic. The boundary that thinned when magic erupted.
- **The Engine:** Cosmological source of Galvanic force. Human industry given metaphysical weight.
- **Aetheric:** Adjective for magic and its effects. "Aetheric accumulation," "Aetheric zone."
- **Galvanic:** Adjective for exotic tech and its effects. "Galvanic technology," "Galvanic resonance."
- **Rationale:** "Aetheric" was doing double duty for both sides. Galvanic is period-appropriate (1920s) and distinct. Veil/Engine are evocative formal terms for where each force originates.

#### 5. Per-Item Aetheric Ratings (NEW)
- Exotic weapons now have an Aetheric rating (1-3) instead of flat -1 per shot
- Exotic Pistol: 1, Exotic Sidearm: 2, Exotic Heavy: 3, Exotic Melee: 1
- Suppressing tag: +1 to weapon's Aetheric rating
- Non-weapon devices get GM-assigned ratings based on scale
- **Rationale:** Parallels spell tier scaling. A lightning cannon should shift the balance more than a flechette pistol.

#### 6. Symmetric Balance Effects (NEW)
- Each net point shifts BOTH sides — penalizing one while empowering the other
- Effective Reliability = Base − (net balance × 2)
- Effective Casting Target = Base + (net balance × 2)
- **Rationale:** Wild Zones aren't just "guns fail" — they're "magic is incredible." Galvanic Zones aren't just "spells fail" — they're "guns are perfect." Much richer than one-sided penalties.

#### 7. Multiplier Change: ×3 → ×2 (REVISED)
- Changed from 3% per net point to 2% per net point
- **Rationale:** At ×3, a bunch of casters rapidly makes every magical effect Spectacular and completely shuts down firearms. At ×2, the balance influences without dominating. A +10 zone gives +20 to casting (significant but not game-breaking) and -20 to Reliability (noticeable but guns still work). Wider range of meaningful zone values.

#### 8. Reliability Always Checked (NEW)
- Old: conventional firearms skip Reliability in clean air
- New: every shot, every time. Tommy gun has 30% malfunction chance even in your living room.
- Firing sequence: Reliability first (does it fire?), then Ranged (does it hit?)
- **Rationale:** Makes Reliability a real weapon characteristic, not just a magic-zone penalty. Parallels backlash — magic always risks burning you, firearms always risk jamming.

#### 9. Symmetric Zone Table (NEW)
- Zone table expanded from 6 entries (5 magic + 1 tech) to 9 symmetric entries
- Deep Galvanic Zone (−25+) through Deep Wild Zone (+25+) with matching entries on both sides
- **Rationale:** The old table was magic-heavy. The sliding scale demands equal representation. Also established zone formation narrative: zones are environmental stains from sustained activity, bleed outward in gradients, and are impossible to hide (forensic investigation hooks).

#### 10. Reload Values Reduced (REVISED)
- All reload times approximately halved
- Crossbows: Light 6→3, Heavy 10→5
- Firearms: range from 2 (holdout, semi-auto, shotgun) to 5 (carbine, exotic heavy)
- **Design philosophy:** Reloading should create "hurry hurry" tension, not boring downtime. The penalty makes you think about magazine management without bogging the game down.

#### 11. Writing Style Conventions (NEW)
- **Dice roll conventions:** Ability checks are roll-under. Consequence checks (backlash, degradation, wild effects) are stated as plain percentages. Don't force consequence checks into roll-under language.
- **Setting terminology guide:** When to use Veil/Engine, Aetheric/Galvanic, Exotic/Conventional/Martial
- **Balance in examples:** Always show both sides of the Aetheric/Galvanic scale in worked examples

#### 12. Minor Fixes
- Piercing tag: 1 point → 2 points (matched all design docs)
- Versatile tag: "+1 damage" → "one die step up"
- Throwable tag: added "+2 speed, one die step lower damage"
- Kael's Ranged stat: PC → PP (Ranged is PP-based)
- Kael's armor: "leather jacket (Soak 2)" → "reinforced leather coat (Soak 2)" to avoid conflict with Modern Armor table
- Worked combat example: fully reworked for Force 2ct, 2d100 wild rolls, correct backlash rates
- Combat section reordered: weapons→tags→malfunction; armor→hinder
- "Industrial Dead Zone" renamed to "Deep Galvanic Zone" throughout
- Misfire example moved from wild caster section to scholarly section
- Wild caster example corrected (was showing misfire incorrectly; now shows forced Spectacular)
- "C3" complexity removed from player-facing Push It example

---

## Files Modified

| File | Change |
|------|--------|
| docs/requirements/MAGIC_SYSTEM.md | Suppress cap, PW framing, terminology, backlash values, templates, concentration check, Push It mechanic, school access resolved, casting times corrected |
| docs/requirements/PROJECT_SPEC.md | Armor degradation, crushing, magic/tech asymmetry, EP section, death saves, hinder, zone descriptions with Aetheric/Galvanic terminology and gradient model |
| docs/requirements/COMBAT_PROCEDURE.md | Concentration math fix, firearm firing sequence (Reliability first), accumulation ×2, Galvanic terminology |
| docs/requirements/FIREARMS_EQUIPMENT.md | Aetheric ratings on exotics, unified number line model, symmetric balance (×2), "always check Reliability," Galvanic terminology, reload values reduced |
| docs/requirements/DESIGN_PHILOSOPHY.md | Veil/Engine cosmology, Aetheric/Galvanic terminology table, updated theories, zone naming |
| docs/requirements/WRITING_STYLE.md | Dice roll conventions (ability vs consequence checks), setting terminology guide, balance-in-examples rule |
| docs/requirements/BASE_MECHANICS.md | Accumulation ×2, Galvanic terminology, symmetric examples, updated scholarly/wild table |
| docs/requirements/SPELL_COMPENDIUM.md | "Industrial Dead Zone" → "Deep Galvanic Zone" in spell descriptions |
| web/rules/index.html | Complete overhaul — sections 3-8 rewritten/expanded, all terminology updated, all examples recalculated for ×2 |
| web/index.html | Landing page accumulation text updated (×2, Aetheric/Galvanic terminology) |
| simulations/config.py | MP → EP terminology |
| simulations/engine.py | MP → EP terminology |
| simulations/run_analysis.py | MP → EP terminology |
| docs/sessions/session-8-notes.md | This file |
| docs/pending-tasks.md | 7 items checked off, 1 new item added |
| docs/continuation-prompt.md | Updated for session 8 |

## Open Issues

- Wild backlash modifier (+5% flat) is "working value" pending playtesting
- Concentration check ((PW+4)×10) is provisional pending playtest tuning
- balance_report.txt still has old MP terminology (auto-fixes when sim re-runs)
- Push Timing mechanic (rush actions with escalating failure) captured as TODO — not yet designed
- Zone formation mechanics (how zones shift over time) still deferred
- Web rulebook needs visual design pass (content is now complete)
- Combat worked example still uses old accumulation ×3 math in some narrative beats (Reliability 83% reference at count 7) — may need another pass

## Next Session
- Visual design pass on web rulebook
- Factions and Adventuring Societies (top of Next Up)
- Leveling/progression mechanics
- Push Timing mechanic design
