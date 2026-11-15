---
date: 2026-11-15
---

# Product: what a person building a whole product needs from formwork

Brief 0022, the `product` role. Evidence is the four projects named in the round
brief, read only. Method is quoted. Product content is not.

Paths to other projects are written in full, starting `~/Personal/Repos/`.
Counts come with the search that produced them. "Grep" below means the
ripgrep search tool, run with the pattern, the folder and the file glob shown.

## The short version

1. **The same phase cycle was invented by hand in all four projects.** The
   person wrote it into a spec, a design brief, a build plan, or a list of
   "three briefs per idea", and never in the same words twice. It is the
   largest gap and it is general.
2. **The person's real gates were one word long.** "go", "accepted",
   "finished, lets go buildinggg". He never wrote the two-line read-back the
   report template asks for in health-app. His read-back was the word that started
   the next phase. A project layer should build its gates around that word,
   not around a form.
3. **"Never stop to ask" is in 57 brief files.** The person had to say it in
   almost every brief. Running alone between gates should be the default for
   anything bigger than a task, with choices collected at the end, each with
   one recommendation.
4. **Taste rules cut both ways, and only one way was ever written down.**
   "Avoid AI slop" produced an app that was "CLEAN UI BUT SOOOOO DEAD". A taste
   pack that only lists what to remove will produce dead products. It needs
   the "alive" half too.
5. **Dynamic roles were mostly relabels, not new files.** the health app wrote four
   project roles and relabelled about eight kit roles inline ("`visual` as
   creative director"). the desktop app wrote none and invented its reviewers inside
   each brief. The cheap form (a relabel plus a skill) carried most of the
   load.
6. **Protecting the person's live device or screen recurs in 105 brief
   files.** No kit rule says it. It is general.
7. **Usage limits were a felt problem once** ("why did we use 97% of my plan")
   and produced four rules that every later brief repeated. General as a
   pattern, personal in its numbers.
8. **The release machine is personal, as the person said.** The general
   pattern under it is small: a release step owned by another session, started
   by one written line, never on a schedule, ending in a release record.

---

## P1. What is missing, with evidence

Each row: where the method lives, a short quote of the method, how often it
recurred, and whether it belongs in a kit (general) or stays in the project
(personal).

### 1. The phase cycle for a whole product

**Where and what.**

- `<health-app>/docs/product-spec.md` section 12: "Three phases,
  each run without interrupting him, each ending with something for him to
  review: 1. Research ... 2. Design ... 3. Build ... then one or two review
  rounds".
- `<health-app>/docs/briefs/` 0001 to 0005: streams `research`,
  `design`, `build`, `review`, `design` (round 2).
- `<desktop-app>/docs/briefs/` 0033 to 0041, all stream `director`:
  "requirements; no design, no code" (0034), "design options; no code" (0035),
  "design input; no design, no code" (0036), "measurements, no product code"
  (0037), "research, no design" (0038), "design; no code" (0039), "plan only;
  no product code" (0041). Then 36 build briefs labelled
  "design A build, step N, part BN" (0440 to 0475), then "release 0.1.N", then
  "launch (wave 1)".
- `~/Personal/Repos/studio/docs/briefs/0001-the-studio-designed.md`: "for each
  studio idea we get the research and and design and implementation brief"
  (his words), and "the three briefs per idea (research, design,
  implementation), what each must answer, and what 'done' means".
- `~/Personal/Repos/ship-ai/docs/briefs/0002-the-staff-deck.md`: the deck runs
  "in three phases (words, design, build) and stops for [the person's] yes
  after each". Then "his change": "i dont want to be stopped in the middle".

**Recurred.** In 4 of 4 projects. In desktop-app, 36 of the 53 briefs from 0440 to
0492 are steps of one phase plan (Grep `^stream:` in
`<desktop-app>/docs/briefs`, counting lines that contain
"design A build"; counted by hand from the 70 lines returned).

**General or personal.** General. The order (spec, research, design, build,
review on the running product, release) is the same everywhere. What differs
is the name of each step, which is a project's choice.

**What the kit has today.** `formwork/loop.md` names a phase in one line: "A
question big enough that its answer is a document." No template, no gate, no
order.

### 2. The research round shape

**Where and what.**

- `<health-app>/docs/briefs/0001-research.md`: each lane writes one
  file "in exactly these six parts: 1. The question, and why it matters ...
  2. Theory ... 3. State of the art ... 4. What it means for [the product] ...
  5. Proposals. Ranked, each with the evidence behind it, its cost, and what it
  replaces or removes ... 6. Risks and unknowns". Then "Round 2, cross
  reading", "Round 3, the story" (one integrator joins everything), "Round 4,
  challenge", "Spec update".
