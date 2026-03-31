# Magic System Design

## Document Status: DRAFT - In Development
**Last Updated:** 2026-03-29

---

## 1. Philosophy

Magic is **new to the world**. It has recently erupted from the aether and nobody fully understands it. The world is in a desperate rush to harness it. It is not part of daily life. It is a hazard, a wonder, and a source of fear.

### Core Principles
- **Wondrous and wild** — Magic inspires awe. It is not routine or mundane.
- **Dangerous and costly** — Every cast is a risk. Not every character should be magical.
- **Unpredictable** — Outcomes vary based on the caster's power and the roll. Magic is never fully tamed.
- **Concept-based spells** — Spells describe broad magical concepts, not narrow specific effects. Players and GMs interpret the specifics within structured guidelines of scope and scale.

### Supernatural Entities

Ancient or powerful magical entities and beasts exist in the world, but they are rare, alien, and fundamentally not understood. They can be petitioned and interacted with for boons or learning, but you never really understand them or what they want. They are not "summoned" or "bound" as a routine magical act. Interaction with these beings is more Call of Cthulhu than D&D — strange, unsettling, and never fully within the caster's control. There are no elemental spirits or bound servitors in the normal spell system.

### Dark Magic

Dark magic exists in the world but is **NOT player-accessible**. It is one of the evils of the setting — something heroes fight against. Cultists resurrecting dead gods, soul-corrupting cybernetic mutations, perversion of natural magical and technological systems. Dark magic should feel rare and *wrong* when encountered.

---

## 2. Two Paths of Magic

Every caster follows one of two paths. This is a meaningful character-defining choice with real mechanical consequences.

### 2.1 Scholarly Path (Control)

The scholarly caster has trained, studied, and disciplined themselves to harness inherently wild forces. They impose structure on chaos through ritual, formula, and practice.

**Mechanical Benefits:**
- **More spell points** — Training expands your magical capacity. More spells known.
- **Possibly more schools accessible** — Study opens doors to additional domains of magic.
- **Choose your tier** — When you cast and qualify for a tier, you can freely choose that tier or any lower one. You decide exactly how much power to channel.
- **Lower backlash chance** — Training insulates you from the raw burn of magical energy.

**Mechanical Limitations:**
- **Spellbook** — You can only cast spells you have specifically learned and recorded. Your training gives you depth but constrains your breadth.
- **Predictable** — You trade surprise and raw potential for reliability.

### 2.2 Wild Path (Power)

The wild caster has a raw, untrained connection to the mana flows. They are naturally gifted — magic comes to them instinctively. They tap into it sometimes spectacularly, sometimes disastrously. The magic uses *them* as much as they use it.

**Mechanical Benefits:**
- **+10 casting target bonus** — Wild casters are naturally attuned. They receive a flat +10 to their casting target number (separate from PW). This reflects their instinctive gift for magic.
- **Entire domain accessible** — You can attempt to cast *any* spell within your schools. No spellbook limitation.
- **Unpredictable power spikes** — The variance mechanic (2d100 take farther from target) means results swing toward extremes — more spectacular successes alongside more dramatic failures.
- **Flexibility** — You're never stuck without the right spell if it's in your domain.

**Mechanical Limitations:**
- **Limited tier control** — Wild casters cannot freely choose their tier. They can suppress their result by a number of tiers based on their skill level (see §2.5 Wild Caster Tier Suppression). Novices are at the mercy of the magic; masters learn to rein it in.
- **Higher backlash chance** — Raw, uninsulated contact with magical forces burns more often.
- **Fewer spell points / fewer schools** — Less training means less capacity and narrower domain access.

### 2.3 The Trade-Off

| Aspect | Scholarly | Wild |
|--------|-----------|------|
| Casting roll | 1d100 (straight) | 2d100, take roll farther from target |
| Casting target bonus | None | +10 (natural attunement) |
| Spells available | Learned spells only (spellbook) | Any spell in your schools |
| Tier selection | Choose freely (at or below qualified tier) | Can suppress by 0-3 tiers based on skill (see §2.5) |
| Backlash risk | Base rates (5%/10%/15%/25%) | Higher (exact modifier TBD) |
| Spell points | More | Fewer |
| School access | Possibly more schools | Fewer schools |
| Power ceiling | Reliable but bounded | Unpredictable, swings to extremes |

### 2.4 Wild Caster Variance Mechanic

Wild casters roll **2d100 and take the result farther from their target number**. This pushes outcomes toward extremes — bigger failures AND bigger successes. Combined with their +10 casting target bonus, wild casters at low levels succeed at roughly the same rate as scholarly casters but spike to higher tiers when they do succeed. At high levels, they become more reliable than scholarly casters but still can't control what tier manifests.

**Probability comparison (with +10 wild bonus):**

| Power Level | Scholarly Target | Wild Target | Scholarly Success | Wild Success | Wild Spectacular |
|-------------|-----------------|-------------|-------------------|-------------|-----------------|
| Low | 30 | 40 | 30.0% | 31.2% | 0% |
| Mid | 45 | 55 | 45.0% | 58.6% | 7.8% |
| High | 60 | 70 | 60.0% | 81.4% | 34.4% |
| Master | 75 | 85 | 75.0% | 95.2% | 56.4% |

**Key behaviors:**
- Wild casters almost never land in the Weak tier (~2.2%) — results swing to extremes
- At low levels, wild and scholarly have similar success rates, but wild successes skew higher-tier
- At high levels, wild casters succeed more often and spike Spectacular frequently — but tier suppression is limited (see §2.5), so they often pay higher costs than they'd choose
- The +10 bonus represents natural magical gift — these are instinctive, talented individuals who lack discipline, not weak casters who chose the wrong path

### 2.5 Wild Caster Tier Suppression

Wild casters are not purely at the mercy of their roll. As they grow in power, they learn to *feel* the magic and rein it in. The number of tiers a wild caster can step down from their rolled result is determined by their casting target number, following the same 25% bracket system used for critical ranges:

