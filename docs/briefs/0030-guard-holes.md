---
brief: 0030
stream: method
title: Close two guard holes
status: done (accepted 2026-11-15)
starts: now
---

# 0030 Close two guard holes

## His words

"next" (2026-11-15), after choosing to add the ECC ideas as small steps (`docs/research/ecc-ideas.md`, ideas 5 and 6, the smallest first; ideas 1 and 2 follow as their own briefs).

## The job

1. **Linked protected files** (ECC idea 5): the protected files guard refuses an edit when the target is a symbolic link to a protected file, or a file with more than one hard link where any link is protected. This closes the hole `formwork/limits.md` lists as open. Write the logic in formwork's own words (ECC is MIT; ideas only, no copied code).
2. **Hidden unicode** (ECC idea 6): a new check that scans kit text files (and the files the kit generates, like role files) for zero width characters and bidirectional control characters, so a role or rule file cannot carry invisible instructions. Kit style: CATCHES, CANNOT TELL, fixtures in must-pass and must-fail, shown to reject the wrong and accept the right.
3. Update `formwork/limits.md`, COSTS.md and the glossary as the kit expects.

## Rules

- Generic only; the leak scan stays green. Do not touch any other repository.
- **If a guard refuses an edit, stop and report it.** (This brief changes a guard: expect refusals on existing files; stop and give him the exact change to make.)
- No git writes. Run `formwork/fw test` and `formwork/fw check`; say that he re-records fingerprints after review.
- Report at `docs/reports/0030-guard-holes.md`: `## For you` first (at most 6 lines, plain), then details. Last message: one line starting `result:`.
