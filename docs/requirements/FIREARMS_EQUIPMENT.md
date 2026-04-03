# Firearms & Steampunk Equipment

## Document Status: DRAFT — First Pass
**Last Updated:** 2026-03-31

---

## 1. Design Philosophy

Firearms are **significantly more lethal** than melee weapons. A few well-placed shots will drop someone. This is intentional — modern weapons *should* be terrifying. The tradeoff is **magical interference**: guns fail near magic, and every spell your party's caster slings makes them worse.

This creates the game's central tactical tension: martial weapons always work, firearms are devastating but fragile, and party composition has real mechanical consequences.

**Feel over simulation.** The stat lines are tuned to evoke the *fantasy* of each weapon — the heavy reliability of a revolver, the devastating spray of a tommy gun — not to model ballistics. Complexity is hidden in the numbers.

---

## 2. Firearm Stats

Every firearm has five stats (exotic weapons add a sixth — **Aetheric**):

| Stat | Description |
|------|-------------|
| **Speed** | Timing track counts to fire one shot (or burst) |
| **Damage** | Dice rolled on a hit |
| **Capacity** | Shots before reload is required |
| **Reload** | Timing track counts to fully reload |
| **Reliability** | Resistance to malfunction. Malfunction chance = 100 − Reliability, checked BEFORE the Ranged roll. Higher = more resistant. Reduced by 2 per net Aetheric point. No check needed for conventional firearms in clean environments. See §4. |
| **Aetheric** | *(Exotic weapons only)* How much Galvanic accumulation the weapon generates per shot. Pushes the Aetheric balance toward tech. See §5. |

**Skill:** Firearms use the **Ranged** combat skill (same as bows/crossbows). The weapon's accuracy is baked into the damage code and speed — a tommy gun's terrible accuracy is reflected in its lower per-round damage relative to its fire rate, not a separate accuracy modifier.

---

## 3. Firearm Categories

Firearms follow the same **category + tag** system as melee weapons (see PROJECT_SPEC.md §4.2). Each category defines Speed, Damage, Capacity, Reload, and Reliability. Individual weapons are examples within a category — a player picks the narrative flavor, the stats come from the category line.

### 3.1 Modern Firearms

| Category | Speed | Damage | Capacity | Reload | Reliability | Examples |
|----------|-------|--------|----------|--------|-------------|----------|
| Holdout Pistol | 2 | 1d6 | 2 | 2 | 95 | Derringer, pocket pistol, muff pistol |
| Revolver | 3 | 2d6 | 6 | 3 | 95 | Service revolver, Colt, Webley |
| Semi-Auto Pistol | 3 | 2d6 | 8 | 2 | 85 | Browning, Luger, Mauser C96 |
| Heavy Pistol | 4 | 2d8 | 6 | 3 | 90 | Magnum revolver, hand cannon |
| Rifle | 6 | 2d10 | 5 | 4 | 95 | Bolt-action, Mauser, Springfield |
| Carbine | 5 | 2d8 | 8 | 5 | 90 | Lever-action, cavalry carbine, trench carbine |
| Shotgun | 4 | 3d6 | 2 | 2 | 95 | Break-action, coach gun, sawn-off |
| Combat Shotgun | 5 | 3d6 | 5 | 4 | 85 | Pump-action, trench gun |
| Submachine Gun | 5 | 3d6 | 50 | 3 | 70 | Tommy gun, MP18, Beretta M1918 |

> **Submachine Gun Note:** Each trigger pull consumes 3 rounds and deals 3d6 damage — representing a burst of fire and the chance of multiple hits. The terrible accuracy and recoil are baked into the damage code (3d6 avg 10.5 for 3 rounds is less per-bullet than a revolver). At 50-round drums, that's 16 bursts before reloading.

### 3.2 Steampunk Exotics

