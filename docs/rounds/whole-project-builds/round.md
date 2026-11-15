---
round: whole-project-builds
brief: 0022
date: 2026-11-15
by: lead
---

# Round record: formwork for building a whole project

The argument. The proposal it produced is in
`docs/research/0022-whole-project-builds.md`. The participants' own files sit
beside this one, each with a "Response to the lead" at the end.

## Who took part

| Role | File | Question cut |
|---|---|---|
| challenger | `predictions.md` first, then `challenger.md` | the case for doing none of this |
| researcher | `researcher.md` | what other methods and tools do, with sources |
| architect | `architect.md` | where a project layer fits, what is fixed and what is generated |
| product | `product.md` | what the person needed, from the four projects |
| record-keeper | `record-keeper.md` | checks, gates, records, and what stays out |

Overlap on purpose: "understanding from one prompt" went to the architect
(structure) and to product (the person's side). Everybody was dispatched at
once. Each got one challenge from the lead after all five were in.

## Facts the lead settled from the files

Four disputes were settled by opening a file, so nobody spent a turn on them.

1. **How often "run alone" was typed by hand.** Challenger counted 38 briefs,
   product 57. Both used narrow patterns. The union, plus "never wait for
   him", is **155 of 218 briefs, in all four projects** (stride 5, ship-ai 1,
   studio 1, argoni 147). Command, from `~/Personal/Repos`:
   `rg -l -i "(never|do not|don't) stop to ask|runs alone|dont want to be stopped|i dont want to get interrupted|never wait for him" stride/docs/briefs ship-ai/docs/briefs studio/docs/briefs argoni/docs/briefs | wc -l`.
2. **Whether the phase cycle appears outside Stride.** Phase cycle wording
   appears in all four projects' docs (stride 4 files, ship-ai 2, studio 2,
   argoni 5), by
   `rg -l -i 'research.{0,40}design.{0,40}(build|implement)|three phases|words, design, build|no design, no code' <project>/docs <project>/AGENTS.md`.
   Keyword floor, not a census.
3. **Whether Stride wrote the read-back.** Product said no. Record-keeper said
   yes. The file decides: reports 0001, 0002 and 0003 carry `accepted:` and
   `in my words:` at lines 85, 96 and 106; a stale "Waiting for your
   read-back" placeholder sits above them in 0001 and 0002. Briefs 0004 and
   0005 are open. **Product's P4 table and point 2 of its short version are
   wrong on this.** The lead also carried the wrong version into the challenge
   sent to the challenger, and withdrew it before the challenger answered.
4. **Argoni brief 0122.** Challenger used its 21.6% misroute figure against a
   router. It measures a two class message classifier inside the product, not
   an agent routing a development request. Analogy, not evidence. The
   challenger agreed.

Also from the files: Argoni has 204 briefs and 198 reports, not 310; the 310
counts attachment folders (record-keeper). The lead's briefing carried 310.

## The positions, attributed

**Challenger.** Option (d) for any layer, router or generated roles. After the
challenge: yielded "convenience only", yielded the prediction it had staked,
yielded 0122. Kept: none of the observed failures is fixed by a layer, a
router or generated roles. Accepts exactly one brief: make
`predictions-first`, `standing-current` and `open_briefs` see where projects
really keep rounds, standing and streams, each fix with a fixture from a real
case. Still objects to changing director and lead.

**Researcher.** Ranked transfers: say the size and let the person override it
(BMAD `bmad-build`, superpowers brainstorming, Shape Up appetite); pick from a
short explicit list, because implicit skill routing collapses as libraries
grow (arXiv 2610.18522, 2603.22455, abstracts only); route in three layers;
measure routing with `claude plugin eval` should and should not cases;
generate, check, freeze, reuse for roles; gates with criteria written first;
taste packs as overridable defaults graded by how a finding is detected
(gstack). Against: a fixed software company of roles. Not challenged; nothing
in the round contradicted a sourced claim.

