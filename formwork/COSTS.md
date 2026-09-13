# What this costs to run

Two of the three numbers below are measured. The most important one is not.

---

## The gate. Measured

```
$ time formwork check
real 3.77
real 3.81
real 3.92
```

About four seconds on this repository, over three runs. That is one
run of all twelve checks over 201 files, including the fixtures each check is tried
against. It runs at the end of
every turn in which something changed.

**What would make that wrong:** it scales with how many files you have, and with
how many checks you add. On a large repository, measure it rather than trusting
this line.

## What the kit adds to your repository. Measured

```
$ find formwork -type f | wc -l
201
```

201 files. Plain text and a few small programs. Python 3, standard library only,
no dependencies of any kind. It costs nothing to carry and nothing to install.

---

## A round, NOT ESTABLISHED

**Nobody has measured what a round costs in money. Not once.**

This is the most important number on this page and it is missing. Treat a round
as expensive until somebody produces the figure.

### What can be measured without spending anything

A round has a floor: the reading everybody has to do before a single thought
happens.

| | words |
|---|---|
| the core everybody reads: the page, the loop, the core rules, the style page | 3,316 |
| five role files, one per participant | 8,567 |
| **five participants, each reading the core plus their role** | **25,147** |

```
wc -w FORMWORK.md formwork/loop.md formwork/rules/core.md formwork/style.md \
      formwork/roles/method/{lead,challenger,architect,researcher,record-keeper}.md
```

**What that number is not.** It is the floor, and only the floor. It excludes:

- your briefing, which is the largest single input and is different every time
- whatever each participant reads from your repository
- everything anybody writes
- every exchange after the first. The challenge, the reply, the record

A real round is a multiple of this, and **nobody knows the multiple.**

**And it will be out of date.** These figures have gone stale twice while this
page existed, because the roles keep growing. The commands are printed above for
that reason: **run them, do not trust the table.**

**What that number is also not:** it is words, not tokens. Models are billed in
tokens, and the conversion depends on the model. Converting it here would be
inventing precision.

### What would establish it

Run one round. Read the token usage the runtime itself reports. Multiply by the
published rate. Write down the size of round it came from.

That is an afternoon, and until somebody spends it this page keeps saying NOT
ESTABLISHED.

### There is no spend cap

Nothing in this kit stops a round costing more than you expected. A cap is on
the list of things not built, deliberately, because nobody has asked for one
yet.

**If you run rounds, set a limit with your provider.** That is outside this kit
and it is the only real protection available today.

---

## The cost that is certain, and is not money

**Every piece of work waits for you.**

That is what the version-control boundary means. The agent stops, reports, and
does nothing further until you say so.

On a busy day that is the bottleneck. It is also the entire point, and it is
the price of the whole method.

---

## What this page does not cover

Time. How long a brief takes to write, how long a review takes to read.
**Never measured**, and it would be a guess dressed as a figure.
