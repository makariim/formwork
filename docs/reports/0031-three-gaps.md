---
brief: 0031
date: 2026-11-15
---

# 0031 Three gaps from the catalogue check

## For you

All three gaps are closed in the tree. The gate is green (17 checks) and all 571 tests pass.
Gap 1: a new page, `formwork/bring-a-skill.md`, and a template, `formwork/templates/upstream.md`. A project keeps the skill in `.claude/skills/<name>/`, not under `formwork/`, because `formwork sync` would delete it there.
Gap 2: the build template and `lead` now ask every builder for "touched outside my files" and "packages added", with licence and source.
Gap 3: `writer` owns words in every language. `visual` owns how a layout mirrors. `frontend` and `mobile` build it. No new role.
The optional check `skill-provenance` is in `docs/reports/0031-three-gaps.patch`, because the guard refused its folder. Apply it, `chmod +x` the check, then re-record. The brief stays `open` until you write your read-back.

## For the director

### Contradictions

- His global instructions say to set the brief to `status: done`. `work-paired` refuses done without his read-back, so the brief stays `open`, as with 0027 to 0030.
- The research suggested a project keep a third party skill "in its own folder". The only place the kit composes skills from is `formwork/skills/`, and `formwork/sync` deletes every file under `formwork/` that the kit does not ship, apart from the project's own roles folder and its pin file (the `HUB_ONLY` list in `formwork/sync`). So the page puts a project's skill in `.claude/skills/<name>/`. That is where Claude Code reads it, and `formwork roles` never overwrites a file it did not make.
- The guard refused `kit-integrity --record` in a scratch copy, even with `FORMWORK_STATE_DIR` set to the job's tmp folder. So in the copy, the gate was run one check at a time, with `kit-integrity` left out. Everything else was run in full.

### Changed in place (not protected)

| file | change |
|---|---|
| `formwork/bring-a-skill.md` | new. Before you bring a skill in (look for a role first, licence or nothing, read all of it). Where it lives. Who names it in `skills:`. The record. Nothing updates on its own (six steps, as in humanizer's). What it does not do. |
| `formwork/templates/upstream.md` | new. The humanizer record made general, plus the one line for a skill written in the project: `written here, no upstream`. |
| `formwork/templates/build.md` | two lines under "The report must contain": **Touched outside my files** and **Packages added** (licence, what it installs, where it came from), each "or none". Then a short paragraph on why they matter in a split build. |
| `formwork/roles/method/lead.md` | under "Collect, then report once": ask each piece for the same two lines in its final message, and say so in its brief. A piece without them goes back. |
| `formwork/roles/packs/writer.md` | Owns: "in every language the product ships". Does not own: how a layout mirrors (`visual` decides, `frontend` or `mobile` builds). |
| `formwork/roles/packs/visual.md` | Owns: how the layout mirrors for a right to left language. Does not own: the words in each language (`writer`). |
| `formwork/roles/packs/frontend.md`, `mobile.md` | Owns: building the mirrored layout, "leading and trailing, never left and right". Does not own: the words in each language (`writer`). |
| generated agents | `.claude/`, `.codex/`, `.gemini/` copies of those five roles, rebuilt with `formwork/build --all`. |
| `formwork/limits.md` | a paragraph on what `skill-provenance` cannot tell. |
| `formwork/glossary.md` | new entry **Upstream record**. |
| `README.md` | the templates row names the upstream record; a row for `bring-a-skill.md`. |
| `formwork/COSTS.md` | kit file count 409 becomes 433. That is measured with the patch applied (411 without it). The gate timing line still says seventeen checks, because that is what was timed. |
| `CHANGELOG.md` | three entries under Unreleased. |
| `docs/standing.md` | one paragraph under "Where we are now". |

The `owns:` slugs did not change, so `role-shape` and routing are untouched.

### In the patch (`docs/reports/0031-three-gaps.patch`)

| file | change |
|---|---|
| the check `skill-provenance` (in `checks/`) | new check. It reads every folder with a `SKILL.md` in `formwork/skills/` and `.claude/skills/`, and skips any folder whose `SKILL.md` carries the `GENERATED FROM` banner. Every other folder needs an `UPSTREAM.md`. That file either starts with `written here, no upstream`, or names a 40 character commit, has a licence file beside it, and gives a sha256 for `SKILL.md` and the licence that matches the file on disk. |
| its fixtures (in `fixtures/skill-provenance`) | 5 must-fail (a branch instead of a commit, copied by hand with no record, edited after recording, a kit skill with no record, no licence). 4 must-pass (a traced project skill, written here, a kit skill and its generated copy, no skills). |
| `FORMWORK.md` | a table row for the check. Kept in the patch because `doc-links` fails a link to a file that does not exist yet. |
| `README.md`, `formwork/glossary.md` | seventeen becomes eighteen checks. In the patch so the tree's counts stay true until it is applied. |

`patch` and `diff` do not carry the executable bit. After applying, run `chmod +x formwork/check/checks/skill-provenance`, or the gate lists it as unable to run.

### What was run

Copies were made with `cp -R . <job tmp>/copy`, `copy2` and `copy3`. The patch was applied only in those copies.

```
$ formwork/build --all                                   # real repo
86 generated file(s) considered (84 role, 2 skill), 10 written, for: claude-code, codex, gemini-cli
$ formwork/fw roles                                      # real repo, final
30 generated file(s) considered (28 role, 2 skill), 0 written, for: claude-code
$ formwork/fw check                                      # real repo, final
GATE: green. 17 check(s), each shown to reject the wrong and accept the right.
$ formwork/fw test                                       # real repo, final
571 tests, all passed
$ patch -p1 --dry-run < docs/reports/0031-three-gaps.patch   # real repo
patching file 'formwork/check/checks/skill-provenance' (and FORMWORK.md, README.md, formwork/glossary.md, the fixtures)
# copy3: patch -p1 applied, chmod +x, FORMWORK_EXCLUDE=formwork/check/fixtures
$ for c in formwork/check/checks/*; do ... done            # every check except kit-integrity
(no FAIL lines: all 17 exit 0, skill-provenance among them)
$ CLAUDE_PROJECT_DIR=<copy3> formwork/fw test
571 tests, all passed
# copy2: each fixture case
$ formwork/check/checks/skill-provenance <case>
exit 1 on all 5 must-fail, exit 0 on all 4 must-pass
$ formwork/check/checks/skill-provenance .               # copy2, the kit itself
2 skill folder(s) read, each generated, written here, or traced to a commit with its licence and matching sha256
$ find formwork -type f -not -path '*/__pycache__/*' | wc -l
411 (real repo), 433 (copy2, patch applied)
```

The two skill folders in the kit are `formwork/skills/humanizer` (traced, and its sha256 lines match) and `.claude/skills/humanizer` (generated, skipped). The test count does not change, because the gate runs the fixtures, not the test suites.

The guard refused one thing during the work: `kit-integrity --record` in the copy. Nothing protected was changed in the real tree. No other repository was touched. No git writes.

### Your steps

```
patch -p1 < docs/reports/0031-three-gaps.patch
chmod +x formwork/check/checks/skill-provenance
formwork/fw check
formwork/fw record
```

`formwork/fw check` goes red on `kit-integrity` until `formwork/fw record` has run.

### NOT ESTABLISHED

- Where Codex, Gemini CLI or Cursor read a project's skills from. The page says so and tells the role to read the file by path.
- The gate timing with eighteen checks. It was not measured. The COSTS line still gives the seventeen check numbers.
- Whether the fifteen skills copied by hand in his two projects are licensed. That is its own job, as the research says.
