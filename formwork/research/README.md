# The research pack

Optional. For a project that learns by building: it makes something, measures
it, and decides what to keep. Most AI products are built this way. The pack
gives that work a method, a card to write before each question, and a list of
the ways it usually goes wrong.

The `researcher` role already holds the core rule: write down what would count
as success before you run anything. This pack is the method around a whole
question, from asking it to deciding what to do and telling someone outside.

**The pack is never a check.** No program here judges a research question. The
pitfalls are for the person, the `researcher`, the `challenger` and the
`reviewer` to look with, the same way taste packs are.

---

## The frame, in one paragraph

Research by building has a name: **design science research**. Peffers et al.
(2007) give its six steps: identify the problem, define objectives, design and
build, demonstrate, evaluate, communicate. Hevner (2007) adds three cycles that
run together: **relevance** (a real problem in a real setting), **design**
(build and evaluate), and **rigor** (grounded in what is already known, and
adding back to it). Starting from the build is allowed. What is not allowed is
skipping the rigor cycle at either end: reading nothing before, or telling
nobody after.

Sources: https://doi.org/10.2753/MIS0742-1222240302 (Peffers et al. 2007);
Hevner, "A Three Cycle View of Design Science Research", Scandinavian Journal of
Information Systems 19(2), 2007.

---

## The question card

Every research question gets a card before any work starts:
[`../templates/research-question.md`](../templates/research-question.md). It is
a brief for a question. Small questions are a task brief that points to a card;
costly ones are a round (see [`../round.md`](../round.md)), with the card as the
round's `brief.md`.

The card has twelve parts. The first eight are written and committed before
anything runs. That commit is the registration.

| Part | Written | Says |
|---|---|---|
| 1. The question | before | something that can come out wrong |
| 2. Why it matters | before | what changes if the answer is yes, and if it is no |
| 3. What is already known | before | prior work read, and **what it predicts here**, as a test |
| 4. The hypothesis | before | the expected answer, and the result that would refute it |
| 5. The method | before | what is built, what is measured, against what baseline |
| 6. The bar, and where it comes from | before | a harm, a cost, a user need, or the measured noise |
| 7. The sample, and why that size | before | the smallest effect worth seeing, and the runs per arm |
| 8. The registration | before | the commit that holds parts 1 to 7 |
| 9. The result | after | numbers with their commands, the tail as well as the middle |
| 10. Deviations | after | anything that differed from the plan, said plainly |
| 11. Threats to validity | after | internal, external, construct, statistical |
| 12. The decision, and who hears | after | keep, change or drop; and who outside the work reviews it |

When the question needs a measurement set, add the evaluation plan:
[`../templates/evaluation-plan.md`](../templates/evaluation-plan.md).

---

## The loop

1. **Ask.** The person and the `researcher` write parts 1 to 4. The skill
   [`../skills/research-question/`](../skills/research-question/) walks this.
2. **Predict.** The `challenger` writes `predictions.md` first, with a
   probability on each prediction. Someone other than the challenger resolves
   them later.
3. **Plan.** Parts 5 to 7, and the evaluation plan if there is one.
4. **Register.** The person commits the card. Git is theirs; the commit date is
   the proof that the plan came first.
5. **Run.** The registered test, as registered. Exploratory runs are welcome and
   are labelled exploratory.
6. **Read the failures.** By hand, before any fix. Count them by cause.
7. **Report.** Parts 9 to 11. A missed bar is a result.
8. **Decide.** Part 12, by the person. If the work ships past a missed bar, the
   decision says so in those words.
9. **Communicate.** Someone outside the work reads the finding: a reviewer with
   no context, a peer, a write up. Without this step the rigor cycle is open.

---

## The names worth knowing

Work like this uses established methods whether or not anyone names them.
Knowing the name finds the literature and its known traps.

| What you are doing | Its name | Read |
|---|---|---|
| Writing the plan and bar before the data | preregistration | Nosek et al. 2018, https://doi.org/10.1073/pnas.1708274114 |
| Working out how many cases a test needs | power analysis; minimum detectable effect | Lakens, *Improving Your Statistical Inferences*, https://lakens.github.io/statistical_inferences/ |
| Choosing the bar from what matters | smallest effect size of interest | Lakens, Scheel and Isager 2018, https://doi.org/10.1177/2515245918770963 |
| Two people labelling the same items | inter-rater reliability (kappa, alpha) | Krippendorff, *Content Analysis* |
| Checking the labels against the truth | validity against a gold standard | Shadish, Cook and Campbell 2002 |
| Running the same thing twice | test-retest reliability | |
| Changing one part and holding the rest | ablation | |
| Granting one part perfection to see the ceiling | oracle or headroom analysis | |
| Fixing on a set, then testing on the same set | holdout reuse; garden of forking paths | Gelman and Loken 2013 |
| A model grading outputs | LLM as a judge | Zheng et al. 2023, https://arxiv.org/abs/2306.05685 |
| Checking the judge | meta-evaluation | Shankar et al. 2024, https://arxiv.org/abs/2404.12272 |
| Auditing the answer key | label error audit | Northcutt, Athalye and Mueller 2021, https://arxiv.org/abs/2103.14749 |
| Reading failures and sorting them by cause | error analysis; open coding | |
| Designing for yourself through real use | autobiographical design | Neustaedter and Sengers 2012 |
| Testing whether a nudge at a moment helps | micro-randomised trial | Klasnja et al. 2015 |
| Saying how a result could be wrong | threats to validity | Shadish, Cook and Campbell 2002 |

---

## How a project uses it

1. **Name it.** In the standing brief, one line: `Research pack: on`.
2. **Override.** One line per item the project turns off, with its reason:
   `res-6 off: no real data exists yet; synthetic only, decided in 0012`.
   An overridden item is not a finding.
3. **Point to it.** A research brief names the card. A review of research
   names the pitfalls the reviewers look with.
4. **Report by id.** `res-1, the reader study: agreement reported as accuracy`.

---

## What this cannot do

Make a question good. A card can be filled in perfectly for a question nobody
needed answered. Part 2 is where that shows, and only a person can judge it.

Know the sources are right for every project. They are public and cited. None
was measured in this kit.

Replace real data, real users or real money. The pack can only make it plain
when a result rests on none of them.
