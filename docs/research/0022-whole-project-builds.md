---
brief: 0022
date: 2026-11-15
by: lead, from a round of five
---

# Formwork for building a whole project: research and proposal

This is the full research for brief 0022. The argument behind it, attributed
role by role, is `docs/rounds/whole-project-builds/round.md`. The five
participant files are beside it. Nothing in the kit was changed.

## Contradictions first

1. **The kit's checks were blind to the practice that already happened.** This
   is the biggest finding, and the brief did not ask about it. In the health app the
   rounds ran with predictions, but in `docs/research/` and `docs/design/`,
   where `predictions-first` never looks, so it printed clean over nothing. Its
   standing brief still names brief 0001 as next while 0001 to 0005 ran, and
   `standing-current` printed "ahead of all 0 record(s)". the desktop app's "one open
   brief per stream" is broken now (engine 2, runner 3, app 5) and
   `open_briefs`, one global number set to 16, cannot see it. Sources:
   record-keeper and challenger, both checked against the files.
2. **"Had to say by hand, every time" is half true.** What he typed nearly
   every time was personal: run alone (155 of 218 briefs, all four projects)
   and his taste. The general method (the phase cycle) appears in all four
   projects too, but cost about one sentence per project, which the director
   expanded. Commands are in the round record.
3. **The brief's picture had two wrong facts.** the desktop app has 198 reports, not 310
   (the rest are attachment folders). Skills were not simply "dropped": 1.0.0
   ships `humanizer`. `docs/standing.md` says both things in two sections.
4. **Nobody wrote a one line brief.** Not in any of the four projects. the desktop app's
   shortest brief is 13 lines; brief 0492 is 39 lines for one email. The
   failure seen in practice is over building small asks, not under building
   big ones.

---

## 1. What is missing, with evidence

Each row: what he supplied by hand, where, how general it is. Counts come
from `docs/rounds/whole-project-builds/product.md` and `record-keeper.md`,
with their commands, except where the lead recounted.

