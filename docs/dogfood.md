# Dogfood log

**Phase:** K8. Running since B3.

What broke, or got in the way, while the kit was being built with the kit.
Written as it happens, not tidied up afterwards.

**This is the only evidence this kit will ever have.** One person, one project,
and the person wrote the method. A kit used on a new kind of project that
produces no friction was not really used, so an empty log here would be the
finding, not a success.

---

## 1 — A check found its own broken examples

**When.** B1, first run of the gate.

**What happened.** The link checker was pointed at the project and immediately
reported two broken links. Both were in its own fixtures — the inputs that
exist to be broken.

Correct behaviour. Wrong result.

**What it cost.** Ten minutes.

**What changed.** The runner now tells each check which paths to stay out of,
through the environment. **The runner decides what is out of bounds; the check
obeys.** A check must not carry knowledge of where the kit keeps things.

**Would not have been found by.** Reading the code. It needed running.

---

## 2 — A rule format broke on a full stop

**When.** B3, first run of the rule checker.

**What happened.** All 46 rules failed at once, reported as "neither Enforced
nor Advice".

The rules were fine. The checker demanded `**Advice**` and the files said
`**Advice.**`. One full stop, inside the bold.

**What it cost.** Five minutes, and a moment of believing 46 files were wrong.

**What changed.** The pattern matches the word, not the punctuation around it.

**The general lesson.** A format that is strict about punctuation will be broken
by a human being polite. Match intent.

---

## 3 — The copy scan caught the author four times

**When.** B3, B4, B5, and the inventory before them.

**What happened.** Writing the kit's own documents produced passages that
matched the private source repositories word for word — 51 in the inventory, 16
in the rules, 10 in the templates, 1 in a role.

Every one was written in the sincere belief it was original.

**What it cost.** Four rewrites.

**What changed.** Nothing in the kit. This is the check working exactly as
intended, repeatedly, against the person who wrote the check.

**The finding.** Discipline did not work. Not once. **The single strongest piece
of evidence in this log is that the author of a rule could not follow it
unaided.**

---

## 4 — The boundary refused a legitimate command

**When.** Immediately after B5, reading a background job's output.

**What happened.** `git sparse-checkout set …` was refused, because
`sparse-checkout` is not on the read-only list and an unknown subcommand is
refused rather than waved through.

**The command was harmless.** It was shaping a throwaway clone in a temporary
directory, not touching this project at all.

**What it cost.** One command, and the work was finished another way — the
output was already on disk and could be read without git.

**What was NOT done, deliberately.** The boundary was not switched off to get
past it. Editing a check because it just failed is the exact failure the rule
exists to prevent, and doing it here would have made this log worthless.

**The real finding, which is bigger than a missing word.** The guard has no idea
*which repository* a command touches. It refused an operation on an unrelated
clone in a temporary directory. The boundary is about the history of the project
you are working on; it is currently about the word `git` anywhere.

**Two possible answers, neither taken yet:**

- add `sparse-checkout` and its like to the read list — treats the symptom
- make the guard notice which repository is being touched — treats the cause,
  and is harder than it sounds, because a command can name a path or inherit
  one

**Status: open.** It belongs in B6 or later, and it is not being fixed now
because B5 is finished and B6 is not authorised.

**What this says about the guard.** It fails closed, loudly, on something safe.
That is the trade that was chosen on purpose, written into the file at the time:
loud and wrong beats quiet and wrong. This is what paying that price looks like,
and it is worth knowing it costs about one command a day.

---

## 5 — The audit, and what it found about this log

**When.** After B5, on request, with fresh eyes over everything.

**What happened.** Eleven findings. The three that matter here:

**The gate could be fooled.** A check that ignores its input and rejects
anything named "broken" passed, while examining nothing. Requiring one broken
input proves a check can say no; it does not prove the check looked. Fixed two
ways: every check now ships an input it must *accept* as well as one it must
reject, and fixtures are copied under a random name before the check sees them,
so recognising the name is no longer available.

**A hanging check hung the gate for ever.** In a hook that freezes the agent
until somebody kills it. Every check now has a deadline, and overrunning is
"could not run", never "fine".

**The allowlist had been quietly poisoned.** 197 entries, most added in bulk
without reading them, including seventeen genuine words from the source
projects. Sixteen of those seventeen were *dead* — kept for text that no longer
existed, while still blinding the scan everywhere.

