---
date: 2026-11-15
by: a research session, from his words of 2026-11-15 ("do the gap check")
source: github.com/affaan-m/ecc, default branch HEAD, MIT licence. Ideas only, no text copied
follows: docs/research/ecc-ideas.md (its verdicts stand; this page goes item by item)
---

# ECC gap check: every agent, skill and hook against formwork

1. ECC has 412 items: 71 agents, 314 skills, 27 hook entries. Every one was read by name and one line purpose.
2. 359 of the 385 agents and skills are already covered by a formwork role's `owns`, a kit template, check or guard, or are out of scope (71 are domain or personal tools). All 27 hooks are covered or were already judged in `ecc-ideas.md`.
3. 26 items point at five real gaps. Two are worth a brief now, one is small, two are leave.
4. **Take: a way to bring in a third party skill.** Two of his projects copied the same 15 skills by hand, with no licence file and no record of where they came from.
5. **Take: two report lines for a split build.** "Touched outside my files" and "packages added, with licence". One project wrote both by hand in its team rules.
6. **Adapt, small: nobody owns localisation and right to left layout.** One project has it as a hard rule; no role's `owns` names it.
7. **Leave: writes outside the repository and destructive commands.** No kit guard; ECC's own answer is advice only. One line in `limits.md`.
8. **Leave: scanning a project before it goes public.** `kit-leak-scan` reads kit files only. No project has needed it yet.
9. No new kit role is needed. No new hook is needed. Nothing here is a taste check, a hidden model call or a network need.
10. Contradiction: the job asks for 314 skills "by name"; 71 of them are vertical tools (logistics, crypto, homelab, video, social) that formwork would never own, so they were sorted, not weighed one by one.

---

## The real gaps

