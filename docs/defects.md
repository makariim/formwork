# Defects

**Phase:** K4. **Date:** 2026-09-12.

Every mechanism that should not be published as it stands, with what to do
about it.

## The two questions this phase asks

**Does this work because of the method, or because of the one person who has
been running it?** Anything that works only because of the person is made
mechanical or labelled. A rule followed by willpower will not be followed.

**Which rules would harm someone who adopts them without the failures that
produced them?** A rule learned from a specific disaster is cheap for whoever
lived through it and expensive for everyone else, because they pay the cost and
never see the benefit.

## Dispositions

Four were planned. A fifth turned out to be needed and is folded into the first,
rather than invented.

| Disposition | Meaning | Count |
|---|---|---|
| **Drop** | Remove it. Where something else already does it, the entry says what to adopt instead | 14 |
| **Enforce mechanically** | Keep it, implemented in configuration. Every entry names the mechanism | 10 |
| **Weaken** | Keep it, but not in its current form. The entry says what changes | 15 |
| **Ship with a warning** | Keep it, with its limit stated where a reader will see it | 12 |
| **Ship as it is** | Nothing wrong with it. Listed for completeness | 19 |
| **Deferred** | Cannot be judged yet | 1 |
| | **Total** | **71** |

Counts produced by tallying the entries in each section below, cross-checked
against the inventory's ten groups. What would make them wrong: a disposition
assigned badly, which is judgement rather than measurement.

**On the fifth disposition.** K3 found eighteen mechanisms that something else
does better. "Adopt theirs instead" is not one of the four dispositions the plan
lists. It is recorded here as **drop**, with a pointer to what replaces it,
because dropping our version is what actually happens. No new category was
invented, but the plan's four did not cover the case cleanly and that is worth
recording.

---

# Drop — 14

## Dropped because something else already does it

### B-09 — the threshold is fixed before measuring
Evaluation harnesses make this structural: the criterion is declared in the
configuration before anything runs. A rule asking a person to do it by hand is
weaker. **Point at the harness; drop the rule.**

### C-04 — a generated overview that holds no authority
The highest recurring cost in the inventory, and its purpose is served by
generating the page from a single source and refusing to build when the two
disagree. **Drop the hand-maintained version.**

### C-05 — the decision record format
Two mature projects between them already supply numbering, bidirectional
supersession, decision drivers, considered options, a forced justification
clause, and consequences split into good and bad. **Adopt those; design nothing.**

### D-05 — size is a boundary
A file count is arbitrary. A published alternative defines the unit by whether a
reviewer could reject one piece while approving the next. **Adopt the review
criterion.**

### E-05 — checkers ship with deliberately broken inputs
Already a shipped artefact elsewhere, stable for years. **Point at it.**

### F-12 — the round record format
The attribution requirement is real and someone else already encodes it, using a
responsibility model with named roles for who decided, who was consulted, and
who was informed. **Adopt the vocabulary.**

### F-15 — roles constrained by their tool grant
Standard practice in published role definitions, including the reasoning for
why it binds. **Nothing to add.**

### H-07 — contest the premise first
### H-08 — name the minimal alternative
Both currently depend on an adversary being present and doing its job. A
published template makes each a mandatory section every proposal must fill.
**Move them out of a role's behaviour and into the artefact.** A section cannot
forget.

## Dropped because they should not be published at all

### I-01, I-02, I-03 — the three environment hazards
These describe the behaviour of specific tools at specific versions: which
search commands silently skip files, which exist only inside an interactive
shell, and where stale copies hide.

**They will become wrong.** A kit that publishes them hands a forker confident,
checkable-looking statements that quietly stop being true, and there is no
mechanism to notice. The underlying principle is already carried by B-04.

**Drop all three.** If any survives, it must carry the tool and version it was
observed on, and an expiry.

### A-07 — one document no agent may edit
Useful, not necessary, and the founder review recorded that people no longer
want to write long documents by hand. **Drop it as a rule.** One line of advice
at most.