| Casting Target | Tiers Can Suppress |
|----------------|-------------------|
| 1-25 | 0 (locked to rolled tier — true novice, the magic controls you) |
| 26-50 | 1 |
| 51-75 | 2 |
| 76+ | 3 |

**Examples:**
- Wild caster, target 40: Rolls Spectacular → can step down to Strong (1 tier). Can't go lower.
- Wild caster, target 65: Rolls Spectacular → can step down to Standard (2 tiers). Can't reach Weak.
- Wild caster, target 85: Rolls Spectacular → can step down to Weak (3 tiers). Near-full control — but still earned through mastery, not training.

**Design intent:** This creates a progression arc. A novice wild caster is genuinely chaotic — the magic uses them. As they grow, they develop an instinctive feel for controlling the flow. A master wild caster has *almost* as much control as a scholarly caster, but got there through a fundamentally different path (experience and instinct vs. study and discipline). The key remaining difference: scholarly casters always choose freely regardless of skill level. Wild casters earn control.

---

## 3. Casting Mechanics

### 3.1 The Casting Sequence

**Step 1 — Cast:** Roll d100 against your casting target number. Scholarly casters roll 1d100. Wild casters roll 2d100 and take the result farther from their target.

**Step 2 — Determine available tier:** Your roll result determines what tier of effect you qualify for. Your casting stat **hard caps** what tiers are possible — no amount of luck gets a novice to Spectacular.

**Step 3 — Choose tier (Scholarly) / Suppress tier (Wild):**
- *Scholarly casters* choose any tier at or below what they qualified for. Want to save exhaustion? Take the Weak result even though you rolled Strong. Full control at any skill level.
- *Wild casters* can suppress their result by a number of tiers based on their casting target (see §2.5). A novice (target 1-25) is locked to what they rolled. A master (target 76+) can step down up to 3 tiers.

**Step 4 — Apply costs:** Each tier of each spell has its own exhaustion cost. Higher tiers cost more. Casting time is fixed per spell (not per tier) — tier measures power drawn, not time spent. See SPELL_COMPENDIUM.md for casting times and exhaustion costs.

**Step 5 — Backlash check:** Separate from spell success. Even a clean, successful cast can burn you. Backlash chance scales with the tier used — more power pulled, more risk of getting burned.

**Step 6 — Push it (optional):** After seeing your result, you can try to squeeze out more power. This **always** costs extra (additional exhaustion, increased backlash chance). You can **never** push past your hard cap — if your stat doesn't allow Spectacular, pushing won't get you there.

**On failure (roll over target):** The spell **misfires**. Each spell has its own misfire description — the magic goes wrong in a spell-specific, narratively interesting way. A healing spell might drain instead of mend. A force blast might rebound. A divination might show you something horrifying and false.

### 3.2 Tier System

| Tier | Description | General Scope |
|------|-------------|---------------|
| **Misfire** | Roll over target — spell fails and goes wrong | Spell-specific negative effect |
| **Weak** | Bare success, minimal effect | Minor, personal-scale, brief |
| **Standard** | The spell works as expected | Moderate, room-scale, short duration |
| **Strong** | Enhanced effect | Significant, area-scale, sustained |
| **Spectacular** | Dramatic, impressive, potentially beyond intent | Major, dramatic, lasting |

**Tier qualification** is based on how far under your target number you rolled:

| Roll Margin | Tier Achieved |
|-------------|---------------|
| Over target | Misfire |
| 1-10 under | Weak |
| 11-30 under | Standard |
| 31-50 under | Strong |
| 51+ under | Spectacular |

**Hard caps based on casting target number:**
- Target 30 or below: Maximum tier = **Standard** (you can never roll 31+ under)
- Target 31-50: Maximum tier = **Strong** (you can never roll 51+ under)
- Target 51+: Maximum tier = **Spectacular** (theoretically possible)

> **EXAMPLE — Novice caster, target 30:**
> Rolls a 5 = 25 under → qualifies for Standard (their ceiling).
> Even a perfect roll of 01 = 29 under → still Standard.
> They will never reach Strong or Spectacular — it's beyond their ability.

> **EXAMPLE — Master caster, target 75:**
> Rolls a 40 = 35 under → qualifies for Strong.
> Rolls a 12 = 63 under → qualifies for Spectacular.
> But Spectacular healing might cost 12+ exhaustion — is it worth it?

### 3.3 Costs Per Tier

Each spell's description includes per-tier costs. These are designed using hidden parameters (not exposed in the rulebook) based on:

- **Complexity** — How intricate is the magical effect? Healing a body (many complex systems) costs more than making light (simple energy manipulation).
- **Scope** — How much area/mass/number of targets is affected?
- **Duration** — How long does the effect persist?
- **Unnaturalness** — How far does the effect push against the natural order?

The player sees the final numbers per tier in the spell description. For example, a spell entry might read:

> **Mend** (Vivimancy)
> | Tier | Exhaustion | Casting Time | Effect |
> |------|-----------|--------------|--------|
> | Weak | 3 | 4 counts | Close a minor wound, stop bleeding |
> | Standard | 6 | 6 counts | Heal moderate injury, knit cracked bone |
> | Strong | 10 | 8 counts | Mend broken bones, cure disease, heal serious wounds |
> | Spectacular | 15 | 12 counts | Regrow lost tissue, purge deep corruption, pull someone back from the edge of death |
> | *Misfire* | 3 | — | *The spell inverts — drains vitality from the target instead of restoring it* |

*(Note: These specific numbers are placeholders — actual values will be determined by the hidden design formula during spell creation.)*

### 3.4 Backlash

Backlash is **separate from misfire**. Misfire = the spell goes wrong (spell-specific). Backlash = the raw magical energy burns you physically. You can have a **successful cast with backlash** — the spell works, but it hurts you too.

**Backlash chance scales with tier used** — higher tier = more power channeled = more chance of getting burned:

