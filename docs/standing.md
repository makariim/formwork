---
updated: 2026-10-17
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

**0.2.1 is what is on PyPI. 1.0.0 is built here and not published.** It
carries everything below. In it: a role's
`description`, `model`, `skills` and `color` now reach the generated Claude
Code agent instead of being dropped. And, from the first multi-repository use,
the human kept in the loop: `work-paired` allows one open brief by default and
refuses a brief marked done until its report carries the human's read-back. A
fourteenth core rule says the human is not the courier. See entry 14 of
`docs/dogfood.md`.

Also unreleased: the kit ships its first skill, `humanizer`, pinned at one
upstream commit in `formwork/skills/humanizer/`, placed into
`.claude/skills/` by `formwork roles`. `formwork/style.md` says text sent as
the human goes through it. Decision 0001, proposed.

Also in 1.0.0, from a clone on another machine, brought home as patches:
reports for two readers, `## For you` first, with a `report-shape` check; and
`sync`, which brings a project's kit copy up to date. `sync` now also runs
from the installed package, as `formwork sync`, pinned to the release, so no
other machine needs a clone. Decision 0002, proposed.

Three guards, thirteen checks, twenty eight roles, forty eight rules, one
skill, 486 tests across eight suites.

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

Two records in `docs/decisions/`, both `proposed`, waiting for him: 0001,
humanizer for text sent as the human; 0002, formwork is changed only here and
installed everywhere else. The decisions before it live in the design pages
in this folder, which are history and are not maintained.

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

Publish 1.0.0. Then other machines install it and drop their clones, as
decision 0002 proposes.

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