**Architect.** Rejected (a), (b) alone and (d). Recommended "beside": brief
cycle unchanged, director the only router, a project file, one check, a thin
pack. After the challenge: **yielded the separate project file.** Its streams
and routing corrections move into two optional headings in `docs/standing.md`,
so "what rebuilds you is docs/standing.md, and nothing else" stays true.
Adjusted on roles: a relabel (existing role plus a title line plus a skill) is
allowed with no file; a pasted persona with no checked role behind it is not.

**Product.** Catalogued what was supplied by hand. After the challenge:
**yielded the phase cycle as a list** ("for the order alone, the honest answer
is nothing, it saves typing"). Kept two gates, each with a failure the
director did not catch: no build before requirements are accepted (argoni
0034, the plan "grew by answering one case after another"); unproven items
listed and seen before the next phase (Stride's UI tests written and never
run, in 0003 and again in 0004). New rank 1: running alone between gates.
Taste cut to three items that survived every change of taste.

**Record-keeper.** Checks to add: rounds visible outside `docs/rounds/`;
size; every named role exists; a generic kit leak scan; later `after:` and
per stream limits. Refused: a taste check, a review content check, a linear
phase order gate, any check that judges the router, any usage meter. After the
challenge: **accepted a durable project file**, on two conditions (streams move
out of standing, never kept twice; routing corrections append only, dated, in
his words). Withdrew "size is the only required field": no `size:` line means
task, and a task over a line ceiling fails until it states its size.
`stream:` is required once streams are declared.

## The disagreements

**1. Where the project's streams and routing corrections live.** The architect
and the record-keeper crossed: each moved to the other's starting point.

- Architect, now: two headings in `docs/standing.md`. Grounds:
  `formwork/roles/method/director.md` says standing is the one thing that
  rebuilds the director; a second file is a second place holding the picture.
- Record-keeper, now: a separate durable file. Grounds: its own K2, standing
  is rewritten and a binding record must not be; Argoni's standing at 412 non
  empty lines (challenger's count) shows what happens when it all goes in one
  page.
- Both persuaded, not overruled, which is why it does not close. The record
  does not decide it. **Deferred to the human.** What hinges: one file to read
  and a two page limit at risk, or two files and a second home for the plan.
  Lead's recommendation, on the grounds that only one of the two is already a
  written rule of the kit: standing headings, with the record-keeper's append
  only condition kept for the routing lines.

**2. Whether to change the director and lead at all.** Challenger: no, it fixes
none of the observed failures and loads the role that already "offered to
build four times". Architect: yes, the director already owns sizing, and
routing is sizing plus a stream plus a team. Not resolved. Deferred: the
person's "most important" requirement is a routing requirement, so declining
any director change means declining that requirement. That is his call to
make, and the round says so rather than closing it.

**3. Whether the lead or anyone may create a role mid project.** Already open in
`docs/standing.md`. Architect: director drafts in the brief, the person's go
accepts, a working session writes it and runs `formwork roles`, then the lead
spawns. Challenger: generated roles pass `role-shape` as costumes and close the
open question by shipping it. Product: most specialists were relabels and need
no file. The relabel rule narrows the disagreement to about four roles per
project. **Deferred to the human**; it is his open question.

**4. How much the read-back should weigh as a phase gate.** Record-keeper keeps
"done with read-back" as the key and shows the go word already is the
read-back in Stride. Product's original claim that he never writes it is
wrong (settled above). What remains open is only how short a read-back may be,
which is `read_back_words`, already a setting. Closed by the file.

## Rejected, with reasons

- **(a) A project layer over the brief cycle.** Rejected by every participant.
  A second process in a kit whose loop page says "they are not five different
  processes", and a second owner of "what happens next" (architect; ship-ai's
  project-manager role is the small version, passed by `role-shape` because it
  compares slugs, not meaning).
- **(b) A pack alone.** It cannot route, and there is no switch for packs, so
  every role in it loads into every project (architect, challenger).
- **A fixed cast of roles.** MetaGPT and ChatDev 1 shapes; ChatDev moved off it,
  AutoGen is archived (researcher).
- **A router skill.** One runtime only and a second copy of the table
  (architect).
- **Routing rules in the person's global CLAUDE.md.** Personal, outside every
  repository, invisible to checks, already a source of drift (architect).
- **A `[project]` section in `.formwork.toml`.** `config-shape` refuses it and
  the guard protects the file from the agent (architect).
- **A taste checklist check.** It can prove a list was copied, not that anybody
  looked (record-keeper).
- **A linear phase order gate.** Stride ran review 0004 and redesign 0005 open
  together, by his choice (record-keeper).
- **A usage meter.** Needs an account or reads private transcripts
  (record-keeper). Plan limits NOT ESTABLISHED (researcher).
- **Anything about a release machine, accounts or devices.** His words rule it
  out. The kit may describe a four line pattern at most (product).
- **The phase cycle as a fixed list of phases.** Product yielded it.

## Left open for the human

1. Streams and routing corrections: two headings in standing, or a separate
   file. Recommendation above.
2. Whether the director takes on routing (disagreement 2).
3. Whether roles may be created mid project, by which path (disagreement 3).
4. Whether the kit ships a template for the person's own defaults (the block
   all four projects copied into AGENTS.md by hand, 26 matches, product item
   12), or leaves that to his global CLAUDE.md.
