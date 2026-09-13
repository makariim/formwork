# When something goes wrong

Find the message you saw. Every entry says what happened, why, and what to do.

> [!TIP]
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
> **If you did install it and still get this**, pip put the command in a folder
> your shell does not search. You do not need to fix your PATH. This is the
> same command, run through Python:
>
> ```
> python3 -m formwork_cli check
> ```
>
> To avoid it next time, install with `pipx install formwork-kit`, or into a
> virtual environment.



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

**Why you and not the agent.** Recording says every one of these files is as
you intend it. An agent that could do that could change a guard and then tell
the kit it was fine.

### `no fingerprints recorded at ~/.formwork/fingerprints.txt`

**What happened.** There is no record to compare against.

**Why.** A fresh machine, a fresh clone, or you moved `FORMWORK_STATE_DIR`.

The record lives outside your project, one file per project, in
`~/.formwork/fingerprints/`. It does not travel with a clone, which is the
point: a record kept beside the thing it describes protects nothing.

**What to do.** Run the installer again. It takes the first record for you:

```
formwork install
```

### `guard-wired: runtime 'X' is declared, but .../hooks.json does not exist`

**What happened.** Your settings say you use tool X, and the hooks for X are
not wired up.

**Why.** The kit ships a wiring file for Claude Code only.

**What to do.** Open your agent's page in `formwork/adapters/`. It says what to
put in that file. Red is correct until then: nothing is guarding you yet.

### `doc-links: N link(s) point at nothing`

**What happened.** A markdown link points at a file that is not there.

**What to do.** Fix the link or create the file. The message gives you the file
and the line number.

### `generated-current: N generated file(s) are not current`

**What happened.** You edited a role, or edited a generated copy by hand, or
deleted a role and left its copy behind.

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

**It gives up after three.** Then it stands aside and says so in capitals, so
a stuck turn is not stuck for ever.

---

## The installer

### `Cannot tell which runtime this project uses`

**What happened.** There is no `.claude`, `.codex`, `.cursor` or `.gemini`
folder, so it cannot guess.

**What to do.** Tell it which one, using the name of your agent:

```
formwork install --runtime claude-code
formwork install --runtime codex
formwork install --runtime cursor
formwork install --runtime gemini-cli
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
work gets switched off, and then nothing is guarded. Report it: the command you
ran is all anybody needs.

Meanwhile:

```
FORMWORK_GIT_BOUNDARY=off
FORMWORK_PROTECT_FILES=off
```

---

## Nothing here matches

Run `formwork check` and `formwork demo`. If both look right and the problem
is still there, it is probably a real bug. Open an issue with the exact message
and what you ran.
