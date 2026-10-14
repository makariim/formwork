# Report

What comes back when the work stops.

**Scale it.** A one-line task gets a three-line report. The full list below is
for a checkpoint.

**How it is written** is [`../style.md`](../style.md), and your own
`docs/style.md` if you wrote one.

**Where it is saved.** `docs/reports/0007-same-name.md`, the same number as the
brief it answers. The brief stays `open`. Your read-back, under Accepted,
is what closes it.

---

## Two parts, in this order

Two people read a report and they need different things. You own the work
and want the whole of it, told as a story you can follow from one point to
the next. The director wants the mechanics. One register serves neither, and
the one reports were written in was the director's: three came back on one
day at about 3,000 words each, and the human stopped after a few paragraphs.

So every report has two parts. Yours comes first. The director's holds
everything else.

**`report-shape` checks the order and the ceiling.** The gate is red when
`## For you` is missing, is not the first heading, runs over 1,000 words, or
holds a fenced code block. It cannot tell a story from a findings list
rewritten as sentences. That part is a habit.

---

## For you

Narrated, start to finish, for the person responsible. What the brief asked.
What was done. Every detail that carries weight. What is open, and what needs
a decision from you.

Not in it: commands, file lists, a catalogue of findings, fillers. If it
needs a code block, it belongs in the other part.

**At most 1,000 words, and the ceiling is not a target.** A one-line task
gets three sentences.

## Accepted

Two lines, written by you, the human, after you have read the part above:

```
accepted: 2026-10-13
in my words: <what changed and what you decided, in your own words>
```

Each starts its own line. The date is the day you accepted it. The second line
is at least five words. **Without both, the brief cannot be marked done**, and
`formwork check` goes red until they are there.

You write them, or you dictate them word for word. **The director may type
them for you. It never writes them for you.** That is the same rule as a
decision: drafting yours is not allowed, transcribing yours is.

The check sees only that the lines exist. It cannot tell whose words they are,
or whether they are true. They are for you: if you cannot write the second
line, you did not read the report, and that is the moment to read it.

## For the director

Everything the mechanics need. Read by the director in full, and by you when
you want to see the working.

### What changed

Each file, one line on why.

### What was run

Every command that wrote something to disk. Installs, generated files,
migrations, anything that touched the world outside this repository.

### The check

The full result of `formwork check`, named as the whole thing rather than a
part of it.

If it is red, say so first. A red gate is the headline, not a footnote.

### Git status

Pasted, so you can see nothing was staged.

### The three that matter

Everything above is routine. These are what you are actually reading for.

- **Done but not asked for**, and why.
- **Asked for but not done**, and why.
- **Wrong in the brief**. Anything that turned out not to match the files.

Work that followed the brief exactly needs no defence. What you are scanning
for happens at the edges of an instruction, and only these three show it.

### The body of the work

Whatever the brief said the report must contain: the review, the runbook, the
pointer to a round record. Last, because it is the longest.

---

## The task version

```
## For you
Renamed foo to bar in the parser and its two tests. Nothing else moved.
Nothing to decide.

## Accepted
accepted: 2026-10-13
in my words: foo is bar now, and I kept the old name out.

## For the director
parser.py, test_parser.py, test_cli.py. Gate green. Nothing staged.
Nothing unasked, nothing skipped, brief was accurate.
```

Five lines from the agent, two from you. Still answers all three.
