# Report 0035: build and measure operations, and a capability map

## For you

You asked for two things. First, bring the working practices from the health app's engine round into formwork. Second, make formwork easy to find your way around, for a person and for an agent. Both are built. The gate is green on all 19 checks and all 578 tests pass.

**Part 1 is a new optional pack, `formwork/operations/`.** It sits beside the taste and research packs and works like them: it guides, and it is never a check. It covers the eight practices in the brief:

- **The ladder.** Check each part alone first, then join them one at a time. Use the perfect input diagnostic to tell a reading fault from a building fault. A lost test says "this build", never "the idea".
- **The iteration loop with limits.** Three failed fixes of one kind of fault means a design call. A part driven by a model gets three revisions. A set that has been read becomes dev.
- **Spending in stages.** Paid runs start only after the free checks pass. Each stage has a written entry condition and a cost.
- **The per route ship rule.** A route ships when it clearly wins. A small gain ships when it stays inside a margin written before the measure. Every shipped route keeps a fallback.
- **Frozen contracts with one owner.**
- **The director's decision log and the sourced release checklist.** The checklist is checked row by row by somebody who built none of it.
- **The checks automatic tests miss.** An applied value check, scorer self tests, an independent re-check, and a scope freeze.
- **Running many sessions safely.** This has its own page, `parallel.md`.

The pack comes with:

- 14 pitfalls, each with a public source;
- four templates: ladder plan, decision log, release checklist, parallel worker brief;
- short pointers in the director, lead, tester and record-keeper roles.

Where the research pack (0034) already says something, this pack links to it instead of saying it again. No 0034 file was touched.

**Part 2 is a capability map, `formwork/capabilities.md`.** It is one page listing everything the kit does, with one example each. It is organised by what you want to do: plan, research, build, measure, review, report, release. Then it lists the method, the roles, the packs, the skills, the templates, the guards and checks, the adapters, the commands and the settings. It tells an agent to answer "what can you do here?" from that page, and to say what is enforced, what is advice and what is NOT ESTABLISHED.

Agents in installed projects find the map three ways:

- Every generated role file now points at it, next to the style page.
- The routing line that `setup` writes into `CLAUDE.md`, `AGENTS.md` or `GEMINI.md` names it.
- `route.md` says that "what can you do here?" is answered from it.

People find it from:

- a new "What it can do" section in the README;
- a pointer in `FORMWORK.md`;
- a new template that gives a project's own README a "how work runs here" section.

**A bug I fixed.** `setup` wrote the routing lines to `AGENTS.md` for Gemini CLI, not `GEMINI.md`. It looked the runtime up as `gemini`, but the runtime is called `gemini-cli`. A new test fails on the old code and passes now.

**Nothing moved.** I decided against reorganising the folders. Moving files would break links in projects that already use the kit, and `sync` would delete the old paths. The map gives the navigation without that cost.

**What installed projects need to do.** After `formwork sync`, run `formwork/fw roles`, as after any change to the generator. If their instruction file came from an older `setup`, `sync` now names that file but never edits it. They paste the new first line from the template. The CHANGELOG says this under Unreleased.

**A fresh reviewer checked the new pages against the files and found real problems. All are fixed:**

- The pack mapped a spending stage to a `starts:` line in prose. The `gates` check refuses prose, so following the pack would have turned the gate red.
- Running parallel workers would trip the one-open-brief limit, and the pack never said so. It now tells the person to raise `open_briefs`, or set it per stream, before the first worker starts.
- The pack let the director ship past a missed bar and make design calls. Those are now the person's decisions, as the research pack and the core rules say. The director proposes and logs the evidence.
- The pack named the reviewer as the release checker, but the reviewer cannot run anything. It is now the record-keeper or the tester.
- The reviewer also found smaller errors in the map, two citations, and numbers repeated in the templates. All fixed.

**What I did not do, and what is open:**

- I added no hook. The adapter files are protected, and the instruction files plus the role pointers already reach the agent. A start-of-session hook that prints the map is possible if you want it, but it would need you to change protected files.
- `route.md` changed by three lines. The routing score written on that page (44 and 45 of 49) was not measured again, because that costs money. Whether the score moved is NOT ESTABLISHED.
- Every number in the pack (3 fixes, 45 minutes, a margin of minus 5 points) is the default from one round. None was measured as the best value.

Nothing needs your decision to keep working. When you are ready, read it back. You commit.

## Accepted
accepted: 2026-11-22
in my words: read it and i accept it, let's push and release

## For the director

### What changed

