# Routing one plain prompt

A person types one plain sentence. This page says what happens next: what kind
of work it is, how big, who does it, what shape the brief takes, and where it
stops.

**Routing accuracy, measured: 44 and 45 of 49 routed as expected**, in two
runs of `formwork/evals/routing/run` with Haiku (2026-11-15, about $0.03 a
run). A prompt counts only when its kind, size and first step all match. The
failing prompts change from run to run by about three, so a difference smaller
than that between two versions of this page is noise. One prompt failed in
every run: a small research ask dressed in big words, routed as a round.

Before this page was changed by that measurement it scored 38 of 49. It
dropped then: new products sent to a round before a spec (3 of 5), and small
asks sized by their words (4). Both now have a line below.

What the number does not show: one model, one person's prompts, scored on the
choice only. It does not say the brief that followed was any good. Run it again
after any change to this page or to the director, and write the new number
here. Until then, treat every route as a guess the person can correct in one
line.

---

## Who routes

| Size | Who routes |
|---|---|
| a task | the session that got the prompt. It may route down only |
| anything above a task | the `director`, and nobody else |

A working session that finds the work is bigger than a task says so in one line
and hands it up. It never writes a bigger brief itself. The `lead` does not
route either: it runs a round or splits a brief once the director has sized it.

---

## Before routing

Read, in this order:

1. `docs/standing.md`: where the project is, and the live stream if streams are
   declared.
2. `docs/routing.md`: this person's corrections, in their words. A correction
   beats this table.
3. This page.

If `docs/routing.md` does not exist, route from this page alone. Do not create
it until there is a correction to write.

---

## The kinds

Pick one from this list. Not from role descriptions, not from skill names. A
short named list is what keeps routing from drifting as the library grows.

| Kind | Size test | Template | Team | Stops |
|---|---|---|---|---|
| **A question** | an answer, nothing changes in the repository | none | the session that got it | after the answer |
| **A fix** | one fault, reproduced, one or two files | one line brief | the session that got it | after the fix, its test and `formwork check` |
| **A change to an existing product** | task if a sentence covers it; checkpoint if you have to say what is out of scope | one line, or `templates/brief.md` | the session, or one working role (`backend`, `frontend`, ...) | at the report |
| **Research** | task if one source answers it; round if the answer is unclear and costly to get wrong | one line, or `templates/round.md` | `researcher`; a round through `lead` | at the report or the round record |
| **A deck or document** | task if the words already exist; checkpoint if the argument has to be built | one line, or `templates/brief.md` | `writer`, with `visual` when it is looked at | at the draft, for the person to read |
| **A new product** | never a task. Milestone, made of phases | `templates/brief.md` for the first brief: a one page spec from the person's words. A round comes later, when the spec leaves a choice open | `director` plans; `lead` splits; the packs build | after each phase's report, and before anything is released |

When two kinds fit, take the smaller one. When none fits, ask one question.

### Templates for a phase, offered, never required

When the work is a phase (above a checkpoint, inside a milestone), offer the
template that matches what this brief does. Pick by kind and size. They are
not a sequence: a project may use one, several, or none, in any order.

| This brief does | Size | Offer |
|---|---|---|
| writes the spec for a new product or a big change | phase | `templates/spec.md` |
| researches a question the spec leaves open | round | `templates/research-lane.md`, inside `templates/round.md` |
| designs a look, screens or an architecture | phase | `templates/design-round.md` |
| builds version 1, or one part of it | phase | `templates/build.md` |
| reviews the running product by journey | checkpoint or phase | `templates/review-round.md` |
| releases a version | checkpoint | `templates/release-step.md` |

A brief that must wait for another stream or a decision carries one
`starts:` line (`now`, `after <stream>`, `decision NNNN`), checked by
`gates`. See Phases and gates in `formwork/loop.md`. A task never carries one.

---

## Size

**The default is a task.** Step up only when the work grows, never at the start
to be safe.

The test is the loop's own (`formwork/loop.md`): could a reviewer sensibly
accept one part and reject the next? If yes, it is more than one piece of
work, and it is above a task.

**Size the work, not the words.** "Critical", "comprehensive", "full",
"deep", "initiative" and "architect" do not make an ask bigger. "Quick" and
"little" do not make it smaller. Size what would actually change. When the
words and the work disagree, the work wins, and you say the size you picked.
Ask only when the work itself is unclear.

Say the size in plain words. The person can override it in one line.

---

## The team

1. An existing role whose `owns` covers the work.
2. A relabel when the work needs a focus: an existing role given a title for
   this brief ("`visual` as art director").
3. A new role only when no `owns` covers it, following
   `formwork/roles/HOW-TO-ADD-A-ROLE.md`.

The brief names the team in a table under `## Team`, the role's name first in
each row. `roles-named` fails a row that names no real role.

Hooks are not chosen per prompt. They are wired once by `formwork install` and
run on everything. `formwork check` runs whole, every time.

---

## Say it back, then act on the size

**A task.** One line, then do it. No "Go?". The person corrects only when the
line is wrong.

> Task, fix: reproduce the empty search result, fix it, add the test. One line
> brief.

**Above a task.** Two lines: kind, size, team, first brief. Then the director
writes that brief and stops with its fixed sentence. The work runs alone inside
the brief, and choices are collected for the report.

> Milestone, new product: a one page spec from your words first, for you to
> read. Then research, design samples for your pick, build, our review beside
> yours; release only when you say.

A request for a stream whose start condition is not met is said back as such,
and not started.

---

## Corrections

When the person says the route was wrong, the director writes their words into
`docs/routing.md`, a dated pair, append only:

```
routed: 2026-11-20
in my words: bugs in the search page are tasks, never rounds
```

The person cuts lines. The director never edits or rewords one. The template is
`formwork/templates/routing.md`.

A correction that turns up in more than one project is a reason for a brief
that changes this page. It is never a reason to copy anybody's words into the
kit.

---

## What this cannot do

Tell that a small ask was born large. No check reads intent, so a one line
request briefed as a round passes every check. The director's rule is the only
guard: if you cannot tell the size, ask one question.

Know that it routed well on prompts unlike the set in `formwork/evals/routing/prompts.json`. See the top of this page.
