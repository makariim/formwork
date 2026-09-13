# Threads

How work starts, who decides what happens next, and when to open a new
conversation.

---

## Two layers

```
   PLANNING          decides what happens next, writes the brief,
                     reads the report that comes back
      |  brief
      v
   WORKING           does that one piece of work in the repository,
      |  report      runs the check, stops
      ^-----------------'
```

**Planning** keeps the whole picture: what we are building, what is decided,
what is next. It writes briefs and it judges what comes back.

**It may read the repository.** Reading makes a brief more accurate, so let it
read. What it does not do is the work: no edits, no commands, no version
control. The line is reading against working, not reading against not reading.

**Working** is a session in the repository with the agents and the guards. It
gets one brief, does that one thing, runs `formwork check`, writes a report and
stops.

**You move the work between them.** Nothing moves on its own, and that is the
point: the two stops in the loop are yours.

- It is slow, and the slowness is what makes you read both.
- **The whole report travels, not your summary of it.** The three lines that
  matter are the ones a summary drops first: what was done without being asked,
  what was skipped, and what the brief got wrong.

---

## Where the planning conversation lives

Anywhere. It is a chat window and a file.

Claude.ai, Claude Code in another folder, another tool entirely. It needs two
things and nothing else: your `docs/standing.md`, and the setup block below.
Move it whenever you like. The plan is in the file, not in the window.

---

## Two ways to move it

Both work. Use whichever fits where your director is running.

**The clipboard.** Copy the brief down, copy the report up. Works everywhere,
including a chat window with no access to your files. Nothing to set up.

**The folder.** The brief and the report are files:

```
docs/briefs/0007-slow-login.md      status: open
docs/reports/0007-slow-login.md     written when the work stops
```

Then you say "do brief 0007" instead of pasting, and later "0007 is done".

**The files exist either way.** Even when you paste, the working session saves
the brief it was given and the report it wrote. So you always end up with the
record, and you choose only whether the director reads it directly or you carry
it.

**What the folder buys you:** `formwork check` can see a brief marked done that
left no report. Without the files, a piece of work that quietly went nowhere
leaves no trace outside your memory.

**What it costs:** for the director to read the folder, it needs access to your
files. In a chat window it has none, and cannot touch your code even if it
decided to. Give it access and that safety stops being a fact and becomes a
rule in its role file. The guards cannot tell a director from a worker.

Neither is more correct. Paste when the director is in a chat window, read the
folder when it is not.

---

## Why not one conversation

You can run everything in one. It works for a while, and then it does not.

A conversation that does the work fills up with the work. Fifty file reads and
a long error later, the plan is still in there somewhere, underneath. The
planning conversation stays small because it reads what a brief needs and
stops, rather than reading its way through a problem.

---

## Where this used to break

The planning layer had no file. It lived in one chat window. Close the window
and the state was gone: what we were building, what was already decided, what
we had tried and dropped. You then told the whole story again to a new window,
from memory, and memory is where the drift comes from.

**The fix is the standing brief.** `docs/standing.md`. One short file that says
what we are building, where we are now, what is decided, what is open, what is
next, and what we tried and stopped.

The upper layer now has a file, so it survives the window closing. It is also
the part a program can watch: `formwork check` goes red when a decision record
is dated later than the standing brief.

Start yours from [`templates/standing.md`](templates/standing.md).

---

## The director

The upper layer is a role like any other:
[`roles/method/director.md`](roles/method/director.md).

It owns what happens next. It holds the whole picture, sizes and writes the
brief, judges the report that comes back, and keeps `docs/standing.md` true.
It does not build anything, and **it never writes down a decision you did not
make.**

**Inside your coding tool**, ask for it by name, the same as any other role.

**Anywhere else**, paste the file. Open
`formwork/roles/method/director.md`, paste the whole thing into a new
conversation, and paste your `docs/standing.md` after it. That is the setup.
There is nothing else to keep in step, because the role file is the only copy
of these rules.

**There is one director per project, and one at a time.** A new window is not a
second one. It is the same one, rebuilt from the standing brief.

---

## How work starts

1. **Open the director.** By name inside your coding tool, or by pasting
   [`roles/method/director.md`](roles/method/director.md) anywhere else. Give it
   `docs/standing.md`.
2. **Decide one piece of work.** Its size comes from
   [`loop.md`](loop.md). When the answer is genuinely unclear and the choice is
   expensive, run a [round](round.md) instead.
3. **The brief is written and saved** as `docs/briefs/0007-short-name.md`, with
   `status: open`. You take the number, with
   `formwork/check/checks/work-paired --next .`. Never by counting the folder,
   because gaps are allowed.
4. **The working session gets it.** Pasted, or "do brief 0007". If it is too
   big for one session, give it to the `lead` role, which splits it, hands the
   pieces out, and gives back one report.
5. **It works, checks, reports, stops.** It does not start the next thing.
   The report is saved as `docs/reports/0007-short-name.md` and the brief
   becomes `status: done`.
6. **The report goes back up, whole.** The director accepts it, or sends it
   back with a reason.
7. **`docs/standing.md` is updated** if anything moved. Then go again.

Anything that turns out to be a real decision gets its own record in
`docs/decisions/`, and **only you write those.**

---

## The same thing, as it actually looks

Two windows. You are the only connection between them.

**Window one, the director.** You paste the role file and your standing brief,
then say what you want:

> The login page takes four seconds. I want it fixed.

It reads the standing brief, says back where it thinks you are, and writes a
brief sized to the work. Not six headings for a one line job.

**Window two, the working session**, in the repository:

> Do brief 0007. Nothing else. Run `formwork check`, then report and stop.

It works. The gate runs. It writes `docs/reports/0007-slow-login.md`, sets the
brief to `status: done`, and stops.

**Back to window one.** You paste the whole report, or say "0007 is done" if
the director can read the folder itself.

> Accepted. Nothing unasked, nothing skipped. Next is the printing bug.
> I have updated the standing brief.

That is one turn of the loop. Two sentences from you, two files on disk, and
nothing started without you saying so.

---

## When to start a new thread

Start a new working session for each piece of work. They are cheap, and a fresh
one has no leftover assumptions from the last one.

Start a new planning conversation when:

- it has got long and slow
- you notice it repeating something already settled
- the subject has changed enough that the old context is noise

**Before you close a planning conversation, do one thing:** update
`docs/standing.md`. That is the handover. If you skip it, the next conversation
starts from your memory again, which is the failure this was built to stop.

A good last instruction to a planning conversation:

> Update the standing brief. Where we are now, what is decided, what is open,
> what is next. Short. Do not write anything I have not agreed to.

---

## More than one person

Everybody reads the same standing brief, because it is a file in the
repository.

**One person holds the planning layer at a time**, and that person is the one
who edits `docs/standing.md`. Two people editing it in two chat windows is the
same drift in a new place.

Everyone can run working sessions at the same time. Those do not need to know
about each other, as long as their briefs do not touch the same files.

**This has not been run by a team.** It is the shape the mechanism allows, not
something anybody has proved. NOT ESTABLISHED.
