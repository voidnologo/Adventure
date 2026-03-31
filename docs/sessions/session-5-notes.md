# Session 5: Combat System & Base Mechanics Codification

**Date:** 2026-03-31
**Goal:** Codify the combat system into a unified, playtest-ready reference document. Then create a base mechanics quick reference.

## Overview

Major codification session. Gathered scattered combat mechanics from PROJECT_SPEC.md, MAGIC_SYSTEM.md, and FIREARMS_EQUIPMENT.md into a single step-by-step combat procedure (COMBAT_PROCEDURE.md). Then created a base mechanics quick reference (BASE_MECHANICS.md) covering stats, skills, resolution, and magic summary. Also assigned fixed casting times to all 37 spells, introduced ritual spells, and ran armor degradation simulations to rebalance the degradation mechanic.

Several new mechanics were designed during codification: active defense (opposed check with tempo cost), declaration order (lowest PC first, Symbaroum-style), range bands (Close/Near/Far/Distant for theater of the mind), Hinder definition (-5% agility per point, +1 casting speed), and death save timing (every 3 counts).

---

## Changes Made

### 1. Combat Procedure (COMBAT_PROCEDURE.md — NEW)
- Full timing track workflow: scene setup, simultaneous declaration, token placement, resolution
- All attack types: melee, ranged martial, firearms (with one-roll malfunction shortcut), spellcasting
- Active defense mechanic: opposed check, +2 speed cost, once per count
- Damage & soak step-by-step with armor degradation (rebalanced — see below)
- Wounds/death spiral with stacking penalty table
- Death saves: every 3 counts, 50/50 check, 3 failures = death (fastest death: 9 counts)
- Declaration order: lowest PC declares first (ties by AW) — better combatants see what opponents commit to
- Range bands: Close/Near/Far/Distant with movement rules
- Malfunction checks integrated into combat flow
- Spell interruption: concentration check at (PW+4)×10
- Healing & recovery in and out of combat
- Full worked combat example (7+ counts, 2v2)
- One-page printable cheat sheet
- 10 open questions for playtesting

### 2. Armor Degradation Rebalance
- Ran simulation (armor_degradation.py) — current rules destroy chainmail 61% of time in 10 hits
- Rebalanced to: any hit exceeding soak → flat 25% chance of losing 1 soak point
- Crushing tag: 50% instead of 25%
- Simulation validated: chainmail vs medium melee averages 3.6/5 soak after 10 hits (survives but wears)

### 3. Fixed Casting Times (SPELL_COMPENDIUM.md — UPDATED)
- All 37 spells assigned fixed casting times (tier = power drawn, not time)
- Speed buckets: 2ct (cantrips), 3ct (reactive), 4ct (standard combat), 5ct (deliberate), 6ct (complex), 8ct (Sever only)
- 4 ritual spells established: Scry (10 min), Shape Flesh (30 min), Circle (30 min), Transmute (1 hour)
- Removed per-tier Time column from all spell tier tables
- Added casting time reference table to compendium header
- Cancellation cost standardized: half Weak tier exhaustion, 10% backlash
- Updated MAGIC_SYSTEM.md casting time references

### 4. Base Mechanics Reference (BASE_MECHANICS.md — NEW)
- Core roll, opposed checks, stats, skills with formulas and examples
- Derived values table, wound/exhaustion tiers
- Magic summary (casting flow, two paths, exhaustion overflow, ritual spells)
- Magic/tech interference and accumulation summary
- Recovery rates, character creation quick steps
- One-page printable rules summary

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/COMBAT_PROCEDURE.md` | **NEW** — Unified playtest-ready combat reference |
| `docs/requirements/BASE_MECHANICS.md` | **NEW** — Core rules quick reference with cheat sheet |
| `docs/requirements/SPELL_COMPENDIUM.md` | **UPDATED** — Fixed casting times, ritual spells, removed per-tier Time columns |
| `docs/requirements/MAGIC_SYSTEM.md` | **UPDATED** — Casting time references updated for fixed-time model |
| `simulations/armor_degradation.py` | **NEW** — Armor degradation balance analysis (4 alternatives tested) |
| `docs/pending-tasks.md` | **UPDATED** — Checked off combat and base mechanics tasks |
| `docs/continuation-prompt.md` | **UPDATED** — Next session context |
| `docs/sessions/session-5-notes.md` | **NEW** — This file |

## Key Design Decisions

1. **Fixed casting time per spell** — Tier measures power drawn, not time. Wild and scholarly casters follow the same timing. Casting time is a per-spell balance lever independent of tier effects.
2. **Ritual spells** — Shape Flesh, Transmute, Circle, Scry are not combat-castable. They take 10 min to 1 hour. Some magic is too complex for the timing track.
3. **Armor degradation: flat 25%, lose 1** — Replaced cascading overflow system. One check per hit exceeding soak, always lose exactly 1 point. Prevents death-spiral where one bad hit destroys armor.
4. **Concentration check: (PW+4)×10** — Ranges 10% (PW-3) to 70% (PW+3). Handles negative stats cleanly, rewards PW investment at character creation.
5. **Declaration order by PC, then AW** — Better combatants declare last and see what opponents commit to. Creates tactical advantage for investing in coordination/awareness.
6. **Death saves every 3 counts** — Gives allies 9+ counts minimum to intervene (cancel action + sprint + medicine). Fast enough to be tense, slow enough to be rescuable.
7. **Cancellation cost: half Weak tier** — Fixed, predictable, narratively grounded ("some power was already flowing"). No need to track what tier you were attempting.

## Open Issues

- 10 playtest questions in COMBAT_PROCEDURE.md §13 (active defense balance, dodging bullets, sprint speed, etc.)
- Wild caster backlash modifier still TBD (exact +% per tier)
- Concentration check may need tuning after playtesting
- Death save 50/50 threshold may benefit from PP modifier

## Next Session

Create a website (landing page + rules) modeled after the card-game/web repo. Establish art style guide and AI generation pipeline for the 1920s steampunk aesthetic.
