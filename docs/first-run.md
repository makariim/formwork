# The first run, as designed

> ## Read this first: it is a record, not a description
>
> **This page says what was planned. It has not been kept in step with what
> was built, and parts of it are wrong.**
>
> An audit found three. It quotes `FORMWORK.md` "in these words" using words
> that page does not contain, and the invented quote tells the reader to do
> the one thing a check refuses. It documents a flag, `--explain`, that does
> not exist. And it says nine rules carry a `SEE IT` line; none do.
>
> **It is kept as written on purpose.** Rewriting a design record to match the
> outcome destroys the evidence of what changed, which is the rule this kit
> applies to decision records.
>
> **For the real first run**, read
> [`../formwork/first-run.md`](../formwork/first-run.md).


**Phase:** K6. **Date:** 2026-09-12.

What happens the first time someone uses a fork, and what it teaches.

## The problem this phase exists for

A rule without the failure that produced it is not learned.

Every rule in this kit came from a specific expensive mistake. **Those mistakes
cannot be published** — they belong to two private projects. So the first run
has to deliver the *why* without the story, or the kit hands someone a list of
rules that read as fussiness and get deleted in week two.

## The answer

**Do not explain the rule. Let the rule catch something, in front of them, in
the first ten minutes.**

A demonstration is not a story. It needs no incident, no project, and no names.
It needs one command and a thing that goes red.

This is not a hopeful idea. It is what happened while this kit was being
planned: a scan caught fifty-one passages that had been written in the sincere
belief they were original; a check caught private repository names hardcoded
into a file about to be published; a test caught a bug that made a scanner skip
every comment in the repository. In each case the rule became obvious in about
four seconds, and no explanation would have done it.

---

# 1. Shape of the first run

**Fifteen minutes. Four steps. One real change to their own project.**

No tutorial project. No toy repository. No sample data.

```
step 0   install                    2 min
step 1   watch it refuse            2 min
step 2   watch it go red            3 min
step 3   do one real thing          8 min
step 4   now read the page          — after, not before
```

## Step 0 — install

One command. It detects the runtime, writes `formwork/` and `.formwork.toml`,
and wires the adapter.

**It touches nothing else.** No files moved, no directories restructured, no
governing documents demanded, no clean working tree required.

This matters because **most forks land on work already in progress**, not on an
empty repository. A kit that needs a fresh start is a kit most people cannot
adopt.

## Step 1 — watch it refuse

The installer prints one instruction: ask your agent to commit something.

The agent tries. The hook refuses. The refusal appears on screen, in the
agent's own transcript, with the reason.

**What this teaches, without saying it:** the boundary is real. It is not
advice, it is not a preference, and it does not depend on the agent
cooperating.

Nothing is explained. They watched it happen.

## Step 2 — watch it go red

Two commands.

```
formwork/check/run              → green
formwork/check/run --demo-fail  → red, and the agent cannot finish its turn
```

`--demo-fail` runs the check suite against its own broken fixtures — the inputs
that are *supposed* to fail. It is not a special mode invented for teaching. It
is the fixture set the gate already requires, pointed at the learner.

**What this teaches:** the gate can fail, failure stops the work, and a check
that has never been seen to fail is not evidence of anything.

That is three rules delivered in one command, none of them explained.

## Step 3 — do one real thing

Pick something small and real in your own project. A rename. A comment. A typo.

- Write a one-line brief.
- The agent does it.
- The gate runs.
- You get a short report: files changed, gate result, anything it did that you
  did not ask for.
- It stops.

That is the loop, at its smallest size, on their own code.

## Step 4 — now read the page

`FORMWORK.md`, one page, **after** doing the work rather than before.

Everything on that page now refers to something they have already seen.

---

# 2. What is taught, and what is not

## Taught in the first run — 4 rules

| Rule | How |
|---|---|
| The agent never touches version control | it refused |
| The gate blocks | it went red |
| A check must be able to fail | they ran the failing fixtures |
| The loop: brief, work, check, report, stop | they did one |

## Not taught — the other 42

