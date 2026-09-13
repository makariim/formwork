---
updated: 2026-09-13
---

# What still needs writing

Live, not history. A running list of documentation owed, filled in as we build
version two, so nothing is remembered only in a chat window.

**This file is meant to be emptied and deleted.** One of the kit's own rules
warns against a "later" file that only grows, and this is one. The defence is
that it has an end: when version two ships, every line here is either written
or dropped with a reason, and the file goes.

Nothing here is a decision. It is a list of writing owed.

---

## Owed from work already done

| What | Where it lands | Why it is not written yet |
|---|---|---|
| The worked example: two windows, what you type, who reads what | `formwork/threads.md`, at the end | deferred on purpose, docs pass comes last |
| Lead can now split a brief, not only run rounds | `formwork/round.md` mentions only rounds. `formwork/loop.md` says nothing about splitting | written in the role, not yet in the pages that point at the role |
| **Splitting a brief has never been run.** NOT ESTABLISHED | `formwork/limits.md` | the claim is true today and must be stated where limits live |
| The two layers are missing from the one page summary | `FORMWORK.md` | the loop diagram shows one layer only |
| A round now takes a number in `docs/briefs/` and leaves a report | `formwork/loop.md` and `formwork/first-run.md` still describe rounds as living only in `docs/rounds/` | decided today |
| Briefs and reports now live in `docs/briefs/` and `docs/reports/` | `formwork/loop.md`, `formwork/first-run.md`, `README.md` | the folder landed after those pages were written |
| **Nobody has run the folder route.** NOT ESTABLISHED | `formwork/limits.md` | built today |
| The upper layer is now the `director` role, not a pasted block | `formwork/loop.md`, `formwork/first-run.md` and `formwork/round.md` do not mention it. `README.md` names roles but not what the director does | the role landed after those pages were written |
| **The director role has never been run.** NOT ESTABLISHED | `formwork/limits.md` | written today, used by nobody |

## Owed from work still to come

| What | Where it lands |
|---|---|
| How agents report to you: length, tone, what a report always says | a new page, and every role reads it |
| Skills: what they are, the six of them, how they are generated | `README.md`, `FORMWORK.md`, `formwork/glossary.md` |
| Model, effort and colour per role, and which runtimes support each | `docs/role-formats.md`, `docs/runtime-capabilities.md`, the roles page |
| The questions `formwork init` asks a first timer | `formwork/first-run.md`, `README.md` |
| **Settings.** The README does not use the word configuration once. Nobody is told when to change a setting, or where | `README.md`, and `FORMWORK.md` has the file but not the when |
| This is version one, and version two is coming | `README.md` |

## Asked for by people who tried it

Two people outside the project read it and ran it. This is what they said.

| What | Where it lands |
|---|---|
| **Split the install section in two.** A packaged install, and "install nothing, the kit is just files". Right now they are one run of text and the second one reads like an afterthought | `README.md` |
| **`pipx` is not the only answer.** A virtual environment is the ordinary way to do this and the page does not mention one | `README.md` |
| **Show how to actually instruct an agent.** One or two worked examples of starting a project with the kit. Whoever forks this already knows how to use an agent. What they do not know is what to type on the first turn | `README.md`, and `formwork/first-run.md` |
| The repository has no About text, no website and no topics on GitHub | not a file. A setting on the repository page |

## Owed from the style page

| What | Where it lands |
|---|---|
| `formwork/style.md` exists and every generated role points at it | `README.md` names it in the map but does not say what it is for. `formwork/loop.md` says nothing about how a report is written |
| `docs/style.md` beats the kit default, and the kit only checks that the pointer exists, never that the style is followed | `FAQ.md`. Somebody will ask why the agent ignored their style file |
| `style-pointed` is the twelfth check | `formwork/glossary.md` counts them, `docs/design.md` and `docs/gap-map.md` are history and stay as written |

## Owed from setup

| What | Where it lands |
|---|---|
| `formwork setup` exists, asks five questions, and writes `docs/style.md` and `docs/standing.md` | `README.md` and `formwork/first-run.md` still send people straight from install to check |
| **Nobody outside has run setup.** NOT ESTABLISHED | `formwork/limits.md` |

## Small things owed

| What | Where |
|---|---|
| `formwork/install` run from a subfolder writes its configuration into that subfolder | fix first, then say so |
| `formwork/fw test` does not print a total, `formwork test` does | fix first |
| Em dashes across the twenty eight role files | the role sources, then regenerate |
| Numbers in `docs/` that are now stale | they are history and say so. Decide whether that is enough |
