# Continuation Prompt

## Last Session (3) — Magic System Balance Simulation
- Built reusable Python simulation framework in `simulations/`
- Power-maximizing strategy: casters use highest tier they can afford without overflow
- Key finding: scholarly gets ~10-11 casts/pool, wild gets ~7-8 but at much higher tiers
- Applied design change: wild tier suppression capped at 2 (not 3 at master)

## Current State
- Project is in **design exploration phase** — collaborative interview-driven design
- Magic system substantially complete (first pass) with simulation data to inform tuning
- Spell compendium complete (first pass, 37 spells)
- Need to propagate suppress cap change back to MAGIC_SYSTEM.md
- No firearms, leveling, factions, or zone mechanics yet

## Immediate Next Task
Continue design interview. Pick from pending-tasks.md Next Up:
1. Firearms & steampunk equipment tables
2. Leveling/progression mechanics (Mouse Guard / Symbaroum inspired)
3. Major factions and Adventuring Societies
4. Magic/tech zone interference rules

## Key References
- `docs/requirements/MAGIC_SYSTEM.md` — Full casting rules, tier system, backlash, wild effects, exhaustion overflow
- `docs/requirements/SPELL_COMPENDIUM.md` — All 37 spells with tier tables
- `docs/requirements/PROJECT_SPEC.md` — Core mechanics, stats, design pillars
- `docs/pending-tasks.md` — Prioritized task list
- `simulations/` — Balance simulation framework (config.py for tweakable params, run_analysis.py to execute)
- `simulations/results/balance_report.txt` — Latest simulation output
- `rules/FunzieRulez.pdf` — Original prototype rules