| Tier Used | Scholarly Backlash Chance | Wild Backlash Chance (TBD) |
|-----------|--------------------------|---------------------------|
| Weak | 5% | Higher |
| Standard | 10% | Higher |
| Strong | 15% | Higher |
| Spectacular | 25% | Higher |

> **OPEN:** Exact wild caster backlash modifier TBD. Options: flat +5% per tier, or multiply by 1.5×, etc.

#### 3.4.1 Backlash Effects

When backlash triggers, two things happen:

**1. Physical Burn (always):** Take **1d4 physical HP damage**. Flat, regardless of tier. Armor doesn't soak it — it's internal, magical. Painful but not deadly. This is the baseline cost: magic always hurts a little when it burns you.

**2. Wild Effect (25% chance):** Roll d100. On 25 or under, something strange happens — roll d10 on the **Wild Effect Table**.

#### 3.4.2 Wild Effect Table

Wild effects have three escalation tiers. If you roll the same effect while a previous instance is still active, it **escalates**. A third escalation while still active makes the effect **permanent**. Escalation tracking is **per-effect** — rolling different numbers gives separate base effects, not escalation.

| d10 | Effect | Base (1st) | Escalated (2nd, same while active) | Permanent (3rd, same while active) |
|-----|--------|-----------|-----------------------------------|-------------------------------------|
| 1 | **Caster's Mark** | Eyes glow faintly for 1d4 hours | Eyes glow brightly for 1d4 days, visible in darkness | Eyes permanently luminous — always visibly marked as a caster |
| 2 | **Thermal Flux** | Temperature shifts sharply around you for several minutes | Extreme shift for 1d4 hours — frost forms or things smolder near you | Permanently radiate unnatural cold or heat — affects those nearby, can't be hidden |
| 3 | **Aetheric Ring** | Sharp ringing sound emanates from you, everyone nearby notices | Ringing persists for 1d4 hours, -10% to Stealth | Faint persistent hum permanently — Stealth always at -10%, animals react to you |
| 4 | **Poltergeist** | Nearby small loose objects levitate briefly then drop | Objects within arm's reach rattle and shift for 1d4 hours, -10% to Conceal and delicate work | Small objects always drift and shift around you — -10% to Conceal permanently |
| 5 | **Sense Burn** | Lose sense of taste and smell for 1d4 hours | Lose taste, smell, and touch sensitivity for 1d4 days, -10% to Awareness checks | One sense permanently dulled — AW reduced by 1 |
| 6 | **Tremors** | Hands tremble for 10 minutes, -10% to fine motor tasks | Hands tremble for 1d4 hours, -10% to all PC-based rolls | Permanent slight tremor — PC reduced by 1 |
| 7 | **Veil Slip** | Brief vivid hallucination — you see something that isn't there (GM describes) | Hallucinations recur for 1d4 hours, -10% to AW checks | Permanently see things at the edge of vision — AW reduced by 1, but GM may occasionally feed genuine supernatural glimpses |
| 8 | **Static Discharge** | You shock the next person or metal object you touch — startling but harmless | Crackle with static for 1d4 hours — metal sparks, -10% to Social interactions, nearby tech glitches | Permanent low-level static field — tech in your hands always slightly unreliable, -10% to tech-related skill checks |
| 9 | **Voice Shift** | Voice changes pitch or timbre for 1d4 hours — unsettling to others | Voice deeply unnatural for 1d4 days — -10% to Persuasion and Social rolls | Voice permanently altered, recognizably inhuman — SP reduced by 1, but +10% to Interrogation |
| 10 | **Bleed** | Nosebleed — dramatic-looking, socially alarming | Bleeding from nose and ears for 1d4 hours, -10% to SP-based checks | Bleed unpredictably from small capillaries when stressed — PP reduced by 1 |

**Design intent:** The escalation mechanic acts as a natural limiter on magic use. After one or two backlash effects, casters become hesitant to keep casting for fear of escalation — especially when a permanent stat reduction is on the line. This reinforces the design goal that not every character should be a caster and that a mixed party of casters and non-casters is the smart approach. The probability of rolling the same number on a d10 three times while previous effects are still active is low, but the *fear* of it is a constant presence.

### 3.5 Spell Cancellation

Cancelling a spell mid-cast:
- Costs exhaustion equal to **half** the normal cost for the tier you were attempting
- Additionally: **10% chance of backlash**, dealing 1d4 physical damage per 2 tiers of the spell AND causing full casting exhaustion

### 3.6 Magic Points & Exhaustion Track

**Magic Points per level:** 7 + PW

Four exhaustion tiers with escalating penalties (mirrors the HP death spiral):

| Level | Status | Penalty |
|-------|--------|---------|
| 1 | OK | None |
| 2 | Weakened | -10% to all rolls |
| 3 | Severely Weak | -25% to all rolls |
| 4 | Incapacitated | -50% to all rolls |

**Recovery:** 1d8 magic points per hour of full rest.

Note: Exhaustion penalties stack with wound penalties. A Harmed (-10%) and Weakened (-10%) caster is at -20% to all rolls. The death spiral applies to both tracks simultaneously.

#### 3.6.1 Exhaustion Overflow

When a spell's exhaustion cost exceeds your remaining MP, the spell still fires. You spend all remaining MP (dropping to zero, Incapacitated on the exhaustion track). The overflow — the exhaustion you couldn't pay — converts to physical HP damage at a rate of **half the overflow, rounded down**.

**Example:** You have 7 MP remaining. You cast (or are forced to cast, as a wild caster) a Spectacular Mend costing 18 exhaustion. You spend all 7 MP → Incapacitated on the exhaustion track. The remaining 11 overflows → you take 5 physical HP damage (11 ÷ 2 = 5.5, rounded down). The spell works. You're on the floor.

This creates genuine heroic sacrifice moments — a caster *can* push past their limits to save a friend, but the magic burns their body to do it. It also serves as a natural consequence for wild casters who can't fully suppress a high-tier result and don't have enough MP to cover it.

### 3.7 Casting Interruption

