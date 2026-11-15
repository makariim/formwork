# Formwork

A way of running a project with coding agents.

---

## The loop

Everything is one loop. Only the size changes.

```
BRIEF → WORK → CHECK → REPORT → STOP → you say go → BRIEF …
```

**The agent halts at STOP and waits for you**, however small the job was.

Five sizes run this way, from a task of minutes to a milestone of months. The
sizes, and how to pick one, are in [`formwork/loop.md`](formwork/loop.md).

Work is handed down from a planning conversation and reported back up by you.
That part is in [`formwork/threads.md`](formwork/threads.md).

**One plain prompt is enough to start.** What kind of work it is, how big, and
who does it are worked out from [`formwork/route.md`](formwork/route.md), and
said back to you in a line or two before anything happens.

---

## What is blocked

These do not ask you. They refuse.

| Rule | Enforced by |
|---|---|
| The agent never writes to version control | `formwork/guard/git-boundary` |
| One command runs every check | `formwork check` |
| Every check ships with an input that breaks it | `formwork check` |
| Every rule is labelled, and names a real check | `formwork/check/checks/rule-labels` |
| Documents link only to files that exist | `formwork/check/checks/doc-links` |
| A declared runtime is actually wired up | `formwork/check/checks/guard-wired` |
| The agent does not quietly alter the kit's own files | `formwork/guard/protected-files` |
| A turn does not end while the aggregate is red | `formwork/guard/quality-gate` |
| The standing brief is not older than the newest decision | `formwork/check/checks/standing-current` |
| Work marked finished left a report behind | `formwork/check/checks/work-paired` |
| Work marked finished carries the human's read-back, dated | `formwork/check/checks/work-paired` |
| One brief is open at a time, unless you raise the limit | `formwork/check/checks/work-paired` |
| An open brief with a `starts:` gate does not run before the gate is met | `formwork/check/checks/gates` |
| Every generated role names the style page | `formwork/check/checks/style-pointed` |
| Kit files carry no home path, private address, local hostname, email or key | `formwork/check/checks/kit-leak-scan` |
| A round file or a brief's team row names a real role | `formwork/check/checks/roles-named` |
| A report opens with a part for the human, under 1,000 words, no commands | `formwork/check/checks/report-shape` |

> [!NOTE]
> **The turn-end gate refuses three times in a session, then stands aside**, so
> a genuinely stuck turn is not trapped for ever. Change it with `gate_budget`.
> The rows below it are checks, and none of them has a budget.

Run them:

```
formwork check              everything, on your project
formwork demo  watch each check refuse a broken input
formwork check --list       what exists
```

**If you did not install the command**, every one of these works by path
instead: `formwork/fw check`, `formwork/fw demo`, `formwork/fw roles`. Run
`formwork/fw` on its own to see the list.

**To bring a project's copy of the kit up to date**, upgrade the command, then
run this inside the project:

```
pipx install --force formwork-kit==X.Y.Z
formwork sync --dry-run                 see what would change
formwork sync                           copy, delete, pin
```

From a clone of the kit itself, which only the kit's maintainer needs, the
same thing is `formwork/fw sync <project>`, and it refuses unless the clone is
clean and committed.

It copies every kit file, deletes the ones the kit no longer has, and writes
the release, or the clone's commit, into the project's SOURCE.txt. It never touches the project's own
roles, the project pack, nor any path the project lists as its own in
`.formwork.toml`, under `[bindings]`, as `local = ["formwork/rules/core.md"]`.
It stops before recording the fingerprints, because that is your decision, and
prints the two commands to run yourself.

---

## What is advice

Everything else. **48 rules**, in two files.

- `formwork/rules/core.md` holds 14. You meet these every day.
- `formwork/rules/full.md` holds 34. Read one when you hit the situation.

> [!TIP]
> Every rule says what it catches. None of them tells you a story, because the
> stories belong to somebody else's project.

---

## Some of this will look like fussiness

Several of these rules were learned from failures you have not had.

Each one states what it catches. **If you never hit that, delete it** from
`formwork/rules/core.md`, so losing a rule is a line in your version control
with your name on it.

There is no `[rules]` switch in `.formwork.toml`, and a check refuses one if you
add it. A rule switched off in a settings file disappears quietly. A rule
deleted from the rules file does not.

