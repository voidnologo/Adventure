"""
Weapon Rebalance Analysis

Compares old individual-weapon table to proposed category-based system.
Tests damage vs armor soak to validate that heavier weapons have a real niche.
"""

import random
import statistics


# ─── PROPOSED CATEGORY SYSTEM ───

MELEE_CATEGORIES = {
    "Unarmed":  {"speed": 2, "damage": "1d3+PP", "avg": 2.0, "avg_pp1": 3.0},
    "Small":    {"speed": 2, "damage": "1d4",     "avg": 2.5},
    "Light":    {"speed": 3, "damage": "1d6",     "avg": 3.5},
    "Medium":   {"speed": 5, "damage": "1d8+1",   "avg": 5.5},
    "Heavy":    {"speed": 7, "damage": "1d10+1",  "avg": 6.5},
    "Great":    {"speed": 9, "damage": "2d6",     "avg": 7.0},
}

RANGED_CATEGORIES = {
    "Light Ranged":     {"speed": 5, "damage": "1d6",    "avg": 3.5},
    "Medium Ranged":    {"speed": 7, "damage": "1d8+1",  "avg": 5.5, "notes": "Bows"},
    "Light Crossbow":   {"speed": 7, "damage": "2d6",    "avg": 7.0, "reload": 6},
    "Heavy Crossbow":   {"speed": 10,"damage": "3d6",    "avg": 10.5, "reload": 10},
}

FIREARM_CATEGORIES = {
    "Derringer":          {"speed": 2, "damage": "1d6",  "avg": 3.5},
    "Revolver":           {"speed": 3, "damage": "2d6",  "avg": 7.0},
    "Semi-Auto Pistol":   {"speed": 3, "damage": "2d6",  "avg": 7.0},
    "Heavy Revolver":     {"speed": 4, "damage": "2d8",  "avg": 9.0},
    "Lever-Action Rifle": {"speed": 5, "damage": "2d8",  "avg": 9.0},
    "Bolt-Action Rifle":  {"speed": 6, "damage": "2d10", "avg": 11.0},
    "Break-Action Shotgun":{"speed":4, "damage": "3d6",  "avg": 10.5},
    "Pump Shotgun":       {"speed": 5, "damage": "3d6",  "avg": 10.5},
    "Hunting Rifle":      {"speed": 7, "damage": "3d6",  "avg": 10.5},
    "Tommy Gun":          {"speed": 5, "damage": "3d6",  "avg": 10.5},
}


def roll_damage(damage_str, pp=0):
    """Parse and roll a damage string like '2d6+1' or '1d3+PP'."""
    damage_str = damage_str.replace("PP", str(pp))
    total = 0
    parts = damage_str.replace("-", "+-").split("+")
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if "d" in part:
            count, sides = part.split("d")
            count = int(count) if count else 1
            sides = int(sides)
            for _ in range(count):
                total += random.randint(1, sides)
        else:
            total += int(part)
    return max(0, total)


def simulate_damage_vs_armor(categories, soak_values, trials=10000):
    """Simulate average damage after soak for each category at each armor level."""
    results = {}
    for name, cat in categories.items():
        results[name] = {}
        for soak in soak_values:
            damage_after = []
            for _ in range(trials):
                raw = roll_damage(cat["damage"])
                after = max(0, raw - soak)
                damage_after.append(after)
            avg_after = statistics.mean(damage_after)
            hit_rate = sum(1 for d in damage_after if d > 0) / len(damage_after) * 100
            results[name][soak] = (avg_after, hit_rate)
    return results


