# Parallel worker brief

Optional. Added to a brief when the working session runs beside others on the
same tree. The rules are in
[`../operations/parallel.md`](../operations/parallel.md).

Pasted under the brief's scope, filled in by the director or the `lead`. The
cadence and thresholds are the project's; the defaults are in `parallel.md`.

---

```markdown
## Running beside others

- **Session name:** <the name the director addresses>
- **Model, and why:** <lighter for well defined work; the strongest for design calls>
- **Yours alone:** scratch folder <path>, build folder <path>, device or simulator <id>
- **Never wait on:** another session's runs, a global process check, "no test run active". Wait only on your own jobs.
- **Status:** one line when asked, every <minutes>: doing, last file or log that moved, waiting on.
- **Progress shows in:** <files or logs whose change proves work is moving>
- **Stuck means:** none of those moved in <minutes>. Say what you are waiting on.
- **When a long job ends:** it notifies by <its completion signal>, never by polling.
- **Before leaving files in the shared tree:** <the build or test command that must pass>. No half written file, ever.
- **Shared contracts:** owned by <owner>. A gap goes to the owner; never patch around it.
- **Usage share:** <heavy or light, within the project's limit on heavy sessions>
- **Disk:** check free space before a large install or long run.
- **You do not:** grade your own work, write your own gate, or tick the release checklist.
```
