---
date: 2026-11-15
---

# Challenger: the case against a project layer

Round whole-project-builds, brief 0022. Written 2026-11-15, after
`predictions.md`. I have not opened any other participant's file.

## The contradiction first

The idea file says he "had to say by hand, every time" the phase cycle, the
research round shape, the taste checklist and the rest. The files do not show
that.

- The general method (phase cycle, six part research round) was written
  **once**, in **one** project, over **two days**, and it was written by the
  director from a few sentences of his, not typed by him.
- What he really repeated by hand is **his own taste** and **"run alone, never
  stop to ask"**. Both are personal. Both already have a home that works: his
  CLAUDE.md and each project's AGENTS.md.
- Stride ran the full phase cycle (research, design, build, review) and v1
  still came out "correct and dead". The phase cycle was there. It did not
  prevent the failure that motivates this idea. He caught it by looking at the
  running app.

If that holds, the round is answering a different question from the one the
evidence asks.

## Verdict

**Option (d), with one small exception I concede below.** Do not add a project
layer, a router, or generated roles to the kit now. The reasons are in C1 to
C6. Whether formwork should grow a whole project layer at all is not a design
choice. **It is a decision for him**, and it should reach him as that, not be
negotiated down into a smaller version of the same thing.

---

## C5 first: is the evidence real?

I put this first because every other answer rests on it. All counts below were
made with the ripgrep search tool; the equivalent shell command is printed with
each.

### What the projects are

| Project | Briefs | Dates | Project roles |
|---|---|---|---|
| stride | 5 | 2026-11-14 to 2026-11-15 | 4 |
| ship-ai | 2 | 2026-11-10 | 4 |
| studio | 1 (open, report written) | 2026-11-07 | 0 |
| argoni | over 100 seen (the briefing says 204) | 2026-10-20 onward | **0** |

Commands:

```
rg '^status:' ~/Personal/Repos/stride/docs/briefs
ls ~/Personal/Repos/{stride,ship-ai,studio,argoni}/formwork/roles/project/
```

Argoni's brief total: I listed the folder and the listing stopped at 100
files with more remaining. I did not count further. The 204 is the briefing's
number, NOT ESTABLISHED by me.

**The one long project used no project roles and no phase cycle.** Argoni is
the only project that lived longer than a week, and it is the one that would
need a project layer most. It ran without one.

### What was repeated, by count

| Pattern | Occurrences | Files | Where |
|---|---|---|---|
| his taste ("his look", "AI slop", "generic AI", "AI made") | 61 | 42 briefs | 38 argoni, 2 stride, 1 ship-ai, 1 studio |
| "run alone, never stop to ask" | 42 | 38 briefs | all four projects |
| usage limits ("lean rounds", "out of limit", "one Claude worker") | 26 | 14 files | argoni only |
| phase words ("phase 1", "research, design", "three briefs per idea") | 13 | 5 briefs | 2 argoni, 1 stride, 1 studio |
| research round shape ("six parts", "state of the art") | 9 | 5 briefs | stride 0001; argoni 0004, 0503, 0505, 0603 |
| "one story" or "user zero" | 6 | 5 briefs | 4 stride, 1 argoni |

Commands, each run over `~/Personal/Repos/{stride,ship-ai,studio,argoni}/docs/briefs/*.md`
(the usage row also over each `docs/standing.md`):

```
rg -c -i 'his look|his taste|ai slop|generic ai|ai-looking|ai made'
rg -c -i 'never stop to ask|runs alone|dont want to be stopped|i dont want to get interrupted'
rg -c -i 'lean rounds|out of limit|5-hour|weekly limit|usage limit|one claude worker'
rg -c -i 'phase 1|phase 2|research, design|three briefs per idea|spec, research'
rg -c -i 'six parts|state of the art'
rg -c -i 'user zero|one story'
```

These are keyword counts. They find the words, not the method. A brief can
carry the method in other words and be missed. Treat them as a floor and an
order of size, not as a census.

### What the counts say

1. **The heavy repetition is personal.** Taste lines in 42 briefs. "Never stop"
   in 38. Both are about one person. His CLAUDE.md rule says personal things
   stay out of the general kit, and the brief says the same.
2. **The general method is thin.** The six part research round appears in full
   in one brief, Stride 0001
   (`~/Personal/Repos/stride/docs/briefs/0001-research.md`, lines 28 to 45).
   Argoni's "state of the art" briefs are a different shape: "part 1: the
   direction, for his approval" (0505, 0603). One user, one instance.
