---
brief: 0037
stream: release
title: Rebuild the two release scans, then finish release 1.1.0
status: open, 2026-11-22
starts: now
size: task
---

# 0037 Rebuild the two release scans

## His words (2026-11-22)

0036 stopped because the two scan tools RELEASING.md names were missing from this Mac. Asked whether to copy them from elsewhere or rebuild them, he said: "rebuild the scans". His permission for 0036 ("no, let a brief do everything") still holds for the release itself.

## What to build (outside the repository, in ~/.formwork/tools/)

1. `privacy_scan.py .`: walks the files that would be published (git tracked files plus the built wheel and sdist when present) and fails on any word or pattern from a private list kept next to it (`~/.formwork/tools/private-words.txt`, one entry per line, case insensitive, `#` comments). Prints file, line and the entry matched. Exit 0 only when clean. An allow list file next to it for known safe lines (for example the public clone URL), each entry with a reason.
2. `overlap_scan.py .`: fails when a long run of text (default 12 or more words in a row, ignoring whitespace and case) in a published file also appears in a private source folder listed in `~/.formwork/tools/private-sources.txt`. Prints both places. Same exit rule.
3. Self tests for both: a pretend repository with one planted private word and one copied paragraph must fail; a clean one must pass. Run them.

The word list and source list are never committed here, and never quoted in this repository, its report or its commit messages: the report gives counts and categories only.

## Then

Run both scans. If clean, continue brief 0036 from step 3 to the end exactly as written, and close both briefs. If either scan finds hits, stop before any version bump or upload, and report the hits (file and line, the entry shown as a category, never the word) to the Director. Do not rewrite git history.

**Rules:** foreground commands only, no wait loops, every command under a timeout. Report `docs/reports/0037-rebuild-release-scans.md` with "For you" first. SendMessage the session named Director at the end or at any stop.

## His ruling on the red scans (2026-11-22, relayed by the director)

"no, i dont want these names to be in formwork's public release, or formwork core even". So: scrub every privacy hit from every tracked file, using neutral words that keep the sense. The author becomes the public GitHub owner name in LICENSE and pyproject. No allow list entries for those words. The overlap scan ignores runs that are also in the 1.0.1 sdist; judge every run that is left. Then rerun both scans until they are clean and continue 0036 from step 3. Do not rewrite git history and do not yank 1.0.1.

## His second ruling (2026-11-22, relayed by the director, then confirmed by him in the working session)

"do both": rewrite formwork's git history to remove the names (backup bundle first, outside the repository), force push main and all tags, release 1.1.0 on the rewritten history, and yank 1.0.0 and 1.0.1 on PyPI.
