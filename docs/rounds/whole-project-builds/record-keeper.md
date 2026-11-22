---
role: record-keeper
round: whole-project-builds
brief: 0022
date: 2026-11-15
---

# Record keeper: checks, gates and records for a project layer

## Contradictions first

1. **This round folder turns the gate red, and nothing in the round says so.**
   `standing-current` walks every file under `docs/rounds/`. A file with no
   date line fails ("no readable date"). A file with a date newer than the
   standing brief's `updated:` line also fails. The standing brief says
   `updated: 2026-10-25`. So every participant file fails one way or the
   other. I dated mine, because the date is true. The fix is the standing
   brief's `updated:` line, which belongs to whoever keeps `docs/standing.md`
   (the director). The round template carries a date line, but only for the
   round record. Participants are never told.
   Commands: `formwork/check/checks/standing-current .` (2 problems now:
   `brief.md` and `predictions.md` have no readable date), and a throwaway
   copy with one dated round file, which failed with "The standing brief says
   2026-10-25, so it does not know about this one".
2. **The gate cannot run on this machine at all.** `formwork/fw check` exits 2.
   `kit-integrity` has no fingerprints recorded here, so the gate stops at pass
   one. Recording them is the human's call, per the check's own text. Every
   "green" below is from a single check run alone, not from the gate.
3. **The briefing's principle and the kit disagree in a small way.** The brief
   says a check that examines nothing must not report clean. The gate obeys
   that (no checks at all is status 2). Individual checks do not. They treat
   "no folder" as "nothing claimed", exit 0, on purpose. Two report clean over
   zero subjects even with the folder present:
   - `formwork/check/checks/predictions-first .` printed "0 round(s) checked,
     each with predictions on record", exit 0.
   - Over the health app, `standing-current` printed "ahead of all 0 record(s)", exit 0,
     while the health app's standing brief still says what is next is "His review of
     the spec. Then brief 0001", and briefs 0001 to 0003 are done.
   Neither is a bug by the kit's own rules. Both matter for a project layer:
   a project is exactly the place where "nothing claimed" stops being true.
4. **The desktop app does not have 310 reports.** It has 198 report files and 112
   attachment folders beside them (`NNNN-files`, `NNNN-shots`). The 310 is a
   folder listing. Commands, in the desktop app: `ls docs/reports | wc -l` (310),
   `ls docs/reports | grep -c '\.md$'` (198),
   `find docs/reports -mindepth 1 -maxdepth 1 -type d | wc -l` (112). Six
   briefs have no report: 0033, 0034, 0035, 0118, 0209, 0426 (open or
   dropped), from `comm` of the two number lists. So reports are fewer than
   briefs, not more. `work-paired` over the desktop app: "204 brief(s), every finished
   one has its report and its read-back, 12 still open".
5. **The desktop app's own concurrency rule is broken, and no check saw it.** Its
   standing brief says "one open brief per stream at a time". It numbers each
   stream in its own band of a hundred (director 0001 to 0099, engine 0101 to
   0199, and so on to launch 0601 to 0699). Open briefs now, from
   `grep -l -E "^status: *open" docs/briefs/*.md`: engine 2, runner 3, app 5.
   The kit's `open_briefs` is one global number, and the desktop app set it to 16. Its
   standing brief also records the rule being relaxed for one overnight wave,
   so a per stream limit would need a way to lift it, in the record.
6. **A small drift in the kit.** `formwork/COSTS.md` says "all twelve checks".
   `ls formwork/check/checks | wc -l` gives 13, and `FORMWORK.md` says
   thirteen. A count stated in three places. Whoever maintains the kit owns
   it. Not touched here.

## What the projects actually did with records

This shapes every answer below, so it comes first.

- **The health app** (5 briefs, 5 reports, no `docs/decisions/`, no `docs/rounds/`).
  Its rounds lived in `docs/research/`, `docs/design/` and `docs/review/`, each
  with its own `predictions.md` and `challenge.md`. `predictions-first` only
  looks in `docs/rounds/`, so it never saw any of them: "no docs/rounds
  directory, no rounds to check". The round discipline happened, and the check
  built for it examined nothing.
- **The health app's "dynamic roles"** were not new role files. Brief 0005's team table
  maps personas onto existing roles: the creative director runs as `visual`,
  and both the motion designer and the interaction designer run as `ux`, with
  skills attached. Four genuinely new roles exist in its project folder
  (ux-principal, behaviour-scientist, nutrition-scientist,
  training-scientist). So the real pattern is "persona over a base role,
  declared in the brief", and `role-shape` sees only the files.
