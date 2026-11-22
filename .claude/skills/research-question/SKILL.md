---
name: research-question
description: |
  Write a research question card with the person before any work starts, then
  check it against the research pitfalls. Use when a project wants to learn
  something by building and measuring: "is this better", "does this help",
  "should we keep this", "measure this", "run an experiment", "set a bar", or
  before any evaluation run that will decide something.
---

<!-- GENERATED FROM formwork/skills/research-question/SKILL.md — DO NOT EDIT. -->
<!-- Change the source and run formwork roles. A hand-edit here fails the gate. -->

# Research question

You help the person write one research question card, in the shape of
`formwork/templates/research-question.md`, and you check it before it is
committed. The method is `formwork/research/README.md`. The pitfalls are
`formwork/research/pitfalls.md`.

## Steps

1. **The question.** Ask what they want to know. Rewrite it as one sentence
   that can come out wrong. Read it back and get a yes.
2. **Why it matters.** Ask what they would do if the answer were yes, and if it
   were no. If both lead to the same action, say so and stop: the question is
   not worth a card.
3. **What is already known.** Search for prior work, inside the project and
   outside it. For each source, write one line on what it predicts here. Each
   prediction becomes a test or says why not (res-9).
4. **The hypothesis.** The expected answer, and the result that would refute
   it.
5. **The method.** What is built, what is measured, over which inputs, chosen
   how; the baseline and its effort (res-8); the real path or a proxy (res-13).
   If a measurement set is needed, fill in
   `formwork/templates/evaluation-plan.md` with them.
6. **The bar and its origin.** Ask where the number comes from. If they do not
   know, offer the four origins: a harm, a cost, a user need, or the measured
   noise. A guess is allowed, written as a guess (res-3).
7. **The sample.** Work out the smallest effect worth seeing, and the cases and
   runs per arm needed to see it. Show the working (res-4, res-11).
8. **Check before commit.** Read parts 1 to 7 against res-1 to res-10 of the
   pitfalls. Write each hit as `res-N: what, where`. The person fixes it or
   overrides it in one line with a reason.
9. **Registration.** Tell the person the card is ready to commit, and that the
   commit date is the registration. Never commit for them; git is theirs.

## After the run

When the person comes back with results, fill in parts 9 to 12 with them.
Check against res-11 to res-21. Every difference from the plan goes in part
10. A missed bar is reported as missed.

## Never

- Choose the bar after seeing a result.
- Report a number without the command that produced it.
- Edit parts 1 to 8 after the commit. A change is a deviation.
- Decide part 12. The decision is the person's.
