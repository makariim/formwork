# Standing brief

One file. The only place that says where the project is right now.

Save it as `docs/standing.md`. Everything else in this kit describes one piece
of work. This describes the state between pieces, so a new conversation can
start without you retelling the whole story.

**Keep it short.** Past two pages it has become a diary, and a diary is the
thing nobody opens.

**Update it before you close a conversation**, not later. `formwork check`
fails when it is older than your newest decision or round.

---

```markdown
---
updated: 2026-09-13
by: the conversation that last touched this
---

# Standing brief

## What we are building

One paragraph. This changes rarely, maybe never.

Write it so a stranger could read it and know what this is.

## Where we are now

What works. What is half done. What is broken and known.

Change this every session. It goes stale faster than anything else here.

## What is decided

Pointers, not arguments. The record holds the reasoning.

- `0001` short title
- `0002` short title

**These are pointers, not the decisions themselves.** If it is not in
`docs/decisions/`, it is not decided. It is a thing somebody remembers, and a
line here will not make it one.

## What is open

Questions genuinely not settled. One line each.

Anything nobody has measured is marked NOT ESTABLISHED instead of guessed at.

## What is next

One or two things. Not a backlog.

A long list here means the thinking has not been done yet.

## What we tried and stopped

Short. It stops the same idea coming back in four months under a new name.
```

---

## The date is the whole mechanism

`updated:` is a real date, in `YYYY-MM-DD`, and a check reads it.

If a decision record or a round record carries a later date than this file, the
gate goes red and names the file. That is the point: the standing brief is the
one document that is worth nothing when it is out of date, so it is the one
document a program watches.

Nothing checks whether what you wrote is true. Nothing can.

## Empty headings

Delete the empty bullets. A bullet with nothing after it fails the check.

A heading with nothing under it is allowed for the last three. **The first two
have to say something**, because a standing brief that does not say what this is
or where we are is not doing its job.
