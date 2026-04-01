# Negative Prompts & Avoidance Guide

What to exclude from generation. FLUX ignores negative prompts, so for FLUX
use the positive reframes to steer the model away from unwanted results.

---

## SDXL Universal Negative Prompt

Use as the base negative for any SDXL/SD1.5 fallback generations:

```
worst quality, low quality, blurry, deformed, extra limbs, bad anatomy,
bad hands, extra fingers, missing fingers, fused fingers, too many fingers,
mutated hands, poorly drawn hands, poorly drawn face, mutation, ugly,
text, watermark, signature, logo, username, artist name, title,
color, colorful, saturated, painted, oil painting, watercolor, pastel,
photorealistic, 3d render, CGI, smooth digital art, airbrushed,
grey tones, greyscale gradient, soft shading, cel shaded,
cute face, chibi, super deformed, kawaii, moe,
photo, photograph, realistic skin texture,
manga screentone, halftone dots
```

---

## Category: Color & Tone Control

The single most important avoidance category. AI generators default to color.

**Avoid:**
- Any color at all — even sepia, even subtle warm/cool tones
- Grey gradients or smooth tonal transitions
- Watercolor washes or ink-wash effects
- Soft digital shading

**FLUX positive reframe:** "pure black and white pen and ink, no color,
no grey tones, only black ink marks on white paper, crosshatching creates
all tonal values, monochrome illustration, high contrast black and white"

---

## Category: Technical Quality

**Avoid:**
- Smooth digital rendering (kills the pen & ink look)
- Soft or blurred edges
- Photorealistic textures
- 3D render appearance
- Perfect geometric shapes (should look hand-drawn, not CAD)
- Overly uniform line weight (real pen work has variation)

**FLUX positive reframe:** "hand-drawn with steel nib dip pen, visible pen
strokes with natural weight variation, traditional media texture, crosshatching
built from individual ink lines, not digitally generated patterns"

---

## Category: Tone & Mood

**Avoid:**
- Cute, kawaii, or chibi aesthetics
- Grimdark gore or body horror (this is heroic, not nihilistic)
- Generic heroic fantasy poses (power stance with cape billowing)
- Medieval fantasy costuming (this is 1920s, not swords & sorcery)
- Anime face conventions (oversized sparkle eyes, tiny nose/mouth)
- Fan service or gratuitous sexualization

**FLUX positive reframe:** "1920s period clothing, heroic but grounded tone,
determined expression, practical adventuring gear, worn and experienced,
classic illustration character design, detailed realistic proportions"

---

## Category: Composition

**Avoid:**
- Detailed landscape backgrounds (for spot illustrations)
- Busy, cluttered compositions
- Text or UI elements in the image
- Borders or frames (unless specifically generating a border)
- Symmetrical passport-photo poses (for character art)
- Multiple overlapping subjects in spot illustrations

**FLUX positive reframe:** "clean composition, strong focal point, white
background, single subject centered, clear silhouette, designed for print
reproduction alongside text"

---

## Category: Style Consistency

**Avoid:**
- Watercolor or ink-wash style (wrong medium — we need PEN not BRUSH)
- Oil painting (too heavy)
- Cel-shaded or flat animation coloring
- Manga screentone (different visual language — we use crosshatching)
- Western comic book style (too bold, too dynamic, wrong line quality)
- Concept art / matte painting style
- Art station "digital painting" aesthetic

**FLUX positive reframe:** "pen and ink illustration in the tradition of
Aubrey Beardsley and classic RPG interior art, crosshatching for all shading,
stippling for texture, Art Nouveau and Art Deco decorative influences,
traditional book illustration, not digital painting, not manga, not comic book"

---

## Per-Type Adjustments

### Character Portraits
Add to avoidance: `armor only, medieval, fantasy robes, wizard hat`
Reframe: "1920s civilian clothing with practical adventuring gear layered over"

### Creature Illustrations
Add to avoidance: `cute, friendly, domestic, tame, small, harmless`
Reframe: "supernatural, imposing, wrong in a 1920s context, erupted from another reality"

### Equipment Studies
Add to avoidance: `character, person, hand holding, wielding, full body, background`
Reframe: "technical illustration, object displayed alone, white background, informative angle"

### Location Vignettes
Add to avoidance: `characters, people, figures, action scene`
Reframe: "empty atmospheric scene, establishing shot, architectural focus, mood through linework density"

### Decorative Borders
Add to avoidance: `realistic, narrative, scene, character, creature, perspective`
Reframe: "flat decorative design, tileable pattern, symmetrical ornament, design element"

### Full-Page Plates
Special case — plates CAN include detailed backgrounds, multiple figures, and narrative action.
Reduce avoidance restrictions. Focus avoidance on color, digital smoothness, and style drift only.

### Spot Illustrations
Add to avoidance: `complex background, multiple figures, decorative border, full scene`
Reframe: "minimal, iconic, single concept, reads clearly at 2 inches wide, clean edges"
