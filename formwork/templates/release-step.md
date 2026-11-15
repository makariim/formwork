# Release step

Optional. The general pattern for putting a version out. The details (where
it goes, how it is signed, who holds the keys) belong to the project, never
to this page.

---

## The pattern

1. **Another session owns the step.** Not the session that built it. It reads
   the build report and the release steps written in the project.
2. **One written line starts it.** The person writes it, in a brief or a
   message the session reads: which version, and go. Never a schedule, never
   a timer, never "when the build is green".
3. **It stops at the first failure.** It does not retry, skip or work
   around. It says which step failed, what it printed, and stops.
4. **It ends with a release record.** One file, saved where the project keeps
   them.

---

```markdown
---
status: open
stream: release
starts: after build
---

# NNNN Release <version>

Started by: <the person's line, word for word, with its date>

## Steps
The project's own release steps, in order, each with the command it runs.

## Stop rule
At the first step that fails: stop, say which, paste what it printed.
```

The release record:

```markdown
# Release <version>

- Started by: <the line>
- Steps run: <each, with its result>
- Stopped at: <step, or "none">
- What is out: <version, and where, in the project's words>
- Not proven: <carried from the build report>
```

---

**Why another session.** The session that built a thing believes it works.
The one that releases it should have only the written record to go on.
