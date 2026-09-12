# When something goes wrong

Find the message you saw. Every entry says what happened, why, and what to do.

> **`command not found: formwork`?**
>
> Everything on this page also works with `formwork/fw` from the top of your
> project, and that needs nothing installed:
>
> ```
> formwork/fw check
> formwork/fw record
> ```
>
> **If you did install it and still get this**, pip put the command somewhere
> your shell does not look. It says so in a warning when it installs. Add that
> folder to your PATH, or use `pipx install formwork-kit` instead, which
> handles this for you.



If your problem is not here, it belongs here. Open an issue with the exact
message and it will be added.

---

## The gate is red

### `kit-integrity: N protected file(s) differ from the record`

**What happened.** A file that enforces something has changed since the last
time you recorded it.

**Why.** Either you changed it on purpose, or something else did.

**What to do.** Look at what changed first:

```
git diff <the file it named>
```

If you meant it, record the new state:

```
formwork record
```

**Why you have to run that yourself.** Recording says "every one of these files
is as I intend it". If an agent could do that, it could change a guard and then
tell the kit the change was fine. The guard refuses that command.

### `no fingerprints recorded at ~/.formwork/fingerprints.txt`

**What happened.** There is no record to compare against.

**Why.** This is a fresh machine, or a fresh clone, or you moved
`FORMWORK_STATE_DIR`.

**The record lives outside your project, and there is one per project.** It is
in `~/.formwork/fingerprints/`, named after your project's path. It does not
travel with a clone, which is the point: a record that travels beside the thing
it describes protects nothing.

**What to do.** Run the installer again. It takes the first record for you:

```
formwork install --runtime claude-code
```

### `guard-wired: runtime 'X' is declared, but .../hooks.json does not exist`

**What happened.** Your settings say you use tool X, and the hooks for X are
not wired up.

**Why.** This kit ships a wiring file for Claude Code only. The other three are
documented but nobody has run them.

**What to do.** Open the README in `formwork/adapters/` for the tool you
use. It says exactly what to put in that file. Then the gate goes green.

**Red is correct until then.** Nothing is guarding you yet, and the kit will
not say green about that.

### `doc-links: N link(s) point at nothing`

**What happened.** A markdown link points at a file that is not there.

**What to do.** Fix the link or create the file. The message gives you the file
and the line number.

### `generated-current: N generated file(s) are not current`

**What happened.** One of three things. You edited a role and the generated
copies have not caught up. You edited a generated copy by hand. Or you deleted
a role and left its generated copy behind.

**What to do.**

```
formwork roles
```

**If you edited a generated file by hand**, move your change into the source
file in `formwork/roles/` first. The next regeneration will throw your edit
away.

**If you deleted a role**, `formwork roles` will not clean up after you. Delete
the generated copy too, then run it:

```
rm .claude/agents/<the role>.md
formwork roles
```

### `role-shape: N problem(s) across N role(s)`

**What happened.** A role is missing something, or two roles claim the same
job.

**What to do.** The message names the file and the problem. Every role needs
four frontmatter fields and five sections. Copy `formwork/roles/TEMPLATE.md` if
you are unsure.

### `N check(s) present but not executable`

**What happened.** A check file lost its execute permission.

**What to do.**

```
chmod +x formwork/check/checks/*
```

**Why this stops everything.** A check that cannot run has not passed. Before
this was caught, the gate reported green while quietly skipping it.

---

## A command was refused

### `REFUSED by the version-control boundary`

**What happened.** The agent tried to commit, push, merge or something like it.

**This is working correctly.** You do those, not the agent.

**What to do.** Run the command yourself.

**If it refused something read-only**, that is a bug and worth reporting. The
guard should allow anything that only looks.

**To turn it off for one session:**

```
FORMWORK_GIT_BOUNDARY=off
```

### `REFUSED by self-protection`

**What happened.** Something tried to change a file that enforces a rule.

**What to do.** If you meant it, make the change yourself in your editor, then
record the new state with `kit-integrity --record .`.

**To turn it off for one session:**

```
FORMWORK_PROTECT_FILES=warn
```

### `REFUSED: the aggregate is red, so this turn cannot conclude`

**What happened.** The gate is red and the turn tried to end.

**What to do.** Read what the gate said and fix that.

**It gives up after three.** Once it has refused three times in a session it stands aside
and says so in capitals. That is deliberate, so a stuck turn is not stuck for
ever.

---

## The installer

### `Cannot tell which runtime this project uses`

**What happened.** There is no `.claude`, `.codex`, `.cursor` or `.gemini`
folder, so it cannot guess.

**What to do.** Tell it:

```
formwork install --runtime claude-code
```

### `more than one runtime is set up here`

**What happened.** You have folders for several tools.

**What to do.** Same as above. Say which one.

### `NOT FINISHED` after installing

**What happened.** It did what it could and stopped.

**What to do.** Read the list it printed. It names the file you need to write
and the page that tells you what goes in it.

---

## Nothing is being blocked at all

**Check the hooks are wired.**

```
formwork check
```

If `guard-wired` passes, the hooks are in place.

**Check the strength setting.** Look in `.formwork.toml`. If it says `warn` or
`off`, that is why.

**Check your shell.** An environment variable overrides the file:

```
echo $FORMWORK_GIT_BOUNDARY $FORMWORK_PROTECT_FILES $FORMWORK_GATE
```

**Check your tool.** Only Claude Code has been watched refusing a real command.
On the other three, wiring is documented and untried.

---

## Something is being blocked that should not be

**This matters as much as the opposite.** A guard that is wrong about ordinary
work is a guard people switch off, and then nothing is guarded.

**Report it.** The command you ran is all anybody needs.

**Meanwhile, get on with your work:**

```
FORMWORK_GIT_BOUNDARY=off
FORMWORK_PROTECT_FILES=off
```

---

## Nothing here matches

Two commands worth running before you ask:

```
formwork check    run every check
formwork demo     watch each check refuse a broken input
```

If both look right and the problem is still there, it is probably a real bug.
Open an issue with the exact message and what you ran.
