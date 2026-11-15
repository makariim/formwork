---
brief: 0030
date: 2026-11-15
---

# 0030 Close two guard holes

## For you

The guard was still on block in this session, so it refused my edits to the guard and the check. Your "warn for 0030" never reached the hook. I stopped editing those files and staged the changes as a patch instead: `docs/reports/0030-guard-holes.patch`.
The patch does three things. The guard now follows a symbolic link (to a file or to a folder) and refuses when it lands on a protected file. It also refuses a file whose hard link is a protected file. Fourteen new tests cover this. In `hidden-unicode`, a run of tag characters is now one hit, not one per letter.
With the patch applied in a copy, all 571 tests pass. In the real repo, without the patch, 557 pass. The gate is red only because `hidden-unicode` is new and not yet recorded.
The docs are done in place: limits, COSTS, glossary, the FORMWORK.md table, and the README counts (17 checks, 571 tests).
Your steps: review and apply the patch, then re-record the fingerprints. The brief stays `open` until your read-back.

## For the director

### Contradictions

- He said the guard was on warn for this brief. In this session it was on block. `.formwork.toml` says `protect_files = "block"`, and `FORMWORK_PROTECT_FILES` was not set in the hook's environment. The first edit to `formwork/check/checks/hidden-unicode` was refused. The brief says to stop and give him the exact change, so every protected-file change is in the patch. None is in the tree.
- His global instructions say to set the brief to `status: done`. `work-paired` refuses done without the read-back, so the brief stays `open`, as with 0027 to 0029.
- The git boundary refuses `git apply --check`, though that command writes nothing. I checked the patch with `patch -p1 --dry-run` on the real tree instead. I applied it for real only in scratch copies under the job's tmp folder.

### Protected files changed (all in the patch, none in the tree)

| file | change |
|---|---|
| `formwork/guard/protected-files` | `is_protected` now calls `named_protected` (the old body, renamed and unchanged), then `linked_protected`. That function follows symbolic links with `realpath`, and compares a regular file that has two or more links by `(st_dev, st_ino)` against every protected file. `protected_files()` lists those files: the project entries, the home word lists and record, and the state dir. Globs and paths that do not exist yet behave as before. |
| `formwork/guard/test_protection.py` | New section `LINKS`, 14 cases in a temp project. Refused: a symbolic link to a guard, a hard link to a guard, a guard reached through a linked folder (relative and absolute each), `echo x >` through a symbolic link, `sed -i` on a hard link, and warn on warn. Allowed: an ordinary file, hard links between ordinary files, a symbolic link to an ordinary file, a new file in a linked guard folder, and `cat` through a symbolic link. |
| `formwork/check/checks/hidden-unicode` | `hits_in` folds consecutive tag characters on one line into one hit named `run of N tag characters`, at the first one's column. The docstring says so. |

The new check and its fixtures (`formwork/check/checks/hidden-unicode`, `formwork/check/fixtures/hidden-unicode/`) were made earlier in this brief. They are also protected and still need recording.

### Not protected, changed in place

- `formwork/limits.md`: the link hole moves from open to closed, and the cost is named (deleting a link to a guard is refused too). A new paragraph for `hidden-unicode` says what it cannot tell.
- `formwork/COSTS.md`: the gate timing was measured again (17.57, 7.08, 13.62 s; seventeen checks), and the file count is now 409.
- `formwork/glossary.md`: "sixteen" becomes "seventeen". New entries for **Link** and **Hidden character**. Self-protection now says a link counts as the file.
- `FORMWORK.md`: a table row for `hidden-unicode`.
- `README.md`: "sixteen" becomes "seventeen" checks, 15 becomes 17 checks, and 494 becomes 571 tests. 571 holds once the patch is in. Without it, the count is 557.
- `docs/reports/0030-guard-holes.patch`: new. The patch to review.

### What was run

Copies were made with `cp -R . <job tmp>/copy` and `<job tmp>/copy2`. The patch was applied only in `copy2`. Nothing wrote outside the repo except those copies.

```
$ CLAUDE_PROJECT_DIR=<copy2> formwork/fw test          # patch applied
571 tests, all passed
$ formwork/fw test                                      # real repo, no patch
557 tests, all passed
$ FORMWORK_EXCLUDE=formwork/check/fixtures python3 formwork/check/checks/hidden-unicode .   # copy2
195 kit file(s) read, no hidden characters
$ python3 <staged>/hidden-unicode formwork/check/fixtures/hidden-unicode/must-fail/tag-characters
  FORMWORK.md:3:30  U+E0073 run of 13 tag characters     (exit 1; the other 4 must-fail exit 1, all 4 must-pass exit 0)
$ patch -p1 --dry-run < docs/reports/0030-guard-holes.patch
patching file 'formwork/guard/protected-files' (and the other two)
$ /usr/bin/time -p formwork/fw check    # x3, real repo
real 17.57 / 7.08 / 13.62
$ find formwork -type f -not -path '*/__pycache__/*' | wc -l
409
```

### The check

The gate is **red**, and only on `kit-integrity`:

```
FAIL  kit-integrity
      1 protected file(s) differ from the record
        added    formwork/check/checks/hidden-unicode
GATE: red. 1 check(s) failed on the project, 0 input(s) wrongly accepted, 0 wrongly rejected.
```

The other 16 checks are ok, including `hidden-unicode`. After the patch is applied, `kit-integrity` will also list the guard, its test and the changed check. Re-recording is his step.

### The three that matter

- **Done but not asked for:** none beyond the patch file, which is how the brief says to hand over a refused change.
- **Asked for but not done:** step 1 and the tag-run tidy are not in the tree, because the guard refused them. They are in the patch. Fingerprints were not re-recorded, as asked.
- **Wrong in the brief:** the warn setting did not exist in this session (see Contradictions). Also, `ln` was already refused when its target is protected. The hole was a link that already existed, or one made some other way.

### Known costs of the fix

- Removing a symbolic link to a guard (`rm docs/soft.md`) is refused, though it leaves the guard in place. Kept, because `shred` and `truncate` go through the link and do harm.
- A hard-link check walks every protected file. It only runs when the target has two or more links, which ordinary files rarely do.

### Apply, after review

```
patch -p1 < docs/reports/0030-guard-holes.patch
formwork/fw test
formwork/fw record
```

accepted: 2026-11-15
in my words: done, he applied the guard patch himself, re-recorded and committed f82feb0
