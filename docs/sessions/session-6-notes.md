# Session 6: Website & Art Pipeline

**Date:** 2026-03-31
**Goal:** Create landing page + rules reference website (static HTML, GitHub Pages). Establish art style guide and AI generation pipeline for 1920s steampunk pen-and-ink aesthetic.

## Overview

Built two major deliverables: (1) a static website with a landing page and full rules reference, modeled after the card-game/web structure, and (2) a comprehensive art style guide and AI generation pipeline for producing original RPG illustration in a consistent 1920s steampunk pen & ink style.

The website uses a dark Art Deco aesthetic with brass/parchment color tokens, Cinzel + Crimson Pro + Josefin Sans typography, scroll-reveal animations, and responsive layout. The landing page showcases the setting, design pillars, and mechanics preview. The rules reference presents the full core mechanics from BASE_MECHANICS.md and COMBAT_PROCEDURE.md in a styled, navigable format with a table of contents, callout boxes, and the one-page cheat sheet.

The art pipeline adapts the card-game repo's docs/art/ structure for pen & ink RPG illustration rather than ink-wash card art. Includes style guide (5 visual pillars), prompt templates for 7 RPG art types, FLUX/ComfyUI generation settings, negative prompts/avoidance guide, and consistency rules (11 rules).

---

## Changes Made

### 1. Website — Landing Page (web/index.html)
- Full-viewport hero section with Art Deco corner brackets, sunburst glow, CTA buttons
- "The World" section: setting intro with magic/tech/steel tension sidebar
- Art showcase: expandable filmstrip with hover effects showing the 3 reference pieces
- Design pillars grid: 6 pillars from PROJECT_SPEC.md
- Mechanics preview: 4-panel grid (core roll, death spiral, two paths of magic, interference)
- CTA footer with link to rules reference
- Scroll-reveal animations, responsive breakpoints, fractal noise grain texture

### 2. Website — Rules Reference (web/rules/index.html)
- Full-viewport cover page
- 2-column table of contents
- 11 sections covering all core mechanics: core roll, opposed checks, stats, skills, derived values, magic (casting, two paths, overflow, rituals), interference (accumulation, zones), combat (timing track, declaration, active defense, range bands, death), recovery, character creation
- Styled callout boxes (examples, notes, warnings)
- Formatted cheat sheet matching BASE_MECHANICS.md one-page summary
- Art Deco ornament dividers between sections

### 3. Art Style Guide (docs/art/style-guide.md)
- Core identity: pen & ink, 1920s steampunk, heroic tone
- 5 visual pillars: pen & ink linework, Art Nouveau meets Art Deco, 1920s period accuracy, supernatural atmosphere, illustrative function
- Character design principles (period-appropriate, silhouette test, diversity of role)
- 8 art composition types: full-page plates, spot illustrations, character portraits, creature illustrations, equipment studies, location vignettes, decorative elements, map elements
- Technical specs (print-ready resolutions, post-processing pipeline)
- Quality checklist

### 4. Prompt Templates (docs/art/prompt-engineering/prompt-templates.md)
- Universal style prefix/suffix for FLUX
- 7 templates: character portrait, creature illustration, equipment study, location vignette, full-page plate, decorative border, spot illustration
- Game-specific visual cues table (12 concepts mapped to visual language)

### 5. Generation Settings (docs/art/prompt-engineering/generation-settings.md)
- FLUX Dev/Schnell model selection
- LoRA stack recommendations (lineart, sketch, B&W contrast)
- Resolution table for each art type
- Post-processing pipeline (threshold, contrast, cleanup, upscaling)
- IP-Adapter consistency chain
- 5-phase batch generation strategy
- Seed & prompt logging format

### 6. Negative Prompts (docs/art/prompt-engineering/negative-prompts.md)
- SDXL universal negative prompt
- 5 avoidance categories with FLUX positive reframes: color/tone control, technical quality, tone/mood, composition, style consistency
- Per-type adjustments for each art type

### 7. Consistency Rules (docs/art/consistency-rules.md)
- 11 rules: reference order, style discipline, checklist, character locks, prompt versioning, generation logging, batch consistency, quality tiers, cross-session continuity, style evolution, reference art vs original art
- File organization (docs/art/ and assets/generated/ directory structures)

---

## Files Modified

| File | Change |
|------|--------|
| `web/index.html` | **NEW** — Landing page |
| `web/rules/index.html` | **NEW** — Rules reference |
| `web/assets/art/cat.png` | **COPIED** — from art/ for web |
| `web/assets/art/dragon.jpg` | **COPIED** — from art/ for web |
| `web/assets/art/fantasy.jpg` | **COPIED** — from art/ for web |
| `docs/art/style-guide.md` | **NEW** — Master visual identity |
| `docs/art/prompt-engineering/prompt-templates.md` | **NEW** — FLUX prompt structures |
| `docs/art/prompt-engineering/generation-settings.md` | **NEW** — Model/LoRA/parameter configs |
| `docs/art/prompt-engineering/negative-prompts.md` | **NEW** — Avoidance guide |
| `docs/art/consistency-rules.md` | **NEW** — Art pipeline enforcement rules |
| `docs/sessions/session-6-notes.md` | **NEW** — This file |

## Key Design Decisions

1. **Pure B&W pen & ink, not ink-wash** — the card-game uses Japanese ink-wash painting with limited color. This project uses precise pen & ink linework with crosshatching. Completely different visual language, despite sharing FLUX/ComfyUI infrastructure.
2. **Art Nouveau for magic, Art Deco for technology** — the visual tension mirrors the mechanical tension. Magic sections use organic flowing lines; technology sections use geometric precision. Both are period-appropriate to the 1920s.
3. **Reference art is placeholder only** — existing art in art/ establishes visual tone but is not original. All published art must be generated through the pipeline. Added Rule 11 to consistency rules making this explicit.
4. **Post-processing pipeline is mandatory** — AI generators struggle with pure B&W. Every piece must go through threshold conversion to eliminate grey tones. This is built into the workflow, not an afterthought.
5. **Google Fonts for web** — using Cinzel (serif display), Crimson Pro (body text), Josefin Sans (UI labels), Fira Code (formulas/code). All loaded from Google Fonts CDN. For print/self-hosted, these are all open-source fonts.
6. **Dark Art Deco color palette** — brass/gold (#b8860b) as accent against near-black backgrounds, parchment (#e8dcc8) for text. Evokes the period while being easy on the eyes for reading rules.

## Open Issues

- Need to generate original art through the pipeline (Phase 1: style lock-in with golden reference set)
- fonts/ directory is empty — fonts are loaded from Google CDN. If self-hosting needed, download and add.
- No favicon yet
- GitHub Pages deploy configuration not yet set up (need gh-pages branch or docs/ folder config)
- Website currently shows reference art with creative captions — replace with original generated art once available
- Rules page doesn't include spell compendium or weapon tables — those are detailed reference that could be separate pages

## Next Session

Generate original art through the pipeline (style lock-in phase). Or continue with game design: factions, leveling, or zone mechanics.
