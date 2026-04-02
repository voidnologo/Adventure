# Writing Style Guide

## Document Status: ACTIVE
**Last Updated:** 2026-04-01

This document defines how Adventure RPG content should be written, depending on who will read it.

---

## The Two Audiences

### Player-Facing Content

Anything a player, GM, or potential reader will see: the rulebook, website, quickstart guide, setting material, published adventures.

**Tone:** Literary, narrative, conversational. Like the best RPG rulebooks — Symbaroum, Shadowrun 3rd Edition, Black Sword Hack. The reader should enjoy reading the rules, not just tolerate them to extract information.

**Principles:**

1. **Lead with fiction, not formulas.** Every section opens with flavor text that grounds the reader in the world before any mechanics appear. The setting is not decoration — it's the reason the mechanics exist.

2. **Address the reader directly.** "You," "your character," "your GM." The reader is a person sitting at a table, not an abstract rules consumer.

3. **Use named characters in examples.** Not "Character A attacks Character B." Kael draws his sword. Sera channels the aether. The thug reaches for his revolver. Recurring characters build familiarity and make examples feel like actual play.

4. **Explain *why* before *what*.** Before presenting a mechanic, explain what it represents and why it exists. "Combat is dangerous in this game because heroes should think before they fight" comes before the wound tier table.

5. **Show, don't just tell.** "At the Table" callout boxes that read like actual play dialogue. Worked examples that feel like a story unfolding, not a math problem being solved. Visual character sheet mockups so readers can connect numbers to the physical artifact they'll hold.

6. **Conversational, not academic.** Write like someone explaining the game across a table. Short sentences are fine. Fragments are fine. Personality is fine. Don't write like a textbook.

7. **The cheat sheet comes last.** Dense reference material (tables, formulas, quick-reference cards) belongs at the end, after the reader understands the system through narrative explanation. The cheat sheet is a reminder, not a teacher.

**Examples of good player-facing writing:**

> *Magic came roaring into the world within living memory. Nobody fully understands it. Some study it with academic rigor, cataloguing incantations in leather-bound books. Others simply feel it — raw power flowing through them like a river they can barely steer.*

> Kael has PC +2 and puts 3 points into Melee: ((10 + 2) × 3) + 30 = **66%** — he hits about two-thirds of the time. Not bad for a former army officer who's been swinging a blade since basic training.

**Examples of bad player-facing writing:**

> Skill target numbers are calculated with the formula ((10 + associated stat modifier) × skill level) + 30.

> The death spiral applies cumulative penalties at each wound tier: Tier 2 = -10%, Tier 3 = -25%, Tier 4 = -50%.

Both of these are *accurate*, but they're not *enjoyable*. The information is there; the humanity isn't.

### Internal / Design Content

Session notes, design documents, simulation results, continuation prompts, pending tasks, project specs, balance analysis.

**Tone:** Technical, efficient, precise. Grids, charts, bulleted lists, formulas, tables — all fine. These documents serve as working reference for the design team, not as published material. Clarity and completeness matter more than readability pleasure.

**No restrictions on format.** Use whatever communicates the information most efficiently.

---

## Document Classification

| Document | Audience | Style |
|----------|----------|-------|
| Rulebook / rules website | Player-facing | Literary, narrative |
| Setting guide / worldbuilding | Player-facing | Literary, narrative |
| Quickstart / one-shot | Player-facing | Literary, narrative |
| Website landing page | Player-facing | Literary, narrative |
| Published adventures | Player-facing | Literary, narrative |
| PROJECT_SPEC.md | Internal | Technical |
| COMBAT_PROCEDURE.md | Internal | Technical |
| BASE_MECHANICS.md | Internal | Technical |
| MAGIC_SYSTEM.md | Internal | Technical |
| DESIGN_PHILOSOPHY.md | Internal | Technical (with some narrative) |
| Session notes | Internal | Technical |
| Simulation scripts/results | Internal | Technical |
| Continuation prompts | Internal | Technical |
| Pending tasks | Internal | Technical |

---

## Reference Styles

These RPGs exemplify the writing quality we're aiming for:

- **Symbaroum** — Atmosphere-first rules presentation. Every mechanic is grounded in the world of Davokar. Rules feel like they emerge from the fiction.
- **Shadowrun 3rd Edition** — Fiction vignettes between rules sections. Named characters (shadowrunners) in every example. The crunch is real, but it's wrapped in setting.
- **Black Sword Hack** — OSR minimalism with personality. Casual, direct tone. Rules are brief and explained through play, not abstraction.

The common thread: **rules as storytelling**, not rules as specification.

---

## Dice Roll Conventions

The game uses d100 for nearly everything, but there are **two distinct types of d100 roll** and they should be written differently.

### Ability Checks (Roll-Under)

