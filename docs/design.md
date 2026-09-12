# Kit design

**Phase:** K5. **Date:** 2026-09-12.

> ## Read this first: it is a record, not a description
>
> **This document says what was planned before the kit was built. It has not
> been updated to match what was built, and parts of it are now wrong.**
>
> An audit found several: it says nine checks were designed and six built (all
> nine exist), that nothing is generated (81 files are, and a check enforces
> it), that `full.md` holds 43 rules (it holds 33), and it points at an
> `adapters/CONTRACT.md` that was never written. Its configuration example
> shows a `[rules]` section that a check now refuses.
>
> **It is kept as written on purpose.** Rewriting a design record to match what
> was built destroys the only evidence of what changed and why — which is the
> same rule the kit applies to decision records.
>
> **For what the kit actually is**, read [`../FORMWORK.md`](../FORMWORK.md) and
> [`../formwork/first-run.md`](../formwork/first-run.md). For what went wrong
> along the way, read [`dogfood.md`](dogfood.md).

What a fork contains, why each part is there, what is enforced, and what it
costs to run.

**This phase writes no kit file.** It names them and says what each is for. K7
builds them.

## What it is designed from

K1 catalogued 71 mechanisms. K3 found 18 that something else does better and 4
already covered well. K4 dropped 14, marked 10 for mechanical enforcement,
weakened 15, and put 12 behind warnings.

**56 mechanisms survive in some form.** A kit that hands someone 56 rules on day
one is a folder, so the central design decision here is layering, not content.

---

# 1. What a fork contains

```
<your project>/
├── README.md                  ← yours, not ours
├── FORMWORK.md                ← the core. One page. Read this first
├── formwork/
│   ├── rules/
│   │   ├── core.md            13 rules. Day one
│   │   └── full.md            the remaining 43, by group
│   ├── roles/
│   │   ├── method/            6 roles the method needs
│   │   ├── packs/             21 more, in 4 packs: product, design,
│   │   │                      software, ship
│   │   ├── project/           yours. Starts empty
│   │   ├── TEMPLATE.md        five required sections
│   │   └── HOW-TO-ADD-A-ROLE.md
│   ├── loop.md                the one loop, and its five sizes
│   ├── templates/
│   │   ├── brief.md
│   │   ├── report.md
│   │   ├── decision.md        MADR shape, adopted not invented
│   │   └── round.md
│   ├── check/
│   │   ├── run                the aggregate. One command
│   │   ├── checks/            one program per check
│   │   └── fixtures/          one failing input per check
│   ├── adapters/
│   │   ├── CONTRACT.md        how to write one
│   │   ├── claude-code/
│   │   ├── codex/
│   │   ├── cursor/
│   │   └── gemini-cli/
│   └── COSTS.md               what this costs, and what is unmeasured
├── docs/                      your governing documents, empty with guidance
└── .formwork.toml             your configuration
```

## Why each part

**`FORMWORK.md`** — one page at the root. What this is, the loop, the thirteen
core rules, and what is enforced. Someone who reads only this can work.

**`rules/core.md` and `rules/full.md`** — the tiering is the answer to a kit the
size of its inventory. Core is what applies to every piece of work. Full is
reference, read when you hit the situation it covers.

**`roles/`** — two kinds, kept apart. See section 5c.

**`templates/`** — the decision and round templates are adopted from published
work rather than designed here. K3 found both already solved.

**`check/`** — the aggregate and its parts. `fixtures/` is not optional: a check
ships with the input that breaks it, and the aggregate fails if a fixture
passes.

**`adapters/`** — four wiring files plus the contract. All four runtimes refuse
a tool call on exit code 2, so there is one program and four ways of attaching
it.

**`docs/`** — the governing documents arrive empty, with guidance inside them
that can be switched off. Adopted from arc42's toggleable help mechanism, which
K3 identified as a published answer to teaching without a worked example.

**`.formwork.toml`** — configuration, structured to keep three layers apart. See
section 4.

---

# 2. The loop

One loop. Five names for how big a turn of it was.

```
   ┌─────────────────────────────────────────┐
   │                                         │
   ▼                                         │
 BRIEF  ──▶  WORK  ──▶  CHECK  ──▶  REPORT  ─┴─▶  STOP
                          │
                          └── red: cannot finish
```