| File | What |
|---|---|
| `formwork/operations/README.md`, `parallel.md`, `pitfalls.md` | new: the operations pack, `ops-1` to `ops-14` |
| `formwork/templates/ladder-plan.md`, `decision-log.md`, `release-checklist.md`, `parallel-worker-brief.md` | new: the pack's templates |
| `formwork/templates/readme-section.md` | new: a project README section |
| `formwork/capabilities.md` | new: the capability map |
| `formwork/roles/method/director.md`, `lead.md`, `record-keeper.md`, `formwork/roles/packs/tester.md` | one paragraph each pointing to the pack |
| `formwork/build`, `formwork/test_build.py` | `CAPABILITY_NOTE` in every generated role; the golden test updated to match |
| `formwork/setup`, `formwork/test_setup.py` | `gemini-cli` maps to `GEMINI.md`; tests for it and for the map in the routing line |
| `formwork/sync`, `formwork/test_sync.py` | names an instruction file that predates the map, never edits it; tests |
| `formwork/templates/project-instructions.md` | the first routing line names the map; migration note |
| `formwork/route.md` | two lines: "what can you do here?" is answered from the map |
| `FORMWORK.md`, `README.md`, `formwork/glossary.md`, `CHANGELOG.md` | pointers, the "What it can do" section, index rows, counts (2 skills, 3 packs), terms, the Unreleased entry and migration note |
| `.claude/agents/*`, `.codex/agents/*`, `.gemini/agents/*` | regenerated |

Not mine, in the tree: `.formwork.toml` and `docs/briefs/0033-three-small.md` (his changes through the director), and all of 0034's files.

### What was run

- `formwork/fw roles --runtime claude-code`, then `codex`, then `gemini-cli` (twice: after the role pointers, then after the generator change).
- `formwork/fw check`: `GATE: green. 19 check(s), each shown to reject the wrong and accept the right.`
- `formwork/fw test`: `578 tests, all passed`.
- The old `setup` against the new test (`git show HEAD:formwork/setup` copied in, then restored): `58 passed, 3 failed`, including `gemini-cli gets GEMINI.md`.
- A scratch project in the job's temp folder: `install --runtime claude-code`, `setup --defaults`, `check`, with `FORMWORK_STATE_DIR` set to that temp folder: green; its `CLAUDE.md` and every agent file name `formwork/capabilities.md`.
- Two subagents: a researcher who read the health app's sources (read only), and a reviewer who checked the new pages against the files (12 findings, all acted on).

### Git status

Only the paths this brief touched; the full list is longer because of 0034 and the regenerated agents.

```
 M CHANGELOG.md  M FORMWORK.md  M README.md
 M formwork/build  M formwork/setup  M formwork/sync  M formwork/route.md  M formwork/glossary.md
 M formwork/roles/method/{director,lead,record-keeper}.md  M formwork/roles/packs/tester.md
 M formwork/templates/project-instructions.md
 M formwork/test_build.py  M formwork/test_setup.py  M formwork/test_sync.py
 M .claude/agents/*  M .codex/agents/*  M .gemini/agents/*
?? formwork/capabilities.md  ?? formwork/operations/
?? formwork/templates/{ladder-plan,decision-log,release-checklist,parallel-worker-brief,readme-section}.md
?? docs/briefs/0035-build-measure-and-map.md  ?? docs/reports/0035-build-measure-and-map.md
```

Nothing staged, nothing committed, no release, no version bump.

### The three that matter

- **Done but not asked for.** The Gemini `setup` fix. The `sync` note for old instruction files, which is the "fw sync handling" the brief asked for, done as a notice because sync never edits a project's own files.
- **Asked for but not done.** No hook change, because the adapters are protected (see above). No folder moves, on purpose. No skill: the roles and templates cover the work.
- **Wrong in the brief.** "Wake timers" are not in the health app's sources. The watchdog appears there only as the thing that failed. The page says what the sources support and marks runtime timers NOT ESTABLISHED. The brief also says "Codex for mechanical work"; the page says "a second vendor's coding agent", to stay generic.

### Limits

- The pitfall sources are public and cited from memory. Two were corrected after the review. None was checked against the book itself.
- The operations pack has not been used in a real project yet.
- The routing score after the `route.md` change is NOT ESTABLISHED.

### Progress notes

- 2026-11-22, start. The gate was red on `work-paired` only (three open briefs). The director then raised `open_briefs` to 5 and dropped 0033.
- Plan sent to the director and approved: a new pack, a map, no folder moves.
- Built Part 2's fix and pointers first, then Part 1 from the researcher's notes, then the map.
- Gate green and 578 tests passing, then a review, fixes, and green again.
