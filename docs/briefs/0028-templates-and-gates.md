---
brief: 0028
stream: method
title: Optional templates and gates
status: done (accepted 2026-11-15)
---

# 0028 Optional templates and gates

## His words

"next" (2026-11-15): step 6 of `docs/research/0022-whole-project-builds.md`. Earlier: "i had to tell explicitly what is and whats not ai vibed, what do we need in each research, the research design implement verify cycle".

## The job

Build "Phases and gates" and "Templates" exactly as the research describes:

1. **Templates**, all optional, one page each, in `formwork/templates/`: spec, research round lane, design round, build, review round, release step (the general pattern only: another session owns the step, one written line starts it, never a schedule, stops at the first failure, ends with a release record; no machine, account or person). Headings are the ones the projects actually used; written generically.
2. **Phases** as a label on a run of ordinary briefs using the existing `stream:` field. No new process, no fixed order of phases.
3. **Gates**: the three `starts:` forms only (`starts: now`, `starts: after <stream>`, `starts: decision NNNN`), checked by a program (a check that refuses an open brief whose gate is not met). The two default gates for a build offered in the templates: no build brief before a spec is accepted; unproven items listed and seen before the next phase opens.
4. The routing table (`formwork/route.md`) offers the matching template by kind and size, never as a required sequence.
5. Fixtures for the gate check in must-pass and must-fail, generic.

## Rules

- Generic only; the leak scan stays green. Do not touch any other repository.
- **If a guard refuses an edit, stop and report it.**
- No git writes. Run `formwork/fw test` and `formwork/fw check`; say that he re-records fingerprints after review if needed.
- Report at `docs/reports/0028-templates-and-gates.md`: `## For you` first (at most 8 lines, plain), then details with each command and result. Last message: one line starting `result:`.
