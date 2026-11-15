---
date: 2026-11-15
---

# Predictions

Round: whole-project-builds, brief 0022. Written by the challenger on
2026-11-15, after reading only the round brief, brief 0022, the idea file and
this template. No other participant's file and no other repository file was
open when this was written.

---

## What I expect to go wrong

- **Researcher.** Will return a long survey (design sprints, stage gates,
  Shape Up, double diamond, and several multi agent orchestrators) and conclude
  that "phases with gates" is the common pattern. Weak point: the survey will
  not show that any of those tools fixed the specific hand supplied method the
  idea file lists. Reason: the brief asks what other tools do, not whether
  they solved this person's problem, and surveys answer the question asked.
- **Architect.** Will propose a project layer that sits over the brief cycle,
  with a `docs/project/` or `docs/phases/` folder, one template per phase
  (spec, research, design, build, review, release) and a phase gate check.
  Weak point: six new templates and at least one new check, when
  `formwork/loop.md` already names phase and milestone and nobody has used the
  untemplated sizes enough to show they need templates. Reason: the brief
  lists those six templates by name in "What to answer", so the architect will
  draw what was listed.
- **Product.** Will report that all three projects needed the phase cycle and
  the research round shape, and will treat the health app's taste checklist as a
  general need. Weak point: the health app will be the source of most of the evidence,
  with ship-ai and studio contributing one or two briefs each that cannot
  carry a general claim. Reason: ship-ai has 2 briefs and studio has 1 (round
  brief, lines 97 to 99), so they cannot show repetition.
- **Record-keeper.** Will propose at least two new checks (a phase gate check
  and a dynamic role check that extends `role-shape`) and a cross phase
  decisions record. Weak point: at least one proposed check will test form
  only (a field is present) and cannot catch a wrong phase or a costume role.
  Reason: the kit's checks are file shape checks, and a role being useful is
  not a file shape.
- **The router.** Every participant except me will put "understanding from one
  prompt" somewhere that runs automatically on every prompt (a CLAUDE.md
  block, a skill, or the director). Nobody will count how often the user's
  prompts were actually ambiguous about size. Reason: the user called it "most
  important", and roles under that framing design the router instead of asking
  whether the current director already does it.
- **Dynamic roles.** The proposal will let `lead` write new project roles
  during a round, checked only by `role-shape`. That check passes any file
  with five headings, so a costume role (a name and a tone, no distinct
  `owns`) will pass. Reason: `role-shape` is described in the round brief as
  a five section shape check, and no participant has a cheaper tool.

## What would show me I was wrong

- Researcher: if the survey names a specific tool or method that ships a
  phase layer for agent coding and cites evidence that it removed hand
  supplied method, with a source, I was wrong.
- Architect: if the recommended option adds two or fewer templates and no new
  check in its first brief, I was wrong.
- Product: if product shows the same hand supplied method in desktop-app AND at
  least one of ship-ai or studio, with file paths, not only in the health app, I was
  wrong. the desktop app showing it alone with counts would make me half wrong.
- Record-keeper: if every proposed check names a fixture that would break it
  on a wrong phase or a duplicated `owns`, not only a missing heading, I was
  wrong.
- Router: if any participant counts the user's real opening prompts across the
  three projects and shows the director mis sized them, I was wrong about
  nobody counting.
- Dynamic roles: if the proposal requires the human to approve a generated
  role before it is used, or checks `owns` overlap across roles, I was wrong.

## What I think this round will decide

The round will recommend option (a) or a blend of (a) and (b): a project layer
shipped as an optional pack, with phase templates, a router in the director,
and dynamic roles written by lead into the project roles folder. It will say
the release pipeline stays out. It will order the briefs so the router or the
phase templates come first. Option (d) will be dismissed in a paragraph. I
expect nobody but me to argue that the first brief should be a project level
`standing.md` convention plus one template, with everything else waiting for a
second real project to ask for it.

## What nobody has asked

Who reads the project layer after the build ends. the health app, ship-ai and studio
are short projects. A phase layer pays off only if a project lives long enough
to cross several phases, and the one long project (desktop-app, 204 briefs) is the
one that ran without such a layer. Nobody will ask whether the long project
needed it.

Second: whether the user's real complaint is "I had to type the method" (a
convenience problem, fixed by copying a project folder) or "the method went
wrong when I did not type it" (a correctness problem). Only the second
justifies kit machinery.

## How confident am I

Fairly sure about the researcher, the architect and the round's outcome.
Guessing about the record-keeper. Fairly sure nobody counts prompts. Unsure
what desktop-app will show; I have not opened it.

---

## Marks (filled in after the round)

Not yet marked.
