---
brief: 0026
stream: method
title: Measure routing
status: done (accepted 2026-11-15)
---

# 0026 Measure routing

## His words

"next" (2026-11-15): step 4 of the build plan in `docs/research/0022-whole-project-builds.md`. Routing (0025) is built; its accuracy is NOT ESTABLISHED until measured.

## The job

1. Write a set of plain prompts in `formwork/evals/routing/` (or the place the research names): at least 40, covering all six kinds and every size, including prompts that **should not** be routed big (small asks dressed in big words) and ambiguous ones, each with the expected kind, size and first step. Written generically, inspired by the real requests in the four projects but with no personal content.
2. Run each prompt once through the routing as a fresh session would see it (the director role, `formwork/route.md`, an empty corrections file), record what it chose, and score it against the expected answer.
3. Write the result on the routing page as a number with the command that produced it (for example "34 of 40 routed as expected"), the failures listed by kind, and change "NOT ESTABLISHED" to that number. Fix the table only where a failure shows a clear gap, then run the set again and record both runs.
4. Keep the set and a one command runner so the measurement can be repeated after any change.

## Rules

- Generic only; the leak scan stays green. Spend: use a small, cheap model for the runs if the runner lets you choose, and say the cost.
- **If a guard refuses an edit, stop and report it.**
- No git writes. Run `formwork/fw test` and `formwork/fw check`.
- Report at `docs/reports/0026-measure-routing.md`: `## For you` first (at most 8 lines: the number, what failed, what was fixed), then details with each command and result. Last message: one line starting `result:`.