def analyze():
    print("=" * 85)
    print("WEAPON CATEGORY REBALANCE ANALYSIS")
    print("=" * 85)

    # ─── Efficiency comparison ───
    print("\n## Proposed Melee Categories — Efficiency\n")
    print(f"{'Category':<16} {'Speed':>5} {'Damage':<10} {'Avg':>5} {'Eff':>6}")
    print("-" * 50)
    for name, cat in MELEE_CATEGORIES.items():
        eff = cat["avg"] / cat["speed"]
        print(f"{name:<16} {cat['speed']:>5} {cat['damage']:<10} {cat['avg']:>5.1f} {eff:>6.2f}")

    print(f"\n{'--- Ranged (Martial) ---':^50}")
    print(f"{'Category':<16} {'Speed':>5} {'Damage':<10} {'Avg':>5} {'Eff':>6} {'Reload':>7}")
    print("-" * 55)
    for name, cat in RANGED_CATEGORIES.items():
        eff = cat["avg"] / cat["speed"]
        reload = cat.get("reload", "—")
        print(f"{name:<16} {cat['speed']:>5} {cat['damage']:<10} {cat['avg']:>5.1f} {eff:>6.2f} {str(reload):>7}")

    print(f"\n{'--- Firearms ---':^50}")
    print(f"{'Category':<22} {'Speed':>5} {'Damage':<10} {'Avg':>5} {'Eff':>6}")
    print("-" * 50)
    for name, cat in FIREARM_CATEGORIES.items():
        eff = cat["avg"] / cat["speed"]
        print(f"{name:<22} {cat['speed']:>5} {cat['damage']:<10} {cat['avg']:>5.1f} {eff:>6.2f}")

    # ─── Damage vs Armor ───
    soak_values = [0, 2, 5, 8, 12]
    print("\n\n## Damage vs Armor Soak (10,000 trials per cell)")
    print("Shows: avg damage after soak (% of hits that penetrate)\n")

    all_weapons = {}
    all_weapons.update(MELEE_CATEGORIES)
    all_weapons.update({"Revolver": FIREARM_CATEGORIES["Revolver"]})
    all_weapons.update({"Bolt Rifle": FIREARM_CATEGORIES["Bolt-Action Rifle"]})

    # Remove unarmed for clarity
    test_weapons = {k: v for k, v in all_weapons.items() if k != "Unarmed"}
    results = simulate_damage_vs_armor(test_weapons, soak_values)

    header = f"{'Weapon':<14}"
    for soak in soak_values:
        header += f" {'Soak '+str(soak):>16}"
    print(header)
    print("-" * (14 + 17 * len(soak_values)))

    for name in test_weapons:
        row = f"{name:<14}"
        for soak in soak_values:
            avg_after, hit_rate = results[name][soak]
            row += f"  {avg_after:>4.1f} ({hit_rate:>4.0f}%hit)"
        print(row)

    # ─── DPS vs Armor (damage per timing count after soak) ───
    print("\n\n## Effective DPS vs Armor (avg damage after soak / speed)")
    print("This is the real metric — damage output per unit of timing track\n")

    header = f"{'Weapon':<14} {'Spd':>3}"
    for soak in soak_values:
        header += f" {'Soak '+str(soak):>10}"
    print(header)
    print("-" * (18 + 11 * len(soak_values)))

    for name, cat in test_weapons.items():
        row = f"{name:<14} {cat['speed']:>3}"
        for soak in soak_values:
            avg_after, _ = results[name][soak]
            dps = avg_after / cat["speed"]
            row += f" {dps:>10.2f}"
        print(row)

    # ─── Kill time analysis ───
    print("\n\n## Rounds to Kill (avg hits needed to deal 25 HP after soak)")
    print("Assumes no crits, no wound penalties applied to attacker\n")

    target_hp = 25
    header = f"{'Weapon':<14} {'Spd':>3}"
    for soak in soak_values:
        header += f" {'Soak '+str(soak):>10}"
    print(header)
    print("-" * (18 + 11 * len(soak_values)))

    for name, cat in test_weapons.items():
        row = f"{name:<14} {cat['speed']:>3}"
        for soak in soak_values:
            avg_after, _ = results[name][soak]
            if avg_after > 0:
                hits = target_hp / avg_after
                timing = hits * cat["speed"]
                row += f" {hits:>4.1f} ({timing:>3.0f}t)"
            else:
                row += f"      never"
        print(row)

    print("\n\n## Key Takeaways\n")
    print("1. Efficiency (raw DPS) favors lighter weapons against unarmored targets.")
    print("2. Against armor, heavy/great weapons shine because more of their damage")
    print("   penetrates soak. This is the natural balancing mechanic.")
    print("3. Firearms outclass all melee at every armor level — the tradeoff is")
    print("   Reliability/magic interference, not raw damage.")
    print("4. Light crossbows and heavy crossbows are the 'martial ranged' bridge —")
    print("   approaching firearm damage but magic-immune.")


if __name__ == "__main__":
    random.seed(42)
    analyze()
