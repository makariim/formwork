# Ladder plan

Optional. For a thing built from parts: the order in which each part is
checked alone, then joined. The method is the ladder in
[`../operations/README.md`](../operations/README.md). Read the "before"
pitfalls in [`../operations/pitfalls.md`](../operations/pitfalls.md) first.

Saved as `docs/plans/<short-name>-ladder.md`, or inside a phase brief. Written
before the first part is measured. A change afterwards is a deviation, written
at the bottom.

---

```markdown
# Ladder: <what is being built>

## Baseline
What every later number is compared with, and the command that measures it.

## The parts, each alone

| Part | Its own set (size, where it came from, hash) | Its bar, and where the bar comes from | Smoke cases | Result alone, with the command |
|---|---|---|---|---|
| | | | | |

## Perfect input diagnostics
For each part after the first: the run that feeds it the gold output of the
part before it.

| Part | Gold input from | Result on gold | Result on the real input | Fault is in |
|---|---|---|---|---|
| | | | | reading / building |

## Join order
1. The first vertical slice, end to end: which parts.
2. Cost and speed smoke test on that slice: budget, result.
3. Each next join, one part at a time.

## Limits (the iteration loop)
Write your own numbers. The defaults are in `formwork/operations/README.md`.
- Sets per part: dev, validation, sealed. Who may read what.
- Failed fixes of one defect class before a design call:
- Measured revisions for a part driven by a model:
- Iterations for the final measure:

| Defect class | Fix 1 | Fix 2 | Fix 3 | Design call |
|---|---|---|---|---|
| | | | | yes / no, ruling |

Sets marked spent (now dev): set, date, why.

## Known bugs carried into each joined result
| Join | Known bugs |
|---|---|

## The wording
Every end to end result reads: "this build scored X, carrying bugs Y". Never
"the idea fails".

## Deviations
```
