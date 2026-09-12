# Your first fifteen minutes

Seven short steps, on your own project. No tutorial, no sample repository.

**Nothing here restructures your work.** The install adds files and touches
nothing else. It does not need a clean working tree.

**The fifteen minutes is a target, not a measurement.** The machine's share is
about a second. Your share is step 4, which is real work on your own project,
and nobody can time that for you.

> **`command not found: formwork`?** Everything here also works as
> `formwork/fw check`, `formwork/fw record` and so on, from the top of your
> project. To get the short command: `pipx install formwork-kit`.

---

## 0. Get the kit into your project

```
formwork init
```

That puts `formwork/` and `FORMWORK.md` here. Without the command, copy those
two in by hand from the source repository. Nothing else in it is needed.

---

## 1. Install

```
formwork install
```

It works out which agent you use, writes `.formwork.toml`, wires the guards
into that agent's hooks, and generates your role files.

**It adds and never removes.** Existing hook settings are kept, the kit's are
added alongside, and a copy of your original is saved first.

**It also writes one file outside your project**, in `~/.formwork/`: a
fingerprint of everything that enforces a rule. Keeping it outside means a
change to a guard cannot be hidden by changing the record next to it. It is
also why a clone on another machine needs installing again.

`formwork install --dry-run` shows what it would do. `--runtime cursor` says
which agent when it cannot tell.

**Read the exit code.** `0` finished. `1` got as far as it could and prints a
`NOT FINISHED` list. `2` could not run.

**On Claude Code the gate is green straight away.** On the other three it
writes your config and roles but cannot wire the hooks, because the kit ships
no wiring file for them. Your gate stays red until you write that file
yourself, using your agent's page in `formwork/adapters/`. Red is correct
there: nothing is guarding yet.

---

## 2. Watch it refuse

Ask your agent to commit something.

```
you:    commit this for me
agent:  (tries)
        REFUSED by the version-control boundary: git commit changes
        the repository.
```

The command never ran.

Now ask it for `git status`. That works, as it always did.

**Nothing was explained to you. You watched it happen.** That is the whole
teaching method here: the rules catch things in front of you rather than being
argued for.

---

## 3. Watch a check go red

```
formwork check
```

Green. Now:

```
formwork demo
```

Each check runs against an input built to break it, and you watch each one
refuse.

**A check nobody has seen fail is not evidence of anything.** Every check ships
an input it must reject and one it must accept, so it has to tell them apart
rather than simply be capable of complaining. If one ever stops rejecting its
broken input, the gate goes red for that reason alone.

---

## 4. Do one real thing

Pick something small and genuinely yours. A rename. A typo. A comment.

Write a one-line brief:

```
Rename `foo` to `bar` in the parser. Nothing else.
```

That is a complete brief: a goal, a scope, and a fence.

Let the agent do it. Then read what comes back:

```
Renamed foo -> bar in parser.py and its two tests.
Gate green.
Nothing staged.
Nothing unasked, nothing skipped, brief was accurate.
```

Four lines, answering the three questions that matter: what was done beyond the
request, what was skipped, and whether the brief was right.

**Then it stops.** It does not start the next thing. That is the loop, and
`STOP` is the part worth keeping if you keep nothing else.

---

## 5. Now read the page

[`FORMWORK.md`](../FORMWORK.md). One page, **after** doing the work rather than
before.

Everything on it now refers to something you have already seen.

---

## 6. What to read when you need it

Nothing else is required today. These are the pages for when the situation
arrives:

| | |
|---|---|
| [`loop.md`](loop.md) | the working loop in full: brief, work, check, report, stop |
| [`round.md`](round.md) | how to run a round, and when one is worth the money |
| [`templates/`](templates/) | the brief, the report, the decision record, the round |
| [`roles/HOW-TO-ADD-A-ROLE.md`](roles/HOW-TO-ADD-A-ROLE.md) | adding your own |
| [`COSTS.md`](COSTS.md) | what this costs, and the number nobody has |
| [`limits.md`](limits.md) | what the guards cannot do. Read before trusting them |
| [`glossary.md`](glossary.md) | any word here you did not recognise |
| [`troubleshooting.md`](troubleshooting.md) | when something goes wrong |

---

## What you have not been told

Forty-six rules exist, in [`rules/`](rules/). Thirteen you meet daily,
thirty-three for particular situations. You have seen three of them, by
watching them catch something.

Reading them now would be reading a list. You would agree with all of them and
remember none.

## Some of it will look like fussiness

It will. Several of these rules came from failures you have not had.

Each one says what it catches. **If you never hit that, delete it** from
`formwork/rules/core.md`, so that losing a rule is a line in your version
control with your name on it. There is no switch for this in `.formwork.toml`
on purpose. What that file tunes is how hard the guards bite: `block`, `warn`
or `off`.

A rule followed without understanding gets dropped quietly later anyway.

## If your agent cannot block

**Only Claude Code has been watched refusing a real command.** The other three
document a way and nobody has tried it. Their adapter pages say so in one word:
untested.

If yours is one of those three:

**Step 2 may do nothing.** Ask for the commit anyway. If it is refused, you
have established something nobody had established before, and it is worth
saying so. If it goes through, you now know that on day one rather than on a
bad day.

**Steps 3 and 4 work either way.** `formwork demo` is a program you run
yourself. The loop, the brief and the stop are things the agent does because
the rules say so.

**The honest division: the checks are yours whatever you run. None of the three
guards is, until the hooks are wired.**

A rule an agent follows most of the time is worth having. It is not the same as
one it cannot break, and this kit will not blur the two.
