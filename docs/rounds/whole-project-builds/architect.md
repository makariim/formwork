---
date: 2026-11-15
---

# Architect: where a project layer fits

Round 0022, whole project builds. Questions A1 to A6.

## The contradiction first

The briefing asks where a "project layer" fits over, under or beside the kit.
The evidence says the layer already exists, three times, built by hand and
built differently each time, and the kit's checks cannot see any of it.

- The health app, ship-ai and this kit's own brief 0022 all carry a `stream:` line in
  brief frontmatter (`<health-app>/docs/briefs/0003-build.md` says
  `stream: build`; `~/Personal/Repos/ship-ai/docs/briefs/0001-the-roadmap.md`
  says `stream: course`; `docs/briefs/0022-whole-project-builds.md` says
  `stream: method`). No check reads it. No file declares which streams exist.
- The desktop app declares streams in a table in `<desktop-app>/docs/standing.md`
  ("How the work is organised"): each stream has a page, a brief number range
  and a start condition, for example that the visual identity and the
  engine design must both be settled first. It also invented "one open brief per stream",
  which the kit cannot express: `open_briefs` in `work-paired` is one number for
  the whole project.
- The health app ran its phase rounds in `docs/research/`, `docs/design/round-2/` and
  `docs/review/round-1/lanes/`, not in `docs/rounds/<name>/`.
  `formwork/check/checks/predictions-first` only looks under `docs/rounds/`
  (its `ROUNDS` constant), so every one of the health app's rounds was invisible to the
  one check that guards rounds.

So the question is not whether to add a layer. It is whether the layer that
people keep building by hand gets one declared home and a check, or stays in
the director's head and in each brief, which is where the idea file says it
lives today.

---

## A1. Over, under or beside

### The four options, judged by who decides

**(a) A new project layer over the brief cycle.** A "project" or "product"
process above the director, with its own phases and its own owner.

Rejected. The director already owns "what happens next"
(`formwork/roles/method/director.md`, Owns). A layer above it either takes that
fact away from the director, or holds a second copy of it. Both are the
authority failure this role exists to catch. It already happened once in
miniature: ship-ai's project-manager role owns "the plan: phases, milestones,
the session calendar" (`~/Personal/Repos/ship-ai/formwork/roles/project/project-manager.md`)
while the director owns what happens next. `role-shape` passed it, because the
slugs differ (`course-plan` against `what-happens-next`). The check compares
slugs, not meaning. A whole layer built that way would be the same overlap at
the scale of the method.

It also breaks the kit's own sentence in `formwork/loop.md`: "These are names
for how big a turn was. They are not five different processes." A phase layer
with its own cycle is a second process.

**(b) A pack of roles, templates and checks.** Ship the specialists (creative
director, scientist, motion designer) and phase templates, and let people use
them.

Rejected as the answer, kept as a part. A pack cannot route. It is a shelf.
Nothing in a pack decides that "fix this bug" is a task and "build me an app"
is a milestone. There is also no switch for packs (`FORMWORK.md`, Your team:
"There is no switch yet"), so a larger role library is more always-on roles.
And `docs/design.md` section 5c already labels the existing 21 pack roles "a
guess" that should be cut down, not grown. Shipping domain specialists is that
guess again, bigger.

**(c) Director and lead changes only.** Teach the director the phase cycle and
the routing, teach the lead to make roles.

Rejected alone. It puts general rules in the right place and project specifics
in the wrong one. The director's file is a kit file, synced into every project.
"This project has a research, design, build and review cycle and a nutrition
scientist" cannot live there. If there is no project file, it lives in the
director's conversation, and that is exactly the failure `formwork/threads.md`
describes under "Where this used to break": a planning layer with no file.

**(d) Nothing.** The kit stays as it is.

Rejected, on the evidence above. Three projects needed the same structure and
built it three ways. Because none of the three ways is declared, the kit's
checks are blind to all of them. That is the cost of doing nothing, and it is
already being paid.

### Recommendation: beside, as one project file plus (c), with a thin pack

