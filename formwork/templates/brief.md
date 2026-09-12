# Brief

Copy this. Fill it in. Hand it over.

**For a task, one line is the whole brief.** Do not use this page for a rename.
Scale the paperwork to the work, or the work stops happening.

---

## 1. Goal

What this is for, and why it exists. One paragraph.

**And one line that is easy to skip and should not be: what happens if we do
not do this at all?** If the honest answer is "nothing much", you have saved
yourself the work.

## 2. Scope

What may be changed, file by file where you can name them.

This is also the fence. What is listed is what may be touched.

**Out of scope:** name the things that must not be touched, not only the things
that may. "Everything else" is not an answer — name the ones somebody might
reasonably assume were included.

## 3. Must not happen

What is forbidden here. The standing ones always apply:

- do not write to version control
- do not decide anything; stop and report instead
- do not change a check because it failed
- where something cannot be established, say so rather than estimating

Add the ones specific to this work.

## 4. Done when

How anyone can tell it is finished — testable, not a matter of opinion.

**Something that cannot come out false is not a criterion.** Where a check
requires a clean working tree and yours will be dirty, record that here.

## 5. Checked by

`formwork/check/run`, named as the whole thing.

You may add commands on top. You may never swap in a hand-picked few instead.

If the gate cannot prove the thing this work changes, say so here and name what
the real evidence will be.

## 6. The report must contain

The standing list in `formwork/templates/report.md`, plus anything else you
want back.

---

## The task version

```
Rename `foo` to `bar` in the parser. Nothing else.
```

That is a complete brief. It has a goal, a scope, and a fence.
