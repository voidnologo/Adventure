# Session 4: Firearms, Weapon Rebalance & Design Philosophy

**Date:** 2026-03-31
**Goal:** Design firearms, steampunk weapons, and equipment tables. Establish the cosmological WHY behind magic/tech tension. Rebalance melee weapons into a category+tag system.

## Overview

Major session covering three interlocked areas: firearms design, the foundational design philosophy document, and a complete overhaul of the weapon system from individual stat lines to categories with tags.

Started with firearms — established Speed/Damage/Capacity/Reload/Reliability stats, built the malfunction system (mirrors spell backlash), and designed Magic Accumulation (spellcasting degrades nearby firearms). Then took a deliberate diversion into the *why* — the cosmological framework, literary influences, and design principles that should guide all future mechanical decisions. Finally, ran balance analysis on the original 20-year-old melee weapon table, found significant issues (dominated weapons, identical stats, outliers), and replaced it with a Symbaroum-inspired category+tag system.

---

## Changes Made

### 1. Firearms & Steampunk Equipment (FIREARMS_EQUIPMENT.md — NEW)
- 9 modern firearm categories (holdout through submachine gun)
- 4 steampunk exotic categories (pistol, sidearm, heavy, melee)
- Malfunction system: roll every shot, base cost = lost action, d10 severity table (mirrors spell backlash)
- Magic Accumulation: each spell tier adds points, 3% Reliability penalty per point, decays 1/minute
- Tech Accumulation: exotic weapons generate counter-resonance that penalizes spellcasting
- Firearm-specific tags: Reliable, Quick Reload, Loud, Quiet, Scatter, Burst, Accurate, Sawn-Off
- Exotic-specific tags: Shocking, Suppressing, Silent, Unstable
- Equipment categories (non-weapons): field gear, investigation tools, protective gear, transport
- Modern armor supplement: leather jacket through ballistic vest

### 2. Design Philosophy (DESIGN_PHILOSOPHY.md — NEW)
- Cosmological framework: two competing forces (magic vs exotic tech) + physical baseline
- Asymmetric interference model: magic erodes all tech; only exotics erode magic; martial is immune
- The Invisible War: designer-facing cosmology, never explicitly visible in-world
- 8 literary/RPG influences with specific design takeaways
- 7 derived design principles (gradient not switch, complexity = vulnerability, belief roots, etc.)
- Setting implications: visual shorthand, magical forensics, arms economy, faction dynamics

### 3. Weapon Category Rebalance (PROJECT_SPEC.md — UPDATED)
- Replaced 28 individual weapon stat lines with 6 melee categories + 4 ranged categories
- Categories: Unarmed / Small / Light / Medium / Heavy / Great
- 9 weapon tags for mechanical differentiation within categories
- Balance validated by simulation: armor soak naturally balances speed vs. damage tradeoff

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/FIREARMS_EQUIPMENT.md` | **NEW** — Full firearms design: categories, tags, malfunction system, accumulation mechanics |
| `docs/requirements/DESIGN_PHILOSOPHY.md` | **NEW** — Cosmological framework, literary influences, design principles |
| `docs/requirements/PROJECT_SPEC.md` | **UPDATED** — Replaced individual weapon table with category+tag system; marked firearms as done |
| `simulations/melee_balance.py` | **NEW** — Analysis of old weapon table balance issues |
| `simulations/weapon_rebalance.py` | **NEW** — Validation of new category system vs armor soak |
| `docs/pending-tasks.md` | **UPDATED** — Marked firearms done, added new completed items |
| `docs/sessions/session-4-notes.md` | **NEW** — This file |

## Key Design Decisions

1. **Category+tag weapon system** — Inspired by Symbaroum. Categories define stats, tags add flavor. Dramatically reduces table size while increasing player expressiveness. "I want a claymore" = Great + Two-Handed. "I want a war pick" = Medium + Piercing.
2. **3% per accumulation point** (not 5%) — At 5%, three moderate casters shut down all firearms in 2 turns. At 3%, sustained heavy casting is needed to seriously threaten reliable firearms. Casters are a cost, not a liability.
3. **Asymmetric interference** — Magic always erodes tech. Only exotic tech erodes magic. Conventional tech is a victim, not a combatant. This creates three tiers of technology with different strategic roles.
4. **Malfunction mirrors backlash** — Same structural shape (base cost + severity table). Reduces cognitive load, reinforces thematic symmetry.
5. **Slow accumulation decay (1/minute)** — Lingering residue enables magical forensics, scene-spanning consequences, and tracking/counter-tracking. Over-emphasizes the tension intentionally.
6. **Invisible War cosmology** — Designer-facing only. The competing metaphysical forces structure consistency but are never confirmed in-world. "The moment you explain it, you kill it."
7. **Feel over simulation** — Weapon stats are tuned to evoke the fantasy of the weapon, not model physics. Complexity hidden in balanced numbers.

## Open Issues

- Accumulation decay rate may need playtesting — 1/minute might be too fast or too slow
- Firearm tag balance untested (especially Scatter +1d6 at close range)
- Crossbow reload times may need adjustment relative to firearms
- Ballistic vest with Reliability score — needs validation that it doesn't overcomplicate armor
- Exotic weapon Tech Accumulation generation rates need playtesting
- Full magic/tech zone mechanics still need dedicated design session

## Next Session

Continue design interview — pick from pending tasks: leveling/progression, factions, or zone mechanics.