Because spells take time on the timing track, they can be interrupted. If a caster takes damage while casting (between declaring the spell and its resolution on the timing track), they must make a **concentration check** to maintain the spell.

> **OPEN:** Concentration check mechanics need design. Key questions:
> - What do you roll? PW check? Flat percentage? Opposed roll?
> - Does the amount of damage taken affect difficulty?
> - On failure, does the spell simply fizzle, or does it misfire?
> - Does the caster still pay exhaustion on an interrupted spell? (Probably yes — partial cost, similar to cancellation)
>
> This interacts with the timing track in a tactically interesting way: if you can see an enemy caster begin casting at count 3 with resolution at count 7, you have a 4-count window to hit them and force a concentration check. Fast weapons (daggers, punches) become valuable for disrupting casters. This is an emergent tactical layer that arises naturally from the timing track + casting time system.

---

## 4. Schools of Magic

Six schools, each representing a domain of magical practice. Schools are humanity's attempt to impose taxonomy on something fundamentally wild — categories that help organize understanding but don't perfectly contain the reality.

### 4.1 Aetheric Manipulation
*Raw force, energy, and elemental power*

The most direct and visceral school. You grab the raw stuff of magic and project it as force, energy, or elemental effect. Least subtle, most immediately impressive. Aetheric Manipulators are the "artillery" of the magical world.

**Spells (7):**

| # | Spell | Concept |
|---|-------|---------|
| 1 | **Force** | Push, pull, strike, crush with raw magical force. Invisible, blunt, undeniable. |
| 2 | **Elemental Manipulation** | Shape, summon, or direct fire, ice, wind, lightning, water, earth. The broadest spell in the school — effects range from lighting a candle to calling lightning from the sky. |
| 3 | **Barrier** | Create walls, shields, or domes of magical energy. Can block physical and magical attacks. |
| 4 | **Kinesis** | Move objects at a distance. Fine manipulation at low tiers, hurling heavy objects at high tiers. |
| 5 | **Disruption** | Shatter, destabilize, or unravel physical matter or magical constructs. Destruction made precise. |
| 6 | **Amplify** | Enhance physical forces already in motion. Make an explosion bigger, a fall harder, a blow heavier, a sound deafening. |
| 7 | **Arc** | Channel energy between points, redirect incoming energy, ground or discharge power. The "electrician's" spell — routing and rerouting raw power. |

### 4.2 Vivimancy
*Life, body, and biology*

The magic of living things. Healing, bolstering, sensing life — but also withering, draining, and the unsettling territory of reshaping flesh. Vivimancers walk an uncomfortable line. Where does "mend this wound" end and "reanimate this corpse" begin? The border between Vivimancy and the dark arts that cultists practice is blurry, which makes Vivimancy practitioners the subject of both gratitude and suspicion.

**Spells (7):**

| # | Spell | Concept |
|---|-------|---------|
| 1 | **Mend** | Heal wounds, knit bone, cure disease, purge poison. The most valued spell in the world — and the one that makes people most uncomfortable about what else Vivimancers might be capable of. |
| 2 | **Fortify** | Bolster stamina, resist pain, harden flesh, enhance physical resilience. Temporary biological enhancement. |
| 3 | **Wither** | Drain vitality, accelerate decay, weaken biological systems. The "offensive" Vivimancy spell. Useful but unsettling. |
| 4 | **Sense Life** | Feel the presence, health, and condition of living things nearby. Detect hidden creatures, assess injuries, feel the "pulse" of an ecosystem. |
| 5 | **Shape Flesh** | Alter biological features — cosmetic changes, functional adaptations, temporary mutations. At high tiers, dramatic physical transformation. Addictive and potentially identity-eroding with overuse. |
| 6 | **Purge** | Cleanse corruption, magical contamination, parasites, and foreign influences from a living body. Critical for dealing with dark magic exposure. |
| 7 | **Bloom** | Accelerate growth, encourage life, cause plants to flourish, seeds to sprout, wounds to scar over rapidly. The "gentle" Vivimancy — gardeners and farmers love Bloomers. |

### 4.3 Warding
*Protection, sealing, and banishment*

The most "respectable" school. Everyone wants protection from the magical chaos engulfing the world, and Warders provide it. Circles of power, barriers against supernatural intrusion, seals against dark forces. Warders are the closest thing the magical world has to trusted professionals.

**Spells (6):**

| # | Spell | Concept |
|---|-------|---------|
| 1 | **Shield** | Personal magical protection against harm — physical or magical. A force that absorbs, deflects, or redirects incoming damage. |
| 2 | **Seal** | Lock, close, bind shut. Works on doors, containers, wounds, portals, magical breaches. What is sealed stays sealed until deliberately unbound. |
| 3 | **Banish** | Drive away magical entities, dispel active magic, force out foreign magical influence. The anti-magic spell — essential for cult hunters. |
| 4 | **Circle** | Create a bounded area with specific magical properties — protection, containment, alarm, sanctuary. Requires preparation and focus but creates powerful, lasting effects. |
| 5 | **Anchor** | Stabilize, fix in place, resist forced movement or transformation. Can stabilize unstable magic zones, hold shifting terrain, or lock down a target. |
| 6 | **Unbind** | Break seals, dispel wards, shatter bindings, unlock magical locks. The counter-school to Warding itself — the locksmith who can also pick locks. |

### 4.4 Divination
*Perception, knowledge, and detection*

Seeing the unseen. Divination is the investigator's school — invaluable for noir detective work, relic hunting, and navigating magical zones. The downside: Divination doesn't filter what you see. Sometimes you learn things you wish you hadn't. Higher tiers of Divination can be psychologically hazardous.

**Spells (6):**

