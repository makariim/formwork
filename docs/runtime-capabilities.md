# Runtime capabilities

**Date:** 2026-09-12. **Question:** which coding agent runtimes can actually
refuse a command, and which can only advise?

This exists because the kit's one possible contribution is enforcement that
blocks, and nobody had checked which runtimes can block. The survey examined
kits, not runtimes.

## What counts as blocking

A runtime blocks if it can run an external program before a tool call and
refuse the call based on that program's result. Advising — printing a warning
while the call proceeds — does not count.

## The evidence rule for this document

**Every row is documented capability, not observed behaviour.** Documentation
was read; nothing here was executed, with one exception noted in the table.

A row marked *documented* means the runtime's own publisher says it can do this.
It does not mean it was seen doing it.

---

## The table

| Runtime | Blocks? | Mechanism | Evidence |
|---|---|---|---|
| **Claude Code** | **Yes** | `PreToolUse`. Exit code 2, or JSON `permissionDecision: "deny"` | Official docs, **plus observed** — a source project runs this in production |
| **Codex** | **Yes** | `preToolUse` and `permissionRequest`. Exit code 2 with reason on stderr, or JSON `permissionDecision: "deny"` | Official docs. Hook machinery also present in the repository source |
| **Cursor** | **Yes** | `preToolUse`, `beforeShellExecution`, `beforeMCPExecution`, `beforeReadFile`, `subagentStart`. Exit code 2, or `"permission": "deny"` | Official docs |
| **Gemini CLI** | **Yes** | `BeforeTool`. Exit code 2 with reason on stderr, or JSON `"decision": "deny"` | Official docs in the project repository |
| **opencode** | **Partly** | `tool.execute.before` — a plugin throws to block | Official docs, **and three open defects** — see below |
| **Windsurf** | **Probably** | Pre-hooks across prompts, reads, writes, shell and MCP; exit code 2 stops the action | **Third-party sources only.** No primary document read. **NOT ESTABLISHED** |
| **Aider** | **No** | No hook system of its own | Official docs. See the warning below |

---

## The finding that matters

**Four independent runtimes converged on the same contract.**

Claude Code, Codex, Cursor and Gemini CLI all implement the same shape: a hook
that runs before a tool call, and **exit code 2 blocks it**. Three of the four
also accept a JSON deny object. The event names differ; the contract does not.

That was decided for this kit before any of this was known. K0 item 4 chose the
exit status as the enforcement contract on the grounds that it names no
language and no tool. It turns out to be the convention the industry already
settled on.

**What this changes.** An adapter is not a rewrite per runtime. It is the same
executable, wired up in four different settings formats. The kit can honestly
support four runtimes, not one.

---

## opencode — blocks, with holes

The mechanism exists: a plugin's `tool.execute.before` handler blocks a call by
throwing. But its own issue tracker carries three defects that matter for
enforcement:

- Tool calls made by **subagents** are not intercepted, so a policy enforced by
  a plugin can be bypassed by delegating the work.
- Permission denials **have no effect when the agent is invoked through the
  SDK**.
- The `permission.ask` hook is defined in the plugin types but **never fires**,
  so a plugin cannot intercept a permission request.

**Disposition: label it partial, and name the subagent gap specifically.** A
forker who believes the boundary holds and delegates to a subagent gets an
enforcement failure they have no way to see.

---

## Aider — the boundary cannot hold

Aider deserves its own note, because "advice only" understates the problem.

**It commits by default.** Its documentation: "Whenever aider edits a file, it
commits those changes with a descriptive commit message." Disabling that
requires `--no-auto-commits`.

**It skips pre-commit hooks by default**, passing `--no-verify`. Enabling them
requires `--git-commit-verify`.

**It has no hook system**, so nothing can enforce either flag.

The kit's most emphasised rule is that the agent never touches version control.
On Aider, committing is the normal behaviour, the usual way of catching that is
disabled by default, and there is no mechanism to restore it.

**Disposition: not "advice only". Aider is incompatible with the git boundary
as stated, and the kit must say so in those words.** Anything softer is a
promise that will be broken silently.

---

## What this answers, and what it does not

**Answers K0 item 7**, which asked which runtime the adapter targets. The
answer is now four rather than one, on a shared contract.

**Does not establish that any of them work.** Documentation was read. Only
Claude Code has been observed blocking anything, and that observation comes
from one project.

**Windsurf is the weakest row.** Its capability was taken from third-party
security tooling that claims to register on its pre-hooks. No primary document
was read, and its naming appears to have changed. Treat it as unverified until
someone reads the publisher's own documentation.

## What would make this document wrong

- A runtime changing its hook contract. All four are actively developed, and
  three of the four contracts were published within the last year.
- A documented capability that does not work in practice. This is the gap
  between *documented* and *observed*, and it is closed only by running each
  one.
- A runtime absent from this table. Aider was included because it is widely
  used and turned out to be the most important row. Others were not searched.

## Sources

- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Codex hooks](https://learn.chatgpt.com/docs/hooks)
- [Codex hook event names, in source](https://raw.githubusercontent.com/openai/codex/main/codex-rs/app-server-protocol/schema/typescript/v2/HookEventName.ts)
- [Cursor hooks](https://cursor.com/docs/agent/hooks)
- [Gemini CLI hooks reference](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/hooks/reference.md)
- [opencode permissions](https://opencode.ai/docs/permissions/)
- [opencode subagent bypass defect](https://github.com/anomalyco/opencode/issues/5894)
- [opencode SDK permission defect](https://github.com/sst/opencode/issues/6396)
- [opencode permission.ask defect](https://github.com/anomalyco/opencode/issues/7006)
- [Aider git integration](https://aider.chat/docs/git.html)
- [Windsurf pre-hook claim, third party](https://agentkeeper.dev/windsurf-security)
