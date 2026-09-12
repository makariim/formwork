# Survey: What already exists for running a project with coding agents

**Phase:** K2 (Survey). **Date:** 2026-09-11.
**Status of this document:** descriptive only. It makes no comparison to any
method, recommends nothing, and decides nothing.

---

## How this survey was made

Every entry below was produced by cloning the repository and reading files in
it. Landing pages and READMEs were not accepted as evidence. Each entry names
at least one file or command actually opened.

Working corpus: 32 repositories shallow-cloned to a scratchpad.

```
git clone --depth 1 --single-branch https://github.com/<owner>/<repo>.git
ls -d */ | wc -l          # -> 32
```

**What would make that number wrong:** it counts clone directories, not
distinct projects. `agents.md` (the website) and `agnix` (a linter for it) are
separate rows but one subject area. Three repositories were cloned in a first
parallel attempt that stalled and were re-cloned sequentially; if a stalled
directory had been left in place the count would have been inflated. It was
checked with `git -C <dir> ls-files | wc -l` returning non-zero for all 32.

HEAD commit dates for every repository, used throughout for staleness claims:

```
for d in */; do d=${d%/}; printf "%-34s %s\n" "$d" \
  "$(git -C $d log -1 --format='%ad' --date=short)"; done
```

**What would make those wrong:** `--depth 1 --single-branch` fetches only the
default branch. A project whose work has moved to a release or `next` branch
looks stale when it is not. This is called out per entry where it matters.

### A note on what "where it stops" means here

Each entry's "where it stops" is a statement about the artifact in the
repository, not a criticism of the project's ambition. Several projects stop
exactly where they say they stop.

---

## Shape 1 — Spec-driven and plan-driven development kits

### 1. GitHub Spec Kit (`github/spec-kit`)

**Evidence opened:** `templates/commands/specify.md`,
`templates/constitution-template.md`, `templates/commands/converge.md`,
`src/specify_cli/integrations/claude/__init__.py`, `scripts/bash/create-new-feature.sh`.
HEAD `c173bf1`, 2026-09-10.

**What it does.** Installs a fixed set of slash commands into a coding agent,
plus markdown templates the commands fill in. The command set is ten files:

```
ls templates/commands/ | wc -l     # -> 10
# analyze, checklist, clarify, constitution, converge,
# implement, plan, specify, tasks, taskstoissues
```

The pipeline is `constitution` → `specify` → `clarify` → `plan` → `tasks` →
`implement`, with `analyze` and `converge` as consistency passes. Artifacts land
under a per-feature directory as `spec.md`, `plan.md`, `tasks.md`; project-level
principles live in `.specify/memory/`. Shell, PowerShell and Python variants of
every helper script are shipped (`scripts/bash/`, `scripts/powershell/`,
`scripts/python/`), selected by `SCRIPT_TYPE_CHOICES` in `_agent_config.py`.

**What it does well.** Breadth of host support is its strongest concrete
property — 41 integration directories:

```
find src/specify_cli/integrations -maxdepth 1 -type d ! -name integrations | wc -l   # -> 41
```
(**Wrong if:** a directory is a shared helper rather than an agent. `base.py`,
`catalog.py`, `manifest.py` are files, not directories, so they do not inflate
it; but `generic` is a fallback pseudo-agent, so 40 named tools + 1 generic is
the fairer reading.)

It is unusually honest in its own code about failure modes it has observed. The
Claude integration carries an empty `FORK_CONTEXT_COMMANDS` dict with a comment
explaining that `analyze` was previously run in a forked subagent, that it
returns a 300–500 line report injected back into the parent conversation, and
that each subsequent fork inherited the growing context "compounding overhead
until the chat freezes (#3185)". The mechanism is kept, the opt-in is withdrawn.
That is a documented retreat from a design, in source, with an issue number.

`converge.md` is a distinct idea: it re-reads `spec.md`/`plan.md`/`tasks.md` as
"the **sole source of intent**", assesses the present state of the code, and
*appends new traceable tasks* for unmet criteria. It explicitly disclaims being a
diff tool: "no git, no branch comparison, no history."

**Where it stops.** At the boundary of its own extension mechanism. Every
command instructs the agent to read `.specify/extensions.yml` for hooks, and
then says: if a hook defines a non-empty `condition`, **do not evaluate it** —
"skip the hook and leave condition evaluation to the HookExecutor
implementation". No HookExecutor runs in the loop; the command emits an
`EXECUTE_COMMAND:` line and relies on the agent to honour it. So conditional
hooks are inert, and mandatory hooks are mandatory only insofar as the model
complies. Separately, the constitution is a template of
`[PRINCIPLE_1_NAME]`/`[PRINCIPLE_1_DESCRIPTION]` placeholders with example
comments; nothing in the repository checks a plan against it. `analyze` asks a
model to look for inconsistency; there is no schema, parser, or exit code.

**What it costs to adopt.** A Python CLI (`specify init`) plus a `.specify/`
directory, a per-feature directory convention, and ten slash commands added to
the agent's namespace. Scripts must run in one of bash/PowerShell/Python. The
ceremony is fixed: the pipeline assumes a feature-sized unit of work and
produces four-plus documents before code.

**Who it appears to be for.** Teams on GitHub-adjacent tooling who want one
recognisable pipeline that survives switching between Copilot, Claude Code,
Cursor and others. The default init integration is hardcoded to `copilot`
(`DEFAULT_INIT_INTEGRATION = "copilot"` in `_agent_config.py`).

---

### 2. OpenSpec (`Fission-AI/OpenSpec`)

**Evidence opened:** `src/core/validation/constants.ts`,
`src/core/parsers/requirement-blocks.ts`,
`openspec/changes/add-validation-findings-report/specs/cli-validate/spec.md`,
`src/commands/validate.ts`, `src/core/command-generation/adapters/`.
HEAD `9d4e597`, 2026-09-09.

**What it does.** Separates the *current* specification from *proposed changes*
to it. A change lives in `openspec/changes/<name>/` with `proposal.md`,
`design.md`, `tasks.md` and delta spec files; the delta files use
`## ADDED Requirements` / `## MODIFIED` / `## REMOVED` headers, with
`### Requirement:` blocks and `#### Scenario:` blocks beneath. Accepted changes
are archived. A TypeScript CLI parses and validates this structure.

**What it does well.** It is the only spec kit in this survey whose specs are
**machine-checkable by a real parser with named error constants**, not by asking
a model to look:

```
grep -rn "must have at least" src/core/validation/constants.ts
# REQUIREMENT_NO_SCENARIOS: 'Requirement must have at least one scenario'
# SPEC_NO_REQUIREMENTS:    'Spec must have at least one requirement'
# CHANGE_NO_DELTAS:        'Change must have at least one delta'
```

The parser is fussy in a way that shows it met real documents:
`requirement-blocks.ts` normalises `#### Foo ####` closing runs and an optional
`Scenario:` prefix so that the scenario name matches "the label the author
reads", and it excludes fenced code blocks from header detection.

It dogfoods visibly. Its own `openspec/` directory holds live and archived
change proposals:

```
ls openspec/changes/archive | wc -l    # -> 83
```
(**Wrong if:** archive entries include non-change scaffolding. Spot-checked
entries such as `2025-08-19-add-zod-validation/` each contain
`proposal.md`/`tasks.md`/`specs/`, so they are real.)

Its shipped spec prose is written in RFC-2119 style with `SHALL`, and its
scenarios are `WHEN`/`THEN`/`AND` — see the `cli-validate` spec above, which
specifies its own `--report findings` flag that way.

**Where it stops.** At well-formedness. The validator can prove a requirement
has a scenario; it cannot prove the requirement is correct, necessary, or
implemented. Nothing in `src/core/validation/` compares a spec to the codebase.
The 31 host adapters under `src/core/command-generation/adapters/` generate
command files per tool; they do not verify that the tool obeyed them.

**What it costs to adopt.** Node/TypeScript CLI, a top-level `openspec/`
directory, and a genuine discipline change: work is expressed as a *delta to a
standing spec*, then archived. Authors must write scenarios in the accepted
header shape or validation fails. It is more ceremony than Spec Kit, not less.

**Who it appears to be for.** Teams that want the specification to be a durable,
queryable asset with history, and are willing to pay parser-strictness for it.

---

### 3. BMAD-METHOD (`bmad-code-org/BMAD-METHOD`)

**Evidence opened:** `skills/bmad-agent-dev/SKILL.md`,
`skills/bmad-agent-dev/customize.toml`, `skills/bmad-spec/assets/spec-template.md`,
`skills/bmad-prfaq/agents/`. HEAD `abe4eb1`, 2026-09-05.

**What it does.** Ships a cast of named personas as agent skills, plus process
skills they invoke. At this HEAD the repository has restructured around skills:

```
ls skills/ | wc -l     # -> 29
```
(**Wrong if:** counted as distinct methods. They are not peers — `bmad-agent-*`
are personas, `bmad-prd`/`bmad-spec`/`bmad-architecture` are artefact producers,
`bmad-party-mode` and `bmad-walkthrough` are session modes.)

`skills/bmad-agent-dev/SKILL.md` is "Amelia — Senior Software Engineer". Its
activation sequence is explicit: resolve the agent block, run prepend steps,
adopt persona, load persistent facts, load config, greet, present a menu.

**What it does well.** Layered customisation with defined merge semantics, which
nothing else here has. `customize.toml` states the rules in the file itself:
"scalars: override wins • arrays (persistent_facts, principles,
activation_steps_*): append • arrays-of-tables with `code`/`id`: replace
matching items, append new ones", resolved base → team → user across
`customize.toml`, `_bmad/custom/{skill}.toml`, `_bmad/custom/{skill}.user.toml`.
It also fences what is *not* customisable: `name` and `title` are marked
"non-configurable skill frontmatter, create a custom agent if you need a new
name/title", and the file is headed "DO NOT EDIT -- overwritten on every
update." The separation of vendor defaults from team and personal overrides is
worked out.

**Where it stops.** At the reliability of a shell-out. Activation Step 1 is
`uv run {project-root}/_bmad/scripts/resolve_customization.py …`, and the
documented fallback is: "**If the script fails**, resolve the `agent` block
yourself by reading these three files … and applying the same structural merge
rules as the resolver." The merge semantics are therefore specified twice — once
executably, once as prose the model is asked to emulate — and the prose path has
no test. The persona layer is also load-bearing in a way nothing verifies:
Step 3 instructs "Do not break character until the user dismisses the persona."

**What it costs to adopt.** A `_bmad/` directory, `uv`/Python on the machine, and
acceptance of a persona-driven interaction style with menus. 573 tracked files
(`git ls-files | wc -l`) — **wrong if** you count `docs-site/` and
`web-bundles/`, which are distribution, not method.

