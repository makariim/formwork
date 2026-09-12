# Gap map

**Phase:** K3. **Date:** 2026-09-12.

Every mechanism in the inventory, set against every tool in the survey, sorted
into four buckets.

## What this document is for

To make the kit smaller.

Buckets 1 and 4 remove work. Bucket 4 is the point of the phase: it names what
the method should change or drop because something else already solves it, more
simply or more rigorously.

## How to read a claim here

Claims that a tool does or does not do something cite the survey entry, which in
turn names the file or command it was read from. Nothing here rests on a
project's description of itself.

**The test is same effect, not same word.** A mechanism is only in bucket 3 if
nothing in the corpus achieves what it achieves, however differently it is
named.

## What is deliberately not here

No mechanism is attributed to where it came from. The inventory records that;
this document does not need it, and carrying it forward would rebuild a leak
that took three rounds to close.

---

## Counts

| Bucket | Meaning | Entries |
|---|---|---|
| 1 | Already covered, and covered well | 4 |
| 2 | Partly covered | 18 |
| 3 | Not covered in the surveyed corpus | 31 |
| 4 | Something else does it better | 18 |
| | **Total** | **71** |

Counts produced by tallying the entries listed in each section below. What
would make them wrong: a mechanism placed in the wrong bucket, which is a
judgement, not a measurement. Bucket 4 and bucket 1 were assigned first and
deliberately generously, because those are the buckets that shrink the kit.

**Where bucket 3 concentrates, and why that is not a victory.** Of its 31
entries, 6 are the rules about writing to a human, 3 are the layer above the
repository, and 3 are environment hazards. That is 12 of 31 sitting in areas
the survey's six shapes were not pointed at. An empty result there is weak
evidence of a gap and strong evidence about where nobody looked.

---

# Bucket 1 — already covered, and covered well

The kit points at these. It does not rebuild them.

### B-09 — the threshold is fixed before measuring

**Covered by:** Inspect AI (survey 22), promptfoo (survey 23).

Both make this structural rather than a matter of discipline. An Inspect task
composes `dataset`, `solver` and `scorer` before anything runs — the scorer *is*
the threshold, declared in the source. promptfoo declares `assert` blocks in
YAML with a schema reference, and `defaultTest` applies one rubric across cases.

You cannot run either tool without having written the criterion first. A rule
telling a person to do the same thing is strictly weaker.

### E-05 — checkers ship with deliberately broken inputs

**Covered by:** Gherkin (survey 32).

`testdata/good/*.feature` (50 files) and `testdata/bad/*.feature` (12 files).
Shipping invalid fixtures means parsers are held to rejecting the right things,
not only to accepting the right things.

This is the same idea the inventory states as a rule, implemented as a shipped
artefact, and it has been stable for years.

### F-15 — roles are constrained by the tools they are given

**Covered by:** VoltAgent (survey 14), CrewAI (survey 16).

VoltAgent scopes each agent to its grant (`tools: Read, Write, Edit, Glob,
Grep`) and then reasons from it in the prompt: "You cannot run a message bus,
spawn processes, open sockets, or execute a workflow engine. Do not claim to."

That is the mechanism plus the explanation of why it binds. Nothing needs
adding.

### H-02 — named categories of premature infrastructure

**Covered by:** VoltAgent (survey 14).

The same file forbids planning around "an imagined RPC/queue/WebSocket layer".
A published agent definition already carries the warning, aimed at the same
components.

---

# Bucket 4 — something else does it better

Eighteen entries. Each names what to change or drop.

### A-04 — verifying the brief against the files

**Better: agents-lint (survey 12).**

The inventory states a discipline: read the brief, open what it cites, stop if
they disagree. `agents-lint` does the resolvable part mechanically —
`checkFilesystem` extracts mentioned paths, skips URLs and environment
variables, resolves each against the repository root, and reports missing ones
at configurable severity. `npm-scripts.ts` and `dependencies.ts` do the same for
scripts and packages.

