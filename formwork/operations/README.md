# The operations pack

Optional. For a project that builds something in parts, measures it, and
ships it, often with several sessions working at once. The research pack
([`../research/README.md`](../research/README.md)) says how to ask a question
and judge the answer. This pack says how to run the build and the measuring
day to day: in what order to test the parts, when to stop fixing, when to
spend money, what ships, and how many sessions share one tree safely.

**The pack is never a check.** No program here judges a ladder, a ship call or
a worker. The pitfalls in [`pitfalls.md`](pitfalls.md) are for the person, the
`director`, the `lead`, the `tester`, the `reviewer` and the `record-keeper`
to look with.

**Source.** One project's three day build and measure round: one director,
four to six worker sessions, about fifty numbered rulings, three paid stages
and a release checked row by row. The numbers below are the defaults that
round used. They are starting points; a project writes its own in its plan,
before it starts.

---

## What is here

| Part | Page or template | Use it when |
|---|---|---|
| The ladder | this page; [`ladder-plan.md`](../templates/ladder-plan.md) | a thing is built from parts, and you are about to test it end to end |
| The iteration loop with limits | this page | you are fixing a part and measuring it again |
| Spending in stages | this page; the budget per run sits in the cost section of [`evaluation-plan.md`](../templates/evaluation-plan.md) | a measurement costs money |
| The per route ship rule | this page | the new thing wins in some places and not others |
| Frozen contracts with one owner | this page | two or more lanes will build against shared definitions |
| The decision log | this page; [`decision-log.md`](../templates/decision-log.md) | a director makes rulings between lanes faster than decisions can be written |
| The sourced release checklist | this page; [`release-checklist.md`](../templates/release-checklist.md) | anything is about to ship |
| Checks automatic tests miss | this page | before any result is believed, and before release |
| Running many sessions | [`parallel.md`](parallel.md); [`parallel-worker-brief.md`](../templates/parallel-worker-brief.md) | two or more sessions work at once |
| The pitfalls | [`pitfalls.md`](pitfalls.md), `ops-1` to `ops-14` | before a plan is set, and before a result or a release is reported |

---

## The ladder

**Every part is checked alone, against its own small set, before any parts are
joined.** Then they are joined one at a time. The first join is one thin slice
from end to end; then it widens.

The rungs, in order:

1. A baseline, so every later number has something to beat.
2. Each part alone, on its own gold set, with its own bar and a few obvious
   smoke cases.
3. **The perfect input diagnostic.** Feed the next part perfect inputs (the
   gold answers of the part before it). If it still fails, the fault is in
   that part's building. If it passes on gold and fails on the real output of
   the part before, the fault is upstream, in the reading. The research pack
   names the same move "oracle or headroom analysis"
   ([`../research/README.md`](../research/README.md), the method names).
4. One vertical slice joined from end to end.
5. A cost and speed smoke test on that slice.
6. Wider joins, one part at a time.
7. The final measure, on a set nobody has seen.

**A lost test says this build, never the idea.** Every end to end result is
written as "this build scored X, carrying these known bugs". A design counts
as tried only when its parts first passed their own checks. A whole chain that
loses before that has tested nothing but its bugs.

**A ladder step never decides shipping.** Its sets are small and its interval
is wide. In the source round, 150 items run twice gave about plus or minus 7
points. Ladder steps tell you where to look; the final measure decides.

Plan it in [`../templates/ladder-plan.md`](../templates/ladder-plan.md).

---

## The iteration loop with limits

Every measured part has three sets, and each set has one job:

| Set | Job | Who may read the items |
|---|---|---|
| dev | fixing | anyone |
| validation | measuring again after a fix | nobody; scores only |
| sealed | the final measure, used once | nobody until the gate |

**The limits, written in the plan before the first fix:**

- **3 failed fixes of one defect class, then a design call.** When the same
  kind of fault survives three fixes, stop patching. The fourth attempt is a
  change of design. The director proposes it with the evidence; the person
  decides it, as with any choice of direction.
- **3 measured revisions for a part driven by a model** (a prompt, a judge, a
  reader). After three, the question moves: to the answer key, the bar, or the
  design. Not to a fourth revision.
- **2 iterations for the final measure.**
- **A used set becomes dev.** A validation set read during error analysis
  counts as read. Fresh evidence needs a fresh set. Fixing on the test set is
  `res-12` in the research pack.
- Past failures go into a regression suite. They guard; they never count as
  evidence.
- A part that still misses after its limit stops only the routes that depend
  on it.

---

## Spending in stages

**Paid runs start only after the free checks pass.** Paid work is split into
stages. Each stage has, in writing before it opens: an entry condition that
can be measured, the steps it covers, a cost forecast, a contingency, and a cap
per run with what happens at the cap.

- The entry condition is checked by somebody who did not build the thing,
  re-running the free gates from their commands (see "an independent re-check"
  below).
