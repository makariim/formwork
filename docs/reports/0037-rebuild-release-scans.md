# 0037 Rebuild the release scans: scans clean, release ready, git steps are yours

## For you

Nothing is published yet. Everything up to the first git command is done and checked. The git commands are yours: the version control guard refused them, as it should.

The two scans are rebuilt and live in the tools folder inside your formwork state folder, beside their private lists. On the first run both were red. The names were in old research, rounds, ideas, briefs and reports, and in the licence and the package author line, and all of those files were already public. You then ruled that the names must not be in formwork's public release or its core. So I scrubbed 23 tracked files. The two private apps became "the health app" and "the desktop app". Your name became "the maintainer" in prose. The licence and the package author now say makariim. Nothing is allow listed for those words.

The overlap scan now ignores any run that was already in the 1.0.1 package. That is kit text that travelled out to your projects. I judged everything that was left. About twenty quotes from the private projects' briefs, spec and standing pages were real private content, all in the old product round file and one line of the architect file. I paraphrased them so they keep their meaning. The rest was generic kit text: gate output, report template headings, kit file lists, public citations, config headers, and one private folder that only holds patches of formwork itself. Each of those has an allow entry with a reason. Both scans are now clean, with the new 1.1.0 packages included.

Then your second ruling: rewrite the history and yank the old releases. You confirmed it to me directly. Here is what I did that touches no git. A backup bundle of the whole repository sits in your formwork state folder, and git says it is complete. I installed git-filter-repo. I bumped the version to 1.1.0, dated the changelog, built both packages and checked them. The package counts are all above zero, nothing private travelled, and a fresh trial install passed the gate and all 578 tests.

The rewrite rules, the mailmap, a history checker and one script are in a rewrite folder inside the tools folder. The script makes the two commits as makariim with the GitHub noreply address, so no new commit carries your private email. It rewrites every commit, message, tag and identity, and checks history with the checker. It checks that the tree at HEAD did not change, then runs the gate and the tests. Then it force pushes main and all tags, tags 1.1.0, uploads to PyPI, creates the GitHub release and installs 1.1.0 back from PyPI. A dry run of the rules over the full history text came out clean. The checker is red on today's history, which shows that it works. The script also sets this repository's commit name and email to makariim, so later commits do not leak either.

Three things stay true after it runs. GitHub may keep the old commits reachable by direct link until its own cleanup. A fork made before the push keeps the old history. PyPI cannot delete or replace 1.0.0 and 1.0.1. Yanking them hides them from new installs only, and needs the PyPI website. The GitHub release for 1.0.1 has no names in its notes, and no 1.0.0 release exists.

What I need from you: run the script, then yank the two old versions on the PyPI website. After that, a short session updates standing and closes 0036 and 0037 from the script's log.

## Accepted

## For the director

### What changed

- 23 tracked files scrubbed (names replaced; quoted private text in `docs/rounds/whole-project-builds/product.md` and `architect.md` paraphrased). `LICENSE` and `pyproject.toml` author is now makariim.
- `pyproject.toml` version 1.1.0; `CHANGELOG.md` Unreleased became `1.1.0 (2026-11-22)`.
- `docs/briefs/0037-rebuild-release-scans.md`: both rulings recorded. `docs/reports/0036-release-1-1-0.md`: one pointer line.
- Outside the repository, `~/.formwork/tools/`: `privacy_scan.py`, `overlap_scan.py` (with the 1.0.1 baseline in `baseline/` and `overlap-allow.txt`, 31 entries), `published.py`, `test_scans.py`, the lists, and `rewrite/` (`replacements.txt`, `mailmap`, `history_check.py`, `run.sh`, a venv with twine). Backup `~/.formwork/backup-pre-rewrite-2026-11-22.bundle`. Homebrew `git-filter-repo` 2.47.0.

### What was run

- `python3 ~/.formwork/tools/test_scans.py`: "7 of 7 passed".
- `python3 ~/.formwork/tools/privacy_scan.py .`: "clean. 1596 files examined, 18 entries, 1 allowed" (with dist).
- `python3 ~/.formwork/tools/overlap_scan.py .`: "clean. 1596 published, 14856 source files examined, n=12, 462 baseline files and 31 allow entries subtracted".
- `git bundle verify ...bundle`: "The bundle records a complete history."
- `python -m build` and `twine check dist/*`: both PASSED. Counts: wheel guard 6, checks 19, roles 30, skills 6; sdist guard 8, roles 56; private travelled 0. RELEASING.md still says 13 checks, 4 skills, 41 sdist roles: stale, not zero.
- Trial install in a fresh venv with a fresh `FORMWORK_STATE_DIR`: `formwork-kit 1.1.0`, gate green 19 checks, "578 tests, all passed".
- `formwork/fw check`: green, 19 checks. `formwork/fw test`: "578 tests, all passed". `formwork/fw demo`: every check rejected its broken input.
- `python3 ~/.formwork/tools/rewrite/history_check.py .` today: RED (account handle 110, login 78, person name 64 lines). The rules dry run over `git log --all -p` text: clean.
- Refused by the git-boundary guard: `git filter-repo`. Not attempted: commit, tag, push, upload, release.

### For him to run

`bash ~/.formwork/tools/rewrite/run.sh` (or stage by stage: `commit`, `rewrite`, `verify`, `push`, `release`). Each run is logged under `~/.formwork/tools/rewrite/logs/`. Then on pypi.org, under Your projects, formwork-kit, Manage, Releases: open 1.0.0, Options, Yank, give a reason, confirm; same for 1.0.1.

### The check

`formwork/fw check` after writing this report: "GATE: green. 19 check(s), each shown to reject the wrong and accept the right."

### Git status

Before the run there were three untracked files; after it, 25 tracked files were modified and four new files (the 0036 and 0037 briefs and reports) were left untracked, with nothing committed.

### The three that matter

- **Done but not asked for**: the script sets this repository's git identity to makariim. Old commits keep the paraphrase only at HEAD; history keeps the old quotes with names replaced.
- **Asked for but not done**: every git step, the upload, the release and the yank. The guard refused git, and the yank needs the website.
- **Wrong in the brief**: RELEASING.md's expected package counts are out of date.
