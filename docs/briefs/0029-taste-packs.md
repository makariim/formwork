---
brief: 0029
stream: method
title: Taste packs
status: done (accepted 2026-11-15)
starts: now
---

# 0029 Taste packs

## His words

"c, go" (2026-11-15): step 7 of `docs/research/0022-whole-project-builds.md`, then ECC ideas as small steps after. Earlier: "i had to tell explicitly what is and whats not ai vibed".

## The job

Build "Taste packs" exactly as the research describes:

1. **The pack shape**: optional, per product kind, named by a project and overridden by it; never a kit default for the look. Each item says what it catches and how it is detected: high (a pattern a check could grep), medium, low (needs eyes). The project's own design file always wins.
2. **The three kit items** that survived every change of his taste: decoration never poses as data (charts only from real numbers, no fake pictures); copy says the thing, not the feature; every rendered screen gets two questions, "generic or AI made?" and "dead?" (clean is not the same as alive).
3. **First packs**: web and deck, from public sources with citations; an iOS pack only as far as Apple's Human Interface Guidelines can be read properly (if the fetch fails, mark it NOT ESTABLISHED and leave the pack short). Generic, adapted from the patterns in the health app's director check (`<health-app>/docs/design/round-2/director-ai-check.md`, read only: pills only for real choices, one soft light per screen, no glowing buttons, solid colours unless a gradient means something, no icon tiles, one neutral surface, standard navigation, no decoration posing as data) written as general rules with no product or person in them.
4. ECC's design signals (generic headlines, uniform card grids, stock gradients, default fonts) only as **detection hints** inside pack items, never as a check. **Taste is never a check**; it is a review round on pictures (the review round template).
5. The routing table and the design and review round templates point to the packs.

## Rules

- Generic only; the leak scan stays green. Do not touch any other repository.
- **If a guard refuses an edit, stop and report it.**
- No git writes. Run `formwork/fw test` and `formwork/fw check`; say that he re-records fingerprints after review if needed.
- Report at `docs/reports/0029-taste-packs.md`: `## For you` first (at most 8 lines, plain), then details. Last message: one line starting `result:`.