Rebuilt from what a run with an empty allowlist actually needs: 47 generic
terms allowed anywhere, 218 scoped to the single file where each was reviewed.
A term appearing anywhere new now fires again.

**What it cost.** A morning.

**The finding underneath all three.** Every one of them is the same mistake:
**making the check quieter because it was inconvenient.** Not deliberately —
each individual allowlist entry was a reasonable-looking response to an
annoying scan. The aggregate was a hole.

This is the second time this log records the author of a rule failing to follow
it. The first was copying. This one is worse, because it was done *to the
check itself*.

## 6 — The installer could not tell what this project runs

Found the first time `formwork/install --dry-run` was pointed at this
repository. It refused:

```
Cannot tell which runtime this project uses: more than one runtime is set
up here: claude-code, codex, gemini-cli.
```

It is right, and the cause is the kit itself. `formwork/build --all` writes
role files into `.codex/` and `.gemini/`, so those directories exist here even
though nothing in this project runs Codex or Gemini CLI. The installer detects
a runtime by looking for its directory, and the generator had put three of them
there.

**What was not done.** The detection was not made cleverer. Refusing and asking
is the correct answer to a genuinely ambiguous project, and a guess that is
usually right is exactly the kind of thing this kit is supposed to avoid. The
user types `--runtime claude-code` once.

**What it says about the kit.** A generated artefact was mistaken for evidence
of intent. That will happen to forkers too, on the same command, and the
installer's own message tells them what to do about it.

## 7 — The scans said clean and a reader still got in

The two scanners passed. Every file, both gates, green. A fresh reader was then
asked to work out what the private projects were, and got a long way.

Not by finding copied text. **By reading the roles.**

The roles had been written deep, on instruction, and depth had been supplied
from real experience. Every one of those passages was a fact about a private
system, restated in new words.

**Neither scanner can see a paraphrase.** One matches words. One matches eight
words in a row. A fact retold in fresh words passes both, cleanly, every time.

**The finding is not about the scanners.** They did exactly what they are. The
finding is that a clean scan had been treated as proof of something it cannot
prove, and nobody noticed until somebody attacked the repository on purpose.

**What fixed it.** Every claim of domain knowledge in the roles was replaced
with public knowledge carrying a public source. Not to make the roles weaker —
most survived — but so that a reader learns nothing about the author from them.
The same sentence, traceable to a public page, discloses nothing, because it
would be there for anybody.

Four examples that were plainly product facts became invented ones.

The reader was then run again and could not say what the projects were.

**What this cost.** A day, and the roles are better for it: naming the public
source turned up several things the roles had wrong or missing.

**The rule that comes out of it.** A scan proves the absence of what it looks
for. It proves nothing about what it cannot see. Say which is which.

## 8 — The kit's own tool described the thing it was protecting

The privacy scanners were going to ship, so forkers could run the same gates.

One of them listed which file types to read and which lock files to skip. That
list had been written to fit the private repositories, so it described them:
languages, package manager, project shape. The blind reader named it as the
single strongest leak in the repository.

**This is the same defect as writing the repository names into a file**, which an earlier
gate caught. Same mistake, different shape, written by the same person who had
recorded the first one in this log.

**What fixed it.** The scanners were moved out of the repository entirely, on
the founder's instruction. They are build-time tools; a forker can write their
own word lists and needs nothing from this one.

**The general form, which is the part worth keeping.** A tool that inspects
private material tends to describe it. The configuration of a privacy control
is itself disclosure.

## 9 — What this log still cannot claim

The kit is being used on itself only in part.

The gate runs constantly. The boundary refuses things. But no brief has been
written from the brief template, no report from the report template, and no
decision recorded from the decision template.

**So the dogfooding is real for the enforced rules and absent for the advisory
ones**, which is precisely the split you would expect. The enforced ones make
themselves felt, and the advice has to be chosen. That is itself a finding
about the method, and it is not a flattering one.

**Entry 10 is the first exception.** The kit was installed from the real index
into a new empty repository, and the friction that produced is recorded below
rather than fixed quietly.

## 10 — The fallback did not exist yet at the moment it was needed

**When.** The evening 0.2.0 was published, on the first fork: a new empty
repository, by the author, installing from the real index like a stranger.

**What happened.**

```
$ python3 -m pip install --upgrade formwork-kit
  WARNING: The script formwork is installed in
  '/Users/…/Library/Python/3.14/bin' which is not on PATH.
Successfully installed formwork-kit-0.2.0
$ formwork init
zsh: command not found: formwork
```