- `~/Personal/Repos/ship-ai/docs/briefs/0001-the-roadmap.md`: two researchers,
  a planner, "Content writer (integrator)", then "Challenger: reads the roadmap
  cold".
- `<desktop-app>/docs/briefs/0034-requirements-first.md` and
  `0039-design-round.md`: requirements first, then "two or three genuinely
  different whole designs", "walk every design through every scenario", score
  against requirements, "the breaker", "compare and recommend one".
- `<health-app>/docs/reports/0001-research.md` shows what the round
  cost and what it would change: "It would have been cheaper without losing
  quality if each round 1 file had ended with a 20 line summary for cross
  reading", and "the shared search budget also ran out ... search should be
  rationed per lane".

**Recurred.** The shape "parallel lanes, then one integrator, then a challenger
read cold" appears in 6 briefs I read: health-app 0001, 0002, 0004, 0005;
ship-ai 0001; desktop-app 0039 (by reading, not a search).

**General or personal.** General. The kit's `formwork/round.md` already has
predictions first and a challenger. What it lacks is the lane file's six parts,
the integrator step, and the spec update at the end.

### 3. Taste and anti AI slop rules

**Where and what.**

- `<health-app>/docs/design/round-2/director-ai-check.md`, ten
  rules: "pills only for a real choice the person makes"; "at most one soft
  light per screen ... buttons never glow"; "solid colours; a gradient only
  where it carries meaning"; icons "without a tile"; "draw a chart only from
  real numbers"; "one neutral surface"; "standard system navigation"; "say the
  thing, not the feature"; no placeholders that look fake; "one category colour
  per row".
- `<health-app>/docs/briefs/0005-bring-it-to-life.md`: "'Avoid AI
  slop' was read as 'remove life'. The goal now: alive, warm, smooth, creative,
  and still calm".
- `<desktop-app>/docs/briefs/0475-quiet-and-right.md`: "no
  unnecessary statements or wordings", "no pills anywhere".
- `<desktop-app>/docs/standing.md`, 2026-11-08: "his taste changed".
  Glow went from banned to welcome.
- `~/Personal/Repos/ship-ai/docs/standing.md`: a deck font "so dead ... so
  generic".

**Recurred.** "dead": 31 times in 15 files (Grep `\bdead\b`, case insensitive,
glob `{health-app,desktop-app,ship-ai,studio}/docs/{standing.md,briefs/*.md}`; a few
desktop-app hits are "dead code", so the taste count is lower, not established
exactly). "AI slop", "AI made", "AI looking", "generic AI", "so AI": 35 times in
23 files (Grep with that pattern over each project's AGENTS.md, standing page
and briefs). Present in all 4 projects.

**General or personal.** Split.

- General: the structural checks (choice versus decoration, one focal light,
  data only from real numbers, copy that says the thing, standard navigation),
  and the lesson that **clean and alive are both required**. These differ by
  product kind (phone app, desktop app, website, deck), so they fit optional
  packs.
- Personal: the colours, fonts, ground colour, the glow preference, the values
  and faith rules on images. These changed during the work, so they must be a
  dated project setting, never a kit default.

### 4. User first story and the user zero pattern

**Where and what.**

- `<health-app>/docs/product-spec.md` 1b: "one story, not a pile of
  features ... Every screen answers 'where am I today, what is next, how am I
  doing' ... Any feature that does not fit the story is cut or folded in. The
  design phase is judged against this section first."
- Same file, section 2: "[the person] is user zero. His real history is how we
  discover what the app must do. Every feature is written as a general need
  that his case revealed, never as a rule about him."
- `<health-app>/docs/review/round-1/findings.md`, item 4 of the five
  that hurt most: "User zero's shape reached everyone". So the pattern needs a
  check at review time, not only a sentence in the spec.
- `<desktop-app>/docs/briefs/0034-requirements-first.md`: "a product
  reviewer standing for the five user kinds (overfitting to him)". And 0039: "a
  product reviewer for the ten user kinds".
- `<health-app>/formwork/roles/project/ux-principal.md`: "Would be
  wrong if. The result is a feature list with screens, a tab bar of tools ... or
  a story that only works in the happy path."

**Recurred.** 2 of 4 projects (health-app, desktop-app). The two other projects are a
course and a design note, where it applies less.

**General or personal.** General as a pattern: one story above every feature,
build on one real person, write every feature as a general need, and check at
review that nothing only true for that person leaked to everyone. The person's
own data stays in the project and, as health-app shows, outside git.

### 5. Review rounds on the running product

Two different kinds showed up. Both were supplied by hand.

