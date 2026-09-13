# Words this kit uses

Plain meanings, collected so you never have to go looking.

---

## The main ones

**Agent**
A program that does work for you using an AI model. You tell it what you want
in plain words. It reads files, writes files and runs commands. Claude Code,
Codex, Cursor and Gemini CLI are agents.

**Runtime**
The particular agent tool you use. This kit supports four of them. You tell it
which one you have in `.formwork.toml`.

**Role**
A job description for an agent. One file. It says what that job owns, what it
does not own, when it should stop, and what bad work from it would look like.
This kit ships twenty eight.

**Guard**
A small program that refuses. Two of the three stop a command before it runs.
The third stops a turn from ending while the gate is red. Not a warning.

**Check**
A small program that reads your project and says green or red. Checks look at
what is there. Guards stop what is about to happen.

**The gate**, also called **the aggregate**
All twelve checks, run together, with one answer at the end. Green or red.

You will see the word aggregate in a refusal: *the aggregate is red, so this
turn cannot conclude*. It means the same thing.

**Adapter**
The instructions for wiring the guards into one particular agent. One folder
per agent, in `formwork/adapters/`.

**Frontmatter**
The block at the very top of a role file, between two lines of three dashes.
It holds the name, the pack, the owns slug and the tools. A role without it
does not load.

**Slug**
A short name with no spaces, used as an identifier. `owns: what-runs-on-a-
server` is a slug. Two roles may not use the same one.

**Turn**
One exchange. You ask for something, the agent works, the agent replies. The
gate runs at the end of every turn where something changed.

---

## Words about the work

**Brief**
What you want, written down before any work starts. Six short headings. The
template is in `formwork/templates/brief.md`.

**Style**
How an agent writes a reply, as against what it does. The kit's default is
`formwork/style.md`. Your own goes in `docs/style.md` and wins where the two
disagree. Nothing enforces either.

**Report**
What came back. What was done, what was skipped, what the agent thinks you
should know. The template is in `formwork/templates/report.md`.

**Round**
Several agents looking at the same question at once, arguing, and one document
coming out. Expensive. Only worth it for a decision you cannot easily undo. See
`formwork/round.md`.

**Predictions**
What the challenger expects to go wrong, written before anybody proposes anything.
Written after the fact it is not a prediction, it is agreement.

**Standing brief**
`docs/standing.md`. One short file saying where the project is right now, so a
new conversation does not have to be told. What goes in it:
`formwork/templates/standing.md`.

**Director**
The role that owns what happens next. One per project, one at a time.

**Director thread** and **working session**
The two layers: the one that plans and the one that builds. You carry the text
between them. See `formwork/threads.md`.

**Split brief**
One piece of work that is too big for a single session, cut into pieces by
`lead`, handed to different roles, and collected back into one report.

**Decision record**
One page saying what was decided, why, and what follows from it. Numbered.
Never edited afterwards. If it changes later, a new one replaces it and both
are kept.

---

## Words about the guards

**Blocked** or **refused**
The command did not run. You will see the word REFUSED and a reason.

**The version-control boundary**
The rule that your agent never commits, pushes or merges. You do that. It is
enforced by a guard, not by asking nicely.

**Self-protection**
The rule that your agent cannot quietly change the kit's own files. The guards,
the checks and the settings.

**Strength**
How hard a guard bites. Three settings: `block` refuses, `warn` lets it through
and tells you, `off` does nothing. Set in `.formwork.toml`.

**Refusal budget**
How many times the turn-end gate refuses before it steps aside. Three by
default, set by `gate_budget`. `formwork/limits.md` says why it gives up at
all.

**Fingerprint**
A short code worked out from the exact contents of a file. Change one character
and the code changes. The kit keeps one for each file that enforces something,
outside your project, so a change to a guard cannot be hidden.

---

## Words about the checks

**Fixture**
A small fake project used to test a check. Every check ships two kinds: one it
must reject, and one it must accept.

**Must-fail** and **must-pass**
Those two kinds. A check has to tell them apart. Being able to complain is not
enough.

**Green** and **red**
Green means every check passed. Red means at least one found something and
named it.

**Cannot run**
A third answer, and the most important one. The check could not do its job.
This is never treated as a pass.

---

## Words you will see in role files

**Owns**
The one thing that job is responsible for. No two roles own the same thing.

**Does not own**
What to hand to somebody else, and who.

**Stops when**
The moment that job should stop and ask you instead of guessing.

**Tools**
Which abilities a role may use: reading, writing, running commands, searching
the web, starting other agents. Only the lead may start other agents.

**Pack**
A group of related roles. The software pack, the design pack, and so on. All
roles are available today. There is no switch yet, and the kit says so.

---

## Two phrases worth knowing

**NOT ESTABLISHED**
Nobody has measured this or checked it. It is not a guess dressed up as a fact.
Where you see this, treat the thing as unknown.

**Catches**
Every rule has a line saying what it catches. If a rule cannot say what goes
wrong without it, it is an opinion, not a rule.