**Who it appears to be for.** Teams that want role separation (analyst,
architect, PM, UX, dev) made explicit, and organisations that need to re-skin
defaults per team without forking.

---

### 4. GSD / get-shit-done (`gsd-build/get-shit-done`)

**Evidence opened:** `hooks/gsd-workflow-guard.js`, `hooks/` listing,
`commands/gsd/` listing, `agents/` listing. HEAD `bdcaab2`, 2026-05-31.

**What it does.** A large command-and-subagent system for Claude Code with
harness-level hooks.

```
ls commands/gsd | wc -l   # -> 67
ls agents | wc -l         # -> 33
ls hooks/                 # 13 hook scripts + lib/
```

**What it does well.** It is the only entry in Shapes 1–4 that attempts
enforcement *outside the model's instruction-following*, via Claude Code hooks
rather than prose. The hook set is specific about distinct risks:
`gsd-workflow-guard.js` (PreToolUse on Write/Edit), `gsd-read-guard.js`,
`gsd-read-injection-scanner.js` (prompt-injection screening of file reads),
`gsd-validate-commit.sh`, `gsd-phase-boundary.sh`, `gsd-context-monitor.js`.
Treating *content the agent reads* as an attack surface is not present in any
other repository surveyed here.

**Where it stops.** Its enforcement is advisory and off by default, and the file
says so plainly:

```
// This is a SOFT guard — it advises, not blocks. The edit still proceeds.
// Enable via config: hooks.workflow_guard: true (default: false)
```

So the guard neither blocks nor runs unless switched on. Separately, this
repository's default branch has not moved since 2026-05-31 — roughly three
months before this survey — while every other actively-developed entry here has
commits within the last two weeks.

**What it costs to adopt.** Claude Code specifically (hooks are harness
features), a Node runtime, 67 commands in the slash namespace, and a `.planning/`
convention. It is the heaviest surface area of the Shape-1 kits.

**Who it appears to be for.** Solo developers and small teams running long
autonomous sessions in Claude Code who are willing to install harness hooks.

**NOT ESTABLISHED.** Web search results assert this repository is no longer the
active home of the project, that development continues under different
governance, and cite a specific precipitating incident. None of that was
verified from a repository. The only fact established here is the HEAD date.
Star counts reported by search results were not verified and are not repeated.

---

### 5. Agent OS (`buildermethods/agent-os`)

**Evidence opened:** `commands/agent-os/shape-spec.md`, `config.yml`,
full `git ls-files` output (24 files). HEAD `475b0ca`, 2026-08-29.

**What it does.** Five commands — `plan-product`, `shape-spec`,
`discover-standards`, `index-standards`, `inject-standards` — plus a profile
system (`profiles/default/global/tech-stack.md`) with optional inheritance
declared in `config.yml`.

**What it does well.** It is the smallest serious entry in this shape, and the
only one that makes the *elicitation* mechanism explicit rather than assumed.
`shape-spec.md` mandates the host's structured question tool — "**Always use
AskUserQuestion tool** when asking the user anything" — and gates itself on
harness state: it requires plan mode and instructs the agent to "**stop
immediately**" with a fixed message if not in it. It also declares its own
scope: "**Keep it lightweight** — This is shaping, not exhaustive
documentation."

**Where it stops.** It has no execution or verification half. Of the five
commands, three concern *standards discovery/indexing/injection* and two concern
*planning*; there is no `implement`, `verify`, `review`, or `tasks` command in
the repository. The shaped spec is handed to the user and the story ends. It is
a front end without a back end, by construction.

**What it costs to adopt.** Very little: a bash installer
(`scripts/project-install.sh`), a `config.yml`, and five commands. 24 tracked
files total.

**Who it appears to be for.** Individuals who want structured intake before
coding and nothing else — no artifact lifecycle, no roles, no validation.

---

### 6. claude-code-spec-workflow (`pimzino/claude-code-spec-workflow`)

**Evidence opened:** `src/markdown/templates/requirements-template.md`,
`src/markdown/agents/spec-requirements-validator.md`, `package.json` `bin`
block. HEAD `f3de74d`, **2025-09-07**.

**What it does.** Installs a requirements → design → tasks workflow plus a
parallel bug workflow (`bug-create`, `bug-analyze`, `bug-fix`, `bug-verify`,
`bug-status`), four validator subagents, and a local web dashboard
(`claude-spec-dashboard` in `package.json`).

**What it does well.** Two things no other Shape-1 entry does. First, it writes
acceptance criteria in **EARS** form as the template default, not as advice —
`requirements-template.md` literally contains
`WHEN [event] THEN [system] SHALL [response]` and
`IF [precondition] THEN [system] SHALL [response]` as numbered slots. Second,
the validators are *separate subagents with their own prompts*, and the
requirements validator is instructed to re-read the template at validation time
via a CLI helper (`claude-code-spec-workflow get-content <path>`) and check
section presence, order, and format against it — a template-conformance check
rather than a vibe check. It also ships a dedicated bug track, acknowledging
that not all work is feature-shaped.

**Where it stops.** It stopped. The default branch's last commit is 2025-09-07,
just over a year before this survey — by far the oldest HEAD among the
agent-era entries here. Its validator invocations hardcode absolute-path
examples for Windows and macOS/Linux and depend on the npm package being
installed and on `PATH`; if the helper is missing the validator's
template-conformance step has no fallback.

**What it costs to adopt.** An npm global install, `.claude/commands/` and
`.claude/templates/` in the project, and acceptance of an unmaintained
dependency.

**Who it appears to be for.** Claude Code users wanting a requirements-first
flow with EARS criteria and a progress dashboard — historically; the archive
value now exceeds the operational value.

---
## Shape 2 — Agent instruction file conventions and their published standards

### 7. AGENTS.md (`openai/agents.md`)

**Evidence opened:** full `git ls-files` (62 files), the repository's own
`AGENTS.md`, `components/CompatibilitySection.tsx`, `Technical_Charter.pdf`
(presence only). HEAD `d001185`, 2026-09-10.

**What it does.** Establishes one filename, `AGENTS.md`, at a repository root as
the place coding agents look for project instructions.

**What it does well.** It solved a coordination problem by refusing to solve
anything else. The compatibility list rendered by the site names roughly twenty
independent tools — Codex, Amp, Jules, Cursor, Factory, RooCode, Aider, Gemini
CLI, goose, Kilo Code, opencode, Phoenix, Zed, Semgrep, Warp, GitHub Copilot,
Ona, Devin, Windsurf, UiPath, Augment Code, Junie — agreeing on a name. The
repository carries a `Technical_Charter.pdf`, consistent with the convention
having been placed under neutral foundation governance rather than remaining a
vendor artifact.

**Where it stops.** There is no specification in the specification repository.
The repo is a Next.js marketing site — `pages/index.tsx`, `components/*.tsx`,
`next.config.ts`, `pnpm-lock.yaml`:

```
git ls-files | grep -iE 'schema|spec|lint|valid|rfc|grammar'
# (no output)
```
**Wrong if:** a spec existed under a name matching none of those six stems. The
full 62-file listing was also read by eye; it contains no such file. So: no
schema, no required fields, no grammar, no conformance tests, no validator, no
version number. The convention is the filename and nothing more.

The repository's own `AGENTS.md` demonstrates the ceiling. It is prose about
that Next.js app: use `npm run dev`, do not run `npm run build` in an agent
session because it "switches the `.next` folder to production assets which
disables hot reload", keep lockfiles in sync, prefer TypeScript, plus a command
table. Useful, project-specific, and entirely unstructured — a worked example of
the format being exactly as strong as whoever writes it.

**What it costs to adopt.** One file. There is no lower-cost convention in this
survey.

**Who it appears to be for.** Everyone, deliberately — the cost is near zero
because the guarantee is near zero.

---

### 8. llms.txt (`AnswerDotAI/llms-txt`)

**Evidence opened:** `llms_txt/core.py`, `llms_txt/miniparse.py`,
`nbs/llms-sample.txt`. HEAD `f5aed2a`, 2026-09-04.

**What it does.** Defines a root-level `llms.txt` listing a project's
documentation as titled, described links grouped under `##` sections, and ships
code to parse it and *expand* it into a single context file.

**What it does well.** Unlike AGENTS.md it publishes an executable grammar. The
link production is built from named regex groups in `core.py`:

```python
pat = fr'-\s*\[{title}\]\({url}\){desc_pat}'   # title/url/desc named groups
```
with `_parse_llms` splitting on `^##\s*(.*?$)` into sections. And it closes the
loop: `llms_txt2ctx` / `create_ctx` fetch the linked documents and materialise
`llms-ctx.txt` and `llms-ctx-full.txt`, both checked into `nbs/`. The convention
therefore produces a verifiable artifact, not just a promise. `nbs/llms-sample.txt`
shows the intended shape, including an `## Optional` section that expanders may
drop — a defined mechanism for budget, which is rare.

**Where it stops.** It is about *retrieval*, not conduct. It tells an agent where
the documentation is; it says nothing about how work should proceed, what must be
decided first, or what "done" means. It also has no notion of staleness: a linked
URL that no longer describes the code parses perfectly.

**What it costs to adopt.** One file plus the discipline of keeping links
accurate; optionally a build step to regenerate context files. The Python package
is `fastcore`-dependent and the sources are nbdev-generated (`core.py` is headed
"AUTOGENERATED! DO NOT EDIT!"), so contributing upstream means working in
notebooks.

**Who it appears to be for.** Library and framework authors who want their docs
consumable by models, and anyone assembling context bundles.

---

### 9. awesome-cursorrules (`PatrickJS/awesome-cursorrules`)

**Evidence opened:** `rules/ai-agent-specialist.mdc`,
`.github/workflows/main.yml`, frontmatter conformance loop. HEAD `b044f95`,
2026-05-31.

**What it does.** A library of per-stack rule files in Cursor's `.mdc` format.

```
git ls-files rules | wc -l    # -> 257
git ls-files | grep -c 'cursorrules$'   # -> 0
```
The second number matters: the collection has fully migrated off the legacy
bare `.cursorrules` filename to frontmattered `.mdc`. **Wrong if:** legacy files
live outside `git ls-files` (they do not; the tree has 295 tracked files total).

**What it does well.** Format conformance is total, and verifiable:

