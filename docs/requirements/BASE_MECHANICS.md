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
| PW | Power | Magical ability, attunement |

**Character creation:** Distribute stats with a net bonus set by GM (default **+1**). Player describes a roleplay justification for each value.

---

## 4. Skills

### 4.1 Skill Target Number

```
((10 + associated stat) × skill level) + 30
```

*Example: Melee at skill level 3, PC +2 → ((10 + 2) × 3) + 30 = 66.*

### 4.2 Unskilled Attempt

```
(5 + associated stat) × 10
```

*Example: Unskilled Athletics, PC +1 → (5 + 1) × 10 = 60. Unskilled Medicine, IN -1 → (5 + -1) × 10 = 40.*

### 4.3 Skill Points

Skill points are allocated per stat group:

```
10 + stat group net modifiers
```

| Group | Stats | Skills |
|-------|-------|--------|
| Physical | PP, PC | Athletics, Brawl, Climbing, Conceal, Melee, Ranged, Running, Swimming |
| Mental | IN, AW | Acting, Boating, Disarm Trap, Disguise, Empathy, Engineering, Forgery, Hunting, Medicine, Metalworking, Music, Observation, Repair, Ride/Drive, Science, Security, Stealth, Survival, Tactics, Woodworking |
| Social | SP | Business, Etiquette, Gambling, Interrogation, Leadership, Persuasion |

**Skill cap:** Maximum 15 skills per character.

*Example: PP +2, PC +1 → Physical skill points = 10 + 2 + 1 = 13.*

> **NOTE:** Skill list pending revision for steampunk setting (add Firearms, Pilot, Occult Lore, Streetwise, etc.).

---

## 5. Derived Values

| Value | Formula |
|-------|---------|
| HP per wound tier | 7 + PP |
| MP per exhaustion tier | 7 + PW |
| Skill target number | ((10 + stat) × skill level) + 30 |
| Unskilled attempt | (5 + stat) × 10 |
| Concentration check | (PW + 4) × 10 |
| Cancellation cost | Half the Weak tier exhaustion (per spell) |

**Wound tiers (HP):**

| Tier | Status | Penalty |
|------|--------|---------|
| 1 | OK | None |
| 2 | Harmed | -10% to all rolls |
| 3 | Maimed | -25% to all rolls |
| 4 | Incapacitated | -50% to all rolls |

**Exhaustion tiers (MP):**

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
8. Area gains Magic Accumulation (Weak +1, Standard +2, Strong +3, Spectacular +4).

### 6.2 Two Paths

| | Scholarly | Wild |
|--|----------|------|
| Spellbook | Required — spells must be in your book | No — cast any spell in known schools |
| Tier control | Full — choose any tier at or below your roll | None — locked to the tier rolled |
| Backlash | Base rates | Higher (TBD modifier) |
| Schools | PW modifier + bonus (TBD) | PW modifier (min 1) |
| Base spells | 7 + PW | 7 + PW |

### 6.3 Exhaustion Overflow

When a spell's exhaustion exceeds remaining MP, the spell still fires. Remaining MP drops to zero (Incapacitated). Overflow converts to **physical HP damage at half rate** (rounded down).

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

### 7.1 The Rules

- **Magic erodes technology.** Each spell cast generates Magic Accumulation. Each point reduces nearby firearm Reliability by 3%.
- **Only exotic tech erodes magic.** Each exotic weapon shot generates 1 Tech Accumulation. Each point applies -3 to casting target numbers.
- **Conventional tech and martial weapons are neutral.** A revolver doesn't push back against magic. A steel sword doesn't care about zones.

### 7.2 Accumulation

| Spell Tier | Magic Accumulation |
|------------|-------------------|
| Weak | +1 |
| Standard | +2 |
| Strong | +3 |
| Spectacular | +4 |

**Decay:** 1 point per minute for both Magic and Tech Accumulation.

### 7.3 Magic Zones

| Zone | Base Accumulation | Effect |
|------|-------------------|--------|
| Industrial Dead Zone | 0 (tech zone) | Magic suppressed, tech works perfectly |
| Normal | 0 | Both work unless casting occurs |
| Light Magic Zone | 3-5 | Revolvers fine, exotics sketchy |
| Moderate Magic Zone | 8-12 | Only reliable firearms work |
| Wild Zone | 15-20 | Most firearms non-functional |
| Deep Wild Zone | 25+ | Swords and sorcery only |

> Full zone mechanics pending dedicated design session.

---

## 8. Recovery

| Type | Rate | Bonus |
|------|------|-------|
| Physical damage | 1d4 HP per hour of full rest | +1d4 with medical care |
| Magical exhaustion | 1d8 MP per hour of full rest | — |
| Armor repair | Metalworking/Repair check | Downtime, tools required |

---

## 9. Character Creation (Quick Steps)

1. **Stats:** Distribute across 6 stats (-3 to +3). Net bonus set by GM (default +1). Justify each value.
2. **Skills:** Up to 15. Points per group = 10 + stat group net.
3. **Spells (if caster):** 7 + PW base spells. Schools = PW modifier (min 1). Scholarly casters need a spellbook. Extra spells cost 3 skill points each.
4. **Archetype label:** Name your character concept. Flavor, not restriction.
5. **Derived values:** HP per tier (7+PP), MP per tier (7+PW), skill targets, concentration check target.
6. **Equip:** Weapons (category + 1-2 tags), armor, gear.

---

## 10. One-Page Rules Summary

```
THE ROLL: d100 ≤ target = success
  01 = always crit │ 00 = always fumble
  Crit range: 1pt per 25% of target, counted down from target

OPPOSED: both roll, larger margin wins │ one success beats one fail

STATS: PP PC IN SP AW PW │ range -3 to +3

SKILL TARGET: ((10 + stat) × level) + 30
UNSKILLED:    (5 + stat) × 10

WOUNDS (HP per tier = 7+PP)     EXHAUSTION (MP per tier = 7+PW)
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
  3% Reliability penalty per point │ Decays 1/minute

CONCENTRATION: (PW + 4) × 10
  PW-3=10% │ PW+0=40% │ PW+3=70%

RECOVERY: HP 1d4/hour │ MP 1d8/hour │ +1d4 HP with medical care
```
