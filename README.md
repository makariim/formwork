<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo-light.svg" width="96" alt="">
</picture>

# Formwork

**You bring the idea. It brings the whole team.**

*Not a typo. Builders use formwork to hold a shape until it can stand on its
own. Projects never had that. Now they do.*

[![licence](https://img.shields.io/badge/licence-MIT-green.svg)](LICENSE)

</div>

---

<div align="center">

| A team | A way of working | Rules that refuse |
|:--:|:--:|:--:|
| everyone a project needs | brief, work, check, report, stop | some mistakes cannot happen |

</div>

```console
$ pipx install formwork-kit
$ formwork init && formwork install
$ formwork setup && formwork check
GATE: green. 12 check(s), each shown to reject the wrong and accept the right.
```

<div align="center">

[Which agent you use](#which-agent-you-use-changes-what-you-get) ·
[Install](#install) · [Your first turn](#your-first-turn) ·
[Settings](#settings) · [What is inside](#what-is-inside) ·
[What it will not pretend](#what-this-will-not-pretend) ·
[Version one](#this-is-version-one) ·
[Where to go next](#where-to-go-next)

</div>

---

## Ideas do not die at the idea

They die at what comes next.

You need someone to find the holes in your plan. Someone who knows what breaks
at 3am, what a screen should do, what the small print means. You need your
choices written down so you are not arguing about them again next month. Most
of all you need someone who will tell you no.

That used to mean hiring people. People cost money. Hiring takes time.

**Now it is a folder you copy into your project.**

Twenty eight roles, already written. A director, a lead, a challenger, a
researcher, a reviewer. Engineers for the back end, the front end, phones,
data, servers and safety. A designer, a writer, a product person, a marketer.
Someone who tells you when to call a real lawyer.

Nobody to hire. Nobody to wait for. They are in the folder.

---

## Who it is for

**Anyone building something with an AI agent.**

**New to this?** The team, the order of work, the notes and the rules all
arrive working. You bring the idea.

**Done it many times?** Now it sits where your agents can read it, and some of
it they cannot ignore. Delete the rules you disagree with. Rewrite any role you
know better.

**Expert in one thing?** Your role file will be thinner than you are. Replace
it. Everything else keeps working around it.

---

## What you get

**A way of working.** You say what you want. The agent works. The checks run.
It tells you what it did, then stops and waits for you.

**Notes that stay put.** Choices get a number and a page in your repository,
instead of living in a chat you will close and lose.

**Rules your agent cannot ignore.** Not tips. Real refusals.

```console
you:    commit this for me
agent:  REFUSED by the version-control boundary: git commit changes
        the repository.
```

Nobody read you a rule. You watched it work.

> [!IMPORTANT]
> That is the whole idea. You think about what you are building. The kit holds
> everything else.

---

## Which agent you use changes what you get

Read this before installing. It decides whether your first `formwork check`
comes back green.

| Agent | Can it stop a command? |
|---|---|
| **Claude Code** | Yes. Seen doing it |
| **Codex** | It should. Nobody has tried |
| **Cursor** | It should. Nobody has tried |
| **Gemini CLI** | It should. Nobody has tried |

**On Claude Code everything below works as written.**

**On the other three, the install finishes and `formwork check` comes back
red**, because the file that hooks the guards into your agent does not exist
yet and you have to write it. Your agent's page in `formwork/adapters/` says
exactly what goes in it. **Red is the honest answer there: nothing is guarding
you yet.**

Everything else works on all four from the start: the roles, the rules, the
checks, the templates, the loop.

**Setting one of those three up is the most useful thing anybody can do for
this project.** [CONTRIBUTING.md](CONTRIBUTING.md) says what to send back.

---

## Install

| You need | Check it |
|---|---|
| **Python 3.8 or newer** | `python3 --version` |
| **git** | `git --version` |
| **An AI coding agent** | Claude Code, Codex, Cursor or Gemini CLI |

**Two ways in. They end in the same place.**

### 1. As a package

```
pipx install formwork-kit
```

pipx puts the `formwork` command on your path and keeps it in its own
environment, away from your project's packages. Then, in your project:

```
cd /your/project
formwork init
formwork install --runtime claude-code    # or codex, cursor, gemini-cli
formwork setup
formwork check
```

**That last line should say green on Claude Code**, and red on the other three
until you write the hook file, as above.

Leave `--runtime` off and it finds your agent itself. It only asks when you
have more than one set up, or none yet.

> [!TIP]
> **Would you rather be walked through it?**
> [`formwork/first-run.md`](formwork/first-run.md) is the same five commands
> with somebody explaining each one: what it writes, what the exit codes mean,
> what to do when your agent cannot block, and a first piece of real work at
> the end. About fifteen minutes.

<details>
<summary><b>Other ways to install the package, and what to do when the command is not found</b></summary>

<br>

**In a virtual environment**, where the command lives inside it:

```
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python3 -m pip install formwork-kit
```

**With pip directly, say `python3 -m pip install formwork-kit`.** Typing `pip`
or `pip3` can reach a different Python than the one you run, and then the
package installs somewhere your `python3` never looks.

**If `formwork` says `command not found`,** it installed fine and the command
landed in a folder your shell does not search. You do not have to fix your
path. Either of these works instead:

```
python3 -m formwork_cli check      the same command, run through Python
formwork/fw check                  the kit's own command, needs no install
```

The second one only works after `formwork init`, because that is what puts the
kit in your project. If you never got that far, use the first one, or install
with pipx and start again.

</details>

### 2. As files, with nothing installed

**There is no package to install and nothing to import.** The kit is text files
and small Python programs, and it runs from where it sits.

```
git clone https://github.com/makariim/formwork.git the-kit
cp -R the-kit/formwork the-kit/FORMWORK.md /your/project/

cd /your/project
formwork/fw install --runtime claude-code    # or codex, cursor, gemini-cli
formwork/fw setup
formwork/fw check
```

The copy is the whole kit, so you can delete `the-kit` afterwards. There is no
`init` step here, because copying the folder in **is** the init step.

Every other command exists both ways: `formwork check` becomes
`formwork/fw check`. Run `formwork/fw` on its own for the list.

### What each step does

| | |
|---|---|
| `init` | puts `formwork/` and `FORMWORK.md` into your project |
| `install` | wires the guards into your agent, writes your role files. Add `--runtime <name>` when it cannot tell |
| `setup` | asks eleven questions once, then writes your style file, your standing brief, and the folders for decisions, briefs and reports |
| `check` | runs all twelve checks and says green or red |

**What it touches.** It adds `formwork/` and `FORMWORK.md`, writes your agent's
settings file keeping anything already there, and puts one file in
`~/.formwork/` holding a fingerprint of each file that enforces a rule.

| System | Does it work? |
|---|---|
| **macOS** | Yes. Built and used here |
| **Linux** | Should do. Nobody has tried. **Try it and tell us** |
| **Windows** | The command installs. The guards assume a unix shell and nobody has run them there |

---

## Your first turn

The kit is files, and your agent reads files. So the first turn is you telling
it to. Four that cover most of it:

**Starting something new**

> Read `FORMWORK.md` and `formwork/first-run.md`. Then use the director role to
> write me a brief for a command line tool that renames photos by the date they
> were taken. Size the brief to the work. Do not build anything yet.

*The **director** is the role that holds the plan and writes the briefs. It
never builds anything.*

**Picking up a project that already exists**

> Read `FORMWORK.md`, then `docs/standing.md`. Tell me where we are in four
> lines, and what you think the next piece of work is.

*`docs/standing.md` is the **standing brief**, the one file that says where the
project stands. `formwork setup` starts it for you. It is what stops every new
window beginning with you retelling the whole story.*

**Handing over one piece of work**

> Here is the brief. [paste it] Do only what it says, nothing next to it. Check
> your work with `formwork check`, tell me what you did, and stop there.

**Asking one role for an opinion**

> Use the security role. Read `formwork/guard/` and tell me what an attacker
> would try first.

**Then it stops and waits for you.** That is the shape, and it is the part
people are surprised by. It does not carry on to the next thing because the
next thing is obvious.

---

## Settings

One file, `.formwork.toml`, in your project. The installer writes it and
`formwork setup` fills it in by asking you.

```toml
[bindings]
runtime = "claude-code"          # which agent you use

[strength]
git_boundary = "block"           # block | warn | off
protect_files = "block"
aggregate_gate = "block"
gate_budget = 3
```

**Your file will be shorter than that**, and nothing is wrong. The installer
writes the first two `[strength]` keys. The other two have working defaults, so
they only appear once you change them. Adding them by hand works too.

| When you would change something | What to change |
|---|---|
| you moved to a different agent | `runtime` |
| a guard keeps stopping work you meant | that key to `warn`. It runs, and tells you |
| you are only trying the kit out | that key to `off` |
| a genuinely stuck turn keeps being refused | `gate_budget`, how many refusals before the gate stands aside |

**For one session only**, without editing anything:

```
FORMWORK_GIT_BOUNDARY=off
FORMWORK_PROTECT_FILES=warn
FORMWORK_GATE=off
```

**Rules are not configured here.** There is no `[rules]` section and adding one
fails a check. You drop a rule by deleting it from `formwork/rules/core.md`.
[`FORMWORK.md`](FORMWORK.md) says why it works that way.

**How the agents talk to you is not in this file.** That is
[`formwork/style.md`](formwork/style.md), and your own `docs/style.md` written
in your own words, which beats it. Every role points at both.

---

## What is inside

| | | count it yourself |
|---|---|---|
| **3 guards** | small programs that refuse. Two stop a command, one stops a turn ending | `ls formwork/guard \| grep -v test_` |
| **12 checks** | small programs that read your project and say green or red | `ls formwork/check/checks \| wc -l` |
| **28 roles** | one file each, saying what that job does and where it stops | `ls formwork/roles/*/*.md \| wc -l` |
| **47 rules** | 13 you meet daily, 34 for when you need them | `grep -c '^### ' formwork/rules/*.md` |
| **334 tests** | every guard and check, proved able to fail | `formwork test` |

It is all text files and small programs. You can read every line. Nothing is
hidden. Nothing is sent anywhere.

---

## Every check has been watched failing

A check nobody has seen fail proves nothing.

So each check ships test cases of both kinds: at least one it must reject, at
least one it must accept. It has to tell them apart. Watch it yourself with
`formwork demo`.

---

## What this will not pretend

Every number here comes with the command that made it. Anything unmeasured says
so in capitals rather than guessing. There are three:

| | |
|---|---|
| **What a round costs in money** | never measured. [`COSTS.md`](formwork/COSTS.md) says NOT ESTABLISHED instead of guessing |
| **Whether the guards stop a determined agent** | they do not. [`limits.md`](formwork/limits.md) lists every way around them |
| **Whether three of the four agents work** | nobody has tried them. Said once already, near the top, because it changes what you get |

> [!WARNING]
> The guards stop the ordinary path, not a clever one. If you need real safety,
> use a sandbox.

Every time this kit failed on the person who wrote it, the failure went into
[`docs/dogfood.md`](docs/dogfood.md) instead of being quietly patched. That page
is the best reason to trust the rest.

---

## This is version one

What is here is built and tested. What is not here, and is not being worked on
today:

| | |
|---|---|
| **Skills** | one word for a common job, instead of a paragraph. Considered, not started |
| **A model per role** | pick the model and effort level for each role. Only Claude Code is known to allow it. Nobody has checked the other three, so this would be one agent out of four until somebody does |
| **Teams** | more than one person on the same standing brief. Today the method says one director at a time, and nobody has tried two |
| **Roles invented on the fly** | asked for by somebody who tried the kit. It cuts across the check that stops two roles owning one job, so it is an open question rather than a plan |

None of these is promised. They are written down so you can see the edge of
what is here.

Version one is not a draft. It is what one person built, used, and broke on
purpose. **NOT ESTABLISHED: whether any of it works for more than one person.**

---

## Where to go next

**[`formwork/first-run.md`](formwork/first-run.md)**. It walks you through the
install, makes you watch a guard refuse something, and has you do one small
real piece of work. On your own project, not a pretend one. About fifteen
minutes.

**Then [`FORMWORK.md`](FORMWORK.md)**, the whole method on one page. It reads
better after you have run it once than before.

---

## Everything else

**While you work**

| | |
|---|---|
| [`loop.md`](formwork/loop.md) | how one job goes, start to finish |
| [`threads.md`](formwork/threads.md) | how work starts, and where the plan lives between conversations |
| [`style.md`](formwork/style.md) | how the agents talk to you, and how to change it |
| [`round.md`](formwork/round.md) | how to run a round, and when it is worth it |
| [`templates/`](formwork/templates/) | brief, predictions, report, decision, round, standing brief |
| [`roles/`](formwork/roles/) | the roles, and how to write your own |
| [`rules/`](formwork/rules/) | the rules, each saying what it catches |

**When you need it**

| | |
|---|---|
| [`troubleshooting.md`](formwork/troubleshooting.md) | every error message and what to do |
| [`glossary.md`](formwork/glossary.md) | every word we use, in plain language |
| [`limits.md`](formwork/limits.md) | what this kit cannot do |
| [`COSTS.md`](formwork/COSTS.md) | what it costs, and the number nobody has |
| [`FAQ.md`](FAQ.md) | questions people ask |

**How it was built**

| | |
|---|---|
| [`docs/`](docs/) | the survey, the design, and what broke |
| [`docs/dogfood.md`](docs/dogfood.md) | the kit failing on its own author, written down |
| [`RELEASING.md`](RELEASING.md) | for the maintainer |

---

## Contributing

Forks are the point. The most useful thing you can send is a command that got
past a guard, or one that was stopped when it should not have been.

[CONTRIBUTING.md](CONTRIBUTING.md) has the rest, and
[SECURITY.md](SECURITY.md) is for anything you would rather not post in public.

---

## Licence

MIT. See [LICENSE](LICENSE).
