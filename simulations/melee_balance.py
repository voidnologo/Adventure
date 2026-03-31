"""
Melee Weapon Balance Analysis

Analyzes the current melee weapon table for balance issues.
Key metric: damage-per-timing-count (DPS equivalent on the timing track).
Also checks for strictly dominated weapons (same speed, less damage).
"""

# Current weapon table from PROJECT_SPEC.md
WEAPONS = {
    # Melee weapons
    "Battle Axe":       {"speed": 7, "damage": "1d10",   "avg": 5.5,  "type": "melee"},
    "Club":             {"speed": 4, "damage": "1d6",    "avg": 3.5,  "type": "melee"},
    "Dagger":           {"speed": 3, "damage": "1d4",    "avg": 2.5,  "type": "melee"},
    "Hand/Throwing Axe":{"speed": 4, "damage": "1d6",    "avg": 3.5,  "type": "melee"},
    "Knife":            {"speed": 3, "damage": "1d3",    "avg": 2.0,  "type": "melee"},
    "Mace":             {"speed": 7, "damage": "1d8+1",  "avg": 5.5,  "type": "melee"},
    "Morning Star":     {"speed": 7, "damage": "3d4",    "avg": 7.5,  "type": "melee"},
    "Polearm - Glaive": {"speed": 8, "damage": "1d10",   "avg": 5.5,  "type": "melee"},
    "Polearm - Halberd":{"speed": 9, "damage": "1d12",   "avg": 6.5,  "type": "melee"},
    "Quarterstaff":     {"speed": 4, "damage": "1d6",    "avg": 3.5,  "type": "melee"},
    "Spear":            {"speed": 6, "damage": "1d8",    "avg": 4.5,  "type": "melee"},
    "Sword - Bastard":  {"speed": 7, "damage": "1d8+1",  "avg": 5.5,  "type": "melee"},
    "Sword - Broad":    {"speed": 5, "damage": "2d4",    "avg": 5.0,  "type": "melee"},
    "Sword - Long":     {"speed": 5, "damage": "1d8",    "avg": 4.5,  "type": "melee"},
    "Sword - Short":    {"speed": 3, "damage": "1d6",    "avg": 3.5,  "type": "melee"},
    "Sword - Two Handed":{"speed": 8, "damage": "1d10+1","avg": 6.5,  "type": "melee"},
    "Trident":          {"speed": 7, "damage": "1d6+1",  "avg": 4.5,  "type": "melee"},
    "Warhammer":        {"speed": 5, "damage": "2d4+1",  "avg": 6.0,  "type": "melee"},
    "Whip":             {"speed": 8, "damage": "1d3",    "avg": 2.0,  "type": "utility"},
    "Punch (unarmed)":  {"speed": 2, "damage": "1d3+PP", "avg": 2.0,  "type": "unarmed"},
    "Kick (unarmed)":   {"speed": 3, "damage": "1d4+PP", "avg": 2.5,  "type": "unarmed"},
    # Ranged (non-firearm)
    "Blow Gun":         {"speed": 5, "damage": "1d2",    "avg": 1.5,  "type": "ranged-utility"},
    "Bow - Composite":  {"speed": 7, "damage": "1d8",    "avg": 4.5,  "type": "ranged"},
    "Bow - Long":       {"speed": 8, "damage": "1d10",   "avg": 5.5,  "type": "ranged"},
    "Crossbow - Hand":  {"speed": 6, "damage": "1d6",    "avg": 3.5,  "type": "ranged"},
    "Crossbow - Light": {"speed": 10,"damage": "2d8",    "avg": 9.0,  "type": "ranged"},
    "Crossbow - Heavy": {"speed": 12,"damage": "3d6",    "avg": 10.5, "type": "ranged"},
    "Sling":            {"speed": 6, "damage": "1d4+1",  "avg": 3.5,  "type": "ranged"},
}

# Firearms for comparison
FIREARMS = {
    "Derringer":        {"speed": 2, "damage": "1d6",    "avg": 3.5},
    "Revolver":         {"speed": 3, "damage": "2d6",    "avg": 7.0},
    "Semi-Auto Pistol": {"speed": 3, "damage": "2d6",    "avg": 7.0},
    "Heavy Revolver":   {"speed": 4, "damage": "2d8",    "avg": 9.0},
    "Bolt-Action Rifle":{"speed": 6, "damage": "2d10",   "avg": 11.0},
    "Lever-Action Rifle":{"speed": 5,"damage": "2d8",    "avg": 9.0},
    "Hunting Rifle":    {"speed": 7, "damage": "3d6",    "avg": 10.5},
    "Break-Action Shotgun":{"speed":4,"damage": "3d6",   "avg": 10.5},
    "Pump Shotgun":     {"speed": 5, "damage": "3d6",    "avg": 10.5},
    "Tommy Gun":        {"speed": 5, "damage": "3d6",    "avg": 10.5},
}