| Size | Span | Brief | Report |
|---|---|---|---|
| Task | minutes | one line | changed files, check result |
| Checkpoint | one sitting | six sections | the full standing list |
| Round | hours–days | questions per role | the round record |
| Phase | weeks | what it settles | one document |
| Milestone | months | a direction | — |

Every size answers the same four questions: what it produces, what must be true
before it starts, who authorises it, and **what would tell us it failed.**

The task exists because K4 found the brief and report do not scale down, and
that work which does not scale down gets bypassed.

---

# 3. Enforced, or advice

Every rule is one or the other. A rule that is neither is a rule broken
silently.

## Enforced — 9 designed, 6 built

Each is a program with an exit status. The adapter wires it to the runtime.

**Six exist today.** The version-control boundary, the aggregate, the
both-kinds fixture rule, the configuration-shape check, the link check, and the
wiring check. The remaining three arrive in B6, and until they do this table
describes an intention rather than a fact.

| Rule | Mechanism | When it runs |
|---|---|---|
| **Version control is the human's** | pre-tool hook matching write subcommands, refusing with exit 2 | every tool call |
| **The aggregate is named, not substituted** | one command; the hook invokes it by name | turn end |
| **Enforcement lives in configuration** | the hook itself | turn end |
| **A blocking check has a budget** | bounded refusals per session, then escalate | turn end |
| **A check must be able to go red** | every check has a fixture; the aggregate fails if a fixture passes | aggregate |
| **Verify the brief against the files** | resolve paths and commands named in the brief | aggregate |
| **Regenerate, never adjust** | derived files must regenerate byte-identical | aggregate |
| **Identifiers come from the record** | next number computed from the directory; no placeholders survive | aggregate |
| **Predictions before exposure** | the predictions file must predate the other reports | round start |

## Declined, in writing — 1

**Content stamping for conflicting records.** K4 marked it for mechanical
enforcement and left the choice here.

**Declined for the first version.** It forces a file format on every governing
document, it is the heaviest mechanism proposed, and nobody has asked for it.
The published implementation is named in the gap map, so a fork that wants it
knows where to look.

Declining in writing is the required outcome. Leaving it unaddressed was not.

## Advice — 46

Everything else. Carried in `rules/core.md` and `rules/full.md`, each line
labelled **advice** in the file itself.

**Thirteen are core**, meaning they apply to every piece of work:

| Rule | |
|---|---|
| One authorised unit at a time | advice |
| Agents never author a decision | advice |
| Out of scope: name the owner, stop | advice |
| Figures carry the command that produced them | advice |
| Structure passing is not content passing | advice |
| An empty search describes the query, not the world | advice |
| Unmeasured is marked unmeasured | advice |
| The brief has six sections | advice |
| The report answers a fixed list | advice |
| Contradictions go first | advice |
| Corrections are stated, not absorbed | advice |
| Favour the modest claim that holds | advice |
| Failure lists are earned, never imported | advice |

The remaining 33 live in `full.md`, grouped as the inventory groups them.

**Twelve of the 46 carry a warning**, printed in the rule itself, not in a
footnote. The warnings come from K4 and say what the rule costs or where it
stops working.

---

# 4. Configuration — three layers, kept apart

K0 fixed three layers and forbade collapsing them. `.formwork.toml` keeps them
in separate blocks so that changing one cannot look like changing another.

```toml
[bindings]          # one person's setup. Change freely
runtime   = "claude-code"
docs_dir  = "docs"
check_cmd = "formwork/check/run"
roles     = ["lead", "challenger", "architect", "reviewer"]

[strength]          # how hard each enforced rule bites
git_boundary   = "block"   # block | warn | off
aggregate_gate = "block"
brief_refs     = "warn"
# defaults are strict. A team may need warn; a solo builder should not

[rules]             # NOT a switch board
# Rules are not disabled here. Dropping one is an edit to rules/core.md,
# which leaves a line in version control with your name on it.
```

**Why rules are not in the configuration.** A kit whose every rule can be
switched off is a folder. Dropping a rule must be a line the forker wrote, never
a default they never saw.

**No knob exists that nothing asked for.** Bindings and strength are the two
things already known to vary. Nothing else is configurable, because nobody has
forked this and there is no evidence about what else varies.

---

# 5. Adapters

