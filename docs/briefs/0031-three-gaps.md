---
brief: 0031
stream: method
title: Three gaps from the catalogue check
status: done (accepted 2026-11-15)
starts: now
---

# 0031 Three gaps from the catalogue check

## His words

"queue 1 to 3" (2026-11-15), on `docs/research/ecc-gaps.md` gaps 1 to 3.

## The job

1. **Bringing in a third party skill** (gap 1): a kit page, and a template, for how a project brings in someone else's skill, following what the kit already does for its one vendored skill (`formwork/skills/humanizer/UPSTREAM.md`): source repository and commit, licence file kept, sha256 of each file, "nothing updates on its own", and where it lives in a project. Optional: a check that a vendored skill folder carries its UPSTREAM record (fixtures must-pass and must-fail), if it fits the kit's style.
2. **Two report lines for a split build** (gap 2): "touched outside my files" and "packages added, with licence and source", added to the build template and the lead's instructions for builders' final messages.
3. **Localisation and right to left layout** (gap 3): name it in an existing role's `owns` (the research's recommendation; most likely `writer` for words in every language and `visual` or `frontend`/`mobile` for mirrored layout), with "Does not own" lines kept consistent. No new role.

## Rules

- Generic only; the leak scan and hidden-unicode stay green. Do not touch any other repository.
- **If a guard refuses an edit, stop and put every protected change in one patch file** (`docs/reports/0031-three-gaps.patch`), as 0030 did.
- No git writes. Run `formwork roles`, `formwork/fw test` and `formwork/fw check`.
- Report at `docs/reports/0031-three-gaps.md`: `## For you` first (at most 6 lines, plain), then details. Last message: one line starting `result:`.
