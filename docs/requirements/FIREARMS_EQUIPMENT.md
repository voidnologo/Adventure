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

Every firearm has five stats:

| Stat | Description |
|------|-------------|
| **Speed** | Timing track counts to fire one shot (or burst) |
| **Damage** | Dice rolled on a hit |
| **Capacity** | Shots before reload is required |
| **Reload** | Timing track counts to fully reload |
| **Reliability** | Base percentage — resistance to malfunction (see §4) |

**Skill:** Firearms use the **Ranged** combat skill (same as bows/crossbows). The weapon's accuracy is baked into the damage code and speed — a tommy gun's terrible accuracy is reflected in its lower per-round damage relative to its fire rate, not a separate accuracy modifier.

---

## 3. Firearm Categories

Firearms follow the same **category + tag** system as melee weapons (see PROJECT_SPEC.md §4.2). Each category defines Speed, Damage, Capacity, Reload, and Reliability. Individual weapons are examples within a category — a player picks the narrative flavor, the stats come from the category line.

### 3.1 Modern Firearms

| Category | Speed | Damage | Capacity | Reload | Reliability | Examples |
|----------|-------|--------|----------|--------|-------------|----------|
| Holdout Pistol | 2 | 1d6 | 2 | 4 | 95 | Derringer, pocket pistol, muff pistol |
| Revolver | 3 | 2d6 | 6 | 6 | 95 | Service revolver, Colt, Webley |
| Semi-Auto Pistol | 3 | 2d6 | 8 | 3 | 85 | Browning, Luger, Mauser C96 |
| Heavy Pistol | 4 | 2d8 | 6 | 6 | 90 | Magnum revolver, hand cannon |
| Rifle | 6 | 2d10 | 5 | 8 | 95 | Bolt-action, Mauser, Springfield |
| Carbine | 5 | 2d8 | 8 | 10 | 90 | Lever-action, cavalry carbine, trench carbine |
| Shotgun | 4 | 3d6 | 2 | 4 | 95 | Break-action, coach gun, sawn-off |
| Combat Shotgun | 5 | 3d6 | 5 | 8 | 85 | Pump-action, trench gun |
| Submachine Gun | 5 | 3d6 | 50 | 5 | 70 | Tommy gun, MP18, Beretta M1918 |

> **Submachine Gun Note:** Each trigger pull consumes 3 rounds and deals 3d6 damage — representing a burst of fire and the chance of multiple hits. The terrible accuracy and recoil are baked into the damage code (3d6 avg 10.5 for 3 rounds is less per-bullet than a revolver). At 50-round drums, that's 16 bursts before reloading.

### 3.2 Steampunk Exotics

Exotic weapons are **rare, emerging technology** — expensive, unreliable, and viewed with suspicion. They represent the bleeding edge of aetheric engineering. Not magical themselves, but leveraging principles that flirt with the boundary. Each exotic weapon fired also generates **Tech Accumulation** (see §5.5).

| Category | Speed | Damage | Capacity | Reload | Reliability | Examples |
|----------|-------|--------|----------|--------|-------------|----------|
| Exotic Pistol | 3 | 1d10 | 12 | 4 | 70 | Pneumatic flechette, needle gun, compressed air pistol |
| Exotic Sidearm | 4 | 2d8 | 6 | 6 | 65 | Arc gun, voltaic pistol, spark thrower |
| Exotic Heavy | 7 | 3d8 | 3 | 8 | 55 | Aether lance, beam projector, lightning cannon |
| Exotic Melee | 2 | 1d8+PP | 10 | — | 60 | Shock gauntlet, arc knuckles, voltaic blade |

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
| Suppressing | Generates +1 Tech Accumulation per shot (beyond the base 1) | Aether lance, beam projector |
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

### 4.1 When to Roll

A **malfunction check** is required when firing a weapon with a Reliability score under any of these conditions:

1. **Magic Accumulation is present** in the area (see §5)
2. **Exotic weapons** always roll a malfunction check, even with zero accumulation
3. **GM calls for it** in narratively appropriate situations (dropped weapon, submerged, damaged, etc.)

**The check:** Roll d100 **every shot** (or burst, for automatic weapons). If the result is **over** the weapon's current effective Reliability, the weapon malfunctions. This mirrors spellcasting, where every cast requires a roll — same rhythm, same tension.

