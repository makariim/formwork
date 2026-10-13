# Report

What comes back when the work stops.

**Scale it.** A one-line task gets a three-line report. The full list below is
for a checkpoint.

**How it is written** is [`../style.md`](../style.md), and your own
`docs/style.md` if you wrote one.

**Where it is saved.** `docs/reports/0007-same-name.md`, the same number as the
brief it answers. Then set that brief's `status` to `done`.

---

## What changed

Each file, one line on why.

## What was run

Every command that wrote something to disk. Installs, generated files,
migrations, anything that touched the world outside this repository.

## The check

The full result of `formwork check`, named as the whole thing rather than a
part of it.

If it is red, say so first. A red gate is the headline, not a footnote.

## Git status

Pasted, so you can see nothing was staged.

## The three that matter

Everything above is routine. These are what you are actually reading for.

- **Done but not asked for**, and why.
- **Asked for but not done**, and why.
- **Wrong in the brief**. Anything that turned out not to match the files.

Work that followed the brief exactly needs no defence. What you are scanning
for happens at the edges of an instruction, and only these three show it.

## Accepted

Two lines, written by you, the human, after you have read the report:

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

---

## The task version

```
Renamed foo -> bar in parser.py and its two tests.
Gate green.
Nothing staged.
Nothing unasked, nothing skipped, brief was accurate.
accepted: 2026-10-13
in my words: foo is bar now, and I kept the old name out.
```

Four lines from the agent, two from you. Still answers all three.