The shape, in one sentence: **the brief cycle is unchanged, the director stays
the only router, and the project's own shape lives in one project-owned file
beside `docs/standing.md`, which the director reads and a check holds the
briefs to.**

- **Beside, not over.** The project file is a sibling of the standing brief.
  It is read by the director, the same way the standing brief is. It is not a
  new process and it has no owner of its own.
- **(c) for the general rules.** How to route a request, how to plan it back,
  how a role gets made: kit text, in one kit page and in the director and lead.
- **A thin pack for the optional parts.** Phase templates and taste
  checklists, as kit files a project points at, never as roles that load.
- **Optional by absence.** A project without the file behaves exactly as today.
  Studio has one brief and ship-ai has two. They should pay nothing.

Why this one: it gives every important fact one home (A2), it adds one field
and one check rather than a process, and it is the shape the three projects
already converged on by hand, made visible.

**What would make it the wrong shape.** If a third project, run with the file,
never fills in its streams, or fills them and then ignores them in its briefs,
the file is ceremony and the right answer was (c) alone. That is checkable
after the fact: count briefs whose `stream:` is set against briefs where it is
blank. NOT ESTABLISHED today, because no project has run with the file.

---

## A2. What is fixed and what is generated

### The rule

**The kit owns the shape. The project owns the content.** A fact about how
formwork works is a kit file and is synced. A fact about this project is a
project file and is never synced over.

### How it maps to the existing sync rules

`formwork/sync` already draws this line, and the proposal needs no new
mechanism, only discipline about where files go:

- It copies every file under `formwork/` and `FORMWORK.md`, and deletes kit
  files the kit no longer has (`KIT_PATHS`).
- It never touches the project's SOURCE.txt and the project roles folder
  (`HUB_ONLY`), nor anything in `.formwork.toml` under `[bindings]` as
  `local = [...]`.
- It never touches anything outside `formwork/` at all. So everything under
  `docs/` is the project's by construction.

| Thing | Owner | Where | Synced |
|---|---|---|---|
| The routing table (how a request becomes a size, a stream, roles) | kit | a new page under formwork/, see A6 | yes |
| Director and lead rules for routing and making roles | kit | `formwork/roles/method/` | yes |
| The shape of the project file, phase brief, lane file, review round, spec | kit | `formwork/templates/` | yes |
| Taste packs per product kind | kit | a new folder under formwork/, see A6 | yes |
| The check that holds briefs to declared streams | kit | `formwork/check/checks/` | yes |
| This project's kinds of work, streams, gates, roles in use, taste pack, routing corrections | project | docs/project.md | never, it is outside formwork/ |
| Optional per stream pages, when streams run in parallel | project | docs/streams/ | never |
| Generated roles | project | formwork/roles/project/ | never, `HUB_ONLY` |
| The pointer in the project's instruction file | project | AGENTS.md or CLAUDE.md | never |
| A project's own taste rules beyond the pack | project | inside docs/project.md | never |

### Three structural traps found while mapping this

1. **Project checks have no safe home.** The runner reads
   `formwork/check/checks/`, which is a kit path. A project that adds a check
   there loses it on the next sync unless it lists it under `[bindings] local`.
   And `.formwork.toml` is on the protected list in
   `formwork/guard/protected-files`, so an agent cannot add that line. That is
   correct (the human decides what is local), but it means a project check is
   a human step every time. The proposal does not need project checks. If one
   is ever needed, the fix is a second excluded folder like the roles one, in
   both `HUB_ONLY` and the runner. Not now.
2. **The project roles folder must stay flat.** `formwork/build` reads it with
   `os.listdir` (`read_roles`), so a role in a subfolder is never generated.
   `role-shape` walks it with `os.walk`, so the same role is checked. A role
   that is checked and never generated exists for the gate and not for the
   runtime, and nothing says so. Rule: one level, no subfolders per stream.
3. **The project file cannot go in `.formwork.toml`.** That file has exactly
   two sections, `config-shape` refuses a section the kit does not document,
   and the guard protects the file from the agent. A `[project]` section would
   be configuration that changes behaviour, written where the person who
   corrects the router cannot easily write. Rejected; see A4.