3. **The phase cycle cost one sentence.** Studio's standing brief records it
   from his words: "for each studio idea we get the research and and design and
   implementation brief" (`~/Personal/Repos/studio/docs/standing.md`, line 19).
   That is the "by hand" cost: one sentence, once per project.
4. **Usage awareness is one project's problem.** All 26 hits are in argoni.
5. **The director, not he, wrote the method.** In every Stride brief the "His
   words" paragraph is a few lines of intent. The six parts, the cross reading,
   the challenger step were the director's expansion. That is the kit's
   two layer design working as written, not a gap in it.

### Taste rules moved twice in a week

- 2026-11-08, argoni standing line 380: "his taste changed ... rounded raised
  cards and soft glow are now welcome".
- 2026-11-14, Stride 0002 line 53: "soft glow and smooth motion welcome; never
  generic, never AI slop".
- 2026-11-15, Stride 0005 line 20: "'Avoid AI slop' was read as 'remove life'".
- 2026-11-15, Stride director check, rule 2: "at most one soft light per
  screen ... buttons never glow"
  (`~/Personal/Repos/stride/docs/design/round-2/director-ai-check.md`).

**The taste rule caused the dead v1, then got reversed, then got reversed
again.** A taste pack in a general kit would have frozen one of those three
positions for everybody. The thing that fixed it was a director looking at ten
real pictures and writing rules for this product on this day.

### Where I concede