5. Whether the first check brief waits until 1.0.0 is published (challenger,
   C6: the kit's own next step is publishing).

## The price

- **Gets harder.** Every new field is a line every brief carries. The round
  kept one field required only once claimed (`stream:`) and made size implicit
  for tasks for that reason.
- **Foreclosed.** A separate product process above the director.
- **Fails silently.** A routing plan said back and then not followed. No check
  can see it. Also: a project that declares streams and stops updating them;
  the check catches undeclared names only.
- **Who keeps it alive.** The kit maintainer, who must also keep the counts in
  `FORMWORK.md`, `docs/standing.md` and `formwork/COSTS.md` in step (they
  already disagree once: COSTS.md says twelve checks, there are thirteen).

## Predictions, marked

From `predictions.md`, against what came back.

| Prediction | Mark |
|---|---|
| Researcher returns a survey concluding phases with gates is common, without showing any tool fixed this problem | **Right** on the second half: researcher says "Whether any of these tools improves outcomes. None was executed." Partly wrong on the first: the survey's centre was routing and sizing, not phases |
| Architect proposes a layer over the brief cycle with six templates and a phase gate check | **Wrong** on "over" (architect rejected it). **Right** that its first brief carried a new check. Wrong if test ("two or fewer templates and no new check in its first brief") not met |
| Product leans on Stride; ship-ai and studio cannot show repetition | **Wrong**, and the challenger conceded it. Method appears in all four projects |
| Record-keeper proposes two or more checks, at least one testing form only | **Right**. Size is form only, and the record-keeper says so |
| Everybody puts routing somewhere automatic; nobody counts prompts | **Partly right.** The architect put it in the director, not an automatic hook. Nobody counted opening prompts; product counted brief sizes instead |
| Lead writes roles checked only by `role-shape` | **Wrong.** The architect requires the person's go before a new role exists, which was the challenger's own wrong if test |
| Round recommends (a) or (a) plus (b) | **Wrong.** (a) rejected by all |
| Nobody but the challenger argues for a standing convention plus one template first | **Wrong in an interesting way.** The architect ended at standing headings; everybody ended with a check brief first |

## Cost of the round

Resolved by file: 4 (run alone counts, phase wording, read-back, 0122).
Closed in exchange: 1 (read-back weight). Deferred to the human: 3. Halted:
none.

Read more than once: Stride's briefs and the director role were read by four
of five participants. Stride's reports were read by product, record-keeper and
the challenger, and two of them reached opposite facts about the same lines.
What would have made it cheaper without making it worse: the briefing should
have carried the read-back fact and the true Argoni counts, checked by the
lead before dispatch. That was the lead's job and it was not done.

Token figures per participant are visible to the lead as tool metadata only and
are not a measure of money. What a round costs in money: NOT ESTABLISHED, as in
`formwork/COSTS.md`.
