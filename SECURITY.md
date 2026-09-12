# Security

---

## Found a way past a guard?

**That is the most useful thing you can send this project.** One line is enough,
and you do not need a fix.

```
Open an issue: https://github.com/makariim/formwork/issues
Title it: bypass: <the command>
```

**Please open it publicly.** These are not secrets. The guards are pattern
matching over a command line and [`formwork/limits.md`](formwork/limits.md)
already lists every route anybody has found. Yours belongs there too.

---

## What counts as a bypass

Any command that does one of these while the guard says it is fine:

- commits, pushes, merges, or rewrites history
- changes a file in `formwork/guard/` or `formwork/check/`
- changes `.formwork.toml` or your agent's settings file
- re-records the integrity fingerprints

---

## What is already known

Read [`formwork/limits.md`](formwork/limits.md) first. It lists the routes that
are open on purpose, and says why closing them would cost more than it saves.

If yours is on that list, it is not a new finding. If it is not, it is.

---

## What this kit does not claim

> [!WARNING]
> **This is not a sandbox.** The guards stop an agent doing the wrong thing by
> habit. They will not stop one doing the wrong thing on purpose, and nothing
> built out of pattern matching would.
>
> If you need real containment, use a container or a machine you do not mind
> losing.

---

## A guard that refuses ordinary work

**Report those too.** They matter just as much.

A guard that blocks normal work gets switched off, and then nothing is guarded
at all. The command you ran is all anybody needs.
