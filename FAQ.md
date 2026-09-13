# Questions people ask

> **`command not found: formwork`?** Every command here has a second form that
> needs nothing installed.
> [`formwork/troubleshooting.md`](formwork/troubleshooting.md) has both.

---

## The basics

### Do I need to be a programmer?

No. You need to be able to run a command in a terminal. That is the only skill
assumed here. You do not need to know how a project is supposed to be run: that
is the part this brings.

### What does it actually do?

Three things. It gives your agent a team to work as instead of one general
assistant. It gives the work an order, so the same steps happen every time. And
it blocks some things outright, so a few mistakes cannot happen at all.

### Is this a framework?

No. It is a folder of text files and small programs. Nothing imports it,
nothing runs it as a library, and you can delete any part you do not want.

### Why can my agent not commit my code?

Because an agent that commits will eventually commit something you did not
read. You commit, the agent works. If you disagree, it is one line in
`.formwork.toml`.

### Will this slow me down?

Yes, in one way: every piece of work stops and waits for you. On a busy day
that is the bottleneck, and it is also the point. Everything else is fast. The
gate takes about three seconds, measured in
[`formwork/COSTS.md`](formwork/COSTS.md).

---

## Using it

### How do I start a piece of work?

Write a brief. Six short headings, in
[`formwork/templates/brief.md`](formwork/templates/brief.md). Then ask your
agent to do it.

The rest of the loop is in
[`formwork/loop.md`](formwork/loop.md).

### How many conversations do I need to keep open?

Two kinds. One director thread, which decides what happens next and reads the
reports. One working session per piece of work, in the repository, which does
that one thing and stops.

The director is a role, `formwork/roles/method/director.md`. Inside your coding
tool, ask for it by name. Anywhere else, paste the file.

You carry the text between them. The plan does not live in the chat window: it
lives in `docs/standing.md`, so closing the window costs you nothing.

[`formwork/threads.md`](formwork/threads.md) has the whole shape.

### How do I use one of the roles?

On Claude Code, ask for it by name in plain words:

```
Use the challenger on this plan. Tell me what is wrong with it.
```

The roles are installed where your tool looks for them. On the other three
tools this is documented but untested.

### Do I have to use all twenty eight roles?

No. Most people will use four or five. The rest sit there until you hit a
situation that needs one.

### Can I delete roles I do not want?

Yes, and it takes two steps. Delete the source file in `formwork/roles/`,
then delete its generated copies:

```
rm formwork/roles/packs/mobile.md
rm .claude/agents/mobile.md
formwork roles
```

**If you forget the second one**, the gate goes red and tells you: a generated
file with nothing producing it. That is the check doing its job.

### Can I write my own?

Yes, and you should. Copy
[`formwork/roles/TEMPLATE.md`](formwork/roles/TEMPLATE.md) and read
[`formwork/roles/HOW-TO-ADD-A-ROLE.md`](formwork/roles/HOW-TO-ADD-A-ROLE.md).

The kit will refuse a role that does not say what it owns.

### What is a round, and do I need one?

Several agents on the same question at once, arguing, with one document at the
end. It costs real money, so use one only when a decision is expensive to undo.
See [`formwork/round.md`](formwork/round.md).

### How much does this cost to run?

**Nobody has measured it.** [`formwork/COSTS.md`](formwork/COSTS.md) says so
and says what would settle it. Set a spending limit with your provider; nothing
here can do that for you.

---

## Trust and safety

### Can I trust this to stop my agent doing damage?

> [!WARNING]
> **Partly.** The guards stop the normal path. Somebody who wants around them
> can get around them. [`formwork/limits.md`](formwork/limits.md) lists every
route anybody has found. If you need real containment, use a sandbox.

### Does it send my code anywhere?

No. There is no network code in the kit at all. Your agent talks to its
provider as it always did, which is between you and them.

### Does it change my project?

It adds and never removes. Install writes your settings, your hook wiring and
your role files, and one file outside your project in `~/.formwork/`.
[`formwork/first-run.md`](formwork/first-run.md) says what that last one is for.

### Why did the agent ignore my style file?

Because nothing makes it obey one. `docs/style.md` is a document, and documents
are advice. The only thing a check can prove is that every role points at the
page, which it does.

If it keeps happening, say so in the turn. A style file is a default, not a
rule that refuses.

### Why does it keep asking me to run `formwork record`?

Because you changed a file that enforces something, and that is a decision a
person makes. If it happens constantly you are editing the kit itself, which is
fine.

---

## The project

### Where did it come from?

It was pulled out of two real projects that were already being run this way.
Nothing here is theoretical. Every rule is in the kit because something went
wrong without it.

Its failures are written down in [`docs/dogfood.md`](docs/dogfood.md). Read that
before you decide what you think of the rest.

### Is it stable?

The guards and checks have 356 tests and five audit rounds behind them. Every
check has been watched failing on purpose, and you can watch them yourself with
`formwork demo`.

### Does it work on Windows?

**Unknown.** The guards assume a unix shell. Nobody has tried.

If you get it working, that is a real contribution.

### Does it work with my tool?

Claude Code has been watched refusing a real command. Codex, Cursor and Gemini
CLI are documented by their publishers and untried.

**Trying one is the single most useful thing you can do for this project.**
Wire it up, ask your agent to commit something, and say what happened.

### Can I use it at work?

MIT licence. Yes.

It was built around one person and their agents. Teams may well find it
useful, and a team version is not a goal yet, so expect to adapt it.

### How do I get help?

Open an issue. The most useful ones contain the exact message you saw and the
command you ran.