The install worked. The command was not reachable. This is the ordinary result
of `pip install --user`, and it had been written up in the README that same
afternoon.

**Why the written answer did not help.** The README offered two ways out:
`python3 -m formwork_cli`, and `formwork/fw` from the top of the project. The
second one does not exist yet at that moment, because `formwork/` is what
`formwork init` puts there and `init` is the command that just failed. The
first one was correct, and was inside a collapsed block halfway down the page.

So the reader had one answer that could not work, and one they could not see.
The author fixed it by editing `PATH`, which is the thing the page says you do
not have to do.

**What fixed it.** The working answer moved out of the fold and into the
install steps, and onto `first-run.md`, which is the page people are sent to.
The ordering matters more than the words: a failure that happens at step two
needs its answer at step two.

**The general form.** A fallback is only a fallback if it exists at the moment
the thing it replaces fails. Two of ours were written together and only one of
them was true that early. Nothing catches this except somebody standing at the
exact point of failure with none of the context.

**What it cost.** Five minutes, and it is the most useful five minutes in this
log, because it is the first time anybody has installed this kit the way a
stranger would.

## 11 — The director held a project that was not this one

**When.** The same evening as entry 10, an hour later, on a different project
in a different repository.

**What happened.** The kit was installed on a new project, `formwork setup` was
answered for the first time by somebody other than a test, and the director was
asked for the first piece of work.

It behaved the way the page says, which is the finding. It read the standing
brief before replying. It noticed the file was still the template below the
first heading and **said so instead of carrying on**. It took the number from
the check rather than counting. It wrote one numbered brief to `docs/briefs/`.
It argued for a recommendation about how the work should be done, said plainly
that the recommendation was not a decision and that no record existed, and
**stopped on one question** rather than taking the small version of the choice
itself.

**What this establishes, narrowly.** The upper layer works for one turn on a
project that is not the kit. `limits.md` said "never held a real project", and
that sentence is now false and has been replaced with what is actually true.

**What it does not establish.** It was one turn, run by the person who wrote
the method, who knew what the role was supposed to do. Nothing is known about
the second week, about somebody else reading those briefs, or about whether any
of this survives a person who did not design it. A split brief has still never
been run.

**The friction, which is the part worth writing down.** Two things, neither of
them the method:

The commits carried a work email, because a global git identity applies to
every repository on the machine. Nothing in this kit has an opinion about that,
and it was caught by looking rather than by any check.

The repository had no remote that existed. Again nothing to do with the kit,
and again the fix was a person looking.

**The general form.** The first real use of a method finds almost nothing wrong
with the method, and two things wrong with the ground it is standing on. That
is normal and it is worth expecting, because the temptation is to read a quiet
first run as proof the method is good, when it mostly proves the setup was
wrong in ways the method never claimed to cover.

## 12 — The director offered to build, four times, and the human caught it

**When.** The day after entry 11, on the same other project, in the same
conversation that had gone well.

**What happened.** The director wrote the brief, wrote three decision records,
kept the standing brief true, and then ended almost every turn with a version of
"say go and I will start building".

Nothing stopped it. The conversation was running inside the repository, so the
tools were right there. The human noticed on the fourth time and asked whether
he had understood the role correctly.

He had. The role's own page lists this under what goes wrong: *it saw the
answer, and typing it was quicker than briefing it*. The page had named the
failure and the failure happened anyway, in the first week, to the person who
wrote the page.

**Why it is not a surprise.** `threads.md` predicted the mechanism exactly: give
the planning layer access to the files and the separation stops being a fact and
becomes a rule in a role file. The guards cannot tell a director from a worker.
In a chat window it could not have built anything if it tried. In the repository
only the words held the line, and the words lost.

**What fixed it.** The role now carries the sentence it should say instead:

> The brief is ready. Open a working session and give it brief 0007.

**A rule that forbids something should supply what to say in its place.** At the
moment of drift the useful next sentence is "I will build it", and if nothing
else is written down, that is what gets reached for. The prohibition was there
and it was not enough, because a prohibition is not a thing you can say.

**What it cost.** Nothing, because the human was reading. That is the part worth
sitting with: the only thing that caught it was a person paying attention, and
the kit's own claim is that people stop paying attention. Nothing here
established that the fix works. It has been written, not tried.
