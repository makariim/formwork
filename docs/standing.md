---
updated: 2026-09-13
by: the conversation that built the standing brief
---

# Standing brief

Live, not history. Everything else in this folder is the record of building the
kit and is left as written. This file describes the present and is rewritten.

## What we are building

Formwork. A forkable starter kit for running a project with coding agents: a
loop, a set of roles, rules that say what they catch, three guards that refuse,
and a gate of checks that shows itself failing as well as passing. It carries
nothing about anybody's product. It is the shape, empty.

## Where we are now

Version 0.1.0 is published on PyPI as `formwork-kit` and the repository is
public. Three guards, ten checks, twenty seven roles, forty seven rules, 295
tests across five suites.

Version two is being built. In: the standing brief, the two layer mechanism,
the `lead` role widened so it also splits a brief that is too big for one
session, a new `director` role that holds the upper layer, briefs and reports as files
in `docs/briefs/` and `docs/reports/` with a check that catches work marked
finished that left no report, one page saying how agents talk to you, and `formwork setup`, which asks a few
questions once and writes what they imply: the style file, the standing brief,
the three document folders and the strength values. Twenty eight roles, twelve checks, 328 tests.

Still to do: how agents report to you, skills, model and effort per role, the
questions `formwork init` asks a first timer, and the settings section the
README does not have yet.

## What is decided

Nothing in `docs/decisions/`. The decisions so far live in the design pages in
this folder, which are history and are not maintained.

Two people outside the project have now run it. One reported that the guards
held on the scenario in the README. That is the first evidence from anybody
who did not write it, and it is one person on one scenario, self reported.

## What is open

Whether the kit should ship a standing brief for itself at all, or only the
template. This file is the experiment.

NOT ESTABLISHED: what a round costs in money. Nobody has measured it once.

NOT ESTABLISHED: whether any of this works for more than one person.

Whether the `lead` may invent a role. Today the twenty eight are files, checked
for a unique job and five sections. Asked for by somebody who tried it: let the
lead make a role on the fly when a task needs one that does not exist. Open,
and it cuts across what `role-shape` is for.

## What is next

One aggressive audit pass over everything version two added, then release
0.2.0.

## What we tried and stopped

Skills, and a model and effort level per role. Both were planned for version
two and both were dropped before starting. The model one turned out to be
Claude Code only as far as anybody has checked, which makes it a smaller
feature than it sounded.

Scrambling the contents of fixtures so a check could not recognise them. It
broke the checks that read filenames for real reasons. Recorded in
`formwork/limits.md` instead of papered over.

One fingerprint file for the whole machine. The second project on the same
machine got accused of tampering. Now one file per project.
