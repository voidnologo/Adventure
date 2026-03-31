# Adventure RPG - Project Specification

## Document Status: DRAFT - In Development
**Last Updated:** 2026-03-31
**Status:** Active design exploration phase. Many sections require further discussion.

---

## 1. Project Vision

A rules-lite, OSR-inspired tabletop RPG set in a 1920s-flavored secondary world where magic has recently erupted into reality, colliding with rapidly advancing technology. The tone is heroic adventurers standing against encroaching darkness — not grimdark nihilism, but a world with real evil where the players are genuinely good people trying to make things better.

### Design Pillars

1. **Theater of the Mind** — No minis, no maps, no movement ranges or cones. Fully playable with a rulebook, character sheets, and a handful of dice around a table.
2. **Rules-Lite but Meaningful** — A 1-page cheat sheet + character sheet should cover 90% of play. Spell/item lookups as needed. No bloat, no complexity for variety's sake.
3. **OSR Lethality** — Combat is dangerous. The death spiral (wound penalties) means getting hurt forces tactical decisions. Character death is not common but is expected. Players should think before they fight.
4. **Mechanical Consistency** — Everything works the same way mechanically. One core resolution system, not special subsystems for every situation.
5. **Magic is Wondrous and Wild** — Magic is new, poorly understood, and dangerous. The world is still grappling with its emergence. It inspires awe and fear in equal measure.
6. **Rulings Over Rules** — The GM has authority to interpret and adjudicate. Crunch exists to smooth gameplay and set flavor, not because mathematicians mapped optimal balance points. However, "rulings over rules" does not mean "be vague." Every mechanic must provide concrete anchor points (numbers, durations, clear conditions) that the GM can interpret flexibly. "Absorbs 8 points of damage" is good — the GM decides the narrative. "Partially deflects damage" is bad — the GM has to guess the mechanic. Give solid mechanical floors, then trust the table to adjudicate from there. This game is not designed for a general audience. It is designed for people who want to play it.

---

## 2. Setting

### 2.1 The World

A secondary world (not Earth, but Earth-like) in a period analogous to the 1920s. Jazz clubs, tommy guns, industrialization, airships — but magic has recently erupted from the aether and transformed everything.

**Not Earth, but familiar.** The cultures, technology level, and social structures mirror the real-world 1920s closely enough that players can ground themselves without needing a 50-page gazetteer.

### 2.2 The Central Tension: Magic vs. Technology

This is the defining feature of the setting and the in-world justification for the full range of equipment and playstyles.

- **Magic disrupts technology.** In areas of high magical concentration, human-refined technology becomes unreliable and unpredictable. Guns may misfire, overheat, or melt. Engines stall. Airships lose power. Electrical systems short out.
- **Technology suppresses magic.** In heavily industrialized, engineered environments, magic wanes. Spells fizzle or misfire. Connections to mana flows are dampened or severed. Magical items lose potency.
- **This is why swords still matter.** A steel blade works everywhere. A tommy gun might betray you in a magical ruin. A spell might fail you in the heart of the factory district. Smart adventurers carry both — and know when to rely on which.

### 2.3 Magic Zones & Tech Zones

The world has varying concentrations of magic and technology:

- **Wild Zones** — Pockets of intense magical concentration in remote, lost, and unknown parts of the world. Legends arise from these places. They give rise to monsters, mutate the landscape, and contain powerful artifacts. Technology is extremely unreliable here.
- **Urban Bleed Zones** — Magic sometimes bubbles up in the middle of cities, warping and mutating neighborhoods into abandoned mystical zones. These are sudden, unpredictable, and terrifying to the populace.
- **Industrial Dead Zones** — Heavily industrialized cities that kill and drain the magic around them. High-tech gadgets flourish. Spells don't function. Magical creatures avoid these places.
- **The In-Between** — Most of the world exists in a spectrum between these extremes, where both magic and technology function but neither perfectly.

### 2.4 Tone & Theme

