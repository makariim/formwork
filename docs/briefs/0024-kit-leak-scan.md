---
brief: 0024
stream: method
title: The kit leak scan
status: open, 2026-11-15
---

# 0024 The kit leak scan

## His words

"next" (2026-11-15): step 2 of the build plan in `docs/research/0022-whole-project-builds.md` (part 4, and the "kit leak scan" row in "The checks"). Formwork is a general repository; nothing about one person or machine may live in the kit.

## The job

A new, small check that scans **kit files only** (`formwork/`, `formwork_cli/`, `FORMWORK.md`, and anything the kit installs into projects) for things that belong to one person or machine: real looking home paths (for example `/Users/<name>/...`, `~/<name>`), private network addresses (10.x, 172.16 to 31.x, 192.168.x, Tailscale 100.64.0.0/10), local hostnames (`*.local`, machine names written as hostnames), email addresses, and API key shaped strings. Patterns stay generic: no list of anybody's real names, paths or machines inside the check. Placeholders like `/Users/<you>/` or `example.com` pass. It must say what it cannot tell (a machine named in plain words).

1. Write the check in the kit's style (CATCHES, CANNOT TELL, fixtures in `must-pass` and `must-fail`, shown to reject the wrong and accept the right).
2. Run it on the current kit; fix any real leak it finds, or explain why each hit is a placeholder.
3. Wire it into the gate; update COSTS.md and limits.md as the kit expects.

## Rules

- **If the kit's self-protection guard refuses an edit, stop and report it.** Do not work around a guard with shell scripts or another tool (that happened in 0023); he decides.
- No git writes. Run `formwork/fw test` and `formwork/fw check`; say that he re-records kit fingerprints after reviewing (`formwork/check/checks/kit-integrity --record .`).
- Report at `docs/reports/0024-kit-leak-scan.md`: `## For you` first (at most 6 lines, plain), then details with each command and result. Last message: one line starting `result:`.
