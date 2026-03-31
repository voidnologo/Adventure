# Session 3: Magic System Balance Simulation

**Date:** 2026-03-30
**Goal:** Build a reusable Python simulation framework to stress-test the magic system's balance across power levels and caster paths.

## Overview

Built a complete simulation framework in `simulations/` that generates realistic casters at four power levels (low/mid/high/master) for both scholarly and wild paths, then runs them to exhaustion casting a random mix of all 37 spells. The simulation uses a power-maximizing strategy — casters use the highest tier they can afford without overflowing into HP damage, which reflects actual play behavior (you want the power, the constraint is not burning yourself out).

Iterated through three versions of the simulation strategy before landing on the right model. First attempt defaulted to always-choose-Weak (unrealistic min-maxing). Second showed raw vs final tier distributions. Final version models "use highest affordable tier" with casts-before-exhaustion as the core metric. Also applied a key design change: capped wild caster tier suppression at 2 (down from 3 at master level) — you can only squash the magic so much.

## Key Findings

1. **Scholarly casters get ~10-11 casts per MP pool; wild casters get ~7-8.** The ~30% fewer casts is the real cost of wild power. This holds across all power levels.

2. **Wild casters hit dramatically higher tiers.** At master level, 60% of wild successes are Spectacular (vs 33% scholarly). At high level, 44% Spectacular (vs 14% scholarly). The dice push wild results to extremes as intended.

3. **The suppress cap at 2 creates meaningful cost pressure.** With the old cap of 3, master wild casters could always suppress to Weak — trivializing costs. At cap 2, master wild casters land at Strong/Spectacular 71% of the time, burning MP fast. This is the lever that prevents wild from being strictly better at high levels.

4. **Backlash is the real wild tax.** Wild backlash rates are roughly double scholarly (~16-24% vs ~5-15%) because wild casters are using higher tiers more often AND have the +5% modifier. Per session, wild casters take 1-4 more backlash HP than scholarly.

5. **Wild effect permanents are negligible.** Across 500 sessions per config, zero permanents in most configs. The escalation mechanic works as intended — a fear factor, not a statistical reality. Rolling the same d10 result 3x while active is astronomically unlikely.

6. **Exhaustion overflow is common but survivable.** ~67-70% of sessions end with an overflow cast (the last spell costs more than remaining MP). Average overflow HP damage is under 2 points. This is the "heroic last spell" moment working as designed.

7. **Misfire gap at high levels is significant.** Master wild casters misfire only 5% vs scholarly 27%. The +10 bonus makes wild casters extremely reliable — offset by higher costs per cast and less spell variety.

## Balance Assessment

The system is well-balanced for low-to-mid tier play (where most campaigns live):
- At **low level**, the gap is small (~1.4 fewer casts for wild) with wild paying through higher backlash
- At **mid level**, gap widens to ~2.7 casts — meaningful but not crippling
- The real tradeoffs aren't captured in numbers alone: scholarly gets any school + full tier control at all levels; wild gets 1-2 schools + power but limited control

At **high/master** the numbers favor wild heavily on raw power, but this is offset by:
- Fewer spells known (1-2 schools vs potentially all)
- No spellbook = can't prepare specific spells for specific situations
- Higher backlash = more HP damage and wild effect risk per session
- Less control = sometimes paying for Spectacular when Standard would suffice

## Design Change Applied

- **Wild tier suppression capped at 2** (was 0/1/2/3 by bracket, now 0/1/2/2). Updated in `simulations/config.py`. This needs to be reflected back in MAGIC_SYSTEM.md when the design is finalized.

---

## Files Modified

| File | Change |
|------|--------|
| `simulations/config.py` | **NEW** — All tweakable parameters: power levels, MP pools, tier thresholds, backlash rates, spell costs, all 37 spells |
| `simulations/engine.py` | **NEW** — Core simulation engine: casting rolls, tier determination, suppression, backlash, wild effects, overflow |
| `simulations/run_analysis.py` | **NEW** — Full analysis runner: sessions to exhaustion, complexity breakdowns, head-to-head comparisons, automated balance flags |
| `simulations/results/balance_report.txt` | **NEW** — Full simulation output with all metrics |
| `docs/sessions/session-3-notes.md` | **NEW** — This file |
| `docs/pending-tasks.md` | Updated with simulation tasks and new backlog items |
| `docs/continuation-prompt.md` | Updated for session 4 |

## Key Design Decisions

1. **Power-maximizing strategy** — Simulating players who want effect power, not cost optimization. The real constraint is "don't overflow into HP damage," not "always pick Weak."
2. **Casts-before-exhaustion as core metric** — How many times can you cast before your pool runs dry? This captures sustainability better than per-cast averages.
3. **Suppress cap at 2** — Master wild casters can no longer suppress all the way to Weak. They're stuck paying for Strong/Spectacular 71% of the time. You can only squash the magic so much.
4. **Mixed spell selection** — Simulation draws randomly from all 37 spells weighted by complexity distribution, reflecting realistic play where casters use a variety of spells.

## Open Issues

- Suppress cap of 2 needs to be reflected back into MAGIC_SYSTEM.md (currently says 3 at 76+)
- Wild backlash modifier (+5% flat) is still TBD in the rules — simulation uses this as default
- Individual spell tuning not yet addressed (compendium is first pass)
- No modeling of Push It mechanic, spell cancellation, or casting interruption

## Next Session

Continue design interview — firearms, leveling, factions, or zone mechanics per pending-tasks.md.