**a. Experience review of the running product.**
`<health-app>/docs/briefs/0004-review-round-1.md`: "our own review,
at the same depth as the design round, on the running app, then the fixes for
both his notes and ours". "Use your own simulator device, never the one he
uses". "Drive every journey ... Screenshot each step ... compare each with its
design render". Findings "group by journey. Start with the five that hurt the
story most. Mark anything that only the real phone can prove." Part B: "merge
them ... his notes first, his words kept". the desktop app 0485 adds "a look check: every
screen drawn and looked at by the reviewer, not only read in code".

**b. Code review rounds until a named reviewer signs off.**
`<desktop-app>/docs/standing.md`: "Code briefs run in rounds until a
staff reviewer signs off ... round after round, logged, until the staff
reviewer writes that it is fine to proceed". Sized per brief: "Small part: one
staff review round", "Medium part ... at most three rounds".

**Recurred.** "staff review" or "fine to proceed": 106 times in 69 desktop-app brief
files (Grep `staff (senior )?review|fine to proceed`, case insensitive, in
`<desktop-app>/docs/briefs`). Experience review on the running
product: health-app 0004, desktop-app 0475 and 0485 (by reading). The ship-ai director
"rendered every PDF page" before the person saw the deck
(`~/Personal/Repos/ship-ai/docs/standing.md`).

**General or personal.** General. After launch, desktop-app added a feedback ledger
(`<desktop-app>/docs/feedback.md`: "Give it the next F- number ...
The director checks each row, sets its severity and state, and plans it for a
numbered release"). Also general.

### 6. Dynamic and project roles

**Where and what.**

- the health app wrote four role files in `<health-app>/formwork/roles/project/`
  (ux-principal, behaviour-scientist, nutrition-scientist,
  training-scientist). Ship-ai wrote four (field-researcher,
  academic-researcher, content-writer, project-manager). Studio wrote none.
  the desktop app has no `<desktop-app>/formwork/roles/project/` folder at
  all (Glob returned no files).
- Far more specialists were made by relabelling a kit role inline, plus a
  skill. the health app 0001: "`researcher` (formwork), as iOS platform researcher",
  "`product` (formwork), as landscape researcher". the health app 0005: "Creative
  director | `visual`", "Motion designer | `ux` with `animate`,
  `review-animations` ... skills", "Apple reviewer | `reviewer` with
  `apple-design`". About 8 relabels across health-app 0001, 0002, 0004, 0005 (by
  reading).
- the desktop app invented its reviewers in each brief with no file: "a requirements
  engineer", "a product reviewer standing for the five user kinds", "the
  breaker ... whose only job is to invent new everyday scenarios", "a staff
  senior engineer who has the last word".

**Recurred.** In all 4 projects, in one of three forms: a written role file
(2 projects), an inline relabel with a skill (health-app), an invented reviewer
with no file (desktop-app).

