---
brief: 0022
stream: method
title: Formwork for building a whole project
status: done (accepted 2026-11-15)
---

# 0022 Formwork for building a whole project

## His words

"launch a formwork session to research these ideas, and the mac air pipeline btw shouldnt be a persistent thing, remember, formwork itself is a general repo, and this research round get back to me with proposed new formwork or what should be added to formwork and how it becomes" (2026-11-15). The idea itself, in his words, is in `docs/ideas/2026-11-15-whole-project-builds.md`: formwork is very good at iterating on a task and managing the agent lifecycle; it should also handle building a whole project end to end, with many new roles spawned dynamically.

Runs alone, start to finish. Never stop to ask him. **Research and a proposal only: no changes to the kit** (`formwork/`, `formwork_cli/`, `FORMWORK.md`) in this brief.

## Evidence to read first

- This repository: `FORMWORK.md`, `docs/standing.md`, `docs/design.md`, `docs/gap-map.md`, `docs/survey.md`, the roles in `formwork/roles/` and packs, the checks in `formwork/check/`.
- Three projects that used formwork for whole products (read only; private data stays private, quote only method, never personal or health content):
  - `<health-app>`: `docs/product-spec.md`, `docs/briefs/` 0001 to 0005, `docs/reports/`, `docs/research/the-story.md`, `docs/design/round-2/director-ai-check.md`, `docs/review/round-1/findings.md`, `<health-app>/formwork/roles/project/`. Never open `docs/profile/`.
  - `<desktop-app>`: `docs/standing.md` (the last 60 entries), `docs/feedback.md`, a sample of briefs and reports from 0440 onward.
  - `~/Personal/Repos/ship-ai` and `~/Personal/Repos/studio`: their briefs and reports.

## The team (run as the `lead` role)

`researcher` (what other methods and tools do for whole products: product development frameworks, design sprints, stage gates, agentic coding frameworks and multi agent orchestrators, with sources), `architect` (where a project layer fits: over, under or beside the kit; what is fixed and what is generated), `product` (what a person building an app actually needs from it, from the three projects above), `record-keeper` (checks, gates and records a project layer would need, true to formwork's style), and `challenger` (the case for keeping formwork small and doing none of this).

## The most important requirement

His words: "most important, is that my claude.md and whatever becomes intelligent, and understand what needs to be done and which layer which role which hook and everything from just my prompt". So the centre of the proposal is **understanding from one prompt**: from a plain request ("build me an iPhone app for X", "fix this bug", "research Y", "make a deck"), the setup works out on its own the kind of work, the layer and phase it belongs to, which roles to bring in or create, which templates, checks and hooks apply, and which briefs to write, then says that plan back in one or two plain lines and runs it. Cover: where that understanding lives (the user's CLAUDE.md, the project's AGENTS.md, a formwork router or skill, the director role), how it stays right as projects grow, how a person corrects it, and how it avoids over building small asks (a task sized job keeps a one line brief).

## What to answer

1. **What is missing**, with evidence from the three projects: every place the person had to supply method by hand (phase cycle, research round shape, taste and anti AI slop rules, user first story, review rounds on the running product, dynamic roles, usage awareness).
2. **The proposal**: what formwork becomes. Options at least: (a) a new layer ("project" or "product") over the brief cycle; (b) a pack of roles, templates and checks; (c) a change to the director and lead roles only; (d) nothing, with the reason. For the recommended one: the files and folders it adds, the phase model and its gates, the templates (spec, research round, design round, build, review round, release), how **dynamic roles** are generated and checked (the five section format), the taste checklists as optional packs per product kind, and the checks that enforce it.
3. **What stays out**: anything personal or machine specific (his release machine, his accounts, his devices) stays in projects, never in formwork, which is a general repository.
4. **How it would be built**: a short ordered plan of briefs, smallest useful first.

## Rules

- No edits to the kit. Write `docs/research/0022-whole-project-builds.md` (the full research) and the report.
- Sources for every claim about other tools. NOT ESTABLISHED when unknown.
- No personal or health data from other projects in anything written here.
- Report at `docs/reports/0022-whole-project-builds.md`: `## For you` first (at most 12 lines, plain: what formwork would become, the recommended option, what it adds, what stays out, the first step), then the details. Last message: one line starting `result:`.
