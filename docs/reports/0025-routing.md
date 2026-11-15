---
brief: 0025
date: 2026-11-15
---

# 0025 Routing one plain prompt

## For you

One prompt now flows like this. The agent reads `docs/standing.md`, then `docs/routing.md` (your corrections, if any), then the new table `formwork/route.md`. It picks one of six kinds, sizes it (task by default), says the plan back, and acts on the size. A task is done by the session that got it. Anything bigger goes to the director, who writes the first brief and stops.
Small example: "the search page shows nothing for one word". The session says "Task, fix: reproduce, fix, add the test. One line brief." and does it. No "Go?".
Big example: "build me an app for X". The director says "Milestone, new product: a one page spec from your words first, for you to read. Then research, design samples, build, our review; release only when you say." It writes brief one and stops.
When you say a route was wrong, the director copies your words into `docs/routing.md` as a dated pair. It never rewords them. That file beats the table.
`formwork setup` now asks a twelfth question and writes the two routing lines to `CLAUDE.md` (or `AGENTS.md`, `GEMINI.md` by runtime), only when the file does not exist. If you have one, it shows the lines to paste.
The kit also ships `formwork/templates/personal-defaults.md` for your own global file. It has one formwork line and no personal content.
Routing accuracy is NOT ESTABLISHED, and the page says so. Step 4 measures it.
No guard refused anything. Tests: 557 passed. Gate green, 14 checks. The brief stays `open` until your read-back.
One gap: the research's step 3 also listed a task size ceiling check. It was not in this brief's job list, so I did not build it.

## For the director

### Contradictions

- Research step 3 (`docs/research/0022-whole-project-builds.md`, part 4) includes "implicit task size with the ceiling" and "two optional standing headings". The brief's job list has neither. His pick moved corrections to a separate file, so the standing headings fall away. The size ceiling is a change to a check under `formwork/check/checks/`, a protected path. Not built. It needs its own brief.
- His global instructions say to set the brief to `status: done`. In this repository `work-paired` refuses done without the read-back, and 0024 followed that. The brief stays `open`.

### What changed

- `formwork/route.md` (new): who routes, what to read first, the six kinds table (question, fix, change, research, deck or document, new product) with size test, template, team and stops; default size task; team order (existing role, relabel, new role); say back and act; corrections; what it cannot do. NOT ESTABLISHED at the top.
- `formwork/templates/routing.md` (new): the corrections file, `docs/routing.md`, created at the first correction, append only, the person's words.
- `formwork/templates/project-instructions.md` (new): the two lines for a project instruction file.
- `formwork/templates/personal-defaults.md` (new): who I am, defaults, taste, how to talk, and one line pointing at `formwork/route.md`. Placeholders only.
- `formwork/roles/method/director.md`: `Owns` names routing above a task; new section "Routing one plain prompt": read order, plan back as kind, size, team, first brief, act on size with no "Go?", corrections transcribed into `docs/routing.md`, the lead does not route, accuracy NOT ESTABLISHED.
- `formwork/roles/method/lead.md`: one sentence under `Does not own`: routing is the director's.
- `formwork/setup`: question 12 (routing), `instruction_lines()` reads the template fence, `instruction_file()` maps the runtime in `.formwork.toml` to `CLAUDE.md`, `AGENTS.md` or `GEMINI.md` (unknown runtime: `AGENTS.md`). An existing file is listed as kept and the lines are printed to paste. The write goes through the existing `Plan.add` and `O_EXCL` path, so it never overwrites.
- `formwork/test_setup.py`: newline counts 11 to 12 in four terminal tests; one more answer in the warn test; nine new checks (claude-code gets CLAUDE.md with both lines, no AGENTS.md; codex gets AGENTS.md, no CLAUDE.md; an existing CLAUDE.md is untouched, reported as kept, lines shown, exit 0; dry run names the file and writes none).
- `FORMWORK.md`: a paragraph under the loop pointing at `formwork/route.md`; one bullet in the setup list.
- `README.md`: setup row says twelve questions and the routing lines.
- `CHANGELOG.md`: three Unreleased lines.
- Generated: `.claude/agents/`, `.codex/agents/`, `.gemini/agents/` director and lead.

### What was run

- `formwork/fw roles`: 2 written for claude-code. `formwork/fw check` then flagged codex and gemini copies stale, so `formwork/fw roles --all`: "86 generated file(s) considered (84 role, 2 skill), 4 written, for: claude-code, codex, gemini-cli".
- `python3 formwork/test_setup.py`: "58 passed, 0 failed".
- `formwork/fw test`: "557 tests, all passed".
- `formwork/fw check`: "GATE: green. 14 check(s), each shown to reject the wrong and accept the right." `kit-leak-scan` ok, `kit-integrity` ok.
- Dash scan over the new files and the added lines: no em or en dashes.

### Fingerprints

`kit-integrity` is green, because nothing under a protected path changed. He re-records fingerprints after review as usual if he wants the record to carry this state.

### Not done, not asked

- No hook injecting the routing table at session start. The research holds it as a later option.
- No routing measurement. That is step 4.
- No check for a task size ceiling or for `docs/routing.md` shape.
- `docs/standing.md` not touched: it is the director's.