**What to change.** Keep the discipline for claims a machine cannot resolve.
Adopt a path-and-command check for the claims it can. A rule that a tool can
enforce should not stay a rule.

### B-02 — a check must have a way to go red

**Better: Gherkin (survey 32), SWE-bench (survey 24).**

The inventory asks an author to consider what would make a check fail.
Gherkin ships the failing cases. SWE-bench goes further and makes "done"
two-sided: `FAIL_TO_PASS` (must start passing) alongside `PASS_TO_PASS` (must
not break), so a fix that breaks something else does not count.

**What to change.** Restate the rule as an artefact requirement — a check ships
with the input that breaks it — rather than as a question to ask oneself.

### B-03 — structure passing is not content passing

**Better: agents-lint (survey 12), SWE-bench (survey 24).**

The survey's own cross-cutting finding splits the ecosystem in two: tools where
a parser or a hash decides, and tools where a model is asked to look. agnix
(survey 11) checks structure and per-tool character limits; agents-lint checks
whether the claims resolve. Both call it validation.

**What to change.** The inventory states the distinction. The kit should ship
the vocabulary for it — two different words — because the ecosystem uses one
word for both and that is where the confusion lives.

### B-08 — conflicting records: surface both, adopt neither

**Better: Doorstop (survey 30).**

Doorstop turns this into arithmetic. An item carries a content hash; the
`reviewed` property recomputes the stamp and compares, so editing the text or
its links silently un-reviews it. A link stores the parent's stamp as it was
when the link was made; if the parent later changes, `cleared` returns false and
the link is flagged suspect.

That is conflict detection propagating across a graph, in plain files, in
version control — where the inventory has a person noticing.

**What to change.** This is the single strongest mechanism in the corpus for
"documents are the source of truth, and they drift". K5 should decide whether
the kit adopts stamping or explicitly declines it.

### B-10 — regenerate, never adjust

**Better: awesome-claude-code (survey 21).**

Its `Makefile` states the contract: one CSV is the source of truth, `make
generate` renders it into the README, "Generation is idempotent (re-running
yields a byte-identical README.md) and fails closed if an Active entry has a
Category missing from config.yaml."

Byte-identical output on re-run makes a hand-edit detectable. The inventory
relies on nobody hand-editing.

**What to change.** Drop the rule; adopt idempotent generation wherever a
derived figure exists.

### C-02 — a small fixed set of governing documents

**Better: arc42 (survey 28) — for one specific mechanism.**

arc42's twelve sections are a comparable partition and not obviously worse. But
arc42 has something the inventory does not: the guidance ships *inside* the
template, wrapped in `ifdef::arc42help[]` blocks, so a team renders a guided
version while learning and a clean version for publication. The scaffolding is
removable without editing the document.

**What to change.** This is a direct input to K6, which has to teach without a
worked example. A toggleable help layer is a published answer to that problem.

### C-04 — a generated overview that holds no authority

**Better: awesome-claude-code (survey 21).**

Same mechanism as B-10. The inventory asks a human to keep an overview in sync
by hand, and names the constant temptation to record something only there.
Generation plus fail-closed validation removes both.

**What to change.** Drop the hand-maintained version. This entry was already
marked for dropping in the founder review; the survey supports that.

### C-05 — the decision log

**Better: adr-tools (survey 26) for mechanics, MADR (survey 27) for content.**

adr-tools makes relationships operational: `adr new -s <n>` supersedes a prior
record and mutates both files, and links are bidirectional by construction.
MADR supplies what a four-section template omits — `Decision Drivers`,
`Considered Options`, a forced `Chosen option … because` clause, and
`Consequences` split into "Good, because" and "Bad, because" lines.

Both are older, simpler, and have artefacts that survive their tooling.

**What to change.** Do not design a decision-record format. Adopt MADR's shape
and adr-tools' supersession, and say so.

### C-06 — identifiers assigned by one role

**Better: adr-tools (survey 26).**

