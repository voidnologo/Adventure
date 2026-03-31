"""
Core simulation engine for the Adventure RPG magic system.
Implements all casting mechanics from MAGIC_SYSTEM.md.
"""

import random
import math
from dataclasses import dataclass, field
from config import (
    TIER_MARGINS, HARD_CAPS, TIER_ORDER,
    WILD_BONUS, WILD_SUPPRESS,
    BACKLASH_SCHOLARLY, WILD_BACKLASH_EXTRA,
    BACKLASH_HP_DIE, WILD_EFFECT_CHANCE, WILD_EFFECT_DIE,
    WILD_EFFECT_BASE_DURATION, WILD_EFFECT_ESCALATED_DURATION,
    OVERFLOW_HP_RATIO, SPELL_COSTS,
)


def get_hard_cap(target: int) -> str:
    """Return maximum achievable tier for a given casting target."""
    for (lo, hi), cap in HARD_CAPS.items():
        if lo <= target <= hi:
            return cap
    return "spectacular"


def tier_index(tier: str) -> int:
    """Return numeric index for tier ordering."""
    return TIER_ORDER.index(tier)


def determine_tier(margin: int, target: int) -> str:
    """Given margin (target - roll) and target, determine achieved tier."""
    if margin <= 0:
        return "misfire"
    for threshold, tier_name in TIER_MARGINS:
        if margin >= threshold:
            raw = tier_name
            break
    else:
        raw = "weak"
    # Apply hard cap
    cap = get_hard_cap(target)
    cap_idx = tier_index(cap)
    raw_idx = tier_index(raw)
    if raw_idx > cap_idx:
        return cap
    return raw


def get_suppress_tiers(effective_target: int) -> int:
    """How many tiers a wild caster can suppress."""
    for (lo, hi), n in WILD_SUPPRESS.items():
        if lo <= effective_target <= hi:
            return n
    return 0


@dataclass
class WildEffectTracker:
    """Tracks active wild effects for escalation."""
    # effect_id -> {"stage": 1|2|3, "remaining": int}
    active: dict = field(default_factory=dict)
    # Counters
    base_count: int = 0
    escalated_count: int = 0
    permanent_count: int = 0

    def tick(self):
        """Decrease remaining duration on all active effects."""
        expired = []
        for eid, info in self.active.items():
            if info["stage"] < 3:  # permanents never expire
                info["remaining"] -= 1
                if info["remaining"] <= 0:
                    expired.append(eid)
        for eid in expired:
            del self.active[eid]

    def apply(self, effect_id: int) -> str:
        """Apply a wild effect. Returns 'base', 'escalated', or 'permanent'."""
        if effect_id in self.active:
            stage = self.active[effect_id]["stage"]
            if stage == 1:
                self.active[effect_id] = {"stage": 2, "remaining": WILD_EFFECT_ESCALATED_DURATION}
                self.escalated_count += 1
                return "escalated"
            elif stage == 2:
                self.active[effect_id] = {"stage": 3, "remaining": 999999}
                self.permanent_count += 1
                return "permanent"
            else:
                # Already permanent, no further escalation
                self.permanent_count += 1
                return "permanent"
        else:
            self.active[effect_id] = {"stage": 1, "remaining": WILD_EFFECT_BASE_DURATION}
            self.base_count += 1
            return "base"


@dataclass
class CastResult:
    spell_name: str
    complexity: int
    is_wild: bool
    roll: int           # effective d100 result
    margin: int         # target - roll
    raw_tier: str       # before suppression
    final_tier: str     # after suppression/choice
    tiers_suppressed: int
    exhaust_cost: int
    backlash: bool
    backlash_hp: int
    wild_effect: bool
    wild_effect_stage: str  # base/escalated/permanent or ""
    overflow: bool
    overflow_hp: int
    mp_before: int
    mp_after: int


