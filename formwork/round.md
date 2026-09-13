# How to run a round

A round is the kit's largest unit of work. Several agents look at the same
question at once, argue, and one document comes out.

**This page is the one that was missing.** The checks enforced a layout that was
written down nowhere, which is the kind of thing this kit is supposed to catch.

---

## When a round is worth it

Not often. A round costs real money, see [`COSTS.md`](COSTS.md).

Use one when **a decision is expensive to reverse** and you do not yet know the
answer. A shape you will build on for a year. A dependency you cannot easily
drop. For everything else use the loop in [`loop.md`](loop.md): one brief, one
agent, one report.

---

## The shape on disk

**A round is one piece of work like any other, so it takes a number** from
`docs/briefs/` and leaves a report behind. The argument itself lives in its own
folder, because it is five files and they would drown the index.

```
docs/briefs/0009-storage-shape.md      status: open. Says "this is a round"
                                       and points at the folder below

docs/rounds/storage-shape/
    brief.md          what is being asked. You write this
    predictions.md    the challenger, written FIRST
                      template: formwork/templates/predictions.md
    <role>.md         one file per participant
    round.md          what came out of it. The lead writes this

docs/reports/0009-storage-shape.md     short. What came out, in a few lines,
                                       pointing at round.md for the argument
```

**Why both.** `docs/briefs/` is the complete list of everything you have ever
asked for, rounds included. Without the number, a round is the one kind of work
that leaves no line in that list, and you would have to remember it happened.

`<name>` is short and says what the round is about, `storage-shape`,
`auth-approach`. It is a folder name, so keep it plain.

**`predictions.md` is not optional and not last.** A check looks for it. See
below for exactly what it can and cannot tell.

---

## The order, and why it is that order

**1. You write the brief.** Use [`templates/brief.md`](templates/brief.md). It
is six headings and it is the whole input, so it is worth the twenty minutes.

Take a number with `formwork/check/checks/work-paired --next .` and save a
short `docs/briefs/0009-storage-shape.md` saying this is a round and where the
folder is. The full brief goes in the folder as `brief.md`.

**2. The challenger writes `predictions.md` first**, before anybody has
proposed anything. It names the failures it expects and what result would show
each one was mistaken.

> [!IMPORTANT]
> **A prediction written after the answer is not a prediction, it is
> agreement.** This is the rule people skip, and it is the reason a round is
> worth anything.

**3. Everybody else works, at the same time.** Each writes their own file, named
for their role. They do not read each other's yet.

**4. The lead collects everything and forces the argument.** Where two
participants disagree, that disagreement is the valuable part. It gets resolved
in the open, not smoothed over.

**5. The lead writes `round.md`.** Use
[`templates/round.md`](templates/round.md). What was asked, who said what, what
was decided, what is still open.

**6. The round leaves a report like any other work.** A short
`docs/reports/0009-storage-shape.md`: what came out, what is still open, and a
pointer to `round.md` for the argument. Then the brief becomes `status: done`.

Do not copy the round record into it. One fact, one home.

**7. Anything decided gets a decision record.** Use
[`templates/decision.md`](templates/decision.md), numbered, in
`docs/decisions/`. Never edited afterwards. Superseded by a later one.

---

## What to actually type

**This depends on your runtime, and only Claude Code has been watched doing
it.**

On Claude Code, the roles are installed as subagents in `.claude/agents/`. You
ask for one by name in plain language:

```
Use the challenger to write docs/rounds/storage-shape/predictions.md.
The brief is docs/rounds/storage-shape/brief.md.
Write predictions only. Do not propose a solution.
```

Then the others:

```
Use the architect, the researcher and the record-keeper on the same brief.
One file each, under docs/rounds/storage-shape/.
```

**On the other three runtimes this is NOT ESTABLISHED.** Their role files are
generated and their documentation says they are read. Nobody has watched it
work. See [`adapters/`](adapters/).

---

## The check that watches this

```
formwork check
```

**Run the gate, not the check on its own.** A check run directly will also scan
the kit's own test fixtures, which contain deliberately broken examples, and
report them as if they were yours. The gate tells each check what to leave
alone; nothing else does.

**What it fails on:** a round folder that has participant reports in it and no
`predictions.md` at all. That is a real finding and it exits 1.

**What it only warns about:** modification times that look out of order. A file
time is weak evidence, a copy, a checkout, a touch, an editor all change it,
so the check says so and does not fail the gate on it.

**What it cannot tell you at all:** whether the predictions are any good. It
stops the cheapest way of fooling yourself, not the clever ones.

---

## What a round is not

**It is not a vote.** Nobody counts opinions. A disagreement that survives is
recorded as an open question, not averaged away.

**It is not a meeting.** Nobody waits for anybody. Everyone works at once, and
the argument happens on the written output.

**It does not decide anything by itself.** The round produces the argument and
the options. **You decide.** That is the boundary the whole kit is built on.
