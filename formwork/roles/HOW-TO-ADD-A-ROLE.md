# Adding a role

---

## Your own

1. `mkdir -p formwork/roles/project` if it is not there. Version control does
   not carry empty folders, so a fresh fork will not have it.
2. Copy `TEMPLATE.md` into `formwork/roles/project/<name>.md`.
3. Fill in the five sections **and the four frontmatter fields**. A role with
   the sections and no frontmatter does not load.
4. Run `formwork roles` to generate it for your runtime.
5. Run `formwork check`.

**There is no step that registers it anywhere.** Every role in
`formwork/roles/` is available. Nothing to add to `.formwork.toml`, and a
check refuses a `[roles]` section if you add one.

If a section is missing, or another role already claims your `owns` slug, the
gate refuses and tells you which.

---

## From somewhere else

There are large public catalogues of ready-made agent definitions. Use them.
Converting one takes about five minutes:

1. **Keep everything they know.** The domain knowledge is why you took it.
2. **Throw away the preamble.** "You are a world-class expert in…" is not a
   role definition, it is a costume.
3. **Write the five sections.** Owns, does not own, tools, stops when, would be
   wrong if. The original almost certainly has none of these, which is exactly
   what the five sections are for.
4. **Set the tool grant deliberately.** Most imported roles assume they can do
   anything. Decide what this one actually needs.
5. **Give it an `owns` slug** nobody else has.

An unconverted role does not load. That is on purpose: a role with no stated
boundary is a role that will wander into somebody else's work.

---

## Turning roles on

**Not built yet, and this section says so rather than pretending.**

Every role in `formwork/roles/` is currently available. There is no switch.

The intention is a `[roles]` block in `.formwork.toml` naming which packs are
on. Until something actually reads it, writing one would be configuration that
does nothing, and a setting that appears to work and does not is worse than an
honest absence.

---

## Where a tool grant actually binds

Every role declares which tools it may use. **That is a real restriction on two
runtimes and advice on two others**, because the other two cannot express it.

| Runtime | What it can hold a role to |
|---|---|
| **Claude Code** | exactly which tools, by name. Enforced |
| **Gemini CLI** | by name, but see below. Enforced for 1 role in 27 |
| **Cursor** | read-only, or not. One bit, nothing finer |
| **Codex** | a sandbox mode, which is not a tool list at all |

**Gemini CLI needs a qualifier.** It takes a named list and would enforce it.
But the documented name of its file-writing tool is not established, and the
generator will not guess one and silently remove a tool a role needs. So it
writes no list for any role that writes, which today is **26 of the 27**. Only
the reviewer gets an enforced grant there.

So the challenger being denied the power to start other agents is enforced on
Claude Code, approximated on Cursor, unrepresentable on Codex, and advice on
Gemini CLI.

**The kit generates a role for all four anyway**, because a Codex forker losing
most of the team over a restriction they were not relying on is worse than a
stated limit. What it does not do is pretend.

This is not only written here. `role-shape` refuses any document in this
repository that claims a grant binds on a runtime that cannot express one
because a sentence can be deleted by somebody tidying up, and a check cannot.

It caught the first draft of this very paragraph, which is the best argument
for it available.

**It does not catch every overclaim**, only those three shapes. The Gemini
qualifier above is held in place by nothing but this page.

Established by reading each publisher's own documentation. Recorded in
`docs/role-formats.md`.

---

## What makes a bad role

- **It owns two things.** Split it.
- **It owns what another role owns.** The gate catches this one.
- **It cannot be wrong.** If you cannot say what bad advice from it looks like,
  it is a mood, not a role.
- **It exists because the pack looked thin.** A role arrives when the work
  arrives, not before.