| # | Spell | Concept |
|---|-------|---------|
| 1 | **Reveal** | See hidden things: invisible objects, concealed doors, disguised creatures, buried items. The world becomes transparent to you. |
| 2 | **Scry** | See distant places, people, or events. Range and clarity scale with tier. The classic "crystal ball" effect. |
| 3 | **Read** | Psychometry. Touch an object or place and sense its history, emotional imprint, last user, purpose. Objects carry echoes of their past. |
| 4 | **Foresight** | Brief, unreliable glimpses of what's about to happen. Better tiers = clearer and further ahead. Never perfectly reliable — the future is mutable. |
| 5 | **Detect** | Sense the presence and nature of magic. Identify spell effects, map magical zones, feel the intensity and flavor of nearby magical activity. |
| 6 | **Commune** | Reach out to distant minds. Send and receive messages, establish brief telepathic contact. At higher tiers, group communication or contact across vast distances. |

### 4.5 Transmutation
*Altering matter and material properties*

The engineer's school. Transmuters change what things *are* — their form, their properties, their very substance. This is where magic and technology get dangerously close. A Transmuter who can reshape metal or alter material properties is doing with magic what factories do with machines, which puts them at the center of the magic-vs-technology tension. The crown jewel — actual transmutation of one substance into another — attracts dangerous attention from powerful interests.

**Spells (6):**

| # | Spell | Concept |
|---|-------|---------|
| 1 | **Reshape** | Change the form of an object without changing its material. Bend bars, shape stone, mold metal, sculpt wood. The material stays the same; the shape obeys you. |
| 2 | **Alter Property** | Change a material property: make iron brittle, stone flexible, wood fireproof, water viscous, glass soft. Includes hardening, softening, and any other property manipulation. |
| 3 | **Refine** | Purify, separate, distill. Extract metals from ore, purify water, separate compounds, isolate poisons. The alchemist's spell. |
| 4 | **Enlarge/Reduce** | Change the size of objects or creatures. Temporary and stressful on living targets. At high tiers, dramatic size shifts. |
| 5 | **Fuse** | Join dissimilar materials or objects into a seamless whole. Metal to stone, wood to glass. Also works in reverse — separate fused things cleanly. |
| 6 | **Transmute** | Actually change one material into another. Lead to gold, wood to stone, water to oil. The signature spell of the school — and the one most likely to attract dangerous attention from corporations, governments, and criminals. |

### 4.6 Ley Weaving
*Manipulating magic itself*

The rarest and most feared school. Ley Weavers don't cast spells so much as reshape the magical landscape itself. They amplify, dampen, redirect, and sever the mana flows that all other casters depend on. Other casters are deeply uncomfortable around Ley Weavers — because a skilled Weaver can shut your magic down. Deliberately kept as the smallest school (5 spells) because of its meta-magical nature.

**Spells (5):**

| # | Spell | Concept |
|---|-------|---------|
| 1 | **Dampen** | Suppress or weaken magic in an area. Reduce spell effectiveness, quiet active enchantments, create zones of magical calm. Useful for stabilizing wild zones or countering enemy casters. |
| 2 | **Channel** | Redirect mana flows, create temporary conduits, draw power from ley lines or magical zones. Can be used to "borrow" ambient magical energy to reduce personal exhaustion costs. |
| 3 | **Attune** | Harmonize with a magical source, artifact, or zone. Understand its nature, tap its power safely, communicate with magical phenomena. The research/investigation spell of the school. |
| 4 | **Surge** | Flood an area with raw mana. Amplifies all magic in the area — friend and foe alike. Destabilizes technology. Extremely dangerous and indiscriminate. |
| 5 | **Sever** | Cut a caster's connection to mana flows. Temporarily strip magical ability. The most feared spell in the game — and the one that makes other casters avoid Ley Weavers. |

---

## 5. Spell Acquisition & Schools Access

### 5.1 Spells Known

- **Base spells known:** 7 + PW modifier
- Additional spells can be acquired by spending **3 skill points per spell** (magic is expensive in opportunity cost)

### 5.2 Schools Accessible

- Number of schools a caster can access equals **PW modifier** (minimum 1)
- Scholarly casters may have access to additional schools (exact bonus TBD)

### 5.3 Scholarly vs Wild Acquisition

- **Scholarly:** Choose specific spells from your accessible schools. These go in your spellbook. You can only cast spells in your book.
- **Wild:** You don't choose individual spells. You have access to your schools as a whole. You can attempt any spell in any of your accessible schools — but you get what the magic gives you.

> **OPEN:** Can scholarly casters learn new spells mid-campaign through research, mentorship, or discovery? Can wild casters develop more control over time (hybrid progression)?

---

## 6. Spell Design Guidelines (Internal)

*This section is for the game designers, not the rulebook. It provides the hidden formula framework for creating consistent spell entries.*

### 6.1 Design Parameters

Each spell tier's costs are derived from these hidden parameters:

- **Base Complexity (1-5):** How intricate is the fundamental magical effect?
  - 1 = Simple (light, sound, basic force)
  - 2 = Moderate (elemental effects, material reshaping)
  - 3 = Complex (healing, biological manipulation, material transmutation)
  - 4 = Very Complex (mental contact, temporal effects, severing magical connections)
  - 5 = Extreme (reality-altering, large-scale transformation)

- **Tier Multiplier:** Each tier scales the base costs
  - Weak: ×1
  - Standard: ×2
  - Strong: ×3
  - Spectacular: ×4-5

- **Casting Time:** Fixed per spell, independent of tier. Tier measures power drawn, not time. Casting time is a per-spell balancing lever:
  - C1 spells: 2ct (snap-cast cantrips)
  - C2 spells: 3-5ct (reactive to deliberate, based on tactical role)
  - C3 spells: 5-6ct (complex, high-investment)
  - C4 spells: 8ct or Ritual (major commitment or non-combat)
  - See SPELL_COMPENDIUM.md for full casting time assignments

> **NOTE:** These formulas are preliminary. Actual values need playtesting and balancing. The goal is internal consistency — players should feel that costs are fair and proportional even without seeing the formula.

### 6.2 Misfire Design Principles

Each spell needs a unique misfire description that:
- Is **thematically appropriate** — the spell goes wrong in a way related to what it does
- Is **narratively interesting** — creates dramatic moments, not just "nothing happens"
- Has **real consequences** — misfires should matter, but shouldn't instantly kill the caster
- **Scales loosely** — a novice's misfire should be less catastrophic than a master's attempt at a powerful tier

