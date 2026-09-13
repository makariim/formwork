# Contributing

Forks are the point. Take it, change it, keep what you like.

---

## What helps most

**A command that got past a guard.** One line is enough, no fix needed. See
[SECURITY.md](SECURITY.md).

**A normal command that was wrongly stopped.** Just as useful. A guard that
blocks real work is a guard people switch off.

**A report from an untried agent.** Codex, Cursor or Gemini CLI. Wire one up,
ask your agent to commit something, and tell us what happened. Worked or not,
both answers help.

**A new role.** Copy `formwork/roles/TEMPLATE.md` and read
[HOW-TO-ADD-A-ROLE.md](formwork/roles/HOW-TO-ADD-A-ROLE.md) first.

---

## Before you open a pull request

```
formwork check    must say green
formwork demo     must reject every broken test case
formwork test     all 295 must pass
```

---

## Two house rules

These are taken from the kit itself.

> [!IMPORTANT]
> **Change a guard or a check, and add the test that would have caught the
> bug.** Show it failing without your fix. A check nobody has seen fail proves
> nothing.
>
> **Write down a number, and write down the command that made it.**

---

## Good first jobs

- Set up the hooks for Codex, Cursor or Gemini CLI and tell us if they work
- Translate [the first run page](formwork/first-run.md)
- Add a role for something the twenty eight do not cover
- Find a command that gets past a guard

---

## What to expect

This is one person's project. Reviews may be slow. A pull request that adds a
rule without saying what it catches will be sent back, because the kit refuses
those too.