| # | Gap | ECC items it comes from | Evidence it matters | Form in formwork | Cost | Verdict |
|---|---|---|---|---|---|---|
| 1 | **Bringing in a third party skill.** The kit has one vendored skill done properly (`formwork/skills/humanizer/UPSTREAM.md`: repository, commit, licence, sha256, "nothing updates on its own"). It has no page for a project that needs stack or craft knowledge from outside. Projects copy folders by hand | `skills/repo-scan` (installs an external skill from a pinned, reviewable commit), `skills/skill-scout` (look for an existing skill before writing one). The stack depth his projects reached for has ECC counterparts: `skills/swiftui-patterns`, `skills/swift-concurrency-6-2`, `skills/swift-actor-persistence`, `skills/swift-protocol-di-testing`, `skills/liquid-glass-design`, `skills/foundation-models-on-device`, `skills/motion-foundations`, `skills/motion-patterns`, `skills/motion-advanced`, `skills/make-interfaces-feel-better`, `skills/frontend-design-direction`, `skills/react-native-patterns` | The desktop-app and health-app repositories each hold the same 15 skills in `.agents/skills/` (9 on motion, plus Swift, design, worst case UI data, a library picker, a prototype picker). The two copies are byte identical. None carries a licence or an upstream record (0 files found). They are wired by hand: briefs and `AGENTS.md` say "read the design skills as files", and no project role names them in `skills:`. The legal pack's own rule applies: "A file with no licence is not free to use" (`formwork/roles/packs/legal.md`) | **Not a catalogue in the kit.** One kit page, "bringing in a skill", that makes the humanizer pattern general: the project keeps the skill in its own folder with an `UPSTREAM.md` (repository, commit, licence, sha256) and the licence file beside it; the human fetches, the kit never does; a role names it in `skills:` so it binds on Claude Code and is read as a file elsewhere. Optionally a check, `skill-provenance`, that fails a project skill folder with no `UPSTREAM.md` or no licence unless it says it was written here, with a breaking fixture | Low to medium. A page, a template, maybe a check | **Take**, one checkpoint brief. The 15 existing copies in his projects are their own job, not this one |
| 2 | **Two report lines a split build needs.** `formwork/roles/method/lead.md` already says "two pieces must not need the same file" and "write down what each piece may not touch", and `formwork/templates/build.md` splits the team by files. But the report a builder returns has no line for files it touched outside its area, and no line for a package it added | `skills/team-agent-orchestration` (work items with owners and scope), `skills/parallel-execution-optimizer` (lane matrix), `skills/search-first` (look before adding), `skills/mcp-dependency-review` (review package references before approval) | health-app's `docs/build/team-rules.md` was written by its lead for parallel builders. Its own final message shape asks for "Touched outside my area" and "Any package or data you added, with its licence and source URL", and its rules forbid adding a package without checking its licence and what it installs. `legal` and `security` own the judgment; nothing makes the builder surface it | Template text. Two lines under "The report must contain" in `formwork/templates/build.md`, owned by `lead` for a split brief: files touched outside the piece's area, each named; packages added, each with licence, what it installs and where it came from | Low | **Take**, one task brief after 0028 lands (0028 owns `build.md` now) |
| 3 | **Localisation and right to left layout.** `writer` owns "every word a person reads"; `visual` mentions "a translated label" once. No `owns` line names words in every language the product ships, or layout that mirrors | `skills/i18n-sync`, `skills/bengali-nlp`, `agents/bengali-reviewer.md` | One of his projects ships in two languages, one right to left, as a numbered hard rule for every builder (strings in both languages through one helper; leading and trailing, never left and right; a digits setting) | Widen `writer`'s owns to the words in every language shipped, and add one line on mirrored layout to `frontend` and `mobile` (or `visual`). A new `localisation` pack role only if a second project needs it, by `formwork/roles/HOW-TO-ADD-A-ROLE.md` | Low | **Adapt**, one task brief. Kit role files, so `protected-files` and `generated-current` apply |
| 4 | **Writes outside the repository, and destructive commands.** `git-boundary` covers git writes and `protected-files` covers kit files. Nothing covers an edit outside the repository root, or `rm -rf`, a forced overwrite, a dropped table | `skills/safety-guard` ("Freeze" locks writes to one folder, "Careful" stops destructive commands). Its own description says "Advisory: the agent applies these rules itself; no hook ships with it" | health-app's team rules forbid touching anything outside the repository by hand (home configs, other repositories, installed apps), and his own instructions say the same. No incident is recorded in either project: NOT ESTABLISHED that it has happened | A guard on file tool paths would be cheap, but shell writes cannot be pattern matched reliably (`formwork/limits.md` already says so for `protected-files`), and the runtimes' own sandboxes and permission prompts cover this in their default modes (not measured here) | Low for one line; medium for a guard | **Leave** as a guard. One line in `formwork/limits.md`: the kit does not guard writes outside the repository or destructive commands; use the runtime's sandbox. Revisit if a report ever records one |
| 5 | **Scanning a project before it becomes public.** `kit-leak-scan` "reads kit files only". The release step template has no line for a repository or artifact that becomes public | `agents/opensource-forker.md`, `agents/opensource-sanitizer.md`, `agents/opensource-packager.md`, `skills/opensource-pipeline` | Weak. `security` owns secrets and `legal` owns personal data, so the work is owned; only the tool is missing. None of his projects has made a repository public yet | When one does: one line in `formwork/templates/release-step.md` (if anything becomes public, `security` reads it for secrets and personal details first), and let `kit-leak-scan`'s patterns run over a named path by hand. No new check in the gate | Low | **Leave** until a project goes public |

What each row keeps from the principles: one loop (all five are template lines, a page or one line; none adds a pipeline); a short named list (gap 1 is a way to bring in a skill, never a shelf of them in the kit); generic kit (no project's words go into the kit, only the shape); taste is never a check (gap 1's check reads provenance, not quality); no hidden model calls; no network (the human fetches).

---

## Appendix: what was already covered

Counted with a script over the names and descriptions (see How this was done). Agents and skills together, 385.

