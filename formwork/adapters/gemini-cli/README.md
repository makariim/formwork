# Gemini CLI adapter

**Label: untested.** Documented by the publisher, never run.

## Blocking

`BeforeTool` refuses on exit code 2, with the reason taken from standard error.
Configure hooks in `.gemini/settings.json`, pointing at:

```
formwork/guard/git-boundary   --format gemini-cli
formwork/guard/protected-files --format gemini-cli
```

## Roles

`formwork roles --runtime gemini-cli` writes `.gemini/agents/<name>.md`:
markdown with YAML frontmatter, `kind: local`, and a `tools:` list.

## Where the tool grant goes, and the gap

Gemini CLI takes a named allowlist and enforces it, which is what the kit
wants. Two documented tool names are known and used:

```
read  →  read_file, grep_search
run   →  run_shell_command
```

**The name of the file-writing tool is not among the publisher's documented
examples.**

An allowlist is exact: writing one that omits a tool the role needs would
silently take that tool away. So the generator **writes no list at all** for
any role that needs `write`, and puts a line in the file saying why.

The consequence, stated plainly: **most roles get no enforced grant on Gemini
CLI today**, because most roles write. Read-only roles, the reviewer, get a
real one.

Closing this needs one fact: the documented name of the write tool. It is a
research task, not a design problem.

## One limit that costs this kit nothing

Subagents cannot start subagents, even with a wildcard grant. Only the lead
spawns, so nothing here is affected.