| Supplied by hand | Evidence | Kit or project |
|---|---|---|
| Run alone between gates, choices at the end with one recommendation | 155 of 218 briefs, all four projects (lead's count) | kit, as a documented mode |
| Phase cycle (spec, research, design, build, review, release) | wording in all four projects; the health app spec section 12; desktop-app 0033 to 0041; studio "three briefs per idea"; ship-ai "words, design, build" | kit, as two gates and optional templates, not a fixed list |
| Research round shape (six part lane file, cross reading, one integrator, challenger, spec update) | the health app 0001; same lanes then integrator then cold challenger in the health app 0002, 0004, 0005, ship-ai 0001, desktop-app 0039 (by reading) | kit template |
| Samples, then a stop for his pick | 80 matches in 54 briefs | kit, inside the design template |
| Review on the running product, on the team's own instance, by journey, his notes first | the health app 0004; desktop-app 0475, 0485; desktop-app staff review rounds in 69 briefs | kit template |
| The person's live device, screen and installed app are off limits | 129 matches in 105 briefs | kit rule (advice) |
| One story above every feature; user zero, written as general needs | the health app spec 1b and 2; the health app review finding 4; desktop-app 0034 | kit template (spec) |
| Taste and anti AI slop, both halves | the health app director AI check; the health app 0005 "'Avoid AI slop' was read as 'remove life'"; desktop-app 0475 | kit: three items and a pack shape; project: the look |
| Project specialists | the health app 4 role files and about 8 relabels; ship-ai 4 files; desktop-app none, reviewers invented in each brief | kit: the mechanism; project: the roles |
| Streams in parallel with their own limits | desktop-app standing, seven streams with number bands | kit: per stream count; project: the streams |
| Usage limits | desktop-app standing line 177, after "why did we use 97% of my plan" | kit: a described pattern; project: the numbers |
| A release step on another machine | desktop-app 0463 and standing 401 to 406; the health app 0003 install guide | project only; the kit may describe a pattern |
| The same rule block copied into every AGENTS.md | 26 matches across all four | personal layer, not kit |

What a phase cycle in the kit would have caught that the director did not
(product, after the lead's challenge): build starting before requirements
existed (desktop-app 0034: "we need to reset the design, start all over again"),
and verify never closing (the health app's UI tests written and never run, in 0003 and
again in 0004, while the next phase started). Neither catches "correct and
dead". His own look at the running app caught that.

---

## 2. The proposal: what formwork becomes

### The options

| Option | Verdict | Why |
|---|---|---|
| (a) a project layer over the brief cycle | **rejected by all five** | a second process beside the one loop; a second owner of "what happens next" |
| (b) a pack of roles, templates and checks | **rejected alone, kept as a part** | a pack cannot route, and there is no switch, so it loads everywhere |
| (c) director and lead changes only | **the base of the recommendation, widened** | the director already owns sizing; routing is sizing plus a stream plus a team |
| (d) nothing | **rejected for the layer as a whole, kept as the challenger's dissent** | the failures above are real and already paid; the challenger still argues (d) for everything except the check brief |

### Recommended: beside, not over

Formwork stays one loop. It does not grow a product process. It becomes able
to do four things it cannot do today:

1. **See the structure projects already build.** Streams, rounds in their real
   folders, standing that has fallen behind. Checks first, because every
   participant, the challenger included, accepts this part.
2. **Understand one plain prompt.** A written routing table, the director as
   the only router above a task, a two line plan said back, corrections kept
   in the person's words.
3. **Field a specialist cheaply.** An existing role with a title and a skill
   first. A new role file only when no existing role owns the work.
4. **Offer optional shapes for big work.** Templates for a research round, a
   review round, a spec, a phase with gates, a release step; taste packs per
   product kind. Offered by size and kind. Never a required sequence.

A project that uses none of it behaves exactly as today.

### The centre: understanding from one prompt

**Where each piece of understanding lives.** One kind of fact per home.

| Home | Holds | Who writes it |
|---|---|---|
| The person's global CLAUDE.md | who they are, personal defaults (run alone, taste, how to talk), and at most one line: "in a project with FORMWORK.md, follow its routing" | the person |
| The project's AGENTS.md or CLAUDE.md | two lines, from a kit template: read `docs/standing.md` and the routing table, say the plan back, act on its size | installed once, offered by `formwork setup`, never written over a file |
| A routing table in the kit (proposed `route.md` under `formwork/`) | the general rules: kind of request to size, template, team, and the stops | the kit maintainer |
| `docs/standing.md` | this project's streams and the person's routing corrections (open question 1 below) | the director, transcribing |
| The director role | doing the routing for anything above a task | kit |

Hooks are not chosen per request. They are wired once at install. A hook that
injects the routing table at session start is possible on Claude Code
(superpowers does this, `hooks/hooks.json`, per the researcher) and is held as
a later option, because it binds on one runtime only.

**What happens to one prompt.**

1. **Kind.** Build a new product, change an existing one, fix, research, make a
   deck or document, or a question. Picked from a short, named list, never
   from dozens of role descriptions firing on their own. The researcher's
   sources show implicit skill selection collapsing as libraries grow (recall
   73.6% to 27.4% with 1,000 distractor skills) while explicit selection holds
   (73.9%): https://arxiv.org/abs/2610.18522, abstract only. Formwork's library
   is far smaller; routing accuracy at its size is NOT ESTABLISHED.
2. **Size.** The loop's own test (`formwork/loop.md`): could a reviewer accept
   one part and reject the next? Default task. Say the size in plain words and
   let the person override it, as superpowers brainstorming and BMAD
   `bmad-build` do (researcher, R3). Step up if it grows; never start big to be
   safe.
3. **Stream.** The live stream in standing, if streams are declared. A request
   for a stream whose gate is not met is said back as such, not started.
4. **Team.** Existing roles first. A relabel when the work needs a focus
   ("`visual` as creative director"). A new role only when no `owns` covers it.
5. **Template.** By size and kind: task none, checkpoint the six headings,
   round the round template, a phase the matching optional template.
6. **Checks.** Always `formwork check`, whole. Never chosen per request.
7. **Say it back.** Then act on the size:
   - **A task:** one line said back, then done, by the session that got it,
     with a one line brief. No "Go?". The person corrects only when it is wrong
     (product: his pattern is to accept silently).
     *Example:* "Task in search: reproduce, fix and test the empty result bug.
     One line brief."
   - **Above a task:** two lines, then the director writes the brief and stops
     with its fixed sentence. Inside the brief, the work runs alone until the
     report, with choices collected at the end.
     *Example:* "Milestone, new product: a one page spec from your words, then
     you read it. Then research, design with samples for your pick, build, our
     own review beside yours, without stopping; release only when you say."

**How it stays right as the project grows.**

- Corrections are stored, never remembered. A dated pair, the same shape as
  the read-back, transcribed word for word:

  ```
  routed: 2026-11-20
  in my words: bugs in the island are tasks, never rounds
  ```

  Append only. The person cuts them; the director never edits one.
- When a phase closes, the director updates the streams in the same turn it
  updates the rest of standing. "A stream's gate opened" joins its list of when
  to update.
- A brief naming a stream that is not declared fails the check, so the
  declaration cannot fall behind the briefs.
- A correction that recurs across projects becomes a kit brief that changes
  the routing table. Never a copy of anybody's words into the kit.
- **Measured before it is claimed.** A small set of should and should not
  prompts (fix a bug, build an app, research, a deck, a question) with the
  expected size and team, run with `claude plugin eval` and a `tool_used`
  grader (https://code.claude.com/docs/en/plugin-evals, researcher). Nobody has
  done this for formwork. Until somebody does, the router's accuracy is NOT
  ESTABLISHED and the kit says so.

**How it avoids over building a small ask.**

- A brief with no `size:` line counts as a task. A task over a line ceiling
  fails the check until it states its size (record-keeper). A one line brief
  carries no extra field.
- A working session may do a task without the director at all. It may only
  route down: anything bigger is said back and handed up, never briefed by it.
- The director's existing rule stays the default: "If you cannot tell which,
  ask one question. Do not pick the biggest one to be safe."
- What no check can do: tell that a small ask was born large. Said plainly so
  nobody believes a check is watching it.

### Phases and gates

A phase is the loop's existing "phase" size. It is a label on a run of
ordinary briefs, using the `stream:` field that all four projects already
write (health-app 5 of 5, ship-ai 2 of 2, studio 1 of 1, desktop-app 66 of 204). A
milestone is the direction above the streams. No new process.

A gate is a start condition a program can evaluate. Three forms only
(architect):

```
starts: now
starts: after <stream>        every brief there done with its read-back
starts: decision NNNN         that decision record exists
```

A gate in prose is decoration. The read-back is the key, because it is
already what he does: the health app 0002's `in my words:` line is "finished, lets go
buildinggg, start" (record-keeper). How short it may be is
`read_back_words`, which exists.

Two gates are recommended as the default for a build, each with a real case
behind it (product): **no build brief before a spec or requirements page is
accepted**, and **unproven items listed and seen before the next phase
opens**. No fixed order of phases. the health app ran review 0004 and redesign 0005
together, and a linear gate would have refused how he worked.

Phase rounds go in `docs/rounds/<stream>-<name>/`, where the checks look. Or
the check learns to find them where they are. Either fixes the health app's blind spot.

### Templates

All optional, in `formwork/templates/`, each one page. Headings are the ones
the projects actually used (product, P5).

| Template | Holds |
|---|---|
| spec | one paragraph; one story above every feature; who it is for, user zero made for many; the parts placed in the story; constraints and values; not in version 1; must not happen; how it will be built; his answers and open choices |
| research round lane | the six parts (question and why, theory, state of the art, what it means here, ranked proposals with evidence and cost, risks), plus a 20 line summary for cross reading (the health app 0001 report's own lesson); then cross reading, one integrator, a challenger, a spec update |
| design round | team table; what to design in story order; the sample stop (a concept on one page and a few samples, then stop for the pick); for architecture, two or three whole designs walked through every scenario |
| build | what version 1 is; order; team split by files nobody shares; review rounds sized to the part; report with what works, what is not done, what only the real device can prove |
| review round | part A on the team's own instance, every journey, a picture per step; findings with his notes first in his words, then by journey with severity; part B fixes both together |
| release step | the general pattern only: another session owns the step, one written line starts it, never a schedule; it stops and says why at the first failing step; it ends with a release record. No machine, account or device named |

### Dynamic roles

Three tiers, cheapest first (architect after challenge, product):

1. **Relabel.** The lead spawns an existing role with a title line and,
   optionally, a skill. Its owns, sections and tool grant still come from its
   checked file. No file, no STOP. the health app used about eight of these.
2. **New project role.** Only when no existing `owns` covers the work (the health app's
   scientists; about four per project). The director drafts it in the brief in
   the five section format; the person's go accepts it; a working session
   writes it to the project roles folder and runs `formwork roles` and
   `formwork check`; then the lead may spawn it. The director cannot write it
   itself: a role file with no generated copy turns `generated-current` red,
   and the director has no `run`.
3. **Never:** a pasted persona, a general agent given a role body in a prompt.
   Its boundary and tools are unchecked.

Checks that hold it: `role-shape` as today (five sections, four fields, unique
`owns`, only lead spawns); a round participant file must be `<role>.md` or
`<role>-<label>.md` for a real role; a role named in a brief's team table must
exist. A template line: a role that touches plans or order names the director
and lead under "Does not own" (ship-ai's project manager shows why).

Generated roles stay in the project. The project roles folder is never synced
in either direction. Promoting one into the kit is a kit brief that rewrites
it with no person, product or machine in it, never a copy.

Whether a role written mid session can be spawned in that same session: NOT
ESTABLISHED on any runtime. If not, adding a role is its own task brief.

This answers an open question in `docs/standing.md`. That is his to decide.

### Taste packs

Optional, per product kind, named by a project and overridden by it, never a
kit default for the look. Three items survived every change of his taste
(product, after challenge), and are the only content that belongs in the kit
from the evidence:

1. Decoration never poses as data. Charts only from real numbers, no fake
   pictures.
2. Copy says the thing, not the feature.
3. Every rendered screen gets two questions: "generic or AI made?" and
   "dead?". Clean is not the same as alive.

Pack shape (researcher): each item says what it catches and how it is
detected, high (a pattern a check could grep), medium, low (needs eyes), after
the gstack design checklist
(https://raw.githubusercontent.com/garrytan/gstack/main/review/design-checklist.md).
The project's own design file always wins, as in Anthropic's
`frontend-design` skill and gstack. A writing pack already half exists in
`humanizer`. Packs for web and deck can start from public sources; an iOS
pack needs Apple's guidelines read properly (the fetch failed: NOT
ESTABLISHED). Taste is never a check. It is a review round on pictures.

### The checks

| Check | Catches | Breaks it | Cannot tell |
|---|---|---|---|
| `predictions-first`, widened | a round held outside `docs/rounds/` | a predictions file beside lane files in `docs/research/` | rounds named otherwise; whether predictions were good |
| `standing-current`, widened | standing older than the newest brief or report | the health app's case: five reports newer than standing's next step | whether the text is true |
| `work-paired`: size | a task brief over the line ceiling with no `size:` | a 22 line brief with no size | a small ask born large |
| `work-paired`: streams | a `stream:` not declared; too many open in one stream; a brief opened before its gate | desktop-app's three overfull streams | whether the stream was the right one |
| roles named exist (new, small) | a team table or round file naming a role with no file | `creative-director` with no file and no base role | whether the right role was picked |
| kit leak scan (new, small) | home paths, private addresses, local hostnames, emails in kit files | a real looking home path in a kit page | a machine named in plain words. Patterns stay generic; a list of anybody's machines would itself be the leak (`docs/dogfood.md` entry 8) |

Refused: a taste check, a review content check, a linear phase order, any
check that judges the router's choice, any usage meter.

### Usage awareness

A described pattern only. The lead's existing lever ("how many turns each
one gets") plus a line in a big brief stating how many builders run at once.
Claude Code exposes five hour and seven day usage percentages to the status
line (https://code.claude.com/docs/en/statusline, researcher); nothing acts
on them, and it is one runtime. No tool tracks concurrent agents against plan
limits: NOT ESTABLISHED. The numbers are personal and stay in projects.

---

## 3. What stays out

Formwork is a general repository. These stay in projects, or in the person's
own global file, and never reach the kit:

- any release machine, how it is reached, its signing, upload targets and steps
- accounts, emails, device names, simulator names, app identifiers
- the person's taste values: colours, fonts, glow, the ground colour
- usage numbers tied to one plan (three threads, three rounds, which model)
- project roles, which name products and people
- the rule block copied into every AGENTS.md (his personal defaults)
- any word list of private names; generic patterns only

The kit may describe the general shape of a release step and of usage limits,
in a few lines, naming nothing.

---

## 4. How it would be built

Smallest useful first. Each is one brief.

1. **The checks see where projects work.** Widen `predictions-first`,
   `standing-current` and `open_briefs` (per stream), each with fixtures made
   from the real shapes, written generically. Fix the COSTS.md count. Nobody
   in the round objects to this one, the challenger included. It needs no
   decision.
2. **The kit leak scan.** Generic patterns, fixtures, over kit files only.
3. **Routing.** The routing table page, the director change, the two line
   plan back, the project instruction template, implicit task size with the
   ceiling, two optional standing headings. Needs his answers to open
   questions 1 and 2 first.
4. **Measure routing.** The should and should not prompt set, run once, the
   result written as a number with its command. Until then the routing page
   says NOT ESTABLISHED.
5. **Roles.** The relabel rule in the lead, the participant and named role
   check, the template line. Needs his answer to open question 3.
6. **Optional templates and gates.** Spec, lane, design, build, review round,
   release step; the three `starts:` forms.
7. **Taste packs.** The three items, the pack shape, web and deck first.

Whether any of this starts before 1.0.0 is published is his call (open
question 5).

## Open questions for him

1. Streams and routing corrections: two headings in `docs/standing.md`
   (architect, and the lead's recommendation), or a separate durable file
   (record-keeper).
2. Does the director take on routing? The challenger says no: it fixes none
   of the observed failures. Declining it means declining the "most important"
   requirement.
3. May roles be created mid project, and by the path above?
4. Does the kit ship a template for a person's own defaults, or leave it to
   their global CLAUDE.md?
5. Before or after publishing 1.0.0?

## Sources

Other tools, all from the researcher's file, which gives the full list and
says for each whether it read the file itself or went through a fetch:
Stage-Gate https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/;
Design Sprint https://www.gv.com/sprint/; Shape Up
https://basecamp.com/shapeup/0.3-chapter-01; Double Diamond
https://www.designcouncil.org.uk/our-resources/the-double-diamond/; dual track
https://www.svpg.com/dual-track-agile/; Claude Code
https://code.claude.com/docs/en/sub-agents, /skills, /hooks, /agent-teams,
/statusline, /plugin-evals; Kiro https://kiro.dev/docs/specs/ and
https://kiro.dev/docs/steering/; AutoBuild
https://microsoft.github.io/autogen/0.2/blog/2023/11/26/Agent-AutoBuild;
CaptainAgent https://classic.docs.ag2.ai/latest/docs/blog/2024/11/15/CaptainAgent/;
Agent Framework
https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview;
routing papers https://arxiv.org/abs/2610.18522 and
https://arxiv.org/abs/2603.22455 (abstracts only); gstack checklist above;
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing. Repositories read
from tarballs at the HEADs listed in the researcher's file: spec-kit,
BMAD-METHOD, superpowers, anthropics/skills, agent-os, claude-task-master,
MetaGPT, ChatDev, autogen, gstack.

The four projects, read only, method quoted, no personal or health content:
`<health-app>`, `<desktop-app>`, `~/Personal/Repos/ship-ai`,
`~/Personal/Repos/studio`. the health app's profile folder was never opened.

NOT ESTABLISHED: routing accuracy at formwork's size; whether a role made mid
session can be spawned in it; Apple's guidelines; plan limits; what a round
costs in money; whether any surveyed tool improves outcomes.
