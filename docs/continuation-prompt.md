# Continuation Prompt

## Last Session (5) — Combat System & Base Mechanics Codification
- Created COMBAT_PROCEDURE.md: full timing track workflow, attacks, active defense, damage/soak, death saves, declaration order, range bands, malfunction integration, spell interruption, cheat sheet
- Rebalanced armor degradation (flat 25% chance, lose 1 soak) — validated by simulation
- Assigned fixed casting times to all 37 spells; 4 ritual spells (Shape Flesh, Transmute, Circle, Scry)
- Created BASE_MECHANICS.md: stats, skills, resolution, magic summary, one-page rules summary
- New mechanics: concentration check (PW+4)×10, declaration order (lowest PC first), cancellation = half Weak tier

## Current State
- Project is in **design exploration phase** — collaborative interview-driven design
- **Playtest-ready documents:** COMBAT_PROCEDURE.md, BASE_MECHANICS.md (with cheat sheets)
- **Complete (first pass):** Magic system, spell compendium (37 spells with fixed casting times), weapons (melee + firearms + exotics), armor/soak, malfunction/accumulation, design philosophy
- **Not yet designed:** Leveling, factions, zone mechanics, death saves (provisional), races, archetype names, skill list revision, currency

## Immediate Next Task
**Priority: Create a website — landing page and rules reference.**
- Model after `~/projects/card-game/web` (static HTML, GitHub Pages deploy structure)
- That repo has a comprehensive art pipeline: `docs/art/style-guide.md`, `docs/art/prompt-engineering/` (FLUX/SDXL templates, LoRA configs, generation settings), `docs/art/color-palettes.md`, consistency rules
- Establish equivalent art style guide for this project's 1920s steampunk pen-and-ink aesthetic (existing art in `art/` is B&W pen & ink)
- Create generation scripts and prompt templates for producing consistent artwork
- Build landing page (setting intro, tone, key features) and rules section (pull from BASE_MECHANICS.md and COMBAT_PROCEDURE.md)

## Key References
- `docs/requirements/COMBAT_PROCEDURE.md` — Full combat rules with cheat sheet
- `docs/requirements/BASE_MECHANICS.md` — Core mechanics with cheat sheet
- `docs/requirements/PROJECT_SPEC.md` — Setting, stats, weapons, armor
- `docs/requirements/MAGIC_SYSTEM.md` — Full casting rules
- `docs/requirements/SPELL_COMPENDIUM.md` — All 37 spells with fixed casting times
- `docs/requirements/FIREARMS_EQUIPMENT.md` — Firearms, malfunction, accumulation
- `docs/requirements/DESIGN_PHILOSOPHY.md` — Cosmology, literary influences
- `art/` — Existing B&W pen & ink art (cat, dragon, fantasy figure)
- `~/projects/card-game/web/` — Reference site structure (landing + rules + app)
- `~/projects/card-game/docs/art/` — Reference art pipeline (style guide, prompt templates, generation settings, LoRAs)