A rule you follow without understanding gets dropped quietly later anyway.

---

## Settings

One file, `.formwork.toml`, and the installer writes it for you:

```toml
[bindings]
runtime = "claude-code"          # which tool you use

[strength]
git_boundary = "block"           # block | warn | off
protect_files = "block"          # block | warn | off
aggregate_gate = "block"         # the turn-end gate
gate_budget = 3                  # refusals before it stands aside
open_briefs = 1                  # briefs open at once, 0 for no limit
open_briefs_per = "project"      # project | stream: the limit for each stream
read_back_words = 5              # words after "in my words:", 0 for none
```

`[bindings]` is your setup. `[strength]` tunes how hard the enforced guards
bite. There is no third section: see above.

**The last five lines appear only once you change them.** They have working
defaults, so a fresh file is shorter than this.

**You do not have to write any of it by hand.** `formwork setup` asks a few
questions once, shows you everything it is about to do, and writes it only if
you say yes:

- `docs/style.md`, from how you said you want to be spoken to
- `docs/standing.md`, seeded with what you are building and what is next
- `docs/decisions/`, `docs/briefs/`, `docs/reports/`, started and explained
- the `[strength]` values, including `gate_budget`
- the two routing lines in `CLAUDE.md` or `AGENTS.md`, only when there is none

It never overwrites a file you already have, and it never touches
`[bindings]`, which the installer worked out by looking at your project.

For one session only:

```
FORMWORK_GIT_BOUNDARY=off
FORMWORK_PROTECT_FILES=warn
FORMWORK_GATE=off
```

---

## Your team

`formwork/roles/` holds 28 roles. Seven run the method. Twenty-one do the work,
grouped into packs.

**All of them are available. There is no switch yet**, and this page says so
rather than describing one that does not exist.

Adding your own is copying `TEMPLATE.md`, filling in five sections and four
frontmatter fields. A role missing any of them does not load.

**Specialists, cheapest first.** The lead spawns an existing role. If the work
needs a focus, it relabels one: "`visual` as art director", optionally with a
skill, with its owns, sections and tools still from its own file. Only when no
existing `owns` covers the work is a new role written: the director drafts it
in the brief in the five section format, your go accepts it, a working session
writes it to `formwork/roles/project/<name>.md` and runs `formwork roles` and
`formwork check`, and then the lead may spawn it. Never a pasted persona or a
general agent given a role's text in a prompt: nothing checks its boundary or
tools. `roles-named` fails a round file or a brief's team row that names no
real role. Whether a role written mid session can be spawned in the same
session is NOT ESTABLISHED, so adding one is its own task brief.

**How they talk to you** is one page, [`formwork/style.md`](formwork/style.md),
pointed at from every generated role. Your own `docs/style.md` overrides it.

The installer generates them for your runtime. To regenerate after an edit:

```
formwork roles
```

---

## What it cannot do

The guards are pattern matching over a command line. They stop the ordinary
path and not a determined one.

[`formwork/limits.md`](formwork/limits.md) lists exactly what got past an audit, what
was closed afterwards, and what cannot be closed this way. Read it before
trusting any of this further than it deserves.

---

## Two things here you will not find elsewhere

**A check that refuses rather than advises.** Most tooling tells you something
is wrong and lets the work continue. This stops the turn.

**Rules about what counts as evidence.** A figure arrives with the command
behind it. A gap is named rather than filled. A check nobody has watched fail
is not treated as proof of anything.

Both came out of real use. Neither has been tried by anybody else yet, and the
kit would rather say that than imply a crowd that does not exist.

---

## What it costs

Nobody has measured what one round costs in money. Not once. `formwork/COSTS.md`
says so plainly, gives the part that can be measured for free, and says what
would establish the rest.

---

## Where to start

[`formwork/first-run.md`](formwork/first-run.md). Fifteen minutes, on your own
project.

Then [`formwork/loop.md`](formwork/loop.md) for the working loop,
[`formwork/threads.md`](formwork/threads.md) for how work starts and where the
plan lives between conversations, and [`formwork/round.md`](formwork/round.md)
when a decision is expensive enough to be worth a round.
