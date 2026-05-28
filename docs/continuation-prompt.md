# Continuation Prompt

## Last Session (34) — Story 03 Edit Pass + Publish

- Addressed PR #2 reviewer feedback (17 comments across ch03–ch08 plus ch01 continuity fix): compass restored to canon (locks in Galvanic, spins in Aetheric; Sera navigates by feel), Barrier dome rewritten to push outward with an active release-tension sequence, EP counts stripped from Aldric's POV
- Refactored `web/_data/fiction.js` from hard-coded story-02 loader into a config-driven `buildStory(config)` helper; Story 02 and Story 03 both pass through the same pipeline
- Added `web/fiction/the-lamplighters-price.njk` reader template; fiction index now lists Story 03 above Story 02
- PR #2 retitled (dropped "(draft)"), body updated, merged. Story 03 is live.

## Previous Session (33) — Story 03 Draft Written

- Revised plan for mechanics-as-narrative, updated series bible with Story 02 outcomes, wrote all 8 chapters

## Current State
- **Game title:** Aetherfall (repo: voidnologo/aetherfall)
- **Build:** Eleventy 3.x — `npm run dev` / `npm run build` — deploys via GitHub Action with `--pathprefix=/aetherfall/`
- **Path rule:** use relative paths in new pages, or run absolute paths through the `| url` filter. Raw `/foo` breaks at the subpath.
- **Website:** 18 chapters + quickstart (.njk) + character sheets + interactive tools + `/fiction/` landing + reader (Stories 02 & 03 live)
- **Fiction:** 6 world reference docs in `fiction/world/`; Stories 02 and 03 published; Story 04 pending (combat-focused)
- **Fiction data loader:** `web/_data/fiction.js` — config-driven via `buildStory(config)`; add new stories as a config entry + reader template
- **Art pipeline:** `art/{type}/{generated|approved|archived}/` — art NEVER deleted, only moved
- **Art generation:** `python tools/comfyui_generate.py` — builds flux-dev workflows, queues via ComfyUI API
- **Founding event:** "The Tear" (was "the Eruption" — renamed session 27)
- **CRITICAL RULE:** Rulebook content must NEVER be changed without explicit user approval.
- **CRITICAL RULE:** Art is NEVER deleted. Moves through generated -> approved or generated -> archived.

## Immediate Next Tasks
- **Plan Story 04** — combat-focused story in the series arc (Kael-heavy, timing track, damage, Galvanic devices, weapon reliability)
- Update series bible with final Story 03 outcomes before or alongside Story 04 planning
- Cross-device reading test of published fiction reader

## Key References
- Fiction world docs: `fiction/world/01-the-world.md` through `06-series-bible.md`
- Story 02 chapters: `fiction/stories/story-02/ch01.md` through `ch10.md`
- Story 03 chapters: `fiction/stories/story-03/ch01.md` through `ch08.md` (+ `PLAN.md`)
- Fiction web data: `web/_data/fiction.js` (config-driven)
- Fiction web templates: `web/fiction/index.njk`, `web/fiction/what-the-mill-remembered.njk`, `web/fiction/the-lamplighters-price.njk`
- Style guide: `fiction/world/05-style-guide.md`
- Magic system: `docs/requirements/MAGIC_SYSTEM.md`
- Spell compendium: `docs/requirements/SPELL_COMPENDIUM.md`
- Character sheets: `web/_data/characters/*.json`

## Color Reference
- **Aether:** `#3dc8e0` | **Galvanic:** `#e8a825` | **Background:** `#080b14`
- **Fonts:** Playfair Display (headings), Source Serif 4 (body), Cormorant Garamond (labels)
