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

**0.1.0 is what is on PyPI. 0.2.0 is ready and not released**, and until it is,
the README describes commands a reader cannot install.

Three guards, twelve checks, twenty eight roles, forty seven rules, 356 tests
across six suites.

Version two added: the standing brief and its check, a `director` role holding
the upper layer, `lead` widened to split a brief as well as run a round, briefs
and reports as numbered files with a check that catches work marked finished
that left nothing behind, one page saying how the agents talk to you, and
`formwork setup`, which asks eleven questions once and writes what they imply.

**Then five audits attacked it and found 71 defects**, nearly all in what had
just been written. The serious ones are fixed: `setup` no longer edits the
section it promised never to touch, no longer reads Ctrl-C as consent, and no
longer overwrites a file made while it was asking; `install` refuses rather
than wiring the wrong project; and the three new checks no longer report clean
while examining nothing. Every fix carries a test or a fixture that fails
without it.

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
