# Codex adapter

**Label: untested.** The hook wiring has not been watched in a live Codex task.

## Blocking

Codex refuses a tool call on exit code 2. Wire both guards to `PreToolUse`
with a matcher that includes `Bash|apply_patch`, pointing at:

```
formwork/guard/git-boundary   --format codex
formwork/guard/protected-files --format codex
```

Hooks go in `.codex/hooks.json`. `protected-files` reads the paths in Codex
`apply_patch` headers, including padded headers and patches passed through
shell arguments, wrappers, pipes, and heredocs. It checks `Add File`,
`Update File`, `Delete File`, and `Move to` paths. An `apply_patch` or
`applypatch` call with no readable patch text is refused. `guard-wired` also
accepts a Codex matcher such as `Bash|Edit|Write`: Codex's `Edit` and `Write`
names cover patch calls, while `Bash` covers shell calls.

For a project that also uses another runtime, list them under `[bindings]`:

    runtime = "claude-code"
    runtimes = ["claude-code", "codex"]

`guard-wired` checks both runtimes. Codex has no supported `Stop` hook for
`quality-gate`, so run `formwork/check/run` by hand at the end of a Codex task.

## Roles

`formwork roles --runtime codex` writes `.codex/agents/<name>.toml`.

**Of the four runtimes, this is the one that does not take markdown.** It takes TOML, with
`name`, `description` and `developer_instructions`.

## Where the tool grant goes

**Nowhere.** Codex has a sandbox mode, which is not a tool list. A role that
may not start other agents cannot say so here.

Each generated file states that in a comment rather than emitting a setting
that looks like a restriction and is not. **On Codex the grant is advice.**

## A defect worth knowing before you rely on this

Its issue tracker carries a report that agents in `.codex/agents/` cannot be
invoked by name from a tool-backed session. The runtime exposing only generic
spawning, and that the configuration has to be extracted and passed as
overrides instead.

If that holds, these generated files exist and cannot be used as documented.
**Not established here**, and worth checking before depending on it.