Exotic weapons are **rare, emerging technology** — expensive, unreliable, and viewed with suspicion. They represent the bleeding edge of Galvanic engineering — technology that channels forces from the Engine. Not magical, but leveraging principles that push back against the Aether. Each exotic weapon fired also generates **Galvanic accumulation** (see §5.5).

| Category | Speed | Damage | Capacity | Reload | Reliability | Aetheric | Examples |
|----------|-------|--------|----------|--------|-------------|----------|----------|
| Exotic Pistol | 3 | 1d10 | 12 | 2 | 70 | 1 | Pneumatic flechette, needle gun, compressed air pistol |
| Exotic Sidearm | 4 | 2d8 | 6 | 3 | 65 | 2 | Arc gun, voltaic pistol, spark thrower |
| Exotic Heavy | 7 | 3d8 | 3 | 5 | 55 | 3 | Aether lance, beam projector, lightning cannon |
| Exotic Melee | 2 | 1d8+PP | 10 | — | 60 | 1 | Shock gauntlet, arc knuckles, voltaic blade |

> **Exotic Availability:** These weapons cannot simply be purchased at a shop. They are prototype-level technology — acquired through faction connections, black markets, salvage, or theft. GMs should treat them as notable gear, not standard loadouts.

> **Exotic Melee** uses the Brawl skill (gauntlet) or Melee skill (blade). Capacity represents charges; recharges overnight or at a power source.

### 3.3 Firearm Tags

Tags work the same as melee weapon tags — they differentiate weapons within a category. Some tags are shared with melee (Concealable, Piercing), others are firearm-specific.

**Shared Tags (also apply to melee):**

| Tag | Effect |
|-----|--------|
| Concealable | Can be hidden on person. Draw speed 1 |
| Piercing | Ignores 2 points of armor soak |

**Firearm-Specific Tags:**

| Tag | Effect | Typical Weapons |
|-----|--------|-----------------|
| Reliable | +5 to effective Reliability in magic zones | Revolver, break-action shotgun, bolt-action rifle |
| Quick Reload | Reload time halved (round up) | Semi-auto pistol, lever-action carbine |
| Loud | Audible across the entire area. Draws attention, may panic civilians | Shotgun, heavy pistol, submachine gun |
| Quiet | Nearly silent. No audible report beyond immediate vicinity | Pneumatic flechette, suppressed pistol |
| Scatter | At close range (melee distance), +1d6 damage. At long range, −1d6 damage | Shotgun, combat shotgun, sawn-off |
| Burst | Fires multiple rounds per trigger pull. Consumes 3 ammo per shot | Submachine gun |
| Accurate | At long range, no penalty. +5% to hit on aimed shots | Bolt-action rifle, hunting rifle |
| Sawn-Off | −1 speed, −1 damage die step, gains Concealable | Sawn-off shotgun, cut-down rifle |

**Exotic-Specific Tags:**

| Tag | Effect | Typical Weapons |
|-----|--------|-----------------|
| Shocking | Ignores 2 points of metal armor soak (arcs through it) | Arc gun, shock gauntlet, voltaic blade |
| Suppressing | +1 to weapon's Aetheric rating per shot | Aether lance, beam projector |
| Silent | No audible report whatsoever | Pneumatic flechette, needle gun |
| Unstable | On malfunction severity roll, +2 instead of exotic's normal +1 | Aether lance, experimental prototypes |

### 3.4 Comparison: Melee vs. Firearms

| Category | Speed | Avg Damage | Eff | Always Works? |
|----------|-------|------------|-----|:---:|
| Medium Melee | 5 | 5.5 | 1.10 | Yes |
| Revolver | 3 | 7.0 | 2.33 | No |
| Rifle | 6 | 11.0 | 1.83 | No |
| Great Melee | 9 | 7.0 | 0.78 | Yes |
| Heavy Crossbow | 10 | 10.5 | 1.05 | Yes |

