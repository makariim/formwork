# Build

Optional. A brief for building version 1, or one phase of it, from an
accepted spec. Give it `stream: build`.

---

```markdown
---
status: open
stream: build
starts: after spec
---

# NNNN Build: <what>

## What version 1 is
One paragraph, from the spec. What it is not, from "Not in version 1".

## Order
What is built first, and why. Each step something a person could try.

## Team, split by files
| Role | Owns these files |
|---|---|
| backend | the server folder |
| frontend | the app folder |

No two roles share a file. Where they must meet, name the contract.

## Review rounds
Sized to the part: a task gets the check; a part a person will use gets a
review round (`formwork/templates/review-round.md`).

## The report must contain
- What works, and how it was shown to work.
- What is not done.
- **Not proven**: what only the real device, the real data or a real user can
  prove. Listed one by one.
- **Touched outside my files**: each file changed outside the files the team
  table gives this role, named one by one, or "none".
- **Packages added**: each package or data set added, with its licence, what it
  installs, and where it came from, or "none".
```

The last two lines matter most when the build is split between agents. They
are how the lead finds two pieces that met in one file, and a dependency that
`legal` or `security` should read before it ships.

---

## Before the next phase opens

The second default gate: **unproven items listed and seen before the next
phase opens.** The build report lists them under "Not proven". The person's
read-back on that report is the "seen". The next brief carries `starts: after
build`, and `formwork check` refuses it until the read-back is there.

A phase that runs beside the build, such as a review of the running product,
does not wait. No order of phases is fixed.
