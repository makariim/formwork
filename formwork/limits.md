# What this kit cannot do

**Written after an audit walked through the guards.** Everything below was
confirmed by running it, not guessed.

Most pages in a repository tell you what something does. This one tells you
where it stops, because a guard you trust further than it deserves is worse
than no guard at all.

---

## The short version

**The guards stop the ordinary path, not a determined one.**

They are pattern matching over a command line. An agent that wants to get past
them can. The value is that an agent which is not trying to get past them —
which is nearly always — is stopped from doing the everyday thing that should
have been your decision.

**If you need containment, this is not it.** Use a sandbox, a container, or a
machine you do not mind losing.

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
- **`xargs`.** `echo <path> | xargs rm` — the path is an argument to `echo`.

**Why these stay open.** Each fix is a longer pattern, and a longer pattern has
more false positives. A guard that refuses ordinary work gets switched off
permanently, and then nothing is guarded. That trade is the reason this page
exists instead of a longer regular expression.

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

## The honest summary

This kit will stop an agent doing the wrong thing by habit. **It will not stop
one doing the wrong thing on purpose**, and nothing built out of pattern
matching would.

If that is not enough for your situation, the answer is not a better pattern.
It is a sandbox.
