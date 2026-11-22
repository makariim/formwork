---
brief: 0033
stream: method
title: Measure a guard, review then refute, the task size ceiling
status: dropped (his words 2026-11-22: "Close 0033")
starts: now
size: checkpoint
---

# 0033 Measure a guard, review then refute, the task size ceiling

## His words

"Formwork: the last two ECC ideas (measuring a guard properly, review then refute) and the small task-size check. start them, they are small" (2026-11-15).

## The job

1. **Measure a guard with arms** (`docs/research/ecc-ideas.md` idea 1): a method page and a small runner for measuring any guard or rule: three arms (off, on, and a placebo that refuses the same calls with generic text), the bar and the funding decision written **before** the pilot, results printed whichever way they fall, cost beside effect. Run it once, small, on one existing formwork guard as the worked example (cheap model, say the cost, cap it at about one US dollar), and record the result with its command.
2. **Review, then refute** (idea 2): add to the review round template and the lead role: reviewers by dimension in parallel, findings deduplicated by their evidence, then a verifier per serious finding that defaults to "refuted" unless the evidence holds; a reviewer that failed makes the result incomplete, never a pass.
3. **The task size ceiling** (from `docs/research/0022-whole-project-builds.md`, step 3's leftover): the check or rule the research described for a task that has grown past a task (a one line brief that turned into many files or a long run) so it is stepped up instead of silently continuing. Kit style with fixtures.

## Rules

- Generic only; leak scan and hidden-unicode stay green. Do not touch other repositories.
- **At a guard refusal, stage every protected change in `docs/reports/0033-three-small.patch`.**
- No git writes. Run `formwork/fw test` and `formwork/fw check`.
- Report at `docs/reports/0033-three-small.md`: `## For you` first (at most 8 lines, plain, with the guard measurement's result as a number), then details. Last message: one line starting `result:`.