**General or personal.** General as a mechanism. The roles themselves are
project content (a domain scientist for a health app belongs to that project).
The finding that matters: **the person did not need a new role file most of
the time**. He needed a new title, a sentence of ownership and a skill on top
of a kit role. A full five-section file paid off where the role carried a
"Would be wrong if" the kit role did not (the ux-principal's "a story that only
works in the happy path").

### 7. Usage awareness

**Where and what.**

- `<desktop-app>/docs/standing.md` line 177: "Usage rules for every
  thread from 2026-10-28 (his words ... 'why did we use 97% of my plan ... we
  are not optimizing in the threads and agents?')": "At most 3 threads at
  once"; models by kind of work, "the staff reviewer, who has the last word" on
  the strong one; "at most 3 review rounds, 2 reviewers a round"; "a thread
  reads standing's rules and decisions that apply to its stream ... not every
  design and report"; "Every brief says these four".
- Same file line 422: "paused for his usage limit (about 95% used)", with what
  was running and how to resume.
- Same file line 370: "queued to start by itself the moment 0480 reports (one
  Claude worker)".
- `<health-app>/docs/reports/0001-research.md`: "Token counts and
  spend were not observable from this session: NOT ESTABLISHED", and the
  search budget ran out mid round.

**Recurred.** 2 of 4 projects (desktop-app, health-app). In desktop-app the four rules were
then repeated in every brief, by its own rule.

**General or personal.** The pattern is general (a cap on parallel builders, a
cap on review rounds, reading only what applies, a summary at the end of each
lane file for cross reading). The numbers (3 threads, 3 rounds, which model) are
personal settings tied to a plan.

### 8. Release steps owned by another machine

**Where and what.**

- `<desktop-app>/docs/briefs/0463-signing-on-the-air.md`: "Runs on
  his [second machine], as a thread." 
- `<desktop-app>/docs/standing.md` line 401: the release session
  "releases only on a director line `release: go <version>` in standing, runs
  package, check, in-app install, R2 upload, update page, live checks, and
  pushes only a release record; tester emails stay his". Lines 404 and 405:
  it stopped twice and said exactly why, then shipped on the third go.
- `<health-app>/docs/reports/0003-build.md`: "To put it on your
  iPhone ... follow [the install guide] on your [second machine]".

**Recurred.** 2 of 4 projects.

**General or personal.** Personal, as the person said ("formwork itself is a
general repo"). The machine, accounts, keys, upload targets and steps stay in
the project. The only general piece is a pattern of four lines: a step owned by
another session; started by one written line from the person or the director,
never on a schedule; stops and says why at the first failing step; ends with a
release record in the repository.

### Gaps the idea file did not list

**9. Samples, then a stop for the person's pick.** the health app 0005: "Phase 1 ends
with ten pictures and stops for his yes". the desktop app 0485: "Draw 2 or 3 versions
... Then stop half 1 ... and wait for his pick". "his pick", "his yes", "stops
for his": 80 times in 54 brief files (Grep `his pick|his yes|stops? for
his|wait for his pick`, case insensitive, glob
`{health-app,desktop-app,ship-ai,studio}/docs/briefs/*.md`). General. This is the one
stop inside a design phase the person kept asking for.

**10. Running alone.** "Never stop to ask" (or "do not stop to ask"): 58 times
in 57 brief files (Grep `(never|do not|don't) stop to ask`, case insensitive,
same glob). the desktop app also has a full overnight mode
(`<desktop-app>/docs/standing.md` line 471: "never stops to ask him;
where a choice comes up it builds the recommended option and lists the choice
at the end ... uses no screen at all"). General.

**11. The person's live surface is off limits.** the health app 0004: "Use your own
simulator device, never the one he uses". the desktop app standing line 475: "When a
thread drives his real screen ... no typed keys at all to whatever app is in
front". "his simulator", "his device", "his screen", "his installed", "own
simulator", "never touch his": 129 times in 105 brief files (Grep with that
pattern, case insensitive, same glob). General: agents use their own instance
of whatever the person is using.

**12. The same project rules copied by hand into every project.** All four
`AGENTS.md` files carry the same block: "never in a worktree", "Standing has
one writer", "[the person] decides every fork", "For you", "near-black", "result:"
(Grep for those phrases over `{health-app,desktop-app,ship-ai,studio}/AGENTS.md`, 26
matches, the same rules on nearly the same line numbers in each). Some of these
are now in the kit (`result:` and `For you` appear in `formwork/templates/report.md`
and `formwork/roles/method/director.md`). The rest are the person's own
defaults. That is a personal layer, not kit content, but nothing carries it
today except copy and paste.

**13. Standing goes stale during phase work.** `<health-app>/docs/standing.md`
says under "What is next": "His review of the spec. Then brief 0001", while its
own decided list runs to brief 0005 phase 2. "Where we are now" lags too.
Phase work moves fast and writes many decided entries. The top sections are
not kept. (Whether `standing-current` would catch this: NOT ESTABLISHED; I did
not run it there.)

**14. Decisions lived in standing, not in decision files.** the health app has 0
decision files (Glob for markdown files in its docs/decisions folder found
none) against 15 dated
decisions in its standing. the desktop app has 3 decision files (name, character, look)
against about 300 dated standing entries (Grep `^- 20` count in
`<desktop-app>/docs/standing.md`: 300). In practice the cross phase
record is the standing's "What is decided" list, in the person's words.

### Summary table

| Gap | Projects | Count (search above) | Kit or project |
|---|---|---|---|
| Phase cycle | 4 of 4 | desktop-app 36 of 53 briefs are steps of one plan | kit |
| Research round shape | 3 of 4 | 6 briefs by reading | kit |
| Taste, both halves | 4 of 4 | "dead" 31, "AI slop" family 35 | kit packs (structure), project (look) |
| One story, user zero | 2 of 4 | by reading | kit pattern, project data |
| Review on the running product | 3 of 4 | 106 "staff review" lines in 69 files | kit |
| Dynamic roles | 4 of 4 | 8 role files, about 8 relabels | kit mechanism, project roles |
| Usage awareness | 2 of 4 | one rule block, repeated per brief | kit pattern, personal numbers |
| Release on another machine | 2 of 4 | by reading | project only; kit at most a pattern |
| Samples then pick | 2 of 4 | 80 in 54 files | kit |
| Runs alone | 4 of 4 | 58 in 57 files | kit |
| Live surface off limits | 2 of 4 | 129 in 105 files | kit |
| Copied AGENTS block | 4 of 4 | 26 matches | personal layer |

---

## P2. What a person building an app actually needs, ranked

Ranked by how many projects needed it and how often, and by what happened
when it was missing.

1. **A phase cycle with the person's gates in fixed places.** Spec read, then
   research, design (with a sample pick), build, own review beside the person's
   review, release on the person's word. Missing it, each project rewrote it,
   and the health-app standing went stale while the phases ran. 4 of 4 projects.
2. **Running alone between gates, with choices collected at the end.** Each
   choice with one recommendation, never a question as the last message. The
   person wrote this into 57 brief files. Missing it is the most common
   interruption complaint ("i dont want to get interrupted", health-app standing,
   first decision).
3. **The cheapest possible way to field a specialist.** A new title, one line
   of ownership, and a skill, over a kit role. A full role file only when the
   specialist has a failure mode the kit role lacks. Evidence: about 8 relabels
   did the work in health-app; desktop-app ran 204 briefs (count from the round
   briefing) with no role files.
4. **A taste pack that names both failures.** "Generic, AI made" on one side,
   "clean but dead" on the other. Per product kind. With the person's own look
   as a dated project setting. Missing the second half cost health-app a whole
   redesign round (brief 0005).
5. **Review on the running product by the team, on its own instance.** By
   journey, with pictures, the person's notes first and in his words, severity
   and "only the real device can prove it" marked. 3 of 4 projects.
6. **A rule that the person's live device, screen and installed app are off
   limits.** 105 brief files had to say it.
7. **A story gate.** One story above features, the user zero pattern, and a
   review question "what here is only true for user zero?". The miss is real
   (health-app findings item 4).
8. **Usage caps as settings.** Parallel builders, review rounds, reading
   scope. Asked for once, under pressure, and then repeated forever.
9. **After launch: a feedback ledger and a release record.** the desktop app needed both
   from its first tester wave.

### What would be overhead

- **Full paperwork for task sized asks.** the desktop app 0492 is a 39 line brief for
  sending one email. 0478 is 25 lines for replacing a link in drafts. A one line
  brief and a two line report would have carried both. The kit already says
  this (`formwork/roles/method/director.md`, Size the brief); a project layer
  must not undo it.
- **A role file for every specialist.** Most relabels did not need one. A rule
  that every spawned role must be a checked file would have added dozens of
  files to health-app for no gain.
- **Decision files per phase.** The person never wrote them for phase gates.
  His one word in standing was the record (health-app 0 decision files, desktop-app 3).
- **Scored stage gates or a gate committee.** Every real gate was one word or
  one pick from samples. A scoring sheet would be a form he would skip.
- **Fixed phase lists for kinds of work that do not need them.** Ship-ai had no
  build phase and no release; studio was a design note. A phase cycle forced on
  a course or a deck is overhead.
- **Kit defaults for taste values.** The person's taste changed mid project
  (desktop-app standing 2026-11-08). Any colour or glow rule in the kit would be
  wrong for him within weeks, and wrong for others at once.
- **Anything about his release machine in the kit.** His own words rule it out.

---

## P3. Understanding from one prompt, from the person's side

**How I counted brief sizes in desktop-app.** I read the `stream:` front matter of
every desktop-app brief from 0440 to 0492 (53 briefs; Grep `^stream:` in
`<desktop-app>/docs/briefs`), the bodies of 13 of them, and the
explicit size labels (Grep `(Small|Medium|Large|Big) part`, which found 11
briefs: 1 Small, 5 Medium, 5 Big). My sorting, by reading:

| Size (kit names) | Briefs 0440 to 0492 | Which |
|---|---|---|
| Task (one job, one result, no review round) | 8 | the 7 launch briefs (emails, links: 0476, 0478, 0482, 0483, 0486, 0491, 0492) and 0479 (the feedback list) |
| Checkpoint or round (build part or release fix, with review rounds) | 45 | 36 "design A build" parts, 7 release fixes, 0477, 0485 |
| Phase (answer is a document) | 0 | none in this window |

The phase that fed these 45 briefs was earlier: 0033 to 0041, nine director
briefs whose answers were documents (requirements, scenarios, facts, prior
art, designs, the build plan). So a rough picture: about one phase per 40 to 50
working briefs, and about one in six briefs is task sized. Across the whole of
desktop-app's history: NOT ESTABLISHED; I sampled one window.

What this means for the router: most of the person's prompts are not "build me
an app". They are "fix this", "go", "send it", inside a phase that already has
a plan. The router's most common job is placing a small ask inside an existing
phase, not starting one.

### Request 1: "build me an iPhone app for X"

**What the person wants said back, in one or two lines.** The size, the gates
and nothing else. For example:

> A new product. I will write a one page spec from your words and stop for you
> to read it. Then research, design (ten samples for your pick), build, and our
> own review beside yours, without stopping; release only when you say.

**What should happen without asking.** A new project with the standing page and
the spec draft. The phase plan written as briefs. The research lanes picked
from X (a domain scientist for a health subject, a platform researcher, a
landscape researcher, a story owner), made as relabels where a kit role fits
and as role files only where they need their own "would be wrong if". The
taste pack for the product kind switched on. The live device rule switched on.

**What must still stop for the person.** The spec read (health-app standing, first
decision: "let me review it, after i review it, i want team of researchers").
Forks only he can settle, collected at the end of each phase. The sample pick in
design. Anything that uses private data about him. Accounts, signing, money,
publishing. Git.

### Request 2: "fix this bug"

**Said back.**

> A task in the app's search: reproduce it, fix it, test it. One line brief.

**Without asking.** Reproduce, fix, run the project's checks, a short report.
Use its own instance, never the person's running copy (health-app 0004, desktop-app
0490: "Never touch his installed the desktop app").

**Must still stop.** Only for a real choice (security, money, behaviour that
changes what users see), and then as a recommended choice in the report, not a
question mid way. One escalation the router should offer on its own: when the
same area has been "fixed" several times. In desktop-app, F-016 was fixed, reopened
and refixed across 0484, 0487, 0488 and 0489
(`<desktop-app>/docs/feedback.md` and standing lines 382 to 397), and
earlier the person himself stopped a run of case by case fixes: "we are
handling case by case ... we need to reset the design" (desktop-app 0034). The
router should say "this is the third fix here; a design question may be under
it" once, and let the person choose.

### Request 3: "research Y"

**Said back.**

> A research round: four lanes in six parts each, one joined summary, a
> challenger, no code. Report when done.

**Without asking.** Lanes, sources, NOT ESTABLISHED where unknown, cross
reading, the integrator, the challenger. Generic search terms where the
subject is private (health-app 0001 report: "Web searches used generic terms
only").

**Must still stop.** Nothing until the report. His choices go at the end, one
recommendation each. If the round would read private material, say so in the
read back line before starting.

### Request 4: "make a deck"

**Said back.**

> A deck: words, design, build. I will show you the outline first, then run to
> the end.

**Without asking.** Draft the outline from the sources, run the deck skill, the
humanizer pass, render every page and look at it (ship-ai standing: "Director
rendered every PDF page").

**Must still stop.** The outline, once (ship-ai 0002: "on the outline below:
... english, go"). Then nothing until the finished deck, because the person
said so: "i dont want to be stopped in the middle ... show me the final slides
in the end". Name and audience details stop for him because they are his.

### How the person corrects a wrong read

From the evidence, corrections came in three shapes, all one line:

- **Size or stops.** "i dont want to be stopped in the middle" (ship-ai 0002).
  "no stops". The read back line should name the size and the stops, because
  those are the two things he corrected.
- **Meaning.** "no i didnt mean to remove the figures completely, i meant to
  draw them better" (health-app standing). "he took back the subscription check
  ins" (health-app standing). Recorded as a dated entry in his words, and the plan
  re-said in one line.
- **Direction.** "we need to reset the design, start all over again" (desktop-app
  0034). This one changes the phase, not the brief.

Words like "correction", "took back", "his change", "i didnt mean", "i meant",
"no i think" appear 27 times in 14 files (Grep with that pattern, case
insensitive, glob `{health-app,desktop-app,ship-ai,studio}/docs/{standing.md,briefs/*.md}`).
So corrections are routine, not rare. The cost of a wrong read must be one
reply.

What the person would not want: a confirmation question before every task. His
pattern is to accept the read silently by saying "go" and to correct only when
it is wrong.

---

## P4. The phase cycle as actually run in health-app

| Phase | Brief | What it produced | What ended it | Where the read-back sat |
|---|---|---|---|---|
| Spec | none (director, in standing) | the product spec, versions 0.1 to 0.3, from his words and answers | his answers on the spec and "go for the research" | standing, decided entries 2026-11-14 |
| Research | 0001 | 7 lane files in six parts, cross reading notes, `the-story.md` (12,301 words by `wc -w`, as the standing says), `challenge.md`, spec 0.4, seven forks | report with seven choices; then his fork decisions | standing: "research closed; his fork decisions" with his words; the report's "Accepted" section still says "Waiting for your read-back" |
| Design | 0002 | language, motion, flows (23), screens (53), accessibility, challenge, gallery, 82 renders of real code; then a taste pass after his review | his review ("generic, busy and AI looking"), the taste pass, then "finished, lets go buildinggg, start" | standing: "design closed, build started" with his words |
| Build | 0003 | the whole app, a relay, data libraries, 512 package tests, an install route on another machine | report; then "now comments ..." | standing: "review round 1 started"; 0003 closed by that entry |
| Verify | inside 0003 | `make test-kit`, `make boundaries`, a screen check against renders; UI tests written but never ran | not a separate phase | report section "Asked for but not done" |
| Review round 1 | 0004 | findings by journey (50 screenshots, counted by the report with ls and wc), his ten notes first, behaviour fixes | narrowed mid round when he asked for a redesign | standing: "0004 review round 1 reported", then his decision on one fork |
| Redesign round 2 | 0005 | concept on one page, ten samples, three motion strips, then the director's ten AI rules | his "yes, apply it with these rules" | standing: "phase 2 approved with the director's AI rules" |
| Release | not reached in health-app | install guide for another machine only | | |

What this shows:

- **Every phase ended on the person's next instruction, not on a written
  read-back.** The two lines the report template asks for were never written
  in health-app's reports (the 0001 and 0002 reports both say "Waiting for your
  read-back"; 0003 to 0005 have an empty "Accepted" heading). The briefs still
  say "done (accepted ...)". The real record is the standing entry quoting his
  next words.
- **Verify was not its own phase.** It lived inside build and was partly
  blocked (UI tests never ran, in 0003 and 0004). A project layer should treat
  "what could not be proven here" as a first class output of build, as health-app's
  reports already did ("Not proven until your phone").
- **Review rounds split.** Round 1 found behaviour and look problems together;
  the person split them into behaviour fixes (0004) and a redesign (0005) mid
  round. A review round template should expect that split.
- **The redesign came from the taste rules overcorrecting.** It was not a
  missing phase. It was a missing half of the taste pack.

---

## P5. Templates a project layer would need

Headings as the projects actually used them. Each one fits on a page.

**Spec** (from `<health-app>/docs/product-spec.md` and
`<desktop-app>/docs/briefs/0034-requirements-first.md`):

- Version line, with who changed what and which lane holds the evidence.
- In one paragraph.
- The first principle: one story, not a pile of features.
- Who it is for: user zero, made for many.
- Why it exists.
- The parts (features or components), each placed in the story.
- Constraints and values (data and privacy, look and feel, values and fit).
- Not in version 1 (non goals).
- Measurable qualities and must not happen (desktop-app 0034).
- How we will build it (the phases).
- The person's answers, and choices still open.

**Research round** (health-app 0001, ship-ai 0001):

- His words. The team table: lane, role, the question.
- Each lane file in six parts: question and why, theory, state of the art,
  what it means here, ranked proposals (evidence, cost, what it replaces; NEW
  marked), risks and unknowns. Plus a short summary for cross reading (health-app
  0001 report's own lesson).
- Rounds: parallel, cross reading, one integrator, challenger (predictions
  first), spec update.
- Report: the answer in five lines, choices with one recommendation each;
  disagreements and how each closed; the challenger's score; cost.

**Design round** (health-app 0002 and 0005, desktop-app 0039 and 0485):

- Team table: who, role, owns.
- What to design, as a numbered list in story order.
- Rounds: the language, the flows, the screens in real code rendered to
  pictures, review and challenge, a gallery.
- The sample stop: a concept on one page and a small set of samples, then stop
  for the pick. Phase 2 applies it.
- For architecture design (desktop-app 0039): two or three whole designs, walked
  through every scenario, scored against the requirements, a breaker,
  recommend one.
- Report: what it looks like, the pictures to see first, choices.

**Build** (health-app 0003, desktop-app 0441 to 0475):

- What version 1 is, numbered.
- Order of work.
- Team, split by what each owns, with files nobody shares.
- Review rounds sized to the part (desktop-app: Small, one round; Medium, up to
  three).
- Report: what works, how to open it, what is not done, what only the real
  device can prove; done but not asked, asked but not done, wrong in the brief.

**Review round** (health-app 0004, desktop-app 0475):

- Part A: on our own instance, drive every journey, a picture per step,
  compare with the design.
- Findings file: the person's notes first in his words; the five that hurt the
  story most; then by journey, each with picture, what is wrong, why it
  matters, severity (blocks, hurts, polish), status (fixed, next round, open,
  device only).
- Part B: fixes for his notes and ours together.
- Report: what was wrong, what is fixed, what to look at again.

**Release** (desktop-app 0480 to 0490, standing lines 401 to 406,
`<desktop-app>/docs/feedback.md`):

- Trigger: one written line naming the version.
- Steps as a list the release owner runs and stops at, saying why.
- A release record in the repository.
- The feedback ledger: ID, date, from, where, what happened, kind, severity,
  release, state. No names or addresses of testers.
- Anything that reaches people (emails, posts) stays the person's to send or
  approve.

---

## What I read

- This repository: `docs/rounds/whole-project-builds/brief.md`,
  `docs/briefs/0022-whole-project-builds.md`,
  `docs/ideas/2026-11-15-whole-project-builds.md`; searches in `formwork/`
  for taste, slop, usage, release and the report shape; `formwork/loop.md`
  (phase and milestone lines).
- the health app (`<health-app>/`): the product spec (sections 1 to 2 and 9
  to 13 in full; the rest by headings), briefs 0001 to 0005 in full, reports
  0001 to 0005 (the first 70 to 80 lines of each), the story (headings only),
  the director's AI check, the round 1 findings (first 50 lines), the four
  project roles, the standing page, AGENTS.md. I did not open the profile
  folder.
- the desktop app (`<desktop-app>/`): the standing page (the top 45 lines and
  lines 370 to 482, which hold the last entries and the standing rules, plus
  lines 177 to 188 for the usage rules), the feedback page (first 40 lines),
  briefs 0034, 0039, 0441, 0445, 0449, 0457, 0463, 0466, 0470, 0475, 0478,
  0485, 0490, 0492 (14 briefs), the stream line of every brief, and reports
  0457 and 0475 plus the headings of 12 reports from 0441 to 0492.
- Ship-ai (`~/Personal/Repos/ship-ai/`): briefs 0001 and 0002, report 0002
  (first 50 lines), standing, the project-manager role, the other three role
  names.
- Studio (`~/Personal/Repos/studio/`): brief 0001, report 0001 (first 40
  lines), the AGENTS.md match lines.

## What I could not establish

- Brief sizes across all of desktop-app's history. I sorted one window (0440 to
  0492). The share of task sized briefs elsewhere is NOT ESTABLISHED.
- The total count of desktop-app briefs. I used the round briefing's 204; only 66
  files match `^brief: ` and 70 lines match `^stream:` (Grep counts), so older briefs
  use another format.
- How many of the 31 "dead" matches are about taste rather than dead code.
  NOT ESTABLISHED exactly.
- The relabel count (about 8) is by reading, not by a search.
- Whether formwork's `standing-current` check would flag health-app's stale top
  sections. I did not run any check in another project.
- Token or plan usage per phase in any project. the health app's report says it was
  not observable; desktop-app records only the percentage the person saw.
- What the person would say back to a one line plan read. No project shows a
  router; every read back here is inferred from how he started and corrected
  briefs. That is an assumption about behaviour and belongs to
  `user-researcher` if it becomes load bearing.

## Response to the lead

**I yield on the cycle as a list of phases, and adjust it to two gates.** For
the order alone, the honest answer is "nothing, it saves typing". Studio's whole
cycle was one sentence (`~/Personal/Repos/studio/docs/standing.md` line 19), and
the director expanded it correctly. A fixed list is overhead for decks and notes.

Two failures a director expanding one sentence did not catch:

1. **Build started before the requirements existed.** In desktop-app the director's
   plan "grew by answering one case after another", and the person himself had
   to stop it: "we need to reset the design, start all over again"
   (`<desktop-app>/docs/briefs/0034-requirements-first.md`). A gate
   "no build brief until a spec or requirements page is accepted" catches this.
2. **Verify never closed.** the health app's UI journey tests were written and never
   ran, in 0003 and again in 0004, and both reports carried it as "not done"
   while the next phase started (`<health-app>/docs/reports/0003-build.md`
   and 0004). A gate "unproven items are listed and seen before the next phase"
   catches this. Neither gate catches "dead"; his own look did that.

New rank 1: running alone between gates (57 brief files). The cycle becomes two
checkable gates, with no fixed list of phases.

**Taste packs: I adjust to what survived every flip** (glow, colour and pills
flipped in desktop-app 2026-11-08, health-app 0002, health-app 0005):

1. **Decoration never poses as data.** Charts only from real numbers, no fake
   pictures (health-app director-ai-check rule 5; desktop-app 0475 "one truth").
2. **Copy says the thing, not the feature** (health-app rule 8; desktop-app 0475 "no
   unnecessary statements or wordings").
3. **Two questions per rendered screen:** "generic or AI made?" and "dead?"
   (health-app 0005 diagnosis; desktop-app 0485 look check). The look stays a dated
   project setting.
