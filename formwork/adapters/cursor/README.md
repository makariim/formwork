# Cursor adapter

**Label: untested.** Documented by the publisher, never run.

## Roles: nothing is generated

Cursor's own documentation names `.claude/agents/` as a location it reads,
alongside `.cursor/agents/` and `.codex/agents/`.

So **the Claude Code output serves Cursor directly.** Generating a second,
identical tree would be duplication for its own sake, and duplication is what
the generator exists to remove.

Run `formwork roles --runtime claude-code` and Cursor finds them.

## Where the tool grant goes

Cursor has `readonly: true|false`. One bit.

That can say "this role may not write". It cannot say "this role may write and
may not start other agents", which is what the challenger needs.

Nothing approximate is emitted. **On Cursor the grant is advice.**

**And no file tells you that**, because nothing is generated for Cursor. The
files Cursor reads are the Claude Code ones, and they carry a Claude Code tool
list that Cursor cannot act on. This page is the only place that says so, which
is worth knowing before you rely on it.

## Blocking

Cursor refuses on exit code 2, and has more hook events than any of the four:
`preToolUse`, `beforeShellExecution`, `beforeMCPExecution`, `beforeReadFile`,
`subagentStart`.

Point `beforeShellExecution` at:

```
formwork/guard/git-boundary   --format cursor
formwork/guard/protected-files --format cursor
```

`subagentStart` is worth knowing about: it can refuse the creation of a
subagent outright, which is the nearest thing Cursor has to the `spawn` grant.
Whether it is a workable substitute is **not established**.