| Runtime | Label | What the fork gets |
|---|---|---|
| Claude Code | **tested** | blocking, observed working |
| Codex | untested | blocking, per the publisher |
| Cursor | untested | blocking, per the publisher |
| Gemini CLI | untested | blocking, per the publisher |
| opencode | **partial** | blocks the main agent; **subagent calls bypass it** |
| Aider | **incompatible** | the version-control boundary cannot hold. Stated in those words |
| anything else | advice only | the rules apply; nothing enforces them |

The label ships next to the adapter, not in a table someone has to find.

`CONTRACT.md` states the whole interface: run a command, non-zero means refuse.
Any runtime that can do that can have an adapter, written by anyone.

---

# 5b. The agent files — instructions, roles, skills

**This section was missing from the first draft of this design, and its absence
made section 5 wrong.** An adapter is not one small wiring file. The exit-code
contract covers the hook and nothing else. Everything a runtime reads *before*
a tool call is in that runtime's own format.

## What each runtime needs

Four kinds of file, not one.

| Kind | What it is | Same across runtimes? |
|---|---|---|
| **Instruction file** | the standing context — the rules, the loop, the boundaries | **Mostly.** One published convention covers about twenty tools |
| **Role definitions** | one file per role, with its tool grant | **No.** Different directory, different frontmatter |
| **Skills or commands** | named procedures, invoked by name | **No.** Different directory and invocation |
| **Hook wiring** | attaching the check | **No**, but the program behind it is shared |

## The instruction file

A cross-tool convention already exists for this and the survey recorded roughly
twenty tools honouring it. Several surveyed projects ship that file plus one
thin file per tool that points at it.

**Design: one instruction file is the source. Per-tool files are one line each,
pointing at it.** No duplicated prose, so no drift.

## Roles and skills

These have no shared convention. Directory, filename and frontmatter differ per
runtime, and a role's tool grant — the one place besides the hook where a rule
becomes configuration — is expressed differently in each.

**This forces generation, and it corrects a decision made earlier in this
document.** Section 10 originally said nothing is generated. That is right for
a status view and wrong here: four hand-maintained copies of every role is
exactly the duplication C-01 calls drift, and the survey found the established
answer is one source generated outward, with a validator over the output.

**Design:**

```
formwork/
  roles/<role>.md         ← the source. One per role, runtime-neutral
  skills/<name>.md        ← the source. One per procedure
  build                   ← generates the per-runtime files
  adapters/<runtime>/
    layout.toml           ← where this runtime wants them, and in what shape
```

`build` is idempotent and fails closed, which is the mechanism K3 identified and
K4 marked for enforcement. Regenerating must produce byte-identical output, so a
hand-edit to a generated file is caught by the aggregate rather than surviving
silently.

## Which roles ship

See section 5c. Two kinds, and only one of them ships.

## What is NOT established here

**The role and skill file formats for Codex, Cursor and Gemini CLI.**

The runtime research of 2026-09-12 asked one question: can this runtime refuse a
tool call? It did not examine how each expects a role or a skill to be
declared.

**So `layout.toml` cannot be written for three of the four runtimes yet.** A
second research pass is required before K7 builds the generator, of the same
shape as the first: read each publisher's own documentation, cite it, and record
what is unknown.

Until that pass runs, only the tested runtime's layout is known.

---

# 5c. Roles — two kinds

The first draft listed six roles and stopped, which made the kit look like it
only suited one sort of project. Two different things were being mixed up.

## Kind 1 — roles the method needs

These are about **how work runs**. They are the same whether you are building a
phone app, running a research project, or opening a restaurant. Six ship with
the kit, ready to use.

| Role | What it does | May it start other agents? |
|---|---|---|
| **lead** | runs a round. Hands out the questions. Does no design of its own | yes |
| **challenger** | argues against whatever is proposed | **no** |
| **architect** | says what must exist and who decides what | no |
| **researcher** | measures things, and says what would make a measurement wrong | no |
| **record keeper** | documents, numbers, the gate, the boundaries | no |
| **reviewer** | reads the changes | no. Reading only |

## Kind 2 — the starter pack

These are about **what you are building**. The kit ships a strong set, ready to
use, and a way to add any others.

Not two hundred. Enough that a fork is a working team on day one.

They are grouped into packs. You switch on a pack, not twenty-five files.

