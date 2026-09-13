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

---

## The task version

```
Renamed foo -> bar in parser.py and its two tests.
Gate green.
Nothing staged.
Nothing unasked, nothing skipped, brief was accurate.
```

Four lines. Still answers all three.
