# Release checklist

Optional. Release scope as rows, each naming where it came from, checked one
by one by somebody who built none of it. The method is in
[`../operations/README.md`](../operations/README.md); the release itself is
[`release-step.md`](release-step.md).

Saved as `docs/release-checklist.md`, or one per release. Scope is frozen when
the checking starts. After that, only fixes for breakage.

---

```markdown
# Release checklist: <release>

Build checked: <build id or commit, a fresh release build>
Checker: <role and session; never a role that built this release>
Scope frozen: YYYY-MM-DD

Every row is verified on the build above and marked pass, fail, or not
testable here, with the evidence. Nothing ships with a fail. A known limit is
written into its row, never dropped.

## <group: a round, a stream, a fix round>

| # | Item, stated so it can be checked | Source | Verdict | Evidence or command |
|---|---|---|---|---|
| A.1 | the behaviour, with its limits and numbers | ruling N, report NNNN, or the human's words | pass / fail / not testable here | |

## Before release
- Backup or rollback named
- Who receives it
- Release notes in plain words
```
