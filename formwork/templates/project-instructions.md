# Project instructions

Two lines for the instruction file your agent reads in this project:
`CLAUDE.md` for Claude Code, `AGENTS.md` for Codex and Cursor, `GEMINI.md` for
Gemini.

`formwork setup` offers them. It writes the file only when the project has none.
When you already have one, it leaves it alone and shows you these lines to paste
yourself.

---

```markdown
Before replying, read `docs/standing.md`, `docs/routing.md` if it exists, and `formwork/route.md`; for what formwork offers here and when to use each part, `formwork/capabilities.md`.
Say the plan back (kind, size, team, first brief) in one line for a task, two above it; then act on its size as `formwork/route.md` says.
```

**If your instruction file was written before the capability map existed**,
its first line ends at `formwork/route.md`. Replace it with the first line
above, so the agent can answer "what can you do here?" from the map.
