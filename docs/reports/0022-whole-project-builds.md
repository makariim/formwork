---
brief: 0022
date: 2026-11-15
---

# 0022 Formwork for building a whole project

## For you

You asked what formwork should become so it can build a whole project from one plain prompt. Five roles researched it and argued it out. The kit was not touched.

The first thing to know: your projects already built the structure by hand, and the kit's own checks could not see it. In the health app the rounds happened, but in folders `predictions-first` never reads, so it said clean over nothing. The health app's standing still names brief 0001 as next. The desktop app breaks its own one-open-brief-per-stream rule today, and no check notices.

My recommendation is "beside, not over". It is one loop, with no product process on top. Formwork gains four things. Its checks learn to look where projects actually work. The director routes a plain prompt from a written table and says the plan back in one or two lines. A specialist is an existing role with a new title, and a new role file appears only when no role owns the work. Optional templates (spec, research round, review round, release step) and small taste packs cover big work.

Your release machine, accounts, devices, look and usage numbers stay out of the kit. It would describe only the general pattern.

The first step is a brief that widens three checks. Nobody objected to it, the challenger included. Five questions for you are at the end of the research file.

## Accepted

accepted: 2026-11-15
in my words: take your picks, start step 1 (picks: routing corrections in a separate small file per project; the director routes; roles may be created mid project by the relabel first path; the kit ships a template for personal defaults; steps 1 to 4 before publishing 1.0.0)

## For the director

### What changed

- `docs/rounds/whole-project-builds/`: the round. `brief.md` (the lead's briefing), `predictions.md` (challenger, written first), one file per role, each ending with a "Response to the lead", and `round.md` (the argument, the disagreements, the predictions marked).
- `docs/research/0022-whole-project-builds.md`: the full research and the proposal.
- `docs/reports/0022-whole-project-builds.md`: this file.
- `docs/standing.md`: `updated:` moved to 2026-11-15, so the round files do not turn `standing-current` red. The open item from 2026-11-15 now points at the research file.
- `docs/briefs/0022-whole-project-builds.md`: one path rewritten as a full `<health-app>/...` path, because `doc-links` read it as a link into this repository.
- Mechanical edits to participant files: a `date:` line at the top of six files, and two backticked paths unquoted (predictions.md line 73, architect.md line 134). predictions.md kept its original timestamp, so `predictions-first` still sees it as written first. No wording of any position was changed.

Nothing under `formwork/`, `formwork_cli/` or `FORMWORK.md` was changed.

### What was run

Read-only searches over the four projects, and the kit's checks. The researcher downloaded public repository tarballs to a scratch folder in /tmp and fetched web pages. That folder (306 MB) was removed at the end. No installs, and no git writes.

### The check

**The full gate does not run on this machine.** `formwork/fw check` stops at pass one:

```
ERROR: check kit-integrity could not run:
ERROR: no fingerprints recorded at ~/.formwork/fingerprints/formwork-cfd31839232c635d.txt
       Run: formwork/check/checks/kit-integrity --record .
ok    config-shape
ok    decision-ids
ok    doc-links
ok    generated-current
ok    guard-wired
```

Recording fingerprints is your decision, so I did not do it. The checks that touch what this brief wrote, each run alone:

```
standing-current   standing brief filled in, dated 2026-11-15, ahead of all 10 record(s)
predictions-first  1 round(s) checked, each with predictions on record
work-paired        1 brief(s), every finished one has its report and its read-back, 1 still open
report-shape       1 report(s), each with its part for the human first and within 1000 words
```

### Git status

```
 M .claude/settings.json      (was modified before this session)
 M docs/standing.md
?? docs/briefs/
?? docs/ideas/
?? docs/reports/
?? docs/research/
?? docs/rounds/
```

Nothing staged.

### The three that matter

- **Done but not asked for.** The lead sent one challenge to each contested position after all five answers were in, as `formwork/roles/method/lead.md` says to. Four factual disputes were settled by opening files. The researcher's scratch downloads were deleted.
- **Asked for but not done.** The brief says to set the brief to `status: done`. I left it `open`. `work-paired` refuses a done brief whose report has no read-back, and only you write the read-back. Once you have written the two lines above, the brief can be marked done.
- **Wrong in the brief.** The desktop app has 198 reports, not 310. The 310 counts attachment folders. "Skills were dropped" is half out of date, since 1.0.0 ships `humanizer`. `docs/standing.md` says both things in two different sections. The idea file's "every time" holds for personal rules (run alone appears in 155 of 218 briefs) and not for the general method, which cost about one sentence per project. Product's claim that the health app never wrote a read-back is wrong: reports 0001 to 0003 carry it. I repeated that error in one challenge and withdrew it before it was answered.

### The body of the work

- The proposal: `docs/research/0022-whole-project-builds.md`. Its sections are what is missing, the options, the routing model, phases and gates, templates, dynamic roles, taste packs, checks, what stays out, the build order, and five open questions.
- The argument: `docs/rounds/whole-project-builds/round.md`.
- Proposed brief order: (1) widen `predictions-first`, `standing-current` and `open_briefs`; (2) a generic kit leak scan; (3) routing, after your answers to questions 1 and 2; (4) measure routing with should and should not prompts; (5) roles, after your answer to question 3; (6) optional templates and gates; (7) taste packs.
- Dissent kept: the challenger still argues (d) for the layer, the router and generated roles. It accepts only brief 1.
- Cost: four disputes resolved by file, one closed in exchange, three deferred to you, none halted. What a round costs in money is NOT ESTABLISHED.