- **The cross phase record already exists, in the standing brief.** The health app's
  "What is decided" is a run of dated entries, each with his words in quotes
  and the brief they bind ("sent to 0005"). The desktop app's is the same at scale: its
  standing brief is 481 lines (`wc -l`), 194 of them contain "his words"
  (`grep -c -i 'his words'`), and it has 3 decision files. Four entries
  replace an earlier rule inline (`grep -c -i -E '\(replaces|supersed'`).
- **Nobody wrote a one line brief.** The desktop app brief lengths from
  `wc -l docs/briefs/*.md`: shortest 13 lines, median about 28, longest 86.
  A brief for one social post is 22 lines. The health app's run 36 to 60 lines. No
  brief in any of the four projects carries a size.
- **The desktop app's `in my words:` lines are typed by the director**, by its own
  standing brief: "The director types his words, never writes them", with
  `read_back_words = 1`. That is allowed by `work-paired` and is exactly the
  limit `formwork/limits.md` names.

## K1. Checks a project layer would need

The standard every one below is held to: it names what it catches, it ships a
must-fail and a must-pass fixture, it says what it cannot tell, and it
separates "nothing claimed" (exit 0) from "claimed and nothing found" (exit 1).
Proposed names are plain text, because none of these files exist.

### Add

**1. Rounds where the check can see them** (an extension of
`predictions-first`, not a new check).
- Catches: a round held outside `docs/rounds/`, so the predictions check
  examines nothing. A file named predictions.md or challenge.md anywhere under
  `docs/` but outside `docs/rounds/` fails.
- Breaks it: `docs/research/predictions.md` beside lane files. That is
  the health app's real layout.
- Cannot tell: a round whose files are named something else. Whether the
  predictions were any good.
- Evidence: the health app, above. This is the one with a real case behind it today.

**2. Every brief names its size, and a task stays small** (a field read by
`work-paired`).
- Catches: a brief with no `size:` line (one of task, checkpoint, round,
  phase, milestone, the five in `formwork/loop.md`). And a brief marked
  `size: task` whose body runs past a ceiling, say 5 lines, as a setting. And a
  `size: round` brief with no round folder.
- Breaks it: a 22 line brief marked task. A brief with no size.
- Cannot tell: whether the size was right. A checkpoint written as a task
  with the detail moved to another file passes. A small ask written up as a
  checkpoint passes, which is the over building failure, and the one the desktop app
  actually shows. The ceiling stops a task growing quietly; nothing stops a
  task being born large.

**3. Every role a brief names exists** (new check, small).
- Catches: a team table naming a role in backticks that has no file under
  `formwork/roles/`. The agent then improvises a role with no boundary, which
  is what `role-shape` exists to prevent.
- Breaks it: a brief whose team row says `creative-director` with no role
  file.
- Cannot tell: whether the right role was picked. Whether a skill named
  beside it exists: skills live in the person's runtime folder, outside the
  repository, and are machine specific.
- Open, for the architect and the human: the same base role named twice in
  one team (the health app 0005 runs two personas on `ux`). That is `role-shape`'s
  "two roles owning one thing" one level up. Whether it caused harm is NOT
  ESTABLISHED, so at most a warning, never a refusal.

**4. A phase cannot open before the one it depends on is accepted**
(an extension of `work-paired`).
- Catches: a brief carrying `after: 0002` that is open or done while brief
  0002 is not done with its read-back.
- Breaks it: 0003 `after: 0002`, status open, 0002 status open.
- Cannot tell: whether the read-back was real (the same limit as
  `work-paired`). Work started in a window with no brief.
- Why a named dependency and not phase order: the health app ran review round 0004 and
  redesign 0005 open at the same time, by his choice, and 0005 is a design
  phase after a build. A gate that enforced spec, research, design, build,
  review in order would have refused the way he actually worked.
- Why inside `work-paired`: it reads the same files. `work-paired` already
  notes that a second parser of `.formwork.toml` would drift from the first;
  a second parser of brief frontmatter would too.

**5. Open briefs per stream** (a setting in `work-paired`).
- Catches: more open briefs in one stream than the stream limit. Stream from
  the `stream:` line (the desktop app has it in 66 of 204 briefs, from counting
  frontmatter keys), or from a declared number band.
