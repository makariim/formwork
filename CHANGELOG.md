# Changelog

What changed in each release, newest first. Before 1.0.0 the record is the
version commit's message in git: `git show 02bd5f0` for 0.2.0 and
`git show 6a923da` for 0.2.1.

---

## Unreleased

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