### B-05 — enumerate rather than interrogate
A useful habit, not a mechanism. It is one sentence inside B-04's problem.
**Fold it in and drop the separate entry.** Volume is a defect here, and a
71-entry inventory that ships whole is a kit nobody reads.

---

# Enforce mechanically — 10

Each names the mechanism. An entry marked for enforcement with no named
mechanism is a K4 failure, so none is listed without one.

### A-01 — version control reserved to the human

**The most emphasised rule in the method, and it is enforced nowhere.** That is
the single clearest finding of this phase.

**Mechanism.** A pre-execution hook matching shell commands against the set of
write subcommands — commit, push, merge, rebase, and the rest — refusing with a
non-zero exit. Read operations pass untouched, because the report requires them.

**Why it must be mechanical.** Prose survives until an instruction casually asks
for a commit. The whole point of a boundary is that it does not depend on
whoever wrote the last brief remembering it.

**Configurable strength, and this is not optional.** Block by default for a
single builder. A team whose reviewer is asleep in another timezone is stopped
for twelve hours by a rule that costs a solo builder ten minutes. Warn and off
must both be available, and choosing one must be a line the forker wrote.

### A-04 — verify the brief against the files

**Mechanism.** A checker that extracts referenced paths and commands from a
brief, skips URLs and environment variables, resolves each against the
repository, and reports what does not exist. This exists as a published tool
aimed at a different file; the same approach applies.

**What stays discipline.** Claims a machine cannot resolve. The rule shrinks to
cover only those.

### B-02 — a check must have a way to go red

**Mechanism.** A check ships alongside an input that makes it fail, one per
failure mode claimed. The aggregate runs the failing inputs and fails if any of
them passes.

This converts the rule from a question an author asks themselves into an
artefact that either exists or does not.

### B-08 — conflicting records: surface both, adopt neither

**Mechanism.** A content hash stored with each reviewed document, and with each
link to another document. Editing the text invalidates the review. Editing a
parent marks every link to it suspect.

**With a caveat.** This is the heaviest mechanism proposed here, and it forces a
file format. K5 decides whether to adopt it or decline it explicitly. Declining
in writing is an acceptable outcome; leaving it unaddressed is not.

### B-10 — regenerate, never adjust

**Mechanism.** Derived pages are generated, generation is idempotent, and the
check fails when regenerating produces a different file. A hand-edited figure
then cannot survive a single run.

### C-06 — identifiers assigned from the integrated state

**Mechanism.** The next number is computed from the directory, not issued by a
role. No queue, no placeholder, no guessing.

The founder review asked to keep this as configuration precisely because hand
assignment fails once several threads are open. The configuration exists and is
about thirty lines of shell.

### E-01 — one named aggregate
### E-02 — enforcement in configuration
### E-03 — a blocking check with a budget

**Mechanism.** One command runs everything. A hook runs that command by name
when the agent tries to conclude a turn in which files changed, and refuses on
failure. The refusal is bounded per session; when the budget is spent the human
is told rather than the failure disappearing.

**These three are the kit's only plausible contribution.** The survey found
enforcement to be advisory almost everywhere, and the one project with
harness-level hooks describes its own guard as advising rather than blocking,
shipped disabled. If Formwork ships something that actually blocks, that is new.
If it does not, Formwork is another advisory kit.

**The budget is not a detail.** A gate that refuses once was defeated in
testing by an agent that edited working code until the broken check agreed with
it, then reported success. A gate that refuses forever strands the work. Bounded
refusal with escalation is the only version that survives contact.

### F-03 — predictions committed before exposure

**Mechanism.** The predictions file must exist before any other participant's
output is shared. A file-existence check, and it is enough — the value comes
from the ordering, and ordering is checkable.

---

# Weaken — 15

Kept, but not as they stand.

