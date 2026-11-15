# Upstream

Optional. The record for a skill brought in from somewhere else, kept as
`.claude/skills/<name>/UPSTREAM.md` beside the copied files. How and why:
`formwork/bring-a-skill.md`.

---

```markdown
# Upstream

`SKILL.md` and `LICENSE` in this folder are copied byte for byte from:

    repository  <address of the source repository>
    commit      <full commit hash, never a branch>
    version     <the source's version, or "none">
    date        <YYYY-MM-DD> (commit date)
    licence     <name>, <copyright line>, in LICENSE beside this file
    sha256      <hash>  SKILL.md
                <hash>  LICENSE

Do not edit either file. This project's own change to the skill is in
`<the project role that names it>`.

Named in `skills:` by: `<role>`.

## Nothing updates on its own

A new upstream version takes effect only when somebody chooses it. To update:

1. Read the upstream diff from the commit above to the new one, all of it.
2. Fetch `SKILL.md` and `LICENSE` at the new commit, and nothing else.
3. Check that the project role's own change still fits.
4. Change the commit, version, date and sha256 lines above.
5. Run `formwork roles`, then `formwork check`.
6. Commit it, so the update is one change with your name on it.
```

For a skill written in the project, the whole file is one line:

```markdown
written here, no upstream
```