Skills, attacks, concentration, weapon Reliability — anything where a character or object is *trying to succeed*. Roll d100 equal to or under a target number. Higher target = better odds.

**How to write:** State the target, then the result. *"Kael rolls against his Melee of 66. He gets a 31 — hit."*

Reliability checks are ability checks — the weapon is "trying to fire." *"Roll d100 against your weapon's Reliability. Under = it fires."*

### Consequence Checks (Percentage Chance)

Backlash, armor degradation, wild effects — anything where the rules impose a *flat probability of something happening*. There's no target number to improve. The odds are the odds.

**How to write:** State the percentage chance as plain English, then say whether it happened. Do NOT convert to a target number. Do NOT specify "roll under" or "roll over." The percentage IS the rule — the dice implementation is just "roll d100, compare to the percentage."

- **Good:** *"There's a 15% backlash chance. She rolls 67 — no backlash."*
- **Good:** *"25% chance the armor degrades. The GM rolls 18 — bad luck, it cracks."*
- **Bad:** *"Roll under 15 for backlash."* (Confuses roll-under with consequence checks)
- **Bad:** *"Roll over 75 to resist degradation."* (Introduces a roll-over convention)

The reader should think *"15% chance, did it happen?"* — not *"what number am I rolling against?"*

### Why This Matters

If everything is forced into roll-under language, consequence checks read like "rolling low = bad," which contradicts the core mechanic where rolling low = good. Keeping them as plain percentage chances avoids the confusion entirely.

---

## Setting Terminology: Aetheric & Galvanic

The game's two opposing forces have specific terminology. Use the right term for the context.

### The Sources (Cosmological)

| Term | What It Is | When to Use |
|------|-----------|-------------|
| **The Veil** | The boundary between the mundane world and the magical beyond. Where the Aether comes from. | When describing the cosmological source of magic, the nature of wild zones ("the Veil is thin here"), or the eruption event ("when the Veil thinned"). Formal, evocative, setting-level. |
| **The Engine** | The metaphysical wellspring of human industry and will. Where Galvanic force comes from. | When describing the cosmological source of exotic tech, the nature of industrial dead zones ("the Engine hums in these walls"), or the emergence of Galvanic technology. Formal, evocative, setting-level. |

### The Forces (Mechanical)

| Term | What It Is | When to Use |
|------|-----------|-------------|
| **Aether** (noun) | The raw magical force itself. | "The Aether poured through." "Drawing on the Aether." Refers to the force as a substance or presence. |
| **Aetheric** (adjective) | Relating to magic and its effects. | "Aetheric accumulation." "Aetheric residue." "Aetheric zone." Describes things touched by or measuring magic. |
| **Galvanic** (adjective) | Relating to exotic tech force and its effects. | "Galvanic accumulation." "Galvanic resonance." "Galvanic technology." Describes exotic devices and their environmental impact. |
| **Galvanic force** (noun phrase) | The counter-resonance generated by exotic tech. | "The Galvanic force pushed back against the Aether." Use when referring to the force itself rather than a specific device or measurement. |

### The Equipment

| Term | What It Is | When to Use |
|------|-----------|-------------|
| **Galvanic technology / Galvanic weapons** | Exotic steampunk devices that channel the Engine's force. | Formal/setting-flavored references. "Galvanic weapons are restricted in the factory district." |
| **Exotic** / **Exotics** | The same devices, described casually. | Mechanical/table-talk context. "She fires her exotic pistol." "Exotics always require malfunction checks." Interchangeable with "Galvanic" — one is the in-world term, the other is the player-shorthand. |
| **Conventional** | Normal firearms and technology. Not Galvanic. | "Conventional firearms don't shift the balance." Distinguishes regular guns from exotic ones. |
| **Martial** | Physical weapons immune to both forces. | "Martial weapons always work." Swords, crossbows, fists. |

### The Balance

| Term | When to Use |
|------|-------------|
| **Aetheric accumulation** | When the balance is tipped toward magic. "The area has +6 Aetheric accumulation." |
| **Galvanic accumulation** | When the balance is tipped toward tech. "The area has −4 Galvanic accumulation." |
| **The balance** / **Aetheric balance** | When discussing the sliding scale as a concept. "The balance is at net +3 Aetheric." |
| **Aetheric rating** | The per-device number on Galvanic weapons that determines how much they shift the balance per use. "This arc gun has an Aetheric rating of 2." |

### Balance in Examples

When writing worked examples, always show both sides of the scale in action. If an example demonstrates Aetheric accumulation from spellcasting, include a Galvanic counterpoint — an exotic weapon pushing back, a tech zone suppressing magic, or at minimum a note about what would shift the balance the other direction. The reader should always see the tug-of-war, not just one side of it.