**These are execution roles.** They do the work of building the thing. Roles for
running a company — hiring, sales, support, day-to-day operations, scheduling —
are deliberately absent. A project is not a company, and a kit that pretends
otherwise ships roles nobody calls.

### `product` — deciding what to make

| Role | Owns |
|---|---|
| product | what gets built, for whom, and what will not be built |
| brainstormer | generating options early, before anything narrows |
| user researcher | talking to real people, and reporting what they did rather than what they said |
| writer | words people read — names, copy, explanations, documentation |

### `design` — how it looks and works

| Role | Owns |
|---|---|
| experience | flows, structure, whether a person can actually use it |
| visual | look, identity, consistency |

### `software` — building it, when the thing is software

| Role | Owns |
|---|---|
| frontend | what runs in a browser |
| backend | what runs on a server |
| mobile | what runs on a phone |
| data | storage, schema, migrations |
| infrastructure | deployment, environments, what runs where |
| security | what an attacker does with this |
| tester | whether it works, and what would show that it does not |
| integrations | contracts with other systems, and third-party services that can fail |
| performance | speed, load, and cost per request |
| accessibility | whether people with disabilities can use it |
| observability | logs, metrics, and being able to tell what happened |
| ai | model choice, prompts, evaluation, and what the model costs |

The last five exist because each is a job that stays invisible until it is
expensive: an outside service that breaks, a page that is slow, a person who
cannot use it, an incident nobody can explain, and a model bill nobody
predicted.

**This is the build pack for software.** A project in another domain switches it
off and adds its own build roles from the template. The kit cannot ship build
roles for every domain and does not pretend to.

### `ship` — putting it in front of people

| Role | Owns |
|---|---|
| marketing | positioning, the message, the launch material |
| analyst | metrics, and what a number does and does not show |
| legal | licence, privacy, terms, intellectual property |

### Totals

| Pack | Roles | On by default |
|---|---|---|
| method | 6 | yes, always |
| product | 4 | yes |
| design | 2 | no |
| software | 12 | no |
| ship | 3 | no |
| | **27** | |

**What was removed, and why.** An earlier draft carried `market` and `business`
packs holding sales, growth, support, finance, people and delivery. Those are
roles for running a company, not for executing a project. They were cut on the
founder's instruction, and the distinction is worth keeping: **every role here
does work that produces part of the thing being built.**

## Adding your own

Every role — shipped or yours — is the same shape and obeys the same rules.

```
formwork/roles/project/<name>.md
```

Copy `TEMPLATE.md`. It has five sections, and all five are required:

> **Owns** — what this role decides
> **Does not own** — and who does
> **Tools** — which it may use, and which it may not
> **Stops when** — the point at which it names someone else and halts
> **Would be wrong if** — what tells you this role gave bad advice

A role missing any of the five does not load. That is a check in the aggregate,
not a request.

**Roles from elsewhere.** Two public catalogues hold several hundred role
definitions between them, named in the survey. `HOW-TO-ADD-A-ROLE.md` explains
converting one: keep their subject knowledge, replace their preamble with the
five sections, and set the tool grant. An imported role that has not been
converted does not load either.

## The honest label on this pack

**These twenty-seven are a guess.** Nobody has forked this kit, so there is no
evidence about which roles a fork actually needs, and F-14 says a role should
appear once its subject exists.

The pack ships anyway, because a starter kit that starts empty is not a starter
kit. The founder made that trade deliberately, and this paragraph is the record
of it.

**What would show it wrong:** K8, or a fork, using three of the twenty-seven and
ignoring the rest. The pack is sized to be cut down, not defended.

## Turning them on

```toml
[roles]
packs = ["method", "product", "software"]     # switch on a pack
add   = ["marketing"]                          # or one role
drop  = ["mobile"]                             # or switch one off
```

Packs first, then adjustments. A role that ends up off is not loaded at all —
it costs nothing in context.

This is a binding, one person's setup, so it sits in the first configuration
layer and may be changed freely.

---

# 6. What is generated, and what is written by hand

**Generated:** nothing, in the first version.

That is a deliberate and uncomfortable answer. K4 dropped the one mechanism that
answered "where are we", and its replacement is on the frozen list, waiting for
evidence that it is needed. **The kit therefore has no status view, and that is
a known hole rather than an oversight.**