### What is derived, and what is not

Nothing in this proposal is derived. docs/project.md is authoritative for the
project's shape: delete it and it cannot be rebuilt from the briefs, because
the start conditions and the person's routing corrections are only there. The
taste packs are not copied into the project, the project names one and lists
its own differences. So there is no copy to drift. **One fact, one home**, the
same rule `formwork/round.md` states for the round record.

---

## A3. The phase model as structure

### Fit it to the sizes the loop already has

`formwork/loop.md` names five sizes. The proposal gives the last two a place
to live and invents nothing beside them.

| Loop size | What it already says | Where it lives in this proposal |
|---|---|---|
| task | one line | a brief, as today |
| checkpoint | six headings | a brief, as today |
| round | a question per role | `docs/rounds/<name>/`, as today |
| phase | "a question big enough that its answer is a document" | one stream entry in docs/project.md, with the document it settles |
| milestone | "a direction. It contains phases" | the top of docs/project.md: what this project is heading for, and the ordered streams under it |

A phase is not a new kind of work. It is a **label on a run of ordinary
briefs**, plus the document that run settles, plus the condition for starting
the next run.

### Where phases are declared

In docs/project.md, one entry per stream. The minimum an entry holds:

```
## Streams

### research
settles: docs/research/the-story.md
starts: now

### design
settles: docs/design/language.md
starts: after research

### build
starts: after design

### review-1
starts: after build
```

Parallel streams, the desktop app's case, are the same entry with a different start
condition (`starts: now` on several). A brief number range per stream, which
The desktop app used to stop threads colliding, is optional; the kit's own
`work-paired --next` already prevents collisions in one folder.

### How a brief knows its phase

The `stream:` frontmatter line, which three projects and this kit already
write. **This is the one decision in the proposal that is hard to reverse**:
the field name accumulates across hundreds of briefs (the desktop app has over two
hundred). So spend care here and nowhere else. Use `stream:`, not a new
`phase:` field, because it is already in use and because the desktop app's streams are
parallel areas, not phases, and the same word covers both. A phase is a stream
that starts after another one.

### What a gate is, mechanically

A gate is a start condition a program can evaluate. Three forms, and only
three:

- `starts: now`
- `starts: after <stream>`: every brief in that stream is `done` or `dropped`,
  and every `done` one carries its read-back
- `starts: decision NNNN`: that decision record exists in `docs/decisions/`

**A gate written in prose is decoration.** The desktop app's "when identity has picked
the look" was a real gate, and it was only true in the human's head. In this
model it becomes `starts: decision NNNN`, where the decision records the pick,
or `starts: after identity`. The human's read-back on the last report of the
earlier stream is what opens the next one. That is what the health app actually did:
brief 0003 is `status: done (accepted 2026-11-15)` and the build brief starts
from the person's words "finished, lets go building"
(`<health-app>/docs/briefs/0003-build.md`). The gate is the STOP the
kit already has, at the end of a phase instead of a task.

The check refuses a brief that is `open` or `done` in a stream whose start
condition is not met. It reuses `work-paired`'s reading of status and
read-back rather than parsing them a second time, the same way `work-paired`
reuses `quality-gate`'s settings reader.

### Where phase rounds live

In `docs/rounds/<stream>-<name>/`, never in a folder named for the phase.
That one placement rule is what brings the health app's rounds back under
`predictions-first`. The document a phase settles lives wherever docs/project.md
says (`settles:`), and the round folder holds the argument. That is the split
`formwork/round.md` already makes between `round.md` and the report.

---

## A4. Understanding from one prompt

This is the overlap with the product role. I look at it as structure: where
each piece of knowledge lives, which role acts on it, and what fails quietly.

### Which role routes

**The director, and only the director, for anything above a task.** It already
owns sizing the brief ("Size the brief to the work", `director.md`). Routing a
request is sizing it, labelling it with a stream, and naming who works on it.
That is the same fact, so it gets the same owner.