- **Heroic, not nihilistic.** Players are good people doing good things. Not amoral murder hobos.
- **"We can make the world a better place."** Adventurers should feel motivated by purpose.
- **Real evil exists.** Cultists resurrecting dead gods. Beasts of legend. Technological monstrosities. People trying to corrupt and pervert both systems — creating magically-activated cybernetic mutations that corrupt the soul and degrade everything around them.
- **Noir-tinged.** City adventures have a noir investigation feel. Moral complexity in NPCs and situations, but the PCs have a moral compass.
- **Wonder and dread.** Magic is new and wondrous. The world is exciting and terrifying in equal measure.

### 2.5 Adventuring Societies

The primary organizational structure for player characters. Societies provide:
- Resources and funding
- Training and mentorship
- Gear and equipment
- Support personnel and contacts
- Missions and purpose

Societies are drawn from various **factions** and serve different masters:
- Cult hunters for religious organizations (e.g., Vatican-equivalent)
- Monster eradication teams for government agencies
- Artifact recovery expeditions for powerful corporations
- And others (TBD — further faction design needed)

### 2.6 Factions (To Be Developed)

A handful of distinct factions that drive the world's politics and conflicts. Each provides different types of Adventuring Societies with different missions, resources, and moral entanglements. Specific factions to be designed in a future session.

---

## 3. Core Mechanics

### 3.1 Resolution System

**Percentile (d100) roll-under.** Success is determined by rolling equal to or under your target number.

- **00 (double zeros):** Always a critical miss.
- **01:** Always a critical hit.
- **Critical range:** For every 25% of your skill rating, you gain 1 point of crit range at the top end. (0-25: 0 crit range; 26-50: 1; 51-75: 2; 76-99: 3). Crits are counted down from your skill value. *Example: Skill 59 = crit range 2, so rolls of 57-59 are critical successes.*
- **Critical hits:** Double damage on attacks. Spectacular success on skill checks with a narrative bonus.

### 3.1b Opposed Checks

When two characters act in direct opposition — resisting a spell, arm wrestling, chasing, sneaking past a guard — both sides roll d100 against their relevant stat or skill target number.

**Resolution:**
- **Both succeed:** Whoever succeeded by the **larger margin** (target number minus roll) wins.
- **One succeeds, one fails:** The one who succeeded wins.
- **Both fail:** Stalemate — the situation doesn't change. GM adjudication.

