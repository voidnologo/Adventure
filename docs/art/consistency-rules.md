# Consistency Rules

Rules for maintaining visual cohesion across generation sessions and the full
art production pipeline. This is the enforcement layer — refer to it before
generating any new art.

---

## Rule 1: Always Reference Before Generating

Before creating any new art, read the following documents in order:

1. `style-guide.md` — What the art should look like
2. `prompt-engineering/prompt-templates.md` — How to construct prompts
3. `prompt-engineering/generation-settings.md` — Technical parameters
4. `prompt-engineering/negative-prompts.md` — What to avoid

Do not generate from memory or assumption. The documents are the source of truth.

---

## Rule 2: Style Discipline

**Hard rules:**
- **Pure black and white only** — no grey tones, no color, no sepia. If the
  generated output has grey values, it must go through the threshold
  post-processing pipeline before evaluation
- **Crosshatching for all shadow/volume** — not smooth gradients, not screentone
- **Consistent line weight** — thick outlines (silhouette), medium lines
  (structure), fine lines (detail and hatching). This hierarchy must be
  maintained across all pieces
- **Crosshatch density consistency** — similar shadow depth should use similar
  hatching density across pieces. Establish density benchmarks from the
  golden reference set
- **Art Nouveau/Deco decorative vocabulary** — all ornamental elements must
  draw from period-appropriate visual language, not generic fantasy decoration
- **1920s period accuracy** — clothing, technology, architecture must be
  era-appropriate unless a specific setting reason overrides

**Verification:** After post-processing to pure B&W, compare line weight and
hatching density against the golden reference set. If the piece looks
noticeably lighter, heavier, or differently styled, regenerate or adjust.

---

## Rule 3: Style Consistency Checklist

Every accepted piece must pass ALL of these checks:

- [ ] Linework quality — clear, confident pen strokes visible throughout
- [ ] Crosshatching present — shadow and volume built from hatching, not gradients
- [ ] Pure B&W — no grey tones survive post-processing (verify at 200% zoom)
- [ ] Art Nouveau/Deco decorative elements consistent with established set
- [ ] 1920s period accuracy in clothing, tech, and architecture
- [ ] No digital smoothness — the piece looks hand-drawn, not rendered
- [ ] Consistent level of detail with existing accepted pieces
- [ ] Composition serves its intended function (spot, plate, portrait, etc.)
- [ ] No text, watermarks, or generation artifacts
- [ ] Anatomy acceptable (hands, faces, proportions)
- [ ] Silhouette clear at reproduction size

If a piece fails 2 or more checks, reject and regenerate.

---

## Rule 4: Character Design Locks

Once a character portrait is approved, the following are **locked** and must
not change in subsequent art featuring that character:

- **Face structure** (bone structure, scars, eye treatment)
- **Hair** (style, length)
- **Signature clothing** (silhouette-defining garments)
- **Signature weapons/equipment** (type, design)
- **Body proportions** (height, build)
- **Distinguishing marks** (magical markers, tattoos, scars)

Use IP-Adapter with the approved portrait as reference for consistency.
If a subsequent generation drifts from locked elements, regenerate.

**Creature design locks** are softer — creatures are supernatural and can
vary somewhat between appearances, but core identifying features (number of
eyes, body plan, scale) must remain consistent.

---

## Rule 5: Prompt Versioning

When modifying a prompt:
1. Note the change and reason in the prompt file
2. Keep the old version (comment it out or move to a "Previous Versions" section)
3. Re-run the quality checklist on new results
4. Update the generation log with the new prompt

Never modify a prompt without recording what changed and why.

---

## Rule 6: Generation Logging

Every generation session must be logged. Create or append to
`docs/art/generation-log.md`:

```markdown
## [Date] — [Session Description]

### [Piece Name]
- **Art type:** [character / creature / equipment / location / decorative / spot / plate]
- **Model:** flux_dev / flux_schnell / etc.
- **LoRA:** lineart:0.75, sketch:0.45, bw:0.35
- **Seed:** 847293651
- **CFG:** 3.5
- **Steps:** 30
- **Resolution:** 832 x 1216
- **Prompt:** (paste or reference the prompt file + modifications)
- **Post-processing:** Threshold: 145, upscaled 2x, manual hand cleanup
- **Result:** Accepted / Rejected (reason)
- **File:** assets/generated/finals/characters/scholarly-caster.png
- **Notes:** Observations about what worked or didn't
```

