---
brief: 0035
stream: method
title: Build and measure operations, and a formwork everyone can navigate
status: done (accepted 2026-11-22)
starts: now
size: checkpoint
---

# 0035 Build and measure operations, and a formwork everyone can navigate

## His words (2026-11-22)

"can we update formwork with any missing structure we are using here that what's in the latest version of it? i mean i like this version here alot" and then: "go ahead, and let formwork work on its structure and reformat it if needed to be user friendly and be illustrative on the capabilities it can do, all of them, either everything is set up in its place like agents.md, rules, claude.md, or the rest, and also that whenever formwork is used in any project the user can navigate and understand through the readme, or the user can just ask the ai agent and the ai agents with everything setup as mentioned in claude.md and agents and rules and hooks and etc would be well knowing its capabilities and methods it can use to work, plan, execute, report and everything".

## Source of the practices

The health app's engine round, 2026-11-20 to 22: `<health-app>/docs/design/engine/decision-log.md` (50 rulings with evidence), `registry.md`, `scoring.md`, `docs/design/outside-views/round-plan-v1.1.md`, `docs/release-checklist-final.md`, the lane reports in `docs/design/engine/`, and the Director's memory notes on pacing, stuck workers, testing the build not the idea. Read them as a source only; never edit the health app.

## Part 1: add what is missing (formwork already has the research question card, 21 pitfalls and the evaluation plan; keep them)

1. **The ladder:** every part checked alone against its own set first, then joined one at a time; the perfect input diagnostic (gold inputs into the next part) to tell a reading fault from a building fault; "a lost test says this build, never the idea".
2. **The iteration loop with limits:** dev to fix, validation to re-measure, sealed once; a design call after 3 failed fixes of one defect class; model parts 3 revisions; a used set becomes dev.
3. **Spending in stages:** paid runs only after the free checks pass, each stage with a written entry condition and cost.
4. **The per route ship rule:** ship what clearly wins; non inferiority for small gains; fallback to the old path; deviations recorded openly.
5. **Frozen contracts with one owner:** shared definitions, fixtures and contract tests before parallel lanes; changes only through the owner.
6. **The director's decision log** (numbered rulings with evidence, lighter than decisions) and **the sourced release checklist** verified row by row by a checker that built nothing.
7. **Running many sessions safely:** never wait on another session's runs; status every 45 minutes when parallel; wake timers and a watchdog; one simulator and scratch folder per worker; never break the shared build; usage pacing (lighter models for workers, Codex for mechanical work); disk hygiene; a stuck worker is judged by its own outputs, not by busy status.
8. **Checks automatic tests miss:** an applied value check (a wrong value reported as success), scorer self tests with known good and bad answers, an independent re-check by a fresh session, scope freeze before release.
Deliver as method pages, templates (ladder plan, release checklist, decision log, parallel worker brief), new pitfalls where they fit, and role or skill updates, all in formwork's existing style.

## Part 2: make formwork navigable and self describing

- **A capability map:** one page (and a short README section) that lists everything formwork can do, with one plain example each: the method (briefs, reports, standing, decisions, rounds), the roles and packs, the skills, the taste packs, the research pack, the guard and checks, hooks, the adapters (Claude Code, Codex, Cursor, Gemini CLI), the CLI commands, and Part 1's operations.
- **In every project formwork installs into:** the generated `AGENTS.md`, `CLAUDE.md` (or the adapter's equivalent), rules and hooks tell the AI agent what formwork offers and when to use each piece (plan, research, build, measure, review, report, release), so a person can ask the agent "what can you do here?" and get a correct answer; and the project README section tells a person where to start.
- **Restructure if needed:** reorganise folders, file names and the README so a new person finds things fast; keep backward compatibility for installed projects (a migration note, `fw sync` handling) and keep every existing check green.
- Coordinate with brief 0034 (the research pack, open): no duplicate pages; Part 1 links to or extends 0034's method rather than repeating it.

## Rules

Plain words, no dashes in prose. Nothing protected is loosened without him; checks stay green (`./formwork/check/run` or `fw check`). No release, no version bump, no git (he commits). Report `docs/reports/0035-build-measure-and-map.md` with "For you" first. Do not set this brief to done.
