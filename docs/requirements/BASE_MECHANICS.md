# Base Mechanics Reference

## Document Status: DRAFT — Playtest Ready
**Last Updated:** 2026-03-31

Quick reference for core rules. For combat, see COMBAT_PROCEDURE.md. For full magic details, see MAGIC_SYSTEM.md.

---

## 1. The Core Roll

**d100 roll-under.** Roll equal to or under your target number = success.

- **01:** Always a critical success.
- **00 (double zeros):** Always a critical failure.
- **Critical range:** 1 point per 25% of your target number, counted down from target.

| Target Number | Crit Range | Crit On |
|---------------|------------|---------|
| 1-25 | 0 | 01 only |
| 26-50 | 1 | Target value only |
| 51-75 | 2 | Target and target-1 |
| 76-99 | 3 | Target, target-1, target-2 |

*Example: Skill target 65 → crit range 2 → crits on 63, 64, 65.*

---

## 2. Opposed Checks

When two characters act in direct opposition, both roll d100 against their relevant target number.

- **Both succeed:** Larger margin (target minus roll) wins.
- **One succeeds, one fails:** The success wins.
- **Both fail:** Stalemate — situation doesn't change. GM adjudicates.

*Examples: arm wrestling (PP vs PP), chase (Running vs Running), stealth vs observation, resisting a spell (caster's roll vs target's PW).*

---

## 3. Stats

Six stats, rated **-3 to +3.**

| Abbr | Stat | Covers |
|------|------|--------|
| PP | Physical Prowess | Strength, endurance, fortitude |
| PC | Physical Coordination | Grace, dexterity, finesse |
| IN | Intellect | Knowledge, quick-thinking, academics |
| SP | Social Prowess | Etiquette, poise, likability |
| AW | Awareness | Perception, alertness, eye for detail |
| PW | Power | Mental fortitude, resilience, magical attunement |

**Character creation:** Distribute stats with a net bonus set by GM (default **+1**). Player describes a roleplay justification for each value.

---

## 4. Skills

> Full skill list with descriptions: [SKILLS_PROGRESSION.md](../requirements/SKILLS_PROGRESSION.md)

### 4.1 Skill Target Number

```
((10 + associated stat) × skill level) + 30
```

*Example: Melee at skill level 3, PC +2 → ((10 + 2) × 3) + 30 = 66.*

### 4.2 Unskilled Attempt

```
(5 + associated stat) × 5
```

*Example: Unskilled Athletics, PP +1 → (5 + 1) × 5 = 30. Unskilled Medicine, IN -1 → (5 + -1) × 5 = 20.*

### 4.3 Skill Points

Skill points are allocated per stat group:

```
10 + stat group net modifiers
```

| Group | Stats | Skills |
|-------|-------|--------|
| Physical | PP, PC | Athletics (PP), Brawl (PP), Melee (PP), Intimidation ★ (PP), Firearms (PC), Piloting (PC), Ranged (PC), Sleight of Hand (PC), Stealth (PC) |
| Mental | IN, AW, PW | Craft (IN), Engineering (IN), Medicine (IN), Occult Lore (IN), Science (IN), Tactics (IN), Empathy (AW), Investigation (AW), Observation (AW), Survival (AW), Resolve (PW), Scholarly Casting (PW), Wild Casting (PW) |
| Social | SP | Deception, Etiquette, Intimidation ★, Leadership, Persuasion, Streetwise |

**Skill cap:** Maximum 15 skills per character.
**Character creation cap:** 3 per skill. **Gameplay maximum:** 5 per skill.

*Example: PP +2, PC +1 → Physical skill points = 10 + 2 + 1 = 13.*

> ★ **Intimidation** is a flex-stat skill. Place it under PP (physical menace) or SP (social pressure) — your choice at character creation.

### 4.4 Progression

**1 XP per session** (automatic) + bonus XP from table vote for standout moments. Typical rate: 1–2 XP per session.

| Action | Cost |
|--------|------|
| Advance skill to level N | N XP |
| Raise an attribute by 1 | 10 XP |

*Example: Skill 3→4 costs 4 XP. Skill 3→5 costs 4+5 = 9 XP. Attribute +1→+2 costs 10 XP.*

---

## 5. Derived Values

