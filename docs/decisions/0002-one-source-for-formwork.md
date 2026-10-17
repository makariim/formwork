---
status: accepted
date: 2026-10-17
deciders: [the maintainer]
consulted: []
informed: []
---

<!-- Proposed by an agent. It becomes a decision when the maintainer changes
     the status to accepted. Until then nothing here is decided. -->

# 0002. Formwork is changed in one place, and installed everywhere else

## What made this a decision

A second machine held a clone of this repository and was using it. Two
commits were made in that clone and existed nowhere else. They were brought
back here as patches. Keeping a clone on every machine that uses the kit makes
every one of them a place the kit can be changed without anyone here knowing.

## What matters here

- One history for the kit. A change made on another machine cannot be lost or
  left behind.
- Every project says which kit it carries, as a release number, so two
  projects can be compared without reading files.

## Options we looked at

- **Released versions everywhere else.** Changes happen only in this
  repository; other machines run `pipx install formwork-kit==X.Y.Z` and
  `formwork sync` inside each project.
- **A clone on each machine, pulled before use.** Always current, but every
  clone is somewhere a commit can be made, which is how the two stray commits
  came to exist.
- **Keep things as they are.** Each machine's clone drifts on its own.

## What we chose, and why

Proposed: **released versions everywhere else.**

1. Formwork is changed only in this repository.
2. Every other machine installs a released version:
   `pipx install formwork-kit==X.Y.Z`, or `python3 -m pip install --user`
   where there is no pipx.
3. A repository gets its kit from the installed tool: `formwork init` the
   first time, `formwork sync` after each upgrade. The project's SOURCE.txt
   names the release.
4. A clone of formwork on another machine is never committed to. Reading one
   is fine. A change wanted there is written down and made here.

`formwork sync` running from the installed package arrived with 1.0.0. Before
that, `sync` ran only from a git clone, so this rule could not have been
followed.

## What follows

**Good:**
- One history. Nothing waits on another machine to be noticed.

**Bad:**
- A fix needed on another machine is a release: change here, publish, install
  there. Minutes, where a local edit was seconds.
- Every release is public on PyPI. Something not ready for others cannot be
  tried elsewhere by installing it.
- Nothing enforces rule 4. It is advice. A clone on another machine can still
  be committed to.

## What would make us revisit this

A change needed on another machine waits for a release often enough to
matter. Or a second person works on formwork, and "only in this repository"
stops describing where changes are made.
