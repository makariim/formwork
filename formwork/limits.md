# What this kit cannot do

**Everything below was confirmed by running it, not guessed.** A guard you
trust further than it deserves is worse than no guard at all.

---

## The short version

**The guards stop the ordinary path, not a determined one.** They are pattern
matching over a command line. An agent that wants past them can get past them.
The value is that an agent not trying to, which is nearly always, is stopped
from doing the everyday thing that should have been your decision.

> [!WARNING]
> **If you need containment, this is not it.** Use a sandbox.

---

## Ways past the version-control boundary

These were all closed during the audit, and are now tested:

`bash -c "git commit"` · `eval` · backticks · `$(...)` · `nice -n 5 git push` ·
`timeout 60 git push` · `env -u FOO git push` · `git config core.hooksPath` ·
`git checkout <file>`

**These are still open, and are not closable by pattern matching:**

- **Building the command out of pieces.** `g="git"; $g push`
- **Encoding it.** Base64 into a shell, a string reversed, a character at a time.
- **A script.** Writing `deploy.sh` and running it. The guard sees `./deploy.sh`.
- **A different tool.** A git library in Python, a language binding, an editor's
  built-in version control.
- **`xargs`.** `echo <path> | xargs rm`. The path is an argument to `echo`.

**Why these stay open.** Each fix is a longer pattern, and a longer pattern
refuses more ordinary work. A guard that does that gets switched off, and then
nothing is guarded.

---

## Ways past self-protection

Closed during the audit: writing through a pipe, `chmod` in every spelling,
deleting or moving the folder that holds the guards, re-recording the integrity
fingerprints, hiding a path inside a here-document.

**Still open:** everything in the list above, for the same reason. Plus:

- **Symbolic and hard links.** A link to a protected file is a different path,
  and the guard compares paths.
- **A long-running program.** Approved once, then doing whatever it likes.

---

## What the checks cannot tell you

**`predictions-first`** fails a round that has reports and no predictions file.
Beyond that it only warns: modification times are weak evidence and it says so.
**It cannot tell you the predictions were any good.**

**The fixture shuffle hides the case name and nothing else.** Before a check
runs, its test folder is copied somewhere with a meaningless name, so a check
cannot pass by spotting the word "must-fail". **Names inside the folder are
left alone**, because several checks read them for real reasons: a decision
record is identified by its numbered filename, a role by its `.md` ending.

So a check that looks for one particular file inside a fixture can still pass
while examining nothing. An audit wrote one and it worked. Scrambling the
contents was tried and broke the checks that read names legitimately.

**What this means in practice:** the pair of fixtures proves a check can tell
two inputs apart. It does not prove the check looked at what is in them.

**`rule-labels`** checks that a rule naming a check names one that exists. It
matches on the name only.

**`doc-links`** resolves links. It does not know whether the page it reached
says what the link promised.

**`kit-integrity`** notices that a file changed. **It has no opinion about
whether the change was good**, and re-recording is a human decision for exactly
that reason.

**`generated-current`** compares generated files with what the source produces.
It now also reports generated files with no source at all.

---

## The gate gives up

The turn-end gate refuses a red gate **three times in a session**, then stands
aside with a loud message.

**That is deliberate and it is a real hole.** Without it, a genuinely stuck turn
is trapped for ever. With it, an agent that fails three times can proceed.

Three refusals in one session is not a subtle signal. It is the point at which
you should be reading, not the point at which the kit should keep refusing.

`gate_budget` in `.formwork.toml` changes the number.

---

## What the privacy scanners cannot see

Both ship outside the repository, and this matters to anyone forking the method
rather than the code.

**The word scan finds words.** The overlap scan finds eight words in a row.

**Neither can see a paraphrase.** A fact from a private project, retold in fresh
words, passes both cleanly. That happened while this kit was being built: both
scans were green and a fresh reader still reconstructed a great deal. It is
written up as entry 7 of `docs/dogfood.md`, in the source repository.

**A clean scan proves the absence of what it looked for. It proves nothing
about what it cannot see.**

---

## Three of the four runtimes are untested

Only Claude Code has been watched refusing a real command.

Codex, Cursor and Gemini CLI all document a way to block, and their adapters say
`untested` at the top. **Their hook payload shapes are assumed**, not verified.
The guards now refuse rather than allow when they cannot read a payload, so a
wrong assumption shows up as a refusal rather than as silent permission.

---

## What has been run, and what has not

| | |
|---|---|
| **`formwork setup`** | run on a new project. Its questions have been answered once, by the author |
| **The director role** | **run twice**, on a different project. It held the plan, wrote the briefs and the decision records, and kept the standing brief true. It also offered to do the building four times, which its own page names as the way this role fails, and the human caught it rather than the kit |
| **The folder route** | used in that same session. The number came from the check, the brief was saved under it |
| **A split brief** | `lead` cutting one brief into pieces and joining the reports back. **Never done once** |

**One run by the person who wrote the method is not a trial.** What it
establishes is narrow: the shape holds together for one turn, on a project that
is not this one. It says nothing about the second week, about somebody else's
judgement of the briefs, or about whether any of it survives a person who did
not design it.

**A split brief remains NOT ESTABLISHED**, and so does everything about more
than one person.

**And one thing the second run established that nobody wanted:** with the
planning layer inside the repository, the separation between planning and
building is a sentence in a file and nothing else. It failed within a day. The
role now carries the words to say instead, and whether that is enough is itself
NOT ESTABLISHED. See entry 12 of `docs/dogfood.md`, in the source repository.

---

## A guard that refuses ordinary writing

The version-control boundary reads a command line. When text is being fed into
a program that could run it, the guard cannot tell writing *about* a command
from running one.

So writing documentation that contains a version-control command, through a
shell, is refused. The self-protection guard does the same: text containing the
words that would re-record the fingerprints is refused, whether or not anything
would run.

Both happened while writing this kit's own pages.

**There is no fix inside the pattern.** The guard would have to understand
where a string ends and a command begins, which is the same problem as being
safe against somebody hiding one inside the other. The way through is to write
the file with an editor rather than a shell. That is a different tool, not a
way around the guard.

---

## The guard does not cover every tool the same way

Self-protection reads a command line. An agent's file-editing tool is not a
command line, so the guard sees it only where the runtime routes it through
one.

During this kit's own building, the same change to a check was refused when
made with the editing tool and allowed when made by a short script. Both are
the same act. The pattern caught one shape of it.

**What holds the line is not the guard here, it is `kit-integrity`:** any
change to a file that enforces something turns the gate red until a person
records it. The guard makes the ordinary route awkward. The record is what
makes the change visible.

---

## What five audits found, after everything above was written

Five agents attacked version two: the three new checks, `formwork setup`,
`formwork install`, the two new roles, and every page. **71 findings.**

The pattern worth repeating, because it is the one this kit exists to prevent:
**six of the fifteen check defects were the check reporting clean having
examined nothing**, and printing a count that made the emptiness look like
coverage. A decision record moved one folder deeper vanished, and the check
said it was ahead of all 0 records. A report file was never opened, so `touch`
satisfied it. A role mentioning "lifestyle.md" satisfied the style check.

All of those are closed and each has a fixture. What the episode establishes
is smaller and more useful than any of the fixes: **a check written by whoever
wrote the thing it checks tends to pass for the wrong reason**, and only
somebody trying to break it finds out.

---

## The honest summary

This kit will stop an agent doing the wrong thing by habit. **It will not stop
one doing the wrong thing on purpose**, and nothing built out of pattern
matching would.

If that is not enough for your situation, the answer is not a better pattern.
It is a sandbox.