| Value | Formula |
|-------|---------|
| HP per wound tier | 7 + PP |
| EP per exhaustion tier | 7 + PW |
| Skill target number | ((10 + stat) × skill level) + 30 |
| Unskilled attempt | (5 + stat) × 5 |
| Concentration check | (PW + 4) × 10 |
| Cancellation cost | Half the Weak tier exhaustion (per spell) |

**Wound tiers (HP):**

| Tier | Status | Penalty |
|------|--------|---------|
| 1 | OK | None |
| 2 | Harmed | -10% to all rolls |
| 3 | Maimed | -25% to all rolls |
| 4 | Incapacitated | -50% to all rolls |

**Exhaustion tiers (EP) — covers all non-physical strain: stress, fatigue, stun, magical drain:**

| Tier | Status | Penalty |
|------|--------|---------|
| 1 | OK | None |
| 2 | Weakened | -10% to all rolls |
| 3 | Severely Weak | -25% to all rolls |
| 4 | Incapacitated | -50% to all rolls |

Wound and exhaustion penalties **stack.** Harmed + Weakened = -20%.

---

## 6. Magic (Summary)

Full rules in MAGIC_SYSTEM.md. Spell details in SPELL_COMPENDIUM.md.

### 6.1 Casting

1. Declare spell. Place token on timing track (each spell has a fixed casting time).
2. When token resolves, roll d100 against casting target number.
3. Margin determines tier: 1-10 = Weak, 11-30 = Standard, 31-50 = Strong, 51+ = Spectacular.
4. **Scholarly casters** choose to accept or restrict down to a lower tier.
5. **Wild casters** take what the magic gives them.
6. Pay exhaustion for the tier used.
7. Backlash check (Weak 5%, Standard 10%, Strong 15%, Spectacular 25%).
8. Area gains Aetheric accumulation (Weak +1, Standard +2, Strong +3, Spectacular +4).

### 6.2 Two Paths

| | Scholarly | Wild |
|--|----------|------|
| Casting roll | 1d100 (straight) | 2d100, take farther from target |
| Target bonus | None | +10 (natural attunement) |
| Spellbook | Required — learned spells only | No — all spells in known schools |
| Tier control | Full — choose any tier at or below your roll | Suppress 0-2 tiers based on skill |
| Backlash | Base rates (5%/10%/15%/25%) | +5% flat per tier |
| Schools | All six schools | PW modifier (min 1) |
| Spells | 7 + PW learned spells (buy more at 3 pts) | All spells in accessible schools |

### 6.3 Exhaustion Overflow

When a spell's exhaustion exceeds remaining EP, the spell still fires. Remaining EP drops to zero (Incapacitated). Overflow converts to **physical HP damage at half rate** (rounded down).

### 6.4 Ritual Spells

Some spells are too complex for combat casting:

| Spell | Ritual Time | Purpose |
|-------|-------------|---------|
| Scry | 10 minutes | Remote viewing |
| Shape Flesh | 30 minutes | Biological transformation |
| Circle | 30 minutes | Inscribed bounded zone |
| Transmute | 1 hour | Material substance change |

Ritual spells still require the casting roll, pay exhaustion, and risk backlash — they just can't be used on the timing track.

---

## 7. Magic & Technology Interference

### 7.1 The Aetheric Balance

A single sliding scale. Spells push toward Aetheric (magic). Galvanic devices push toward Galvanic (tech). Each net point shifts **both sides** — penalizing one while empowering the other:

- **Effective Reliability** = Base Reliability − (net balance × 2)
- **Effective Casting Target** = Base Target + (net balance × 2)

Net Aetheric hurts firearms AND helps magic. Net Galvanic hurts magic AND helps firearms. Reliability is **always checked** — every shot, every time. Conventional tech and martial weapons don't move the balance, but a steel sword doesn't care about it either.

### 7.2 What Moves the Balance

| Source | Shift |
|--------|-------|
| Spell (by tier) | +1/+2/+3/+4 Aetheric |
| Galvanic weapon (by Aetheric rating) | −1/−2/−3 Galvanic (Pistol 1, Sidearm 2, Heavy 3) |
| Suppressing tag | +1 to weapon's Aetheric rating |

**Decay:** 1 point per minute toward zone baseline (normal areas = 0).

### 7.3 Examples

**Aetheric example:** Sera casts two Standard spells (+2 each = +4 Aetheric). Net balance: +4. Firearms lose 8 Reliability — a revolver (95) is at effective 87 (13% malfunction). Sera's casting target gains +8 — her base 55 is now 63. The Aether is feeding her magic while making the guns twitchy.

