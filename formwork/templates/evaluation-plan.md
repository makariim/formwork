# Evaluation plan

Optional. Goes with a research question card
([`research-question.md`](research-question.md)) when the question needs a
measurement set. Committed with the card, before any run. Each part names the
pitfall it guards against, from [`../research/pitfalls.md`](../research/pitfalls.md).

Saved beside the card as `<short-name>-evaluation.md`.

---

```markdown
# Evaluation plan: <question>

## Sets
| Set | Size | Written by | Labelled by | Settled by | Real or synthetic | Split (dev, validation, sealed) |
|---|---|---|---|---|---|---|

Real data share: <how much of any set comes from real use. Zero is allowed, and
it goes on every result> (res-6)

## The answer key
Who wrote the gold answers, and with what expertise. How a sample of them will
be audited blind before scores are trusted. (res-1, res-15)

## Agreement
The statistic (Cohen's kappa, Krippendorff's alpha), the fields it covers, and
what level is required before the labels are used. (res-2)

## Judges
Model family at each stage: writing, answering, judging. Control items per
judge run, and how many are needed to resolve the judge's rule. A human sample
checked against the judge. (res-4, res-7)

## Instrument check
Known answer cases fed to the scorer and the prompt before results, including
cases built to fail. What the metric can and cannot show. (res-14)

## Baseline
What it is, what tuning it got, and whether the tasks were written before the
new design. (res-8)

## Runs and sample size
Runs per arm. Cases per set. The smallest difference each bar can resolve at
that size, and how it was worked out. (res-4, res-11)

## Looks at the data
How many times each set may be scored before the final run. Which set is kept
untouched until the end. (res-12)

## Real path or proxy
Which results come from the real path. If a proxy is used, the check that it
agrees, and what happens to the plan if it does not. (res-13)

## Kept
Where raw outputs, judge outputs, traces and the scoring code are saved, by
path, for every result. (res-16)

## Cost
The budget, and what happens when it runs out before the registered runs are
done. A run cut short is a deviation, not a result. (res-19)
```