**Examples:**
- **Sever vs caster:** Ley Weaver rolls casting target, defending caster rolls PW to resist. Larger margin wins.
- **Arm wrestling:** Both roll PP. Larger margin wins.
- **Chase:** Both roll Running. Larger margin gains or closes distance.
- **Stealth vs Observation:** Sneaker rolls Stealth, watcher rolls Observation. Larger margin determines if they're spotted.
- **Resisting Persuasion:** Speaker rolls Persuasion, target rolls an appropriate resistance (AW, SP, or relevant skill — GM decides based on how they're resisting).

This is the same d100 roll-under system used everywhere else. Higher-skilled characters naturally win opposed checks more often because they have higher target numbers and therefore larger possible margins. No special modifiers needed.

### 3.2 Stats

Six stats, rated from **-3 to +3**:

| Abbr | Stat | Covers |
|------|------|--------|
| PP | Physical Prowess | Strength, brawn, endurance, fortitude |
| PC | Physical Coordination | Grace, dexterity, finesse |
| IN | Intellect | Knowledge, intelligence, quick-thinking, academics |
| SP | Social Prowess | Etiquette, refinement, social standing, poise, likability |
| AW | Awareness | Perception, alertness, eye-for-detail |
| PW | Power | Magical ability, strength, attunement |

**Character creation:** GM sets a challenge level. Default is a net bonus of **+1** across all stats. Players describe roleplay reasons for each stat value.

### 3.3 Skills

**Skill target number formula:**
```
((10 + associated stat modifier) × skill level) + 30
```

**Unskilled attempt formula:**
```
(5 + associated stat) × 10
```

**Skill cap:** Up to 15 skills per character.

**Skill points per group:**
```
10 + stat group net modifiers
```

**Stat Groups:**
- **Physical:** PP, PC
- **Mental:** IN, AW
- **Social:** SP

#### Skill List

**Physical (PC) — Coordination:**
Athletics, Brawl (Combat), Conceal, Melee (Combat)

**Physical (PP) — Prowess:**
Climbing, Ranged (Combat), Running, Swimming

**Mental (AW) — Awareness:**
Empathy, Forgery, Hunting, Observation, Ride/Drive, Security, Stealth

**Mental (IN) — Intellect:**
Acting, Boating, Disarm Trap, Disguise, Engineering, Medicine, Metalworking, Music, Repair, Science, Survival, Tactics, Woodworking

**Social (SP):**
Business, Etiquette, Gambling, Interrogation, Leadership, Persuasion

> **NOTE:** Skill list may need revision for steampunk setting. Consider additions like: Demolitions, Pilot (airship), Arcana/Occult Lore, Streetwise, Intimidation, Firearms-specific skills, Magitech. Further discussion needed.

### 3.4 Classes (Archetype Labels)

Classes are **descriptive shorthand**, not mechanical restrictions. Think Shadowrun: you spend build points and can spec into anything, but your build naturally gravitates toward an archetype.

The "class" field on the character sheet is a **label for how you envision playing** — not a rules gate. A "Smoke Surgeon" and a "Gutter Knight" use the same skill system; they just invested differently.

> **NOTE:** Archetype names to be developed. Should be setting-flavored (not generic Fighter/Thief/Mage). Examples to brainstorm: Artificer, Channeler, Gutter Knight, Smoke Surgeon, Relic Hunter, Wardbreaker, etc.

### 3.5 Races

**Deferred.** To be discussed in a future session. May include non-human options, magical mutations, or may remain human-only. TBD.

---

## 4. Combat

### 4.1 Timing Track (No Initiative)

Combat uses a **timing track** instead of traditional initiative. This is a core differentiating feature of the system.

- When a scene begins where timing matters, a marker is placed on the timing track.
- Players announce when they begin an action and place a token on the square when their action will **complete**.
- If multiple actions complete simultaneously, they resolve in the order of whoever started their action first.
- A player can cancel an action at any time and begin a new one with a **penalty of one additional count**.

#### Action Timing Reference

| Time | Action |
|------|--------|
| 1 | Shout a command; manipulate a door; toss something; turn around |
| 2 | Go through a closed door; draw most weapons; pick up something; throw an item |
| 3 | Drink a vial; retrieve item from a sack |
| 4 | — |
| 5 | Mount a horse; light a torch |
| 6 | Climb a 10' ladder; light a lantern |
| 7 | — |
| 8 | — |
| 9 | Retrieve item from a backpack |
| 10 | Drink a flask; climb a 10' rope |

> **NOTE:** This table needs expansion for steampunk/magic actions: reloading firearms, activating gadgets, starting vehicles, etc.

### 4.2 Weapons — Category System

Weapons use a **category-based system** rather than individual stat lines. Each category defines the Speed and Damage; players choose a specific weapon within the category for narrative flavor. A longsword and a battle axe are both **Medium** — the player picks what fits their character.

#### Melee Weapons

| Category | Speed | Damage | Examples |
|----------|-------|--------|----------|
| Unarmed | 2 | 1d3+PP | Punch, kick, headbutt |
| Small | 2 | 1d4 | Knife, dagger, stiletto, knuckle dusters |
| Light | 3 | 1d6 | Short sword, hatchet, club, baton, rapier |
| Medium | 5 | 1d8+1 | Longsword, battle axe, mace, saber, warhammer, spear |
| Heavy | 7 | 1d10+1 | Bastard sword, morning star, heavy mace, war flail |
| Great | 9 | 2d6 | Greatsword, halberd, great axe, claymore, polearm |

**Balance note:** Lighter weapons are more damage-efficient per timing count against unarmored targets. Heavier weapons penetrate armor soak better — a knife can't hurt someone in chainmail, but a greatsword gets through 72% of the time. Speed vs. armor penetration is the core tradeoff. No weapon category is strictly better; the right choice depends on the opponent.

#### Ranged Weapons (Martial)

Martial ranged weapons are immune to magic zone interference. Crossbows require reloading; bows do not.

| Category | Speed | Damage | Reload | Examples |
|----------|-------|--------|--------|----------|
| Light Ranged | 5 | 1d6 | — | Short bow, sling |
| Medium Ranged | 7 | 1d8+1 | — | Composite bow, longbow |
| Light Crossbow | 7 | 2d6 | 6 | Hand crossbow, light crossbow |
| Heavy Crossbow | 10 | 3d6 | 10 | Heavy crossbow, arbalest |

#### Weapon Tags

Tags differentiate weapons within the same category. A longsword and a mace are both **Medium**, but one has **Piercing** and the other has **Crushing**. Each weapon gets 1–2 tags chosen at character creation (with GM approval). Tags also apply to firearms (see [FIREARMS_EQUIPMENT.md](FIREARMS_EQUIPMENT.md)).

| Tag | Effect | Typical Weapons |
|-----|--------|-----------------|
| Concealable | Can be hidden on person. Draw speed 1 | Knife, dagger, derringer, stiletto |
| Throwable | Can throw as ranged attack at +2 speed, one die step lower damage | Hatchet, spear, throwing knife |
| Reach | Can strike before an approaching enemy closes to melee range | Spear, halberd, glaive, polearm |
| Piercing | Ignores 2 points of armor soak | Stiletto, war pick, rapier, spear |
| Crushing | On armor degradation, overflow counts 1-for-1 instead of 2-for-1 | Mace, warhammer, morning star, war maul |
| Parrying | +10% to active defense rolls when wielded | Rapier, sword-and-buckler, quarterstaff |
| Entangling | On hit, target's next action costs +2 speed | Whip, flail, chain |
| Two-Handed | Requires both hands (already factored into category damage) | Greatsword, halberd, great axe |
| Versatile | Can use one- or two-handed. Two-handed: one die step up | Bastard sword, spear |

#### Firearms & Steampunk Exotics

> **Full firearms design document:** [FIREARMS_EQUIPMENT.md](FIREARMS_EQUIPMENT.md)
>
> Firearms are significantly more lethal than melee (roughly 2x damage efficiency at comparable speeds). The tradeoff is Magic Accumulation — spellcasting in the area degrades firearm Reliability, causing jams, misfires, and failures. Steampunk exotic weapons are rarer, less reliable, and generate Tech Accumulation that penalizes enemy spellcasting. See FIREARMS_EQUIPMENT.md for full tables, the malfunction system, and accumulation rules.

### 4.3 Armor & Degradation

Armor absorbs (soaks) damage but can be **degraded** when hit hard.

**Degradation rule:** If damage exceeds armor's soak value, for every 2 points over, there is a 25% chance of degradation. If the roll fails, armor's soak is permanently reduced by the overflow amount.

*Example: Chainmail (soak 5) takes 8 damage. 3 over = 25% chance of degradation. On failure, chainmail drops to soak 2.*

| Armor Type | Soak | Hinder |
|------------|------|--------|
| Cloth | 0 | — |
| Heavy Cloth | 1 | — |
| Leather | 2 | — |
| Scale | 3 | — |
| Chainmail | 5 | — |
| Half Plate | 8 | 1 |
| Full Plate | 12 | 2 |

| Shield Type | Soak | Hinder |
|-------------|------|--------|
| Wood Buckler | 2 | — |
| Steel Buckler | 3 | — |
| Wood | 5 | — |
| Infantry | 7 | — |
| Kite | 9 | 1 |
| Knight | 10 | 2 |

> **NOTE:** "Hinder" mechanic is referenced but not fully defined. Presumably applies as a penalty to certain actions (stealth, agility, spellcasting?). Needs clarification. Also: how does armor interact with magic zones? Can armor be enchanted?

---

## 5. Health & Damage

### 5.1 Hit Points

**Formula:** 7 + PP per health level.

Four wound tiers with escalating penalties (death spiral):

| Level | Status | Penalty |
|-------|--------|---------|
| 1 | OK | None |
| 2 | Harmed | -10% to all rolls |
| 3 | Maimed | -25% to all rolls |
| 4 | Incapacitated | -50% to all rolls |

**Typical HP range:** 20-32 total (5-8 per level). A single heavy hit (e.g., shotgun blast, heavy crossbow) can push a character into Harmed or Maimed territory immediately.

### 5.2 Death & Dying

When a character is reduced past Incapacitated: **death saves** (mechanics TBD). Teammates have a window to intervene and save you.

> **NOTE:** Death save mechanics need design. Options to discuss: flat percentage roll each round? Escalating difficulty? Bleed-out timer? Permanent injury tables for near-death experiences?

### 5.3 Recovery

- **Magical exhaustion:** Recover 1d8 per hour of full rest.
- **Physical damage:** Recover 1d4 per hour of full rest.

> **NOTE:** Recovery rates may need balancing. Consider: medical treatment bonuses, magical healing, long-term injury rules.

---

## 6. Magic System

> **Full magic system design document:** [MAGIC_SYSTEM.md](MAGIC_SYSTEM.md)

### 6.1 Summary

Magic is new, wild, dangerous, wondrous, and feared. Casting uses a **tiered results system** (inspired by DCC): roll d100, and how well you roll determines what tier of effect is available (Misfire / Weak / Standard / Strong / Spectacular). Each spell is a broad concept with a full tier table describing effects, costs, and casting times at each level.

**Two Paths:** Scholarly casters have spellbooks, can choose their tier, and have lower backlash. Wild casters can cast any spell in their schools but are locked to whatever tier the magic gives them, with higher backlash risk. Spells are concept-based — broad tools that players and GMs interpret within structured scope/scale guidelines.

**Six Schools, 37 Spells:**
- Aetheric Manipulation (7) — raw force, energy, elemental power
- Vivimancy (7) — life, body, biology
- Warding (6) — protection, sealing, banishment
- Divination (6) — perception, knowledge, detection
- Transmutation (6) — altering matter and properties
- Ley Weaving (5) — manipulating magic itself

**Dark Magic** is NOT player-accessible. It is a setting-level evil.

**Supernatural Entities** (ancient beings, beasts of legend) exist but are rare, alien, and not understood. Interaction is more Cthulhu than D&D — unsettling and never fully within the caster's control.

### 6.2 Key Mechanics (see MAGIC_SYSTEM.md for full details)

- **Tier qualification** based on roll margin: 1-10 under = Weak, 11-30 = Standard, 31-50 = Strong, 51+ = Spectacular
- **Hard cap** from casting target number (e.g., target 30 can never reach Strong)
- **Costs per tier** built into each spell using hidden design parameters (complexity, scope, duration, unnaturalness)
- **Backlash** is separate from misfire, scales with tier used (5%/10%/15%/25%)
- **Push It** mechanic for trying to exceed your result at additional cost/risk
- **Exhaustion track** mirrors HP death spiral (OK / Weakened / Severely Weak / Incapacitated)

### 6.3 Magic & Technology Interference

> **NOTE:** Mechanical rules for magic/tech interference zones are not yet designed. Need to define:
> - How zones are classified (levels of magic/tech intensity?)
> - Mechanical penalties for using tech in magic zones and vice versa
> - Can items be shielded or hardened against interference?
> - Do magitech hybrids exist, and if so, are they inherently unstable/corrupting?

---

## 7. Progression & Leveling

### 7.1 Design Intent

Progression should be **skill-use driven**, not kill-count driven.

Inspirations:
- **Mouse Guard:** Every failure teaches lessons. Every successful use teaches lessons. You mark skills as you use them, and advancement comes from play.
- **Symbaroum:** XP for meaningful scenes, not combat victories.

### 7.2 Core Concept

> **NOTE:** Leveling system is deferred for detailed design. Key principles established:
> - Learn by doing — skills improve through use (successes and failures both count)
> - Session-based points that can be invested in skill advancement
> - NO XP-for-killing-monsters
> - Reward meaningful scenes, clever problem-solving, heroic moments
> - Specific mechanics TBD

---

## 8. Character Creation Summary

1. **Set stats:** Distribute points across 6 stats (-3 to +3), net bonus set by GM (default +1). Write a description justifying each value.
2. **Choose skills:** Up to 15 skills. Skill points per group = 10 + stat group net modifiers.
3. **Choose spells (if magical):** Base spells = 7 + PW. Can buy more at 3 skill points each. Choose from schools equal to PW modifier (min 1).
4. **Label your archetype:** Write a class name that describes your concept. This is flavor, not restriction.
5. **Select race:** (TBD)
6. **Calculate derived values:**
   - HP per level: 7 + PP
   - MP per level: 7 + PW
   - Skill target numbers: ((10 + stat mod) × skill level) + 30
7. **Equip:** Select weapons, armor, and gear.

---

## 9. Adventure Scope & Play Style

### 9.1 What This Game Is

- **City-based noir investigations** — tracking cultists, unraveling conspiracies, navigating faction politics in a sprawling 1920s metropolis
- **Wilderness expeditions** — venturing into wild zones, exploring magical ruins, confronting legendary beasts
- **Faction-driven missions** — jobs from your Adventuring Society's patron faction
- **Theater of the mind** — fully narrative combat and exploration, no battlemaps

### 9.2 What This Game Is NOT

- Not a dungeon crawler
- Not a tactical miniatures game
- Not a game where you need cones, movement ranges, or grid maps
- Not a game about amoral murder hobos
- Not a game with class-locked abilities or feat trees

---

## 10. Open Design Questions

The following topics need further discussion and design work:

### High Priority
1. ~~**Schools of Magic** — Define schools, design spell lists~~ **DONE** (Session 2 — see MAGIC_SYSTEM.md)
2. ~~**Firearms & Steampunk Equipment** — Tables for guns, gadgets, vehicles~~ **DONE** (Session 4 — see FIREARMS_EQUIPMENT.md, DESIGN_PHILOSOPHY.md)
3. **Magic/Tech Interference Mechanics** — How zones work mechanically (framework established in FIREARMS_EQUIPMENT.md §5, full zone rules TBD)
4. **Leveling System** — Detailed progression mechanics
5. **Death Saves** — Mechanics for dying and near-death
6. **Races** — Whether to include, and if so, what options
7. **Archetype Names** — Setting-flavored class labels
8. **Factions** — Define the major power groups
9. **Individual Spell Tier Tables** — 37 spells each need full tier descriptions, costs, casting times, misfire effects

### Medium Priority
10. **Hinder Mechanic** — Full definition of armor hindrance effects
11. ~~**Wild vs. Scholarly Magic** — Mechanical differentiation~~ **DONE** (Session 2 — see MAGIC_SYSTEM.md, details TBD for exact variance mechanic)
12. **Skill List Revision** — Update for steampunk setting (add Firearms, Pilot, Occult Lore, etc.)
13. **Equipment Prices & Economy** — Currency system, costs
14. **Bestiary** — Monsters, cultists, corrupted beings, magical creatures
15. **NPC Creation** — Simplified stat blocks for GM use

### Lower Priority
15. **Sample Adventures** — Starter scenarios
16. **Worldbuilding Gazetteer** — Geography, nations, cities
17. **Adventuring Society Generator** — Tools for creating societies
18. **Magical Artifacts** — Unique items and relics
19. **Corruption & Madness** — Exposure to dark magic effects
20. **Vehicle Rules** — Airships, automobiles, boats (simple, theater-of-mind)

---

## 11. Existing Assets

### Art
- `art/cat.png` — Bat-winged cat, pen & ink, steampunk/gothic style
- `art/dragon.jpg` — Multi-eyed dragon, pen & ink, detailed scales
- `art/fantasy.jpg` — Angelic/winged figure, pen & ink, decorative border piece

### Rules Documents
- `rules/Cover.pdf` — Cover page with setting introduction and fantasy.jpg art
- `rules/FunzieRulez.pdf` — 4-page rules summary (stats, skills, combat, timing, magic, equipment, character creation)
- `rules/FunziescharSheet.pdf` — Character sheet (1 page, landscape)

### Art Style Note
All existing art is **black & white pen & ink** with a detailed, slightly whimsical-dark aesthetic. Future art should maintain this style for consistency.
