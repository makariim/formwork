---
brief: 0027
stream: method
title: Specialists cheaply
status: done (accepted 2026-11-15)
---

# 0027 Specialists cheaply

## His words

"b, everything is already working, no need to disrupt them now" (2026-11-15): continue the kit's plan, step 5 of `docs/research/0022-whole-project-builds.md`, without touching his projects. His pick from 0022: roles may be created mid project, by the relabel first path.

## The job

Build "Dynamic roles" exactly as the research describes (three tiers):

1. **Relabel** in the lead role: the lead may spawn an existing role with a title line and, optionally, a skill; its owns, sections and tools still come from its checked file.
2. **New project role**: only when no existing `owns` covers the work. The director drafts it in the brief in the five section format; the person's go accepts it; a working session writes it to the project roles folder and runs `formwork roles` and `formwork check`; then the lead may spawn it. Write this path into the director and lead roles and FORMWORK.md.
3. **Never** a pasted persona or a general agent given a role body in a prompt: say so in the lead.
4. **Checks**: a round participant file must be `<role>.md` or `<role>-<label>.md` for a real role; a role named in a brief's team table must exist. Fixtures in must-pass and must-fail, generic.
5. **The template line**: a role that touches plans or order names the director and lead under "Does not own" (add to `formwork/roles/TEMPLATE.md`).
6. Write down plainly, as NOT ESTABLISHED, whether a role written mid session can be spawned in the same session; if it cannot, adding a role is its own task brief.

## Rules

- Generic only; the leak scan stays green. Do not touch any other repository.
- **If a guard refuses an edit, stop and report it.**
- No git writes. Run `formwork roles`, `formwork/fw test` and `formwork/fw check`; say that he re-records fingerprints after review if kit-integrity needs it.
- Report at `docs/reports/0027-roles.md`: `## For you` first (at most 8 lines, plain, with one worked example of each tier), then details with each command and result. Last message: one line starting `result:`.
