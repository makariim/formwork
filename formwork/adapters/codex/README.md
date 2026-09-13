# Codex adapter

**Label: untested.** The publisher documents everything below. Nobody has run
it. It stays untested until somebody watches it work.

## Blocking

Codex refuses a tool call on exit code 2, the same as the other three, so the
same guards serve it. Wire both to `preToolUse`, pointing at:

```
formwork/guard/git-boundary   --format codex
formwork/guard/protected-files --format codex
```

Hooks go in `.codex/hooks.json`, or inline in `~/.codex/config.toml`. Its own
source carries `PreToolUseHookResult::Blocked`, so the mechanism is real even
though this wiring has not been exercised.

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
