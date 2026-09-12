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

You know what you want to build. Now you need help.

You need someone to find the holes in your plan. Someone to think about how it
should be put together. Someone who knows what breaks at 3am. Someone who knows
what a screen should do. Someone who knows what a word should say. Someone who
reads the small print.

You need your choices written down. Then you will not argue about the same
thing again next month.

Most of all, you need someone who will tell you no.

That used to mean hiring people. People cost money. Hiring takes time.

**Now it is a folder you copy into your project.**

Twenty seven roles. Already written. Ready to work.

A lead to run things. A challenger to attack your plan. An architect. A researcher.
A reviewer. Engineers for the back end, the front end, phones, data, servers,
and safety. A designer. A writer. A product person. A marketer. Someone who
tells you when to call a real lawyer.

Nobody to hire. Nobody to wait for. They are in the folder.

**So the thing stopping you is not the thing you thought.**

## Who it is for

**Anyone building something with an AI agent.**

**Never run a project before?** This is the part nobody gives you. The team.
The order of work. The notes. The rules. It all works as soon as you install
it. You bring the idea.

**Done this many times?** Then you know most of it already. What is new is that
it now sits where your agents can read it. And some of it they cannot ignore.
Delete the rules you do not like. Rewrite any role you know better.

**Expert in one thing?** Your role file will be thinner than you are. Replace
it with what you know. Everything else keeps working around it.

## What you get

**A way of working.** Every job goes the same way. You say what you want. The
agent works. The checks run. It tells you what it did. Then it stops and waits
for you.

**Notes that write themselves.** Choices get a number and a page. Nothing
important is left in a chat you will close and lose.

**Rules your agent cannot ignore.** Not tips. Real refusals.

Ask your agent to save your work to git, and nothing happens:

```
you:    commit this for me
agent:  REFUSED by the version-control boundary: git commit changes
        the repository.
```

Nobody read you a rule. You watched it work.

**That is the whole idea.** You think about what you are building. The kit
holds the rest.

## Before you install

| You need | How to check |
|---|---|
| **Python 3.8 or newer** | run `python3 --version`. Mac and most Linux have it |
| **git** | run `git --version` |
| **An AI coding agent** | Claude Code, Codex, Cursor or Gemini CLI |

**No packages to install.** The kit itself is text files and small Python
programs. They use only what comes with Python.

| System | Does it work? |
|---|---|
| **macOS** | Yes. Built and used here |
| **Linux** | Should do. Nobody has tried. **Try it and tell us** |
| **Windows** | The command installs. The guards assume a unix shell and nobody has run them there. **If you get it working, that helps everyone** |

## Install

**1. Get the command.**

```
pipx install formwork-kit
```

The command is `formwork`.

**pipx is worth it here.** Plain `pip install formwork-kit` also works, but pip
often puts the command in a folder your shell does not look in, and you get
`command not found` with no obvious cause.

**Do not want to install anything?** Skip to the bottom of this section.

**2. Go to your project and set it up.**

```
cd /your/project

formwork init
formwork install --runtime claude-code
formwork check
```

That last line should say green.

**What each one did.** `init` put a `formwork/` folder and `FORMWORK.md` in your
project. `install` wired the guards into your agent and wrote your role files.
`check` ran all nine checks.

Type `formwork` on its own to see everything it can do.

### Or without installing anything

The kit is just files. Copy them in and run them by path:

```
git clone https://github.com/muhammadelsherif/formwork.git  the-kit
cp -R  the-kit/formwork  the-kit/FORMWORK.md   /your/project/

cd /your/project
formwork/fw install --runtime claude-code
formwork/fw check
```

**What it touches.** It adds `formwork/` and `FORMWORK.md`. It writes your
agent's settings file, keeping anything already in it and saving a copy first.
And it writes one file outside your project, in `~/.formwork/`, holding a
fingerprint of each file that enforces a rule. Nothing else.

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

So each check ships test cases of both kinds. At least one it must say no to,
at least one it must say yes to. It has to tell them apart.

Try it:

```
formwork demo
```

Before a check runs, its test files are copied into folders with random names.
So a check cannot pass by knowing the file name. It has to look.

## Which agents work

| Agent | Can it stop a command? |
|---|---|
| **Claude Code** | Yes. Seen doing it |
| **Codex** | It should. Nobody has tried |
| **Cursor** | It should. Nobody has tried |
| **Gemini CLI** | It should. Nobody has tried |

For the three nobody has tried, `formwork check` stays red until you set up
the hooks yourself. The file in `formwork/adapters/` for your agent tells you
what to write.

Red is the right answer there. Nothing is guarding you yet, and the kit will
not say green about that.

**Those three are the easiest way to help.** Set one up. Ask your agent to
commit something. Tell us what happened. If it said no, that turns a guess into
a fact. If it did not, we need to fix it. Either way, open an issue.

## What this will not pretend

Every number here comes with the command that made it. If something has not
been measured, the page says so in capital letters instead of guessing.

There are three of those. Know them before you fork:

**Nobody knows what a round costs in money.** Not once measured. See
[`formwork/COSTS.md`](formwork/COSTS.md). It says NOT ESTABLISHED instead of a
made up number.

**The guards stop the normal way, not a clever one.** They read the command and
look for patterns. [`formwork/limits.md`](formwork/limits.md) lists every way
around them that we found, what got fixed, and what cannot be fixed this way.
If you need real safety, use a sandbox.

**Three of the four agents are untried.** Claude Code has been seen saying no.
The other three have not.

Every time this kit failed on the person who wrote it, the failure went into
[`docs/dogfood.md`](docs/dogfood.md). Nothing was quietly patched. That page is
the best reason to trust the rest.

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

Forks are the point. Take it. Change it. Keep what you like.

If you want to send something back, these help most:

**A command that got past a guard.** One line is enough. You do not need a fix.

**A normal command that was wrongly stopped.** Just as useful. A guard that
blocks normal work is a guard people switch off. Then nothing is guarded.

**A report from an untried agent.** Codex, Cursor or Gemini CLI. Tell us if it
worked or not. Both answers help.

**A new role.** Copy `formwork/roles/TEMPLATE.md`. Read
[`formwork/roles/HOW-TO-ADD-A-ROLE.md`](formwork/roles/HOW-TO-ADD-A-ROLE.md)
first. The kit will refuse a role that does not say what it does.

### Before you open a pull request

```
formwork check    must say green
formwork demo     must say no to every broken test case
formwork test     all 295 tests must pass
```

Two house rules, taken from the kit itself:

**Change a guard or a check? Add the test that would have caught the bug.**
Then show it failing without your fix. A check nobody has seen fail proves
nothing.

**Write down a number? Write down the command that made it.**

### Good first jobs

- Set up the hooks for Codex, Cursor or Gemini CLI and tell us if they work
- Translate the first run page
- Add a role for something the twenty seven do not cover
- Find a command that gets past a guard

## Licence

MIT. See [LICENSE](LICENSE).
