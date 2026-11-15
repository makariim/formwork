---
brief: 0023
stream: method
title: The checks see where projects work
status: done (accepted 2026-11-15)
---

# 0023 The checks see where projects work

## His words

"take your picks, start step 1" (2026-11-15), on the proposal in `docs/research/0022-whole-project-builds.md` (step 1 of part 4). His picks for the open questions, for later briefs: routing corrections in a separate small file per project; the director routes; roles may be created mid project by the relabel first path; the kit ships a template for personal defaults; steps 1 to 4 before publishing 1.0.0.

## The job

Step 1 of the build plan, exactly as the research describes it (read part 1 "What is missing" and part 4 step 1):

1. Widen `predictions-first` so it sees rounds in the folders projects really use, not only `docs/rounds/`.
2. Widen `standing-current` so it notices a standing page that has fallen behind the briefs and reports (for example a "next" that names a brief already done).
3. Make `open_briefs` count per stream where a project declares streams, so a project with several streams can follow the one open brief per stream rule and the check sees a breach.
4. Fix the COSTS.md count the research named.
5. Each change with fixtures made from the real shapes seen in the four projects, **written generically** (no project names, no personal data), in `must-pass` and `must-fail`, and the check shown to reject the wrong and accept the right.

## Rules

- Change only what these four items need. No routing, roles, templates or packs yet.
- Run `formwork/fw test` and `formwork/fw check`. Kit fingerprints were never recorded on this machine (`kit-integrity --record .`); do not record them yourself: say in the report that he runs `formwork/check/checks/kit-integrity --record .` once after reviewing the change.
- No git writes. Report at `docs/reports/0023-checks-see-projects.md`: `## For you` first (at most 8 lines, plain), then details with each command and its result. Last message: one line starting `result:`.
