# Generation Settings

Model configurations and parameters for consistent pen & ink RPG illustration.

---

## Primary Recommendation: FLUX via ComfyUI

FLUX produces the best results for this style because natural language prompts
allow detailed description of pen technique, crosshatching, and decorative elements.

### Model Selection

| Priority | Model | Use Case |
|----------|-------|----------|
| 1st | `flux_dev.safetensors` | Final art — highest quality |
| 2nd | `flux1-schnell-fp8.safetensors` | Drafts, iteration, style testing |

### LoRA Stack (Style-Critical)

Apply these LoRAs to push FLUX toward pen & ink illustration. Exact LoRA names
vary by source — search for equivalents matching these descriptions:

| LoRA | Strength | Purpose |
|------|----------|---------|
| Lineart / pen & ink LoRA | **0.70-0.80** | Core pen & ink line quality, crosshatching |
| Sketch / illustration LoRA | **0.40-0.55** | Traditional media rendering, hand-drawn feel |
| High contrast B&W LoRA | **0.30-0.45** | Push toward pure black/white, eliminate grey |

**Recommended LoRA search terms:** `lineart`, `pen_and_ink`, `crosshatch`,
`manga_lineart`, `sketch_style`, `ink_illustration`, `monochrome`

**Tuning notes:**
- If results have too much grey/softness, increase lineart LoRA strength
- If crosshatching looks mechanical/repetitive, decrease lineart, increase sketch
- If results drift toward color, add "monochrome, black and white only" to prompt
  and increase B&W LoRA strength
- Start with one LoRA at a time to evaluate individual contributions before stacking

### FLUX Generation Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| **CFG Scale** | 3.0-3.5 | Standard FLUX range |
| **Steps** | 25 | Up to 35 for finals |
| **Sampler** | euler | Standard FLUX sampler |
| **Scheduler** | normal | Standard FLUX scheduler |
| **Seed** | Record every seed | For reproducibility |

### Resolution by Art Type

| Art Type | Resolution | Aspect Ratio | Notes |
|----------|-----------|--------------|-------|
| Full-page plate | 1024 x 1408 | ~0.73:1 (portrait) | Upscale 2x for print |
| Half-page illustration | 1024 x 704 | ~1.45:1 (landscape) | Upscale 2x for print |
| Spot illustration | 768 x 768 | 1:1 (square) | Crop to subject |
| Character portrait | 832 x 1216 | ~0.68:1 (portrait) | Upscale 2x for print |
| Equipment study | 1024 x 1024 | 1:1 (square) | |
| Decorative border | 1408 x 320 | ~4.4:1 (wide) | Tile-friendly |
| Location vignette | 1024 x 704 | ~1.45:1 (landscape) | |
| Map element | 1024 x 1024 | 1:1 (square) | |

---

## Post-Processing Pipeline (Critical)

AI generators struggle with pure B&W pen & ink. Every piece requires post-processing:

### Step 1: Threshold Conversion
- Open in image editor (GIMP, Photoshop, etc.)
- Convert to greyscale
- Apply threshold (typically 128-160 — adjust per piece)
- Goal: pure black (#000) and pure white (#FFF) only

### Step 2: Contrast & Cleanup
- Boost contrast before thresholding if line quality is weak
- Remove generation artifacts (stray dots, smudges, border noise)
- Clean up any areas where thresholding created unwanted fills

### Step 3: Line Refinement
- Check crosshatching areas — threshold may close gaps between lines
- Check fine detail — stippling may vanish if threshold is too aggressive
- Manual touchup in key areas (faces, hands, focal details)

### Step 4: Upscaling (for print)
- Use a detail-preserving upscaler (Real-ESRGAN with lineart model, or Topaz)
- Upscale to 2x generation resolution for print-ready output
- Re-threshold after upscaling if grey values reappear

### Optional: ComfyUI Automation
Build a post-processing workflow node chain:
1. Output from generation → Greyscale conversion → Threshold node → Save
2. Parameter: threshold level (expose as widget for per-piece adjustment)

---

## IP-Adapter for Character Consistency

Once a character design is approved, use it as IP-Adapter reference for all
subsequent illustrations featuring that character.

### Setup
1. Generate and approve the character portrait
2. Use as IP-Adapter reference image for subsequent pieces
3. Use CLIP Vision for style matching across the full art set

### Consistency Chain
```
Approved Character Portrait
  ├── IP-Adapter reference for character appearances in plates/spots
  ├── CLIP Vision style reference for creature/location art
  └── Line weight and crosshatch density anchor for all art
```

---

## Batch Generation Strategy

### Phase 1: Style Lock-In

1. Generate 5-10 test pieces across different art types (1 portrait, 1 creature,
   1 equipment, 1 spot, 1 border)
2. Evaluate against style guide checklist
3. Tune LoRA strengths and prompt language
4. Run post-processing pipeline on each to verify B&W conversion quality
5. Establish the "golden reference set" — the approved pieces that define the standard

### Phase 2: Character & Creature Art

1. Character portraits for major character types (6-8 portraits)
2. Key creature illustrations (10-15 creatures)
3. Use IP-Adapter with approved portraits for consistency

### Phase 3: Locations & Equipment

1. Location vignettes for major zone types (dead zone, normal, light magic,
   wild zone, deep wild — 5-8 pieces)
2. Equipment studies for key weapon categories (sword, revolver, tommy gun,
   exotic arc gun, magical artifact — 8-12 pieces)

### Phase 4: Decorative Elements & Spots

1. Border templates (4-6 variations: Deco, Nouveau, blended, magic-themed, tech-themed)
2. Section dividers (3-4 variations)
3. Spot illustrations for rules concepts (15-25 pieces)
4. Drop cap alphabet (optional — 26 decorated initials)

### Phase 5: Full-Page Plates

1. Chapter opener plates (6-10 depending on chapter count)
2. These are the showcase pieces — allocate the most iteration time here

---

## Seed & Prompt Logging

**Critical for reproducibility.** For every generation, record:

| Field | Example |
|-------|---------|
| Piece name | Adventurer Portrait — Scholarly Caster |
| Art type | Character portrait |
| Model | flux_dev |
| LoRA stack | lineart:0.75, sketch:0.45, bw:0.35 |
| Seed | 847293651 |
| CFG | 3.5 |
| Steps | 30 |
| Resolution | 832 x 1216 |
| Full prompt | (paste complete prompt) |
| Post-processing | Threshold: 145, upscaled 2x, manual cleanup on hands |
| Accepted? | Yes / No (if no, note why) |
| File path | assets/generated/finals/characters/scholarly-caster.png |

Store in `docs/art/generation-log.md` (create when generation begins).