---

## 7. Summary — Spell Count by School

| School | Spells | Count |
|--------|--------|-------|
| Aetheric Manipulation | Force, Elemental Manipulation, Barrier, Kinesis, Disruption, Amplify, Arc | 7 |
| Vivimancy | Mend, Fortify, Wither, Sense Life, Shape Flesh, Purge, Bloom | 7 |
| Warding | Shield, Seal, Banish, Circle, Anchor, Unbind | 6 |
| Divination | Reveal, Scry, Read, Foresight, Detect, Commune | 6 |
| Transmutation | Reshape, Alter Property, Refine, Enlarge/Reduce, Fuse, Transmute | 6 |
| Ley Weaving | Dampen, Channel, Attune, Surge, Sever | 5 |
| **Total** | | **37** |

---

## 8. Open Questions

1. ~~**Wild caster variance mechanic**~~ **RESOLVED** — 2d100 take roll farther from target, +10 casting target bonus
2. **Scholarly bonus to schools** — How many extra schools does scholarly training grant? +1? Based on IN?
3. ~~**Backlash severity**~~ **RESOLVED** — 1d4 flat physical damage + 25% chance of Wild Effect (d10 table with 3-tier escalation, permanent on 3rd)
4. **Wild vs Scholarly backlash rates** — Exact multiplier/modifier for wild casters' higher backlash chance
5. **Push It mechanic details** — Exact costs and risks of pushing for a higher tier
6. **Mid-campaign spell learning** — Can scholarly casters find/learn new spells? Can wild casters develop control?
7. **Spell interaction with magic/tech zones** — How do zone levels modify casting? Penalty to target number? Forced tier reduction? Automatic backlash increase?
8. **Individual spell tier tables** — The 37 spells each need full tier descriptions, costs, casting times, and misfire effects. This is the single largest remaining design task. Force and Mend drafted as templates (see §9).
9. ~~**Wild caster tier suppression**~~ **RESOLVED** — Can step down tiers based on 25% skill brackets (0/1/2/3 tiers at 1-25/26-50/51-75/76+). Mirrors crit range mechanic.
10. ~~**Exhaustion overflow**~~ **RESOLVED** — Spell fires, remaining MP spent to zero, overflow converts to physical HP damage at half rate (rounded down).
11. **Casting interruption** — Concentration check when damaged mid-cast. Mechanics TBD (what to roll, does damage affect difficulty, misfire vs fizzle on failure).

---

## 9. Spell Tier Tables — Templates

These two spells serve as the design templates for all 37 spells. Force (Complexity 1) establishes the baseline for simple, direct magic. Mend (Complexity 3) establishes the baseline for complex, intricate magic. All other spells should be designed using the same hidden formula framework, with individual adjustments where the fiction demands.

### 9.1 Force (Aetheric Manipulation)
*Complexity: 1 (simple, raw force)*

Push, pull, strike, crush with raw magical force. Invisible, blunt, undeniable. The most basic expression of Aetheric power — you grab the raw stuff of magic and hurl it at the problem.

| Tier | Exhaustion | Casting Time | Damage | Effect |
|------|-----------|--------------|--------|--------|
| **Weak** | 2 | 2 counts | 1d4 | A blunt shove of force. Enough to knock someone back a step, slam a door, shove an object off a table. Can wind or stagger a target. Like getting hit with an invisible fist. |
| **Standard** | 4 | 3 counts | 2d6 | A solid, focused blast. Cracks wood, dents metal, sends a person stumbling or flying back several feet. Can knock a target prone. Comparable to being hit by a charging horse. |
| **Strong** | 6 | 4 counts | 3d8 | A crushing wave of force. Splinters doors, buckles armor, hurls a person across a room. Can affect a small group if tightly clustered. Shatters glass and loose objects in the area. Comparable to being hit by a car. |
| **Spectacular** | 10 | 6 counts | 4d10 | Devastating, concussive impact. Collapses walls, caves in structures, sends multiple targets flying. Can level a small building or clear a street. The air visibly distorts. Everyone nearby feels the shockwave. |
| *Misfire* | 2 | — | 1d6 to caster | *The force rebounds — the caster is hurled backward and takes the impact themselves. Nearby allies may be caught in the blast.* |

**Design notes:**
- Damage at Weak (1d4, avg 2.5) is deliberately below a longsword (1d8) — Force is fast (2 counts vs 5 for a longsword) and requires no weapon, so lower damage balances the convenience.
- At Standard (2d6, avg 7), comparable to strong melee weapons but faster. The exhaustion cost and backlash risk are the balancing factors.
- At Spectacular (4d10, avg 22), can nearly drop a full-health character in one hit. But at 10 exhaustion, you can do this maybe twice before serious consequences.

### 9.2 Mend (Vivimancy)
*Complexity: 3 (complex, biological systems)*

Heal wounds, knit bone, cure disease, purge poison. The most valued spell in the world — and the one that makes people most uncomfortable about what else Vivimancers might be capable of. Healing is expensive because you're manipulating the full complexity of living biological systems.

| Tier | Exhaustion | Casting Time | Healing | Effect |
|------|-----------|--------------|---------|--------|
| **Weak** | 4 | 4 counts | 1d4 HP | Stop bleeding, close a shallow wound, dull pain. Enough to stabilize someone who's hurt but not keep them in a fight. |
| **Standard** | 8 | 6 counts | 2d6 HP | Heal a moderate wound, knit a cracked bone, neutralize a common poison. Can pull someone back from the edge of Maimed to functional. |
| **Strong** | 12 | 8 counts | 3d8 HP | Mend broken bones, cure disease, close deep wounds, purge serious poison. Can bring someone back from Incapacitated to Harmed. |
| **Spectacular** | 18 | 12 counts | 4d10 HP | Regrow lost tissue, purge deep corruption, mend catastrophic injury, pull someone back from the edge of death. The target is visibly, dramatically healed — flesh knits, color returns, bones snap into place. Witnesses never forget it. |
| *Misfire* | 4 | — | -1d6 HP (drains) | *The spell inverts — drains vitality from the target instead of healing. The caster's hands blacken briefly. If used on someone in Incapacitated, this could trigger death saves.* |

