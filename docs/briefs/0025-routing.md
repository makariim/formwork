---
brief: 0025
stream: method
title: Routing one plain prompt
status: done (accepted 2026-11-15)
---

# 0025 Routing one plain prompt

## His words

"next" (2026-11-15): step 3 of the build plan in `docs/research/0022-whole-project-builds.md`. The most important requirement, in his words: "my claude.md and whatever becomes intelligent, and understand what needs to be done and which layer which role which hook and everything from just my prompt". His picks (0022 read-back): routing corrections live in a separate small file per project; the director routes; the kit ships a template for a person's own defaults.

## The job

Build step 3 exactly as the research describes ("The centre: understanding from one prompt", "What happens to one prompt", and part 4 step 3):

1. **The routing table**: a kit page (proposed `formwork/route.md`): the short named list of kinds (build a new product, change an existing one, fix, research, a deck or document, a question), each with its size test, template, team and stops. Default size is a task; step up only when the work grows.
2. **The director change**: the director role is the only router above a task; it reads the table, says the plan back in one or two plain lines (kind, size, team, first brief), then acts on it. The lead keeps running rounds.
3. **The project instruction template**: two lines a project's AGENTS.md or CLAUDE.md carries (read `docs/standing.md` and the routing table, say the plan back, act on its size), offered by `formwork setup`, never written over.
4. **The routing corrections file**: a small per project file (name it in the kit) where the director writes the person's corrections in their words, read before routing.
5. **The personal defaults template**: a kit page a person copies into their own global CLAUDE.md (who they are, defaults such as run alone, taste, how to talk), with at most one line pointing to formwork's routing in projects that have FORMWORK.md. No personal content in the kit.
6. Mark routing accuracy **NOT ESTABLISHED** on the routing page until step 4 measures it.

## Rules

- Generic only: the leak scan must stay green.
- **If the self protection guard refuses an edit, stop and report it.** Do not work around it.
- No git writes. Run `formwork/fw test`, `formwork/fw check` and `formwork roles` if a role changed; say that he re-records fingerprints after review.
- Report at `docs/reports/0025-routing.md`: `## For you` first (at most 10 lines, plain: how one prompt now flows, with two worked examples, one small and one big), then details. Last message: one line starting `result:`.