```
for f in $(git ls-files rules); do head -1 "$f" | grep -q '^---$' || echo "NO FM: $f"; done
# (no output) -> 257/257 carry YAML frontmatter
```
**Wrong if:** a file opened with a `---` horizontal rule rather than frontmatter;
sampled files carry real `description`/`globs`/`alwaysApply` keys, e.g.
`globs: **/*`, `alwaysApply: false`. The best rule files also do something the
rest of this shape does not: they state *why*. `ai-agent-specialist.mdc` appends a
`> WHY:` line to each rule ("Use strict TypeScript. Never use `any`. … > WHY: Type
safety prevents runtime errors"), which gives a model grounds to generalise rather
than pattern-match.

**Where it stops.** At prescription of style, with no check on substance. The CI
workflow is about *contribution hygiene and spam*, not rule quality — it verifies
PR author account age against a minimum (`check-pr-author.mjs`,
`PR_AUTHOR_MINIMUM_AGE_DAYS`) and runs a `readme-hygiene` job. Nothing validates
that a rule's advice is current, that its `globs` match anything, or that two
rules do not contradict each other. Rules are also frozen opinions: a file
asserting "React Query for server state, Zustand for client state. No Redux."
carries no expiry.

**What it costs to adopt.** Copy one file. The real cost is downstream — adopting
a stranger's architectural opinions wholesale into an agent's standing context.

**Who it appears to be for.** Cursor users starting a project in a common stack
who want a defensible default instead of a blank rules file.

---

### 10. agent-rules (`steipete/agent-rules`)

**Evidence opened:** `project-rules/commit.mdc`, `install-project-rules.sh`,
frontmatter count. HEAD `42993e4`, 2026-04-27.

**What it does.** A personal library of reusable commands (`/commit`, `/check`,
`/clean`, `/bug-fix`, `/implement-task`, `/five`, `/context-prime`) and
domain references (Swift, SwiftUI, SwiftData, MCP), installed globally.

**What it does well.** The command files are written as *procedures with
options*, not personas — `commit.mdc` documents `/commit` and `/commit
--no-verify`, states that pre-commit checks run by default, and that it
"Suggests splitting commits for different concerns". That is a small, sharp,
testable behaviour. The Swift/MCP references are genuinely deep domain material
rather than generic advice, which is why the repo doubles as a knowledge base.

**Where it stops.** Its own format convention is not upheld. Fewer than half the
`.mdc` files carry the frontmatter the extension implies:

```
ls project-rules/*.mdc docs/*.mdc global-rules/*.mdc | wc -l          # -> 32
for f in $(git ls-files '*.mdc'); do head -1 "$f" | grep -q '^---$' && echo "$f"; done | wc -l   # -> 15
```
15 of 32. **Wrong if:** a file legitimately opens with a `---` rule, or if Cursor
treats frontmatter as optional (it does — which is the point: the convention is
advisory even in its reference library). Installation is also global, not
per-project: `install-project-rules.sh` appends an `@<abs-path>/project-rules`
import to `~/.claude/CLAUDE.md`, so the rules follow the *developer*, not the
repository, and are not shared with collaborators or captured in version control
alongside the code they govern.

**What it costs to adopt.** A bash script and a mutation of the user's global
Claude memory file, plus an absolute path that breaks if the clone moves.

**Who it appears to be for.** An individual developer — heavily Apple-platform —
curating their own cross-project toolkit.

---

### 11. agnix (`agent-sh/agnix`) — conformance tooling for the conventions

**Evidence opened:** `crates/agnix-core/src/rules/agents_md.rs`, the
`crates/agnix-core/src/rules/` listing, root file listing. HEAD `e557022`,
2026-09-07.

**What it does.** A Rust linter and LSP for agent configuration files, with
per-tool rule modules: `agents_md.rs`, `claude_md.rs`, `claude_settings.rs`,
`cursor.rs`, `codex.rs`, `copilot.rs`, `gemini_*.rs` (five of them),
`kiro_*.rs` (five), `mcp.rs`, `hooks/`, `imports.rs`, `cross_platform.rs`.

**What it does well.** It supplies the machinery the AGENTS.md standard omitted,
with numbered, severity-tagged rules and autofixes. From the module header:

```
//! AGM-001: Valid Markdown Structure (HIGH) - unclosed code blocks, malformed links
//! AGM-002: Missing Section Headers (MEDIUM)
//! AGM-003: Character Limit (HIGH) - over 12000 chars (Windsurf compatibility)
//! AGM-004: Missing Project Context (MEDIUM)
//! AGM-005: Platform-Specific Features Without Guard (HIGH)
//! AGM-006: Nested AGENTS.md Hierarchy (MEDIUM)
```
It correctly refuses to apply AGENTS.md rules to CLAUDE.md
(`if !matches!(filename, "AGENTS.md" | "AGENTS.local.md" | "AGENTS.override.md")
{ return diagnostics; }`) — it models the conventions as genuinely different
formats rather than aliases. It ships a `SPEC.md` and `.pre-commit-hooks.yaml`,
so it is installable as a gate.

**Where it stops.** Its rules are about *tool compatibility and syntax*, not
truth. `AGM-003` is a 12,000-character cap justified by Windsurf's limit
(`WINDSURF_CHAR_LIMIT`); `AGM-002` wants headers to exist. None of these can tell
you the build command documented in the file is wrong. A perfectly conformant
AGENTS.md may be entirely false.

**What it costs to adopt.** A Rust binary (Homebrew formula present at
`Formula/agnix.rb`) plus `.agnix.toml`. It is a large dependency for a linting
concern.

**Who it appears to be for.** Teams maintaining agent config across several
tools who want CI to catch drift in format and per-tool limits.

---

### 12. agents-lint (`giacomo/agents-lint`)

**Evidence opened:** `src/checkers/filesystem.ts`, the `src/checkers/` listing,
`.agents-lint.json`. HEAD `203f33e`, 2026-03-26.

**What it does.** Checks an `AGENTS.md` against the repository it describes.
Checkers: `filesystem.ts`, `npm-scripts.ts`, `dependencies.ts`, `framework.ts`,
`structure.ts`, `memory.ts`, `cross.ts`.

**What it does well.** It attacks the failure mode agnix cannot: *the file is
well-formed and wrong*. `checkFilesystem` extracts `parsed.mentionedPaths`,
skips URLs and `$`-prefixed environment variables, resolves each against the repo
root, and reports non-existent paths at configurable severity
(`config.severity?.missingPath ?? 'error'`). Paired with `npm-scripts.ts` and
`dependencies.ts`, this is drift detection against ground truth in the
repository — the only instance of that idea in Shape 2.

**Where it stops.** At references it can resolve mechanically. It can prove
`src/foo.ts` exists; it cannot check that the *description* of `src/foo.ts` is
accurate, that the architectural claims hold, or that an instruction is still the
team's intent. It is also the second-oldest agent-era HEAD in the corpus
(2026-03-26) and a small single-maintainer project (40 tracked files).

**What it costs to adopt.** An npm dev dependency, `.agents-lint.json`, and a CI
job (`.github/workflows/agents-lint.yml` is present and runs on itself).

**Who it appears to be for.** Teams whose AGENTS.md has grown large enough to rot.

---

### Shape 2 — what was searched and not found

**No formal schema for AGENTS.md exists in its own standards repository.**
Searched: `git ls-files | grep -iE 'schema|spec|lint|valid|rfc|grammar'` over
`openai/agents.md` (no output), plus a full read of the 62-file listing. Varied
by tool and wording: web search for
`"AGENTS.md" specification schema linter validator standard`, which returned
third-party explainers describing the format and one of which states plainly that
the spec "defines no required fields, so there is no fixed schema" — consistent
with the repository. A second, differently-worded search
(`agents.md validator lint github repository ... npm`) surfaced validators, all
of which turned out to be **third-party** (agnix, agents-lint, cclint,
agent-skills-lint, AgentLinter). Two were cloned and are entries 11 and 12.
Conclusion: validation exists, but none of it is published by the standard.

**Not pursued, therefore not entries:** `carlrannaberg/cclint`,
`swarmclawai/agent-skills-lint`, `agentsmd/agents.md`, `AgentLinter`. All
returned HTTP 200 from `api.github.com/repos/<owner>/<repo>`, so they exist, but
no file in any of them was opened and they are excluded under the evidence rule.

---
## Shape 3 — Subagent, role, and multi-agent orchestration frameworks

### 13. wshobson/agents

**Evidence opened:** `plugins/accessibility-compliance/agents/ui-visual-validator.md`,
`plugins/agent-orchestration/commands/multi-agent-optimize.md`,
`tools/validate_generated.py`, `tools/` listing. HEAD `a30778f`, 2026-09-01.

**What it does.** Ships a very large catalogue of agent, skill and command
definitions, organised as plugins and generated out to several harnesses.

```
ls plugins | wc -l                                        # -> 92
git ls-files | grep -cE 'plugins/[^/]+/agents/.*\.md$'    # -> 202
git ls-files | grep -cE 'plugins/[^/]+/skills/'           # -> 425
git ls-files | grep -cE 'plugins/[^/]+/commands/.*\.md$'  # -> 105
```
**Wrong if:** the skills figure is read as 425 skills — it counts *files* under
`skills/`, and a skill directory holds `SKILL.md` plus references and scripts, so
the number of skills is materially lower. The agents and commands counts are
one-file-per-unit and hold.

**What it does well.** It is the only markdown-catalogue project here with a real
build and verification pipeline. `tools/` contains `generate.py`,
`validate_generated.py`, `check_agent_name_collisions.py`, `doc_gardener.py`, and
installers for Copilot, OpenCode and Antigravity, plus `tools/adapters/`. The
validator states its purpose precisely: "Approximates harness round-trip without
installing each CLI. For every adapter output, parse and validate against
documented schemas. Surface issues with file paths and remediation hints." It
supports `--harness codex` and `--strict` (exit non-zero on warnings). A
name-collision checker exists because at 202 agents collisions are a real
failure. Individual agent prompts are also sharper than the genre average —
`ui-visual-validator.md` sets an adversarial prior: "Default assumption: The
modification goal has NOT been achieved until proven otherwise … Ignore any code
hints or implementation details - base judgments solely on visual evidence."

**Where it stops.** Its orchestration is prose. `agent-orchestration` is a plugin
containing one agent (`context-manager.md`) and two commands; the command named
`multi-agent-optimize.md` reads as a description of a system that does not exist
in the repository — "Intelligent multi-agent coordination", "Distributed
performance monitoring across system layers", "Real-time metrics collection",
with `$TARGET`/`$BUDGET_CONSTRAINTS` argument placeholders and no code to bind
them. The rigour visible in `tools/` did not reach the orchestration content.

**What it costs to adopt.** Install a plugin (marketplace manifests exist for
Claude, Cursor, Codex, `.agents/`). Cost is context and namespace: adopting
broadly means many agent descriptions competing for selection.

**Who it appears to be for.** People who want a specialist on hand for almost any
technology, chosen à la carte.

---

### 14. awesome-claude-code-subagents (`VoltAgent`)

**Evidence opened:** `categories/09-meta-orchestration/multi-agent-coordinator.md`,
`categories/01-core-development/README.md`, `.github/workflows/` listing.
HEAD `3097abe`, 2026-09-07.

**What it does.** 178 files under `categories/`, ten numbered categories from
core development to meta-orchestration and research.

**What it does well.** It is the most epistemically disciplined agent catalogue in
this survey, and visibly the product of a correction. `multi-agent-coordinator.md`
constrains itself against the exact failure seen in entry 13:

> "There is **no runtime message bus in this repo**. Subagents in Claude Code
> coordinate two ways: through shared files … and through the orchestrator …
> Plan around those two mechanisms, not an imagined RPC/queue/WebSocket layer."
> "Do not invent throughput, latency, efficiency, or agent-count numbers. If you
> have not measured something, do not state it as a fact."

It also scopes each agent to its actual tool grant (`tools: Read, Write, Edit,
Glob, Grep`) and reasons from it: "You cannot run a message bus, spawn processes,
open sockets, or execute a workflow engine. Do not claim to." And it requires
inputs rather than guessing: "If the agent roster or the task boundaries are not
given, ask." Category READMEs carry explicit "Use when:" guidance per agent.

**Where it stops.** At markdown. There is no generator, no validator, no
collision check; the sole CI workflow is `enforce-plugin-version-bump.yml`. Its
honesty is a property of how the prompts were *written*, enforced by review
rather than by tooling — which means it holds only as long as the maintainers
keep holding it.

**What it costs to adopt.** `install-agents.sh`, or copy individual files. Low.

**Who it appears to be for.** Claude Code users who want role definitions that
will not hallucinate infrastructure.

---

### 15. claude-flow (`ruvnet/claude-flow`)

**Evidence opened:** `v3/src/coordination/application/SwarmCoordinator.ts`,
`v3/src/` tree, `.claude/commands/` listing. HEAD `005a0ed`, 2026-09-11.

**What it does.** A runtime for coordinating many agents — topologies, memory
backends, an MCP server, a plugin system — alongside a very large body of
markdown commands and agent definitions.

```
git ls-files | wc -l                          # -> 5685
git ls-files | grep -cE '\.claude/agents/'    # -> 297
git ls-files | cut -d/ -f1 | sort | uniq -c | sort -rn | head -3
#   3515 v3   641 plugins   556 ruflo
```

**What it does well.** Unlike entries 13 and 14, coordination here is executable
code, layered in a deliberate architecture: `agent-lifecycle/domain/Agent.ts`,
`coordination/application/SwarmCoordinator.ts`,
`task-execution/domain/Task.ts`, `infrastructure/mcp/MCPServer.ts`, and three
memory backends (`SQLiteBackend`, `AgentDBBackend`, `HybridBackend`).
`SwarmCoordinator` is typed against real concepts — `SwarmTopology`,
`MeshConnection`, `ConsensusDecision`, `ConsensusResult`, `AgentMetrics` — and
documents its lineage ("Based on agentic-flow's AttentionCoordinator pattern").
Persistent cross-session memory as a first-class backend is rare here.

**Where it stops.** At comprehensibility and boundaries. 5,685 tracked files with
a `v3/` rewrite (3,515 files) sitting beside `ruflo/` (556) and `plugins/` (641)
means a reader cannot easily tell which surface is current. The 297 agent
definitions under `.claude/agents/` are on the same scale as entry 13's entire
catalogue, and `.claude/commands/analysis/` contains a
`COMMAND_COMPLIANCE_REPORT.md` — an artifact implying the command set had drifted
far enough to need auditing. Adoption means adopting its whole world: its MCP
server, its memory store, its plugin model.

**What it costs to adopt.** High. Node/TypeScript runtime plus Rust crates
(`v3/crates`), an MCP server, a database, and a large slash-command namespace.

**Who it appears to be for.** People who want a persistent multi-agent swarm
runtime and will accept a large, fast-moving dependency to get it.

---

### 16. CrewAI (`crewAIInc/crewAI`)

**Evidence opened:** `lib/cli/src/crewai_cli/templates/crew/config/agents.yaml`,
`.../crew/config/tasks.yaml`, `lib/crewai/src/crewai/` module listing, templates
listing. HEAD `c5759ce`, 2026-09-11.

**What it does.** A Python framework for building applications out of
role-playing agents with assigned tasks. Scaffolds a project where roles and
tasks are declared in YAML and wired in `crew.py`.

**What it does well.** It separates *declaration* from *code* cleanly, and the
declaration is small enough to read. Agents are `role` / `goal` / `backstory`;
tasks are `description` / `expected_output` / `agent`, with `{topic}` and
`{current_year}` interpolation. Crucially, every task must state an
`expected_output` — the schema forces an answer to "how will we know this task
produced the right thing", which most role catalogues in Shape 3 never ask. The
surrounding library is broad and current: `flow/`, `memory/`, `knowledge/`,
`rag/`, `security/`, `a2a/`, `hooks/`, `skills/`, and a `declarative_flow`
template with `flow.yaml`. It also ships `AGENTS.md` inside its own scaffolds
(`templates/AGENTS.md`, `templates/declarative_flow/AGENTS.md`) — a framework
generating the Shape-2 convention for the projects it creates.

**Where it stops.** At a different problem. CrewAI builds *agentic products* —
a crew that researches a topic and writes a report. It is not a discipline for a
repository of human-and-agent software work: nothing in it concerns
specifications, review gates, decision records, or the state of your codebase.
The default scaffold is a researcher and a reporting analyst, not a developer.

**What it costs to adopt.** A Python project, a `crew.py`, and the framework's
execution model. It is a dependency of your application, not a layer over your
editor.

**Who it appears to be for.** Developers shipping multi-agent features inside
their own software.

---

### 17. AutoGen / Magentic-One (`microsoft/autogen`)

**Evidence opened:**
`python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_prompts.py`,
the `_group_chat/` listing, `python/packages/agbench/` tree. HEAD `027ecf0`,
**2026-04-06** (default branch).

**What it does.** A research framework for multi-agent conversation: group chats
with pluggable managers, a graph/digraph team builder
(`_graph/_digraph_group_chat.py`, `_graph_builder.py`), and the Magentic-One
orchestrator. Packages include `autogen-core`, `autogen-agentchat`,
`autogen-ext`, `autogen-studio` and `agbench`.

**What it does well.** Magentic-One's orchestrator maintains a structured
*ledger* whose fields encode the failure modes of long agent runs as
first-class, model-answered questions:

```python
class LedgerEntry(BaseModel):
    is_request_satisfied: LedgerEntryBooleanAnswer
    is_in_loop: LedgerEntryBooleanAnswer
    is_progress_being_made: LedgerEntryBooleanAnswer
    next_speaker: LedgerEntryStringAnswer
    instruction_or_question: LedgerEntryStringAnswer
```
Explicit stall-and-loop detection, re-evaluated each turn and used to choose the
next speaker, is a mechanism no other Shape-3 entry implements. It is also the
only orchestration project here shipping its own benchmark harness in-tree
(`agbench`, with GAIA templates, `init_tasks.py`, `custom_tabulate.py`).

**Where it stops.** At research framing, and possibly at maintenance. It is a
library for building agent teams in Python — there is no project-repository
discipline in it, no artifacts, no gates over a codebase. Its default branch is
five months stale at the time of this survey, by far the longest gap among
actively-marketed entries.

**NOT ESTABLISHED:** whether that staleness reflects abandonment, a branch move,
or consolidation into a successor product. `--single-branch` fetched only the
default branch, so a `main`-adjacent active branch would be invisible here. No
claim is made either way.

**What it costs to adopt.** A Python dependency and its execution model; adopting
Magentic-One additionally implies its browser/file/coder agent set.

**Who it appears to be for.** Researchers and engineers studying or building
multi-agent systems.

---

## Shape 4 — Prompt and workflow libraries shipped as repositories

### 18. fabric (`danielmiessler/fabric`)

**Evidence opened:** `data/patterns/extract_wisdom/system.md`,
`data/strategies/` listing, pattern inventory. HEAD `b682dad`, 2026-09-07.

**What it does.** A Go CLI plus a large library of "patterns" — single-purpose
system prompts applied to piped input.

```
ls data/patterns | wc -l          # -> 256
ls data/patterns/*/user.md | wc -l # -> 47
ls data/strategies                 # aot, cod, cot, ltm, reflexion,
                                   # self-consistent, self-refine, standard, tot
```

**What it does well.** Its patterns are unusually *specified* for prompts. They
are written as an explicit contract — `# IDENTITY and PURPOSE`, `# STEPS`,
`# OUTPUT INSTRUCTIONS` — and the steps name the output sections and bound their
size: "Extract 20 to 50 … into a section called IDEAS:", "Extract a summary … in
25 words", "a 15-word sentence". A downstream consumer can predict the shape of
the output, which makes the patterns composable in shell pipelines. Separating
reasoning *strategies* (chain-of-thought, tree-of-thought, self-refine,
reflexion) into `data/strategies/*.json`, orthogonal to the 256 task patterns, is
a genuine factorisation. The Go core is tested (`internal/plugins/db/fsdb/patterns_test.go`,
`internal/tools/patterns_loader_test.go`, `internal/tools/custom_patterns/custom_patterns_test.go`).

**Where it stops.** At the single stateless transform. A pattern takes text in
and gives text out; there is no state between invocations, no notion of a
project, a file tree, or a previous decision. The library is also uneven — only
47 of 256 patterns supply a `user.md`, and patterns carry no frontmatter,
version, or metadata, so there is nothing to lint and no way to tell a
maintained pattern from an abandoned one. The tests cover the *loader*, not the
patterns.

**What it costs to adopt.** A Go binary and an API key; patterns are plain
directories, trivially copied or forked.

**Who it appears to be for.** Individuals doing high-volume text work —
summarising, extracting, analysing — from a terminal.

---

### 19. anthropics/skills

**Evidence opened:** `template/SKILL.md`, `skills/skill-creator/` file listing,
`skills/skill-creator/scripts/run_eval.py`,
`skills/skill-creator/scripts/quick_validate.py`. HEAD `34040c9`, 2026-09-10.

**What it does.** A small reference set of Agent Skills — a `SKILL.md` with
YAML frontmatter (`name`, `description`) plus optional bundled scripts,
references and assets.

```
git ls-files | grep -c 'SKILL.md$'   # -> 20   (19 skills + 1 template)
```

**What it does well.** It is the only prompt-library repository in this survey
that ships **an evaluation loop for its own prompts**. `skills/skill-creator/`
contains `scripts/run_eval.py`, `run_loop.py`, `aggregate_benchmark.py`,
`generate_report.py`, `improve_description.py`, `package_skill.py`,
`quick_validate.py`, three grader subagents (`agents/grader.md`,
`comparator.md`, `analyzer.md`) and an `eval-viewer/`. `run_eval.py` targets a
precise, measurable property — *triggering*: it "Tests whether a skill's
description causes Claude to trigger (read the skill) for a set of queries",
spawning real `claude -p` subprocesses in a process pool and emitting JSON. It
also mimics the harness's own project-root discovery by walking up for `.claude/`
so the generated command file lands where the CLI will find it. `quick_validate.py`
enforces the structural contract (SKILL.md present, frontmatter parses).
The `template/SKILL.md` is five lines — the format's floor is deliberately low.

**Where it stops.** The eval measures *selection*, not *quality*: whether the
skill fires, not whether following it produces good work. And the catalogue is
about document and artifact production — `docx`, `pdf`, `pptx`, `xlsx`,
`canvas-design`, `brand-guidelines`, `slack-gif-creator`. Of nineteen skills, the
only ones touching software process are `mcp-builder`, `webapp-testing` and
`skill-creator` itself. There is no skill here about running a project.

**What it costs to adopt.** Copy a directory. The format is the cheapest
structured unit in Shape 4; the eval tooling costs API spend and wall time.

**Who it appears to be for.** Skill authors — it is a reference implementation
and a toolkit for making more skills, more than a body of work-process content.

---

### 20. superpowers (`obra/superpowers`)

**Evidence opened:** `skills/writing-plans/SKILL.md`, `skills/` listing, root
listing. HEAD `b36e082`, 2026-08-12.

**What it does.** Fourteen skills covering software *process* rather than
technology: `brainstorming`, `writing-plans`, `executing-plans`,
`test-driven-development`, `systematic-debugging`, `requesting-code-review`,
`receiving-code-review`, `verification-before-completion`,
`subagent-driven-development`, `dispatching-parallel-agents`,
`using-git-worktrees`, `finishing-a-development-branch`, `writing-skills`,
`using-superpowers`.

**What it does well.** It is the only entry in Shape 4 whose subject is the
conduct of engineering work, and its guidance is specific enough to act on.
`writing-plans` sets the reader model explicitly ("assuming the engineer has zero
context for our codebase and questionable taste"), fixes an output location
(`docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`), requires a file-structure
map *before* tasks ("This is where decomposition decisions get locked in"), and
defines task granularity by a review criterion rather than by size: "A task is
the smallest unit that carries its own test cycle and is worth a fresh reviewer's
gate … split only where a reviewer could meaningfully reject one task while
approving its neighbor." It also pairs each skill with an artifact where useful
(`plan-document-reviewer-prompt.md`) and requires the agent to announce which
skill it is using. Distribution manifests exist for six harnesses
(`.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.devin-plugin/`,
`.hermes-plugin/`, `.kimi-plugin/`, plus `.opencode/` and `.pi/`), with
`AGENTS.md`, `CLAUDE.md` and `GEMINI.md` at root.

**Where it stops.** Nothing verifies compliance. These are instructions to a
model about how to behave; there is no schema for a plan, no validator, no gate,
and no persisted decision record — `verification-before-completion` is a prompt,
not a check. Plans are written to a directory and their conformance to the
skill's own rules is never tested. Unlike entry 19's sibling, there is no eval
harness in the repository.

**What it costs to adopt.** Install a plugin; 195 tracked files, no runtime.

**Who it appears to be for.** Developers who want their agent to follow a
recognisable engineering process — plan, review, test, verify — rather than a
technology specialisation.

---

### 21. awesome-claude-code (`hesreallyhim`)

**Evidence opened:** `Makefile`, `THE_RESOURCES_TABLE_NEW.csv` (header + rows),
`.github/workflows/` listing. HEAD `63c84a1`, 2026-09-11.

**What it does.** An index of the ecosystem, generated from a CSV.

```
tail -n +2 THE_RESOURCES_TABLE_NEW.csv | wc -l   # -> 211
```
**Wrong if:** a description field contains an embedded newline, which would
inflate the line count above the true row count; the file is comma-quoted and the
sampled rows are single-line, but this was not parsed as CSV.

**What it does well.** It treats a list as a data pipeline, which is rare and
worth noting on its own. The `Makefile` states the contract: "THE_RESOURCES_TABLE_NEW.csv
is the single source of truth. `make generate` renders it (plus config.yaml +
templates/README.template.md) into README.md. Generation is idempotent
(re-running yields a byte-identical README.md) and fails closed if an Active
entry has a Category missing from config.yaml." The schema carries lifecycle
columns — `Active`, `Date Added`, `Last Checked`, `Stale` — so entries can be
*retired* rather than accumulating, and CI automates submission and README
regeneration (`validate-new-issue.yml`, `handle-resource-submission-commands.yml`,
`regenerate-readme.yml`, `update-repo-ticker.yml`). Idempotent generation plus
fail-closed validation is a stronger discipline than most of the content it
indexes.

**Where it stops.** It ships no prompts, skills, or commands of its own — it is a
pointer, and its `Description` fields are editorial claims about other
repositories, exactly the kind of secondhand evidence this survey does not treat
as sufficient. `Last Checked` and `Stale` exist as columns; whether they are
maintained was not verified.

**What it costs to adopt.** Nothing — it is read, not installed.

**Who it appears to be for.** People surveying the ecosystem, and maintainers
wanting a model for how to keep a list from rotting.

---
## Shape 5 — Research and evaluation harnesses

### 22. Inspect AI (`UKGovernmentBEIS/inspect_ai`)

**Evidence opened:** `examples/hello_world.py`, `src/inspect_ai/scorer/` listing,
`src/inspect_ai/approval/` listing, `src/inspect_ai/util/_sandbox/` listing,
`src/inspect_ai/_cli/` listing. HEAD `03befb4`, 2026-09-11.

**What it does.** A framework for writing and running evaluations. A `Task`
composes a `dataset`, a `solver` chain, and a `scorer`:

```python
@task
def hello_world():
    return Task(dataset=[Sample(input="Just reply with Hello World",
                                target="Hello World")],
                solver=[generate()], scorer=exact())
```

**What it does well.** Three things stand out in the source. First, scoring is a
library, not an exercise for the reader — `scorer/` ships `_match.py`,
`_pattern.py`, `_choice.py`, `_classification.py`, `_math.py`, `_model.py`
(model-graded), `_cascade.py`, `_multi.py`, `_perplexity.py`, plus `_metrics/`
and `_reducer/` for aggregating repeated runs. Second, it takes *execution*
seriously: `util/_sandbox/` contains a Docker backend, `limits.py`,
`self_check.py`, `exec_remote.py` and a JSON-RPC transport — agents under
evaluation run in real, bounded sandboxes. Third, and unusually, it has a
first-class **approval** layer (`approval/_policy.py`, `_approver.py`,
`_human/`), so a human can gate tool calls mid-evaluation. Operationally it is a
product, not a script: the CLI carries `eval`, `score`, `view`, `log`, `trace`,
`cache`, `detach`, `sandbox`, and the log module has `_recover.py`, `_condense.py`
and `_bundle.py` — recovery of interrupted runs and shareable log bundles.

**Where it stops.** It evaluates *a model or agent on tasks you define*. It has
no opinion about, and no hooks into, the repository you are building. Nothing in
it reads your specs, gates your commits, or scores your project's own artifacts.
The dataset, the solver and the scorer are all yours to author; the harness
supplies rigour, not content.

**What it costs to adopt.** A Python dependency plus Docker for sandboxed tasks,
and — the real cost — authoring datasets and scorers, which is the majority of
the work in any evaluation.

**Who it appears to be for.** Safety institutes, labs and teams doing systematic
model and agent evaluation, including with human oversight in the loop.

---

### 23. promptfoo (`promptfoo/promptfoo`)

**Evidence opened:** `src/assertions/` listing,
`examples/eval-assertions-generate/promptfooconfig.yaml`, `examples/` count.
HEAD `c2b1a2f`, 2026-09-11.

**What it does.** Declarative prompt/agent testing from a YAML file: providers,
prompts, `tests` with `vars`, and `assert` blocks.

```
ls src/assertions/*.ts | wc -l   # -> 57
ls examples | wc -l              # -> 229
```
**Wrong if:** the 57 is read as 57 assertion *types* — it counts files, and
`index.ts`, `contextUtils.ts`, `assertionsResult.ts` and
`scriptResultNormalization.ts` are infrastructure, so the true count is a few
lower.

**What it does well.** It makes prompt testing look like ordinary testing, with a
low activation cost: a YAML file, a schema reference
(`# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json`) so
editors autocomplete and validate, and 229 runnable examples. Its assertion range
covers both deterministic checks (`equals`, `contains`, `regex`, `json`,
`levenshtein`, `cost`, `latency`, `finishReason`, `functionToolCall`) and graded
ones (`llmRubric`, `geval`, `factuality`, `modelGradedClosedQa`,
`agentRubric`), alongside RAG-specific scorers (`contextFaithfulness`,
`contextRecall`, `contextRelevance`, `answerRelevance`) and safety ones
(`moderation`, `guardrails`, `refusal`, `redteam`). `defaultTest` lets one rubric
set apply across cases, and named `metric:` labels aggregate across assertions —
so you get a scorecard, not a pass/fail. Escape hatches to `javascript.ts`,
`python.ts` and `ruby.ts` mean anything unsupported is still expressible.

**Where it stops.** At an input/output pair. Its unit is a prompt and a
completion; multi-step work in a repository — an agent that reads files, edits
them, runs tests over an hour — is not what the config shape describes. Graded
assertions also move the problem rather than solving it: `llm-rubric` is a model
judging a model, and nothing in the config calibrates the judge.

**What it costs to adopt.** An npm dependency and a YAML file. Lowest adoption
cost of the three general harnesses here. Running graded assertions costs API
spend per test matrix cell.

**Who it appears to be for.** Product teams shipping LLM features who want
regression tests and a red-team pass in CI.

---

### 24. SWE-bench (`SWE-bench/SWE-bench`)

**Evidence opened:** `swebench/harness/grading.py`,
`swebench/harness/log_parsers/` listing, `swebench/harness/run_evaluation.py`.
HEAD `02e7a74`, 2026-09-02.

**What it does.** Evaluates whether a generated patch resolves a real GitHub
issue, by building a container per instance, applying the patch, running the
repository's own test suite, and parsing the results.

**What it does well.** Its grading criterion is the sharpest definition of "done"
in this survey, and it is two-sided. `grading.py` computes over both
`FAIL_TO_PASS` (tests that must start passing) and `PASS_TO_PASS` (tests that
must not break):

```
grep -n "FAIL_TO_PASS\|PASS_TO_PASS" swebench/harness/grading.py
```
Requiring non-regression alongside the fix is what makes the metric meaningful.
The unglamorous part is where the real work is: `log_parsers/` has separate
parsers for C, Go, Java, JavaScript, PHP, Python, Ruby and Rust, because "did the
test pass" is a per-ecosystem text-parsing problem. `infra_failure.py` exists to
distinguish a harness failure from a model failure — a distinction most
evaluation code omits, and without which scores are quietly wrong. Execution is
containerised (`docker_utils.py`, `image_builder/`) with a Modal backend
(`--modal`) for scale.

**Where it stops.** At its own instances. It grades submissions against a fixed,
curated dataset of historical issues from specific repositories; you cannot point
it at your project and ask how your agent is doing. It measures patch outcomes
only — nothing about process, cost, number of turns, or whether the change is
maintainable. And because the instances are historical public commits, it says
nothing about work on private code.

**What it costs to adopt.** Docker and substantial compute; it is a benchmark you
submit to, not a tool you install in a project.

**Who it appears to be for.** Researchers and tool builders measuring
issue-resolution capability.

---

### 25. In-repo eval loops: `skill-creator` and `agbench`

**Evidence opened:** `anthropics/skills/skills/skill-creator/scripts/run_eval.py`,
`.../agents/grader.md`, `.../scripts/aggregate_benchmark.py`;
`microsoft/autogen/python/packages/agbench/benchmarks/GAIA/Scripts/init_tasks.py`
and `.../Templates/MagenticOne/scenario.py`.

**What they do.** Both are evaluation harnesses shipped *inside* the project they
evaluate rather than as standalone products — described under entries 19 and 17
respectively, and recorded here so Shape 5 reflects them.

**What they do well.** They demonstrate the smallest viable form of the shape: a
script that runs the real thing many times, a grader, and an aggregator
(`run_eval.py` → `agents/grader.md` → `aggregate_benchmark.py` →
`generate_report.py` → `eval-viewer/viewer.html`). `agbench` shows the same
pattern with per-benchmark `Templates/` and `Scripts/custom_tabulate.py`, i.e.
tabulation is expected to be benchmark-specific.

**Where they stop.** Neither is reusable outside its parent: `run_eval.py` imports
`scripts.utils` and shells out to `claude -p`, so it is bound to one harness and
one narrow property (does the skill trigger); `agbench`'s benchmarks are GAIA and
friends, not your repository.

**What they cost to adopt.** As products, nothing — they are not distributed as
such. As a pattern, the cost is API spend and writing your own grader.

**Who they appear to be for.** Maintainers of prompt/agent artifacts who want to
stop guessing whether an edit helped.

---

### Shape 5 — what was searched and not found

Searched for an evaluation harness aimed at *a team's own coding-agent project*
— i.e. one you point at your repository to test whether your instructions,
skills and workflows are working — as opposed to a model benchmark or a
prompt-level test runner.

- Repository inspection: `inspect_ai`, `promptfoo`, `SWE-bench`, `agbench`,
  `skill-creator`. All five evaluate either a model on authored tasks, a prompt
  on authored cases, or a patch against a fixed benchmark.
- Web search, first wording: `evaluation harness for your own coding agent
  project regression testing prompts CI github repo`. Returned several small
  candidate repositories (`ai-evaluation-harness`, `pi-harness`,
  `proofagent-harness`, `agent-eval-harness`, plus two "awesome harness
  engineering" lists).
- **None of those candidates was cloned or opened.** Under the evidence rule they
  are not entries and nothing is claimed about them. They are recorded as
  unexplored leads, not as absence.

The honest statement: **within the corpus actually opened, this sub-shape is
empty.** Every harness examined evaluates the model or the prompt; none evaluates
the project's own agent-facing scaffolding against that project. Whether the
unexplored candidates fill it is NOT ESTABLISHED.

---

## Shape 6 — Documentation-as-source-of-truth systems that predate coding agents

### 26. adr-tools (`npryce/adr-tools`)

**Evidence opened:** `src/adr-new`, `src/template.md`, `src/_adr_add_link`,
`src/` listing. HEAD `b3279ba`, **2020-03-30**.

**What it does.** A bash CLI for Nygard-style Architecture Decision Records:
`adr init`, `adr new`, `adr link`, `adr list`, `adr generate` (table of contents
and a graph).

**What it does well.** It makes the *relationships between decisions*
operational, not just documented. `adr new -s <n>` supersedes a prior ADR and
mutates both files: `_adr_add_link` walks the target's `## Status` section with
awk and inserts a markdown link, and the superseded record's status is rewritten
to record it. Links are bidirectional by construction — the `-l
TARGET:LINK:REVERSE-LINK` form takes both directions as arguments. The template
is four sections and does not budge: Status, Context, Decision, Consequences,
with Consequences framed as "What becomes easier or more difficult to do and any
risks introduced". The whole thing is POSIX shell and awk with no runtime, and
`adr new` prints the filename to stdout "so the command can be used in scripts".

**Where it stops.** It stopped six years ago. The default branch has not moved
since 2020-03-30 — the oldest HEAD in this corpus by a wide margin. Functionally
it records and links; it never validates. Nothing checks that a decision is still
true, that the code reflects it, that a superseded ADR is not still being cited,
or that a decision was made at all before the code changed.

**What it costs to adopt.** A shell script on `PATH` and a `doc/adr/` directory.
Essentially free, and the artifacts survive the tool — plain markdown with
numbered filenames.

**Who it appears to be for.** Any team wanting decisions recorded in the
repository with the reasoning attached. Its ideas outlived its maintenance.

---

### 27. MADR (`adr/madr`)

**Evidence opened:** `template/adr-template.md`, `template/` listing,
`template/.markdownlint.yml`. HEAD `ba75bb1`, 2026-08-28.

**What it does.** A maintained ADR template — Markdown Any Decision Records — in
four graded sizes: `adr-template.md`, `adr-template-minimal.md`,
`adr-template-bare.md`, `adr-template-bare-minimal.md`, plus i18n (`i18n/de/`).

**What it does well.** It captures what entry 26's template omits: the
*alternatives* and the *people*. The full template has `Decision Drivers`,
`Considered Options`, `Decision Outcome` with a forced justification clause —
`Chosen option: "{title}", because {justification …}` — and `Consequences`
split into "Good, because" / "Bad, because" lines. Its YAML frontmatter names
roles from a responsibility model: `decision-makers`, `consulted` ("typically
subject-matter experts; and with whom there is a two-way communication"),
`informed` ("one-way communication"). Every optional element is marked
`<!-- This is an optional element. Feel free to remove. -->`, so shrinking the
template is sanctioned rather than a deviation — which is why four sizes exist.
It documents its own founding decision as an ADR
(`template/0000-use-markdown-architectural-decision-records.md`) and ships
`.markdownlint.yml`.

**Where it stops.** At the document. There is no CLI, no numbering helper, no
supersede mechanic, no link graph — the capabilities entry 26 had. Adopting MADR
means adopting a shape and doing the bookkeeping yourself or with another tool.
Nothing validates that `Considered Options` actually lists more than one.

**What it costs to adopt.** Copy a template file. Near zero.

**Who it appears to be for.** Teams that want richer decision records than
Nygard's four sections, especially where who-was-consulted matters.

---

### 28. arc42 (`arc42/arc42-template`)

**Evidence opened:** `EN/adoc/01_introduction_and_goals.adoc`, the `EN/` file
listing, top-level language directories. HEAD `8dff0d9`, 2026-07-07.

**What it does.** A fixed twelve-section table of contents for software
architecture documentation: Introduction and Goals, Constraints, Context and
Scope, Solution Strategy, Building Block View, Runtime View, Deployment View,
Concepts, Architecture Decisions, Quality Requirements, Technical Risks,
Glossary.

**What it does well.** Two mechanisms worth naming. First, the help text is
*toggleable and ships inside the template*: every section wraps its guidance in
`ifdef::arc42help[]` / `endif::arc42help[]` blocks with `[role="arc42help"]`, so
a team renders a guided version while learning and a clean version for
publication — the scaffolding is removable without editing the document.
Structured `.Contents` / `.Motivation` headings inside those blocks tell the
author what belongs there *and why it is worth writing*. Second, it is genuinely
internationalised: roughly ten language directories (CZ, DE, EN, ES, FR and more,
at 18–21 files each), which matters for the organisations that use it. Section 9
delegates to ADRs rather than reinventing them, so it composes with entries 26
and 27.

**Where it stops.** At the table of contents. There is no traceability of any
kind — no links from a quality requirement to the building block that satisfies
it, no identifiers, nothing that connects any section to code. It cannot tell you
a section is empty, stale, or contradicted by the system. It is a prompt for
humans, rendered by AsciiDoc.

**What it costs to adopt.** Copy the language/format variant you want (AsciiDoc,
and other formats in the wider distribution) and wire up a doc build.

**Who it appears to be for.** Architects in organisations where a recognisable,
complete architecture document is expected — often regulated or large.

---

### 29. Diátaxis (`evildmp/diataxis-documentation-framework`)

**Evidence opened:** `source/compass.rst`, `source/` listing, tooling check.
HEAD `957c09c`, 2026-08-06.

**What it does.** Classifies all documentation into four modes — tutorials,
how-to guides, reference, explanation — along two axes (practical/theoretical,
study/work), and argues the four must not be mixed.

**What it does well.** It provides a *decision procedure*, not just a taxonomy.
`source/compass.rst` is explicit that intuition is insufficient — "Often when
working with documentation, an author is faced with the question: *what form of
documentation is this?* … and no obvious, intuitive answer. Worse, sometimes
intuition provides an immediate answer that is also wrong" — and answers it with
a compass table ("If the content…") described as "something like a truth-table or
decision-tree of documentation … a course-correction tool". Reducing a
two-dimensional judgement to a lookup is what makes it usable under pressure, and
it is why the framework spread. It also treats documentation quality as a
separate concern (`source/quality.rst`) from structure.

**Where it stops.** It ships no artifacts at all:

```
git ls-files | grep -iE 'template|lint|check'
# _templates/page.html      (a Sphinx HTML theme override — not a doc template)
```
**Wrong if:** templates live outside version control, which for a docs repository
would be unusual. So: no page templates for the four modes, no linter, no
classifier, no conformance test. Application is entirely human and entirely
unchecked; a repository can claim Diátaxis while mixing all four modes on one
page and nothing will say otherwise. It is also silent on decisions, requirements
and process — it organises explanation of a system that already exists.

**What it costs to adopt.** Nothing to install; the cost is editorial — usually
restructuring existing documentation, which is substantial.

**Who it appears to be for.** Documentation authors and maintainers of
open-source projects and products.

---

### 30. Doorstop (`doorstop-dev/doorstop`)

**Evidence opened:** `reqs/REQ008.yml`, `doorstop/core/item.py` (the `cleared`
and `reviewed` properties), `doorstop/core/types.py` (`class Stamp`),
`doorstop/core/` listing. HEAD `1f57563`, 2026-09-05.

**What it does.** Requirements management in version control. Each requirement is
a YAML file; documents form a tree; items link to parent items; the tool
validates the tree and publishes it.

**What it does well.** It is the only system in this survey that solves
*review invalidation cryptographically*. An item carries a content hash:

```yaml
# reqs/REQ008.yml
active: true
level: 3.2
links: []
normative: true
reviewed: Y9QwGNJVzJSHbW9sHzBqswqAtF5v8OJup8HEH7E2qHU=
text: |
  Doorstop **shall** provide a way to view document items interactively.
```

`Stamp` is documented as "Hashed content for change tracking", and the `reviewed`
property recomputes `self.stamp(links=True)` and compares — so editing the text
*or its links* silently un-reviews the item. The companion property is `cleared`:

```python
@property
def cleared(self):
    """Indicate if no links are suspect."""
    for uid, item in self._get_parent_uid_and_item():
        if uid.stamp != item.stamp():
            return False
    return True
```
A link stores the stamp of the parent *as it was when the link was made*; if the
parent later changes, the link becomes **suspect** and validation flags it. This
is change propagation across a requirements graph, in plain files, in git — the
mechanism that makes "the document is the source of truth" survive editing. It
also supports `Y`/`True` as a "manually-confirmed matching hash, to be replaced
later", so a human can bless a change without hand-computing a digest.

**Where it stops.** At text against text. A stamp proves an item has not changed
since review; it cannot prove the item is *true of the code*. Traceability runs
requirement → requirement (and, via `ref:` and `reference_finder.py`, to a named
source location), but nothing verifies the referenced code implements the
requirement. The format is also demanding — one YAML file per requirement, an
item tree with `.doorstop.yml` configuration per document — and the surrounding
tooling (`gui/`, `server/`, `views/`) reflects a heavier, pre-web-app era.

**What it costs to adopt.** A Python tool plus a genuine requirements practice:
levels, UIDs, link discipline and review passes. This is the highest process cost
in Shape 6.

**Who it appears to be for.** Teams with traceability obligations — safety,
medical, aerospace, regulated embedded — who want requirements in git rather than
in a proprietary ALM tool.

---

### 31. Sphinx-Needs (`useblocks/sphinx-needs`)

**Evidence opened:**
`packages/sphinx-needs/src/sphinx_needs/config.py` (the `types` default and the
`constraints` field), `packages/sphinx-needs/docs/directives/need.rst`, the
`packages/` listing. HEAD `4a54ea2`, 2026-09-08.

**What it does.** Turns Sphinx documentation into a typed, linked object database.
Directives declare objects with IDs and options:

```rst
.. req:: User needs to login
   :id: ID123
   :status: open
   :tags: user;login
```
Default types are `req` (Requirement, prefix `R_`), `spec` (`S_`), `impl` (`I_`),
`test`, each with a colour and diagram style.

**What it does well.** It makes prose *queryable and constrainable* inside the
normal documentation build. IDs are validated against a configurable pattern
(`id_regex`), and `constraints` is a mapping of "constraint name, to check name,
to filter string" with per-constraint `severity` and a Jinja2-templated
`error_message`, plus `constraint_failed_options` deciding what happens when one
fails — so a team can assert, for example, that every requirement has a linked
test, and choose whether that breaks the build. Around it sit generated views
(`needflow`, `needgantt`, `needbar`, `needtable`, `needextract`, `needimport`,
`needextend`) and `needarch` for PlantUML embedded in the object itself. The
monorepo also contains `sphinx-codelinks`, whose
`sphinx_extension/directives/src_trace.py` and `source_discover/` trace needs to
*source code* — the one mechanism in this shape that reaches past documents into
the codebase.

**Where it stops.** It is inseparable from Sphinx. Everything — validation,
constraints, queries — happens during a documentation build, so the feedback loop
is a build, not a commit hook or a quick command, and the authoring format is
reStructuredText directives. Its constraint language is a filter over need
attributes: it can assert a link exists, not that the linked test is meaningful.
It is also large (1,761 tracked files across several packages), which is a real
onboarding cost.

**What it costs to adopt.** A Sphinx documentation stack, a `conf.py` with a
declared type system, optional PlantUML, and RST authoring. Highest tooling cost
in this shape.

**Who it appears to be for.** Engineering organisations — heavily automotive and
embedded — needing requirements, specifications and tests linked and reportable
from documentation they already build.

**Notable for this survey:** it is the only Shape 6 project in the corpus that has
adopted the Shape 2 conventions, shipping `AGENTS.md`, `CLAUDE.md` and a
`.claude/` directory at its root.

---

### 32. Gherkin / Cucumber (`cucumber/gherkin`)

**Evidence opened:** `gherkin.berp`, `gherkin-languages.json`,
`testdata/good/background.feature`, `testdata/` counts. HEAD `f5aa947`,
2026-09-11.

**What it does.** Defines the `.feature` language — `Feature`, `Rule`,
`Background`, `Scenario`, `Examples`, steps, data tables, doc strings — and
supplies parsers for it in many host languages.

**What it does well.** It is the most rigorously formalised specification format
in this entire survey, in three distinct ways. First, a real grammar file:

```
GherkinDocument! := Feature?
Feature!         := FeatureHeader Background? ScenarioDefinition* Rule*
Scenario!        := #ScenarioLine DescriptionHelper Step* ExamplesDefinition*
Step!            := #StepLine StepArg?
```
with documented lookahead hints for genuinely ambiguous cases — "Interpreting a
tag line is ambiguous (tag line of rule or of scenario)" — i.e. the ambiguities
were found and resolved explicitly rather than left to implementations. Second,
conformance is testable and adversarial:

```
ls testdata/good/*.feature | wc -l   # -> 50
ls testdata/bad/*.feature  | wc -l   # -> 12
```
Shipping *invalid* fixtures (e.g. `backslash_at_end_of_line_in_datatable.feature`)
means parsers are held to rejecting the right things, not only accepting them.
Third, it is localised at the keyword level — `gherkin-languages.json` carries
80 language entries (`python3 -c "import json;d=json.load(open('gherkin-languages.json'));print(len(d))"`),
and that same file is vendored into the JavaScript, PHP, Python and Ruby
implementations so they cannot drift. **Wrong if:** the JSON contains non-language
metadata keys at top level; sampled keys are language codes. The payoff of all
this is the original claim: the specification *is* the test, executed on every
build.

**Where it stops.** At the sentence boundary. The grammar guarantees a step line
parses; it says nothing about what `Given the minimalism` means. The mapping from
step text to behaviour — step definitions — is ordinary code in your project,
unversioned against the feature file and unvalidated by anything here; a
perfectly valid `.feature` may bind to step definitions that assert nothing. The
format also covers behaviour only: there is no place in it for a decision, a
constraint, an architecture, or a rationale.

**What it costs to adopt.** A parser plus a test runner for your language, and
the sustained cost of maintaining step definitions — historically the reason
teams abandon it.

**Who it appears to be for.** Teams practising BDD/specification-by-example who
want acceptance criteria executable and readable by non-programmers.

---

### 33. The Rust RFC process (`rust-lang/rfcs`)

**Evidence opened:** `0000-template.md`, `README.md` section headings,
`text/` count. HEAD `51783df`, 2026-09-10.

**What it does.** A pull-request-based process for substantial changes: write an
RFC from a template, discuss in the PR, a team moves to Final Comment Period,
accepted RFCs merge into `text/` and become the durable record.

```
ls text/*.md | wc -l    # -> 642
```
**Wrong if:** `text/` contains non-RFC files; the glob matched only numbered RFC
documents in the sampled listing.

**What it does well.** The template is the most psychologically well-designed
artifact in this survey — it forces the arguments people avoid. It mandates
`Drawbacks` ("Why should we *not* do this?"), `Rationale and alternatives` ("Why
is this design the best in the space of possible designs? … What is the impact of
not doing this?"), `Prior art`, and `Unresolved questions`, which it splits by
*when* each will be resolved: "What parts … do you expect to resolve through the
RFC process before this gets merged? What parts … through the implementation …
before stabilization? What related issues … out of scope?" It also separates
`Guide-level explanation` (teach it as if it already shipped, with examples and
error messages) from `Reference-level explanation` (corner cases, interactions),
which forces a proposal to be defensible at two altitudes. `Future possibilities`
is explicitly fenced against misuse: "having something written down in the
future-possibilities section is not a reason to accept the current or a future
RFC". The README carries the whole lifecycle including `RFC Postponement` — a
defined state for "not now", which most processes lack — and a section literally
headed "Help this is all too informal!".

**Where it stops.** At human social process, with zero tooling in the repository.
There is no CLI, no linter, no status field, no schema — the template is a
markdown file with a numbered filename and the process lives in GitHub PRs and
in team members' judgement. It also scales by *gatekeeping*: it works because
named teams with authority run FCP, which is not transplantable to a project that
lacks them. And the record is decisions-about-the-language; an accepted RFC is
not kept in sync with the implementation that follows it (hence the separate
tracking issue field in the template header).

**What it costs to adopt.** Nothing technical; everything organisational. It
requires people with standing to accept and reject, and the patience for long
threads.

**Who it appears to be for.** Open-source projects and organisations making
consequential, contested, long-lived decisions in public.

---
## Coverage of the six shapes

All six shapes returned entries. None was silently omitted.

| # | Shape | Entries | Nos. |
|---|---|---|---|
| 1 | Spec-driven / plan-driven kits | 6 | 1–6 |
| 2 | Agent instruction file conventions + their tooling | 6 | 7–12 |
| 3 | Subagent / role / multi-agent orchestration | 5 | 13–17 |
| 4 | Prompt and workflow libraries shipped as repositories | 4 | 18–21 |
| 5 | Research and evaluation harnesses | 4 | 22–25 |
| 6 | Documentation-as-source-of-truth predating coding agents | 8 | 26–33 |

33 entries drawn from 32 cloned repositories (entries 19 and 25 both draw on
`anthropics/skills`; entries 17 and 25 both draw on `microsoft/autogen`).

### Absences recorded, with what was searched

Two sub-shapes came back empty. Both were searched with varied wording, varied
tooling, and varied term sets before being called.

**(a) No schema, grammar, or validator published with the AGENTS.md standard.**
Searched by `git ls-files | grep -iE 'schema|spec|lint|valid|rfc|grammar'` over
`openai/agents.md` (empty), by full visual read of its 62-file listing, and by two
differently-worded web searches. Third-party linters exist and two were cloned
and opened (entries 11, 12); none is published by the standard. See the Shape 2
absence note for the full record.

**(b) Within the corpus opened, nothing evaluates a project's own agent-facing
scaffolding against that project.** Every harness examined (entries 22–25)
evaluates a model on authored tasks, a prompt on authored cases, or a patch
against a fixed benchmark. Candidate repositories surfaced by search were not
cloned and are explicitly *not* claimed as absence — see the Shape 5 absence note.

### Where searching stopped short — declared, not disguised

The following were surfaced by web search, confirmed to exist via
`curl -s -o /dev/null -w "%{http_code}" https://api.github.com/repos/<owner>/<repo>`
returning 200, and then **not opened**. They are excluded under the evidence rule
and nothing is claimed about them. They are the most likely gaps in this survey:

- `carlrannaberg/cclint`, `swarmclawai/agent-skills-lint`, `agentsmd/agents.md`
  (Shape 2 tooling)
- `MarcKarbowiak/ai-evaluation-harness`, `forrestbthomas/pi-harness`,
  `ProofAgent-ai/proofagent-harness`, `linny006/agent-eval-harness` (Shape 5)
- `NeoLabHQ/context-engineering-kit`,
  `muratcankoylan/Agent-Skills-for-Context-Engineering` (Shapes 1/4)

Named by search results but never located as an inspectable repository, and
therefore absent from this survey entirely: **AWS Kiro** and **Tessl** (both
appear to be products rather than open repositories — NOT ESTABLISHED), and the
successor governance repository for GSD.

---

## Cross-cutting observations

Each of these is a measurement over the corpus, not a judgement.

**1. Adoption of the agent instruction conventions, inside this corpus.**

```
for d in <the 27 first-round repos>; do
  git -C $d ls-files | grep -cx 'AGENTS.md'
  git -C $d ls-files | grep -cx 'CLAUDE.md'
done
```
Result: 10 of 27 carry a root `AGENTS.md`; 7 of 27 carry `CLAUDE.md`.
**Wrong if:** the file exists but is untracked, lives in a subdirectory, or the
repo uses `GEMINI.md`/`.cursor/rules` instead — `superpowers` (cloned later, not
in this 27) carries all three of AGENTS.md, CLAUDE.md and GEMINI.md, so the
figure understates convention use generally. Of the six pre-agent documentation
systems (entries 26–31), only `sphinx-needs` carries either file.

**2. Two different things are called "validation".** Entries split cleanly into
those where a parser or hash decides (OpenSpec's `constants.ts`, Doorstop's
`Stamp`, Gherkin's `testdata/bad/`, Sphinx-Needs' `constraints`, agents-lint's
`checkFilesystem`, SWE-bench's `FAIL_TO_PASS`) and those where a model is asked
to look (Spec Kit's `analyze`, the validator subagents in
`claude-code-spec-workflow`, promptfoo's `llm-rubric`). Both appear under the
same word throughout the ecosystem's own documentation.

**3. Enforcement is nearly always advisory.** The only harness-level enforcement
found in Shapes 1–4 is GSD's hook set, and its own source says the workflow guard
is a soft guard that advises rather than blocks and is off by default. Spec Kit
explicitly declines to evaluate hook conditions. Everything else relies on the
model following instructions.

**4. Two projects document a retreat from a design in source.** Spec Kit's empty
`FORK_CONTEXT_COMMANDS` (with issue #3185 cited) and VoltAgent's
"no runtime message bus in this repo" constraints. Both are, in effect, negative
results published in code.

**5. The pre-agent systems solved problems the agent-era kits have not
re-solved.** Supersession with bidirectional links (adr-tools), review
invalidation by content hash and suspect-link propagation (Doorstop), typed
objects with build-failing constraints (Sphinx-Needs), executable acceptance
criteria with a published grammar and negative conformance fixtures (Gherkin), a
defined "not now" state (Rust RFC postponement). None of the Shape 1–4 entries
implements any of these mechanisms.

**6. Staleness varies by an order of magnitude.** Within this corpus, HEAD dates
range from 2020-03-30 (`adr-tools`) to 2026-09-11 (five repositories). Among
agent-era entries the oldest is `claude-code-spec-workflow` at 2025-09-07.
**Wrong if:** work moved to a non-default branch, which `--single-branch` would
hide.

---

## Decisions encountered and NOT authored

Per the phase boundary, these are surfaced, not resolved. Each is a real fork
this survey ran into; what changes on each answer is stated so the decision can
be taken later with the consequence visible.

1. **One host harness or many.** Spec Kit maintains 41 integration directories
   and OpenSpec 31 adapters; GSD and superpowers target a primary harness and
   port outward. *Changes:* whether enforcement may use harness features (hooks,
   plan mode, subagents) at all — portable kits cannot, and are therefore
   advisory by construction.
2. **Parser-checked artifacts or model-reviewed artifacts.** *Changes:* whether
   the kit needs a runtime and a schema, who can author artifacts without
   tripping validation, and whether "valid" means anything when the reviewer is
   the same class of system being reviewed.
3. **Whether stale artifacts are detected mechanically.** Doorstop's stamp and
   agents-lint's path checking are the two mechanisms observed. *Changes:*
   whether artifacts need identifiers and hashes — which forces a file format —
   or stay free prose.
4. **Whether the unit of work is feature-shaped.** Every Shape 1 kit assumes it;
   only `claude-code-spec-workflow` ships a separate bug track. *Changes:* how
   much ceremony a one-line fix incurs, and whether the kit gets bypassed for
   small work (and therefore for most work).
5. **Whether roles/personas are part of the model.** BMAD and the two agent
   catalogues say yes; Spec Kit and OpenSpec say no. *Changes:* the entire
   customisation surface — BMAD needed three-layer TOML merge semantics to
   support it.
6. **Whether the kit evaluates itself.** Only `anthropics/skills` does, and only
   for triggering. *Changes:* whether the project can tell improvement from
   churn, and adds API spend and grader authorship as ongoing costs.

---

## What could not be established

- **Any popularity, adoption or star figure.** Search results quoted several
  (93,000+ for Spec Kit, 52,100 for OpenSpec, 64,559 for GSD). None was verified
  against a primary source and none is relied on anywhere above. NOT ESTABLISHED.
- **Whether GSD's canonical repository has been superseded**, and the
  circumstances alleged around it. Only the HEAD date (2026-05-31) is
  established. NOT ESTABLISHED.
- **Whether `microsoft/autogen` is maintained, branch-moved, or consolidated**
  into a successor. Only the default-branch HEAD date (2026-04-06) is
  established. NOT ESTABLISHED.
- **Whether any of these tools works**, in the sense of improving outcomes. No
  tool in this survey was executed. Every claim above is about files that exist,
  not about behaviour observed. No comparative or effectiveness claim is made.
- **Whether `awesome-claude-code`'s `Last Checked` / `Stale` columns are
  maintained.** The schema supports lifecycle tracking; whether it is exercised
  was not checked. NOT ESTABLISHED.
- **True skill counts for `wshobson/agents`** (425 is a file count under
  `skills/`, not a skill count) and **true assertion-type count for promptfoo**
  (57 is a file count including infrastructure). Both are upper bounds.
- **Coverage completeness.** This corpus was assembled from prior knowledge plus
  four web searches. The unexplored-leads list above names eleven repositories
  confirmed to exist and never opened. This survey is a floor, not a census.

---

## Appendix — corpus

32 repositories, with the HEAD inspected. All shallow single-branch clones taken
2026-09-11.

| Repository | HEAD | Date | Shape |
|---|---|---|---|
| `github/spec-kit` | c173bf1 | 2026-09-10 | 1 |
| `Fission-AI/OpenSpec` | 9d4e597 | 2026-09-09 | 1 |
| `bmad-code-org/BMAD-METHOD` | abe4eb1 | 2026-09-05 | 1 |
| `gsd-build/get-shit-done` | bdcaab2 | 2026-05-31 | 1 |
| `buildermethods/agent-os` | 475b0ca | 2026-08-29 | 1 |
| `pimzino/claude-code-spec-workflow` | f3de74d | 2025-09-07 | 1 |
| `openai/agents.md` | d001185 | 2026-09-10 | 2 |
| `AnswerDotAI/llms-txt` | f5aed2a | 2026-09-04 | 2 |
| `PatrickJS/awesome-cursorrules` | b044f95 | 2026-05-31 | 2 |
| `steipete/agent-rules` | 42993e4 | 2026-04-27 | 2 |
| `agent-sh/agnix` | e557022 | 2026-09-07 | 2 |
| `giacomo/agents-lint` | 203f33e | 2026-03-26 | 2 |
| `wshobson/agents` | a30778f | 2026-09-01 | 3 |
| `VoltAgent/awesome-claude-code-subagents` | 3097abe | 2026-09-07 | 3 |
| `ruvnet/claude-flow` | 005a0ed | 2026-09-11 | 3 |
| `crewAIInc/crewAI` | c5759ce | 2026-09-11 | 3 |
| `microsoft/autogen` | 027ecf0 | 2026-04-06 | 3, 5 |
| `danielmiessler/fabric` | b682dad | 2026-09-07 | 4 |
| `anthropics/skills` | 34040c9 | 2026-09-10 | 4, 5 |
| `obra/superpowers` | b36e082 | 2026-08-12 | 4 |
| `hesreallyhim/awesome-claude-code` | 63c84a1 | 2026-09-11 | 4 |
| `UKGovernmentBEIS/inspect_ai` | 03befb4 | 2026-09-11 | 5 |
| `promptfoo/promptfoo` | c2b1a2f | 2026-09-11 | 5 |
| `SWE-bench/SWE-bench` | 02e7a74 | 2026-09-02 | 5 |
| `npryce/adr-tools` | b3279ba | 2020-03-30 | 6 |
| `adr/madr` | ba75bb1 | 2026-08-28 | 6 |
| `arc42/arc42-template` | 8dff0d9 | 2026-07-07 | 6 |
| `evildmp/diataxis-documentation-framework` | 957c09c | 2026-08-06 | 6 |
| `doorstop-dev/doorstop` | 1f57563 | 2026-09-05 | 6 |
| `useblocks/sphinx-needs` | 4a54ea2 | 2026-09-08 | 6 |
| `cucumber/gherkin` | f5aa947 | 2026-09-11 | 6 |
| `rust-lang/rfcs` | 51783df | 2026-09-10 | 6 |

**Method boundary honoured:** this survey was written without reference to, and
in deliberate ignorance of, the method the kit will be based on. No comparison to
any method appears above.
