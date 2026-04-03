# Session 9: Rules Review, Ballistic/Martial Armor, Galvanic Weapons, Full UI Redesign

**Date:** 2026-04-03
**Goal:** Continue rules review for consistency, then complete UI redesign of the web rulebook and landing page

## Overview

Session split into two phases: rules review and corrections, then a complete visual redesign of the entire web presence.

The rules review caught several inconsistencies left over from session 8 decisions — the "always check Reliability" rule wasn't applied everywhere, the malfunction explanation used unnecessary reverse formulas, and the worked combat example had timing errors with accumulation and incorrect wild caster mechanics. The biggest design change was splitting armor into Ballistic/Martial ratings (inspired by Shadowrun) and redesigning Galvanic weapons from a generic stat table into 7 named weapons with unique abilities.

The UI redesign replaced the single-page rulebook with an 8-page documentation site using a completely new design system ("The Aetheric Codex"). The landing page was rewritten to be narrative-first, leading with world and story over mechanics.

---

## Changes Made

### Phase 1: Rules Review and Mechanical Changes

#### Reliability Always Checked
- Fixed firearms intro text that still said "conventional firearms skip the Reliability check in clean environments"
- Fixed cheat sheet that still had the old x3 multiplier (now x2)
- Rewrote malfunction section to use plain roll-under language instead of reverse formula ("malfunction chance = 100 - Reliability")
- Added malfunction severity roll to the worked example (Thug rolls d10, gets 3 = Click)

#### Ballistic/Martial Armor Split (NEW SYSTEM)
- Armor now has two soak ratings: **Ballistic** (firearms) and **Martial** (melee)
- Ballistic vest: B8/M2 — great against bullets, useless against blades
- Full plate: B4/M12 — turns swords, not bullets
- Chainmail: B2/M5 — rings stop blades, not bullets
- Shields get both ratings (wood shields have B0)
- All armor tables, shield tables, worked examples, and cheat sheet updated
- Piercing tag now specifies "Martial soak"

#### Galvanic Weapons Redesign (NEW SYSTEM)
- Replaced generic Exotic Pistol/Sidearm/Heavy/Melee stat table with 7 named weapons
- **Ranged:** Pneumatic Flechette (silent, piercing), Arc Gun (arcing, shocking), Galvanic Lance (lancing, suppressing, unstable), Spark Thrower (scatter, arcing)
- **Melee:** Force Blade (armor breaker -3 Martial), Shock Gauntlet (stun, shocking), Voltaic Whip (reach, entangling, arcing)
- Added Galvanic Keyword Reference table (Arcing, Armor Breaker, Lancing, Shocking, Silent, Stun, Suppressing, Unstable)
- Renamed "Aether Lance" to "Galvanic Lance" (it channels Engine forces, not Aetheric)

#### Worked Combat Example Overhaul
- Fixed accumulation timing: takes effect immediately when spell fires, not "after the count"
- Added Reliability rolls to every gunshot (always checked)
- Fixed wild caster mechanic: Sera takes the farther die (84, not 29), which is a misfire with consequences (2 EP, 1d6 damage, backlash check)
- Added Galvanic force generator scene: Thug B activates a sustained device that pulses -2 every 3 counts, pulling balance back toward neutral and eventually Galvanic
- Fixed math throughout (Reliability 87 not 83 for +4 accumulation, etc.)

#### Design Doc Updates
- Wild caster equidistant tie rule: caster chooses (MAGIC_SYSTEM.md)
- Misfires generate 0 accumulation (COMBAT_PROCEDURE.md, FIREARMS_EQUIPMENT.md)
- Cheat sheet: expanded wild suppression brackets, added misfire line

