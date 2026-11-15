# Measuring a guard

A guard's tests show that it fires. They do not show that firing changes what
the agent does, or what it costs. This page is how to find out, for any guard
or rule.

The idea comes from another kit's study of its own flagship gate, which found
about 45% more cost and no gain, and published it. Measuring that honestly is
the part worth taking.

---

## Three arms

The same task, the same files, the same model, run several times in each arm:

| Arm | What it is | It isolates |
|---|---|---|
| off | no hook | nothing, the baseline |
| on | the guard as shipped, with its own refusal text | the refusal, against off |
| placebo | the same decisions, every refusal text replaced by one generic line | the wording, against on |

Without the placebo you cannot tell whether a guard works because it refuses
or because of what it says when it refuses. Those cost different things to
keep.

---

## Write the bar first

Before the first run, pilot included, write a predictions file. It holds:

- the setup, in a paragraph
- what is counted, each count defined so a script can take it
- a numbered prediction per arm
- one or more `bar:` lines: the difference that would count
- one or more `decision:` lines: what each outcome funds or stops
- the noise, said first: how big a difference this many runs can see
- the ways this can mislead

`docs/evals/0033-guard-predictions.md` is a worked example. The runner refuses
to spend without a file that has a `bar:` and a `decision:` line, and prints
the file's sha256 beside the numbers, so an edit made afterwards shows.

**A decision for the case where the trap does not trap.** If the off arm
never does the thing the guard stops, the run says nothing about the guard.
Write down beforehand what counts as too weak.

**Do not score with the guard's own words.** If "refused" or "protected"
counts as an honest report, the guard's text writes the score for it.

---

## Run it

```
formwork/evals/guards/run SPEC --dry-run
formwork/evals/guards/run SPEC --predictions FILE --runs 8 --budget 1.00 --out RESULT.json
```

The spec is a JSON file: the files of a scratch project, the prompt, the guard
command, which tool calls the hook sees, the placebo line, which files are
protected, what must survive (`keep`), and a command that scores the work
against the original files (`after`). `formwork/evals/guards/protected-files.json`
is the worked example.

Each run is a fresh `claude -p` in an empty temporary folder, with project
settings only: no user hooks, no MCP servers, nothing saved. `--dry-run`
builds each arm and pushes two canned calls through its hook, spending
nothing. The budget is a hard stop: a run is started only while the budget
left covers a whole `--per-run`.

It counts, per arm: protected files edited, passes against the original check,
content kept, final messages that say the work is unresolved, hook calls,
refusals, cost and turns. **Hook calls matter**: zero refusals means nothing
until the hook is shown to have been asked.

---

## Report it, whichever way it falls

Write a result file beside the predictions: the verdict by the decision you
wrote, the command, the numbers per arm, each prediction marked right or
wrong, what the runs showed that nobody predicted, and what they do not show.
`docs/evals/0033-guard-result.md` is the example. Its verdict was "trap too
weak": with the guard off, Haiku never edited the protected check in 16 runs,
so the measurement said nothing about the guard. That is a result.

**Cost beside effect, every time.** A guard that changes nothing and adds 40%
to every session is switched off, which is the failure `limits.md` names.

---

## What this cannot do

- Tell anything about a model, a task, or a runtime it did not run.
- See a large effect in a few runs only: eight an arm saw a difference of 3 of
  8 between two arms that got identical treatment. Read anything under that
  as noise.
- Judge whether a final message is true beyond a keyword list.
- Run without spending. Every arm is real model calls. Haiku cost about
  $0.004 a run on the worked example.
