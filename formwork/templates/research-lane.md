# Research round lane

Optional. One participant's file in a research round, when the answer is
unclear and costly to get wrong. The round itself runs as
[`../round.md`](../round.md) says: predictions first, then lanes, then the
record in [`round.md`](round.md).

Saved as `docs/rounds/<name>/<role>.md`, or `<role>-<label>.md` for a
relabel.

---

```markdown
# <Lane>: <the question this lane answers>

## Summary for cross reading
At most 20 lines. What the other lanes need from this one, so they can read
it without reading all of it.

## 1. The question, and why it matters here

## 2. Theory
What is known in principle. Sources linked.

## 3. State of the art
What others have built or measured. Sources linked, each with what it does
and does not show.

## 4. What it means here
The general answer applied to this product and this spec.

## 5. Proposals, ranked
Each with its evidence and its cost. The first is the recommendation.

## 6. Risks
What would make the top proposal wrong, and how we would find out.

NOT ESTABLISHED: anything this lane could not measure or source.
```

---

## After the lanes

1. **Cross reading.** Each lane reads the others' summaries and answers in
   its own file under `## After reading the others`.
2. **One integrator** writes the round record. Every position attributed.
3. **A challenger** reads the record cold and writes the case against it.
4. **The spec is updated** with what the round settled, and the open choices
   go to the person.
