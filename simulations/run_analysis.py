#!/usr/bin/env python3
"""
Magic System Balance Simulation
================================
Simulates realistic casters who want maximum power effects.
Core strategy: use highest affordable tier (don't overflow into HP damage).

Primary analysis: how many spells before exhaustion, tier distributions,
backlash/wild effect rates, and what happens when casters push past limits.

Usage:
    python run_analysis.py              # full analysis
    python run_analysis.py --quick      # fewer iterations
"""

import sys
import os
import random
import math
from collections import defaultdict
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (
    POWER_LEVELS, MP_BY_LEVEL, SPELLS, SPELL_COSTS,
    NUM_CHARACTERS_PER_CONFIG, RANDOM_SEED,
    TIER_ORDER, WILD_BONUS, BACKLASH_SCHOLARLY, WILD_BACKLASH_EXTRA,
)
from engine import simulate_cast, WildEffectTracker


def build_spell_mix():
    spells = []
    for name, info in SPELLS.items():
        spells.append((name, info["complexity"]))
    return spells

SPELL_MIX = build_spell_mix()

# Also build complexity-specific lists for focused analysis
SPELLS_BY_COMPLEXITY = defaultdict(list)
for name, info in SPELLS.items():
    SPELLS_BY_COMPLEXITY[info["complexity"]].append((name, info["complexity"]))


@dataclass
class SessionResult:
    """Result of one caster casting until they can't (or overflow)."""
    casts_before_empty: int = 0        # casts before MP hits 0
    casts_until_overflow: int = 0      # casts before first overflow event
    had_overflow: bool = False
    total_casts: int = 0               # total casts in session (including overflow cast)
    misfires: int = 0
    raw_tiers: dict = field(default_factory=lambda: defaultdict(int))
    final_tiers: dict = field(default_factory=lambda: defaultdict(int))
    backlash_count: int = 0
    backlash_hp_total: int = 0
    wild_effects: int = 0
    wild_base: int = 0
    wild_escalated: int = 0
    wild_permanent: int = 0
    overflow_hp: int = 0
    exhaust_total: int = 0
    suppress_events: int = 0
    suppress_tiers_total: int = 0
    mp_remaining: int = 0
    tier_by_complexity: dict = field(default_factory=lambda: defaultdict(lambda: defaultdict(int)))
    raw_tier_by_complexity: dict = field(default_factory=lambda: defaultdict(lambda: defaultdict(int)))
    misfire_by_complexity: dict = field(default_factory=lambda: defaultdict(int))


def run_until_exhausted(level, path, rng, spell_filter=None):
    """
    Cast spells until MP is exhausted. No resting.
    Returns SessionResult capturing everything that happened.
    """
    from config import POWER_LEVELS, MP_BY_LEVEL
    target = POWER_LEVELS[level]
    is_wild = (path == "wild")
    max_mp = MP_BY_LEVEL[level]
    current_mp = max_mp

    res = SessionResult(mp_remaining=max_mp)
    wild_tracker = WildEffectTracker()
    found_overflow = False
    mix = spell_filter if spell_filter else SPELL_MIX

    # Cast until MP is 0 (or would be 0 after next cast's minimum cost)
    while True:
        spell_name, complexity = rng.choice(mix)

        # Check if we can even cast the cheapest version (Weak tier cost)
        min_cost = SPELL_COSTS[complexity]["misfire"]  # misfire cost = weak tier cost
        # If MP is 0, stop — we're fully exhausted
        if current_mp <= 0:
            break

        result = simulate_cast(
            spell_name, complexity, target, is_wild,
            current_mp, wild_tracker, rng,
        )

        res.total_casts += 1

        # Track raw tier
        if result.raw_tier == "misfire":
            res.misfires += 1
            res.misfire_by_complexity[complexity] += 1
        else:
            res.raw_tiers[result.raw_tier] += 1
            res.raw_tier_by_complexity[complexity][result.raw_tier] += 1

        # Track final tier
        if result.final_tier != "misfire":
            res.final_tiers[result.final_tier] += 1
            res.tier_by_complexity[complexity][result.final_tier] += 1

        res.exhaust_total += result.exhaust_cost

        if result.backlash:
            res.backlash_count += 1
            res.backlash_hp_total += result.backlash_hp
        if result.wild_effect:
            res.wild_effects += 1
        if result.tiers_suppressed > 0:
            res.suppress_events += 1
            res.suppress_tiers_total += result.tiers_suppressed

        if result.overflow:
            if not found_overflow:
                res.casts_until_overflow = res.total_casts
                found_overflow = True
            res.had_overflow = True
            res.overflow_hp += result.overflow_hp
            current_mp = 0
        else:
            current_mp = result.mp_after

        # If overflow happened, the caster is done (MP = 0, incapacitated on exhaust track)
        if current_mp <= 0:
            res.casts_before_empty = res.total_casts
            break

    if not found_overflow:
        res.casts_until_overflow = res.total_casts  # never overflowed

    res.wild_permanent = wild_tracker.permanent_count
    res.wild_escalated = wild_tracker.escalated_count
    res.wild_base = wild_tracker.base_count
    res.mp_remaining = current_mp

    return res