A revolver is **2x more efficient** than a medium melee weapon. A rifle does double a longsword's damage. This is the price of "swords always work." In a clean environment, firearms dominate. In a magically saturated area, they're expensive paperweights.

---

## 4. Malfunction System

### 4.1 The Firing Sequence

When a character fires a weapon, the sequence is:

1. **Reliability check (does it fire?)** — Roll d100 as a consequence check. Malfunction chance = **100 − Reliability**, modified by the Aetheric balance (+2% per net point). If the roll falls within the malfunction percentage, the weapon fails. The shot does not fire. Your action is spent.
2. **If it fires → Ranged skill check (does it hit?)** — Roll d100 under your Ranged skill target as normal. Hit, miss, or critical.
3. **If it malfunctions → Severity roll** — Roll d10 to determine how bad the malfunction is.

This mirrors spellcasting in reverse: magic commits the action first, then checks for consequences (backlash). Firearms check for failure first, then resolve the action. Both create tension at different moments.

### 4.2 When to Roll Reliability

**Every shot. Every time.** Reliability is always checked before the Ranged roll, regardless of environment. A tommy gun has a 30% malfunction chance in your living room. A revolver has 5%. That's the baseline — the inherent reliability of the mechanism.

The Aetheric balance modifies this: net Aetheric accumulation makes guns worse, net Galvanic accumulation makes them better. At effective Reliability 100+ (malfunction chance 0% or below), the weapon cannot malfunction — the Galvanic force is actively stabilizing it.

### 4.3 Malfunction Chance

**Malfunction chance** = 100 − effective Reliability

**Effective Reliability** = Base Reliability − (net balance × 2)

