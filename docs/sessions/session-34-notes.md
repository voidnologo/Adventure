# Session 34: Story 03 Edit Pass + Publish

**Date:** 2026-04-22
**Goal:** Address PR #2 reviewer feedback on Story 03, publish the story on the fiction reader, merge the PR.

## Overview

Closed out Story 03 end-to-end: a full editing pass against the reviewer's 17 comments on PR #2 (mostly ch03–ch08 craft notes plus a continuity fix to ch01), followed by wiring the story into the live fiction reader. Refactored `web/_data/fiction.js` from a hard-coded story-02 loader into a config-driven `buildStory()` helper so future stories just need a config entry, and added a reader template at `web/fiction/the-lamplighters-price.njk`. PR #2 retitled (dropped "(draft)"), body updated to reflect the published state, and merged by the user.

Story 03 is now live — the fiction index lists "The Lamplighter's Price" as Story No. 03, above Story 02. Next session picks up Story 04 planning.

---

## Changes Made

### Editing Pass (commits 426ef26, 671f5d5 — pre-conversation)
- **ch01 continuity fix**: clarified that the Society disrupted Fels's operation (during the Ashwick Job), not the reverse — the motivational bedrock for the whole story's blackmail.
- **ch03 craft pass**: compass behavior brought back in line with canon — it *locks* in Galvanic territory and *spins* in Aetheric (barometer, not guide). Sera now navigates by feel of the Aether current, not by the compass. Barrier dome rewritten: it pushes outward and *bulges* the collapse rather than sealing it off; added a release-tension sequence so the team moves to stable ground before Sera drops the dome and the held collapse comes down behind them. Eye-glow fade shifted to future-conditional.
- **ch04 craft pass**: removed "he reached / didn't reach" repetition; replaced the second "tightening in his chest"; stripped explicit game-mechanic numbers (exhaustion point counts) from the Detect/Shield passages so the scholarly-casting showcase reads as sensation rather than bookkeeping; varied the "pale seamless / luminous veins" descriptor cluster.
- **ch05–ch08 polish**: smaller line-level fixes across the back half.

### Publish to Reader (commit b5e876f — this conversation)
- Refactored `web/_data/fiction.js` from a single `loadStory02()` function into a `buildStory(config)` helper with per-story config objects. Story 02 and Story 03 both now pass through the same pipeline; adding Story 04 will just mean adding one config entry.
- Added `web/fiction/the-lamplighters-price.njk` — reader template modeled on `what-the-mill-remembered.njk` (same TOC drawer, scroll-spy, reading progress bar, chapter rendering).
- Verified `npm run build` cleanly produces `_site/fiction/the-lamplighters-price.html` and the updated `_site/fiction/index.html` (Story 03 listed above Story 02).

### PR #2 Closeout
- Retitled from "Fiction — Story 03: The Lamplighter's Price (draft)" → "Fiction — Story 03: The Lamplighter's Price"
- Body updated to note the story is now published on the reader, with the site-changes section describing the fiction.js refactor.
- Merged by user.

---

## Files Modified

| File | Change |
|------|--------|
| `fiction/stories/story-03/ch01.md` | Continuity fix: Society disrupted Fels's operation, not the reverse |
| `fiction/stories/story-03/ch03.md` | Compass canon restored; Barrier dome rewrite; release-tension sequence |
| `fiction/stories/story-03/ch04.md` | Repetition trims; mechanic numbers stripped; descriptor variance |
| `fiction/stories/story-03/ch05.md` | Line-level polish |
| `fiction/stories/story-03/ch06.md` | Line-level polish |
| `fiction/stories/story-03/ch07.md` | Line-level polish |
| `fiction/stories/story-03/ch08.md` | Line-level polish |
| `web/_data/fiction.js` | Refactored to `buildStory(config)` helper; added Story 03 config entry |
| `web/fiction/the-lamplighters-price.njk` | New — Story 03 reader template |

---

## Key Design Decisions

- **Compass is a barometer, not a guide.** Reviewer caught ch03 using the compass as a navigational aid in the tunnels; canonically the compass *locks* in Galvanic zones and *spins* in Aetheric zones — it tells you the weather of the Aether, not the direction. Sera navigates underground by *feel* of the Aether current (passive sensitivity, cost-free). The fix strengthens the magic-system showcase: Sera has an intuitive pathfinding ability that Aldric, the scholarly caster, does not.
- **Barrier dome pushes outward, doesn't just shield.** The original draft had the dome stop a ceiling fracture. The reviewer's instinct was that a Spectacular-tier cast in a zone surge should have more physicality — so it now pushes the collapse outward, bulges the tunnel, and needs an active release sequence (team clears stable ground *before* Sera drops it and the held mass comes down). Costlier to Sera, more vivid, and more mechanically legible: you see the wild-caster variance *and* the team managing a controlled release.
- **No explicit EP counts in Aldric's POV.** The original ch04 had lines like "four exhaustion points spent, twenty-eight remaining" — too mechanical. Stripped; the counting-as-ammunition metaphor stays, but the numbers do not. The reader should feel the resource scarcity without reading a spreadsheet.
- **fiction.js refactor now, not later.** Pending-tasks had "generalize fiction.js when Story 03 ships, not before" — Story 03 shipped, so this was the moment. Single `buildStory(config)` helper + per-story config objects. Story 04 will drop in as a config entry plus a reader template.

---

## Open Issues

- Series bible (`fiction/world/06-series-bible.md`) still needs an update with final Story 03 outcomes — seeds, character status (Sera's accumulation, Kael-Mira trust crack), world state (Syndicate relationship, Collective expedition intel), new NPC notes.
- Story 04 to be planned — user has flagged it as the combat-focused story in the series arc (Kael-heavy, timing track, Galvanic devices, damage & injury). Will be next session's main work.

## Next Session

- **Plan Story 04** — the combat-focused story. Establish premise, chapter structure, which combat mechanics to showcase (timing track, damage, weapon reliability, Galvanic devices).
- Before or during planning: update series bible with Story 03 outcomes so Story 04 planning has a current state snapshot to build on.