def run_many_sessions(level, path, n_sessions, rng, spell_filter=None):
    """Run n_sessions and return list of SessionResults."""
    return [run_until_exhausted(level, path, rng, spell_filter) for _ in range(n_sessions)]


def pct(n, total):
    return 100.0 * n / total if total else 0.0


def avg(values):
    return sum(values) / len(values) if values else 0.0


def median(values):
    if not values:
        return 0
    s = sorted(values)
    n = len(s)
    if n % 2 == 0:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    return s[n // 2]


def format_report(all_results, complexity_results):
    lines = []
    W = 100

    lines.append("=" * W)
    lines.append("MAGIC SYSTEM BALANCE SIMULATION — POWER-MAXIMIZING STRATEGY")
    lines.append("=" * W)
    lines.append("")
    lines.append("Strategy: Casters use the HIGHEST tier they can afford without overflow.")
    lines.append("          Scholarly choose freely. Wild suppress only when forced by MP.")
    lines.append("          Each session = one caster casting until MP fully exhausted.")
    lines.append("")

    # ── 1. Casts Before Exhaustion ──────────────────────────────────
    lines.append("-" * W)
    lines.append("1. CASTS BEFORE EXHAUSTION (core sustainability metric)")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'MP Pool':>7} {'Avg Casts':>10} {'Median':>8} {'Min':>6} {'Max':>6} {'Overflow%':>10}")
    lines.append("-" * 75)
    for key in sorted(all_results.keys()):
        sessions = all_results[key]
        level, path = key
        mp = MP_BY_LEVEL[level]
        casts = [s.casts_before_empty for s in sessions]
        overflows = sum(1 for s in sessions if s.had_overflow)
        lines.append(
            f"{level}/{path:<20} {mp:>7} {avg(casts):>10.1f} "
            f"{median(casts):>8.0f} {min(casts):>6} {max(casts):>6} "
            f"{pct(overflows, len(sessions)):>9.1f}%"
        )
    lines.append("")
    lines.append("  'Overflow%' = sessions where the final cast overflowed into HP damage.")
    lines.append("  Higher = casters are regularly pushing past their limits.")
    lines.append("")

    # ── 2. Casts by Complexity ──────────────────────────────────────
    lines.append("-" * W)
    lines.append("2. CASTS BEFORE EXHAUSTION BY SPELL COMPLEXITY")
    lines.append("   (how many times can you cast ONLY spells of this complexity?)")
    lines.append("-" * W)
    for comp in [1, 2, 3, 4]:
        comp_data = complexity_results.get(comp, {})
        if not comp_data:
            continue
        cost_str = f"Weak={SPELL_COSTS[comp]['weak']}, Std={SPELL_COSTS[comp]['standard']}, Str={SPELL_COSTS[comp]['strong']}, Spec={SPELL_COSTS[comp]['spectacular']}"
        lines.append(f"\n  Complexity {comp} ({cost_str}):")
        lines.append(f"  {'Config':<25} {'Avg Casts':>10} {'Median':>8} {'Avg Tier':>10}")
        lines.append(f"  {'-'*58}")
        for key in sorted(comp_data.keys()):
            sessions = comp_data[key]
            casts = [s.casts_before_empty for s in sessions]
            # Weighted avg tier
            all_tiers = defaultdict(int)
            for s in sessions:
                for t, c in s.final_tiers.items():
                    all_tiers[t] += c
            total_success = sum(all_tiers.values())
            tier_weights = {"weak": 1, "standard": 2, "strong": 3, "spectacular": 4}
            avg_tier = sum(all_tiers.get(t, 0) * tw for t, tw in tier_weights.items()) / max(total_success, 1)
            lines.append(f"  {key[0]}/{key[1]:<20} {avg(casts):>10.1f} {median(casts):>8.0f} {avg_tier:>10.2f}")
    lines.append("")

    # ── 3. Misfire Rates ────────────────────────────────────────────
    lines.append("-" * W)
    lines.append("3. MISFIRE RATES")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'Total Casts':>12} {'Misfires':>10} {'Rate':>8}")
    lines.append("-" * 58)
    for key in sorted(all_results.keys()):
        sessions = all_results[key]
        total = sum(s.total_casts for s in sessions)
        misfires = sum(s.misfires for s in sessions)
        lines.append(f"{key[0]}/{key[1]:<20} {total:>12} {misfires:>10} {pct(misfires, total):>7.1f}%")
    lines.append("")

    # ── 4. Raw Tier Distributions ───────────────────────────────────
    lines.append("-" * W)
    lines.append("4. RAW TIER DISTRIBUTIONS (what the dice produce)")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'Weak':>8} {'Standard':>10} {'Strong':>10} {'Spectacular':>12}")
    lines.append("-" * 70)
    for key in sorted(all_results.keys()):
        sessions = all_results[key]
        raw = defaultdict(int)
        for s in sessions:
            for t, c in s.raw_tiers.items():
                raw[t] += c
        total_success = sum(raw.values())
        parts = [f"{pct(raw.get(t, 0), total_success):>7.1f}%" for t in TIER_ORDER]
        lines.append(f"{key[0]}/{key[1]:<20} {'  '.join(parts)}")
    lines.append("")

    # ── 5. Final Tier Distributions ─────────────────────────────────
    lines.append("-" * W)
    lines.append("5. FINAL TIER DISTRIBUTIONS (after choice/suppression)")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'Weak':>8} {'Standard':>10} {'Strong':>10} {'Spectacular':>12}")
    lines.append("-" * 70)
    for key in sorted(all_results.keys()):
        sessions = all_results[key]
        final = defaultdict(int)
        for s in sessions:
            for t, c in s.final_tiers.items():
                final[t] += c
        total_success = sum(final.values())
        parts = [f"{pct(final.get(t, 0), total_success):>7.1f}%" for t in TIER_ORDER]
        lines.append(f"{key[0]}/{key[1]:<20} {'  '.join(parts)}")
    lines.append("")

    # ── 6. Backlash & Wild Effects ──────────────────────────────────
    lines.append("-" * W)
    lines.append("6. BACKLASH & WILD EFFECTS (per session = one caster's full MP pool)")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'Backlash/Ses':>13} {'BL HP/Ses':>10} {'WildFx/Ses':>11} {'Esc':>5} {'PERM':>6}")
    lines.append("-" * 75)
    for key in sorted(all_results.keys()):
        sessions = all_results[key]
        n = len(sessions)
        bl = sum(s.backlash_count for s in sessions)
        bl_hp = sum(s.backlash_hp_total for s in sessions)
        wfx = sum(s.wild_effects for s in sessions)
        esc = sum(s.wild_escalated for s in sessions)
        perm = sum(s.wild_permanent for s in sessions)
        lines.append(
            f"{key[0]}/{key[1]:<20} {bl/n:>13.2f} {bl_hp/n:>10.1f} "
            f"{wfx/n:>11.2f} {esc:>5} {perm:>6}"
        )
    lines.append("")
    lines.append("  Backlash/Ses = avg backlash events per session (one full MP drain)")
    lines.append("  PERM = total permanent wild effects across ALL sessions")
    lines.append("")

    # ── 7. Exhaustion Overflow Detail ───────────────────────────────
    lines.append("-" * W)
    lines.append("7. EXHAUSTION OVERFLOW DETAIL")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'Sessions':>8} {'Overflow%':>10} {'AvgOvHP':>8} {'MaxOvHP':>8}")
    lines.append("-" * 64)
    for key in sorted(all_results.keys()):
        sessions = all_results[key]
        n = len(sessions)
        ov_sessions = [s for s in sessions if s.had_overflow]
        ov_hps = [s.overflow_hp for s in ov_sessions] if ov_sessions else [0]
        lines.append(
            f"{key[0]}/{key[1]:<20} {n:>8} "
            f"{pct(len(ov_sessions), n):>9.1f}% "
            f"{avg(ov_hps):>7.1f} "
            f"{max(ov_hps):>8}"
        )
    lines.append("")

    # ── 8. Wild Caster Suppression ──────────────────────────────────
    lines.append("-" * W)
    lines.append("8. WILD CASTER TIER SUPPRESSION")
    lines.append("-" * W)
    lines.append(f"{'Config':<25} {'Supp Events':>12} {'Supp%':>8} {'AvgTiers':>10} {'ForcedHigh%':>12}")
    lines.append("-" * 72)
    for key in sorted(all_results.keys()):
        if key[1] != "wild":
            continue
        sessions = all_results[key]
        total_success = sum(sum(s.final_tiers.values()) for s in sessions)
        supp = sum(s.suppress_events for s in sessions)
        supp_tiers = sum(s.suppress_tiers_total for s in sessions)
        # "Forced high" = times they wanted to suppress more but couldn't
        # (final tier > weak AND they used all their suppress capacity)
        # Approximate: any time final tier != weak and suppress was used
        forced = 0
        for s in sessions:
            for t in ("standard", "strong", "spectacular"):
                forced += s.final_tiers.get(t, 0)
        lines.append(
            f"{key[0]}/{key[1]:<20} {supp:>12} "
            f"{pct(supp, total_success):>7.1f}% "
            f"{supp_tiers / max(supp, 1):>9.2f} "
            f"{pct(forced, total_success):>11.1f}%"
        )
    lines.append("")
    lines.append("  ForcedHigh% = % of successful casts where wild caster ended above Weak")
    lines.append("  (either by choice because they could afford it, or forced because suppression limit)")
    lines.append("")

    # ── 9. Head-to-Head ─────────────────────────────────────────────
    lines.append("-" * W)
    lines.append("9. SCHOLARLY vs WILD HEAD-TO-HEAD")
    lines.append("-" * W)
    for level in POWER_LEVELS:
        s_sessions = all_results.get((level, "scholarly"), [])
        w_sessions = all_results.get((level, "wild"), [])
        if not s_sessions or not w_sessions:
            continue

        s_casts = [s.casts_before_empty for s in s_sessions]
        w_casts = [s.casts_before_empty for s in w_sessions]

        s_total = sum(s.total_casts for s in s_sessions)
        w_total = sum(s.total_casts for s in w_sessions)
        s_mf = sum(s.misfires for s in s_sessions)
        w_mf = sum(s.misfires for s in w_sessions)
        s_suc = s_total - s_mf
        w_suc = w_total - w_mf

        s_raw = defaultdict(int)
        w_raw = defaultdict(int)
        s_final = defaultdict(int)
        w_final = defaultdict(int)
        for s in s_sessions:
            for t, c in s.raw_tiers.items(): s_raw[t] += c
            for t, c in s.final_tiers.items(): s_final[t] += c
        for s in w_sessions:
            for t, c in s.raw_tiers.items(): w_raw[t] += c
            for t, c in s.final_tiers.items(): w_final[t] += c

        tier_w = {"weak": 1, "standard": 2, "strong": 3, "spectacular": 4}
        s_avg_raw = sum(s_raw.get(t, 0) * tw for t, tw in tier_w.items()) / max(s_suc, 1)
        w_avg_raw = sum(w_raw.get(t, 0) * tw for t, tw in tier_w.items()) / max(w_suc, 1)
        s_avg_final = sum(s_final.get(t, 0) * tw for t, tw in tier_w.items()) / max(s_suc, 1)
        w_avg_final = sum(w_final.get(t, 0) * tw for t, tw in tier_w.items()) / max(w_suc, 1)

        s_bl = sum(s.backlash_count for s in s_sessions)
        w_bl = sum(s.backlash_count for s in w_sessions)
        s_bl_hp = sum(s.backlash_hp_total for s in s_sessions)
        w_bl_hp = sum(s.backlash_hp_total for s in w_sessions)

        lines.append(f"\n  === {level.upper()} (scholarly target {POWER_LEVELS[level]}, wild effective {POWER_LEVELS[level]+WILD_BONUS}) ===")
        lines.append(f"  {'Metric':<35} {'Scholarly':>12} {'Wild':>12} {'Delta':>12}")
        lines.append(f"  {'-'*73}")

        def row(name, sv, wv, fmt=".1f", unit="%"):
            delta = wv - sv
            sign = "+" if delta >= 0 else ""
            if unit == "%":
                lines.append(f"  {name:<35} {sv:>11{fmt}}% {wv:>11{fmt}}% {sign}{delta:>10{fmt}}%")
            elif unit == "n":
                lines.append(f"  {name:<35} {sv:>12{fmt}} {wv:>12{fmt}} {sign}{delta:>11{fmt}}")
            else:
                lines.append(f"  {name:<35} {sv:>12{fmt}} {wv:>12{fmt}} {sign}{delta:>11{fmt}}")

        row("Casts before exhaustion (avg)", avg(s_casts), avg(w_casts), ".1f", "")
        row("Casts before exhaustion (med)", median(s_casts), median(w_casts), ".0f", "")
        row("Success rate", pct(s_suc, s_total), pct(w_suc, w_total))
        row("Avg raw tier (1-4)", s_avg_raw, w_avg_raw, ".2f", "")
        row("Avg final tier (1-4)", s_avg_final, w_avg_final, ".2f", "")
        row("Spectacular (raw) %", pct(s_raw.get("spectacular", 0), s_suc), pct(w_raw.get("spectacular", 0), w_suc))
        row("Spectacular (final) %", pct(s_final.get("spectacular", 0), s_suc), pct(w_final.get("spectacular", 0), w_suc))
        row("Backlash rate", pct(s_bl, s_suc), pct(w_bl, w_suc))
        row("Backlash HP / session", s_bl_hp / len(s_sessions), w_bl_hp / len(w_sessions), ".1f", "")

    lines.append("")

    # ── 10. Balance Flags ───────────────────────────────────────────
    lines.append("-" * W)
    lines.append("10. AUTOMATED BALANCE FLAGS")
    lines.append("-" * W)
    flags = generate_flags(all_results)
    for flag in flags:
        lines.append(f"  {flag}")
    if not flags:
        lines.append("  No balance flags triggered.")
    lines.append("")
    lines.append("=" * W)
    lines.append("END OF REPORT")
    lines.append("=" * W)
    return "\n".join(lines)