**A working session may route exactly one way: down.** If a plain request
lands in a working session and it is task sized by the loop's test, the session
saves it as a one line brief and does it. That is already allowed
(`formwork/threads.md`: "the working session saves the brief it was given").
If it is bigger, the session writes nothing but the plan back and the sentence
"this is a phase in stream design; it needs the director". It never writes a
brief above a task. So the director keeps every brief that is worth reviewing,
and a one line fix never costs two windows.

**The lead never routes.** It receives a brief that already says "lead, with
these roles" and spawns. **The director never spawns and never builds.**
Nothing here changes either rule.

### Where the routing knowledge lives

Five candidate homes. Each holds one kind of fact, or nothing.

| Home | Holds | Why |
|---|---|---|
| The person's global instruction file | at most one line: "in a project with FORMWORK.md, a plain request goes to the director first" | it is personal and machine specific, it is outside every repository, and a rule kept there drifts from the kit with nobody seeing it |
| The project's AGENTS.md or CLAUDE.md | two lines pointing at the director, docs/standing.md and docs/project.md | it is what the runtime loads every session, so it is the trigger. Nothing more, or it becomes a second copy |
| A router skill | nothing | skills are generated for Claude Code only (`SKILL_TARGETS` in `formwork/build`), and "skills per role" were planned and dropped (`docs/standing.md`). A skill holding the table would be a second copy that exists on one runtime |
| A kit page, the routing table | the general rules: request to kind, size, stream, roles, templates, checks | general, synced, readable by both the director and a working session. One home, two readers |
| docs/project.md | this project's specifics, and the person's corrections | the only home that is both project owned and survives the window closing |

Note the general finding behind the first row: the kit writes **no**
instruction file into a project (no match for AGENTS.md or CLAUDE.md under
`formwork/` or `formwork_cli/`, by grep). So today the entry point a runtime
reads every session belongs to nobody, and people fill it by hand, often by
restating the director's rules in their global file. That restated copy is the
drift. The proposal gives the kit a two line template for the project's
instruction file and keeps the rules themselves in one kit page.

### What decides each part of the plan

Read in this order. A later source never overrides an earlier one.

1. **The person's routing corrections** in docs/project.md.
2. **docs/standing.md**: what is open now, what is next.
3. **docs/project.md**: which streams exist, which is live, which gates are
   met, which roles exist, which taste pack applies.
4. **The kit's routing table** for everything not said above.

| Part of the plan | Decided by |
|---|---|
| kind of work (fix, build, research, deck) | the request's words against the project's declared streams, else the table |
| size | the loop's split test (`formwork/loop.md`, "Where the size comes from"). Default task. Up only when a reviewer could accept one part and reject the next |
| stream and phase | the live stream in docs/project.md whose gate is met. A request for a stream whose gate is not met is said back as such, not quietly started |
| roles | existing roles first. A new role only when no existing `owns` covers the work, and then drafted in the brief (A5) |
| templates | by size: task none, checkpoint the six headings, round the round template, phase the phase template |
| checks | always `formwork check`, whole. Never chosen per request |
| hooks | never chosen per request. They are wired once at install and are fixed for the project. A router that switched guards per request would be configuration that changes behaviour, which is the thing `FORMWORK.md` refuses for rules |

### How it says the plan back

Two lines, a fixed shape, before any brief is written:

```
<size> in <stream>: <what it produces, one clause>. <what would show it failed>.
<who>: <one session | lead with roles A, B; new role C drafted>. Go?
```

For example: "Task in build: the login timeout fixed in one file. Fails if the
slow path still takes four seconds. One working session. Go?" And: "Phase in
design: the visual language, settling docs/design/language.md. Fails if the
challenger's predictions hold. Lead with ux, visual and a new motion role
drafted in the brief. Go?"

**The person's "go" is the STOP.** "And runs it" in the brief means: after go,
the director writes the brief and ends with its fixed sentence; the working
session runs it. Nothing runs before go. That is the kit's one rule kept, not
relaxed.

### How a person corrects it, and where the correction is stored

When the person says "no, island bugs are tasks, never rounds" or "always use
the scientist on food questions", the director transcribes it, word for word,
into docs/project.md:

