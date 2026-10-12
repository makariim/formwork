---
name: your-role
pack: project
owns: a-short-slug-nobody-else-uses
tools: [read, write, run]
---

# Your role

**Owns.** The one thing this role decides. If you need "and" twice, it is two
roles.

**Does not own.** What people will wrongly bring here, and who it actually
belongs to. Naming the owner is the useful half.

**Tools.** Which of `read`, `write`, `run`, `web`, `spawn` it may use, and why
anything is withheld. Only the lead gets `spawn`.

**Stops when.** The point at which it hands over and halts rather than guessing.

**Would be wrong if.** What it looks like when this role gives bad advice. If
you cannot answer this, you do not yet know what the role is for.

---

All five are required. A role missing one does not load, and the gate says so.

**Four more frontmatter keys are optional**, for a role that started life as a
Claude Code agent:

```
description: the text an agent is picked by. Replaces the Owns sentence
model: opus
skills:
  - a-skill-name
color: blue
```

`description` is used on every runtime. `model`, `skills` and `color` bind on
Claude Code only. Elsewhere the generated file says the role asked for them and
writes nothing. Leave all four out and the generated role is what it always was.