def generate_flags(all_results):
    flags = []
    for level in POWER_LEVELS:
        s_sessions = all_results.get((level, "scholarly"), [])
        w_sessions = all_results.get((level, "wild"), [])
        if not s_sessions or not w_sessions:
            continue

        s_casts = avg([s.casts_before_empty for s in s_sessions])
        w_casts = avg([s.casts_before_empty for s in w_sessions])

        s_total = sum(s.total_casts for s in s_sessions)
        w_total = sum(s.total_casts for s in w_sessions)
        s_mf = pct(sum(s.misfires for s in s_sessions), s_total)
        w_mf = pct(sum(s.misfires for s in w_sessions), w_total)
        s_suc = s_total - sum(s.misfires for s in s_sessions)
        w_suc = w_total - sum(s.misfires for s in w_sessions)

        # Cast count divergence
        if w_casts > s_casts * 1.5:
            flags.append(f"[{level}] SUSTAINABILITY GAP: Wild gets {w_casts:.0f} casts vs scholarly {s_casts:.0f} — wild lasts {w_casts/s_casts:.1f}x longer")
        if s_casts > w_casts * 1.5:
            flags.append(f"[{level}] SUSTAINABILITY GAP: Scholarly gets {s_casts:.0f} casts vs wild {w_casts:.0f}")

        # Misfire gap
        if s_mf > 10 and w_mf < s_mf * 0.5:
            flags.append(f"[{level}] MISFIRE GAP: Wild {w_mf:.1f}% vs scholarly {s_mf:.1f}%")

        # Wild spectacular dominance
        w_raw = defaultdict(int)
        for s in w_sessions:
            for t, c in s.raw_tiers.items(): w_raw[t] += c
        w_spec = pct(w_raw.get("spectacular", 0), w_suc)
        s_raw = defaultdict(int)
        for s in s_sessions:
            for t, c in s.raw_tiers.items(): s_raw[t] += c
        s_spec = pct(s_raw.get("spectacular", 0), s_suc)
        if w_spec > 40:
            flags.append(f"[{level}] WILD SPECTACULAR: {w_spec:.1f}% of wild successes are Spectacular (scholarly: {s_spec:.1f}%)")

        # Wild casters stuck paying high costs
        w_final = defaultdict(int)
        for s in w_sessions:
            for t, c in s.final_tiers.items(): w_final[t] += c
        total_w_final = sum(w_final.values())
        forced_high = sum(w_final.get(t, 0) for t in ("strong", "spectacular"))
        if pct(forced_high, total_w_final) > 20:
            flags.append(f"[{level}] WILD COST PRESSURE: {pct(forced_high, total_w_final):.1f}% of wild casts land at Strong/Spectacular — high exhaust drain")

        # Very few casts at low level
        if s_casts < 4 or w_casts < 4:
            flags.append(f"[{level}] LOW SUSTAINABILITY: {'Scholarly' if s_casts < 4 else 'Wild'} only gets {min(s_casts, w_casts):.1f} avg casts per pool")

        # Permanent wild effects
        perms = sum(s.wild_permanent for s in s_sessions) + sum(s.wild_permanent for s in w_sessions)
        if perms > 3:
            flags.append(f"[{level}] WILD PERMANENTS: {perms} permanent effects across all sessions")

    return flags