```
## How work here is routed

routed: 2026-11-15
in my words: bugs in the island are tasks, never rounds
```

The same two line shape as the read-back in `formwork/templates/report.md`,
and the same rule: **the director transcribes, it never authors.** A routing
rule the director wrote in its own words is a decision nobody made.

Why here and not elsewhere: it is project owned (never synced over), it is a
plain file the person can edit, the director reads it first every
conversation, and `.formwork.toml` is protected from the agent and is the wrong
layer anyway.

### How it stays right as the project grows

- **When a phase closes**, the director updates the stream entries, in the
  same turn it updates `docs/standing.md`. It already has a list of when to
  update the standing brief; "a stream's gate opened" joins it.
- **A brief naming a stream that is not declared fails the check.** So the file
  cannot fall behind the briefs without the gate going red. That is the
  `standing-current` idea applied to the project's shape.
- **Corrections accumulate and get cut.** Same rule as the standing brief: cut
  before you add. A correction that the kit table now covers gets deleted by
  the person.

### How it keeps a task to a one line brief

- The table's default is task. It moves up only on the loop's split test, and
  the director's existing rule applies: "If you cannot tell which, ask one
  question. Do not pick the biggest one to be safe."
- A working session can do a task without the director at all (above).
- A declared stream never forces a size. A one line fix in the build stream is
  a one line brief with `stream: build` in it.
- **Nothing mechanical can check that the size was right.** A check that judged
  size would pass for the wrong reason. The protection is the default, the one
  question, and the person's corrections. Said plainly so nobody believes a
  check is watching it.

### What fails quietly here

- **The trigger line is missing** from the project's instruction file. Then a
  plain request goes straight to whatever session is open, and the routing
  never runs. Nothing goes red. A check could look for the pointer when
  docs/project.md exists; cheap, and worth it.
- **The router reads a stale project file.** Covered by the undeclared stream
  check only for names. A stream declared and abandoned stays green.
- **Corrections the director paraphrased.** The check can require the dated
  two line shape. It cannot tell who typed it, the same limit `work-paired`
  states about the read-back.

---

## A5. Dynamic roles

### Who writes them, and when