#### World Between Content Expansion (APPROVED)
- Added expanded Veil/Engine/Baseline cosmology descriptions
- Added terminology reference table (Veil, Engine, Aetheric, Galvanic, Balance, Conventional, Martial)
- Added "The Three Theories" callout (Immune Response, Rival Gods, Engineer's Shrug)

### Phase 2: UI Redesign

#### New Design System ("The Aetheric Codex")
- Deep blue-black palette (#080b14 base) replacing warm brown/parchment
- Playfair Display (headings), Source Serif 4 (body), JetBrains Mono (code), Cormorant Garamond (labels)
- Glassmorphic panels with backdrop-filter blur
- Animated particle canvas background (blue and gold motes)
- CSS mist animations (Aetheric blue, Galvanic amber)
- Gear-shaped SVG bullet points that rotate on hover
- Glowing electric dividers with spark animations
- Per-page color themes (aether, galvanic, neutral, split)

#### Multi-Page Rulebook
- Split single 2600-line page into 8 discrete pages
- Persistent sidebar TOC with scroll spy and active section tracking
- Compact breadcrumb nav above page hero
- Full prev/next navigation cards at bottom
- Collapsible sidebar on mobile
- Shared CSS (styles.css) and JS (main.js)

#### Landing Page Redesign
- Narrative-first structure: world and story before mechanics
- Evocative triptych (Veil / Engine / Bedrock) replacing mechanical descriptions
- Four scenario cards (Wild Zone, Resonance Lab, Jazz Club, Expedition)
- Mechanics framed as table experiences, not formulas
- Inline SVG icons (Lucide set) replacing system-dependent emoji
- Same design system as rulebook for visual consistency

---

## Files Modified

| File | Change |
|------|--------|
| docs/requirements/MAGIC_SYSTEM.md | Wild caster equidistant tie rule |
| docs/requirements/COMBAT_PROCEDURE.md | Misfires generate 0 accumulation |
| docs/requirements/FIREARMS_EQUIPMENT.md | Misfire accumulation row clarified |
| web/rules/index.html | Rewritten as Chapter 1 (Welcome) standalone page |
| web/rules/creating.html | NEW — Chapter 2 (Creating Your Adventurer) |
| web/rules/rolling.html | NEW — Chapter 3 (Rolling the Dice) |
| web/rules/getting-hurt.html | NEW — Chapter 4 (Getting Hurt) |
| web/rules/magic.html | NEW — Chapter 5 (The Two Paths of Magic) |
| web/rules/world-between.html | NEW — Chapter 6 (The World Between) with expanded cosmology |
| web/rules/combat.html | NEW — Chapter 7 (Combat) with Ballistic/Martial, Galvanic weapons, fixed example |
| web/rules/reference.html | NEW — Chapter 8 (Quick Reference) |
| web/rules/css/styles.css | NEW — Complete design system |
| web/rules/js/main.js | NEW — Sidebar, scroll spy, particles, page detection |
| web/index.html | Complete redesign — narrative-first, new design system, inline SVG icons |
| docs/sessions/session-9-notes.md | This file |

## Key Design Decisions

1. **Ballistic/Martial armor split** — Resolves the absurdity of a ballistic vest soaking less than plate armor. Different armor for different threats. Inspired by Shadowrun's Ballistic/Impact split.

2. **Galvanic weapons as unique items** — Each weapon has personality, abilities, and flavor like the tech side's answer to spells. Moved from generic stat categories to named weapons with keywords.

3. **Rulebook content is sacred** — Established that web rulebook text must never be changed without explicit user review and approval. Layout/design changes only; every word change goes through the designer.

4. **Per-page themes** — Magic pages use Aetheric blue, combat/tech pages use Galvanic amber, World Between uses both. The site visually embodies the tug-of-war.

5. **Narrative-first landing page** — Scenarios and world before mechanics. People need to want the stories before they care how the dice work.

## Open Issues

- Wild backlash modifier (+5% flat) still "working value" pending playtesting
- Concentration check ((PW+4)x10) still provisional
- Push Timing mechanic (rush actions) captured as TODO, not designed
- Zone formation mechanics still deferred
- Some pages (magic, world-between, combat) were rebuilt from git originals after agents incorrectly reconstructed content from design docs — should be verified for exact match
- Mobile sidebar UX needs testing on real devices
- Particle canvas performance on low-end devices untested

## Next Session
- Verify all page content matches approved rulebook text exactly
- Continue visual polish / iteration based on feedback
- Factions and Adventuring Societies design
- Leveling/progression mechanics
- Push Timing mechanic
