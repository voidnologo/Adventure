# Prompt Templates

Reusable prompt structures for generating pen & ink RPG illustration art.
FLUX (natural language) format — the primary generation model.

**Important:** Always prepend the style prefix and append the style suffix.
The middle section is subject-specific.

---

## Universal Style Prefix

```
Black and white pen and ink illustration. Detailed crosshatching and fine
linework drawn with a steel nib dip pen. Art Nouveau and Art Deco decorative
influences. 1920s steampunk aesthetic. Pure black ink on white paper, no grey
tones, no color. The style of classic fantasy RPG interior illustration
crossed with Aubrey Beardsley's ornamental precision.
```

---

## Universal Style Suffix

```
Rendered in pure black and white with confident penwork and crosshatching
for shadow and volume. Clean linework with thick-to-thin variation.
Decorative detail that rewards close inspection. White background.
No color, no grey wash, no digital smoothness. Traditional pen and ink
illustration technique. High contrast, crisp lines, printable at 300 DPI.
```

---

## Template: Character Portrait

Adventurers, NPCs, and character type examples.

```
[STYLE PREFIX]

A [body type] [gender] [role/class description] in [pose — standing ready,
examining a map, mid-stride, leaning against a wall]. [Age descriptor] with
[distinctive physical features — scars, unusual eyes, weathered face].

Wearing [1920s-appropriate clothing — suit, overcoat, leather boots, hat type].
[Equipment details — holstered revolver, sheathed sword at hip, slung rifle,
leather satchel, tool belt, brass instruments]. [Magical markers if caster —
faint geometric marks on hands, unusual eye quality, subtle aura rendered
in stippling].

Expression is [emotional quality — determined, wary, scholarly, haunted,
quietly confident]. Posture conveys [character quality — seasoned competence,
restless energy, quiet authority, barely contained power].

[STYLE SUFFIX]
```

---

## Template: Creature Illustration

Supernatural beings, monsters, corrupted creatures.

```
[STYLE PREFIX]

A [creature description — size, body plan, key features] in a [dynamic or
menacing pose]. [Scale reference — towering over a human figure, coiled in
a doorway, perched on a rooftop]. [Key visual features that convey game
mechanics — armored plates, multiple eyes, vestigial wings, magical
corruption marks, organic growths].

The creature conveys [threat quality — predatory intelligence, mindless
hunger, alien indifference, corrupted majesty]. It should feel like
something that erupted into a 1920s world — wrong, impossible, and
awe-inspiring.

[Decorative framing if desired — the creature breaking through an Art Deco
border, tendrils of magic dissolving geometric patterns].

[STYLE SUFFIX]
```

---

## Template: Equipment Study

Weapons, artifacts, gear, and technology.

```
[STYLE PREFIX]

A [equipment type — revolver, sword, aetheric device, magical artifact]
displayed in a technical illustration style. [Detailed physical description
— materials, construction, wear, craftsmanship, period-appropriate design].
[Mechanical or magical details — inscribed runes, brass fittings, vacuum
tubes, arc coils, crystalline components].

The object rests on a flat surface or floats against a white background.
[Condition — well-maintained, battle-worn, corroded by magical exposure,
prototype with exposed mechanisms]. No character holding or wielding it.

[Optional: multiple views or detail callouts in the manner of a technical
diagram, with fine annotation lines].

[STYLE SUFFIX]
```

---

## Template: Location Vignette

Environments, zones, atmospheric scene-setters.

```
[STYLE PREFIX]

A [establishing shot / atmospheric view] of [location description — Art Deco
skyscraper district, overgrown wild zone ruins, noir alleyway at night,
industrial factory floor, occult bookshop interior, airship dock].

[Atmospheric detail — fog rendered in stippling, smoke from chimneys in
flowing Art Nouveau lines, magical energy as geometric patterns dissolving
into organic growth]. [Period detail — gas lamps, automobiles, radio aerials,
telegraph wires, jazz club signage].

The mood is [atmospheric quality — oppressive industrial weight, eerie magical
stillness, noir shadow and light, frontier wildness at the edge of
civilization].

[Zone type if relevant — show the magic/tech spectrum through visual language:
industrial dead zones are all geometry and machinery, wild zones are organic
chaos consuming built structures].

[STYLE SUFFIX]
```