def main():
    quick = "--quick" in sys.argv
    n_sessions = 20 if quick else NUM_CHARACTERS_PER_CONFIG * 10  # 500 sessions per config

    print(f"{'Quick' if quick else 'Full'} mode: {n_sessions} sessions per config")
    print(f"Each session = one caster casting until MP exhausted\n")

    rng = random.Random(RANDOM_SEED)

    # ── Main analysis: mixed spell selection ────────────────────────
    all_results = {}
    configs = [(l, p) for l in POWER_LEVELS for p in ("scholarly", "wild")]
    total = len(configs)

    for i, (level, path) in enumerate(configs, 1):
        sessions = run_many_sessions(level, path, n_sessions, rng)
        all_results[(level, path)] = sessions
        avg_c = avg([s.casts_before_empty for s in sessions])
        print(f"  [{i}/{total}] {level}/{path}: avg {avg_c:.1f} casts before exhaustion")

    # ── Complexity-specific analysis ────────────────────────────────
    print("\n  Running complexity-specific sessions...")
    complexity_results = {}
    for comp in [1, 2, 3, 4]:
        complexity_results[comp] = {}
        spell_list = SPELLS_BY_COMPLEXITY[comp]
        for level, path in configs:
            sessions = run_many_sessions(level, path, n_sessions // 2, rng, spell_filter=spell_list)
            complexity_results[comp][(level, path)] = sessions

    report = format_report(all_results, complexity_results)
    print("\n" + report)

    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "balance_report.txt")
    with open(outpath, "w") as f:
        f.write(report)
    print(f"\nReport saved to {outpath}")


if __name__ == "__main__":
    main()