**Effective Reliability** = Base Reliability − (Magic Accumulation × 3)

*Example: A revolver (Reliability 95) in an area with 4 points of Magic Accumulation has effective Reliability 83. Roll over 83 = malfunction. Still quite reliable — a couple of spells isn't enough to shut down a good sidearm.*

*Example: A tommy gun (Reliability 70) in the same area has effective Reliability 58. Getting dicey, but still more likely to fire than not.*

*Example: After heavy casting (12 accumulation), the revolver drops to 59 — unreliable. The tommy gun hits 34 — more likely to malfunction than fire. Time for swords.*

### 4.2 Base Malfunction: Lost Action

On any malfunction, the shot **does not fire**. The timing counts for the shot are spent — you've pulled the trigger and nothing happened. Your action is wasted.

### 4.3 Malfunction Severity Table

After any malfunction, roll d10 to determine if something worse happens:

| d10 | Result | Effect |
|-----|--------|--------|
| 1–5 | **Click** | No additional effect. Weapon is fine, just didn't fire. Try again. |
| 6–7 | **Jam** | Weapon is jammed. Clearing costs the weapon's Reload time in timing counts before it can fire again. |
| 8 | **Misfire** | Round discharges unpredictably. GM determines where it goes — stray shot hits something or someone nearby. |
| 9 | **Mechanical Failure** | Something breaks. Weapon is non-functional until repaired (out of combat, tools required, Repair skill check). |
| 10 | **Catastrophic** | Weapon is destroyed. Wielder takes 1d6 damage from the failure (shrapnel, electrical discharge, burst barrel, etc.). |

> **Exotic Escalation:** Exotic weapons add +1 to the d10 malfunction severity roll (a 5 becomes a 6, etc., max 10). Their experimental nature means when things go wrong, they go *more* wrong.

### 4.4 Design Parallel

This system deliberately mirrors **spell backlash**: a base cost (lost action / MP cost) plus a severity table for worse outcomes. Same mechanical shape, different fiction — reinforcing the magic/tech parallel at the system level.

---

## 5. Magic Accumulation

### 5.1 How It Works

Every spell cast in an area generates **Magic Accumulation** — residual magical energy that lingers and disrupts technology.

| Spell Tier Achieved | Accumulation Generated |
|---------------------|----------------------|
| Misfire | 0 |
| Weak | 1 |
| Standard | 2 |
| Strong | 3 |
| Spectacular | 4 |

Accumulation is **localized** — it affects the immediate area where the spell was cast (a room, a street corner, a clearing). GM adjudicates boundaries.

### 5.2 Effect on Firearms

Each point of Magic Accumulation reduces effective Reliability by **3 percentage points**.

| Accumulation | Reliability Penalty | Revolver (95) | Tommy Gun (70) | Arc Gun (65) |
|-------------|--------------------|----|----|----|
| 0 | 0 | 95 | 70 | 65 |
| 2 (one Standard spell) | −6 | 89 | 64 | 59 |
| 5 (a couple spells) | −15 | 80 | 55 | 50 |
| 10 (sustained casting) | −30 | 65 | 40 | 35 |
| 15 (heavy combat magic) | −45 | 50 | 25 | 20 |
| 20 (magical storm) | −60 | 35 | 10 | 5 |
| 25+ (deep wild zone) | −75+ | 20 | — | — |
| 32+ | −96+ | — | — | — |

At effective Reliability 0 or below, the weapon **simply does not function**. No roll needed.

> **Design Note:** At 3% per point, a single caster throwing a couple of Standard spells (4 accumulation = −12%) is noticeable but not crippling. It takes sustained, heavy casting (10+ accumulation) to seriously threaten reliable firearms. This means casters are a *cost*, not a liability — the party feels the tension without being punished for bringing magic.

### 5.3 Decay Rate

Magic Accumulation decays at **1 point per minute** in normal areas.

This means:
- A single Weak spell (1 point) fades in a minute — barely noticed
- A Standard spell (2 points) lingers for 2 minutes — guns are slightly less reliable for a short scene
- A combat with 3-4 spells cast (8-12 points) leaves the area magically saturated for 8-12 minutes — guns are unreliable for the rest of the encounter and probably the next scene too
- A major magical event (20+ points) renders firearms useless for 20+ minutes

