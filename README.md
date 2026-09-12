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

## Ideas do not die at the idea

They die at what comes next.

You need someone to find the holes in your plan. Someone who knows what breaks
at 3am, what a screen should do, what the small print means. You need your
choices written down so you are not arguing about them again next month. Most
of all you need someone who will tell you no.

That used to mean hiring people. People cost money. Hiring takes time.

**Now it is a folder you copy into your project.**

Twenty seven roles, already written. A lead, a challenger, an architect, a
researcher, a reviewer. Engineers for the back end, the front end, phones,
data, servers and safety. A designer, a writer, a product person, a marketer.
Someone who tells you when to call a real lawyer.

Nobody to hire. Nobody to wait for. They are in the folder.

## Who it is for

**Anyone building something with an AI agent.**

**New to this?** The team, the order of work, the notes and the rules all
arrive working. You bring the idea.

**Done it many times?** Now it sits where your agents can read it, and some of
it they cannot ignore. Delete the rules you disagree with. Rewrite any role you
know better.

**Expert in one thing?** Your role file will be thinner than you are. Replace
it. Everything else keeps working around it.

## What you get

**A way of working.** You say what you want. The agent works. The checks run.
It tells you what it did, then stops and waits for you.

**Notes that write themselves.** Choices get a number and a page, instead of
living in a chat you will close and lose.

**Rules your agent cannot ignore.** Not tips. Real refusals.

```
you:    commit this for me
agent:  REFUSED by the version-control boundary: git commit changes
        the repository.
```

Nobody read you a rule. You watched it work.

## Install

| You need | Check it |
|---|---|
| **Python 3.8 or newer** | `python3 --version` |
| **git** | `git --version` |
| **An AI coding agent** | Claude Code, Codex, Cursor or Gemini CLI |

No packages, no setup. The kit is text files and small Python programs.

```
pipx install formwork-kit

cd /your/project
formwork init
formwork install --runtime claude-code
formwork check
```

That last line should say green.

`init` puts `formwork/` and `FORMWORK.md` in your project. `install` wires the
guards into your agent and writes your role files. Type `formwork` on its own
to see the rest.

**Use pipx, not pip.** Plain pip works, but often puts the command somewhere
your shell does not look, and you get `command not found` with no clue why.

**Or install nothing.** The kit is just files:

```
git clone https://github.com/makariim/formwork.git  the-kit
cp -R  the-kit/formwork  the-kit/FORMWORK.md   /your/project/

cd /your/project
formwork/fw install --runtime claude-code
formwork/fw check
```

**What it touches.** It adds `formwork/` and `FORMWORK.md`, writes your agent's
settings file keeping anything already there, and puts one file in
`~/.formwork/` holding a fingerprint of each file that enforces a rule.

| System | Does it work? |
|---|---|
| **macOS** | Yes. Built and used here |
| **Linux** | Should do. Nobody has tried. **Try it and tell us** |
| **Windows** | The command installs. The guards assume a unix shell and nobody has run them there |

## What is inside

| | | count it yourself |
|---|---|---|
| **3 guards** | small programs that refuse. Two stop a command, one stops a turn ending | `ls formwork/guard \| grep -v test_` |
| **9 checks** | small programs that read your project and say green or red | `ls formwork/check/checks \| wc -l` |
| **27 roles** | one file each, saying what that job does and where it stops | `ls formwork/roles/*/*.md \| wc -l` |
| **46 rules** | 13 you meet daily, 33 for when you need them | `grep -c '^### ' formwork/rules/*.md` |
| **295 tests** | every guard and check, proved able to fail | `formwork test` |

It is all text files and small programs. You can read every line. Nothing is
hidden. Nothing is sent anywhere.

## Every check has been watched failing

A check nobody has seen fail proves nothing.

So each check ships test cases of both kinds: at least one it must reject, at
least one it must accept. It has to tell them apart. Watch it yourself with
`formwork demo`.

## Which agents work

| Agent | Can it stop a command? |
|---|---|
| **Claude Code** | Yes. Seen doing it |
| **Codex** | It should. Nobody has tried |
| **Cursor** | It should. Nobody has tried |
| **Gemini CLI** | It should. Nobody has tried |

For the three nobody has tried, `formwork check` stays red until you write the
hook file yourself. Your agent's page in `formwork/adapters/` says what goes in
it. Red is the right answer there: nothing is guarding you yet.

**Those three are the easiest way to help.** Set one up, ask your agent to
commit something, and tell us what happened. Either answer is useful.

## What this will not pretend

Every number here comes with the command that made it. Anything unmeasured says
so in capitals rather than guessing. There are three:

**Nobody knows what a round costs in money.**
[`formwork/COSTS.md`](formwork/COSTS.md) says NOT ESTABLISHED instead of a made
up number.

**The guards stop the normal way, not a clever one.**
[`formwork/limits.md`](formwork/limits.md) lists every way around them anybody
has found. If you need real safety, use a sandbox.

**Three of the four agents are untried.**

Every time this kit failed on the person who wrote it, the failure went into
[`docs/dogfood.md`](docs/dogfood.md) instead of being quietly patched. That page
is the best reason to trust the rest.

## Where to start

[`formwork/first-run.md`](formwork/first-run.md). Seven short steps, on your
own project. No tutorial. No pretend example.

It should take about fifteen minutes. Nobody has timed the part you do, and the
page says so.

## The rest

| | |
|---|---|
| [`FORMWORK.md`](FORMWORK.md) | the whole method on one page. Read it after your first run |
| [`formwork/loop.md`](formwork/loop.md) | how one job goes, start to finish |
| [`formwork/round.md`](formwork/round.md) | how to run a round, and when it is worth it |
| [`formwork/rules/`](formwork/rules/) | the rules, each saying what it catches |
| [`formwork/roles/`](formwork/roles/) | the roles, and how to write your own |
| [`formwork/templates/`](formwork/templates/) | brief, predictions, report, decision, round |
| [`formwork/glossary.md`](formwork/glossary.md) | every word we use, in plain language |
| [`formwork/troubleshooting.md`](formwork/troubleshooting.md) | every error message and what to do |
| [`formwork/limits.md`](formwork/limits.md) | what this kit cannot do |
| [`FAQ.md`](FAQ.md) | questions people ask |
| [`docs/`](docs/) | how it was built, and what broke |
| [`RELEASING.md`](RELEASING.md) | for the maintainer, how a version gets published |

## Contributing

Forks are the point. Take it, change it, keep what you like.

What helps most, in order:

- **A command that got past a guard.** One line is enough, no fix needed.
- **A normal command that was wrongly stopped.** Just as useful. A guard that
  blocks real work is a guard people switch off.
- **A report from an untried agent.** Codex, Cursor or Gemini CLI. Worked or
  not, both answers help.
- **A new role.** Copy `formwork/roles/TEMPLATE.md` and read
  [`HOW-TO-ADD-A-ROLE.md`](formwork/roles/HOW-TO-ADD-A-ROLE.md) first.

Before you open a pull request:

```
formwork check    must say green
formwork demo     must reject every broken test case
formwork test     all 295 must pass
```

Two house rules, taken from the kit itself. **Change a guard or a check, and
add the test that would have caught the bug**, shown failing without your fix.
**Write down a number, and write down the command that made it.**

## Licence

MIT. See [LICENSE](LICENSE).