- Breaks it: two open briefs, both `stream: engine`, limit one.
- Cannot tell: briefs with no stream line. Whether the overnight relaxation
  was his decision, unless the lift is itself a line in the record.
- A related cheap catch: a number band within a few numbers of full. The desktop app's
  app band holds 90 briefs in 0401 to 0499 (`ls docs/briefs | grep -c '^04'`),
  and `work-paired --next` hands out max plus one across all bands, so it does
  not know bands exist. Only worth adding if bands become a kit pattern.

**6. Nothing machine specific in kit files.** See K6.

### Refuse, or hold

**Project file shape check. Refuse.** The project file is the standing brief,
and `standing-current` already checks its headings and date. A second "project
file" with its own shape check is the same fact owned twice. If the spec is
meant, see the next item.

**Spec currency check. Hold until a second case.** In the health app, briefs name the
spec version they read ("version 0.5"). A check could fail an open brief that
cites an older spec version than the spec's own `version:` line. Breaks it: an
open brief citing 0.4 when the spec says 0.5. Cannot tell whether the
difference matters. One project did this. `formwork/rules/full.md` says build
the general version on the second real case.

**Review round shape check. Refuse the content, keep the location.** Item 1
already makes review rounds visible. Checking "findings by journey, each with
a screenshot" would check headings and file names, and `doc-links` already
resolves the screenshot paths if they are written in backticks. The rest is
the right shape passing for the wrong reason.

**Generated role provenance field. Hold.** An optional `made-for: 0005` field
on a project role, checked against an existing brief, catches an orphan role
nobody remembers asking for. Cheap. But `role-shape` keeps a fixed list of
optional keys, and this is the open question already on record in
`docs/standing.md`: whether the lead may invent a role. That is the human's
decision. The check follows the decision, never the other way round. What I
can say without deciding: if generated roles are allowed, `role-shape` already
does the important part. A generated file still needs five sections, four
fields, and an `owns` slug nobody else has, or it does not load.

**Taste checklist check. Refuse.** "One soft light per screen" is a judgement
about pixels. A text check can only verify that a report lists the items with
a mark beside each, which proves the list was copied, not that anyone looked.
That is a check that passes for the wrong reason, which `formwork/rules/core.md`
names directly. Ship taste lists as advice in a pack, in the same shape as the
rules: each item says what it catches.

## K2. The cross phase record

**It is not something new. In practice it already exists, in the wrong
place for its job.** Both projects kept it as dated entries under the standing
brief's "What is decided", each with his words quoted and the brief it binds.
The standing brief is rewritten and describes the present. A binding record
must not be rewritten. The desktop app's four inline "replaces" entries are where that
starts to show: the old rule survives only in version control.

Two kinds of thing are being mixed:

- **Forks.** "Version 1 includes the AI", "app only". These change later work
  and cannot be undone by editing. They are decisions. The kit's decision
  template fits, with two optional fields:

  ```
  his-words: "<quote, verbatim>"
  binds: [0003, 0005]      or   binds: all-after
  ```

- **Settlements.** Small answers to open questions. The health app logged about
  twenty in two days. A decision file each, with options and a bad column, is
  the paperwork that kills the method (`formwork/roles/method/director.md`,
  Size the brief). These stay as dated lines in the standing brief.

Fit to the existing checks:

- `decision-ids` needs nothing. It reads numbers and superseding, and the new
  fields do not touch either.
- `standing-current` already fails when a decision is newer than the standing
  brief, so a new binding decision forces the standing brief to move.
- One new catch is possible: an open brief listed in a decision's `binds:`
  that does not cite that decision's number. Breaks it: decision 0004 binds
  0007, brief 0007 never mentions 0004. Cannot tell whether the brief honours
  it. Hold until the field has been used for real.

Authorship stays as it is. Only the human writes a decision. An agent may copy
his accepted words verbatim, which is what the health app's director already did in
the standing brief.

## K3. Usage awareness

**`open_briefs` does not cover it.** It counts briefs, not builders. One
The health app brief, 0005, ran a team of six. And it is global, while the desktop app's real
limit was per stream.

What a kit with no network and no account access can measure:

- **Declared**: open briefs, per stream (item 5), and the rows in each open
  brief's team table. A declared builder count against a `builders` setting is
  checkable. It limits the plan, not the usage, and must be labelled that way.
