# Operations pitfalls

The ways building and measuring in parts usually goes wrong. Read them before
a ladder plan or a stage is set, and again before a result or a release is
reported. The research pitfalls ([`../research/pitfalls.md`](../research/pitfalls.md))
cover the question and its measure; these cover the running of the work.
Where one of those already names a fault, the item here points to it instead
of repeating it.

**Source.** One project's three day build and measure round, where each of
these happened or was caught, written generally, with no product or person in
them. Each item also cites the public method that names it.

The shape follows the taste and research packs. Each item has an id,
**Catches**, **Detected** (high: a search finds it; medium: a search finds
candidates and a person decides; low: needs a reader), a hint, and a
**Source**. Even a high item is a hint, never a gate.

---

## Before the run

### ops-1 The whole chain tested before its parts
**Catches** an end to end test run on parts that never passed a check of
their own. When it loses, nobody can say which part lost it.
**Detected** medium. A hint: an end to end result in a report with no earlier
result for each part on its own set.
**Source** Myers, *The Art of Software Testing*, on incremental against big
bang integration.

### ops-2 A lost test read as a lost idea
**Catches** "the approach does not work" written after a test of a build that
carried known bugs. The build failed; the idea was never tested.
**Detected** medium. A hint: a conclusion about an approach with no list of
the bugs the build carried, or no wording of the form "this build scored X".
**Source** Shadish, Cook and Campbell 2002, on treatment implementation: an
operation that was not delivered as designed tests nothing about the design.

### ops-3 Reading faults and building faults not told apart
**Catches** a part blamed for errors that came from the part before it. No
run fed it perfect inputs, so the two kinds of fault stay mixed.
**Detected** medium. A hint: error attribution in a chain with no run where a
part received the gold output of the part before it.
**Source** Ng, *Machine Learning Yearning* (2018), the chapters on error
analysis by parts.

### ops-4 Spending before the free checks pass
**Catches** a paid run started while a free gate is red or was never run, or a
paid plan with no written entry condition per stage.
**Detected** high. A hint: a cost line in a report dated before the free
check results it depended on; a stage with no entry condition.
**Source** Cooper, "Stage-Gate Systems: A New Tool for Managing New Products",
*Business Horizons* 33(3), 1990.

### ops-5 A shared definition changed by one lane
**Catches** a schema, generated type or shared fixture edited by a lane that
does not own it, so the other lanes build against something that moved under
them.
**Detected** high. A hint: a change to a frozen file whose hash no longer
matches the freeze record, with no owner's note.
**Source** Robinson, "Consumer Driven Contracts: A Service Evolution Pattern",
martinfowler.com, 2006.

## During the run

### ops-6 Patching one defect class for ever
**Catches** the fourth, fifth and sixth fix for the same kind of fault, each
local, none asking why the design keeps producing it. Also a part driven by a
model revised again and again with no limit.
**Detected** medium. A hint: the same defect class in three or more fix
entries; a prompt or judge revised more times than the plan allowed.
**Source** Ohno, *Toyota Production System* (1988), on stopping to find the
root cause instead of repairing the symptom again.

### ops-7 A used set kept as evidence
**Catches** a validation set read during error analysis and then reported as
a fresh measure. See `res-12` (fixing on the test set); this item adds the
rule that the read set becomes dev, and the next measure needs a fresh one.
**Detected** medium. A hint: a set named in error analysis notes and again as
the source of a headline result.
**Source** Kapoor and Narayanan, "Leakage and the reproducibility crisis in
machine-learning-based science", *Patterns* 4(9), 2023.

### ops-8 A harness artifact believed
**Catches** a comparison that is really a bug in the harness: a dropped id, a
timeout counted as a wrong answer, a scorer that misreads one format.
**Detected** medium. A hint: one check failing on every item of one kind; a
result too good or too bad to be true.
**Source** Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments*
(2020), on Twyman's law: any figure that looks interesting is probably wrong.

### ops-9 Waiting on another session, or busy read as progress
**Catches** a worker waiting for a global condition another session keeps
true, or a watchdog that counts live processes as work done.
**Detected** low. Needs somebody to look at the worker's own outputs. A hint:
a wait loop on a global process check; no file of the worker's own changed in
30 minutes.
**Source** Beyer, Jones, Petoff and Murphy, *Site Reliability Engineering*
(2016), the monitoring chapter: watch the symptom the user sees, not the
process that should cause it.

### ops-10 Workers sharing a device, scratch or build folder
**Catches** two sessions on one simulator, one scratch folder or one build
output, each failing on the other's state.
**Detected** high. A hint: two worker briefs naming the same scratch path or
device.
**Source** Meszaros, *xUnit Test Patterns* (2007), on the shared fixture and
interacting tests.

## After the run

### ops-11 Ahead on the point estimate only
**Catches** "the new path wins" from a point estimate whose paired interval
crosses zero, or a small gain shipped with no non inferiority margin written
before the measure.
**Detected** high. A hint: a ship call with no lower bound beside it; a margin
first written in the same report as the result.
**Source** Piaggio et al., "Reporting of Noninferiority and Equivalence
Randomized Trials", *JAMA* 308(24), 2012.

### ops-12 All or nothing shipping, with no way back
**Catches** a whole release held for one losing route, or shipped with every
route on the new path and no fallback to the old one on failure.
**Detected** medium. A hint: one ship decision for the whole product; no
fallback named per route.
**Source** Beyer et al. 2016, the release engineering chapter; Beyer, Murphy,
Rensin, Kawahara and Thorne, *The Site Reliability Workbook* (2018), the
chapter on canarying releases.

### ops-13 Success reported for a wrong value
**Catches** a product that says "done" after applying the wrong value, or none,
and a test that checks the reply instead of the result.
**Detected** medium. A hint: tests that assert on a success message with no
read back of the changed value.
**Source** Barr, Harman, McMinn, Shahbaz and Yoo, "The Oracle Problem in
Software Testing: A Survey", *IEEE Transactions on Software Engineering*
41(5), 2015.

### ops-14 The builder checks its own work or its own release
**Catches** the session that built a part writing its gate, running its final
measure, or ticking its release checklist; a release row with no source.
**Detected** high. A hint: the same session named as builder and checker; a
checklist row whose source column is empty.
**Source** IEEE 1012, *Standard for System, Software, and Hardware
Verification and Validation*, on independent verification.

---

## Using this list

Before a ladder plan, a stage or a parallel round is set, read the "before"
items. Before a result, a ship call or a release is reported, read the rest.
A project drops an item it never meets by deleting it from its copy, and adds
its own in the same shape.
