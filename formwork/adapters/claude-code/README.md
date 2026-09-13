# Claude Code adapter

**Label: tested.** The boundary has been watched refusing a real command in
this runtime.

## What it wires

**Four hooks across three events**, not one. Copying only part of this file
leaves you with part of the protection.

| Event | What runs | What it does |
|---|---|---|
| `PreToolUse` on `Bash` | `git-boundary` | refuses commits, pushes and merges |
| `PreToolUse` on `Bash` | `protected-files` | refuses changes to the kit's own files |
| `PreToolUse` on `Write\|Edit\|NotebookEdit` | `protected-files` | the same, for direct edits |
| `Stop` | `quality-gate` | refuses to end a turn while the gate is red |

Before any shell command runs, the guards read it and decide.

- exit `0`. The command runs
- exit `2`. The command is refused, and the reason goes back to the agent

Exit code 2 is the runtime's documented way to block a tool call.

## Installing it

Merge `settings.json` here into `.claude/settings.json` in your project. If you
have no hooks yet, copying the file is enough.

`$CLAUDE_PROJECT_DIR` is set by the runtime and points at your project root, so
the path works wherever the project lives.

## Checking it took

```
formwork check
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