- **Observed, this machine only**: a hook could write a heartbeat per session
  to the state folder the kit already uses outside the repository, and count
  sessions seen in the last few minutes. That sees one runtime with hooks, on
  one machine, in projects that installed the kit. It does not see another
  machine, a chat window, or a session in a repository without the kit.
  Nobody has built or measured this. NOT ESTABLISHED whether it is accurate.

What stays NOT ESTABLISHED:

- The person's plan limits, what is left, and when it resets. That needs the
  account.
- Tokens spent per builder. The runtime keeps transcripts on disk, but
  reading them is runtime specific, machine specific, and reads private
  content. I would refuse a check that does it.
- What a round costs. `formwork/COSTS.md` already says nobody has measured it
  once.

## K4. The router's record

Both projects already keep half of it: every brief opens with "## His words",
the prompt in quotes. What is missing is what the router made of it. One
block at the top of each brief would do:

```
size: task | checkpoint | round | phase | milestone
stream: <name>
roles: [<role>, ...]
said back: "<the one or two lines the router said before running>"
```

A wrong route is then visible: his words, next to the size and roles chosen,
next to what was said back. A correction is a line, never an edit:

```
resized: task to checkpoint, 2026-11-20, "<his words or the reason>"
```

What a check can keep honest:

- every brief has a size (item 2)
- a task stays under the line ceiling (item 2)
- a round sized brief has its round folder (item 2)
- every role named exists (item 3)
- a brief carrying a `resized:` line has a date on it

What is advice only, and must be written as advice:

- whether the size was right
- whether the roles were the right ones
- whether "said back" matches what then ran
- whether he read the line before it ran
- a resize nobody recorded. A check sees the line, never the absence of one
  that should exist.

The commonest misroute in the evidence is not a wrong role. It is over
building: no task sized brief anywhere in four projects. A check can only
catch the opposite direction, a task that grew.

## K5. What each check costs to keep

Measured, for scale: the 13 checks run 74 to 306 lines each, 2,210 in all
(`wc -l formwork/check/checks/*`). They ship 49 must-fail and 35 must-pass
fixtures (counted over `formwork/check/fixtures/*/must-*`). The gate's time is
NOT ESTABLISHED here, because the gate exits 2 on this machine. Commit history
per check cannot measure upkeep: the repository was rebuilt from a sync, with
38 commits in all (`git log --oneline | wc -l`).

What one more check costs, beyond its own lines:

- two fixtures at least, and one more for every failure it claims to catch
- a place in the next audit. The standing brief records five audits finding
  71 defects, "nearly all in what had just been written", including new
  checks that reported clean while examining nothing
- re-recording the integrity fingerprints, a human step
- counts in `FORMWORK.md`, `docs/standing.md` and `formwork/COSTS.md`, which
  already disagree once
- **the biggest cost: every new required field is a line every brief carries
  for ever.** `size:`, `stream:`, `after:`, `binds:` together are four lines
  on a brief whose whole point, for a task, is to be one line. So: `size:` is
  the only field I would make required. The rest are optional, and checked
  only when present.

Would add, in this order: rounds visible (1), size and task ceiling (2), roles
exist (3), the leak scan (K6), then `after:` and per stream limits (4, 5) only
once a project has asked for them twice.

Would refuse: a taste checklist check, a project file shape check, a review
round content check, a linear phase order gate, any check that judges the
router's choice, and any usage meter that reads runtime files or needs an
account.

## K6. What stays out of the kit, and a scan for it