The inventory has a role reading the integrated state and issuing a number,
with a placeholder for anything unassigned, and a queue as the stated cost.
`adr new` computes the next number from the directory and prints the filename to
stdout so it can be used in scripts.

No role, no queue, no placeholder.

**What to change.** This is the mechanism the founder asked to keep as
configuration rather than as a rule. adr-tools is what that configuration looks
like, in POSIX shell and awk, and it has existed since 2020.

### C-07 — a holding area outside active scope

**Better: the Rust RFC process (survey 33).**

The inventory keeps deferred questions in a separate document that accumulates,
with "it becomes a burial ground" as its stated cost. The RFC process has
**Postponement** as a defined state inside one lifecycle — a documented answer
to "not now" that does not require a second document.

**What to change.** Consider a status field over a separate file.

### D-01 — the six-part brief

**Better: the Rust RFC template (survey 33).**

The six headings cover purpose, scope, prohibitions, completion, validation and
reporting. The RFC template mandates the sections people avoid: `Drawbacks`
("Why should we *not* do this?"), `Rationale and alternatives` ("What is the
impact of not doing this?"), `Prior art`, and `Unresolved questions` split by
*when* each resolves — before merge, before stabilisation, or out of scope.

It also separates a guide-level explanation from a reference-level one, forcing
a proposal to hold up at two altitudes. And it fences `Future possibilities`
against misuse in as many words.

**What to change.** The brief has no section that argues against the work. That
is a real omission and the fix is published.

### D-05 — size is a boundary

**Better: superpowers (survey 20).**

A file-count boundary is arbitrary. superpowers defines
task granularity by a review criterion instead: the smallest unit that carries
its own test cycle and is worth a fresh reviewer's gate, split only where a
reviewer could meaningfully reject one task while approving its neighbour.

**What to change.** Replace the file count with the review criterion.

### F-09 — three endings for a surviving disagreement

**Better: the Rust RFC process (survey 33).**

Settle, park, or stop is a lead's judgement made in private. The RFC lifecycle
has named public states, a Final Comment Period, and defined authority for who
moves between them.

**What to change.** The inventory's version depends entirely on one agent
judging well. Named states do not.

**The caveat, which matters.** The RFC process works by gatekeeping — named
teams with standing. The survey says so plainly. That is not transplantable to a
project without them, so this is a partial adoption at best.

### F-11 — repeated failure stops the round

**Better: SWE-bench (survey 24).**

The rule is "two deaths mean the environment is at fault". SWE-bench ships
`infra_failure.py` to separate a harness failure from a real failure — a
distinction the survey notes most evaluation code omits, and without which
scores are quietly wrong.

**What to change.** Make the distinction a recorded outcome, not a heuristic
about counting deaths.

### F-12 — the round record

**Better: MADR (survey 27).**

The inventory requires attribution so the human can trace a position to whoever
held it. MADR encodes exactly that in frontmatter, from a responsibility model:
`decision-makers`, `consulted` ("subject-matter experts; and with whom there is
a two-way communication"), `informed` ("one-way communication").

**What to change.** Adopt the role vocabulary rather than free prose
attribution.

### H-06 — the cost to the maintainer later

**Better: adr-tools (survey 26).**

Its template's fourth section is Consequences, framed as "What becomes easier or
more difficult to do and any risks introduced". That is the same question
without the assumption of a single maintainer — which is the change the founder
already asked for in review.

**What to change.** Adopt the wording. It solves the transferability problem
this entry was flagged for.

### H-07 — contest the premise first

**Better: the Rust RFC template (survey 33).**

The inventory makes this the adversary's highest-value objection, dependent on
an adversary being present and doing its job. The RFC template makes it a
section every proposal must fill.

**What to change.** Move it from a role's behaviour into the artefact.

### H-08 — name the minimal alternative

**Better: the Rust RFC template (survey 33), MADR (survey 27).**

`Rationale and alternatives` and `Considered Options` both require it in
writing. MADR forces the justification clause that follows it.

**What to change.** Same as H-07: put it in the template, not in a role.

---

# Bucket 2 — partly covered

The kit says what it adds and what it assumes.

| Mechanism | What exists | What is missing |
|---|---|---|
| A-01 version control reserved to the human | GSD ships harness hooks including a commit validator (survey 4); Inspect AI has a first-class approval layer gating tool calls mid-run (survey 22) | No surveyed project forbids the agent from version control. The machinery exists; the boundary does not |
| A-02 agents never author a decision | The RFC process gives decisions a human acceptance gate (survey 33) | Nothing prevents an agent writing one, and nothing defines the stop-and-report response |
| A-03 one authorised unit at a time | GSD ships a phase-boundary hook (survey 4) | The survey records GSD's guards as advisory and off by default |
| B-01 figures carry their derivation | VoltAgent forbids inventing numbers: "If you have not measured something, do not state it as a fact" (survey 14) | The positive requirement — carry the command and what would invalidate it — appears nowhere |
| B-06 unmeasured is marked unmeasured | Same VoltAgent constraint | No fixed marker, and no rule keeping unmeasured figures out of documents entirely |
| B-07 no invented sources | Same VoltAgent constraint | Nothing covers invented precedent as distinct from invented numbers |
| C-01 one owner per category of fact | Diátaxis supplies a decision procedure for where content belongs (survey 29); arc42 assigns one topic per section (survey 28) | Nothing detects that two documents state the same fact. Diátaxis ships no linter or classifier at all |
| D-03 scope echoed back before editing | Agent OS mandates the host's structured question tool and stops if not in plan mode (survey 5); superpowers requires a file-structure map before tasks (survey 20) | Neither requires the agent to state what is out of scope |
| D-04 checks and documentation inside the unit | superpowers ships `verification-before-completion` (survey 20); Spec Kit's pipeline sequences them (survey 1) | The survey records that nothing verifies compliance — it is a prompt, not a check |
| E-04 a pass names its blind spots | Two projects publish retreats from a design in source: Spec Kit's empty `FORK_CONTEXT_COMMANDS` citing issue #3185, and VoltAgent's constraint block (survey, cross-cutting 4) | Publishing a known limitation is not the same as a check enumerating what it did not examine |
| F-01 a convenor holding no stake | Magentic-One's orchestrator selects the next speaker without doing the work (survey 17); CrewAI has a manager role (survey 16) | The conflict-of-interest argument — a convenor that owns design reviews its own work less harshly — is stated nowhere |
| F-02 a standing adversary | Adversarial priors exist per task, e.g. "Default assumption: The modification goal has NOT been achieved until proven otherwise" (survey 13) | An adversary present in every round, by rule, does not exist in the corpus |
| F-04 partition by authority | Role catalogues split by function and technology (surveys 13, 14, 16); CrewAI forces `expected_output` per task | Splitting by who holds authority over an answer, rather than by topic, appears nowhere |
| F-05 one prepared briefing | VoltAgent documents that subagents coordinate through shared files and the orchestrator, and nothing else (survey 14). Spec Kit's #3185 is the negative evidence: forked context compounded until sessions froze | A curated pack, restated rather than quoted, is absent |
| F-13 the escalation format | The RFC template and MADR both structure a decision for a reader (surveys 33, 27) | Neither is shaped for an interruption mid-work, and neither forbids a transcript |
| H-01 generalise on the second real case | VoltAgent forbids designing against imagined infrastructure (survey 14) | The second-use trigger is not stated as a rule anywhere |
| H-05 ask how it fails quietly | SWE-bench's `PASS_TO_PASS` is the mechanical form: a change that quietly breaks something else fails (survey 24) | Nothing asks the question of a design before it is built |
| D-02 the standing report | Magentic-One keeps a per-turn ledger of structured questions — `is_request_satisfied`, `is_in_loop`, `is_progress_being_made` (survey 17) | The report's load-bearing items — work done that was not asked for, work asked for and skipped, inaccuracies in the brief — have no counterpart |

---

# Bucket 3 — not covered in the surveyed corpus

Thirty-one entries. This is the kit's possible contribution, and it needs
reading carefully, because a gap in a survey is not a gap in the world.

### Genuinely absent, and the survey looked

- **E-01** one named aggregate command that may be added to but never
  substituted
- **E-02** enforcement in configuration that actually blocks. The survey's own
  cross-cutting finding is that enforcement is nearly always advisory, and that
  the sole harness-level attempt advises rather than blocks and ships disabled
- **E-03** a blocking check with a budget that reports to a human when spent
- **F-03** predictions committed before exposure to anyone else's work
- **F-06** per-participant reading lists, with out-of-list reads declared
- **F-07** all responses read before any is answered
- **F-08** one challenge per position, then closed
- **F-10** unanimity treated as a warning, with named symptoms and an
  intervention
- **F-14** roles created only once their subject exists
- **F-16** failure histories earned locally and never imported
- **B-04** the three-variable rule for what a search actually observed
- **B-05** enumerate rather than interrogate
- **A-05** out of remit means name the owner and stop
- **A-06** verification machinery owned by one role regardless of who finds the
  fault
- **A-07** one document no agent may edit
- **C-03** documents describe the present, not the change
- **H-03** name which declared non-goal the work drifts toward
- **H-04** stored material nothing consumes

### Absent, but the survey was not pointed here

Weak evidence. Recorded so K5 does not mistake it for a finding.

- **G-01 to G-06** — the six rules about writing to the human. No surveyed shape
  concerns the report an agent gives a person. Diátaxis is about documentation
  for readers, which is a different artefact
- **J-01 to J-03** — the standing partner above the repository, the human
  carrying messages between layers, and whole reports travelling upward. The
  survey's own recorded absence (b) is adjacent: within the corpus opened,
  nothing evaluates a project's own agent-facing scaffolding against that
  project
- **I-01 to I-03** — environment hazards. These describe one tool at one
  version. K4 should consider dropping them outright rather than shipping them

### One entry that is in bucket 3 wrongly, and the reason

**E-06, deliberate breakage.** Nothing in the corpus does it. But mutation
testing is a mature discipline with established tools outside this survey, and
none of the six shapes would have found them.

Placing E-06 in bucket 3 would be exactly the failure K3 is meant to avoid:
claiming a contribution because the survey did not look. **The honest status is
NOT ESTABLISHED**, and a targeted search is needed before K4 rules on it.

---

## What this phase found

**Bucket 4 has eighteen entries.** The largest single source is the Rust RFC
template, which mandates four arguments the inventory's brief never asks for.
The second is the pair of decision-record projects, which between them already
solve numbering, supersession, alternatives and consequences.

**The pre-agent systems account for almost all of bucket 4.** Of the eighteen,
fourteen point at projects that predate coding agents. The survey said this
plainly as a cross-cutting finding, and mapping the mechanisms confirms it: the
problems the method solves by discipline were solved mechanically years ago, by
tools that are still maintained.

**Enforcement is where the method might genuinely contribute.** E-01, E-02 and
E-03 are in bucket 3 with the survey's own evidence behind them. If the kit
ships something that actually blocks, that is a contribution nothing in
thirty-three projects makes. If it does not, the kit is one more advisory kit.

**Two areas of bucket 3 are untested, not empty.** Writing to the human, and the
layer above the repository. K5 must not treat either as established
contribution.

## What could not be established

- **Whether any of it works.** No tool in the survey was executed, and the
  method has one practitioner. This document compares descriptions of
  mechanisms, not outcomes.
- **E-06's status**, as above.
- **Whether the eleven unopened repositories change any bucket.** The survey
  names them as its most likely gaps. Three of them are Shape 5 evaluation
  harnesses, which is where bucket 3 currently looks thinnest.
