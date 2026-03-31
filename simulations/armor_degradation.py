"""
Armor degradation analysis.

Current rule: If damage > soak, overflow / 2 (round down) = number of 25% degradation checks.
On each failed check, soak permanently drops by the overflow amount.

Question: Does armor fall apart too fast?
"""
import random
import statistics

def simulate_combat_degradation(
    armor_soak: int,
    damage_dice: str,  # e.g. "1d8+1", "2d6", "1d6"
    num_hits: int,
    overflow_divisor: int = 2,
    degrade_chance: float = 0.25,
    degrade_amount: str = "overflow",  # "overflow" or "1"
    trials: int = 50000,
):
    """Simulate armor degradation over a number of hits."""

    def roll_damage(dice_str):
        # Parse simple dice notation
        parts = dice_str.replace(" ", "")
        bonus = 0
        if "+" in parts:
            dice_part, bonus_str = parts.split("+")
            bonus = int(bonus_str)
        elif "-" in parts and "d" in parts.split("-")[0]:
            dice_part, bonus_str = parts.rsplit("-", 1)
            bonus = -int(bonus_str)
        else:
            dice_part = parts

        num, sides = dice_part.split("d")
        num = int(num)
        sides = int(sides)

        total = sum(random.randint(1, sides) for _ in range(num)) + bonus
        return max(1, total)

    results = {
        "final_soak": [],
        "hits_to_first_degrade": [],
        "total_degrades": [],
        "soak_lost": [],
    }

    for _ in range(trials):
        current_soak = armor_soak
        degrades = 0
        first_degrade_hit = None

        for hit_num in range(1, num_hits + 1):
            dmg = roll_damage(damage_dice)
            overflow = dmg - current_soak

            if overflow > 0:
                if overflow_divisor > 0:
                    checks = overflow // overflow_divisor
                    if checks == 0:
                        checks = 1  # At least 1 check if any overflow
                else:
                    checks = overflow  # 1:1 ratio

                for _ in range(checks):
                    if random.random() < degrade_chance:
                        if degrade_amount == "overflow":
                            current_soak = max(0, current_soak - overflow)
                        elif degrade_amount == "1":
                            current_soak = max(0, current_soak - 1)
                        degrades += 1
                        if first_degrade_hit is None:
                            first_degrade_hit = hit_num
                        break  # Only degrade once per hit

            if current_soak <= 0:
                break

        results["final_soak"].append(current_soak)
        results["hits_to_first_degrade"].append(first_degrade_hit if first_degrade_hit else num_hits + 1)
        results["total_degrades"].append(degrades)
        results["soak_lost"].append(armor_soak - current_soak)

    return results


def print_report(label, armor, damage, hits, results):
    final = results["final_soak"]
    first_deg = [x for x in results["hits_to_first_degrade"] if x <= hits]

    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  Armor: Soak {armor} | Weapon: {damage} | Over {hits} hits")
    print(f"{'='*60}")
    print(f"  Avg final soak:       {statistics.mean(final):.1f} / {armor}")
    print(f"  Soak at 0 (destroyed): {sum(1 for s in final if s == 0) / len(final) * 100:.1f}%")
    print(f"  Soak unchanged:       {sum(1 for s in final if s == armor) / len(final) * 100:.1f}%")
    print(f"  Avg soak lost:        {statistics.mean(results['soak_lost']):.1f}")
    if first_deg:
        print(f"  Avg hits to 1st deg:  {statistics.mean(first_deg):.1f}")
        print(f"  Ever degraded:        {len(first_deg) / len(final) * 100:.1f}%")
    else:
        print(f"  Ever degraded:        0%")


# ================================================================
# CURRENT RULES: overflow / 2, 25% chance, lose full overflow
# ================================================================
print("\n" + "=" * 60)
print("  CURRENT RULES: overflow ÷ 2 checks, 25% chance, lose overflow")
print("=" * 60)

scenarios = [
    ("Leather (2) vs Small melee (1d4)", 2, "1d4", 10),
    ("Leather (2) vs Light melee (1d6)", 2, "1d6", 10),
    ("Chainmail (5) vs Light melee (1d6)", 5, "1d6", 10),
    ("Chainmail (5) vs Medium melee (1d8+1)", 5, "1d8+1", 10),
    ("Chainmail (5) vs Revolver (2d6)", 5, "2d6", 10),
    ("Chainmail (5) vs Rifle (2d10)", 5, "2d10", 10),
    ("Half Plate (8) vs Medium melee (1d8+1)", 8, "1d8+1", 10),
    ("Half Plate (8) vs Revolver (2d6)", 8, "2d6", 10),
    ("Half Plate (8) vs Rifle (2d10)", 8, "2d10", 10),
    ("Full Plate (12) vs Heavy melee (1d10+1)", 12, "1d10+1", 10),
    ("Full Plate (12) vs Rifle (2d10)", 12, "2d10", 10),
]

for label, armor, damage, hits in scenarios:
    results = simulate_combat_degradation(armor, damage, hits, overflow_divisor=2, degrade_chance=0.25, degrade_amount="overflow")
    print_report(label, armor, damage, hits, results)

# ================================================================
# ALTERNATIVE 1: overflow / 2, 25% chance, lose only 1 soak
# ================================================================
print("\n\n" + "=" * 60)
print("  ALT 1: overflow ÷ 2 checks, 25% chance, lose only 1 soak")
print("=" * 60)

for label, armor, damage, hits in scenarios:
    results = simulate_combat_degradation(armor, damage, hits, overflow_divisor=2, degrade_chance=0.25, degrade_amount="1")
    print_report(f"[ALT1] {label}", armor, damage, hits, results)

# ================================================================
# ALTERNATIVE 2: overflow / 3, 25% chance, lose full overflow
# ================================================================
print("\n\n" + "=" * 60)
print("  ALT 2: overflow ÷ 3 checks, 25% chance, lose overflow")
print("=" * 60)

for label, armor, damage, hits in scenarios:
    results = simulate_combat_degradation(armor, damage, hits, overflow_divisor=3, degrade_chance=0.25, degrade_amount="overflow")
    print_report(f"[ALT2] {label}", armor, damage, hits, results)

# ================================================================
# ALTERNATIVE 3: flat 1 check per overflow event, 25%, lose 1
# ================================================================
print("\n\n" + "=" * 60)
print("  ALT 3: 1 flat check per overflow event, 25%, lose 1 soak")
print("=" * 60)

for label, armor, damage, hits in scenarios:
    results = simulate_combat_degradation(armor, damage, hits, overflow_divisor=999, degrade_chance=0.25, degrade_amount="1")
    print_report(f"[ALT3] {label}", armor, damage, hits, results)

# ================================================================
# ALTERNATIVE 4: 1 flat check per overflow event, 10%, lose 1
# ================================================================
print("\n\n" + "=" * 60)
print("  ALT 4: 1 flat check per overflow event, 10%, lose 1 soak")
print("=" * 60)

for label, armor, damage, hits in scenarios:
    results = simulate_combat_degradation(armor, damage, hits, overflow_divisor=999, degrade_chance=0.10, degrade_amount="1")
    print_report(f"[ALT4] {label}", armor, damage, hits, results)
