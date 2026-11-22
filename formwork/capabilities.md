# What formwork can do

Everything the kit offers, on one page, with one plain example each. For a
person finding their way, and for an agent asked "what can you do here?".

**For an agent:** when somebody asks what you can do in this project, answer
from this page, in their words, and name the file behind each answer. Say what
is enforced and what is advice. Do not offer what is not on this page. When a
row says NOT ESTABLISHED, say that too.

---

## By what you want to do

| You want to | Use | Example |
|---|---|---|
| **start from one sentence** | routing, [`route.md`](route.md) | "add dark mode" is said back as kind, size, team and first brief before anything happens |
| **plan** | the `director` role; the brief and spec templates; the standing brief | "use the director to write me a brief for a photo renaming tool; do not build" |
| **argue a costly choice** | a round, [`round.md`](round.md), run by the `lead`, with the `challenger` writing predictions first | "run a round on whether we move to Postgres" |
| **research a question** | the research pack, [`research/README.md`](research/README.md); the `research-question` skill; the `researcher` role | "is the new prompt better? Write the question card with me first" |
| **build** | a working session on one brief; the 21 pack roles; the operations ladder | "here is brief 0007; do only that, run `formwork check`, report and stop" |
| **build in parts, or with several sessions** | the operations pack, [`operations/README.md`](operations/README.md) and [`operations/parallel.md`](operations/parallel.md) | "plan the ladder for the parser, the planner and the writer before any end to end test" |
| **measure** | the evaluation plan; spending in stages; [`measure-a-guard.md`](measure-a-guard.md); the routing eval | "plan the measure, free checks first, and tell me what stage 1 costs" |
| **review** | the `reviewer` role; the review round template (review, then refute); the taste packs | "review this diff, then have each serious finding refuted or kept" |
| **report** | the report template, `## For you` first; the `report-shape` check | every finished brief leaves `docs/reports/NNNN-name.md` |
| **decide** | `docs/decisions/`, written by you only; the director's decision log for rulings between lanes | "record decision 0004 in my words" |
| **release** | the release step and the sourced release checklist, checked by somebody who built none of it | "check every release row on a fresh build" |
| **pick up where you left off** | the standing brief, `docs/standing.md` | "read the standing brief and tell me where we are in four lines" |

---

## The method

| Piece | What it is | Where |
|---|---|---|
| The loop | brief, work, check, report, stop, you say go | [`../FORMWORK.md`](../FORMWORK.md), [`loop.md`](loop.md) |
| Five sizes | task, checkpoint, round, phase, milestone | [`loop.md`](loop.md) |
| Briefs | numbered files, `docs/briefs/NNNN-name.md`, open until your read back | [`templates/brief.md`](templates/brief.md) |
| Reports | same number, `## For you` first, that part under 1,000 words | [`templates/report.md`](templates/report.md) |
| The standing brief | the one file that says where the project is | [`templates/standing.md`](templates/standing.md) |
| Decisions | numbered, written by the human only | [`templates/decision.md`](templates/decision.md) |
| Rounds | several roles argue one question, predictions first | [`round.md`](round.md), [`templates/round.md`](templates/round.md) |
| Threads | how work is handed down and reported back up | [`threads.md`](threads.md) |
| Routing | one plain prompt to a kind, a size and a team | [`route.md`](route.md) |
| Style | how the agents talk to you; your `docs/style.md` wins | [`style.md`](style.md) |

---

## The roles

28 roles, each one file saying what the job is and where it stops. Your agent
gets one generated file per role; edit the source in `roles/` and run
`formwork roles`.

| Group | Roles |
|---|---|
| **Method** (run the work) | `director` (what happens next), `lead` (running other agents), `challenger` (the case against), `architect` (structure and authority), `researcher` (measurement), `reviewer` (reading the diff), `record-keeper` (repository integrity) |
| **Packs** (do the work) | `backend`, `frontend`, `mobile`, `data`, `devops`, `sre`, `integrations`, `performance`, `security`, `tester`, `ai`, `analyst`, `accessibility`, `ux`, `visual`, `writer`, `product`, `brainstormer`, `user-researcher`, `marketing`, `legal` |

Example: "use the security role; read `formwork/guard/` and tell me what an
attacker tries first". A role you need and do not have is written by brief
into `roles/project/` ([`roles/HOW-TO-ADD-A-ROLE.md`](roles/HOW-TO-ADD-A-ROLE.md)),
never pasted as a persona.

---

## The packs (optional, never a check)

| Pack | What it gives | Where |
|---|---|---|
| **Taste** | three kit items for every product, and packs for screens, web, decks, iOS and motion | [`taste/README.md`](taste/README.md) |
| **Research** | a method for learning by building, a question card, an evaluation plan, 21 pitfalls | [`research/README.md`](research/README.md) |
| **Operations** | the ladder, limits on fixing, spending in stages, the per route ship rule, frozen contracts, the decision log, the release checklist, running many sessions, 14 pitfalls | [`operations/README.md`](operations/README.md) |

---

## Skills

| Skill | Does | Where |
|---|---|---|
| `humanizer` | rewrites text the agent sends as you, so it reads like you | [`skills/humanizer/`](skills/humanizer/) |
| `research-question` | writes a research question card with you and checks it against the pitfalls | [`skills/research-question/`](skills/research-question/) |

`formwork roles` places them in `.claude/skills/` for Claude Code. On the other
runtimes the agent reads the skill file directly. Bringing in somebody else's
skill: [`bring-a-skill.md`](bring-a-skill.md).

---