The open question on record (`docs/standing.md`, What is open: "Whether the
`lead` may invent a role") has a structural answer: **the lead does not invent
roles. The director proposes them, the person's go accepts them, a working
session writes them, the check holds them, and only then does the lead spawn
them.**

Why each step sits where it does:

1. **The director drafts the role inside the brief**, five sections in a
   fenced block. Proposing who works on what is planning, and it is visible to
   the person before go.
2. **The director cannot write the role file itself.** Found by reading:
   `generated-current` runs `formwork roles --check`, which reports a role
   source with no generated file as "missing" and exits 1. A director that
   writes a role file turns the aggregate red, and with `aggregate_gate =
   block` the turn-end gate refuses its turn. The director has no `run`, so it
   cannot regenerate. That is not a bug to route around; it puts the write
   where the run is.
3. **The working session writes the file** in the project roles folder, runs
   `formwork roles` and `formwork check`. The lead cannot do this either: its
   grant is read, write and spawn, no run.
4. **The lead spawns only a role that exists as a generated file.** Never a
   persona pasted into a spawn prompt. A pasted persona has no checked
   boundary, no unique `owns`, and on Claude Code it runs with the general
   agent's tools rather than its own grant. It is the widest grant wearing the
   narrowest description, which is the failure the comment in `formwork/build`
   describes for an unreadable tools line.

**Whether a role generated mid session can be spawned in that same session is
NOT ESTABLISHED** on any runtime. If it cannot, the role creation is its own
task brief ("add these two roles"), which stops, and the next session uses
them. That costs one STOP, and the person sees the new roles before they work.
The health app made four project roles and ship-ai four, so this is a rare step, not a
per brief one.

### How they pass role-shape

They already can. `role-shape` walks all of `formwork/roles/`, requires the
four fields and five sections, refuses a duplicate `owns`, and refuses `spawn`
outside the lead. Generated roles need nothing new from it. Two additions are
worth having:

- **A round participant must be a real role.** Every `<role>.md` in a round
  folder names a role that exists. This is checkable from files, and it is the
  only mechanical evidence that the lead spawned a declared role rather than a
  persona. The health app's lane files (`a-journeys.md`, `b-behaviour.md`) would have
  failed it, and that is the point.
- **The template should say**: a role that touches plans, phases or order names
  the director and the lead in "Does not own". The ship-ai project manager
  shows why. `role-shape` compares slugs, so it cannot see two roles owning the
  same thing under different names. This stays a review item, labelled as one,
  because a word list over Owns sentences would be fragile and would claim more
  than it sees.

### Library or generated

**Generated per project, starting from a library role when one fits.** No
growth of the kit library from projects.

- The kit's 21 pack roles stay the library. `docs/design.md` already calls them
  a guess, sized to be cut.
- A domain specialist (the health app's nutrition and training scientists, ship-ai's
  field researcher) is project content. It is created when the work arrives,
  which is the rule in `formwork/roles/HOW-TO-ADD-A-ROLE.md`: "A role arrives
  when the work arrives, not before."
- A library of domain experts in the kit would be the starter pack mistake
  again, and every one of them would load into every project, because there is
  no switch.

### How a generated role avoids leaking into the kit

- **By sync, in both directions.** The project roles folder is in `HUB_ONLY`,
  so sync never writes it and never deletes it. The kit's own clone carries the
  same exclusion, so even a kit maintainer's project roles are never published
  by sync.
- **The only leak path is a person copying a project role into the library by
  hand.** Generated roles do carry private content in their projects: a ship-ai
  role's `description` names the person and their hours, and a the health app role
  names the product. That is correct in the project and must never reach the
  kit.
- **So promotion is a kit brief, never a copy.** The role is rewritten without
  any person, product, device, account or machine, and reviewed as any kit
  change. Whether the kit's existing word lists (`~/.formwork/denylist-*`,
  named in `formwork/guard/protected-files`) could scan pack roles for this is
  NOT ESTABLISHED; I did not read what they are matched against.

---

## A6. What the recommended option adds

Proposed paths, written inside a fence so the link check does not read them as
files that should exist.

### Kit files, synced

```
FORMWORK.md
    one paragraph: a project may declare its shape in docs/project.md, and the
    director routes plain requests. Absent file, nothing changes

formwork/route.md
    the routing table: request to kind, size, stream, roles, templates.
    One home for the rule, read by the director and by a working session

formwork/roles/method/director.md        (changed)
    routes from route.md, plans back in two lines, drafts new roles inside the
    brief, keeps docs/project.md beside the standing brief, transcribes
    routing corrections and never authors them

formwork/roles/method/lead.md            (changed)
    spawns only roles that exist as generated files, never a pasted persona;
    says so in the round record

formwork/roles/TEMPLATE.md               (changed)
    a role touching plans or order names director and lead under Does not own

formwork/templates/project.md
    the shape of docs/project.md: direction, streams with settles and starts,
    roles in use, taste pack, how work here is routed

formwork/templates/phase.md
    the brief for a phase: what it settles, starts when, the team, closes with
    which report. Includes the general pattern of a step owned by another
    machine or session (release), with no machine named

formwork/templates/lane.md
    one participant file in a research or design round: the question and why,
    theory, state of the art, what it means here, ranked proposals, risks

formwork/templates/review-round.md
    a round on the running product: findings by journey, with evidence,
    the person's notes and the team's fixed together

formwork/templates/spec.md
    one story above every feature; every feature written as a general need

formwork/templates/instructions.md
    the two lines a project puts in AGENTS.md or CLAUDE.md to send a plain
    request to the director. Offered by setup, never written over a file

formwork/taste/README.md
    what a taste pack is, how a project names one and lists its differences,
    and the honest label: these are a guess, like the starter pack

formwork/taste/ios-app.md
formwork/taste/mac-app.md
formwork/taste/web.md
formwork/taste/deck.md
    optional checklists, items with ids, each saying what it catches.
    Read by the reviewer and the visual role. Never loaded as roles

formwork/check/checks/stream-known
    a brief's stream is declared in docs/project.md; its start condition is
    met; every round participant file names a real role; the instruction file
    carries the pointer when docs/project.md exists. Silent when the project
    has no docs/project.md

formwork/check/fixtures/stream-known/
    the input that breaks each of the four, as every check ships
```