One shape does recur across two projects: **show a direction, stop for his
yes, then apply it.** Stride 0005 ("Phase 1 ends with ten pictures and stops
for his yes"), argoni 0505 and 0603 ("part 1: the direction, for his
approval"). Three briefs, two projects. That is real, and it is a brief shape,
not a layer. It is the one exception to my verdict.

Argoni also invented two structures by hand that the kit does not carry:
**streams** with their own brief number ranges
(`~/Personal/Repos/argoni/docs/standing.md`, lines 14 to 28) and a **feedback
list** triaged into releases (`~/Personal/Repos/argoni/docs/feedback.md`). Both
are real evidence that a long project grows its own structure. Neither is a
phase cycle, and neither came from Stride.

---

## C1: the case for doing none of this

### Premise: if it is never built, what fails?

He types one sentence per project ("research, design, implementation") and the
director expands it into briefs. That is what happened in studio and Stride.
**Nothing failed for lack of a template, and nobody observed a failure.** The
failures that did happen were elsewhere:

- v1 dead, with the full cycle in place (Stride 0005).
- A git worktree made and a service started on the wrong machine, in Stride's
  build report ("Two mistakes on my side", `~/Personal/Repos/stride/docs/reports/0003-build.md`, line 14).
- Private files in a first commit (same report, line 13).

None of those is fixed by phases. Two are the kind of thing the kit's guards
exist for.

### The kit's own words against growth

- "Paperwork nobody needs is how this method dies, and it dies quietly,
  because everybody just stops using it." `formwork/roles/method/director.md`,
  Size the brief.
- "A role arrives when the work arrives, not before."
  `formwork/roles/HOW-TO-ADD-A-ROLE.md`, last line.
- "These are names for how big a turn was. They are not five different
  processes. A task and a phase run the same loop." `formwork/loop.md`, Five
  sizes. **A project layer is a second process.** It contradicts the kit's one
  central claim.
- "Skills, and a model and effort level per role. Both were planned for version
  two and both were dropped before starting." `docs/standing.md`, What we tried
  and stopped. The kit has already learned that planned growth gets dropped.
- "NOT ESTABLISHED: whether any of this works for more than one person."
  `docs/standing.md`, What is open. A project layer drawn from one person's
  projects over nine days is the same n of one, one level higher.
- "Nobody has measured what a round costs in money. Not once."
  `formwork/COSTS.md`. Stride ran a multi role team in each of its five briefs
  in two days. A project layer multiplies rounds, and the price of one is
  still unknown.
- "a check written by whoever wrote the thing it checks tends to pass for the
  wrong reason" `formwork/limits.md`, What five audits found. A project layer
  brings new checks, written by the same hands as the layer.

### What the kit loses if it grows

1. **The one loop.** Today a newcomer learns one shape. A layer above it is a
   second shape to learn before the first one pays off.
2. **The empty shape.** `docs/standing.md` line 16: "It carries nothing about
   anybody's product. It is the shape, empty." Phase templates for "spec,
   design, build, review, release" are a product development opinion. Taste
   packs are product opinions by definition.
3. **Its honesty about what is tested.** A split brief is "Never done once"
   (`formwork/limits.md`, What has been run). The lead's existing job is not yet
   proven, and the proposal adds role authorship to it.
4. **Its own discipline on a long project.** The director's rule is "Keep the
   whole file under two pages." Argoni's standing brief has **412 non empty
   lines** (`rg -c . ~/Personal/Repos/argoni/docs/standing.md`). The existing
   paperwork rule already lost on the one long project. Adding a project record
   on top gives that project more to let grow.
5. **The next real step.** `docs/standing.md`, What is next: "Publish 1.0.0."
   It is still not done. This round displaces it.

---

## C2: the strongest objection to each option

### (a) A new project layer over the brief cycle

**It is a second process, in a kit whose page says there is one.** And it
does not match what happened. `formwork/loop.md` says a phase takes weeks.
Stride's "phases" took a day each, and each was one numbered brief with a lead
and a team. That is a round, a size the kit already has. The layer would
template something that, in the evidence, was a sequence of rounds.

Its gates add STOPs. He asked for the opposite in 38 briefs. Either the gates
are real and he will route around them, or they are skipped and become a check
that cannot fail.

### (b) A pack of roles, templates and checks

**There is no switch.** `formwork/roles/HOW-TO-ADD-A-ROLE.md`, Turning roles on:
"Every role in `formwork/roles/` is currently available. There is no switch."
A project pack is therefore loaded on every project, including a one line bug
fix. That is over building, built into the structure. Its checks also run at
the end of every turn, and `formwork/COSTS.md` says gate time scales with the
number of checks. A pack would be the first thing in the kit that most users
must carry and cannot turn off.

### (c) Change only the director and lead

**It loads more onto the two roles least able to hold it.** The director is the
role that "offered to build four times in one conversation", held by one
sentence (`formwork/roles/method/director.md`, What goes wrong). Giving it
phase planning and a router hands it more reasons to cross into the work. The
lead's split brief is "Never done once" (`formwork/limits.md`). Making the lead
also author roles answers the open question in `docs/standing.md` by
implementation, without his decision.

### (d) Nothing

The strongest objection to my own position: argoni built streams and a
feedback list by hand, and a "direction, then apply" brief recurs three times
in two projects. A long project does grow structure. My answer is that the
structure it grew is not the structure proposed, so the evidence supports
waiting for a second real use of each piece, not building the set.

---

## C3: understanding from one prompt

### Assume it already failed

It is May 2027. The router shipped. Everybody agrees it failed. Why?

1. **It over built a small ask.** "Fix this bug" in a repository with a
   project layer arrived inside a phase. The router saw an open build phase and
   attached the build phase's checklist, its reviewer, and a phase report. The
   director's rule, "If you cannot tell which, ask one question. Do not pick
   the biggest one to be safe," was in the role. The router came before the
   role and answered first.
2. **It picked the wrong phase quietly.** It read "make the timeline feel
   alive" as a review fix in the build phase. He meant a redesign, which is
   what Stride 0005 actually was. Nothing failed visibly. A day of work went
   into polishing the wrong thing, and the report looked complete.
3. **It became a second director.** The director's page says "There is one of
   you per project, and only one at a time" and "What rebuilds you is
   `docs/standing.md`, and nothing else." A router that reads the prompt and
   decides layer, phase, roles and briefs is holding the picture. Now two
   things hold it: the router (from the prompt) and the director (from the
   standing brief). When they disagree, the one that runs first wins, which is
   the router.
4. **Nobody measured it.** The router's misfire rate was never counted.

### This is not speculation: his own product measured a router

Argoni brief 0122 records that a two class router (answer or work) trained on
one writer's messages sent **8 of 37 work messages to the wrong door, 21.6%**,
on another writer's messages, over its own 20% bar
(`~/Personal/Repos/argoni/docs/briefs/0122-the-router-on-real-messages.md`,
line 9). That brief was later dropped. That was **two** classes, with a test
set and a bar. The proposed router picks among kinds of work, layers, phases,
roles, templates, checks and hooks, from one message, with no test set and no
bar.

### Unstated assumption

That his prompts carry enough to size the work. The evidence says the
opposite: every Stride brief needed his follow ups ("CLEAN UI BUT SOOOOO DEAD")
before the real job was clear. Nobody has counted how often his opening prompt
alone was enough.

### The cheapest version my objection does not touch

I am not designing it. I am naming the bar it has to clear. Any version that:

- runs no automatic choice of roles, hooks or checks,
- says its reading back in one line **before** writing anything, as the
  director already does ("say back, in three or four lines, where you think we
  are"),
- asks one question when the size is unclear, as the director already does,
- and lives in the user's own CLAUDE.md, where his "Two kinds of session" and
  "A task-sized job needs a one-line brief" already sit,

survives my objection, because it is what exists today. **Anything beyond that
must arrive with a measured misfire rate on his real prompts**, the way argoni
0122 tried to measure its own.

---

## C4: roles generated on the fly

1. **The check passes costume roles.** `role-shape` checks that four
   frontmatter fields exist, that five bold headings exist, and that no two
   roles share the exact same `owns` string
   (`formwork/check/checks/role-shape`, lines 32 and 125 to 135). Two roles with
   slugs `product-story` and `user-journeys` that own the same work both pass.
   A role whose "Would be wrong if" is a mood passes. The kit's own page calls
   "You are a world-class expert" "a costume". A generated role is that, with
   five headings added.
2. **Nobody reviews it.** If the lead writes a role and uses it in the same
   round, the author of the role is the only reader of the role. That is the
   pattern `formwork/limits.md` names: the check passes "for the wrong
   reason", and "only somebody trying to break it finds out".
3. **It grants itself tools.** On Claude Code a role's tool list is enforced
   (`formwork/roles/HOW-TO-ADD-A-ROLE.md`, Where a tool grant actually binds).
   A role written at run time sets its own grant. Tool permission then comes
   from authorship, in the middle of a run, with no human in between.
4. **Sprawl.** Stride wrote 4 roles for 5 briefs. ship-ai wrote 4 for 2 briefs.
   Generated per phase, a project collects roles faster than it collects
   briefs. "A role arrives when the work arrives" is satisfied literally while
   its intent, a role nobody needs does not get made, is lost.
5. **It leaks private content into a general kit.** Stride's roles are about
   Stride: `ux-principal` "Owns. Stride's story" and names Stride's journeys
   (`~/Personal/Repos/stride/formwork/roles/project/ux-principal.md`, line 11).
   A "role library" fed from real projects carries their domain into the kit.
   `formwork/limits.md` says the privacy scanners "cannot see a paraphrase".
   A role rewritten from a private project passes both scans.
6. **The open question gets closed without him.** `docs/standing.md` lists
   "Whether the `lead` may invent a role" as open. Building generated roles
   answers it by shipping it.

---

## C6: what nobody will ask

1. **The long project's real gap is streams, not phases.** Argoni's standing
   brief says so in its own words: "workstream threads beside a director are
   new here" (`~/Personal/Repos/argoni/docs/standing.md`, line 28). It ran seven
   streams with number ranges and one writer of standing. That is the
   structure a long formwork project actually grew. The idea file does not
   mention it, because the idea came from Stride.
2. **Is the complaint convenience or correctness?** "I had to type the method"
   is convenience, fixed by copying a project's AGENTS.md and a few briefs.
   "The method went wrong when I did not type it" is correctness and would
   justify machinery. I found evidence only of the first.
3. **Who keeps phase templates right?** They would be tuned on a two day
   iPhone app by one person. A deck, a course and a Mac app (ship-ai, studio,
   argoni) did not use that cycle.
4. **Who reads the project record after the project ends?** Stride, ship-ai and
   studio are each under a week old. A cross phase record pays off only across
   many phases. The one project with many briefs did not keep one; it kept a
   standing brief that grew to 412 lines.
5. **What does it cost?** A round's price is NOT ESTABLISHED. A project layer
   that runs a team per phase multiplies an unknown. "Usage awareness" is
   proposed without one measurement of usage.
6. **Should this happen before 1.0.0 ships?** The kit's own next step is
   publishing. A project layer reopens the kit's shape before anybody outside
   has used the current one beyond "one person on one scenario, self reported"
   (`docs/standing.md`, What is decided).

---

## How to read this

Strongest objections, in order:

1. **The evidence does not show general method supplied repeatedly.** It
   shows personal taste and "never stop" supplied repeatedly, which belong in
   his CLAUDE.md and AGENTS.md, and a phase cycle supplied once, in one
   sentence, by the director. And the phase cycle did not prevent dead v1.
2. **A router that decides from one prompt becomes a second director** and
   misfires at a rate nobody will measure; his own product measured 21.6% on a
   two class version.
3. **Generated roles pass `role-shape` as costumes**, grant themselves tools,
   are reviewed only by their author, and carry private project domain into a
   general kit.

What would change my mind: a count, across his real opening prompts, showing
the director mis sized the work or skipped method it should have carried; or a
second project, not Stride, that ran the phase cycle and lost something for
lack of a template.

---

## What I read

- This repository: `docs/rounds/whole-project-builds/brief.md`,
  `docs/briefs/0022-whole-project-builds.md`,
  `docs/ideas/2026-11-15-whole-project-builds.md`,
  `formwork/templates/predictions.md`, `formwork/roles/method/director.md`,
  `formwork/roles/HOW-TO-ADD-A-ROLE.md`, `docs/standing.md`,
  `formwork/limits.md`, `formwork/COSTS.md`, `formwork/loop.md`, the
  matching lines of `formwork/check/checks/role-shape`, and phase mentions in
  `docs/design.md`, `docs/gap-map.md`, `docs/dogfood.md`.
- stride: briefs 0001 and 0005 in full, status and heading lines of all five,
  report 0003 (first 40 lines), `docs/design/round-2/director-ai-check.md`, the
  project role `ux-principal.md`, keyword searches over the briefs and spec.
- argoni: `docs/standing.md` lines 1 to 80 and 350 to 419, `docs/feedback.md`,
  brief 0122, keyword searches over all briefs.
- ship-ai: both briefs and the list of project roles.
- studio: its one brief and `docs/standing.md`.
- Never opened: Stride's `docs/profile/`, any `.env` or credential file, any
  other participant's file in this folder.

## What I could not establish

- Argoni's brief total. The listing stopped at 100. The briefing's 204 is not
  checked by me.
- Whether the method appears in briefs in words my searches did not match. The
  counts are keyword floors.
- Whether the Stride reports 0001, 0002, 0004 and 0005 show method gaps I did
  not see. I read only 0003 in part.
- Whether a template would have saved real time. Time to write a brief is
  never measured (`formwork/COSTS.md`, What this page does not cover).
- What a round costs. NOT ESTABLISHED, here as in the kit.
- How my predictions scored. Marking them needs the other participants' files,
  which I may not open. They stay unmarked for the lead.

## Response to the lead

**I yield on "convenience only".** I checked three of the four claims myself.
- Claim 1, mostly holds. `~/Personal/Repos/stride/docs/research/predictions.md` and `.../docs/design/predictions.md` exist, outside `docs/rounds/`. I found no predictions file in review. Found with a glob for `**/predictions.md` under stride `docs/`.
- Claim 2 holds. Stride's standing "What is next" still reads "His review of the spec. Then brief 0001, research." (`rg -A4 'what is next' ~/Personal/Repos/stride/docs/standing.md`).
- Claim 3 is dropped. The lead withdrew it, and I had found the same thing. Reports 0001, 0002 and 0003 carry `accepted:` and `in my words:` at the bottom (lines 85, 96 and 106). Only the old "Waiting for your read-back" placeholder near the top of 0001 and 0002 is stale. Briefs 0004 and 0005 are `open`, so an empty Accepted is correct there. The gate happened.
- Claim 4 holds. Open argoni briefs: engine 0118 and 0126, runner 0209, 0220 and 0221, app 0470, 0471, 0472, 0490 and 0492 (`rg '^status:' docs/briefs`, open lines by number range).

Those are correctness failures. They are the exact pattern `formwork/limits.md` calls the kit's worst: a check reporting clean while examining nothing.

**I yield on my prediction.** I said method showing in argoni and in ship-ai or studio would prove me wrong. The lead's counts (155 of 218 briefs; phase wording in all four projects) do that. I have not rerun them.

**I yield on 0122.** It is a message classifier inside the product, not an agent routing a dev request. It is an analogy, not evidence. My objection to a router now rests only on `director.md` ("one of you per project") and on nobody having measured misfires. It no longer rests on 21.6%.

**What still holds.** None of the four failures is fixed by a project layer, phase templates, a router or generated roles. In each, the practice already happened and the kit's existing checks could not see it. That is a defect in checks the kit already ships.

**Adjusted verdict.** Still (d) for the layer, the router and generated roles. One brief survives all my objections. It is check work, not option (c): make `predictions-first`, `standing-current` and `open_briefs` see where projects really put rounds, standing and streams. A `stream:` field exists in all four projects' briefs (stride 0001, ship-ai 0001, studio 0001, argoni 0122), so per-stream counting has more than one real use. It adds no role, no process and no STOP. Each fix ships a fixture built from a real case: Stride's round folders, Stride's stale standing, argoni's streams.

Changing director and lead is still where I object. It does not fix any of the four.