def simulate_cast(
    spell_name: str,
    complexity: int,
    target: int,
    is_wild: bool,
    current_mp: int,
    wild_tracker: WildEffectTracker,
    rng: random.Random,
) -> CastResult:
    """Simulate a single spell cast. Returns CastResult."""

    effective_target = target + (WILD_BONUS if is_wild else 0)

    # Step 1: Roll
    if is_wild:
        r1 = rng.randint(1, 100)
        r2 = rng.randint(1, 100)
        # Take the roll farther from target
        d1 = abs(r1 - effective_target)
        d2 = abs(r2 - effective_target)
        roll = r1 if d1 >= d2 else r2
    else:
        roll = rng.randint(1, 100)

    margin = effective_target - roll

    # Step 2: Determine tier
    if margin <= 0:
        raw_tier = "misfire"
    else:
        raw_tier = determine_tier(margin, effective_target)

    # Step 3: Choose/suppress tier
    # Strategy: use the HIGHEST tier you can afford without overflowing MP.
    # If you can't afford even Weak, you still cast (overflow happens).
    tiers_suppressed = 0
    if raw_tier == "misfire":
        final_tier = "misfire"
    elif is_wild:
        max_suppress = get_suppress_tiers(effective_target)
        raw_idx = tier_index(raw_tier)
        # Try raw tier first, step down only if it would overflow
        best_tier = raw_tier
        suppress_used = 0
        for step in range(max_suppress + 1):
            candidate_idx = raw_idx - step
            if candidate_idx < 0:
                break
            candidate = TIER_ORDER[candidate_idx]
            cost = SPELL_COSTS[complexity][candidate]
            if cost <= current_mp:
                best_tier = candidate
                suppress_used = step
                break
            best_tier = candidate
            suppress_used = step
        # If nothing affordable, we're stuck at the lowest we can suppress to
        final_tier = best_tier
        tiers_suppressed = suppress_used
    else:
        # Scholarly: choose the highest tier they rolled that doesn't overflow.
        # They can freely pick any tier at or below their roll.
        raw_idx = tier_index(raw_tier)
        final_tier = raw_tier
        for idx in range(raw_idx, -1, -1):
            candidate = TIER_ORDER[idx]
            cost = SPELL_COSTS[complexity][candidate]
            if cost <= current_mp:
                final_tier = candidate
                break
            final_tier = candidate  # stuck at lowest if nothing affordable

    # Step 4: Apply costs
    costs = SPELL_COSTS[complexity]
    exhaust_cost = costs[final_tier]

    # Exhaustion overflow
    mp_before = current_mp
    overflow = False
    overflow_hp = 0
    if exhaust_cost > current_mp:
        overflow = True
        overflow_amount = exhaust_cost - current_mp
        overflow_hp = math.floor(overflow_amount * OVERFLOW_HP_RATIO)
        mp_after = 0
    else:
        mp_after = current_mp - exhaust_cost

    # Step 5: Backlash check
    backlash = False
    backlash_hp = 0
    wild_effect = False
    wild_effect_stage = ""

    if final_tier != "misfire":
        base_chance = BACKLASH_SCHOLARLY[final_tier]
        if is_wild:
            chance = base_chance + WILD_BACKLASH_EXTRA
        else:
            chance = base_chance
        if rng.random() < chance:
            backlash = True
            backlash_hp = rng.randint(1, BACKLASH_HP_DIE)
            # Wild effect check
            if rng.random() < WILD_EFFECT_CHANCE:
                wild_effect = True
                effect_id = rng.randint(1, WILD_EFFECT_DIE)
                wild_effect_stage = wild_tracker.apply(effect_id)

    # Tick wild effect durations
    wild_tracker.tick()

    return CastResult(
        spell_name=spell_name,
        complexity=complexity,
        is_wild=is_wild,
        roll=roll,
        margin=margin,
        raw_tier=raw_tier,
        final_tier=final_tier,
        tiers_suppressed=tiers_suppressed,
        exhaust_cost=exhaust_cost,
        backlash=backlash,
        backlash_hp=backlash_hp,
        wild_effect=wild_effect,
        wild_effect_stage=wild_effect_stage,
        overflow=overflow,
        overflow_hp=overflow_hp,
        mp_before=mp_before,
        mp_after=mp_after,
    )
