---
brief: 0024
date: 2026-11-15
---

# 0024 The kit leak scan

## For you

I stopped because the guard refused an edit, as the brief says to. The new check `kit-leak-scan` flags its own regex on line 88 as a home path. Fixing that one line is an edit to `formwork/check/checks/`, and the guard refused it.
So the gate is red for two reasons. One is that self-hit. The other is `kit-integrity` reporting the new check as an addition, which is expected until you re-record.
Apart from that self-hit, the kit is clean. A corrected copy of the check found nothing in 174 kit files, and a plain grep agrees.
Fixtures (7 must-fail, 3 must-pass), FORMWORK.md, COSTS.md, limits.md, README, glossary and CHANGELOG are done. Tests: 546 passed.
Your step: make the one-line fix below, review the new check, then run `formwork/check/checks/kit-integrity --record .`. The brief stays `open`.

## For the director

### The refusal

- Edit on `formwork/check/checks/kit-leak-scan` line 88, refused by `formwork/guard/protected-files`: "REFUSED by self-protection: editing formwork/check/checks/." I did not work around it.
- Creating the check, its fixtures and `chmod +x` were allowed. New files under protected paths pass, because they remove nothing. Once a file exists, it is protected.
- The fix, line 88, the `HOME` pattern: change the capture group `([^/\\\s`'\"<>)\]]+)` to `([A-Za-z0-9_][A-Za-z0-9_.-]*)`. A user name then has to start with a letter, digit or underscore, so `/Users/|` in the check's own regex no longer matches. Placeholders like `/Users/<you>/` still pass, because they no longer match at all.
- Optional tidy, line 196: `if local in NOT_PEOPLE or placeholder_word(local) and domain in PLACEHOLDER_DOMAINS:` can become `if local in NOT_PEOPLE:`. The next lines already skip every placeholder domain. Behaviour does not change.
- A copy with both changes ran in my scratch folder: `FORMWORK_EXCLUDE=$PWD/formwork/check/fixtures python3 -I <copy> .` printed "174 kit file(s) read, nothing that belongs to one person or machine", exit 0. Every fixture gives the same result with that copy as with the live check.

### What was built

- `formwork/check/checks/kit-leak-scan` (new). It reads `formwork/`, `formwork_cli/`, `FORMWORK.md`, and role files under `.claude/agents`, `.gemini/agents` and `.codex/agents` that carry `GENERATED FROM`. It looks for home paths (`/Users/`, `/home/`, `C:\Users\`, `~name/`), private IPv4 (10/8, 172.16/12, 192.168/16, 100.64/10), hostnames ending `.local`, `.lan`, `.internal`, `.localdomain`, `.home.arpa` or `.ts.net`, email addresses, and key prefixes (`sk-`, `ghp_` and friends, `github_pat_`, `glpat-`, `AKIA`/`ASIA`, `xox?-`, `AIza`, private key headers). Placeholders pass: names in angle brackets, `$VAR`, a short list of generic words (you, user, example and the like, no real names), RFC 2606 domains, `git@`/`noreply@`, documentation addresses, and keys made of x's or containing `...`. It prints keys cut to six characters. It honours `FORMWORK_EXCLUDE`. The docstring has CATCHES and CANNOT TELL.
- Fixtures, all invented. must-fail: a-home-path, a-private-address, a-tailscale-address, a-local-hostname, an-email, an-api-key (random `sk-` string, no real provider shape), a-generated-role. must-pass: placeholders, a-leak-outside-the-kit (a home path in `docs/` is the project's own business), a-hand-written-agent (an agent with no generated marker is not read).
- Wiring: the gate finds checks on its own. I added a row to the "What is blocked" table in `FORMWORK.md`, a `kit-leak-scan` paragraph in `formwork/limits.md`, and a CHANGELOG line. I changed thirteen to fourteen in README (three places) and `formwork/glossary.md`.
- `formwork/COSTS.md`: re-measured timing and file count (below). The old 201 had already gone stale after 0023.

### Commands and results

- Each fixture, run directly: all 7 must-fail exit 1, all 3 must-pass exit 0, with both the live check and the corrected copy. Each must-fail fails on its intended line, for example `formwork/models.md:3 a private address: 192.168.40.12` and `formwork_cli/__init__.py:2 an email address: rowan.hale@hale-and-sons.co.uk`.
- `FORMWORK_EXCLUDE=$PWD/formwork/check/fixtures formwork/check/checks/kit-leak-scan .`: exit 1, two hits, both on line 88 of the check itself.
- Grep over the kit, fixtures excluded, for home paths, emails, private addresses and `.local`/`.lan`/`.internal`: only placeholders (`git@example.com` in `formwork/guard/test_boundary.py:65`, `t@example.invalid` in `formwork/test_sync.py:54`) and the check's own docstring and regex. No real leak, so nothing in the kit needed fixing.
- `formwork/fw test`: "546 tests, all passed".
- `formwork/fw check`: red. kit-integrity "added formwork/check/checks/kit-leak-scan". kit-leak-scan has the two self-hits. 0 inputs wrongly accepted, 0 wrongly rejected. The other twelve checks are ok.
- `/usr/bin/time -p formwork/fw check`, three runs: real 4.76, 4.88, 5.29.
- `find formwork -type f | wc -l`: 310.

### Not established

- Whether the generic name list lets a real user name through. A real name that is not on the list is flagged, which is the intent. A real name that happens to be on it (for example "joe") passes.
