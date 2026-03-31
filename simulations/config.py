"""
Tweakable parameters for magic system simulation.
Edit values here and re-run to compare balance changes.
"""

# ── Character Power Levels ──────────────────────────────────────────
# Casting target numbers (PW-based) for each tier of caster.
# Wild casters get +10 added automatically.
POWER_LEVELS = {
    "low":    30,
    "mid":    45,
    "high":   60,
    "master": 75,
}

# MP = 7 + PW.  PW here approximates the casting target.
# (In the actual game PW is a stat, target derives from it.
#  For simulation purposes we treat them as roughly equal.)
MP_BY_LEVEL = {
    "low":    37,   # 7 + 30
    "mid":    52,   # 7 + 45
    "high":   67,   # 7 + 60
    "master": 82,   # 7 + 75
}

# ── Tier Thresholds (margin under target) ───────────────────────────
# Over target = Misfire.  These are inclusive lower bounds of margin.
TIER_MARGINS = [
    (51, "spectacular"),
    (31, "strong"),
    (11, "standard"),
    ( 1, "weak"),
    # anything <= 0 is misfire
]

# Hard cap: maximum tier reachable given casting target
# target <= 30 => max standard, 31-50 => max strong, 51+ => spectacular
HARD_CAPS = {
    (0, 30):   "standard",
    (31, 50):  "strong",
    (51, 100): "spectacular",
}

TIER_ORDER = ["weak", "standard", "strong", "spectacular"]

# ── Wild Caster ─────────────────────────────────────────────────────
WILD_BONUS = 10  # flat bonus to casting target

# Tier suppression brackets (based on EFFECTIVE target including bonus)
# Capped at 2 max — you can only squash the magic so much.
WILD_SUPPRESS = {
    (1,  25): 0,
    (26, 50): 1,
    (51, 75): 2,
    (76, 999): 2,
}

# ── Backlash ────────────────────────────────────────────────────────
# Chance of backlash per tier used
BACKLASH_SCHOLARLY = {
    "weak":        0.05,
    "standard":    0.10,
    "strong":      0.15,
    "spectacular": 0.25,
}

# Wild modifier: +5% flat per tier (TBD in rules, this is default guess)
WILD_BACKLASH_EXTRA = 0.05

BACKLASH_HP_DIE = 4       # 1d4 physical damage on backlash
WILD_EFFECT_CHANCE = 0.25  # 25% chance of wild effect on backlash
WILD_EFFECT_DIE = 10       # d10 table

# Wild effect durations (in "casts" for simulation purposes).
# Base lasts ~5 casts, escalated ~15 casts.  If still active on 3rd hit => permanent.
WILD_EFFECT_BASE_DURATION = 5
WILD_EFFECT_ESCALATED_DURATION = 15

# ── Exhaustion Overflow ─────────────────────────────────────────────
OVERFLOW_HP_RATIO = 0.5  # overflow * this = HP damage (rounded down)

# ── Misfire Exhaustion ──────────────────────────────────────────────
# On misfire the caster still pays exhaustion equal to the Weak tier cost
# (this is the misfire cost shown in the compendium).

# ── Spell Cost Table ────────────────────────────────────────────────
# complexity -> tier -> (exhaust, casting_time)
SPELL_COSTS = {
    1: {"weak": 2,  "standard": 4,  "strong": 6,  "spectacular": 10, "misfire": 2},
    2: {"weak": 3,  "standard": 6,  "strong": 9,  "spectacular": 14, "misfire": 3},
    3: {"weak": 4,  "standard": 8,  "strong": 12, "spectacular": 18, "misfire": 4},
    4: {"weak": 6,  "standard": 10, "strong": 16, "spectacular": 24, "misfire": 6},
}

# ── All 37 Spells ───────────────────────────────────────────────────
SPELLS = {
    # Aetheric Manipulation
    "Force":          {"school": "Aetheric", "complexity": 1},
    "Elemental":      {"school": "Aetheric", "complexity": 2},
    "Barrier":        {"school": "Aetheric", "complexity": 2},
    "Kinesis":        {"school": "Aetheric", "complexity": 2},
    "Disruption":     {"school": "Aetheric", "complexity": 2},
    "Amplify":        {"school": "Aetheric", "complexity": 1},
    "Arc":            {"school": "Aetheric", "complexity": 2},
    # Vivimancy
    "Mend":           {"school": "Vivimancy", "complexity": 3},
    "Fortify":        {"school": "Vivimancy", "complexity": 2},
    "Wither":         {"school": "Vivimancy", "complexity": 3},
    "Sense Life":     {"school": "Vivimancy", "complexity": 1},
    "Shape Flesh":    {"school": "Vivimancy", "complexity": 4},
    "Purge":          {"school": "Vivimancy", "complexity": 3},
    "Bloom":          {"school": "Vivimancy", "complexity": 2},
    # Warding
    "Shield":         {"school": "Warding",   "complexity": 2},
    "Seal":           {"school": "Warding",   "complexity": 2},
    "Banish":         {"school": "Warding",   "complexity": 3},
    "Circle":         {"school": "Warding",   "complexity": 3},
    "Anchor":         {"school": "Warding",   "complexity": 2},
    "Unbind":         {"school": "Warding",   "complexity": 2},
    # Divination
    "Reveal":         {"school": "Divination", "complexity": 2},
    "Scry":           {"school": "Divination", "complexity": 3},
    "Read":           {"school": "Divination", "complexity": 2},
    "Foresight":      {"school": "Divination", "complexity": 3},
    "Detect":         {"school": "Divination", "complexity": 1},
    "Commune":        {"school": "Divination", "complexity": 3},
    # Transmutation
    "Reshape":        {"school": "Transmutation", "complexity": 2},
    "Alter Property": {"school": "Transmutation", "complexity": 2},
    "Refine":         {"school": "Transmutation", "complexity": 2},
    "Enlarge/Reduce": {"school": "Transmutation", "complexity": 3},
    "Fuse":           {"school": "Transmutation", "complexity": 2},
    "Transmute":      {"school": "Transmutation", "complexity": 4},
    # Ley Weaving
    "Dampen":         {"school": "Ley Weaving", "complexity": 3},
    "Channel":        {"school": "Ley Weaving", "complexity": 3},
    "Attune":         {"school": "Ley Weaving", "complexity": 2},
    "Surge":          {"school": "Ley Weaving", "complexity": 3},
    "Sever":          {"school": "Ley Weaving", "complexity": 4},
}

# ── Simulation Parameters ───────────────────────────────────────────
CASTS_PER_CHARACTER = 500
NUM_CHARACTERS_PER_CONFIG = 50  # characters per (level, path) combo
RANDOM_SEED = 42