### Project files, never synced

```
docs/project.md
    the project's shape: direction (the milestone), streams and gates, roles
    in use, the taste pack and its differences, routing corrections in the
    person's words. Optional

docs/streams/<name>.md
    only when streams run in parallel, the desktop app style. One page per stream,
    under two pages, cut before you add

docs/rounds/<stream>-<name>/
    phase rounds, in the folder the checks already watch

formwork/roles/project/<name>.md
    generated roles, flat, one per specialist, five sections

AGENTS.md or CLAUDE.md
    the project's instruction file, holding the two line pointer
```

### Taste packs as optional packs

A project opts in by naming a pack in docs/project.md (`taste: ios-app`).
Naming none loads nothing. Its own additions and the items it rejects go in
the same file, each rejection with a reason, so dropping an item is a line
with the person's name on it, the same principle `FORMWORK.md` applies to
rules. The general items (for example "pills only for real choices", "no
decoration posing as data", from
`<health-app>/docs/design/round-2/director-ai-check.md` via the idea
file) are method and may be in the kit. Anything specific to one product, an
accent colour, a character, stays in the project.

**Nothing mechanical judges taste.** The check can at most see that a review
round's report answers each item of the named pack. Whether it answered
honestly is the reviewer's, and the page should say so.

### Smallest useful first

1. templates/project.md, the `stream:` field, and stream-known for "declared
   only". Cheap, and it makes three projects' existing practice visible.
2. The routing table and the director change, with the two line plan back and
   the routing corrections.
3. The dynamic role path: the lead rule and the participant check.
4. Gates in stream-known.
5. The phase, lane, review round and spec templates.
6. Taste packs, last, because they are the most taste and the least structure.

### What I did not choose, and why

- **A project manager role owning phases.** Two owners of "what happens next".
- **A `[project]` section in `.formwork.toml`.** `config-shape` refuses it, the
  guard protects the file from the agent, and configuration is the wrong layer
  for corrections a person types in conversation.
- **A router skill.** One runtime only, and a second copy of the table.
- **Routing rules in the person's global instruction file.** Personal, outside
  the repository, invisible to the kit's checks, and already a source of drift.
- **A `phase:` field next to `stream:`.** Two names for one fact, in a field
  that is hard to change later.
- **Subfolders of project roles per stream.** Checked and never generated.
- **Per stream `open_briefs`.** The desktop app needed it. It is a change to
  `work-paired` and a new setting, and only parallel streams need it. Leave it
  until a second project asks.
- **Usage awareness as a setting** (how many builders at once against plan
  limits). It is one of the lead's three levers already ("how many turns each
  one gets"). The limit itself has never been measured, so a setting for it
  would be a number nobody can defend. NOT ESTABLISHED; belongs to the
  researcher and devops, not to structure.

---

## What I could not establish

- Whether a role generated during a session can be spawned in that same
  session, on Claude Code or any other runtime. The dynamic role path has a
  fallback (a separate task brief) because of this.
- Whether a project run with docs/project.md would actually keep `stream:`
  filled in. No project has run with it.
- What the kit's denylist word lists are matched against, and whether they
  could guard promotion of a project role into the library.
- Whether the desktop app's briefs carry `stream:` in frontmatter. I could not find its
  briefs folder by the paths I tried, and I read only the standing brief's head
  and one stream page.
- The cost of routing, in turns or money. `formwork/COSTS.md` says rounds are
  unmeasured; the plan back adds one exchange per request, unmeasured.
- The health app's full docs layout: a broad search timed out, so I listed only
  `docs/briefs/`, `docs/design/`, `docs/review/`, `docs/research/` one by one.
  `docs/profile/` was not opened.

## What I read

