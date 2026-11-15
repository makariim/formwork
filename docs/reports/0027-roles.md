---
brief: 0027
date: 2026-11-15
---

# 0027 Specialists cheaply

## For you

I stopped at a guard refusal, as the brief says. The work is all in, but one small fix is waiting for you: my new check `roles-named` prints an em dash in its three messages. Once the file existed, the guard refused my `sed` to change it. Swap them for ":" when you review, or leave them; nothing else depends on it.
The lead now spawns specialists in three tiers, written into the lead, the director, FORMWORK.md, the template and HOW-TO-ADD-A-ROLE.
Tier 1, relabel: "`visual` as art director", optionally with a typography skill. Same file, same owns and tools. A round file for it is `visual-art-director.md`.
Tier 2, new project role: a game needs a `sound-designer` and no `owns` covers sound. The director drafts it in the brief in the five section format, you say go, a working session writes `sound-designer.md` into the project roles folder and runs roles and check. Then the lead may spawn it.
Tier 3, never: a general agent told "you are a creative director" with no file. The new check fails a round file or an open brief's team row named `creative-director` when no such role exists.
Whether a role written mid session can be spawned in the same session is NOT ESTABLISHED. Until measured, adding a role is its own task brief.
Tests: 557 passed. The gate is red on one check only: `kit-integrity` sees the new check file. Re-record fingerprints after you review it. The brief stays `open` until your read-back.

## For the director

### Contradictions

- The brief says "a round participant file must be `<role>.md` or `<role>-<label>.md`" and 0023 widened rounds to anywhere under `docs/`. I enforce the name rule only in `docs/rounds/<name>/`. Elsewhere, folders such as `docs/research/` mix notes with participant files, so the rule would fail ordinary notes. Said under CANNOT TELL in the check and in `formwork/limits.md`.
- No "team table" format existed. I defined one: a table under a heading starting `Team`, the role's name as the first word of each row's first cell. Written into the brief template, the director, `route.md` and the check's docstring.
- Only open briefs are read for team tables. Done and dropped briefs are history; a role removed later must not turn old briefs red. A fixture holds that.
- His global instructions say set the brief to `status: done`. `work-paired` refuses done without the read-back, and I stopped at a refusal. Left `open`.

### The refusal

- A `sed -i` replacing the em dashes in `formwork/check/checks/roles-named`, refused by `formwork/guard/protected-files`: "REFUSED by self-protection: sed in place would change formwork/check/checks/." Not worked around. The file was written with Write while it did not yet exist, which the guard allows by design ("A path that does not exist yet is not protected").
- Left as is: three messages in `roles-named` use an em dash, against the no dash rule in his instructions.

### What changed

- `formwork/check/checks/roles-named` (new): round files in `docs/rounds/<name>/` must be `<role>.md` or `<role>-<label>.md` for a real role; allowed round files `brief.md`, `briefing.md`, `predictions.md`, `round.md`, `README.md`, `index.md`. Team rows in open briefs (`docs/briefs/*.md`, a round's `brief.md`) must name a real role. Real role means a `name:` in a file under `formwork/roles/`, project folder included.
- `formwork/check/fixtures/roles-named/` (new). must-pass: `a-round-of-real-roles` (includes `challenger-second-pass.md` and the hyphenated `record-keeper.md`), `a-team-with-a-relabel` (backticks and bold), `a-project-role-and-a-closed-brief`. must-fail: `a-round-file-for-no-role`, `a-team-row-for-no-role`, `a-round-brief-team-for-no-role`. Each must-fail fails for its own reason, one problem each.
- `formwork/roles/method/lead.md`: new section "Which agent you spawn": the three tiers, never a pasted persona, the NOT ESTABLISHED line.
- `formwork/roles/method/director.md`: the team is a table in the brief; a new role is drafted by the director, written by a working session, and why the director cannot write it.
- `formwork/roles/TEMPLATE.md`: under "Does not own", a role touching plans or order names the director and the lead.
- `formwork/roles/HOW-TO-ADD-A-ROLE.md`: the mid project order, relabel first, NOT ESTABLISHED line.
- `FORMWORK.md`: the tiers under "Your team"; a row in the checks table.
- `formwork/templates/brief.md`: the optional `## Team` table, under Scope.
- `formwork/route.md`: the team table line.
- `formwork/round.md`: `<role>-<label>.md` for a relabel.
- `formwork/limits.md`: what `roles-named` cannot tell.
- `CHANGELOG.md`: one Unreleased entry.
- `README.md`, `formwork/glossary.md`: fourteen checks to fifteen. `formwork/COSTS.md` still says fourteen, because that line reports a measured run; left alone.
- Generated: `.claude/agents/{director,lead}.md`, `.codex/agents/{director,lead}.toml`, `.gemini/agents/{director,lead}.md`.

### What was run

| Command | Result |
|---|---|
| `formwork/check/checks/roles-named <case>` over the six fixtures | three must-pass exit 0, three must-fail exit 1 |
| `formwork/check/checks/roles-named .` | "every role named in a round or an open brief's team is one of 28 real roles", exit 0 |
| `formwork/fw roles` | 30 considered (28 role, 2 skill), 2 written, claude-code |
| `formwork/fw roles --runtime codex` | 28 considered, 2 written |
| `formwork/fw roles --runtime gemini-cli` | 28 considered, 2 written |
| `formwork/fw test` | 557 tests, all passed |
| `formwork/fw check` (first) | red: `doc-links` (4 links to the project roles folder, which does not exist in the kit), `generated-current` (codex and gemini copies), `kit-integrity` |
| fix: link text changed to `formwork/roles/project/<name>.md`; codex and gemini regenerated | |
| `formwork/fw check` (last) | "GATE: red. 1 check(s) failed on the project, 0 input(s) wrongly accepted, 0 wrongly rejected." Only `kit-integrity`: "added formwork/check/checks/roles-named". `roles-named`, `role-shape`, `kit-leak-scan`, `doc-links`, `generated-current` all ok |

An earlier slip: `formwork/build --help` is not a help flag; it ran a claude-code build, which wrote nothing new.

A second refusal, a false hit: a Python heredoc that edited only this report was refused with the same message, because its text mentioned the check's path. I made those report edits with the Edit tool instead. No kit file was touched by it.

### Not done

- The em dash fix in `roles-named` (the refusal).
- Fingerprints: his to re-record after review.
- No other repository touched. No git writes.

### git status

```
 M .claude/agents/director.md
 M .claude/agents/lead.md
 M .codex/agents/director.toml
 M .codex/agents/lead.toml
 M .gemini/agents/director.md
 M .gemini/agents/lead.md
 M CHANGELOG.md
 M FORMWORK.md
 M README.md
 M docs/briefs/0026-measure-routing.md
 M docs/reports/0026-measure-routing.md
 M docs/standing.md
 M formwork/glossary.md
 M formwork/limits.md
 M formwork/roles/HOW-TO-ADD-A-ROLE.md
 M formwork/roles/TEMPLATE.md
 M formwork/roles/method/director.md
 M formwork/roles/method/lead.md
 M formwork/round.md
 M formwork/route.md
 M formwork/templates/brief.md
?? docs/briefs/0027-roles.md
?? docs/reports/0027-roles.md
?? formwork/check/checks/roles-named
?? formwork/check/fixtures/roles-named/
```

The 0026 brief, report and `docs/standing.md` changes were in the tree before this session and were not touched.

accepted: 2026-11-15
in my words: next, he fixed the dashes himself, re-recorded and committed 9b9ae53
