# Research pitfalls

The ways research by building usually goes wrong. Read them before a question
is registered, and again before its result is reported.

**Source.** The items come from one project's months of research by building,
reviewed afterwards against how research labs work. The review found these
patterns repeatedly. Each item cites the public method that names it. They are
written generally, with no product or person in them.

The shape follows the taste packs ([`../taste/README.md`](../taste/README.md)).
Each item has an id, **Catches**, **Detected** (high: a search finds it;
medium: a search finds candidates and a person decides; low: needs a reader),
a hint, and a **Source**. Even a high item is a hint, never a gate.

---

## Before the run

### res-1 Agreement reported as correctness
**Catches** two readers, two judges or a writer and a labeller agreeing, with
the agreement then used as the quality score. Agreement is reliability. It says
the readers are consistent, not that they are right.
**Detected** medium. A hint: a headline figure that compares two annotators and
no figure that compares either one to an answer key written by a domain expert.
**Source** Shadish, Cook and Campbell 2002, on reliability and validity.

### res-2 Agreement with no correction for chance
**Catches** exact match agreement on labels where some agreement happens by
luck. Two readers who both answer "yes" 90 percent of the time agree often and
mean little.
**Detected** high. A hint: an agreement percentage with no kappa or alpha
beside it.
**Source** Krippendorff, *Content Analysis*, the reliability chapter.

### res-3 A gate with no origin
**Catches** a pass mark (80 percent, 98, 70) that nobody can trace to a harm, a
cost, a user need, or the measured noise. A gate with no reason cannot be
argued with, so a miss teaches nothing.
**Detected** medium. A hint: find every threshold in the plan and ask where it
came from. "It seemed right" is an origin, and it should be written as one.
**Source** Lakens, Scheel and Isager 2018, on the smallest effect size of
interest. https://doi.org/10.1177/2515245918770963

### res-4 A sample too small for its own bar
**Catches** a bar that the sample cannot resolve. A 95 percent rule checked on
5 control items cannot tell 95 from 80. A 2 point gap on 50 cases sits inside
the noise.
**Detected** medium. A hint: for every bar, write the smallest difference the
sample could detect. If it is bigger than the bar's margin, the bar is
decorative.
**Source** Lakens, *Improving Your Statistical Inferences*, the chapter on
sample size justification. https://lakens.github.io/statistical_inferences/

### res-5 A registration nobody can date
**Catches** a plan or a registry that was written "first" but holds no
timestamp anyone else can check. If its file time is after the results, or it
was never committed, it proves nothing.
**Detected** high. A hint: `git log` on the plan. Untracked, or first committed
after the first result, means unregistered.
**Source** Nosek et al. 2018, "The preregistration revolution".
https://doi.org/10.1073/pnas.1708274114

### res-6 Synthetic data only
**Catches** every test set written by a model, and none from the real users or
real use. Synthetic sets give coverage; they do not show that the real
distribution looks like them.
**Detected** high. A hint: the provenance of every set. If no set has a real
source, say so on every result.
**Source** the general principle of external validity, Shadish, Cook and
Campbell 2002.

### res-7 One family writes, answers and judges
**Catches** models from one family writing the tasks, producing the answers
and grading them. Model judges are known to prefer their own family's output
and the first answer shown.
**Detected** medium. A hint: list the model family at each stage. Any family on
two stages is a candidate.
**Source** Zheng et al. 2023 (position bias), https://arxiv.org/abs/2306.05685;
Panickssery, Bowman and Feng 2024 (self preference),
https://arxiv.org/abs/2404.13076

### res-8 A weak baseline
**Catches** a new system compared with a baseline that got no tuning, or with
tasks written for the new system's own shape. A large win over a straw baseline
measures the tasks, not the system.
**Detected** low. A hint: did the baseline get the same effort? Were the tasks
written before the new design, or for it?
**Source** the principle of a fair comparison; see Kapoor et al. 2024, "AI
Agents That Matter". https://arxiv.org/abs/2407.01502

### res-9 Prior art read and never used
**Catches** a literature review that is written, filed and never turned into a
prediction or a test. Reading without testing is how a design reinvents a known
idea and also misses its known failures.
**Detected** medium. A hint: for each source the review cites, is there one
line saying what it predicts here, and was that tested?
**Source** Hevner 2007, the rigor cycle.

### res-10 No outcome, or a measure that is not the outcome
**Catches** success defined as passing a test set, with nothing checking that
passing means a person is better off. Construct validity comes first: does the
measure track what users value?
**Detected** low. A hint: write the chain from the measured number to a benefit
for a person. Every link that was never checked is a gap.
**Source** Shadish, Cook and Campbell 2002 (construct validity); for timed
interventions, Klasnja et al. 2015 on micro-randomised trials.