In this repository: `docs/rounds/whole-project-builds/brief.md`,
`docs/briefs/0022-whole-project-builds.md`,
`docs/ideas/2026-11-15-whole-project-builds.md`, `FORMWORK.md`,
`formwork/loop.md`, `formwork/threads.md`, `formwork/round.md`,
`formwork/roles/method/director.md`, `formwork/roles/method/lead.md`,
`formwork/roles/method/architect.md` (my own role),
`formwork/roles/HOW-TO-ADD-A-ROLE.md`, `formwork/roles/TEMPLATE.md`,
`formwork/templates/brief.md`, `formwork/templates/standing.md`,
`formwork/build`, `formwork/sync`, the head of `formwork/setup`,
`formwork/check/checks/role-shape`, the head of
`formwork/check/checks/work-paired`, the heads of `config-shape`,
`generated-current` and `predictions-first` (searched), the protected list in
`formwork/guard/protected-files`, the file list of `formwork/adapters/`,
`docs/design.md` sections 5b to 6 and its headings, `docs/gap-map.md` entries
B-10 to D-05 and its headings. The method roles other than director, lead and
architect I listed but did not open; the other templates I listed but did not
open.

In other projects, method only: `<health-app>/formwork/roles/project/ux-principal.md`,
the file lists of the health app's `docs/briefs/`, `docs/design/`, `docs/review/`,
`docs/research/`, and the first 40 lines of
`<health-app>/docs/briefs/0003-build.md`;
`~/Personal/Repos/ship-ai/formwork/roles/project/project-manager.md` and the
`stream:` lines of its two briefs; the head of
`<desktop-app>/docs/standing.md`, the file list of its `docs/` and
`docs/streams/`, and the first 50 lines of
`<desktop-app>/docs/streams/app.md`. I did not open the health app's
`docs/profile/`, any `.env`, credential, token or key file, nor any other
participant's file in this round.

## Response to the lead

**Objections 1 and 2: I yield on the separate file. I keep the field, the gates and the check.**
Here is what docs/project.md held, and where each item really belongs:
- **Roles in use:** a copy of the project roles folder. That is a second home for one fact, so I drop it. My own derived-copy test fails it.
- **Streams, gates and what each one settles:** "where we are" and "what is next", made structured. That is standing's job. The desktop app already keeps its stream table in its standing brief.
- **Routing corrections and the taste pack name:** the only items standing does not hold today. Neither changes faster or slower than "what is decided", so change rate does not justify a second file.

So the adjustment is:
- Two optional headings in `docs/standing.md`: "## Streams" (name, settles, starts, two or three lines each) and "## How work here is routed" (dated "in my words" lines, plus the taste pack name).
- stream-known reads the standing brief instead of a project file.
- "What rebuilds you is docs/standing.md, and nothing else" stays true.

The length risk is real. The desktop app's bloat came from free narrative ("Now:" paragraphs). Fixed-field stream entries do not need narrative. Whether they stay short is NOT ESTABLISHED, and the two-page rule still applies: cut before you add. Separate stream pages stay optional, for parallel streams only, as the desktop app did.

**Objection 3: I adjust. A relabel is allowed. A pasted persona is not.** The line is where the boundary comes from:
- **Relabel, allowed:** the lead spawns an existing generated role (for example `visual`) with a title line ("creative director for this round") and, if useful, a skill to follow. The role's owns, sections and tool grant still come from its checked file. The title adds focus, not authority. The health app brief 0003 pointing roles at skills is this shape.
- **Pasted persona, not allowed:** a spawn whose instructions are not an existing generated role, such as a general agent given a role body in the prompt. Its boundary and tool grant are unchecked.
- **The test for a new file and a STOP:** does an existing role's owns cover the work? If yes, it is a relabel and needs no file. If no, as with the health app's scientists, it needs a file. That was about four per project, not the eight relabels.
- **The desktop app's reviewers invented inside briefs:** these were relabels if each was the reviewer role with a lens. They needed files only if they owned something new.
- **The participant check loosens to match:** a round file is `<role>.md` or `<role>-<label>.md`, where `<role>` is a real role. So `visual-creative-director.md` passes and an unknown name fails.
