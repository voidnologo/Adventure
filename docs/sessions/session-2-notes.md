# Session 2: Magic System Design & Spell Compendium

**Date:** 2026-03-29
**Goal:** Continue design interview — define schools of magic, casting mechanics, spell lists, scholarly/wild caster paths, backlash, and build out full spell compendium.

## Overview

Deep-dive session on the magic system, spanning two conversation blocks. Established the tiered casting mechanic (inspired by DCC's variable spell results mapped onto the existing d100 percentile system), defined six schools of magic with 37 total spells, designed the scholarly vs. wild caster paths with meaningful mechanical differences, and worked out the full casting pipeline: misfire, backlash (with escalating wild effect table), exhaustion overflow, tier suppression for wild casters, and opposed checks as a core system mechanic.

In the second block, completed the full first-pass spell compendium — all 37 spells across 6 schools with complete tier tables (Weak/Standard/Strong/Spectacular/Misfire), exhaustion costs, casting times, and effect descriptions. Established "rulings over rules" as a core design pillar — concrete mechanical anchors that GMs can interpret flexibly, with a careful distinction between vague mechanics (bad) and narrative flavor (fine).

---

## Changes Made

- [x] Defined 6 schools of magic with thematic identities (37 spells)
- [x] Designed tiered casting mechanic (Misfire/Weak/Standard/Strong/Spectacular)
- [x] Hard caps based on casting target number
- [x] Scholarly vs wild caster paths with full mechanical differentiation
- [x] Wild caster variance: 2d100 take farther from target, +10 casting bonus (probability verified with real math)
- [x] Wild caster tier suppression: 0/1/2/3 tiers based on 25% skill brackets
- [x] Backlash: 1d4 flat damage + 25% chance of Wild Effect (d10 table, 3-tier escalation to permanent)
- [x] Exhaustion overflow: spell fires, excess converts to physical HP damage at half rate
- [x] Casting interruption: noted as open design question with timing track interaction
- [x] Opposed check mechanic: added to core rules (PROJECT_SPEC.md §3.1b)
- [x] Six template spells designed in detail: Force, Mend, Shield, Reveal, Reshape, Sever
- [x] Hidden cost formula validated across Complexity 1-4
- [x] Full spell compendium: all 37 spells with complete tier tables
- [x] "Rulings over rules" added as design pillar #6 in PROJECT_SPEC
- [x] Vague mechanical language cleaned up across spell compendium

---

## Files Modified

| File | Change |
|------|--------|
| `docs/requirements/MAGIC_SYSTEM.md` | **NEW** — Full magic system design: philosophy, paths, casting mechanics, backlash, wild effects, 6 template spells |
| `docs/requirements/SPELL_COMPENDIUM.md` | **NEW** — All 37 spells with complete tier tables, complexity assignments, cost formula reference |
| `docs/requirements/PROJECT_SPEC.md` | Added opposed check mechanic (§3.1b), "rulings over rules" design pillar, updated magic section and open questions |
| `docs/sessions/session-2-notes.md` | **NEW** — This file |
| `docs/pending-tasks.md` | Updated throughout session |
| `docs/continuation-prompt.md` | Updated at session end |

## Key Design Decisions

1. **DCC-inspired tiered casting on d100** — Roll determines tier available (Weak/Standard/Strong/Spectacular). Not just pass/fail.
2. **Hard caps from stats** — A target of 30 can NEVER achieve Strong. Power ceiling is built into ability, not luck.
3. **Scholarly vs Wild** — Scholarly: spellbook, choose tier freely, lower backlash. Wild: entire domain, 2d100 extreme variance, +10 bonus, limited tier suppression.
4. **Wild caster tier suppression** — Can step down 0/1/2/3 tiers based on 25% skill brackets. Novices are chaotic, masters learn control. Mirrors crit range mechanic. Solved the problem of high-power wild casters being forced into Spectacular costs they don't want.
5. **Concept-based spells** — "Elemental Manipulation" covers fire through lightning. GM and player interpret specifics within tier guidelines.
6. **Misfire and Backlash are separate** — Misfire is spell-specific (healing drains instead). Backlash is raw energy burn (1d4 + wild effect chance). You can succeed and still get backlash.
7. **Backlash escalation** — Wild effects escalate per-effect if same number rolled while active. Third instance = permanent stat reduction. Fear of escalation naturally limits casting without needing hard daily limits.
8. **Exhaustion overflow** — Spell fires even if you can't pay. Overflow → physical HP damage at half rate. Enables heroic sacrifice moments.
9. **Opposed checks** — Core system mechanic, not magic-specific. Both roll d100 vs relevant target, larger margin wins. Applies everywhere: Sever resistance, arm wrestling, chases, stealth vs observation.
10. **No separate "magical damage"** — Shield absorbs all damage equally. Mechanical consistency over special subsystems.
11. **Rulings over rules** — Core design pillar. Concrete mechanical anchors for GM interpretation. Not vague ("partially blocks" = bad), but trusting English and context for narrative consequences ("nearby allies may be caught" = fine).
12. **Cost formula** — Complexity 1-4 drives all spell costs. Consistent, predictable, but hidden from players. Designers use it; players see final numbers.

## Open Issues

- Push It mechanic needs exact costs/risks
- Wild vs Scholarly exact backlash rate modifier
- Scholarly bonus to school count
- Casting interruption/concentration check mechanics
- Spell interaction with magic/tech zones
- Mid-campaign spell learning for scholarly casters
- Weapon timing table may need rebalancing relative to casting times
- Spell compendium is first pass — individual spells may need tuning after playtesting

## Next Session

Continue design interview:
1. Firearms and steampunk equipment tables
2. Leveling/progression mechanics
3. Faction design
4. Magic/tech zone interference rules