---

## Rule 7: Batch Consistency

When generating multiple pieces in one session:

1. **Use the same model and LoRA stack** for the entire batch
2. **Use the same CFG and steps** across the batch
3. **Generate all pieces of one type before switching types** — this maintains
   visual consistency within categories
4. **Compare each new piece against the golden reference set** before accepting
5. If you change any parameter mid-batch, note it in the log and re-evaluate
   earlier pieces

---

## Rule 8: Quality Tiers

Not all art needs the same polish level:

| Tier | Art Types | Generation | Iteration |
|------|-----------|------------|-----------|
| **S-tier** | Full-page plates, key character portraits | flux_dev, 35 steps | 5-10 generations, extensive post-processing |
| **A-tier** | Major creatures, location vignettes | flux_dev, 25-30 steps | 3-5 generations |
| **B-tier** | Equipment studies, minor characters, spots | flux_dev, 25 steps | 2-3 generations |
| **C-tier** | Decorative borders, dividers, simple spots | flux_schnell for testing, flux_dev for finals | 1-2 generations |

---

## Rule 9: Cross-Session Continuity

**When starting a new art generation session:**

1. Read this document first
2. Read `docs/continuation-prompt.md` for project context
3. Read `docs/art/generation-log.md` to see what's been done
4. Load approved reference pieces for visual comparison
5. Check for any parameter adjustments noted in the log
6. Continue from where the last session left off

**When ending a session:**

1. Update the generation log with everything generated
2. Note any parameter adjustments that worked well
3. Note any style drift concerns
4. Update `docs/continuation-prompt.md` with art pipeline status

---

## Rule 10: Style Evolution (Controlled)

The art style may evolve as the project develops. This is allowed but controlled:

- **Minor adjustments** (LoRA strength tweaks, prompt wording) — any time, just log
- **Significant changes** (new LoRA, different model, different line quality) —
  re-evaluate all previously accepted art for consistency
- **If more than 5 pieces need regeneration** due to a change, treat it as a
  full art reset and regenerate from the golden reference set

Evolution, not revolution. Small tracked changes that compound into improvement.

---

## Rule 11: Reference Art vs. Original Art

The existing art in `art/` (cat, dragon, fantasy figure) is **reference art only** —
it establishes the visual tone and aesthetic direction but is not original to this
project and may have copyright restrictions.

- **Use as mood/style reference** — these pieces demonstrate the desired line quality,
  crosshatching approach, and decorative sensibility
- **Do not use in final publications** — all published art must be originally generated
- **Do not use as IP-Adapter source** — generate original reference pieces instead
- **The golden reference set** (Phase 1 approved originals) replaces these as the
  authoritative style anchors once it exists

---

## File Organization

```
docs/art/
├── style-guide.md              ← Master visual identity
├── consistency-rules.md        ← THIS FILE — enforcement rules
├── generation-log.md           ← Created when generation begins
├── input-samples/              ← Reference art (style mood board)
├── prompt-engineering/
│   ├── prompt-templates.md     ← Reusable structures
│   ├── negative-prompts.md     ← Avoidance guide
│   └── generation-settings.md  ← Model/param configs
└── prompts/
    ├── characters/             ← One file per character
    ├── creatures/              ← One file per creature
    ├── locations/              ← One file per location
    ├── equipment/              ← One file per equipment piece
    └── decorative/             ← Border/divider/ornament prompts
```

Generated art goes in:
```
assets/generated/
├── drafts/                 ← Work in progress, testing
├── finals/                 ← Approved art (post-processed)
│   ├── characters/
│   ├── creatures/
│   ├── locations/
│   ├── equipment/
│   ├── decorative/
│   └── plates/
└── web/                    ← Web-optimized versions
```
