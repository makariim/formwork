# Formwork

A starter kit for running a serious project with coding agents. Research,
design, building, shipping. Meant to be forked.

The name is the metaphor. Formwork is the temporary structure you build so the
permanent thing sets in the right shape. Then you take it away.

```
git clone https://github.com/<you>/formwork.git
cp -R formwork/formwork formwork/FORMWORK.md  /your/project/   # the kit is these two

cd /your/project
formwork/install --runtime claude-code   # wires it up, writes your roles
formwork/check/run                       # green, on Claude Code
```

## What it actually does

Most advice about working with agents is advice. You read it, you agree, and by the end of
the week you have forgotten it.

**This kit refuses things instead.**

Ask your agent to commit, and the command does not run:

```
you:    commit this for me
agent:  REFUSED by the version-control boundary: git commit changes
        the repository.
```

Nothing was explained to you. You watched it happen.

## Three parts

**Guards.** Programs that block a command before it runs. Your agent cannot
commit, push, or merge — you do that. It cannot edit the kit's own files
without you knowing.

**Checks.** Nine programs that read the project and go green or red, at the end
of every turn. A red gate stops the turn — three times in a session, then it
stands aside loudly, so a genuinely stuck turn is not trapped for ever.

**Roles.** 27 agent definitions. Each one says what it owns, what it does not
own, when it stops, and what it would look like if it were wrong.

Plus 13 rules you meet daily and 33 more for when the situation arrives. All 27
roles are available; there is no switch to turn packs on yet, and the kit says
so rather than describing one.

## Every check has been watched failing

A check nobody has seen fail is not evidence of anything.

So every check ships with an input it must reject **and** one it must accept.
It has to tell them apart, not merely be capable of complaining. You can watch
this yourself:

```
formwork/check/run --demo-fail
```

The fixtures are copied into randomly named folders first, so a check cannot
pass by recognising a filename.

## What is weak about this

**One person, two projects, and that person wrote it.** That is the whole of
the evidence. It is weak evidence and no amount of detail below changes that.

**Only one of four runtimes has been watched refusing anything.** Claude Code.
Codex, Cursor and Gemini CLI document a way to block and nobody has tried it.
Their adapters say `untested` at the top.

**Nobody knows what a round costs in money.** Not once measured. See
[`formwork/COSTS.md`](formwork/COSTS.md), which says so rather than guessing.

**The guards stop the ordinary path, not a determined one.** They are pattern
matching over a command line. [`formwork/limits.md`](formwork/limits.md) lists what an
audit walked through, what was closed, and what cannot be closed this way.

**It does not claim to work for a team.** A team version is not a goal here.

## Start here

[`formwork/first-run.md`](formwork/first-run.md). Fifteen minutes, on your own
project. No tutorial, no sample repository.

**Install adds and never removes.** It writes `.formwork.toml`, the hook wiring
for your runtime, and your role files — and it takes a first fingerprint of the
kit's own files in `~/.formwork/`, outside your repository. It does not need a
clean working tree and it moves nothing.

## The rest

- [`FORMWORK.md`](FORMWORK.md) — the whole method on one page. Read it *after*
  the first run.
- [`formwork/rules/`](formwork/rules/) — the rules, each with a line saying
  what it catches.
- [`formwork/roles/`](formwork/roles/) — the 27 roles, and how to add your own.
- [`formwork/loop.md`](formwork/loop.md) — the working loop, in full.
- [`formwork/round.md`](formwork/round.md) — how to run a round, and when one is
  worth the money.
- [`formwork/templates/`](formwork/templates/) — the brief, the report, the
  decision record, the round.
- [`docs/`](docs/) — how it was built, what was found, what broke.
- [`docs/dogfood.md`](docs/dogfood.md) — the kit's own failures, recorded as
  they happened. Including the times its author broke his own rules, which the
  log counts for you.

## Licence

MIT. See [LICENSE](LICENSE).