| Mechanism | What changes, and why |
|---|---|
| **A-02** agents never author a decision | The rule cannot tell a real decision from a routine choice, and it demands that judgement on every task. For a newcomer almost everything looks like a decision, so the kit stalls constantly in week one. Ship a test: it is a decision when the alternative would produce different work later, and the difference is not recoverable by editing |
| **A-06** verification machinery owned by one role | Meaningless for one person. Restate as a property rather than a role: the gate is never modified by the work that trips it |
| **B-04** what a search actually observed | Keep the three variables. Strip the tool-specific detail, which belongs to a version and will rot |
| **B-06** unmeasured is marked unmeasured | As written, a young project's documents become a wall of admissions. That reads as low quality and is demoralising. Scope it to claims a reader would act on |
| **C-02** a small fixed set of governing documents | Do not defend a seven-way split against a published twelve-way one with no evidence. Keep the ownership principle; adopt the toggleable in-template guidance mechanism, which is a direct answer to the problem K6 has to solve |
| **C-07** a holding area outside active scope | A second document accumulates and becomes a graveyard — its own stated cost. Replace with a status value inside the record it belongs to, following the published "not now" state |
| **D-01** the six-part brief | It has no section that argues against the work. Add the missing ones from the published template: why not, what happens if we do nothing, prior art, and unresolved questions split by when each resolves |
| **D-02** the standing report | Scale it. A fixed list applied to a one-line fix produces a report longer than the change, and that is how a kit gets bypassed for small work, and therefore for most work |
| **F-06** per-participant reading lists | Real preparation cost, and a wrong list silently starves a participant. Default to a shared pack plus one targeted addition, not a bespoke list each |
| **F-09** three endings for a disagreement | The published alternative uses named public states, but it works by gatekeeping — people with standing to accept and reject. That does not transplant. Adopt the named states; do not claim the authority model comes with them |
| **F-10** unanimity treated as a warning | Adopted without judgement this manufactures conflict, which the adversary's own rules forbid. Add the guard: intervene by naming an unexamined assumption, never by requiring that someone disagree |
| **F-11** repeated failure stops the round | Counting deaths is a heuristic. Adopt the sharper form: record whether a failure was infrastructure or real, and let that decide |
| **G-04** the threshold for interrupting | Its reasoning invokes a person who builds daily and notices within a day. Strip the reasoning, keep the criterion: interrupt for what cannot be undone and for what fails quietly. Someone who opens their project weekly is harmed by the version that exists |
| **H-02** named categories of premature infrastructure | **The clearest case in this phase of a rule that is cheap for its author and expensive for an adopter.** It names specific technologies to argue against. Someone whose project genuinely needs one of them gets argued out of it by a rule carrying no evidence about their situation. Weaken to the test rather than the list: what does this component do that nothing present already does, and who operates it in six months |
| **H-06** the burden on the maintainer later | Drop "one person". Adopt the published wording: what becomes easier or harder, and what risks are introduced |

---

# Ship with a warning — 12

Kept as they are, with the limit stated where a reader will see it — not in a
footnote.

| Mechanism | The warning |
|---|---|
| **A-03** one authorised unit at a time | Some of the stopping is pure waste and nothing tells you which instances in advance. The cost is real and has never been measured |
| **A-05** out of remit, name the owner and stop | Known problems sit unfixed while a report travels. For a solo builder this is often slower than just fixing it |
| **B-01** figures carry their derivation | Ceremony on a project with nothing to count |
| **C-01** one owner per category of fact | Nothing detects a duplicated fact. This is a discipline with no check behind it, and the survey found no tool that supplies one |
| **D-04** checks and documentation inside the unit | Every unit becomes larger than the change that prompted it |
| **F-01** a convenor holding no stake | An entire participant that produces no design. On a narrow question that is most of the budget |
| **F-02** a standing adversary | It pays for itself only when the round would otherwise have converged wrongly, and that is not knowable in advance. **No round cost has ever been measured.** K5 must state what a round costs in money before anyone commits to one |
| **F-05** one prepared briefing | The convenor becomes a single point of misunderstanding. A wrong briefing is wrong for everyone |
| **G-01** two parts, invariably | Everything gets written twice. The format was tuned to one named reader |
| **G-03** economise on exchanges | Assumes a human manually relaying between separate threads. If that is not your arrangement, these rules solve a problem you do not have |
| **J-01** a standing partner above the repository | It has no definition, no configuration, and no artefact anywhere. It cannot be reviewed, corrected, or handed to anyone. **This is the least publishable thing in the inventory and the most load-bearing** |
| **J-02** the human carries messages between layers | Known not to transfer as it stands. It is what remains when two systems that must cooperate have no channel, and it does not scale past one person |

