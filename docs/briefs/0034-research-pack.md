---
brief: 0034
stream: method
title: The research pack: a method for research by building, with its pitfalls
status: open, 2026-11-21
starts: now
size: checkpoint
---

# 0034 The research pack

## His words (translated)

"Extract the research machinery into formwork (skills, templates, roles), like the UI best practices, plus a page about formwork in its new shape." Approved to run without him overnight on 2026-11-20.

## Goal

Formwork already has a researcher role that says: write the bar first, carry the command, record failures. What it lacks is the method around a whole research question, and the list of the ways such work usually goes wrong. One project's four months of research by building, reviewed against how labs work, showed the same gaps again and again: agreement measured instead of correctness, gates with no origin, one run per arm, synthetic data only, a registration nobody can date, no outcome measure. This brief puts the method and those pitfalls into the kit, in the same shape as the taste packs.

If we do not do this: every project rebuilds a research method from scratch and falls into the same holes.

## Scope (new files unless marked)

- `formwork/research/README.md`: the research pack. A question card, the loop from question to decision, how it maps onto a brief and a round, how a project names and overrides it, and what it cannot do.
- `formwork/research/pitfalls.md`: items `res-1` to `res-N`, in the taste pack shape (Catches, Detected, a hint, Source). Generic; each item cites a public method source.
- `formwork/templates/research-question.md`: the question card, written before any work.
- `formwork/templates/evaluation-plan.md`: for a measurement: the gold set and where it came from, splits, runs, agreement statistic, sample size, judge controls, baseline parity, registration.
- `formwork/skills/research-question/SKILL.md` and `UPSTREAM.md` (`written here, no upstream`): a skill that writes the card with the person, and checks it against the pitfalls.
- `formwork/roles/method/researcher.md` (edit): point to the pack in "Read first".
- `README.md` (edit): one row for `research/` in the kit index.
- Generated role files, by `formwork/fw roles` if the generator needs to rerun.

**Out of scope:** any check (the gate folder is protected, and a pack is never a check), other roles, the taste packs, releases, other repositories except reading the source project's research notes.

## Must not happen

No git writes. Nothing personal or product specific in kit files (the leak scan). No dashes. A pitfall is listed only with a public source. If the guard refuses a file, stage the change in `docs/reports/0034-research-pack.patch`.

## Done when

The files above exist; `formwork/fw check` and `formwork/fw test` were run and their results are reported exactly; every pitfall item has Catches, Detected and Source. Known before starting: `work-paired` allows one open brief by default and 0033 is still open waiting for his read back, so the gate is expected to be red on that check alone.

## Report

`docs/reports/0034-research-pack.md`, `## For you` first. His read back is pending.
