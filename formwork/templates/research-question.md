# Research question

Optional. One card per research question, written before any work. The method
is in [`../research/README.md`](../research/README.md). Read the pitfalls in
[`../research/pitfalls.md`](../research/pitfalls.md) before committing it.

Saved as `docs/research/questions/<short-name>.md`, or as a round's `brief.md`
when the question is a round. A brief points to it.

**Parts 1 to 8 are committed before anything runs.** The commit date is the
registration. Parts 9 to 12 are filled in afterwards, below a line, and the
parts above the line are never edited after the commit. A change to the plan is
a deviation, written in part 10.

---

```markdown
# <the question, in a few words>

## 1. The question
One sentence that can come out wrong.

## 2. Why it matters
What we do if the answer is yes. What we do if it is no. If both answers lead
to the same action, stop here.

## 3. What is already known
The prior work read, each with one line on what it predicts here.
Each prediction becomes a test in part 5, or says why not.

## 4. The hypothesis
The expected answer. The result that would refute it.

## 5. The method
What is built. What is measured, in what unit, over which inputs, chosen how.
The baseline, and the effort it got. Which path (real or a proxy) produces the
numbers that count. The evaluation plan, if there is one:
`formwork/templates/evaluation-plan.md`.

## 6. The bar, and where it comes from
The number that separates pass from fail. Its origin: a harm, a cost, a user
need, or the measured noise. "A guess" is allowed, written as a guess.

## 7. The sample, and why that size
The smallest effect worth seeing. How many cases and runs per arm are needed to
see it, and how that was worked out (a formula, a simulation, or a pilot).

## 8. Registration
Committed in <commit> on <date>, before any run.

---

## 9. The result
Every number with its command. The middle and the bad end. Split by kind and by
judge where they differ.

## 10. Deviations
Everything that differed from parts 1 to 8, plainly. "None" if none.

## 11. Threats to validity
- Internal: could something other than the change explain the result?
- External: would it hold on real users and real data?
- Construct: does the measure track what matters?
- Statistical: is the sample big enough, and how many comparisons were made?

## 12. The decision, and who hears
Keep, change or drop, decided by the person. Who outside the work reviews the
finding, and when.

NOT ESTABLISHED: what this question could not settle.
```
