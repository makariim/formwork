# Build plan

**Phase:** K7, planned. **Date:** 2026-09-12.

The order the kit gets written in. Nine build steps, one research step, one
measurement step.

**This document authorises nothing.** Each step is authorised separately, one at
a time.

## The rule this plan is built around

**Get the kit running on itself as early as possible.**

Steps 1 and 2 build the two things that make the kit usable: a check that can
fail, and a boundary that refuses. From step 3 onward, every step is done *using
the kit*, and what breaks gets written down.

That is K8, and it starts on step 3 rather than at the end. A kit tested only
when finished has already set its mistakes in concrete.

## Every step answers four questions

Produces · needs first · who authorises · what would tell us it failed.

The founder authorises every step. That is not repeated below.

---

## R1 — How the other runtimes declare a role

**Produces.** A short document: how Codex, Cursor and Gemini CLI expect a role
and a skill to be declared. Folder, filename, frontmatter, how a tool grant is
written. Each answer cited from the publisher's own documentation.

**Needs first.** Nothing.

**Fails if.** An answer comes from memory rather than a cited page. A runtime is
guessed at rather than marked unknown.

**Why it is first.** Step 7 cannot start without it, and it needs no code.

---

## B1 — The gate

**Produces.** `formwork/check/run`, the one command. The rule that a check ships
with an input that breaks it. One real check, to prove the shape works. A test
that shows the gate red and green.

**Needs first.** Nothing.

**Fails if.** The gate cannot be made to fail. A broken fixture passes and
nothing notices. A missing check reads as success.

---

## B2 — The boundary, and the first adapter

**Produces.** The program that refuses version-control writes. The Claude Code
wiring. Proof it refuses, and proof it lets reading through.

**Needs first.** B1.

**Fails if.** It refuses reads as well as writes. It can be talked out of it. It
passes when the hook is not installed at all.

**This is the point the kit becomes real.** One rule, enforced, watched working.

---

## B3 — The rules

**Produces.** `FORMWORK.md`, one page. `rules/core.md`, thirteen. `rules/full.md`,
thirty-three. Every rule carries what it catches, and says whether it is enforced
or advice.

**Needs first.** B2.

**Fails if.** A rule has no line saying what it catches. A rule is neither
enforced nor labelled advice. The one page runs past one page.

**K8 starts here.** This step is done using the kit, and what breaks is recorded.

---

## B4 — The loop and the paperwork

**Produces.** `loop.md`. Four templates: brief, report, decision, round. The
decision and round templates follow the published shapes named in the gap map,
rather than new ones.

**Needs first.** B3.

**Fails if.** The smallest size of work produces paperwork longer than the work.
A template is invented where one was already adopted.

---

## B5 — The team

**Produces.** `TEMPLATE.md` with its five required sections. Six method roles.
Twenty-one pack roles. A check that refuses to load a role missing a section.
`HOW-TO-ADD-A-ROLE.md`, including converting one from a public catalogue.

**Needs first.** B3.

**Fails if.** A role is missing a section and still loads. Two roles own the same
thing. A role in the software pack is needed by a project that has no code.

---

## B6 — The rest of the enforced rules

**Produces.** The remaining checks, so that nine rules are enforced rather than
two: the gate named and not substituted, the refusal budget, brief references
resolved, regeneration byte-identical, identifiers computed, predictions written
first.

**Needs first.** B1, B5.

**Fails if.** An enforced rule has no check behind it. A check has no failing
input. The budget can be exhausted without anyone being told.

---

## B7 — The other three runtimes

**Produces.** The generator that writes per-runtime role files from one source.
Adapters for Codex, Cursor and Gemini CLI. A label on each: tested, untested,
partial, or incompatible.

**Needs first.** R1, B5, B6.

**Fails if.** An adapter is labelled tested without anyone running it.
Regenerating produces a different file than last time. A hand-edit to a
generated file survives.

---

## B8 — Day one

**Produces.** The installer. The mode that runs the failing fixtures on demand.
`COSTS.md`. The fifteen-minute first run, start to finish.

**Needs first.** B2, B3, B4, B5.

**Fails if.** Install needs a clean working tree, moves a file, or demands a
document. The first run takes materially longer than fifteen minutes. It cannot
run on a project that already has work in it.

**Open question this step must answer.** On a runtime that cannot block, steps 1
and 2 of the first run do not happen. What those users see instead is NOT
ESTABLISHED and K6 left it here.

---

## M1 — What a round costs

**Produces.** One number, with the command that produced it: what one round
costs in money. Recorded in `COSTS.md`.

**Needs first.** B5.

**Fails if.** The figure is estimated rather than read from the runtime's own
reporting. It is quoted without the size of round it came from.

**Why this is a step of its own.** K4 and K5 both recorded this as the most
important missing number, and neither could supply it. Until it exists the kit
tells people a round is expensive and cannot say how expensive.

---

## B9 — Publish

**Produces.** A rewritten README. A final run of both privacy gates. The
repository made public.

**Needs first.** everything above.

**Fails if.** A gate is red. A claim in the README is stronger than the evidence.
The blind reader test has not been re-run since the kit files were written.

**The founder does every commit and the publish.** No agent touches it.

---

# The order

```
R1 ──────────────────────────────┐
                                 │
B1 ──▶ B2 ──▶ B3 ──▶ B4 ──┐      │
               │           │      │
               └──▶ B5 ────┼──▶ B6 ──▶ B7 ──┐
                    │      │                │
                    │      └──▶ B8 ─────────┼──▶ B9
                    └──▶ M1 ────────────────┘
```

R1 can run at any time and blocks only B7.
M1 can run at any time after B5.

**K8 runs from B3 onward** — the kit builds itself, and every failure is written
into `docs/dogfood.md` as it happens, not afterwards.

---

# What would tell us the whole phase failed

- **Nothing broke.** The kit used on a new kind of project with no friction was
  not really used. K8 says this and it is the condition that matters most.
- Friction was found and fixed quietly, without being recorded.
- A step was skipped because it looked obvious.
- The kit was finished and then tested.

# What could not be established

- **How long any of this takes.** No step has an estimate, because there is no
  basis for one. A number here would be a guess wearing a schedule's clothes.
- **Whether the order is right.** The dependencies are real; the sequencing
  between independent steps is a judgement.
- **Whether nine steps is the right number.** It is not compared against any
  alternative.