| Count | ECC group | Covered by |
|---|---|---|
| 65 | Language and framework patterns, testing and verification by stack (`*-patterns`, `*-testing`, `*-tdd`, `*-verification`, framework `*-security`) | The working packs (`backend`, `frontend`, `mobile`, `data`, `tester`). Stack depth arrives as a project skill, which is gap 1 |
| 34 | Code review, by language and by dimension (the 17 language reviewers, `code-reviewer`, silent failures, comments, types, simplifying, dead code, change impact, self rating) | `reviewer` (reading the diff), `challenger` (the case against), the review round template. ECC's review then refute idea is `ecc-ideas.md` idea 2 |
| 33 | Planning and pipelines (`planner`, `blueprint`, the six `orch-*`, GAN harness, loop operator, RFC to DAG, story lifecycle, spec mining, brownfield retro) | `director`, `lead`, the one loop, `formwork/route.md`, `templates/spec.md` and `build.md`. GAN scoring is the taste check 0022 refused |
| 27 | Writing, marketing, product, research, decks, video (`seo`, `brand-voice`, `market-research`, `product-lens`, `deep-research`, `frontend-slides`) | `writer`, `marketing`, `product`, `researcher`, `user-researcher`; decks by `writer` with `visual` and the `deck` taste pack. Web search MCP ones are network needs |
| 22 | ECC managing itself (setup wizard, guides, install sorting, skill lint, stocktake, config cleanup, Hookify, instinct learning) | `fw`, `install`, `sync`, `role-shape`, `generated-current`, `kit-integrity`. Instincts: left in `ecc-ideas.md` |
| 12 | Testing (`tdd-guide`, `e2e-runner`, `browser-qa`, `click-path-audit`, `verification-loop`) | `tester`, the review round by journey, the gate. Worst case UI data (which one project fetched as a skill) is in `tester`'s hostile inputs table and `visual`'s "design for content that is too long" |
| 12 | Build failure fixers (11 `*-build-resolver`, introspection debugging) | The "A fix" kind in `formwork/route.md`, done by the session that got it |
| 12 | Measurement, evals, cost (`eval-harness`, `skill-comply`, `cost-tracking`, `context-budget`) | `researcher`, the routing eval; `ecc-ideas.md` ideas 1, 3, 4 and 9 |
| 10 | Architecture (`architect`, ADRs, contracts, codebase onboarding, code tours) | `architect`, decisions, `integrations`. Onboarding is also his own handover skill, outside the kit |
| 10 | Models and AI products (RAG review, prompt caching, MLE workflow) | `ai` |
| 9 | Security (`security-reviewer`, config scan, bounty hunter, GateGuard) | `security`; GateGuard left in `ecc-ideas.md`; hidden unicode is `ecc-ideas.md` idea 6 |
| 8 | Records, memory, docs (`doc-updater`, living docs, session memory, growth log) | `record-keeper`, `docs/standing.md`, `standing-current`, `doc-links`, routing corrections |
| 7 | Databases and migrations | `data` |
| 6 | Second opinions (`council`, `santa-method`, `dev-team`, `team-builder`) | A round through `lead`, with `challenger`. The external model loop needs the network |
| 6 | Performance and operations (`performance-optimizer`, `canary-watch`, dashboards) | `performance`, `sre` |
| 6 | Deployment (`docker-patterns`, `kubernetes-patterns`, `github-ops`) | `devops` |
| 6 | Accessibility and design systems | `accessibility`, `visual`. Motion is `visual` section 7 plus `accessibility`'s reduced motion; its craft depth is gap 1 |
| 3 | Commit messages and git workflow | `git-boundary`; the human commits |
| 71 | Vertical or personal tools (logistics, energy, customs, healthcare, homelab and network, crypto and markets, scientific databases, video taste, social, mail and messages, hosted services) | Out of scope for a generic kit. A project that needs one writes a project role (health-app did, four of them) |
| **359** | **covered or out of scope** | |
| 26 | gaps 1 to 5 above (14, 4, 3, 1, 4) | |

The 27 hooks:

| Count | Hooks (ids from `hooks/hooks.metadata.json`) | Covered by |
|---|---|---|
| 1 | `pre:bash:dispatcher` (no `--no-verify`, commit quality, push reminder, dev server in tmux, GateGuard) | `git-boundary` refuses git writes outright; the rest is left in `ecc-ideas.md` |
| 2 | `pre:powershell:gateguard-fact-force`, `pre:edit-write:gateguard-fact-force` | Left in `ecc-ideas.md` (its own study: about 45% more cost, no gain) |
| 1 | `pre:config-protection` | `ecc-ideas.md` idea 8, adapt later |
| 3 | `pre:hookify-runtime`, `prompt:hookify-runtime`, `stop:hookify-runtime` | The three guards and `[strength]`; left in `ecc-ideas.md` |
| 2 | `stop:format-typecheck`, `stop:check-console-log` | `quality-gate` runs the project's own aggregate |
| 2 | `post:dispatcher:sync`, `post:dispatcher:async` | Their parts (quality, design hints, context and cost warnings, logging) judged in `ecc-ideas.md` |
| 4 | `pre:compact`, `session:start`, `stop:session-end`, `session:end:marker` | `docs/standing.md`; the hidden summary call is left |
| 4 | `pre:observe:continuous-learning`, `stop:evaluate-session`, `pre:governance-capture`, `post:skill:track` | Left: inferred learning and telemetry |
| 1 | `stop:cost-tracker` | `ecc-ideas.md` idea 3, run by hand |
| 2 | `pre:mcp-health-check`, `post:mcp-health-check` | Network services; out |
| 2 | `session-start:plan-canvas-sessions`, `stop:plan-canvas-pending` | A local browser canvas; out. The design round's sample stop does the picking |
| 2 | `pre:edit-write:suggest-compact`, `stop:desktop-notify` | Runtime conveniences, not the kit's job |
| 1 | `pre:write:doc-file-warning` | `record-keeper`, `doc-links` |

---

## How this was done

All reading. Nothing from the copy was run, installed or sourced.

```
curl -sSL -o ecc.tar.gz https://codeload.github.com/affaan-m/ecc/tar.gz/HEAD
tar -xzf ecc.tar.gz -C src
ls agents | wc -l                                  -> 71
ls skills | wc -l                                  -> 314
python3 -I list.py <copy> inv.txt (hooks/hooks.json entries)   -> 27
python3 -I group.py inv.txt                        -> 385 of 385 agents and skills assigned, 0 unassigned
```

The two scripts lived outside the copy and read it by path. Hook names came from `hooks/hooks.metadata.json`, because `hooks.json` routes every hook through one bootstrap file.

His projects, read only, method only:

```
ls -d desktop-app/.agents/skills/*/ | wc -l             -> 15
ls -d health-app/.agents/skills/*/ | wc -l             -> 15
diff -rq desktop-app/.agents/skills health-app/.agents/skills   -> no difference
find both skill folders -iname 'licen*' -o -iname 'upstream*' | wc -l   -> 0
```

Kit files read: `docs/research/ecc-ideas.md`, `formwork/route.md`, the `owns` line and Owns sentence of all 28 roles, `formwork/skills/humanizer/`, the three guards, the 16 checks by name, `formwork/templates/build.md`, `report.md`, `release-step.md`, `design-round.md`, `formwork/roles/packs/visual.md`, `tester.md`, `legal.md`, `security.md`, `formwork/roles/method/lead.md`. No kit file, brief or standing was changed. The downloaded copy was deleted at the end.

## NOT ESTABLISHED

- That any of the five gaps has caused a failure. The evidence is rules and copies written by hand, not incidents.
- Whether the 15 hand copied skills are licensed for the use made of them. No licence file was found; their upstream was not looked up.
- That the runtimes' sandboxes stop writes outside the repository in every mode he uses (gap 4).
- The full text of every ECC item. Each was judged on its name and its one line description; the candidates for a gap were read further.
