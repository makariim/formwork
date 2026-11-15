---
brief: 0026
date: 2026-11-15
---

# 0026 Measure routing

## For you

Routing is now measured. With the table as it stands, 44 and 45 of 49 prompts routed as expected, in two runs with Haiku. A prompt counts only when its kind, size and first step all match. The routing page and the director now say that number, with the command, in place of NOT ESTABLISHED.
Before any fix, the first run scored 38 of 49. Two gaps caused 7 of the 11 failures. New products went to a round before a spec (3 of 5). Small asks dressed in big words were sized by the words (4). I added one line to the table for each, and the next run scored 45.
One prompt failed in all four runs: "a deep multi angle research effort" on commas or semicolons in CSV export. It is always routed as a round. You may think a round is right there. If so, change its expected answer; I did not change any answer after seeing results.
The failing prompts change by about three from run to run. So any difference smaller than three between two versions of the table is noise.
Total spend for four full runs and one three prompt trial: about $0.13. Tests: 557 passed. The gate is red on one check, and not from this work: the 0025 read-back in your working tree has 4 words and the minimum is 5.
No guard refused anything. The brief stays `open` until your read-back.

## For the director

### Contradictions

- The brief says "run each prompt once". I ran the set four times. Runs 1 and 2 are the before and after the brief asks for. Run 3 tested a runner wording change. Run 4 repeated the final setup, because one run cannot tell 44 from 45 and the spread had to be seen before a number was written down. The extra runs cost about $0.06.
- His global instructions say to set the brief to `status: done`. `work-paired` refuses done without the read-back, as in 0024 and 0025. Left `open`.
- `formwork check` is red on `work-paired` for `docs/reports/0025-routing.md`. The uncommitted read-back there, "next (he committed eafd01c)", has 4 words and `read_back_words` is 5. That line is the human's, so it was not touched.

### The set

`formwork/evals/routing/prompts.json`, 49 prompts. Kinds: change 11, question 7, fix 7, research 7 (3 accept question too), document 7 (2 accept fix or change), new product 5, ambiguous 5. Sizes: task 29, checkpoint 7, round 3, milestone 5, any 5. Tags: plain 34, dressed in big words 10 (small asks; one small sounding new product, n05), ambiguous 5 (expected first step `ask`). Expected first step is one of: answer, do, brief, round, ask.

The five accepted lists (r01 to r03, d03, s03) were set before the first full run, after a three prompt trial. No expectation changed after a full run.

Generic only: a stand in standing brief (`formwork/evals/routing/standing.md`) describing a document search product. `kit-leak-scan` is green.

### The runner

`formwork/evals/routing/run`. Each prompt goes to `claude -p --safe-mode --model haiku --tools "" --no-session-persistence --output-format json`, from an empty temporary folder. Safe mode drops CLAUDE.md, skills, hooks, plugins and MCP. The system prompt holds the stand in standing brief, an empty `docs/routing.md`, `formwork/route.md` and `formwork/roles/method/director.md`, and asks for a final JSON line `{"kind", "size", "first"}`. Six in parallel. `--model`, `--only`, `--out`, `--dry-run` (validates the set, sends nothing). Exit 0 only when every prompt passes.

It cannot tell whether the words said back match the JSON line, or whether the brief that would follow is good. It scores the choice only.

### Runs

| Run | Setup | Command | Result | Cost | Failed |
|---|---|---|---|---|---|
| trial | before | `formwork/evals/routing/run --only f01,a01,n01` | 2 of 3 | $0.0050 | n01 |
| 1 | table before | `formwork/evals/routing/run --out docs/evals/0026-run1-haiku.json` | 38 of 49 | $0.0280 | f06 c09 c10 r01 r07 d02 n03 n04 n05 s01 s02 |
| 2 | table fixed | `formwork/evals/routing/run --out docs/evals/0026-run2-haiku.json` | 45 of 49 | $0.0366 | c10 r02 r05 r07 |
| 3 | table fixed, runner wording | `formwork/evals/routing/run --out docs/evals/0026-run3-haiku.json` | 44 of 49 | $0.0351 | q04 c09 r05 r07 n04 |
| 4 | same as 3 | `formwork/evals/routing/run --out docs/evals/0026-run4-haiku.json` | 45 of 49 | $0.0262 | f06 r06 r07 d02 |

Every answer, with its full text, is in `docs/evals/0026-run*-haiku.json`.

### Run 1 failures by kind

- New product (3): n03, n04, n05 routed milestone correctly but first step round. The table row said "`templates/brief.md` for the first brief, a round when a choice is open", and a new product always has an open choice. Clear gap.
- Small asks in big words (4): f06 (fix routed as a round, a size the table never gives a fix), c10 (change routed checkpoint), r07 (research routed round), s01 (asked). Nothing in the table said to size the work, not the words. Clear gap.
- Change (1): c09 asked whether "complete redesign" or the 404 text was meant. Defensible, same root as above.
- Runner limits (3): r01 and d02 asked for a detail the session would read from the repository (which framework, which report). s02 answered the question at length and gave no JSON line.

### What changed in the table

- New product row: "`templates/brief.md` for the first brief: a one page spec from the person's words. A round comes later, when the spec leaves a choice open". This matches the page's own milestone example.
- Under Size: "Size the work, not the words": named words do not make an ask bigger or smaller; when words and work disagree, the work wins, and the size picked is said; ask only when the work itself is unclear.
- Top of the page: the measured number, the command, the noise of about three, the one persistent failure, the before score and why, and what the number does not show.
- "What this cannot do": now points at the prompt set.

### What changed in the runner between runs 2 and 3

One sentence: a real session could read the repository, so where a detail would come from reading it, assume it will be read after routing and do not ask. It targeted r02 and r05 asking for a library name. Run 3 did not improve (44); r05 still asked and q04 now refused to count briefs without the folder. Kept, because it is closer to a fresh session that has the files, but it is not shown to help.

### Also changed

- `formwork/roles/method/director.md`: the NOT ESTABLISHED line now points at the measured number on `formwork/route.md`. Regenerated with `formwork/fw roles --all`: "86 generated file(s) considered (84 role, 2 skill), 3 written, for: claude-code, codex, gemini-cli".
- `CHANGELOG.md`: the Unreleased routing line carries the number; two new lines for the eval and the table changes.

### What was run

- `formwork/evals/routing/run --dry-run`: "49 prompt(s), set is valid. Nothing was sent."
- `formwork/fw test`: "557 tests, all passed".
- `formwork/fw check`: "GATE: red. 1 check(s) failed on the project, 0 input(s) wrongly accepted, 0 wrongly rejected." The one is `work-paired` on the 0025 read-back, above. The other 13 are ok, including `kit-leak-scan` and `kit-integrity`.
- `grep -n "[—–]"` over every file written: no hits.

### Not done, not asked

- No test suite for the runner in `formwork/fw test`; it needs a model to run. `--dry-run` validates the set offline.
- Not run with any other model, or against a project with real corrections in `docs/routing.md`.
- `docs/standing.md` not touched: it is the director's.
- r07's expected answer left as task. Whether a round is right there is his call.

accepted: 2026-11-15
in my words: b, everything is already working, no need to disrupt them now (he committed 6223baf; keep the CSV prompt's expected answer as a small task)
