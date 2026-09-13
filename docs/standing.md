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
session, a new `director` role that holds the upper layer, and briefs and reports as
files in `docs/briefs/` and `docs/reports/` with a check that catches work
marked finished that left no report. Twenty eight roles, eleven checks.

Still to do: how agents report to you, skills, model and effort per role, the
questions `formwork init` asks a first timer, and the settings section the
README does not have yet.

## What is decided

Nothing in `docs/decisions/`. The decisions so far live in the design pages in
this folder, which are history and are not maintained.

## What is open

Whether the kit should ship a standing brief for itself at all, or only the
template. This file is the experiment.

NOT ESTABLISHED: what a round costs in money. Nobody has measured it once.

NOT ESTABLISHED: whether any of this works for more than one person.

## What is next

How agents report to you: length, tone, and what a report always says.

Then skills, so the common jobs are one command instead of a paragraph.

## What we tried and stopped

Scrambling the contents of fixtures so a check could not recognise them. It
broke the checks that read filenames for real reasons. Recorded in
`formwork/limits.md` instead of papered over.

One fingerprint file for the whole machine. The second project on the same
machine got accused of tampering. Now one file per project.
