# How each runtime declares a role

**Phase:** R1. **Date:** 2026-09-12.

The earlier research asked one question: can this runtime refuse a command? It
never asked how each one expects a *role* to be declared. B7 cannot build the
generator without that, so this is the second pass.

## The evidence rule for this document

Every row is **documented capability, not observed behaviour.** Publishers'
own documentation was read. Nothing here was run.

---

## The table

| Runtime | Where | Format | Tool restriction |
|---|---|---|---|
| **Claude Code** | `.claude/agents/*.md` | markdown, YAML frontmatter | `tools:` — a list of permitted tools |
| **Cursor** | `.cursor/agents/`, **or `.claude/agents/`, or `.codex/agents/`** | markdown, YAML frontmatter | `readonly: true` — a single boolean |
| **Gemini CLI** | `.gemini/agents/*.md` | markdown, YAML frontmatter | `tools:` — an allowlist, wildcards allowed |
| **Codex** | `.codex/agents/*.toml` | **TOML, not markdown** | `sandbox_mode` — not a tool list |

---

## The finding that changes B7

**Three of the four agree, and one does not.**

Claude Code, Cursor and Gemini CLI all use a markdown file with YAML
frontmatter, and two of the three restrict tools with a `tools:` list. Codex
uses TOML with a different field set entirely.

**And Cursor reads Claude Code's directory.** Its documentation names
`.claude/agents/` and `.codex/agents/` alongside its own, so one file can serve
two runtimes without generation at all.

## What this means for the generator

The earlier design assumed four different outputs from one source. In fact:

- **one markdown file** covers Claude Code and Cursor directly, and Gemini CLI
  with a field rename
- **Codex needs a genuine conversion**, markdown to TOML, with the fields
  remapped

So the generator is smaller than expected in three cases and a real translation
in the fourth.

## Where the tool grant does not survive translation

This is the part K5 will have to decide about, because it cannot be papered
over.

| Runtime | What a grant can say |
|---|---|
| Claude Code | exactly which tools, by name |
| Gemini CLI | exactly which tools, by name, with wildcards |
| Cursor | **read-only, or not.** Nothing finer |
| Codex | **a sandbox mode.** Not a tool list at all |

The kit's 28 roles each declare a list like `["read", "write", "run"]`. That
maps cleanly onto two runtimes, collapses to one bit on Cursor, and does not
map onto Codex at all.

**Decided 2026-09-12: generate everywhere, and say plainly where the grant
binds.**

The kit generates a role file for all four runtimes. It states, in one place
and not in a footnote, that a tool grant is **enforced on Claude Code and
Gemini CLI** and is **advice on Cursor and Codex**.

Two options were rejected:

- **Generate the nearest available setting and leave it unlabelled.** This is
  the only one that lies. A file reading `readonly: false` looks like a
  decision and is not the one the role asked for — a restriction that appears
  real and is not is the precise failure this kit exists to prevent.
- **Refuse to generate what cannot be enforced.** Honest, and punishing. A
  Codex forker would lose most of the kit over a restriction most of them were
  never relying on, and a kit that mostly refuses to work is a kit nobody keeps.

**And the honesty is a check, not a sentence.** `role-shape` already reads tool
grants; it is extended so that nothing in the repository can claim a runtime
enforces a grant it cannot express. A sentence can be deleted by somebody
tidying up. A check cannot.

---

## Two defects worth knowing before relying on any of this

**Codex: named subagents may not be invocable.** Its own issue tracker carries a
report that custom agents in `.codex/agents/` cannot be called by name from a
tool-backed session — "the runtime only exposes generic spawning" — and that
the configuration has to be extracted and passed as overrides instead. If that
holds, a generated Codex role file exists and cannot be used as documented.

**Gemini CLI: subagents cannot call subagents.** Recursion is prevented even
with a wildcard grant. The lead role is the only one that spawns, so this costs
the kit nothing — but it would matter to anyone designing deeper nesting.

---

## Skills and commands

Not established. This pass asked about roles only.

Each runtime also has some notion of a named procedure — a skill, a command, a
prompt — and their formats differ again. **B7 should not assume anything about
them**, and a third pass is required before the kit ships anything of that
shape.

---

## What would make this document wrong

- A runtime changing its format. All four are actively developed.
- A documented field that does not work in practice, which is precisely the
  Codex defect above and is the gap between *documented* and *observed*.
- Reading a third-party summary instead of the publisher. Every row here came
  from the publisher, except the Codex defect, which came from its own issue
  tracker.

## Sources

- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Cursor subagents](https://cursor.com/docs/agent/subagents)
- [Gemini CLI subagents](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/core/subagents.md)
- [Codex custom agents, and the invocation defect](https://github.com/openai/codex/issues/15250)