## During the run

### res-11 One run per arm
**Catches** results from a single run of each arm on a model that varies from
run to run. One run cannot show its own noise.
**Detected** high. A hint: count runs per arm in every results table.
**Source** Cohen, *Empirical Methods for Artificial Intelligence*, 1995.

### res-12 Fixing on the test set
**Catches** the bar reached by repeated fix rounds on the same set, or fix
rounds after validation and then a comparison on fresh sets against the same
baselines without counting the comparisons. Each look at the data spends some of
its power to surprise you.
**Detected** medium. A hint: count how many times each set was scored before
the reported run.
**Source** Gelman and Loken 2013, "The garden of forking paths"; Dwork et al.
2015, "The reusable holdout".

### res-13 A proxy that failed its check stays the instrument
**Catches** a cheaper stand in (a different client, a local model, a mock
path) compared once with the real path, found to differ, and then still used for
the numbers that matter.
**Detected** medium. A hint: for every result, say whether it came from the
real path. If a proxy check failed, which results still rest on the proxy?
**Source** the general principle of measurement validity; in ML, the sim to
real gap.

### res-14 The instrument is never tested
**Catches** a prompt, a scorer or a metric trusted before anyone checked it. A
prompt that truncates its input, a scorer with a bug, a metric that cannot fall
when it should. Each one produces confident numbers about nothing.
**Detected** medium. A hint: before results, feed the instrument cases with a
known answer, including ones built to fail. Prove what the metric can and
cannot show.
**Source** Shankar et al. 2024, "Who Validates the Validators?".
https://arxiv.org/abs/2404.12272

### res-15 The answer key is never audited
**Catches** a gold set trusted as truth. Blind audits of gold sets routinely
find a share of the answers wrong.
**Detected** low. A hint: have a judge compare system output and gold without
knowing which is which, on a sample, and count the gold errors.
**Source** Northcutt, Athalye and Mueller 2021, "Pervasive Label Errors in Test
Sets". https://arxiv.org/abs/2103.14749

### res-16 Raw outputs and scoring code not kept
**Catches** a result whose model outputs, judge outputs or scoring script are
gone. Nothing can reproduce it, and nobody can check it later.
**Detected** high. A hint: for each reported number, can the raw outputs and
the script that produced it be found by path?
**Source** the general practice of computational reproducibility.

## After the run

### res-17 The average hides the story
**Catches** one blended number over judges, slices or kinds of task, when one
judge, one slice or one kind behaves differently. The mean says everyone is
fine.
**Detected** medium. A hint: split every headline by judge and by kind before
reporting it.
**Source** the researcher role, "report the shape, not just the middle"
([`../roles/method/researcher.md`](../roles/method/researcher.md)).

### res-18 The predictor scores itself
**Catches** a challenger or a forecaster who writes predictions and later
grades them. Without a probability on each prediction and someone else
resolving it, the score cannot be checked.
**Detected** high. A hint: who resolved each prediction, and was there a
probability?
**Source** Brier 1950 (the Brier score); Tetlock and Gardner, *Superforecasting*,
2015.

### res-19 A silent deviation
**Catches** a bar missed and the work shipped anyway, with nothing recorded, or
a recorded plan quietly changed. An open deviation ("this ships past the reader
bar, which it missed") is fine. A silent one is not.
**Detected** medium. A hint: compare the registered plan with what was run and
what was decided. Every difference needs a line.
**Source** Nosek et al. 2018, on reporting deviations from a registration.

### res-20 Nothing leaves the room
**Catches** findings that no one outside the work has read: no reviewer without
context, no peer, no write up. The rigor cycle stays open, and errors that
outsiders would see in a day stay in.
**Detected** high. A hint: name the last person outside the work who read a
finding, and when.
**Source** Peffers et al. 2007, the communicate step.
https://doi.org/10.2753/MIS0742-1222240302

### res-21 Other people's data before consent and a safety review
**Catches** outside users given a build that records their health, money or
private life before anyone asked for consent, reviewed privacy, or analysed the
hazards of the advice it gives.
**Detected** medium. A hint: the first build any outside person received, and
whether consent, a privacy review and a hazard analysis came before it.
**Source** GDPR Article 35 (data protection impact assessment); ISO 14971 for
medical device risk management.

---

## Using this list

Read it at two moments. Before registration, against parts 5 to 8 of the card.
Before the report, against parts 9 to 11. A finding names the item:
`res-12: validation set scored four times before the reported run`.