**Design notes:**
- Mend costs roughly 2× Force at every tier — Complexity 3 vs Complexity 1. This makes healing precious and limited; a dedicated healer can't just spam it.
- Casting times are significantly longer than Force. Healing takes time; you're knitting biological systems back together.
- A caster with 28 MP can cast Mend at Standard (8 exhaustion) 3 times before hitting Weakened. Healing is a limited resource — use it wisely.
- Spectacular Mend at 18 exhaustion is deliberately punishing. Miraculous healing should cost you almost everything. This is the kind of cast where exhaustion overflow (§3.6.1) is a real possibility.
- The misfire is intentionally horrifying — inverting a healing spell into a drain creates high drama and reinforces that magic is dangerous.

### 9.3 Cost Comparison — The Hidden Formula at Work

| Tier | Complexity 1 (Force) | Complexity 3 (Mend) | Ratio |
|------|---------------------|---------------------|-------|
| Weak | 2 exhaust / 2 counts | 4 exhaust / 4 counts | ~2× |
| Standard | 4 exhaust / 3 counts | 8 exhaust / 6 counts | 2× |
| Strong | 6 exhaust / 4 counts | 12 exhaust / 8 counts | 2× |
| Spectacular | 10 exhaust / 6 counts | 18 exhaust / 12 counts | ~1.8× |

This ratio should hold roughly consistent across all spells of similar complexity. Complexity 2 spells (elemental manipulation, material reshaping) should fall between these two benchmarks.

### 9.4 Shield (Warding)
*Complexity: 2 (moderate — creating and sustaining a magical barrier)*

Personal magical protection against harm. A force that absorbs, deflects, or redirects incoming damage. The bread-and-butter of Warding — everyone wants a Warder nearby.

| Tier | Exhaustion | Casting Time | Effect |
|------|-----------|--------------|--------|
| **Weak** | 3 | 3 counts | A flickering, fragile shell. Absorbs the next **4 points** of damage from a single source, then shatters. Lasts until hit or 1 minute. Visible as a faint shimmer. |
| **Standard** | 6 | 4 counts | A solid barrier. Absorbs **8 points** of damage, can take multiple hits until depleted. Lasts up to 10 minutes. Visible as a faint glow around the caster. |
| **Strong** | 9 | 6 counts | A resilient ward. Absorbs **15 points** of damage across any number of hits. Lasts up to 1 hour. Can be extended to one adjacent ally. Hums faintly when struck. |
| **Spectacular** | 14 | 8 counts | A blazing aegis. Absorbs **25 points** of damage. Lasts up to several hours. Can cover a small group (3-4 people). Visibly radiant — everyone can see you're warded. |
| *Misfire* | 3 | — | *The shield inverts — instead of protecting, it amplifies the next source of damage the caster takes by 1d4. The caster doesn't know until they're hit.* |

**Design notes:**
- Soak values are calibrated against weapon damage. Weak Shield (4 soak) absorbs one dagger hit. Standard (8) absorbs one longsword hit. Strong (15) can tank a Strong-tier Force blast. Proportional to the threat landscape.
- Shield absorbs damage from any source — physical or magical — using the same soak mechanic. No separate "magical damage" system. This maintains mechanical consistency.
- Duration matters here more than for instant spells — a Shield cast before combat lasts through the fight.
- The misfire is insidious — you think you're protected, but you're actually more vulnerable. Creates dramatic reveals in combat.

### 9.5 Reveal (Divination)
*Complexity: 2 (moderate — extending perception beyond normal senses)*

See hidden things: invisible objects, concealed doors, disguised creatures, buried items. The world becomes transparent to you. Essential for investigators, relic hunters, and anyone navigating areas altered by magic.

| Tier | Exhaustion | Casting Time | Effect |
|------|-----------|--------------|--------|
| **Weak** | 3 | 3 counts | A brief flash of enhanced perception. You notice one hidden thing within arm's reach — a concealed pocket, a hidden latch, a disguised face. Instantaneous, like a camera flash of truth. |
| **Standard** | 6 | 5 counts | Sustained enhanced perception for several minutes. Hidden objects, secret doors, and concealed creatures within a room become apparent to you. Magical concealments shimmer at the edges. |
| **Strong** | 9 | 7 counts | Deep sight lasting up to an hour. See through thin walls, detect buried objects underground, pierce magical disguises and illusions. Range extends to a large building. Hidden things glow faintly in your vision. |
| **Spectacular** | 14 | 10 counts | The veil is stripped away completely. For several hours, nothing within a city block can hide from you. See through solid matter, detect hidden rooms, buried vaults, concealed passages. Magical concealment of any strength is visible to you. Your eyes visibly change — pupils dilate to impossible size, irises glow. Overwhelming if not focused — the caster must concentrate to filter the flood of information or suffer -10% to all other actions. |
| *Misfire* | 3 | — | *You see things that aren't there. The GM introduces 1d3 false hidden objects, doors, or creatures that appear completely real to you. You cannot tell them from genuine revelations until you interact with them.* |

**Design notes:**
- Divination spells are about information, not damage. The "cost" is exhaustion, but the value is narrative — what you learn shapes decisions.
- The misfire is perfect for investigation scenarios — false leads planted by your own failed magic.
- Duration is the primary scaling axis rather than damage. Weak is a snapshot, Spectacular is sustained omniscience.
- Spectacular has a built-in drawback beyond cost: sensory overload. Seeing everything is not always comfortable. The -10% penalty for not concentrating gives it mechanical teeth.

### 9.6 Reshape (Transmutation)
*Complexity: 2 (moderate — altering physical form without changing substance)*