---

## Template: Full-Page Plate

Chapter-opening narrative illustrations.

```
[STYLE PREFIX]

A dramatic narrative scene: [scene description — adventurers entering a wild
zone ruin, a creature erupting through a city street, a scholar casting amid
failing machinery, a gunfight in a magic-saturated jazz club].

[Composition — foreground action with background atmosphere, diagonal dynamic
lines, strong contrast between light and shadow areas]. Multiple figures
interacting in a moment of [tension / discovery / combat / wonder].

[Art Nouveau/Deco decorative border framing the scene — organic magical
motifs on one side, geometric industrial motifs on the other, meeting and
conflicting at the edges].

Full page composition, portrait orientation. Maximum crosshatching detail
in focal areas, lighter linework in atmospheric background.

[STYLE SUFFIX]
```

---

## Template: Decorative Border

Frames, dividers, drop caps, page ornaments.

```
[STYLE PREFIX]

A decorative [border / divider / corner piece / drop cap letter "[X]"]
in [Art Deco geometric style / Art Nouveau organic style / blended style].

[Motif elements — interlocking gears and vines, sunburst patterns with
magical symbols, geometric frames with organic growths breaking through,
compass rose with arcane markings, stylized flames and machinery].

Symmetrical design suitable for [framing a full page / dividing sections /
beginning a chapter]. Clean lines, precise geometry where geometric,
flowing curves where organic. Designed to tile or mirror.

[STYLE SUFFIX]
```

---

## Template: Spot Illustration

Small inline illustrations for rules and flavor text.

```
[STYLE PREFIX]

A small, focused illustration of [subject — a hand gripping a revolver,
a spell effect crackling between fingers, a wound being bandaged, a
compass spinning near a magic zone, an aetheric device overloading].

Simple composition, strong silhouette, minimal background. Must read
clearly at 2-3 inches wide. [Key detail that communicates the rule or
concept being illustrated].

Clean edges suitable for integration with body text on a printed page.

[STYLE SUFFIX]
```

---

## Game-Specific Visual Cues

When illustrating game mechanics or setting concepts, include these visual elements:

| Concept | Visual Cue |
|---------|------------|
| **Magic Accumulation** | Stippled energy halos, geometric patterns forming in the air, fine lines radiating from the caster |
| **Tech Interference** | Machinery with hairline cracks, gears seizing, sparks rendered as sharp radiating lines |
| **Wild Zone** | Organic growth consuming architecture, flowing Art Nouveau lines overtaking Art Deco geometry |
| **Dead Zone** | Pure geometric order, heavy industrial detail, stark angular shadows, absence of organic forms |
| **Exhaustion** | Sagging posture, heavy crosshatching under eyes, equipment hanging loose |
| **Wound Tiers** | Progressive damage: clean (OK) → torn clothing (Harmed) → heavy bandaging (Maimed) → collapsed (Incapacitated) |
| **Scholarly Magic** | Controlled geometric patterns, precise lines, book/scroll props, deliberate gestures |
| **Wild Magic** | Chaotic organic energy, stippled auras, involuntary posture, uncontrolled growth |
| **Backlash** | Cracked skin, energy leaking, pain response, surrounding environment damaged |
| **Steampunk Exotics** | Brass and copper construction, vacuum tubes, arc coils, aetheric crystals, visible energy conduits |
| **Conventional Tech** | Standard 1920s firearms and machinery, no exotic elements, reliable and mundane |
| **The Eruption** | Reality cracking open, the mundane world splitting to reveal something vast beneath |

---

## Prompt Assembly Order

1. Style prefix (universal)
2. Subject description (from template)
3. Period and setting details (1920s elements)
4. Game-specific visual cues (from table above)
5. Composition notes (size, function, framing)
6. Style suffix (universal)

Always be explicit about "black and white," "pen and ink," "crosshatching,"
and "no color." AI generators default toward color and digital rendering —
you must actively steer away from both in every prompt.