## Templates

| Template | For |
|---|---|
| `brief`, `report`, `standing`, `decision`, `round`, `predictions` | the method, every project |
| `spec`, `research-lane`, `design-round`, `build`, `review-round`, `release-step` | a phase, offered by kind, never required |
| `research-question`, `evaluation-plan` | the research pack |
| `ladder-plan`, `decision-log`, `release-checklist`, `parallel-worker-brief` | the operations pack |
| `routing`, `personal-defaults`, `project-instructions`, `readme-section`, `upstream` | setting a project up |

All in [`templates/`](templates/).

---

## What refuses (enforced)

**Three guards**, wired into your agent as hooks. On Claude Code: before every
shell command and every file write, and when a turn ends.

| Guard | Refuses | Example |
|---|---|---|
| `git-boundary` | the agent writing to version control | "commit this" is refused; you commit |
| `protected-files` | the agent quietly changing what enforces the rules | an edit to a check is refused; the agent stages a patch instead |
| `quality-gate` | a turn ending while `formwork check` is red (three refusals, then it stands aside) | the agent must fix or report a red gate before it stops |

**Nineteen checks**, run together by `formwork check`. Each ships an input it
must reject and one it must accept; `formwork demo` shows them failing.

| Check | Says red when |
|---|---|
| `config-shape` | `.formwork.toml` is not the shape the pages describe |
| `decision-ids` | a decision number was guessed or repeated, or a superseding link is broken. `--next` prints the next number |
| `doc-links` | a link points at nothing |
| `gates` | a brief starts before its `starts:` gate |
| `generated-current` | a generated role differs from its source |
| `guard-wired` | a declared runtime has no guard wiring |
| `hidden-unicode` | a kit file carries a character nobody can see |
| `kit-integrity` | something that enforces changed without being recorded |
| `kit-leak-scan` | a kit file carries a home path, address, email or key |
| `predictions-first` | the challenger read before predicting |
| `report-shape` | a report does not open with `## For you`, or runs long |
| `role-shape` | a role is incomplete, or two roles claim one job |
| `roles-named` | a round or brief names a role that does not exist |
| `rule-labels` | a rule is unlabelled, has no `Catches:` line, or names a check that does not exist |
| `skill-provenance` | a skill does not say where it came from |
| `standing-current` | the standing brief is empty or older than the record |
| `style-pointed` | a generated role does not point at the style page |
| `task-size` | a task grew past a task without saying so |
| `work-paired` | finished work left no report or read back, or more briefs are open than `open_briefs` allows. `--next` prints the next brief number |

**48 rules**, nearly all advice, each saying what it catches and naming the
check when one enforces it: 14 daily in [`rules/core.md`](rules/core.md), 34
in [`rules/full.md`](rules/full.md). Drop one by deleting it, never by a
setting.

What the guards cannot stop: [`limits.md`](limits.md).

---

## The adapters

| Agent | Instruction file | Can it block a command? |
|---|---|---|
| Claude Code | `CLAUDE.md` | yes, seen doing it |
| Codex | `AGENTS.md` | it should; nobody has tried |
| Cursor | `AGENTS.md` | it should; nobody has tried |
| Gemini CLI | `GEMINI.md` | it should; nobody has tried |

Each has a page in [`adapters/`](adapters/) saying what wires the guards in.

---

## The commands

| Command | Does |
|---|---|
| `formwork init` | puts `formwork/` and `FORMWORK.md` in your project |
| `formwork install` | wires the guards into your agent and writes the role files. `--runtime <name>` when it cannot tell |
| `formwork setup` | asks a few questions once; writes your style, standing brief, folders and the routing lines |
| `formwork check` | runs every check: green or red |
| `formwork demo` | shows each check refusing a broken input |
| `formwork roles` | regenerates role files and skills after an edit |
| `formwork record` | records the fingerprints after you changed something that enforces; yours to run |
| `formwork test` | runs every test in the kit |
| `formwork sync` | brings the project's kit copy up to the installed release. `--dry-run` first |
| `formwork where`, `formwork version` | where the installed kit lives, which release it is |

Without the installed command, `formwork/fw <name>` runs the same `install`,
`setup`, `check`, `demo`, `roles`, `record` and `test`. `init`, `where` and
`version` belong to the installed command only. `formwork/fw sync <target>`
works the other way round: from a clone of the kit, onto another project.

---

## Settings

One file, `.formwork.toml`, protected from the agent. `[bindings]` says which
agent you use; `[strength]` says how hard the guards bite (`git_boundary`,
`protect_files`, `aggregate_gate`: block, warn or off), the gate's refusal
budget (`gate_budget`), how many briefs may be open (`open_briefs`, per
project or per stream with `open_briefs_per`), and how long your read back
must be (`read_back_words`). The README's settings section has the whole file.

---

## Measuring the kit itself

| What | Where |
|---|---|
| routing accuracy, measured | [`evals/routing/`](evals/routing/), result in [`route.md`](route.md) |
| what a guard changes, with three arms | [`evals/guards/`](evals/guards/), method in [`measure-a-guard.md`](measure-a-guard.md) |
| what a round costs | NOT ESTABLISHED, see [`COSTS.md`](COSTS.md) |

---

## Your first fifteen minutes

[`first-run.md`](first-run.md): install, watch a guard refuse, and do one small
real piece of work.

---

## When something goes wrong

[`troubleshooting.md`](troubleshooting.md) for every error message,
[`glossary.md`](glossary.md) for every word, [`limits.md`](limits.md) for what
the kit cannot do.
