# Running many sessions safely

Part of the operations pack ([`README.md`](README.md)). For a director or a
`lead` with two or more working sessions on one tree at once. How work is
handed down and reported back is [`../threads.md`](../threads.md); this page is
what keeps parallel sessions from stalling each other or breaking the shared
build.

Brief each worker with
[`../templates/parallel-worker-brief.md`](../templates/parallel-worker-brief.md).

**Before the first worker starts:** one open brief per worker means more than
one open brief, and `work-paired` allows one by default. The person raises
`open_briefs` under `[strength]` in `.formwork.toml`, or sets
`open_briefs_per = "stream"` with one stream per lane. The agent never edits
that file; it is protected.

---

## The rules

**Never wait on another session's runs.** A worker never waits for "no test
run active", a global process count, or another session's job to finish. With
several sessions, one of them is almost always running something, so that
wait never ends. Wait only on your own jobs, by their own completion signal.

**One of everything per worker.** Each worker has its own scratch folder, its
own build folder, and its own simulator, emulator or test device. Two workers
sharing one get each other's state and each other's failures.

**Never break the shared build.** No half written file is left in the shared
tree. Build the whole package before leaving files in place. A shared name
(a type, a module, a fixture) is checked for a clash before it is added. A
worker that breaks the build fixes it at once, before anything else.

**Status every 45 minutes when parallel.** Each worker, asked by the director,
answers in one line: what it is doing, what file or log last moved, what it
is waiting on.

**A stuck worker is judged by its own outputs, not by busy status.** Live
processes and a "working" label prove nothing. Look at its own files and logs.
If none of them has moved in 30 minutes, ask it what it is waiting on. In the
source round, a fix session sat waiting for a condition another session kept
true, and the watchdog counted it busy because build processes were live.

**Wake timers and a watchdog.** A long job runs in the background so its end
notifies the director; a finished job once sat unseen for 1 hour 45 minutes.
Where the runtime offers a timer, the director sets one for the next status
check instead of relying on memory. The watchdog looks at outputs moving,
never at processes alive.

**Pace the shared usage budget.**

- At most 2 to 3 heavy sessions at once. In the source round, running more
  used a five hour usage window in an hour and a half.
- Lighter models for workers doing well defined work; the strongest model for
  the director and for design calls.
- A second vendor's coding agent for mechanical work: renames, generated
  code, bulk edits.
- At most 3 sessions writing to shared files at once.

**Disk hygiene.** Simulators, emulator runtimes and build caches fill a disk
quietly. Check free space before a large install or a long run, and clean only
what a worker made, or with the human's yes.

**The builder never grades itself.** The session that built a part does not
write its gate or run its final check. A separate session does (see
"an independent re-check" in [`README.md`](README.md)).

---

## What it cannot do

Nothing here is enforced. No check sees a worker waiting, a shared folder, or
a stalled log. The numbers (45 minutes, 30 minutes, 2 to 3 heavy sessions) are
one round's defaults on one machine and one usage plan. NOT ESTABLISHED:
whether they hold for other plans or larger teams. Whether a given runtime
offers wake timers is NOT ESTABLISHED here; check its own documentation.