Deliberately. Someone who must read forty-six rules before doing anything will
do nothing.

The remaining rules are met when the situation arrives. Each carries two lines
and no story:

```
RULE      Every figure carries the command that produced it.
CATCHES   A number nobody can reproduce, which cannot be told
          apart from one that was remembered.
SEE IT    formwork/check/run --explain figures
```

**`CATCHES` is the whole answer to this phase's question.** It states the *class*
of failure the rule prevents. A class needs no incident, so nothing private
crosses, and it is more useful than a story anyway — a story is one instance and
a class covers all of them.

`SEE IT` exists only where a check exists. Nine rules have it.

---

# 3. The rules that cannot be taught this way

Honesty, because pretending otherwise is how kits lose trust.

**Forty-six rules are advice.** No demonstration is possible for most of them.
Nothing can show you, in ten minutes, why leading with the contradiction matters
or why the smaller claim is the better one.

Those rules will read as fussiness, and some of them are. K4 already found that
several are cheap for the person who lived through the failure and expensive for
everyone else.

So the kit says this, in `FORMWORK.md`, in these words:

> Some of these rules will look like fussiness. Several of them were learned
> from failures you have not had. Each one states what it catches. If you never
> hit that, turn it off — and `.formwork.toml` is where, so that turning it off
> is a line you wrote rather than a habit you drifted into.

**Permission to switch a rule off is part of the teaching.** A rule kept out of
obedience is not understood, and it will be abandoned silently later, which is
worse.

---

# 4. Day thirty

The kit stops teaching.

Guidance inside the governing documents is wrapped so it can be switched off in
one setting, and the documents stay valid without it. The mechanism is adopted
rather than designed — K3 found it published in an existing template, where it
exists so a team renders a guided version while learning and a clean one
afterwards.

```toml
[bindings]
guidance = false     # day thirty
```

**Formwork is named after a temporary structure that is stripped once the
concrete sets.** Switching the guidance off is the first piece of stripping. The
rest — which rules come out, and when — is on the frozen list and has no
mechanism yet. That is a stated hole, not an oversight.

---

# 5. What would tell us this phase failed

Taken from the plan, answered.

| Failure condition | How this design avoids it |
|---|---|
| Hands over files and explains nothing | Three rules are demonstrated before anything is read |
| Requires reading everything before doing anything | One page, read at step 4. Four rules taught, 42 deferred |
| Someone finishes and cannot say why any rule exists | They can say three: it would not let the agent commit; the check went red and stopped it; the failing inputs really fail |
| Only works on a fresh empty project | Install is additive. No clean tree, no restructuring, no required documents |
| Teaches with an example from a source project | **There is no example.** Every demonstration runs against the learner's own repository. Nothing to leak, because nothing is supplied |

That last row is the load-bearing one. The privacy problem is not managed here,
it is **structurally absent**: a first run with no worked example cannot leak
one.

---

# 6. What this phase decided

1. **Teach by demonstration, not explanation.** Three rules catch something real
   in the first ten minutes.
2. **The fixtures are the teaching material.** No separate tutorial content
   exists, so none can go stale or leak.
3. **`CATCHES` replaces the story.** Every rule states the class of failure it
   prevents. Classes are generic by construction.
4. **Forty-two rules are deferred to the moment they matter.**
5. **Switching a rule off is sanctioned and recorded**, because a rule obeyed
   without understanding is abandoned silently later.
6. **Install is additive**, because most forks land on work in progress.

# 7. What could not be established

- **Whether this teaches.** Nobody has run it. The claim that a demonstration
  beats an explanation rests on three incidents during this kit's own planning,
  which is one person's experience of watching checks catch him.
- **Whether four demonstrated rules is the right number.** Three, six and ten
  were not compared.
- **Whether `CATCHES` lines are actually read.** They may be skipped exactly as
  a story would be.
- **How much of the first run survives a runtime that cannot block.** On an
  advice-only runtime, step 1 and step 2 do not happen, and the first run
  loses its two strongest moments. **What that leaves is NOT ESTABLISHED**, and
  K7 must decide what those users see instead.
