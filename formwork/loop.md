# The loop

There is one loop. Only its size changes.

```
BRIEF → WORK → CHECK → REPORT → STOP → you say go → BRIEF …
```

**Nothing continues past STOP without you.** That is the whole shape.

---

## Five sizes

| Size | How long | Brief | Report |
|---|---|---|---|
| task | minutes | one line | files, check result |
| checkpoint | one sitting | six headings | the full list |
| round | hours to days | a question per role | a round record |
| phase | weeks | what it settles | one document |
| milestone | months | a direction | none |

**These are names for how big a turn was.** They are not five different
processes. A task and a phase run the same loop.

---

## Four questions, every size

Before starting anything, answer these. A phase and a five-minute task both
deserve them, in proportion.

1. **What does it produce?** One thing.
2. **What has to be true before it starts?**
3. **Who says go?** You.
4. **What would tell us it failed?**

Question four is the one people skip. A piece of work that cannot fail is a
piece of work nobody can check.

---

## Picking a size

Start small. The cost of picking too small is one more turn of the loop. The
cost of picking too big is work nobody can review, which is worse.

**Task**. You can describe it in a sentence and it touches a file or two.

**Checkpoint**. You need to state what is out of scope. Past a small number of
files you are looking at two of them.

**Round**. The answer is genuinely unclear and you want it argued. Rounds cost
real money and nobody has measured how much. Do not run one out of habit.

**Phase**. A question big enough that its answer is a document.

**Milestone**. A direction, not a piece of work. It contains phases.

---

## Where the size comes from

Not from counting files. From this question:

> Could a reviewer sensibly accept one part of this and reject the next part?

If yes, it is two pieces of work. Split it there.

*That test comes from a published engineering-process kit, not from this
method. A file count is arbitrary and this is not.*

**One brief can still be too big for one sitting.** Then it goes to the `lead`
role, which cuts it up, hands the pieces to other roles, and gives you back one
report. You still say go once, and read one report.

---

## Where the brief and the report live

Both are files, numbered in pairs:

```
docs/briefs/0007-slow-login.md      status: open, done or dropped
docs/reports/0007-slow-login.md     the same number, written when work stops
```

A round takes a number too. Its argument lives in `docs/rounds/<name>/` and its
line in the list is a short brief and a short report, like everything else.

`formwork check` fails when a brief says done and no report exists. Work that
happened and left nothing behind cannot be reconstructed later, and that is the
only thing the check is watching for.

Take the next number from the check, never by counting:

```
formwork/check/checks/work-paired --next .
```

---

## How a report is written

What it contains is [`templates/report.md`](templates/report.md). How it reads
is [`style.md`](style.md), and your own `docs/style.md` overrides that.

---

## What STOP means

STOP is not "finished". It is "your turn".

The agent halts, reports, and waits. It does not start the next piece because
the next piece is obvious. It does not commit. It does not tidy up first.

**If you only keep one thing from this kit, keep STOP.**