def analyze():
    print("=" * 80)
    print("MELEE WEAPON BALANCE ANALYSIS")
    print("=" * 80)

    # Calculate DPS (damage per timing count)
    print("\n## Damage Efficiency (Avg Damage / Speed) — sorted best to worst\n")
    print(f"{'Weapon':<22} {'Speed':>5} {'Damage':<10} {'Avg':>5} {'Eff':>6} {'Type':<15}")
    print("-" * 70)

    weapons_with_eff = []
    for name, w in WEAPONS.items():
        eff = w["avg"] / w["speed"]
        weapons_with_eff.append((name, w, eff))

    weapons_with_eff.sort(key=lambda x: -x[2])

    for name, w, eff in weapons_with_eff:
        print(f"{name:<22} {w['speed']:>5} {w['damage']:<10} {w['avg']:>5.1f} {eff:>6.2f} {w['type']:<15}")

    # Firearms comparison
    print(f"\n{'--- FIREARMS (for comparison) ---':^70}")
    print(f"{'Weapon':<22} {'Speed':>5} {'Damage':<10} {'Avg':>5} {'Eff':>6}")
    print("-" * 50)
    firearms_eff = []
    for name, w in FIREARMS.items():
        eff = w["avg"] / w["speed"]
        firearms_eff.append((name, w, eff))
    firearms_eff.sort(key=lambda x: -x[2])
    for name, w, eff in firearms_eff:
        print(f"{name:<22} {w['speed']:>5} {w['damage']:<10} {w['avg']:>5.1f} {eff:>6.2f}")

    # Find dominated weapons (same or higher speed, less damage than another weapon)
    print("\n\n## Strictly Dominated Weapons")
    print("(A weapon is dominated if another weapon has equal or better speed AND equal or better damage)\n")

    melee_only = {k: v for k, v in WEAPONS.items()
                  if v["type"] in ("melee", "ranged")}

    for name, w in melee_only.items():
        dominators = []
        for other_name, other_w in melee_only.items():
            if other_name == name:
                continue
            if (other_w["speed"] <= w["speed"] and
                other_w["avg"] >= w["avg"] and
                (other_w["speed"] < w["speed"] or other_w["avg"] > w["avg"])):
                dominators.append(other_name)
        if dominators:
            print(f"  ✗ {name} (Speed {w['speed']}, {w['damage']} avg {w['avg']:.1f})")
            for d in dominators:
                dw = melee_only[d]
                print(f"    → dominated by {d} (Speed {dw['speed']}, {dw['damage']} avg {dw['avg']:.1f})")

    # Group by speed tier
    print("\n\n## Speed Tier Analysis")
    print("(Weapons grouped by speed — within a tier, damage should increase with any tradeoff)\n")

    tiers = {}
    for name, w in WEAPONS.items():
        if w["type"] in ("utility", "unarmed", "ranged-utility"):
            continue
        s = w["speed"]
        if s not in tiers:
            tiers[s] = []
        tiers[s].append((name, w))

    for speed in sorted(tiers.keys()):
        weapons_at_speed = sorted(tiers[speed], key=lambda x: -x[1]["avg"])
        print(f"  Speed {speed}:")
        for name, w in weapons_at_speed:
            eff = w["avg"] / w["speed"]
            flag = ""
            if len(weapons_at_speed) > 1:
                best = weapons_at_speed[0][1]["avg"]
                worst = weapons_at_speed[-1][1]["avg"]
                if best - worst > 2.0 and w["avg"] == worst:
                    flag = " ← WEAK for tier"
                if w["avg"] == best and len(weapons_at_speed) > 1:
                    flag = " ← STRONG for tier"
            print(f"    {name:<22} {w['damage']:<10} avg {w['avg']:>5.1f}  eff {eff:.2f}{flag}")

    # Firearm vs melee ratio
    print("\n\n## Firearm vs Melee Damage Ratio (at comparable speeds)")
    print("(How much better are firearms than melee at similar timing costs?)\n")

    for speed in [3, 4, 5, 6, 7, 8]:
        melee_at_speed = [(n, w) for n, w in WEAPONS.items()
                         if w["speed"] == speed and w["type"] in ("melee", "ranged")]
        firearms_at_speed = [(n, w) for n, w in FIREARMS.items()
                            if w["speed"] == speed]
        if melee_at_speed and firearms_at_speed:
            best_melee = max(melee_at_speed, key=lambda x: x[1]["avg"])
            best_firearm = max(firearms_at_speed, key=lambda x: x[1]["avg"])
            ratio = best_firearm[1]["avg"] / best_melee[1]["avg"]
            print(f"  Speed {speed}: {best_firearm[0]} ({best_firearm[1]['avg']:.1f}) vs "
                  f"{best_melee[0]} ({best_melee[1]['avg']:.1f}) → {ratio:.1f}x")

    # Summary flags
    print("\n\n## Balance Flags\n")

    flags = []

    # Check for efficiency outliers (> 1 std dev from mean)
    melee_effs = [(n, w["avg"]/w["speed"]) for n, w in WEAPONS.items()
                  if w["type"] == "melee"]
    mean_eff = sum(e for _, e in melee_effs) / len(melee_effs)
    import statistics
    std_eff = statistics.stdev(e for _, e in melee_effs)

    for name, eff in melee_effs:
        if eff > mean_eff + std_eff:
            flags.append(f"HIGH EFFICIENCY: {name} (eff {eff:.2f}, mean {mean_eff:.2f} ± {std_eff:.2f})")
        if eff < mean_eff - std_eff:
            flags.append(f"LOW EFFICIENCY: {name} (eff {eff:.2f}, mean {mean_eff:.2f} ± {std_eff:.2f})")

    # Check for weapons with identical stats
    for name, w in WEAPONS.items():
        for other_name, other_w in WEAPONS.items():
            if name >= other_name:
                continue
            if w["speed"] == other_w["speed"] and w["avg"] == other_w["avg"] and w["type"] == other_w["type"]:
                flags.append(f"IDENTICAL: {name} and {other_name} (Speed {w['speed']}, avg {w['avg']:.1f})")

    for f in sorted(flags):
        print(f"  ⚑ {f}")


if __name__ == "__main__":
    analyze()