| Weapon | Base Rel | Base Malfunc. | At −10 Galvanic | At +5 Aetheric | At +10 Aetheric | At +15 Aetheric |
|--------|---------|--------------|-----------------|----------------|-----------------|-----------------|
| Revolver | 95 | 5% | 0% (can't fail) | 15% | 25% | 35% |
| Semi-Auto | 85 | 15% | 0% | 25% | 35% | 45% |
| Tommy Gun | 70 | 30% | 10% | 40% | 50% | 60% |
| Exotic Heavy | 55 | 45% | 25% | 55% | 65% | 75% |

At effective Reliability 100+ (malfunction chance 0% or below), the weapon **cannot malfunction** — the Galvanic force is holding it together. At effective Reliability 0 or below (malfunction chance 100%+), the weapon **simply does not function**.

*Example: A revolver (Rel 95) in clean air has a 5% malfunction chance. One shot in twenty goes wrong. You barely notice.*

*Example: That same revolver in a Galvanic Zone (−10): effective Rel 115, malfunction chance 0%. Cannot malfunction. The Engine is stabilizing every mechanism in the area.*

*Example: That same revolver in a Wild Zone (+15): effective Rel 65, malfunction chance 35%. One in three shots fails. And you still have to hit with the ones that fire.*

*Example: A tommy gun (Rel 70) at +10 Aetheric: effective Rel 50, malfunction chance 50%. Coin flip every shot. Time for swords.*

### 4.4 Malfunction Severity Table

When a weapon malfunctions, the shot doesn't fire and your action is wasted. Roll d10 to see if it's worse than that:

| d10 | Result | Effect |
|-----|--------|--------|
| 1–5 | **Click** | Nothing additional. Weapon is fine, just didn't fire this time. Try again next action. |
| 6–7 | **Jam** | Weapon is jammed. Clearing costs the weapon's Reload time in counts before it can fire again. |
| 8 | **Misfire** | Round discharges unpredictably. GM determines where it goes — stray shot hits something or someone nearby. |
| 9 | **Mechanical Failure** | Something breaks internally. Weapon is non-functional until repaired (out of combat, tools required, Repair skill check). |
| 10 | **Catastrophic** | Weapon is destroyed. Wielder takes 1d6 damage from the failure (shrapnel, electrical discharge, burst barrel, etc.). |

> **Exotic Escalation:** Exotic (Galvanic) weapons add +1 to the d10 severity roll (a 5 becomes a 6, etc., max 10). Their experimental nature means when things go wrong, they go *more* wrong.

### 4.5 Design Parallel

The firearm sequence mirrors spellcasting in reverse:

| Step | Magic | Firearms |
|------|-------|----------|
| 1 | Cast: roll skill, spell fires | Check Reliability: does the weapon fire? |
| 2 | Check backlash: did the magic bite you? | Roll Ranged: did you hit? |
| Consequence | Backlash hurts the caster | Malfunction hurts the weapon |
| Tension point | After the action (will I get burned?) | Before the action (will it even work?) |

Same mechanical shape, different fiction. Magic risks the caster. Technology risks the tool.

---

## 5. The Aetheric Balance — The Number Line

### 5.1 The Core Concept

Magic and technology pull the environment in opposite directions. The area's **Aetheric Balance** is a single sliding scale — a number line with neutral (zero) in the middle. Spells push it toward magic. Exotic tech pushes it toward tech. The **net value** determines who suffers.

- **Net positive (magic-heavy):** Technology suffers. Firearms lose Reliability.
- **Net negative (tech-heavy):** Magic suffers. Casting targets drop.
- **At zero:** Neither side is penalized.

Conventional firearms and martial weapons don't move the needle in either direction. They're bystanders — affected by the balance, but not affecting it.

### 5.2 What Moves the Balance

**Toward magic (positive):**

| Source | Accumulation |
|--------|-------------|
| Spell — Misfire (failed cast) | 0 |
| Spell — Weak | +1 |
| Spell — Standard | +2 |
| Spell — Strong | +3 |
| Spell — Spectacular | +4 |

**Toward tech (negative):**

Each exotic item has an **Aetheric rating** — how much it shifts the balance per use.

| Source | Accumulation |
|--------|-------------|
| Exotic weapon shot | −(weapon's Aetheric rating) per shot |
| Suppressing tag | Adds +1 to weapon's Aetheric rating |
| Non-weapon exotic device | −(device's Aetheric rating) per activation or per minute sustained |

| Exotic Category | Aetheric Rating |
|-----------------|----------------|
| Exotic Pistol | 1 |
| Exotic Sidearm | 2 |
| Exotic Heavy | 3 |
| Exotic Melee | 1 per charge used |

Non-weapon exotics (aetheric generators, plasma shields, resonance engines) are assigned Aetheric ratings by the GM based on their scale and power. A portable aetheric lamp might be 1; a factory-scale resonance engine might be 10+.

Accumulation is **localized** — it affects the immediate area (a room, a street corner, a clearing). GM adjudicates boundaries.

### 5.3 The Net Effect

Only the **net balance** matters. Each net point shifts **both sides** — penalizing one while empowering the other:

- **Effective Reliability** = Base Reliability − (net balance × 2)
- **Effective Casting Target** = Base Target + (net balance × 2)

Positive net (Aetheric) hurts firearms AND helps magic. Negative net (Galvanic) hurts magic AND helps firearms.

**Reliability is always checked.** Every shot, every time. A tommy gun (Rel 70) has a 30% malfunction chance even in clean air — that's the price of burst fire. A revolver (Rel 95) has a 5% chance. In most cases you won't notice. In a Wild Zone, you'll notice fast. At effective Reliability 100 or above (malfunction chance 0% or below), the weapon cannot malfunction. At effective Reliability 0 or below, the weapon simply does not function.

| Net Balance | Eff. Revolver (95) | Malfunction% | Eff. Tommy (70) | Malfunction% | Casting Mod |
|-------------|----|----|----|----|-----|
| +20 (Deep Wild) | 55 | 45% | 30 | 70% | +40 |
| +15 (Wild Zone) | 65 | 35% | 40 | 60% | +30 |
| +10 (heavy magic) | 75 | 25% | 50 | 50% | +20 |
| +5 (moderate magic) | 85 | 15% | 60 | 40% | +10 |
| 0 (neutral) | 95 | 5% | 70 | 30% | +0 |
| −5 (moderate Galvanic) | 105 | 0% | 80 | 20% | −10 |
| −10 (heavy Galvanic) | 115 | 0% | 90 | 10% | −20 |
| −15 (Galvanic Zone) | 125 | 0% | 100 | 0% | −30 |
| −20 (Deep Galvanic) | 135 | 0% | 110 | 0% | −40 |

**Example:** Three spells generate +12. Two exotic sidearm shots generate −4. Net = +8 (Aetheric). Firearms lose 16 Reliability — a revolver is at effective 79 (21% malfunction). But casters gain +16 to their targets. A caster with base 55 is now at 71 — Strong tier is within easy reach. The magic feeds on itself.

**Example (reversed):** One spell generates +2. An aether lance fires three times (−4 each = −12). Net = −10 (Galvanic). Casting targets drop by 20 — that base-55 caster is at 35, barely managing Standard. But firearms gain +20 Reliability. The tommy gun (70 + 20 = 90) has only a 10% malfunction chance. The Engine is drowning out the Veil.

> **Design Note:** The symmetric model means zones don't just suppress one force — they actively empower the other. A Wild Zone isn't just "guns don't work here." It's "magic is *incredible* here." A Galvanic factory isn't just "spells fail." It's "firearms are *perfect*." This makes zone-specific encounters feel dramatically different in both directions.

### 5.4 Decay

Accumulation decays toward the area's **baseline** at **1 point per minute**.

- In a normal area, baseline is 0. An accumulation of +8 takes 8 minutes to fully clear.
- In an environmental zone, baseline is the zone's permanent value (see §5.5). Added accumulation decays, but the base never changes.

> **Slow Decay Is A Feature:** The lingering residue is narratively significant. Magical forensics experts can track casters by their residue trails. A neighborhood where a Spectacular spell was cast an hour ago still reads as magically active.

### 5.5 Environmental Zones

Some areas have a permanent **baseline accumulation** that the balance decays toward instead of zero:

| Zone Type | Baseline | Effect |
|-----------|----------|--------|
| Deep Galvanic Zone | −25 or more | Magic non-functional. The Engine roars. |
| Galvanic Zone | −15 to −20 | Most spells fail. Galvanic devices thrive. |
| Moderate Galvanic Zone | −8 to −12 | Only powerful casters can push through. |
| Light Galvanic Zone | −3 to −5 | Casting noticeably harder. Tech runs clean. |
| Normal / In-Between | 0 | Everything works until someone tips the balance. |
| Light Aetheric Zone | +3 to +5 | Firearms slightly less reliable. Sensitive equipment twitchy. |
| Moderate Aetheric Zone | +8 to +12 | Only reliable firearms work. |
| Wild Zone | +15 to +20 | Most firearms non-functional. Strange creatures. Reality gets soft. |
| Deep Wild Zone | +25 or more | Swords and sorcery only. |

Spellcasting and exotic tech use **shifts the balance from the baseline**. A party firing exotic weapons in a Wild Zone (+15 baseline) can temporarily push the balance down — from +15 to +10, say — making firearms briefly usable. But once they stop, the balance drifts back to +15.

> **Zone formation, gradients, and environmental staining** are setting-level concepts documented in PROJECT_SPEC.md §2.3. Full zone mechanics (how zones form, shift, and interact over time) are deferred to a dedicated design session.

### 5.6 Tactical Implications

- **The tug-of-war.** Your caster and your exotic gunner are pulling the environment in opposite directions. Coordinating who acts when is a real tactical decision.
- **Party composition matters.** A caster makes your guns worse. An exotic gunner makes your spells worse. Smart parties balance their loadout — and carry a sword for when both sides cancel out.
- **Exotic weapons are anti-magic fields.** Carrying an arc gun into a fight against casters has value beyond the damage. Every shot pushes the balance toward tech, penalizing enemy casting.
- **Zone scouting.** Checking an area's balance before committing is smart tactics. Walking into a Wild Zone with only firearms is suicide.
- **The last-spell problem.** Your caster dropping a Spectacular spell (+4) mid-firefight might win the moment but costs the party's firearms for the next several minutes. Timing matters.
- **Asymmetric warfare.** Cultists in a magically charged lair don't need guns. Factory district enforcers don't need magic. Adventurers operating in both worlds need versatility.

---

## 6. Steampunk Equipment (Non-Weapons)

> **NOTE:** Prices and a full equipment list are deferred to the currency/economy design session. Below are categories and notable items that have mechanical implications.

### 6.1 Equipment Categories

**Field Gear:**
- Aether lanterns (magical light sources, no fuel needed, useless in Dead Zones)
- Compressed air grapples
- Portable generators (for powering gadgets in the field)
- Communication devices (short-range radio, unreliable near magic)

**Investigation Tools:**
- Magical residue detectors (measures local Accumulation — the magical forensics toolkit)
- Photographic equipment (1920s cameras, flash powder)
- Lock-picking kits (mechanical and aetheric variants)
- Alchemical field kits

**Protective Gear:**
- Gas masks
- Insulated gloves (for handling magical artifacts or live aether conduits)
- Reinforced goggles (protect against arc flash, magical flares)

**Transport:**
- Automobiles (unreliable in magic zones)
- Motorcycles (faster, lighter, same zone problems)
- Airships (major zone vulnerability — a stalled engine at altitude is catastrophic)
- Horses (always work, eat oats, don't care about magic)

> **Vehicle rules** are deferred to a separate session. Key principle: vehicles suffer from Aetheric accumulation the same way firearms do, using a vehicle-level Reliability score.

### 6.2 Modern Armor Supplement

The existing armor table covers medieval-style armor. Modern additions:

| Armor Type | Soak | Hinder | Reliability | Notes |
|------------|------|--------|-------------|-------|
| Leather Jacket | 1 | — | — | Not really armor. Looks good |
| Trench Coat (lined) | 2 | — | — | Reinforced leather and wool. No tech to fail |
| Ballistic Vest | 5 | — | 80 | Experimental. Can degrade in magic zones |
| Steel Breastplate | 6 | 1 | — | Old-fashioned but magic-proof |

> **Ballistic Vest Note:** This is bleeding-edge technology in the setting. Reliability applies the same way as firearms — in high-accumulation areas, the experimental materials may lose structural integrity. Traditional metal and leather armor never has this problem.

---

## 7. Open Questions

1. **Crossbow Reliability:** Current table has heavy crossbow at 3d6. Should crossbows have Reliability scores? They're mechanical but much simpler than firearms. Proposed: no — they're simple enough to be treated as martial weapons.
2. **Ammunition Types:** Special ammo (incendiary, armor-piercing, silver bullets for magical creatures)? Or is that overcomplicating it?
3. **Dual Wielding:** Pistol in each hand? Flavor is great for the setting. Mechanically — second pistol at +2 speed and a penalty to hit?
4. **Weapon Modifications:** Scopes, extended magazines, silencers? Or keep it simple with the base weapon tables?
5. **Melee Weapon Rebalancing:** Current melee table may need adjustment now that firearms set the damage ceiling. Does a dagger at 1d4 still feel right when a derringer does 1d6?
6. **Aetheric accumulation Exact Decay:** 1 per minute is the baseline. Should this vary by environment? (Faster in Dead Zones, slower in Wild Zones?)
7. **Malfunction Check Frequency:** Every shot? Every burst? Once per engagement at current accumulation? Every shot is grittier but more rolls.
