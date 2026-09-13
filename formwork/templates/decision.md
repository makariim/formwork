# Decision record

One file per decision, in `docs/decisions/`, numbered in the order you accepted
them.

**This shape is borrowed, not invented.** It follows the widely used Markdown
decision-record format. The survey found decision records already solved, twice
over, so this kit does not design its own. If you want the fuller original, go
and take it. It has four sizes and translations.

**Only you write these.** An agent may copy in wording you have accepted, word
for word. It may never author one.

---

```markdown
---
status: accepted
date: 2026-09-12
deciders: [who actually decided]
consulted: [who was asked, and answered]
informed: [who was told afterwards]
---

<!-- Save as docs/decisions/0007-short-title.md. The number and the hyphen
     are required. `formwork check` verifies the numbering. For the next free
     number, run `formwork/check/checks/decision-ids --next .` and ignore any
     other output it prints: run on its own it also scans the kit's test
     fixtures. Do not count the files yourself, because gaps are allowed and
     counting collides. -->

# 0007. Short title in plain words

## What made this a decision

The situation. What forced a choice. Keep it to what a stranger needs.

## What matters here

The two or three things any answer has to satisfy. Name them before the
options, or you will pick an option and then invent the reasons.

## Options we looked at

- **Option A**, one line.
- **Option B**, one line.
- **Do nothing**, one line. Always include this one.

## What we chose, and why

Chose **Option B**, because …

The "because" is the whole point of the file. A record without it is a note
saying what happened, and in six months you will not be able to tell whether
the reasoning still holds.

## What follows

**Good:**
- …

**Bad:**
- …

Both lists. A decision with no bad column was not a decision, it was a
preference.

## What would make us revisit this

The thing that would have to become true. If you cannot name one, say so.
```

---

## Numbering

The number comes from the check, not from counting:

```
formwork/check/checks/decision-ids --next .
```

**Do not count the files.** Gaps are allowed, and counting collides with a
number that is already taken. Nobody
assigns it by hand and nobody guesses.

Gaps are fine. **Renumbering is never fine**, because references break quietly.

## Superseding

Do not delete and do not rewrite. Change the status to say it is superseded,
naming the number of the record that replaces it, and
leave the rest alone. The old reasoning is the useful part.