**Written by hand:** everything. Briefs, reports, decisions, round records, the
governing documents.

**Checked mechanically:** the nine rules in section 3.

---

# 7. What a fork costs

Stated before anyone commits, as K5 requires.

## Measured

| Thing | Cost | Command |
|---|---|---|
| The aggregate, on a small repository | about 1 second | `time formwork/check/run` |
| Setup | one command, then wiring the adapter | — |

Both measured on this repository, which has ten files. **Wrong if** your
repository is large; the aggregate scales with file count.

## Not measured — and this is the honest part

**What a round costs in money: NOT ESTABLISHED.**

A round is a lead, up to three specialists, and an challenger. Nobody has
measured one. K4 recorded this and it is still true.

**What would measure it:** run one round, record the token usage reported by the
runtime, and multiply by the published rate. Until that is done, the kit says a
round costs an unknown amount of money and should be treated as expensive.

**There is no spend cap.** A cap is on the frozen list. Until it exists, nothing
in the kit stops a round from costing more than you expected.

**Time cost per unit: NOT ESTABLISHED.** Writing a brief takes real effort and
nobody has timed it.

## The cost that is certain

Every piece of work waits for you. That is what the version-control boundary
means. On a busy day it is the bottleneck, and it is the price of the whole
method.

---

# 8. Day one, and day thirty

## Day one

1. Fork.
2. Run setup. It writes `.formwork.toml` and wires the adapter for your runtime.
3. Read `FORMWORK.md`. One page.
4. Do one task. One line of brief, the work, the check, a short report, stop.

**One rule is enforced immediately: the agent cannot touch version control.**
That is the demonstration, and it happens in the first few minutes.

The governing documents are empty, with their guidance switched on.

## Day thirty

- A decision record with entries in it, numbered from the directory.
- Round records for whatever was argued.
- Several governing documents partly filled, guidance switched off where it is
  no longer needed.
- Two or three rules turned down from block to warn, each a visible line in
  `.formwork.toml`.
- Possibly a rule deleted from `rules/core.md`, with your reason in the commit.

**What will not exist on day thirty:** any answer to "where does everything
stand" other than reading the documents.

---

# 9. What this design does not claim

It has been used by one person, on two projects, and that person wrote it.

**No part of this kit is claimed to be better than anything in the survey.** The
survey found 33 projects, several of which are maintained by organisations,
support dozens of runtimes, and have users. This has none of those things.

Two things it does that were not found in the corpus: enforcement that refuses
rather than advises, and a set of rules about what counts as evidence. Both are
**unproven**. Whether they help anyone is unknown, and K8 is the only evidence
that will exist.

---

# 10. Decisions this phase made

Design decisions, not founder decisions. Each is reversible in K7.

1. **Rules ship in two tiers.** Thirteen core, 33 reference. Without tiering the
   design is the size of the inventory, which K3 and K4 both existed to prevent.
2. **Content stamping is declined for the first version**, with the published
   implementation named for anyone who wants it.
3. **Nothing is generated, except the per-runtime agent files.** No status view
   until the freeze lifts. Roles and skills are generated from one source,
   because four hand-maintained copies is the drift C-01 names, and the survey
   found generation to be the established answer. This corrects the first
   draft, which said nothing is generated at all.
4. **Roles come in two kinds, and both ship.** Six method roles, plus a starter
   pack of twenty-one in four packs, plus a template and a conversion guide. An
   earlier draft shipped only the six on the grounds that public catalogues
   already hold hundreds. The founder overruled it: a starter kit that starts
   empty is not a starter kit. The pack is labelled a guess in section 5c, and
   sized to be cut down.
5. **The privacy scanners do not ship.** They exist to build this repository out
   of private material. A forker has no equivalent problem, and shipping them
   would be a knob nothing asked for.

# 11. What could not be established

- **What a round costs.** The single most important missing number.
- **Whether three of the four adapters work.** Documented, never run.
- **Whether the tiering is right.** Thirteen core rules is a judgement with no
  evidence behind it. K8 will show whether people read `full.md` at all.
- **How Codex, Cursor and Gemini CLI expect roles and skills to be declared.**
  The runtime research covered blocking only. A second pass is needed before
  K7 can build the generator.
- **Whether any of this works.**