- Funding is asked for one stage at a time, never the whole plan at once.
- "Ahead" means the paired lower bound is above zero, not the point estimate.
  In the source round, with no true gain the point estimate came out ahead in
  about half of simulated runs, and the lower bound in about 2 to 3 percent.
- A run that stops at its cap says how many items did not run. A run cut short
  is a deviation (the evaluation plan's cost section; `res-19`).

The forecast and the actual spend sit side by side in the report.

---

## The per route ship rule

Decide shipping route by route, never all or nothing. A route is any path the
product takes for one kind of input.

| The route | Ships? |
|---|---|
| clearly wins, passes its bars, no integrity defect | yes, on the new path |
| ahead on the point estimate, no worse on any safety or integrity check, paired lower bound no worse than the stated non inferiority margin | yes, as a small gain |
| has any integrity defect (a wrong result reported as success) | no. Held, fixed, measured again on fresh items |
| loses, or misses the margin | no. The old path stays |

- **Every shipped route keeps a fallback** to the old path on any failure.
- **The non inferiority margin is written before the measure.** The source
  round used minus 5 points on the paired lower bound.
- **A deviation is recorded openly, and the person makes it.** Shipping a
  route that missed a registered bar is the person's decision, written in
  those words (the research pack, step 8 of the loop; `res-19`). The
  director's log records the recommendation and the evidence behind it.

---

## Frozen contracts with one owner

Before lanes work in parallel, freeze what they share: schemas, generated
types, shared fixtures, and the contract tests. **One owner** holds them.

- Every rule in a contract has a valid fixture and a planted fault fixture
  that expects an exact error.
- A hash of the frozen files makes a silent change visible.
- A change goes through the owner and arrives whole: the schema edit, the
  regenerated code, the new fixtures, every suite green, and a line to the
  director.
- A lane that finds a gap sends it to the owner. It never patches around it
  locally.
- Gold data is fixed by a rule, never by editing one item by hand.

---

## The decision log

**Lighter than a decision, heavier than a chat.** A director running several
lanes makes rulings every hour inside a direction the person already set:
hold this route, use that set, measure this again.
Anything that changes the direction, ships past a bar, or spends money not
yet approved is the person's, and the log points to their decision. Each is a numbered row with its evidence, in one file, newest last. It
is the thread between lanes; each lane's own work stays in its report.

A ruling that changes the project's direction still becomes a decision in
`docs/decisions/`, written by the human. The log is the director's record, not
the human's.

Template: [`../templates/decision-log.md`](../templates/decision-log.md).

---

## The sourced release checklist

Every row of release scope names its source: a ruling, a report, a fix round,
or the human's words. **A checker that built none of it** verifies each row on
a fresh release build and marks it pass, fail, or not testable here, with the
evidence. Nothing ships with a fail. A real limit is carried into its row,
never dropped.

Template: [`../templates/release-checklist.md`](../templates/release-checklist.md).
The `record-keeper` (or the `tester`) is the checker, because the check means
building and running things; the `reviewer` reads only, so it cannot. Never a
role that built the release.

---

## Checks automatic tests miss

**An applied value check.** For every change the product says it made, read
the value at the place it addressed and compare it with what was asked. Three
results, kept apart: ok; wrong value applied (an integrity defect); not
applied. A test that checks the reply said "done" misses the second one
entirely.

**Scorer self tests.** Before trusting a scorer or a judge, feed it the gold
itself and expect full marks; feed it planted faults and expect them caught.
The source round voided a judge run that caught under 95 percent of its planted
faults. This extends `res-14` (the instrument is never tested).

**An independent re-check.** A fresh session that built nothing re-runs every
gate from its commands, never from the lane reports, and lists contradictions
first. Before any spend, and before any release.

**An artifact audit.** Before believing a comparison, read a sample of failures
and ask: real, or the harness? A check that fails on every item of one kind is
usually the harness.

**Scope freeze before release.** Release comes last, once, after every part
and the independent re-check. After the freeze, only fixes for breakage.

---

## How it maps onto the method

| Here | In the method |
|---|---|
| a ladder plan | a brief, or a phase of briefs, one rung per brief when rungs are big |
| a stage of spending | a brief whose body states the entry condition and cost; its `starts:` line uses one of the three forms the `gates` check accepts, for example `starts: after <stream>` where that stream holds the free checks |
| the decision log | the director's file, beside `docs/standing.md` |
| a parallel worker | one working session per brief, briefed with the worker template. Raise `open_briefs` in `.formwork.toml`, or set `open_briefs_per = "stream"`, or `work-paired` goes red at the second open brief |
| the release checklist | the release step (`../templates/release-step.md`) |

A project names the parts it uses in its standing brief or its plan, and
overrides any number here by writing its own before it starts.

## What it cannot do

It cannot tell you a bar is right, only that you wrote one first. It cannot see
a worker stalling; a person or a director has to look. Every number on this
page is one round's default, not a measured optimum. NOT ESTABLISHED: whether
these limits suit a project of a different size.
