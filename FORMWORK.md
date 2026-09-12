# Formwork

A way of running a project with coding agents.

## The loop

Everything is one loop. Only the size changes.

```
BRIEF → WORK → CHECK → REPORT → STOP → you say go → BRIEF …
```

| Size | How long | The brief is | The report is |
|---|---|---|---|
| task | minutes | one line | files changed, check result |
| checkpoint | one sitting | six headings | the full list |
| round | hours to days | a question per role | a round record |
| phase | weeks | what it settles | one document |
| milestone | months | a direction | — |

Each one answers four questions: what it produces, what must be true before it
starts, who says go, and **what would tell us it failed.**

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

**The last one has a limit worth knowing.** It refuses three times in a session
and then stands aside, so that a genuinely stuck turn is not trapped for ever.
Three refusals is loud. Set `gate_budget` in `.formwork.toml` to change it.

Run them:

```
formwork check              everything, on your project
formwork demo  watch each check refuse a broken input
formwork check --list       what exists
```

**If you did not install the command**, every one of these works by path
instead: `formwork/fw check`, `formwork/fw demo`, `formwork/fw roles`. Run
`formwork/fw` on its own to see the list.

## What is advice

Everything else. **46 rules**, in two files.

- `formwork/rules/core.md` — 13. You meet these every day.
- `formwork/rules/full.md` — 33. Read one when you hit the situation it covers.

Every rule says what it catches. None of them tells you a story, because the
stories belong to somebody else's project.

## Some of this will look like fussiness

Several of these rules were learned from failures you have not had.

Each one states what it catches. **If you never hit that, drop it** — delete it
from `formwork/rules/core.md`, so that losing a rule is a line in your version
control with your name on it.

There is deliberately no `[rules]` switch in `.formwork.toml`, and a check
refuses one if you add it. A rule switched off in a settings file disappears
quietly. A rule deleted from the rules file does not.

A rule you follow without understanding gets dropped quietly later anyway.

## Settings

This is the whole file, and the installer writes it for you:

```toml
[bindings]
runtime = "claude-code"          # which tool you use

[strength]
git_boundary = "block"           # block | warn | off
protect_files = "block"          # block | warn | off
```

`[strength]` tunes how hard the enforced guards bite. `[bindings]` is your
setup. There is no third section: see above.

**Two more keys exist and both live in `[strength]`:**

```toml
aggregate_gate = "block"   # block | warn | off. The turn-end gate
gate_budget = 3            # how many times it refuses before standing aside
```

For one session only:

```
FORMWORK_GIT_BOUNDARY=off
FORMWORK_PROTECT_FILES=warn
FORMWORK_GATE=off
```

## Your team

`formwork/roles/` holds 27 roles. Six run the method. Twenty-one do the work,
grouped into packs.

**All of them are available. There is no switch yet**, and this page says so
rather than describing one that does not exist.

Adding your own is copying `TEMPLATE.md`, filling in five sections and four
frontmatter fields. A role missing any of them does not load.

The installer generates them for your runtime. To regenerate after an edit:

```
formwork roles
```

## What it cannot do

The guards are pattern matching over a command line. They stop the ordinary
path and not a determined one.

[`formwork/limits.md`](formwork/limits.md) lists exactly what got past an audit, what
was closed afterwards, and what cannot be closed this way. Read it before
trusting any of this further than it deserves.

## Two things here you will not find elsewhere

**A check that refuses rather than advises.** Most tooling tells you something
is wrong and lets the work continue. This stops the turn.

**Rules about what counts as evidence.** A figure is reported together with the
command behind it. Anything unmeasured says so in capitals. A check that nobody has
watched fail is not treated as proof of anything.

Both came out of real use. Neither has been tried by anybody else yet, and the
kit would rather say that than imply a crowd that does not exist.

## What it costs

Nobody has measured what one round costs in money. Not once. `formwork/COSTS.md`
says so plainly, gives the part that can be measured for free, and says what
would establish the rest.

## Where to start

[`formwork/first-run.md`](formwork/first-run.md). Fifteen minutes, on your own
project.

Then [`formwork/loop.md`](formwork/loop.md) for the working loop, and
[`formwork/round.md`](formwork/round.md) when a decision is expensive enough to
be worth a round.
