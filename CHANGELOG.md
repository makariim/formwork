# Changelog

What changed in each release, newest first. Before 1.0.0 the record is the
version commit's message in git: `git show 02bd5f0` for 0.2.0 and
`git show 6a923da` for 0.2.1.

---

## Unreleased

- Optional templates and gates for big work. Six one page templates in
  `formwork/templates/`: spec, research lane, design round, build, review
  round, release step (the general pattern only). A phase is a label on a run
  of ordinary briefs, using `stream:`; no fixed order. New check `gates`: a
  brief may carry one `starts:` line, `now`, `after <stream>` or `decision
  NNNN`, and an open brief whose gate is not met, or whose gate is in prose,
  is refused. The two default gates for a build (no build before the spec is
  accepted; unproven items listed and seen before the next phase) are offered
  in the spec and build templates. `formwork/route.md` offers the matching
  template by kind and size, never as a sequence.
- Specialists, cheapest first. The `lead` spawns an existing role, then a
  relabel (an existing role with a title line and optionally a skill, its
  owns, sections and tools still from its file), and only then a new project
  role: drafted by the `director` in the brief, accepted by the person,
  written to `formwork/roles/project/<name>.md` by a working session. Never a pasted
  persona. New check `roles-named`: a round file must be `<role>.md` or
  `<role>-<label>.md` for a real role, and a role in an open brief's team
  table must exist. `TEMPLATE.md` says a role touching plans or order names
  the director and lead under "Does not own".
- Routing one plain prompt. `formwork/route.md` is the routing table: six
  kinds of request, each with its size test, template, team and stops.
  Default size is a task. The `director` is the only router above a task and
  says the plan back in one or two lines before acting. Corrections go in
  `docs/routing.md`, in the person's words (`formwork/templates/routing.md`).
  Routing accuracy, measured: 44 and 45 of 49 in two runs with Haiku.
- `formwork/evals/routing/`: 49 plain prompts with the expected kind, size
  and first step, and `run`, which sends each to a fresh safe mode
  `claude -p` session holding only the routing table and the director, and
  prints the score. `--dry-run` checks the set and spends nothing.
- `formwork/route.md`: a new product's first brief is a one page spec, and a
  round comes later; size the work, not the words.
- `formwork setup` asks a twelfth question and offers the two routing lines
  (`formwork/templates/project-instructions.md`) as `CLAUDE.md`, `AGENTS.md`
  or `GEMINI.md` by runtime, only when the file does not exist. When it does,
  setup shows the lines to paste and writes nothing there.
- `formwork/templates/personal-defaults.md`: a page to copy into your own
  global instruction file, with one line pointing at formwork's routing.
- `predictions-first` reads rounds outside `docs/rounds/`: any folder under
  `docs/` with a predictions file (`predictions.md`, `*-predictions.md`) or a
  challenge file (`challenge.md`, `challenger.md`). A challenge file with no
  predictions on record fails. Predictions under a heading inside the
  challenge file pass with a warning.
- `standing-current` compares the standing brief with dated briefs and
  reports (`date:`, `updated:`, `accepted:`), and fails a "What is next" that
  names a brief marked done or dropped.
- `open_briefs_per = "stream"` under `[strength]` makes `open_briefs` the
  limit for each stream, read from a brief's `stream:` or `**Stream:**` line.
- `formwork/COSTS.md` counts thirteen checks, not twelve.
- New check `kit-leak-scan` reads kit files only (`formwork/`,
  `formwork_cli/`, `FORMWORK.md`, generated roles) and fails on a real looking
  home path, a private network address, a local hostname, an email address or
  an API key shaped string. Placeholders such as `/Users/<you>/` and
  `example.com` pass. It cannot see a machine named in plain words.
- `protected-files` checks Codex `apply_patch` headers, including patches fed
  through shell arguments, wrappers, pipes, and heredocs, before a guarded
  file can be changed. It reads Codex's whitespace forms and refuses an
  `apply_patch` call with no readable patch text.
- `guard-wired` checks every runtime named in `[bindings].runtimes` and any
  wiring file that names a formwork guard. Codex requires the two tool guards,
  with a matcher whose regex reaches a Codex patch tool name; `Edit` and
  `Write` are accepted as well as `apply_patch`.

## 1.0.0

**This one can turn a green gate red.** Two checks are stricter and there is a
new core rule. By [`RELEASING.md`](RELEASING.md) that is a breaking change, so
the first number moves.

### Can turn your gate red

- `work-paired` allows one open brief at a time. Raise it with `open_briefs`
  under `[strength]`, and 0 means no limit.
- `work-paired` refuses a brief marked `done` until its report carries
  `accepted:` with a date and `in my words:` with a sentence, five words by
  default. Change it with `read_back_words` under `[strength]`: 1 lets a
  single word through, and 0 lets the line be empty.
- New check, `report-shape`: a report opens with `## For you`, a part for the
  human, under 1,000 words and with no commands, before `## For the director`.
  Reports written before the rule pass if they carry a dated `## For you`
  bridge above their old headings.

### Added

- `formwork sync`. After upgrading the command, run it inside a project and
  the project's `formwork/` and `FORMWORK.md` come up to the installed
  release. Files the project owns stay: its own roles in the project pack, and
  anything listed as `local` under `[bindings]` in `.formwork.toml`. It writes
  the release into the project's SOURCE.txt and stops before recording the
  fingerprints, because that is yours to do. `formwork/fw sync <project>` does
  the same from a clean clone of the kit, pinned to the commit.
- `formwork/skills/`, and the first skill in it, `humanizer` 3.1.0, pinned to
  one upstream commit with formwork's change to its rule on bold kept in a
  separate file. `formwork roles` places it in `.claude/skills/` on Claude
  Code, and `generated-current` goes red if that copy is edited by hand.
- `formwork/style.md`: text the agent writes as you, such as an email or a
  comment, goes through `humanizer` first. A section on reports for two
  readers.
- A fourteenth core rule: the human is not the courier.
- A role's `description`, `model`, `skills` and `color` reach the generated
  Claude Code agent instead of being dropped. Codex and Gemini CLI get the
  description and a note.

### Counts

Three guards, thirteen checks, twenty eight roles, forty eight rules, one
skill, 494 tests.
