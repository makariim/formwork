# Claude Code adapter

**Label: tested.** The boundary has been watched refusing a real command in
this runtime.

## What it wires

One hook. Before any shell command runs, the guard reads it and decides.

- exit `0` — the command runs
- exit `2` — the command is refused, and the reason goes back to the agent

Exit code 2 is the runtime's documented way to block a tool call.

## Installing it

Merge `settings.json` here into `.claude/settings.json` in your project. If you
have no hooks yet, copying the file is enough.

`$CLAUDE_PROJECT_DIR` is set by the runtime and points at your project root, so
the path works wherever the project lives.

## Checking it took

```
formwork/check/run
```

The `guard-wired` check fails if `.formwork.toml` names a runtime and that
runtime's wiring is missing. A boundary that is not installed is a boundary
that is not there, and nothing else would tell you.

## Turning it down

In `.formwork.toml`:

```toml
[strength]
git_boundary = "block"   # block | warn | off
```

`block` is the default and is the right setting for one person working alone.
Turning it down is a line you wrote, which is the point.
