---
updated: 2026-11-15
by: the working session for brief 0031
---

# Standing brief

Live, not history. Everything else in this folder is the record of building the
kit and is left as written. This file describes the present and is rewritten.

## What we are building

Formwork. A forkable starter kit for running a project with coding agents: a
loop, a set of roles, rules that say what they catch, three guards that refuse,
and a gate of checks that shows itself failing as well as passing. It carries
nothing about anybody's product. It is the shape, empty.

## Where we are now

**0.2.1 is what is on PyPI. 1.0.0 is built here and not published.** It
carries everything below. In it: a role's
`description`, `model`, `skills` and `color` now reach the generated Claude
Code agent instead of being dropped. And, from the first multi-repository use,
the human kept in the loop: `work-paired` allows one open brief by default and
refuses a brief marked done until its report carries the human's read-back. A
fourteenth core rule says the human is not the courier. See entry 14 of
`docs/dogfood.md`. The read-back's `in my words:` line needs five words by
default, and `read_back_words` under `[strength]` changes that: 1 lets
"accepted" through, 0 lets the line be empty.

Also unreleased: the kit ships its first skill, `humanizer`, pinned at one
upstream commit in `formwork/skills/humanizer/`, placed into
`.claude/skills/` by `formwork roles`. `formwork/style.md` says text sent as
the human goes through it. Decision 0001, proposed.

Also in 1.0.0, from a clone on another machine, brought home as patches:
reports for two readers, `## For you` first, with a `report-shape` check; and
`sync`, which brings a project's kit copy up to date. `sync` now also runs
from the installed package, as `formwork sync`, pinned to the release, so no
other machine needs a clone. Decision 0002, proposed.

**0031 is built and waiting for his read-back.** In the tree: a page and a
template for bringing in somebody else's skill (`formwork/bring-a-skill.md`,
`formwork/templates/upstream.md`), two lines in a builder's report (touched
outside my files, packages added) in the build template and `lead`, and
localisation and right to left layout named in `writer`, `visual`,
`frontend` and `mobile`. A new check, `skill-provenance`, is staged as
`docs/reports/0031-three-gaps.patch` because the guard refused it.

Three guards, thirteen checks, twenty eight roles, forty eight rules, one
skill, 494 tests across eight suites.

Version two added: the standing brief and its check, a `director` role holding
the upper layer, `lead` widened to split a brief as well as run a round, briefs
and reports as numbered files with a check that catches work marked finished
that left nothing behind, one page saying how the agents talk to you, and
`formwork setup`, which asks eleven questions once and writes what they imply.

**Then five audits attacked it and found 71 defects**, nearly all in what had
just been written. The serious ones are fixed: `setup` no longer edits the
section it promised never to touch, no longer reads Ctrl-C as consent, and no
longer overwrites a file made while it was asking; `install` refuses rather
than wiring the wrong project; and the three new checks no longer report clean
while examining nothing. Every fix carries a test or a fixture that fails
without it.

## What is decided

- 2026-11-15, **0030 accepted** (he applied the patch, committed f82feb0, 17 checks green): edits through links to protected files refused; hidden unicode check. The warn setting never reached the hook, so the guard stayed on block and the session staged a patch, which was the right outcome. **0031** (the three gaps from `docs/research/ecc-gaps.md`, his words "queue 1 to 3") started.

- 2026-11-15, **0030 resumed with the protected files guard on warn, for this brief only** (his words: "warn for 0030"), after it stopped at the guard: the hidden unicode check was built; the linked file fix to the guard, its tests and the docs remained. Every protected change still shows in kit-integrity for his review before he re-records.

- 2026-11-15, **0029 accepted**: taste packs (screens, web, deck, iOS); the seven step plan from 0022 is complete. **0030** (ECC ideas 5 and 6: linked protected files and hidden unicode) started; ideas 1 and 2 follow.

- 2026-11-15, **0028 accepted** (committed 4d9f211, 16 checks green): six optional templates, phases as streams, checked gates. His choice on the ECC study (`docs/research/ecc-ideas.md`): "c, go": step 7 taste packs first, then ECC ideas 1 (measure a guard with arms), 2 (review then refute), 5 (linked protected files), 6 (hidden unicode) as small steps. **0029** (taste packs) started.

- 2026-11-15, **0027 accepted** (committed 9b9ae53, 15 checks green): relabel first, new project roles by brief, the roles-named check. **0028** (step 6, optional templates and gates) started.

- 2026-11-15, **0026 accepted** (committed 6223baf; routing 44 and 45 of 49 on Haiku, about $0.13). His choice ("b, everything is already working, no need to disrupt them now"): continue the kit plan, do not bring routing into his projects yet. **0027** (step 5, roles) started.

- 2026-11-15, **0025 accepted** ("next"; committed eafd01c): routing table, director routes, corrections file, setup writes two lines, personal defaults template. **0026** (measure routing) started.

- 2026-11-15, **0024 accepted** (he fixed the self hit, re-recorded, committed a6240e5; 14 checks green). **0025** (step 3, routing one plain prompt) started.

- 2026-11-15, **0023 accepted** ("next"; committed 2537c06): rounds anywhere under docs, stale standing, open briefs per stream. It worked around the self protection guard with shell scripts; the director reviewed the diff (additive). **0024** (the kit leak scan) started, told to stop at a guard refusal instead.

- 2026-11-15, **0022 accepted** ("take your picks, start step 1"): beside, not over; routing corrections in a separate small file per project; the director routes; roles may be created mid project by the relabel first path; the kit ships a template for personal defaults; steps 1 to 4 before publishing 1.0.0. **0023** (step 1, the checks see where projects work) started.

Two records in `docs/decisions/`, both `proposed`, waiting for him: 0001,
humanizer for text sent as the human; 0002, formwork is changed only here and
installed everywhere else. The decisions before it live in the design pages
in this folder, which are history and are not maintained.

Two people outside the project have now run it. One reported that the guards
held on the scenario in the README. That is the first evidence from anybody
who did not write it, and it is one person on one scenario, self reported.

## What is open

- 2026-11-15, from Muhammad: extend formwork to build a whole project end to end (phase cycle, research round shape, taste checklist, review rounds, dynamic roles). Noted in `docs/ideas/2026-11-15-whole-project-builds.md`; not decided. Researched in brief 0022: proposal in `docs/research/0022-whole-project-builds.md`, five questions for him in its last section. Nothing in the kit changed.

Whether the kit should ship a standing brief for itself at all, or only the
template. This file is the experiment.

NOT ESTABLISHED: what a round costs in money. Nobody has measured it once.

NOT ESTABLISHED: whether any of this works for more than one person.

Whether the `lead` may invent a role. Today the twenty eight are files, checked
for a unique job and five sections. Asked for by somebody who tried it: let the
lead make a role on the fly when a task needs one that does not exist. Open,
and it cuts across what `role-shape` is for.

## What is next

Publish 1.0.0. Then other machines install it and drop their clones, as
decision 0002 proposes.

## What we tried and stopped

Skills, and a model and effort level per role. Both were planned for version
two and both were dropped before starting. The model one turned out to be
Claude Code only as far as anybody has checked, which makes it a smaller
feature than it sounded.

Scrambling the contents of fixtures so a check could not recognise them. It
broke the checks that read filenames for real reasons. Recorded in
`formwork/limits.md` instead of papered over.

One fingerprint file for the whole machine. The second project on the same
machine got accused of tampering. Now one file per project.