Stays in projects: machine names and hostnames, private network addresses,
absolute home paths, account names and emails, signing identities, app
identifiers, device names, release machines and how they are reached,
runtime skills installed only for one person, and any taste list written from
one product. The kit may describe a general pattern ("a release step owned by
another machine or session"), nothing more.

A check can catch the crude form. Proposed: a kit leak scan over kit files
only (`FORMWORK.md`, `formwork/`).

- Catches: an absolute home path (a path under a named user's home on macOS,
  Linux or Windows), a private network address, a hostname ending in a local
  network suffix, an email address.
- Breaks it: a kit document containing a real looking home path with a user
  name.
- Passes: `~/`, a placeholder, and the reserved example domains. The kit's own
  tests already use `example.invalid` and `example.com`.
- Today the kit is clean on a crude version of this: a grep for home paths
  over `formwork` and `FORMWORK.md` found 0 files, and the only email like
  strings were the two reserved test domains above.
- Cannot tell: a machine named in plain words ("the second laptop"), a
  paraphrase of private facts, a name that is also an ordinary word.
  `formwork/limits.md` already says a clean scan proves nothing about what it
  cannot see.
- **The rule that matters most:** the patterns must be generic. Entry 8 of
  `docs/dogfood.md` records the kit's own privacy tool describing the private
  repositories through its configuration. A scan with a list of this person's
  machines in it would be the leak. Specific word lists stay outside the
  repository, where the kit already keeps them.
- Not `kit-integrity`: that check compares fingerprints and has no opinion on
  content. A separate small check is the honest shape.

## What I read

In this repository: `docs/rounds/whole-project-builds/brief.md`,
`docs/briefs/0022-whole-project-builds.md`,
`docs/ideas/2026-11-15-whole-project-builds.md`, `FORMWORK.md`,
`formwork/rules/core.md`, `formwork/rules/full.md` (headings and the rules on
roles, generalising and cost), `formwork/check/run`, the docstrings of all 13
checks, and in full `work-paired`, `role-shape`, `predictions-first`, most of
`report-shape` and `standing-current`; the fixture list; the docstrings of the
three guards; `formwork/limits.md`; all six templates; `formwork/COSTS.md`;
`formwork/roles/HOW-TO-ADD-A-ROLE.md`; parts of `formwork/loop.md` and the
director role; `docs/standing.md`; `docs/decisions/`; parts of
`docs/defects.md`, `docs/design.md` and `docs/dogfood.md`.

In the projects, read only: the health app's docs layout, `docs/standing.md`, the
heads of its five briefs, brief 0005's team table, the frontmatter of its
project roles and `.formwork.toml`. The desktop app's `.formwork.toml`, the structure
and tail of `docs/standing.md` with its "How the work is organised" section,
`docs/decisions/` (list), report and brief counts, the frontmatter of three
briefs from 0450 onward. Ship-ai's and Studio's brief heads and one project
role. I did not open the health app's profile folder or any credential file.

Commands I ran, all read only: `formwork/fw check` (exit 2), each kit check
run alone over this repository and over the four projects, and the counts
named beside each number above.

## What I could not establish

- Whether the full gate is green here. It cannot run until fingerprints are
  recorded.
- What the gate costs in time with more checks added.
- Whether two personas on one base role ever caused a wrong answer.
- Whether a heartbeat hook would count builders accurately. Never built.
- Anything about plan limits or token use.
- Whether the desktop app versioned a spec the way the health app did. I did not look, so the
  spec currency check has one case, not two.
- Whether anyone reads the `said back` line before work runs.

## Response to the lead

**1. Adjust. A durable project file is the missing home, on two conditions.**
I refused a file that repeats the standing brief's headings. Declared streams,
start conditions and routing corrections are a different kind of fact: they
bind later work, so they should not live in a page that is rewritten. Today
The desktop app keeps its streams table inside the standing brief. Condition one: moving
it means deleting it there, leaving a pointer, never keeping both. Condition
two: the file is append only for corrections, dated, in his words. A fork
still goes to a decision record. The check is worth having: every brief's
`stream:` is declared in the project file. Breaks it: a brief with
`stream: engine` and no engine stream declared. Cannot tell: whether the
stream was the right one. With no project file, nothing is claimed.

**2. Rebut the fact, keep the key.** The health app's reports do carry the read-back.
`grep -n -i -E "^accepted\s*:|^in my words\s*:" docs/reports/*.md` in the health app
finds both lines in all three done reports (0001, 0002, 0003). And the go word
is the read-back: 0002's `in my words:` line is "finished, lets go buildinggg,
start". So the gate already keys off something he actually does. The weak part
is the one `formwork/limits.md` names: who typed the line. The desktop app's director
types it, with `read_back_words = 1`. No file check can see a hand on a
keyboard. A phase gate keyed off a standing entry would be weaker still,
because that page is rewritten. I keep `after:` keyed off done with read-back,
labelled with that limit.

**3. Adjust: neither required everywhere, each required once claimed.**
`stream:` is the field people already write. The desktop app has it in 66 of 204
briefs, and none of the four projects writes a size. So: `stream:` becomes
required once the project file declares streams, and checked against it.
For size: **a brief with no `size:` line counts as a task**, and a task over
the line ceiling fails until it states its size. A one line brief carries no
extra field, and a brief that grew past a task has to say so. That keeps the
over building signal, the reason the router needs a record, at no cost to
small asks. My earlier "size is the only required field" is withdrawn.