Change the form of an object without changing its material. Bend bars, shape stone, mold metal, sculpt wood. The material stays the same; the shape obeys you. The workhorse spell of Transmutation — practical, versatile, and the reason Transmuters are always in demand.

| Tier | Exhaustion | Casting Time | Effect |
|------|-----------|--------------|--------|
| **Weak** | 3 | 3 counts | Reshape a small, simple object — bend a nail, flatten a coin, warp a key, seal a crack in a cup. Up to roughly a handful of material. Changes are crude, like working clay with your fingers. |
| **Standard** | 6 | 5 counts | Reshape a moderate object with reasonable precision — bend iron bars apart, mold a stone block into a different shape, reshape a lock mechanism, sculpt a tool from raw material. Up to roughly a single object you could carry. |
| **Strong** | 9 | 7 counts | Reshape a large object or multiple smaller ones with fine control — warp a door out of its frame, open a doorway through a thin wall, sculpt a detailed statue from a boulder, bend a vehicle chassis. Precise enough for functional mechanical parts. |
| **Spectacular** | 14 | 10 counts | Reshape a small structure or create intricate, precise works — create a passageway through a thick wall, reshape a room's architecture, forge a perfectly functional mechanism from raw metal, collapse or restructure a small building. The material flows like liquid under your will. Witnesses describe it as deeply unsettling to watch. |
| *Misfire* | 3 | — | *The reshaping hits the wrong target — an object on the caster's person warps and deforms. A weapon bends, armor crumples, a tool becomes useless. GM chooses the most inconvenient item.* |

**Design notes:**
- Reshape is pure utility — no damage, no healing, but enormous problem-solving potential. Locked door? Reshape the hinges. Trapped in a cell? Bend the bars. Need a tool? Make one.
- The scaling is about size and precision. Weak is crude and small, Spectacular is room-scale and precise. Not building-scale — even at Spectacular, you're reshaping a small structure, not a skyscraper.
- The misfire targets the caster's equipment — thematically perfect (the reshaping energy hit the wrong thing) and mechanically impactful without being deadly.

### 9.7 Sever (Ley Weaving)
*Complexity: 4 (very complex — cutting a caster's connection to mana flows)*

Cut a caster's connection to mana flows. Temporarily strip magical ability. The most feared spell in the game — and the one that makes other casters avoid Ley Weavers. Using this on someone feels violent and invasive even though it deals no physical damage. The magical equivalent of blinding someone.

**Sever is a targeted spell against another caster and is resolved as an opposed check** (see PROJECT_SPEC.md §3.1b). The Ley Weaver rolls their casting target; the defending caster rolls their own casting target (PW-based) to resist. If the defender's margin of success exceeds the attacker's, the Sever is fought off entirely. If the attacker wins, the Sever lands at the tier achieved.

| Tier | Exhaustion | Casting Time | Effect |
|------|-----------|--------------|--------|
| **Weak** | 6 | 5 counts | A brief, jarring disruption. Target caster's connection flickers — their current casting is interrupted (forces concentration check at -20%), and they suffer -10% to casting for 1d4 rounds. They feel it like a sudden headache. |
| **Standard** | 10 | 7 counts | The connection frays. Target cannot cast for 1d4 minutes. Active magical effects they're sustaining (shields, wards) begin to fade. They feel hollow, dizzy, like a sense has been cut off. Deeply unpleasant. |
| **Strong** | 16 | 10 counts | The connection is severed. Target cannot cast for 1d4 hours. All active magical effects they're sustaining collapse immediately. They feel deaf and blind to the magical world. Psychologically distressing — many targets panic. |
| **Spectacular** | 24 | 14 counts | Complete severance. Target cannot cast for 1d4 days. Their connection to mana is utterly silenced. Magical items on their person may temporarily lose attunement. The target often describes it as the worst experience of their life — a profound, existential emptiness. Other casters nearby can feel the severance happen, like a shockwave of absence. |
| *Misfire* | 6 | — | *The severance rebounds — the caster severs their own connection. They cannot cast for 1d4 hours and all their active effects collapse. The psychic shock deals 1d4 damage.* |

**Design notes:**
- Sever is the most expensive spell designed so far — Complexity 4. Spectacular Sever at 24 exhaustion will overflow for almost any caster. Shutting down another caster's magic for days should cost you nearly everything.
- **Opposed check required.** A powerful caster is naturally harder to Sever because their PW-based casting target is higher, giving them a larger resistance margin. A weak Ley Weaver cannot just spam Sever against a master and expect results. This is the template for how all targeted magical effects against casters should work.
- No physical damage at any tier — purely about stripping magical ability. But the psychological and narrative weight is enormous.
- Casting times are long (5-14 counts), making Sever very vulnerable to interruption on the timing track. You don't casually Sever someone — you commit, and your target has time to react (or their allies do).
- The misfire is poetic — you sever yourself. A Ley Weaver who misfires Sever is out of the fight for hours.

### 9.8 Cost Comparison — All Six Templates

| Spell | School | Complexity | Weak | Standard | Strong | Spectacular |
|-------|--------|-----------|------|----------|--------|-------------|
| Force | Aetheric | 1 | 2 / 2ct | 4 / 3ct | 6 / 4ct | 10 / 6ct |
| Shield | Warding | 2 | 3 / 3ct | 6 / 4ct | 9 / 6ct | 14 / 8ct |
| Reveal | Divination | 2 | 3 / 3ct | 6 / 5ct | 9 / 7ct | 14 / 10ct |
| Reshape | Transmutation | 2 | 3 / 3ct | 6 / 5ct | 9 / 7ct | 14 / 10ct |
| Mend | Vivimancy | 3 | 4 / 4ct | 8 / 6ct | 12 / 8ct | 18 / 12ct |
| Sever | Ley Weaving | 4 | 6 / 5ct | 10 / 7ct | 16 / 10ct | 24 / 14ct |

The complexity-to-cost pattern is consistent and predictable. All remaining spells should be designable by assigning a complexity rating and applying this framework.
