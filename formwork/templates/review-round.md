# Review round

Optional. A brief for reviewing the running product the way a person uses
it. Give it `stream: review`.

---

```markdown
---
status: open
stream: review
---

# NNNN Review: <what>

## Part A: look
On the team's own running copy, never the person's own device or account.
Walk every journey in the spec's story, start to finish. One picture per
step, saved beside the findings.

## Findings
First, the person's own notes, in their words, unchanged.
Then the team's, by journey, each with a severity:

| Journey | Step | What is wrong | Severity |
|---|---|---|---|

Each rendered screen gets two questions: does it look generic, and does it
look dead? Clean is not the same as alive.

Look with the taste packs the project names (`formwork/taste/`), and report
a pack finding by its id: `screens-2, checkout: three glowing buttons`. The
project's design file wins over any pack. Taste is judged here, on the
pictures, never by a check. Where the product moves, the `motion` pack is
judged on recordings, watched at full and half speed and with reduced motion
on (`formwork/taste/motion.md`).

## Part B: fix
Fix the person's notes and the team's findings together, in one pass.
Then walk the journeys again.

## Done when
Every journey walked again after the fixes, pictures updated, and what is
still wrong listed.
```

---

**Why the person's notes come first.** They saw it as a user. The team's
findings are sorted around theirs, never the other way.
