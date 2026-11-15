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

## Refute
Reviewers by dimension (journeys, words, accessibility, security, whatever
the brief names) work in parallel, one each, and none reads another's
findings first. Then:

1. Merge findings that rest on the same evidence: the same screen, line or
   picture. One finding per piece of evidence, every reviewer who saw it
   named.
2. Every serious finding goes to a verifier who did not raise it. Its answer
   is "refuted" unless the evidence holds when it looks for itself: it opens
   the screen, the file or the picture, and says what it saw.
3. A finding that is refuted is listed as refuted, with why. It is not
   deleted.
4. A reviewer that failed, timed out or came back empty makes the review
   **incomplete**. Say which dimension is missing. Incomplete is never a
   pass, and a review with a missing dimension is not done.

| Finding | Evidence | Raised by | Verifier | Holds or refuted, and why |
|---|---|---|---|---|

The person's own notes are not sent to a verifier. They saw it.

## Part B: fix
Fix the person's notes and the team's findings together, in one pass.
Then walk the journeys again.

## Done when
Every dimension reported, every serious finding verified, every journey
walked again after the fixes, pictures updated, and what is still wrong
listed.
```

---

**Why the person's notes come first.** They saw it as a user. The team's
findings are sorted around theirs, never the other way.

**Why a verifier that defaults to refuted.** A reviewer asked to find
problems finds some, real or not. A second reader who must see the evidence
for themselves cuts the ones that were not there, and the fixes go to what is.

**Why a missing reviewer is a failure.** A dimension nobody reported looks
exactly like a dimension with nothing wrong.