> **Persistent Magic Zones:** Wild Zones and Urban Bleed Zones have permanent base Accumulation (see §5.4). Spellcasting *adds* to this — they can get dangerously high.

> **Slow Decay Is A Feature:** The lingering residue is narratively significant. Magical forensics experts can track casters by their residue trails. A neighborhood where a Spectacular spell was cast an hour ago still reads as magically active. This has investigative, tactical, and worldbuilding implications.

### 5.4 Environmental Magic Zones

> **NOTE:** Full zone mechanics are deferred to a dedicated design session (see pending tasks). The framework below establishes how they interact with firearm Reliability.

Environmental zones have a **base Accumulation** that doesn't decay:

| Zone Type | Base Accumulation | Firearm Impact |
|-----------|------------------|----------------|
| Industrial Dead Zone | 0 (magic suppressed) | Firearms work perfectly. Spellcasting penalized instead. |
| Normal / In-Between | 0 | Firearms work unless spellcasting occurs |
| Light Magic Zone | 3–5 | Revolvers still fine, exotics getting sketchy |
| Moderate Magic Zone | 8–12 | Reliable firearms only. Exotics non-functional |
| Wild Zone | 15–20 | Only the most reliable firearms work, barely |
| Deep Wild Zone | 25+ | Firearms non-functional. Swords and sorcery only |

Spellcasting in a zone **adds to** the base, and the added accumulation decays normally. The base never changes (unless the zone itself shifts — another design topic).

### 5.5 Tech Accumulation — The Mirror Mechanic

Steampunk exotic weapons and devices generate **Tech Accumulation** — the technological counter-force pushing back against magic. This mirrors Magic Accumulation exactly (see DESIGN_PHILOSOPHY.md §1 for the cosmological reasoning).

**Only exotic/steampunk tech generates Tech Accumulation.** Conventional firearms do not. A revolver is just a machine — it doesn't push back against magic any more than a windmill does. Only the bleeding-edge technology that channels forces people don't fully understand generates counter-resonance.

| Exotic Action | Tech Accumulation Generated |
|---------------|---------------------------|
| Firing an exotic weapon | 1 per shot |
| Activating a major exotic device | 2–4 (GM discretion based on device) |
| Exotic tech sustained operation | 1 per minute |

**Effect on Spellcasting:** Each point of Tech Accumulation applies as a **−3 penalty** to the caster's roll (same 3-per-point rate, applied to the casting target number rather than a Reliability score). This makes misfire more likely and caps achievable tiers lower.

**Decay:** Tech Accumulation decays at 1 per minute, same as Magic Accumulation.

**Environmental Tech Zones:** Industrial Dead Zones have permanent base Tech Accumulation. Full zone rules deferred to the zone mechanics design session.

> **Design Note:** The asymmetry is intentional. Magic *always* erodes tech. Conventional tech *never* erodes magic. Only exotic tech erodes magic — it's the new paradigm pushing back. This means exotic weapons serve a dual purpose: they're weapons AND they're anti-magic field generators. Carrying them into a fight against casters has value beyond the damage they deal.

### 5.6 Tactical Implications

- **Party composition matters.** A caster makes your guns worse. You want them anyway — magic is powerful — but there's a cost. Smart parties carry sidearms AND swords.
- **Enemy analysis.** Opponents decked out in martial gear probably have a caster. Opponents with all firearms probably don't — and are vulnerable to magical assault.
- **Zone scouting.** Checking an area's magical residue before committing is smart tactics. Walking into a Wild Zone with only firearms is suicide.
- **Asymmetric warfare.** Cultists in a magically charged lair don't need guns. Factory district enforcers don't need magic. Adventurers operating in both worlds need versatility.
- **The last-spell problem.** Your caster dropping a Spectacular spell (4 accumulation) mid-firefight might win the moment but costs the party's firearms for the next 4 minutes. Timing matters.

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

> **Vehicle rules** are deferred to a separate session. Key principle: vehicles suffer from Magic Accumulation the same way firearms do, using a vehicle-level Reliability score.

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
6. **Magic Accumulation Exact Decay:** 1 per minute is the baseline. Should this vary by environment? (Faster in Dead Zones, slower in Wild Zones?)
7. **Malfunction Check Frequency:** Every shot? Every burst? Once per engagement at current accumulation? Every shot is grittier but more rolls.
