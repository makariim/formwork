---
brief: 0028
date: 2026-11-15
---

# 0028 Optional templates and gates

## For you

Step 6 of the research is in. Six optional one page templates now sit in `formwork/templates/`: spec, research lane, design round, build, review round and release step. The release step is the general pattern only.
A phase is just a `stream:` label on ordinary briefs. There is no new process and no fixed order. Two phases can run side by side.
A brief can carry one gate: `starts: now`, `starts: after <stream>` or `starts: decision NNNN`. A new check, `gates`, refuses an open brief whose gate is not met, and refuses any gate written in prose.
The two default build gates are in the spec and build templates. Example: a build brief with `starts: after spec` stays red until the spec report has your read-back.
`route.md` now has a table that offers the matching template by kind and size. It says plainly that the templates are not a sequence.
No guard refused anything. Tests: 557 passed. The gate is red on `kit-integrity` only, because the new check file was added. Re-record fingerprints after you review it.
The brief stays `open` until you write the read-back.

## For the director

### Contradictions

- His global instructions say to set the brief to `status: done`. `work-paired` refuses done without the read-back, so the brief is left `open`, as with 0027.
- The research says the build's second gate is "unproven items listed and seen". No program can see "seen". So I built it from the three forms only: the build report lists the items under "Not proven", the read-back on that report counts as "seen", and the next brief carries `starts: after build`. The check does not look for the heading. Adding that would be a fourth form, and the brief says three only.

### Choices made

- `gates` is a new check, not part of `work-paired`. `work-paired` is protected and the guard would refuse an edit to it. A separate check also keeps one job per check. It loads `work-paired` as a module (`SourceFileLoader`, with bytecode writing off so no `__pycache__` appears in the protected folder). That way the stream, status and read-back parsing is not copied a second time.
- `starts: after <stream>` is met when every other brief in that stream is done with its read-back or dropped, and at least one is done. A stream that no brief names, or one where every brief was dropped, counts as not met. A brief that waits on its own stream is refused.
- Only `starts:` lines in the frontmatter count, so a quoted example in the body is not read as a gate. Only open briefs are read, so a closed one with an old gate is history.
- More than one `starts:` line on a brief is refused: one gate per brief.
- The check was drafted and tested in the job's scratch folder first. It was then copied into `formwork/check/checks/` while that path did not exist yet, because the guard would block any fix after that.

### What changed

- `formwork/check/checks/gates` (new): the gate check.
- `formwork/check/fixtures/gates/` (new). Seven must-pass cases: `no-gate-is-no-gate`, `starts-now`, `build-after-an-accepted-spec`, `a-dropped-brief-does-not-hold-the-gate`, `after-a-decision-that-exists` (`0003` and `3`), `two-streams-side-by-side`, `closed-briefs-are-history`. Eight must-fail cases, one problem each: `build-before-the-spec-is-accepted` (no read-back), `after-a-stream-still-open`, `after-a-stream-nobody-named`, `after-a-stream-all-dropped`, `a-decision-not-written`, `a-gate-in-prose`, `waits-on-its-own-stream`, `two-gates-on-one-brief`.
- `formwork/templates/{spec,research-lane,design-round,build,review-round,release-step}.md` (new): one page each. Headings follow the research's template table. They name no machine, account, person or product.
- `formwork/loop.md`: new section "Phases and gates": the three forms, the two default gates, links to the six templates.
- `formwork/route.md`: a "Templates for a phase" table, by kind and size, offered and never required.
- `formwork/templates/brief.md`: the optional `stream:` and `starts:` lines.
- `FORMWORK.md`: a row in the rules table for `gates`.
- `formwork/glossary.md`: Phase and Gate entries; fifteen checks to sixteen.
- `README.md`: sixteen checks; the templates row lists the optional ones.
- `formwork/limits.md`: what `gates` cannot tell.
- `CHANGELOG.md`: one Unreleased entry.

### What was run

| Command | Result |
|---|---|
| draft `gates` over each of the 15 fixture cases | 7 must-pass exit 0, 8 must-fail exit 1, each with its own single message |
| `formwork/check/checks/gates .` | "no open brief carries a gate", exit 0 |
| `formwork/fw check` (first, after adding the check) | red on `kit-integrity` only: "added formwork/check/checks/gates". `gates` ok |
| `formwork/fw test` | "557 tests, all passed" |
| `formwork/fw check` (last) | "GATE: red. 1 check(s) failed on the project, 0 input(s) wrongly accepted, 0 wrongly rejected." Only `kit-integrity`. `gates`, `doc-links`, `kit-leak-scan`, `roles-named`, `work-paired` all ok |
| grep for em and en dashes in the new files and in `git diff` added lines | none |

### Not done

- Fingerprints: his to re-record after review.
- Brief left `open` until the read-back.
- No other repository touched. No git writes.

### git status

```
 M CHANGELOG.md
 M FORMWORK.md
 M README.md
 M docs/briefs/0027-roles.md
 M docs/reports/0027-roles.md
 M docs/standing.md
 M formwork/glossary.md
 M formwork/limits.md
 M formwork/loop.md
 M formwork/route.md
 M formwork/templates/brief.md
?? docs/briefs/0028-templates-and-gates.md
?? docs/reports/0028-templates-and-gates.md
?? formwork/check/checks/gates
?? formwork/check/fixtures/gates/
?? formwork/templates/build.md
?? formwork/templates/design-round.md
?? formwork/templates/release-step.md
?? formwork/templates/research-lane.md
?? formwork/templates/review-round.md
?? formwork/templates/spec.md
```

The 0027 brief and report changes, the `docs/standing.md` changes and the 0028 brief were already in the tree before this session. I did not touch them.

accepted: 2026-11-15
in my words: c, go, he re-recorded the fingerprints and committed 4d9f211