---

# Ship as it is — 19

No defect found. Listed so the total accounts for all 71.

B-03 structure is not content · B-07 no invented sources · C-03 documents
describe the present · D-03 scope echoed back before editing · E-04 a pass names
its blind spots · F-04 partition by authority · F-07 all responses read before
answering · F-08 one exchange per position · F-13 a prescribed shape for
escalation · F-14 roles appear with their subject · **F-16 failure histories are
earned, never imported** · G-02 contradictions go first · G-05 corrections are
stated, not absorbed · G-06 favour the modest claim · H-01 generalise on the
second case · H-03 name the non-goal approached · H-04 stored material nothing
consumes · H-05 interrogate the quiet failure · J-03 complete reports travel
upward

**F-16 belongs at the front of the kit.** It is the method saying that
principles transfer and illustrations do not, which is the exact problem
Formwork exists to solve. It is also the only entry that anticipates its own
misuse.

---

# Deferred — 1

### E-06 — deliberate breakage

K3 placed this in "not covered" and immediately flagged the placement as unsafe:
mutation testing is a mature discipline with established tools, and none of the
survey's six shapes would have found them.

**Ruling on it now would be ruling on an absence nobody verified.** Status is
**NOT ESTABLISHED**. A targeted search is required before K5 can treat it as
either a contribution or a redundancy.

---

# The harm analysis

The phase's second question, answered directly. These are the rules most likely
to hurt someone who adopts them without having lived through what produced them.

**1. The infrastructure list (H-02).** The sharpest case. It names specific
technologies as things to argue against, drawn from one person's experience on
two projects. An adopter whose project genuinely needs one of them is talked out
of it by a rule that knows nothing about their situation. Weakened to a test.

**2. The interrupt threshold (G-04).** Its reasoning depends on daily building.
Adopted unchanged by someone who checks weekly, it downgrades real problems to
notes for a week. Weakened.

**3. The brief and report, together (D-01, D-02).** For small work the ceremony
exceeds the work. This is the failure mode the survey named for spec-driven
kits: the process gets bypassed for small changes, and most changes are small,
so it gets bypassed entirely. Both weakened to scale with the work.

**4. Decision stalling (A-02).** Correct in principle and unusable without a
test for what counts as a decision. A newcomer stalls on everything. Weakened
with a test.

**5. Round cost (F-01, F-02, F-05).** A convenor, three specialists and an
adversary for one question. The cost has never been measured and is nowhere
stated. Someone adopting this for a small question spends real money finding
out. Shipped with a warning, and K5 must supply a figure.

**6. The environment hazards (I-01 to I-03).** Published facts about tool
versions that will silently become false. Dropped.

---

# What this phase did not find

**No mechanism was found that is dishonest or unsound.** The defects are of
four kinds: unenforced rules that depend on willpower, rules calibrated to one
person's working rhythm, ceremony that does not scale down, and mechanisms
someone else already built better.

That is not a defence of the method. It is a statement of what kind of list this
is, so K5 knows what it is designing against.

# What could not be established

- **Whether any of this works.** One practitioner, two projects, no control.
- **What a round costs**, in money or wall time. Never measured. Ships as a
  warning and K5 must resolve it.
- **E-06's status**, pending a targeted search.
- **Whether the weakened forms are better.** Every "weaken" here is a judgement
  made without evidence from a second practitioner, because none exists.
