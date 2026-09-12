# Your first fifteen minutes

Seven short steps, on your own project. No tutorial, no sample repository.

**Nothing here restructures your work.** The install adds files and touches
nothing else. It does not need a clean working tree.

**About the fifteen minutes.** The machine's share is small, and measured:

```
$ time formwork install --dry-run     0.03s
$ time formwork demo                 1.0s
```

Your share has never been timed, because step 4 is you doing real work on your
own project and nobody can measure that for you. **The fifteen minutes is a
target, not a measurement.** If it takes you materially longer, that is worth
telling whoever gave you this.

---

> **`command not found: formwork`?**
>
> You have the kit but not the command. Everything on this page also works
> with `formwork/fw` from the top of your project:
>
> ```
> formwork/fw check
> formwork/fw record
> ```
>
> To get the short command: `pipx install formwork-kit`.

## 0 — Get the kit into your project

**The short way**, if you installed the command:

```
formwork init
```

That puts the two things the kit is made of into this folder: `formwork/` and
`FORMWORK.md`.

**The long way**, if you did not:

```
cp -R path/to/the-kit/formwork  .
cp    path/to/the-kit/FORMWORK.md .
```

Either way, that is all. Nothing else in the source repository is needed.
`docs/` is how it was built, not part of it.

---

## 1 — Install

```
formwork install
```

It works out which runtime you use, writes `.formwork.toml`, wires the guards
into that runtime's hooks, and generates your role files.

**It also writes outside your project.** A fingerprint of every file that
enforces something goes into `~/.formwork/`, so that a change to a guard cannot
be hidden by changing the record beside it. That is the only thing the kit puts
outside your repository, and it is why a clone on a second machine needs the
installer run again.

**It adds and never removes.** If you already have hook settings, yours are
kept and the kit's are added alongside, and a copy of your original is saved
next to it first.

To see what it would do without doing it:

```
formwork install --dry-run
```

If it cannot tell which runtime you use, it says so and asks rather than
guessing:

```
formwork install --runtime cursor
```

**Read the exit code.** `0` finished. `1` got as far as it could, and prints a
list under `NOT FINISHED` — that happens on the three runtimes nobody has
tested. `2` could not run at all, usually because it cannot tell which runtime
you use; say which with `--runtime`.

**On Claude Code it writes all of it** and the gate is green straight away.

**On the other three it writes the config and your role files, and cannot wire
the hooks** — the kit ships no wiring file for them. It says so under `NOT
FINISHED`, exits 1, and **your gate stays red until you write that file by
hand.** The configuration to write is in that runtime's adapter README.

Red is the correct answer there: nothing is guarding yet.

---

## 2 — Watch it refuse

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

## 3 — Watch a check go red

```
formwork check
```

Green. Now:

```
formwork demo
```

Each check runs against an input built to break it, and you watch each one
refuse.

**Why this exists as a command:** a check nobody has seen fail is not evidence
of anything. Every check in this kit ships with an input it must reject *and*
one it must accept — so it has to discriminate, not merely be capable of
complaining.

If a check ever stops rejecting its broken input, the gate goes red for that
reason alone.

---

## 4 — Do one real thing

Pick something small and genuinely yours. A rename. A typo. A comment.

Write a one-line brief:

```
Rename `foo` to `bar` in the parser. Nothing else.
```

That is a complete brief. It has a goal, a scope, and a fence.

Let the agent do it. Then read what comes back:

```
Renamed foo -> bar in parser.py and its two tests.
Gate green.
Nothing staged.
Nothing unasked, nothing skipped, brief was accurate.
```

Four lines, and it answers the three questions that matter: what was done
beyond the request, what was skipped, and whether the brief was right.

**Then it stops.** It does not start the next thing. That is the loop, and
`STOP` is the part worth keeping if you keep nothing else.

---

## 5 — Now read the page

[`FORMWORK.md`](../FORMWORK.md). One page, **after** doing the work rather than
before.

Everything on it now refers to something you have already seen.

---

## 6 — What to read when you need it

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

Forty-six rules exist, in [`formwork/rules/`](rules/) — thirteen you meet daily
and thirty-three more for particular situations. You have been shown three of
them, by watching them catch something.

Reading them now would be reading a list. You would agree with all of them and
remember none.

## Some of it will look like fussiness

It will. Several of these rules came from failures you have not had.

Each one says what it catches. **If you never hit that, drop it** — by
deleting it from `formwork/rules/core.md`, so that losing a rule is a line in
your version control with your name on it.

There is deliberately no switch in `.formwork.toml` for this. What that file
tunes is how hard the three *enforced* guards bite: `block`, `warn` or `off`.

A rule followed without understanding gets dropped quietly later anyway.

## If your runtime cannot block

**Only Claude Code has been watched refusing a real command.** Codex, Cursor and
Gemini CLI all document a way to refuse, and nobody has tried it. Their adapters
say so at the top, in one word: untested.

If yours is one of the three, the page above still works, with two changes.

**Step 2 may do nothing.** Ask for a commit anyway. If it is refused, the
boundary is live on your runtime and you have just established something nobody
had established before — please say so. If the commit goes through, the boundary
is advice on your runtime, and you should know that on day one rather than on a
bad day.

**Step 3 works either way.** `formwork demo` is a program you
run yourself. It does not depend on hooks, on your runtime, or on anything
refusing. Every reader gets this one.

**Step 4 works either way**, minus the guarantee. The loop, the brief, the
report and the stop are all things the agent does because the rules say so, not
because something blocks it.

So the honest division is: **the checks are yours whatever you run. None of
the three guards is, until the hooks are wired.**

What that is worth is not nothing. A rule an agent follows most of the time is
worth having. It is just not the same as a rule it cannot break, and this kit
will not blur the two.