**Galvanic example:** A factory enforcer fires an arc gun (Aetheric 2) three times (−2 each = −6 Galvanic). Net: −6. Casting targets drop by 12 — a caster with base 55 is at 43, barely managing Standard. Firearms gain +12 Reliability — the enforcer's semi-auto (85 + 12 = 97) has only a 3% malfunction chance. The Engine empowers its own.

**Both sides in combat:** Sera casts Standard Force (+2 Aetheric). The enforcer fires his arc gun twice (−4 Galvanic). Net: −2 Galvanic. Sera's target drops by 4 (55 → 51). The enforcer's revolver gains +4 Reliability (95 → 99, 1% malfunction). Sera needs to cast more to tip the balance back, but every spell at a reduced target is more likely to misfire.

### 7.4 Zones

| Zone | Baseline | Effect |
|------|----------|--------|
| Deep Galvanic Zone | −25 or more | Magic non-functional. The Engine roars. |
| Galvanic Zone | −15 to −20 | Most spells fail. Galvanic devices thrive. |
| Moderate Galvanic Zone | −8 to −12 | Only powerful casters can push through. |
| Light Galvanic Zone | −3 to −5 | Casting noticeably harder. Tech runs clean. |
| Normal | 0 | Both work until someone tips the balance. |
| Light Aetheric Zone | +3 to +5 | Firearms slightly less reliable. |
| Moderate Aetheric Zone | +8 to +12 | Only reliable firearms work. |
| Wild Zone | +15 to +20 | Most firearms non-functional. |
| Deep Wild Zone | +25 or more | Swords and sorcery only. |

> Full zone mechanics pending dedicated design session.

---

## 8. Recovery

| Type | Rate | Bonus |
|------|------|-------|
| Physical damage | 1d4 HP per hour of full rest | +1d4 with medical care |
| Exhaustion (mental) | 1d8 EP per hour of full rest | — |
| Armor repair | Metalworking/Repair check | Downtime, tools required |

---

## 9. Character Creation (Quick Steps)

1. **Stats:** Distribute across 6 stats (-3 to +3). Net bonus set by GM (default +1). Justify each value.
2. **Skills:** Up to 15. Points per group = 10 + stat group net.
3. **Spells (if caster):** Magic is a skill choice (Scholarly or Wild). 7 + PW base spells (min 1). Schools = PW modifier (min 1). Scholarly casters need a spellbook. Extra spells cost 3 skill points each.
4. **Archetype label:** Name your character concept. Flavor, not restriction.
5. **Derived values:** HP per tier (7+PP), EP per tier (7+PW), skill targets, concentration check target.
6. **Equip:** Weapons (category + 1-2 tags), armor, gear.

---

## 10. One-Page Rules Summary

```
THE ROLL: d100 ≤ target = success
  01 = always crit │ 00 = always fumble
  Crit range: 1pt per 25% of target, counted down from target

OPPOSED: both roll, larger margin wins │ one success beats one fail

STATS: PP PC IN SP AW PW │ range -3 to +3

SKILL TARGET: ((10 + stat) × level) + 30   max level 5 (cap 3 at creation)
UNSKILLED:    (5 + stat) × 5

XP: 1/session + table vote bonus │ Skill to N costs N │ Attribute +1 costs 10

WOUNDS (HP per tier = 7+PP)     EXHAUSTION (EP per tier = 7+PW)
  OK         —                    OK          —
  Harmed    -10%                  Weakened   -10%
  Maimed    -25%                  Sev. Weak  -25%
  Incap     -50%                  Incap      -50%
  Penalties STACK across both tracks

CASTING: fixed time per spell → roll d100 → tier by margin
  1-10 Weak │ 11-30 Standard │ 31-50 Strong │ 51+ Spectacular
  Scholarly: choose tier │ Wild: ride the wave
  Backlash: W5% S10% St15% Sp25% → 1d4 damage + 25% wild effect

ACCUMULATION: each spell adds tier value to area
  2% Reliability penalty per point │ Decays 1/minute

CONCENTRATION: (PW + 4) × 10
  PW-3=10% │ PW+0=40% │ PW+3=70%

RECOVERY: HP 1d4/hour │ EP 1d8/hour │ +1d4 HP with medical care
```
