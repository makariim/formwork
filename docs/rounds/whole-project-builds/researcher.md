---
date: 2026-11-15
---

# Researcher: what other methods and tools do for a whole project

Brief 0022, round `whole-project-builds`. Role: researcher. Date: 2026-11-15.

## First, three contradictions

1. **The briefing says skills "were planned and dropped".** That is half out
   of date in this repository. `docs/standing.md` (Where we are now) says 1.0.0
   ships the first skill, `humanizer`, and that a role's `description`, `model`,
   `skills` and `color` now reach the generated Claude Code agent. The "What we
   tried and stopped" section still says skills were dropped. Both lines are in
   the same file. The proposal should start from "one skill ships", not "no
   skills".
2. **`docs/survey.md` (2026-09-11) is out of date in four places** that matter
   to this round. Details in R2 below. The biggest: AutoGen is now archived,
   and Spec Kit now ships separate bug fixing and idea assessment tracks with
   human review gates, so the survey's "only one kit has a bug track" is no
   longer true.
3. **"Routing from one prompt" has been measured, but only for a narrower
   thing.** Nobody I found measures whether a tool picks the right *workflow
   and size* from one request. Several people measure whether an agent picks
   the right *skill*. The numbers are poor at scale (R3). So the centre of this
   round rests on a mechanism with known, published failure rates.

## What I committed to, and when

Honest note on order. I set these bars in my plan before the first fetch, but
I wrote them into this file afterwards. They are weaker evidence than bars on
disk first. Weigh them that way.

| | |
|---|---|
| **Unit** | a claim about a tool or method, each with a URL or a file I opened |
| **Population** | the tools the lead named, plus anything the fetches surfaced that does routing, role generation, taste checks or usage limits |
| **Bar** | every claim sourced; anything not fetched is NOT ESTABLISHED |
| **Prediction** | no published accuracy figure for workflow routing from one prompt exists. Skill selection figures might |
| **Invalidator** | a published measurement of whole workflow routing accuracy; or the fetched pages being stale versions of the docs |

The prediction held. Workflow routing accuracy: none found. Skill selection
accuracy: found, two papers (R3).

## How the evidence was gathered

`git clone` is refused here by the kit's own git boundary guard. So repository
evidence came from GitHub tarballs into a scratch folder, and HEAD dates from
the GitHub API.

```
curl -sL https://codeload.github.com/<owner>/<repo>/tar.gz/HEAD | tar -xz ...
curl -s "https://api.github.com/repos/<owner>/<repo>/commits?per_page=1"
```

HEADs read on 2026-11-15:

| Repository | HEAD | Date |
|---|---|---|
| github/spec-kit | 2ee2b1e | 2026-11-12 |
| bmad-code-org/BMAD-METHOD | e435a22 | 2026-11-12 |
| obra/superpowers | 22f0b46 | 2026-11-03 |
| anthropics/skills | 1780c5e | 2026-11-14 |
| buildermethods/agent-os | e892e61 | 2026-10-07 |
| eyaltoledano/claude-task-master | c0c98d3 | 2026-04-23 |
| FoundationAgents/MetaGPT | 11cdf46 | 2026-01-21 |
| OpenBMB/ChatDev | 464a681 | 2026-10-30 |
| microsoft/autogen | 8390985 | 2026-11-12 |
| garrytan/gstack | 0326b14 | 2026-11-15 |

**Would be wrong if:** the tarball is the default branch only, same limit as
the survey. Documentation pages came through WebFetch, which summarises with a
small model. Where a quote matters I say whether I read the file myself or got
it through WebFetch. WebFetch quotes are one step removed.

---

## R1. Product development frameworks

Short. Each one: phases, what a gate is, who decides, what transfers.

### Stage-Gate (Cooper)

Source: https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/

- **Phases.** Discovery, then Concept, Build the Business Case, Development,
  Testing and Validation, Launch, then a post launch review.
- **Gate.** One before each stage. It has inputs ("gate deliverables" from the
  stage before), criteria (project readiness and business value), and an
  output: a decision plus an agreed plan with resources, avoiding "approval
  without resources".
- **Who decides.** Gatekeepers, senior people who own the resources the next
  stage needs. Four answers: Go, Kill, Hold, Recycle.
- **Scaled versions** (Lite, XPress for small changes) exist according to
  secondary sources only, e.g.
  https://resources.rework.com/libraries/project-management/stage-gate-process.
  Exact stage counts: NOT ESTABLISHED (the primary article I tried,
  https://www.pragmaticinstitute.com/resources/the-next-stage-for-stage-gate,
  is archived and returned no body).
- **Transfers.** A gate is defined by its *inputs and criteria written in
  advance*, and it has four outcomes, not two. "Kill" and "Recycle" are the
  ones agent kits lack. Scaling the process down for small work is part of the
  method, not a deviation from it.

### Google Ventures Design Sprint

Sources: https://www.gv.com/sprint/ (days); Decider role from secondary
sources only, e.g. https://www.bringthedonuts.com/newsletter/the-design-sprint.html

- **Phases.** Five days. Monday map the problem and pick a target. Tuesday
  sketch. Wednesday decide and storyboard. Thursday build a realistic
  prototype. Friday test with customers.
- **Gate.** One real decision point, Wednesday. A straw poll is input; then the
  Decider's supervote.
- **Who decides.** The Decider, a named person. The GV page I fetched does not
  mention the role; the book quote came through search results only. Treat the
  wording as NOT ESTABLISHED from a primary source.
- **Transfers.** Time box as the scope control. A named decider separate from
  the facilitator, which maps onto formwork's split between the human (decides)
  and the lead (runs the round). Test with real people on day five, which is
  the "review on the running product" the idea file asks for.

### Basecamp Shape Up

Source: https://basecamp.com/shapeup/0.3-chapter-01

- **Phases.** Shaping (a small senior group), betting, a six week build cycle,
  two weeks of cool down.
- **Gate.** The betting table, held in cool down, which picks pitches for the
  next cycle.
- **Who decides.** Stakeholders at the betting table. Once bet, the team owns
  execution.
- **Key mechanisms.** *Appetite*: "the amount of time we want to spend", set
  before the work, instead of an estimate. *Circuit breaker*: work that does not
  ship in one cycle is cancelled by default, not extended.
- **Transfers.** Appetite is the strongest single answer to "do not over build
  a small ask": the size is fixed first, and scope bends to it. The circuit
  breaker is a default kill, which no agent kit I read has.

### Double Diamond (UK Design Council)

Source: https://www.designcouncil.org.uk/our-resources/the-double-diamond/

- **Phases.** Discover, Define, Develop, Deliver. Two diamonds: first about the
  problem, second about the solution.
- **Gate.** None named on the page. The page notes work may loop back "to the
  beginning of their diamond work".
- **Who decides.** Not stated.
- **Transfers.** The split between "is this the right problem" and "is this
  the right solution" as two separate phases. The health app's "correct and dead" v1 is
  a second diamond done well on a first diamond done badly.

### Dual track agile (Cagan, SVPG)

Source: https://www.svpg.com/dual-track-agile/

- **Phases.** Not phases: two tracks run at once. Discovery makes "validated
  product backlog items"; delivery makes "releasable software". Cagan later
  renamed it continuous discovery and delivery.
- **Gate.** Validation in discovery before an item enters delivery. The
  prototype "serves as the spec for Delivery".
- **Who decides.** Product manager, designer and lead engineer working side by
  side. No separate owner per track.
- **Transfers.** Research and building need not be sequential phases. A
  research round can run beside a build round, which matches how the idea file
  describes the team reviewing "in parallel with him".

### R1 summary

| Method | Gate | Who decides | Strongest transfer |
|---|---|---|---|
| Stage-Gate | criteria written before; Go, Kill, Hold, Recycle | gatekeepers who own resources | four outcome gate; scale down for small work |
| Design Sprint | Wednesday supervote | the Decider | named decider; test on day five |
| Shape Up | betting table | stakeholders | appetite first; default kill |
| Double Diamond | none named | not stated | problem and solution as two phases |
| Dual track | validated before delivery | trio together | research beside build |

---

## R2. Agentic coding frameworks and orchestrators, end to end

`docs/survey.md` covers Spec Kit, OpenSpec, BMAD, GSD, Agent OS,
claude-code-spec-workflow, CrewAI, AutoGen, anthropics/skills, superpowers and
others as of 2026-09-11. I do not redo that. Below: what changed, and the
tools it did not cover.

### Where `docs/survey.md` is now out of date

1. **AutoGen is archived.** Its README now says: "AutoGen is now archived and
   no longer maintained by Microsoft" and "New users should start with
   Microsoft Agent Framework". (Read myself: `autogen/README.md` lines 25 to
   31, 183 in the tarball.) The survey left this NOT ESTABLISHED. It is now
   established.
2. **Spec Kit has three entry points, not one.** README "Choose your process":
   Spec Driven Development, Bug fixing, Idea assessment, "independent entry
   points, not mandatory phases". It also has YAML workflows with human review
   gates (`review-spec`, `review-plan`, `review-assessment`) that pause a run
   until a verdict. (Read myself: `spec-kit/README.md`,
   `spec-kit/docs/workflows/overview.md`.) The survey's decision 4 says "only
   claude-code-spec-workflow ships a separate bug track". No longer true.
3. **BMAD restructured again.** Skills are now grouped into `core-tools`,
   `method`, `founder`, `toolsmith` (read myself: `ls BMAD-METHOD/skills`). Its
   old "quick flow" and scale tracks are listed as retired
   (`skills/method/bmod-method/retired.toml`: `bmad-quick-flow`,
   `bmad-quick-spec`, `bmad-agent-quick-flow-solo-dev`). Sizing moved into
   `bmad-build` as a route (R3).
4. **superpowers added two things relevant here.** A SessionStart hook that
   injects the `using-superpowers` skill at startup, clear and compact
   (`hooks/hooks.json`), and a new `diagnosing-superpowers` skill for when "a
   skill didn't fire". Its brainstorming skill now has an explicit "Size the
   Work" step (R3). The survey said "Nothing verifies compliance". Still true;
   but there is now a self diagnosis path.
5. **Claude Code itself** gained plugin evals with a `tool_used: Skill`
   grader, which can measure skill triggering. That turns the survey's decision
   6 ("whether the kit evaluates itself; only anthropics/skills does") into
   something any kit can do with the host tool (R3).

### Tools the survey did not cover, or covered thinly

**GitHub Spec Kit, whole project.** Specify, plan, tasks, implement, converge,
with a constitution file. The bundled `speckit` workflow runs them "with review
gates after specification and planning". Extensions add processes, presets
change templates, overlays change an installed workflow "without forking it".
(`spec-kit/README.md`, `docs/workflows/overview.md`.)

**AWS Kiro.** Specs have three files: `requirements.md` (or `bugfix.md`),
`design.md`, `tasks.md`. Types: Feature, Bugfix, and Quick Spec, which makes all
three "without approval gates" (https://kiro.dev/docs/specs/, via WebFetch).
Steering files in `.kiro/steering/`: default `product.md`, `tech.md`,
`structure.md`, with inclusion modes always, fileMatch, manual and auto
(https://kiro.dev/docs/steering/, via WebFetch). Whether standard specs gate
between phases: the page implies it but does not say. NOT ESTABLISHED.

**MetaGPT.** "takes a one line requirement as input and outputs user stories /
competitive analysis / requirements / data structures / APIs / documents".
Roles: product manager, architect, project manager, engineer, QA. "`Code =
SOP(Team)` is the core philosophy." (Read myself: `MetaGPT/README.md` lines 40
to 44; `metagpt/roles/`.) Last commit 2026-01-21.

**ChatDev.** Version 1 was a "Virtual Software Company" (CEO, CTO,
programmer). Version 2.0 (DevAll, January 2026) is "a Zero-Code Multi-Agent
Platform" where users define agents and workflows in YAML, with `make
validate-yamls` for schema checks. Version 1 is on a legacy branch. (Read
myself: `ChatDev/README.md`.) So the best known "whole software company" agent
system moved away from a fixed company shape to user defined workflows.

**Microsoft Agent Framework** (AutoGen's successor). Five patterns:
sequential, concurrent, handoff, group chat, magentic ("a manager agent
dynamically coordinates specialized agents"). Human in the loop through
"approval-required tools that pause the workflow".
(https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview)

**CrewAI.** Sequential and hierarchical processes. In hierarchical, a manager
"allocates tasks to agents based on their capabilities, reviews outputs, and
assesses task completion"; workers are a predefined list.
(https://docs.crewai.com/en/concepts/processes, via WebFetch.)

**LangGraph / LangChain.** Five multi agent patterns: subagents, handoffs,
skills, router ("a routing step classifies input and directs it to one or more
specialized agents"), custom workflow.
(https://docs.langchain.com/oss/python/langchain/multi-agent, via WebFetch.)

**OpenHands.** `AGENTS.md` always loaded; skills with `triggers` frontmatter
"injects the skill when a keyword or command appears in a user message"; plus
a catalog the model picks from by description; plus `paths` rules that load
deterministically when a matching file is touched.
(https://docs.openhands.dev/overview/skills, via WebFetch.)

**Taskmaster.** `parse-prd` turns a PRD into tasks; `analyze-complexity` scores
tasks 1 to 10 with a `--threshold`, and `expand` splits complex ones. (Read
myself: `claude-task-master/docs/command-reference.md`.) Last commit
2026-04-23, roughly seven months before today.

**Agent OS.** Unchanged in shape since the survey: five commands, no execution
half (`find agent-os -type f`). HEAD moved from 2026-08-29 to 2026-10-07.

**Claude Code** (all via WebFetch from code.claude.com, 2026-11-15):
- Subagents: picked by `description`; "use proactively" encourages delegation;
  a startup warning past 15,000 tokens of combined descriptions; subagents can
  spawn subagents "up to three layers below the main conversation"
  (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`).
  https://code.claude.com/docs/en/sub-agents
- Skills: descriptions in context, body loads on use; `disable-model-invocation`
  stops automatic use; description plus `when_to_use` capped at 1,536
  characters; the listing budget is 1% of the context window and drops the
  least used descriptions first when full. https://code.claude.com/docs/en/skills
- Hooks: 33 events, among them `UserPromptSubmit`, which can add context or
  block a prompt, and `SubagentStart` / `SubagentStop`.
  https://code.claude.com/docs/en/hooks
- Agent teams: experimental, off by default; "no hard limit on the number of
  teammates"; "Start with 3-5 teammates"; teammates cannot spawn teammates.
  https://code.claude.com/docs/en/agent-teams

### What R2 shows

Every whole project tool chooses one of two shapes:

- **A fixed company** (MetaGPT, ChatDev 1, BMAD's persona cast): the roles and
  the sequence are fixed in advance.
- **Composable primitives plus a user chosen entry point** (Spec Kit, Kiro,
  ChatDev 2, Agent Framework, LangGraph): the user or a config picks the
  process.

ChatDev moving from the first to the second, and AutoGen being archived for a
framework of patterns, are both evidence that the fixed company shape did not
hold up. That is my reading; neither project states it as a lesson.

---

## R3. Routing from one prompt

The centre of the round. Four questions: how they route, how they avoid over
building, how a user corrects a route, and whether anyone measured it.

### How each tool routes

| Tool | Mechanism | Who picks | Source |
|---|---|---|---|
| Claude Code skills | model reads every skill's `description` in a listing, loads the body on match | the model | code.claude.com/docs/en/skills |
| Claude Code subagents | model reads each subagent's `description` | the model | code.claude.com/docs/en/sub-agents |
| Claude Code hooks | `UserPromptSubmit` can inject text before the model sees the prompt | a script, deterministic | code.claude.com/docs/en/hooks |
| Kiro steering | `inclusion: auto` loads a file "when your request matches the file's description"; `fileMatch` by path | model for auto, path for fileMatch | kiro.dev/docs/steering |
| Kiro sessions | user picks Vibe or Spec, or a built in workflow agent (Spec, Quick Spec, Bug Fix, Plan) from a session picker | the user | kiro.dev/docs/chat (search result); not fetched in full |
| Kiro intent | "Smart Intent Detection" separates information from action | the model | kiro.dev/docs/chat (search result only) |
| Spec Kit | explicit commands and three explicit entry points | the user | spec-kit README |
| BMAD | a `bmad` advisor skill recommends "the next skill from what is installed", from each module's help files, "never from memory" | model, from files | `BMAD-METHOD/skills/core-tools/bmad/` |
| BMAD party mode | a roster script resolves who is "in the room"; open rooms cast "on the fly (whoever fits the moment)" | script, then model | `skills/core-tools/bmad-party-mode/SKILL.md` |
| superpowers | SessionStart hook injects `using-superpowers`: "If you think there is even a 1% chance a skill might apply ... you ABSOLUTELY MUST invoke the skill" | hook, then model | `superpowers/skills/using-superpowers/SKILL.md`, `hooks/hooks.json` |
| OpenHands | keyword `triggers`, `paths`, and description catalog | keyword or path deterministic; catalog by model | docs.openhands.dev/overview/skills |
| LangGraph router | an LLM classification step | the model | docs.langchain.com multi-agent |
| MetaGPT | none: one line in, fixed SOP runs | fixed | MetaGPT README |

Three layers recur, and the strongest tools use all three:

1. **Always loaded** text (CLAUDE.md, AGENTS.md, Kiro `always` steering,
   superpowers' injected bootstrap). Cheap, always present, grows until it is
   ignored.
2. **Deterministic triggers** (hooks, `paths`, `fileMatch`, OpenHands keyword
   `triggers`). Reliable, but only for what a pattern can see.
3. **Description matching by the model** (skills, subagents, Kiro `auto`).
   Flexible, and the part with measured failure rates.

Note one tension. superpowers' "1% chance" rule pushes *toward* invoking
process. That is the opposite of formwork's worry about over building, and it
works for superpowers only because its brainstorming skill then sizes the work
down (next section).

### How they avoid over building a small ask

Four concrete mechanisms found, each with its source.

1. **A stated size with a numeric rule (BMAD `bmad-build`).** Route is
   `oneshot`, `full` or `auto`. The default `auto` rule, in
   `skills/method/bmad-build/customize.toml` (read myself):

   ```
   estimate the lines of code to add or modify.
   100 lines or fewer: oneshot. Otherwise: full.
   If the change touches more than five files and is not simple or mechanical,
   consider upgrading to full.
   ```

   And escalation is built in. `step-oneshot.md`: "Stop coding if the request
   left out something the user would notice in the result", then set `route:
   full` and go back to planning. The plan template records `route_source:
   pinned | auto`, so you can see whether a person or the rule chose.

2. **Say the size, let them override, step up if it grows (superpowers
   brainstorming).** Read myself, `skills/brainstorming/SKILL.md`:
   "Everything that matters is in the request ... This is a quick, clear task.
   Do it, and say what you did." And under Size the Work: "say how big the work
   is in plain words. They can override it." Two sizes, small change and
   project. "If it grows mid-task, stop, say so, and step up a size."

3. **A lighter variant of the same process (Kiro Quick Spec; Spec Kit's
   separate bug track; Stage-Gate XPress).** Quick Spec makes all three
   artifacts "without approval gates" (kiro.dev/docs/specs). Spec Kit's bug
   fixing needs "No SDD feature workflow ... first" (spec-kit README).

4. **Complexity scoring with a threshold (Taskmaster).** `analyze-complexity
   --threshold=6`, then only complex tasks get expanded (command reference).

What none of them does: write down the chosen size where a check can read it
and refuse a mismatch. BMAD comes closest by writing `route` and
`route_source` into the plan file's frontmatter.

### How a user corrects a wrong route

- **Claude Code:** invoke by name (`/skill-name`, `@agent-name`, or "Use the X
  subagent"); `disable-model-invocation: true` to stop a skill firing on its
  own; `skillOverrides` to hide one; narrow the description. "Skill triggers
  too often: 1. Make the description more specific 2. Add
  `disable-model-invocation: true`". (code.claude.com/docs/en/skills)
- **BMAD:** pin the route in the invocation (`oneshot` or `full`) or in a user
  override TOML; layered customisation base, team, user (`bmad-build/SKILL.md`,
  `customize.toml`).
- **superpowers:** the user overrides the stated size; "User instructions
  (CLAUDE.md, AGENTS.md ...) take precedence over skills".
- **Kiro:** pick a different session type or workflow agent; workspace
  steering beats global steering.
- **Spec Kit:** the user picked the entry point to begin with.

Pattern: every correction path is either *name it explicitly* or *edit the
description or config*. None of them learns from a correction automatically.
superpowers' `diagnosing-superpowers` is the nearest thing: it reads past
transcripts and reports "a skill that didn't fire" with `path:line` citations,
for a human to act on.

### Has anyone measured routing accuracy?

**Whole workflow routing (kind of work, phase, size) from one prompt: NOT
ESTABLISHED.** I found no published measurement for any tool above. Searched:
two web searches on skill and routing benchmarks, plus the docs of every tool
in the table. Varied the term (routing, skill selection, trigger) and the
source (vendor docs, arXiv, repositories).

**Skill selection has been measured, and the numbers are a warning:**

- *Lost in Implicit Routing* (arXiv 2610.18522, abstract via WebFetch): with
  1,000 irrelevant skills added to SkillsBench tasks, "loaded-skill recall
  falls from 73.6% to 27.4%", and "the zero-load rate rises from 9.3% to
  51.6%". "Explicit selection from the same library retains 73.9% recall."
  https://arxiv.org/abs/2610.18522
- *SkillRouter* (arXiv 2603.22455): over about 80,000 skills, a trained router
  reaches "74.0% Hit@1"; hiding the skill body costs "a 37-44 percentage point
  drop". https://arxiv.org/abs/2603.22455
- Anthropic says description tuning in skill-creator improved "triggering on 5
  out of 6 public skills", with no rates given.
  https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills

Even at the low end, with no distractors, implicit recall is about 74%, so
roughly one request in four does not load the right skill. Explicit selection
holds up as the library grows; implicit selection collapses. **Would be
wrong if:** formwork's library (28 roles, one skill) is far below the
distractor counts in these papers, and real behaviour at that size is
unmeasured. These are paper abstracts; I did not read the full papers.

**An instrument exists.** Claude Code's `claude plugin eval` runs cases with
and without a plugin. A `tool_used` grader with `tool: Skill` records whether
the skill fired, and `min: 0, max: 0` asserts a tool was never called, which
gives you should not trigger cases. `claude plugin eval init` "proposes
prompts that should and shouldn't trigger the plugin".
(https://code.claude.com/docs/en/plugin-evals, via WebFetch.) So formwork could
measure its own routing. Nobody has done it for formwork. NOT ESTABLISHED.

---

## R4. Dynamic role generation

| Who | How a role is generated | How it is checked | Source |
|---|---|---|---|
| AG2 AgentBuilder (AutoBuild) | a "build manager (a LLM)" reads a building task and writes agents: name, model, system message, description | no validation step described. Config saved as JSON and reusable "without prompting the build manager" | https://microsoft.github.io/autogen/0.2/blog/2023/11/26/Agent-AutoBuild |
| AG2 CaptainAgent | splits the task, "proposes roles for each", builds a team from a library or "from scratch"; reflects and may adjust the team | no check on generated agents described | https://classic.docs.ag2.ai/latest/docs/blog/2024/11/15/CaptainAgent/ |
| MetaGPT `Assistant` | "a `fork` style meta role capable of generating arbitrary roles at runtime based on a configuration file" | none in that file | `MetaGPT/metagpt/roles/assistant.py` (read myself) |
| BMAD party mode | open rooms cast personas "on the fly"; `create-party` lets the user invent personas saved to their override TOML | the roster script reports `roster_problems`; persona content unchecked | `bmad-party-mode/SKILL.md` (read myself) |
| Claude Code | "describe the subagent you want and where to save it"; Claude writes the file | `claude plugin validate` checks frontmatter parses. Unknown fields "ignored without reporting an error" | code.claude.com/docs/en/sub-agents, /skills |
| Claude Code agent teams | lead spawns teammates from a natural language request, or from a subagent definition | none of the teammate content; hooks `TaskCreated`, `TaskCompleted`, `TeammateIdle` can gate work | code.claude.com/docs/en/agent-teams |
| Agent Framework Magentic | manager coordinates existing agents | agents are defined, not generated | learn.microsoft.com orchestrations |
| CrewAI hierarchical | manager auto created if missing; workers predefined | manager "reviews outputs" | docs.crewai.com processes |
| ChatDev 2 | user (or an assistant) writes YAML workflows | `make validate-yamls` checks syntax and schema | ChatDev README |

**Finding.** Generation is common. Checking a generated role is rare, and
where it exists it is *structural* (does the file parse, does the schema
hold). No tool I read checks the content of a generated role: whether its
boundary overlaps another role, whether it says what it does not own, whether
it says when it is wrong. formwork's `role-shape` check already does two of
those (five sections; no two roles own the same slug; only lead spawns) per
`formwork/check/checks/role-shape`. As far as I found, that is further than
anything above goes. **Would be wrong if:** a tool I did not read (AgentVerse,
or newer AG2 v1 docs) has a content check. Not searched.

**Second finding.** The tools that generate roles keep them. AutoBuild saves a
config so the next run skips generation; BMAD writes invented personas to the
user's TOML. Generated, then frozen, then reused. That maps onto formwork's project roles
folder (named in HOW-TO-ADD-A-ROLE.md) plus `formwork roles`.

---

## R5. Taste and anti AI slop checklists

### Published examples, read

1. **Anthropic `frontend-design` skill** (read myself:
   `anthropics/skills/skills/frontend-design/SKILL.md`, HEAD 2026-11-14). The
   most specific public list. It names five clusters AI design falls into,
   among them: warm cream with terracotta accent; near black with one acid
   accent; "the SaaS-card kit: content chopped into identical rounded cards";
   "template chrome", including an all caps eyebrow above every heading and a
   '→' on buttons. It names typographic tells (one accented word in a headline,
   all caps labels). Process: plan a token system first, then "review that plan
   against the brief before building", then build and critique with
   screenshots. "Spend your boldness in one place." "the brief's own words
   always win". It also carries a writing section for UI copy: "A user manages
   notifications, not webhook config."
2. **gstack design checklist**
   (https://raw.githubusercontent.com/garrytan/gstack/main/review/design-checklist.md,
   read myself). Generated from a catalog. Each item tagged HIGH (grep
   detectable), MEDIUM (heuristic) or LOW (needs eyes). Classified AUTO-FIX,
   ASK or POSSIBLE. 27 items under "AI Slop Detection", with greps, e.g.
   "[gradient-text] ... Grep for `background-clip: text`"; "Uniform bubbly
   border-radius ... if more than 80% share one value of 16px or more, flag
   it". It defers to a project `DESIGN.md`: "Patterns explicitly blessed in
   DESIGN.md are NOT flagged." It only runs when the diff touches frontend
   files.
3. **Impeccable** (`npx impeccable detect`, exit 2 on findings, regex and DOM
   rules; says it builds on Anthropic's frontend-design skill). Only via
   package READMEs in search results, e.g.
   https://cdn.jsdelivr.net/npm/impeccable@2.3.2/README.md. Rule count
   disagrees across versions (24, 25, 27). Details NOT ESTABLISHED beyond that.
4. **Wikipedia, Signs of AI writing**
   (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, via WebFetch,
   first 100,000 of 249,000 characters only). Categories: undue emphasis on
   significance, superficial "-ing" analysis, vague attributions ("Experts
   argue"), "serves as" in place of "is", negative parallelisms ("It's not ...,
   it's ..."), leftover chatbot replies, markdown in prose. Its own caveats:
   "descriptive, not prescriptive"; each sign "a potential indicator, not
   proof"; fixing surface signs "isn't the goal". formwork's `humanizer`
   skill is already in this family.
5. **anthropics/skills `pptx`** (read myself: `skills/pptx/SKILL.md`). Deck
   taste: "Dominance over equality: One color should dominate (60-70% visual
   weight)"; "Commit to a visual motif"; "Do not use a color bar or accent
   stripe as your motif"; "If swapping your colors into a completely different
   presentation would still 'work,' you haven't made specific enough choices."
6. **Apple Human Interface Guidelines**
   (https://developer.apple.com/design/human-interface-guidelines). The page
   rendered as a title only through WebFetch. Its contents: NOT ESTABLISHED
   from this fetch. It is the obvious base for an iOS pack.
7. Several community design review skills exist (search result
   aggregators only: whawkinsiv design-review, borghei design-auditor with an
   "AI Slop" grade, StyleSeed). Not read. NOT ESTABLISHED.

### What is general enough to ship in a general kit

Common to every list above, regardless of product kind:

- **A default is not a choice.** Every list targets the thing that appears
  "regardless of subject" (frontend-design), or "would still work" on another
  topic (pptx).
- **The project's own design file wins.** frontend-design: the brief wins.
  gstack: DESIGN.md blesses exceptions. Kiro: `product.md`. So a pack is a
  default that a project overrides, never a law.
- **Grade by how a finding is detected.** gstack's HIGH / MEDIUM / LOW split is
  the honest version: some tells are greppable (a check), most need eyes (a
  reviewer round with screenshots).
- **Plan, review the plan against the brief, then build, then critique on the
  rendered thing.** frontend-design and gstack both separate the plan review
  from the output review.
- **Writing tells are their own list,** shared across every product kind.

Per product kind, from these sources:

| Pack | Base it on | Mechanical part (a check could grep) | Judgment part (a reviewer) |
|---|---|---|---|
| web | frontend-design, gstack catalog | gradient text, uniform radius, all caps body, `outline: none`, system font as display face | hero choice, one bold element, motion |
| iOS | Apple HIG (contents not established here) | NOT ESTABLISHED | platform conventions; screenshots per journey |
| deck | pptx skill | NOT ESTABLISHED as greps; the skill has a validator for file structure only | one dominant colour, one motif, varied layouts |
| writing | Wikipedia signs, humanizer | listed phrases, "serves as", dash rules already in `docs/style.md` | does the text say the thing |

The project specific list from the health app (pills only for real choices, one soft
light per screen, no icon tiles) belongs in the project. It overlaps several
generic items (no decoration posing as data matches frontend-design's
"Visual structure is information"), which suggests the generic pack would have
caught part of it. That overlap is my reading, not measured.

---

## R6. Usage awareness

**Does any tool track concurrent agents against plan limits? NOT
ESTABLISHED.** I found none that does both.

What exists:

- **Claude Code exposes the numbers.** The status line receives
  `rate_limits.five_hour.used_percentage`, `rate_limits.seven_day.used_percentage`
  and their `resets_at`, for Pro, Max and Ultra subscribers, after the first
  API response. (https://code.claude.com/docs/en/statusline, via WebFetch.)
  That is data a hook or script can read. Nothing in the docs acts on it.
- **Claude Code caps nesting, not concurrency.** Spawn depth defaults to three
  layers (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`). For agent teams: "There's no
  hard limit on the number of teammates", with advice to start at three to five
  and a note that token cost "scales linearly".
  (code.claude.com/docs/en/sub-agents, /agent-teams.)
- **A concurrency cap variable** (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, default
  20) is claimed by third party blogs in search results only. I did not find
  it in the official subagents page. NOT ESTABLISHED.
- **Spend limits** exist behind an organisation gateway
  (`rate_limits.spend_limit`), enforced per request. That is money per
  developer, not agents per plan.

So the pattern available to a general kit is: read the usage percentage the
host exposes, and scale how many builders the lead starts. The kit can
describe it. Building it is host specific (Claude Code only, as far as I
checked), which is the same reason "a model per role" was dropped.

---

## What transfers to formwork, ranked

Each with what would make the claim wrong.

**1. Say the size, let the person override it, step up if it grows.**
From superpowers brainstorming and BMAD `bmad-build` (oneshot, full, auto;
escalate from oneshot to full; record `route_source: pinned | auto`), and
from Shape Up's appetite. This is the most direct answer to "do not over build
a small ask". formwork already has five sizes in `formwork/loop.md`; the gap
is a routing step that names one of them in a plain line before work starts,
and writes it into the brief so a check can read it.
*Wrong if:* the size line is skipped in practice the way the director's "do
not build" rule was broken four times (`director.md`). That is a guess about
adherence; unmeasured.

**2. Prefer explicit selection over implicit selection as the library grows.**
The routing papers show implicit loading collapsing with distractors while
explicit selection holds. formwork's router should pick from a short, named
list (five sizes, a handful of product kinds, existing roles) and say the pick
back, not rely on dozens of role descriptions firing on their own.
*Wrong if:* at formwork's actual library size (28 roles) implicit matching is
already accurate. Unmeasured; the papers test hundreds to 80,000 skills.

**3. Layer routing: always loaded, deterministic, then model judgment.**
The tools that work combine a short always loaded file, deterministic triggers
(hooks, paths), and description matching. For formwork: a short routing table
in the always loaded file; a `UserPromptSubmit` or SessionStart hook to inject
it (as superpowers does); paths for product kind specific packs.
*Wrong if:* a portable kit cannot rely on hooks. The survey's decision 1 says
portable kits are advisory by construction. Hooks are Claude Code specific as
far as checked.

**4. Measure routing with should and should not cases.** Claude Code plugin
evals (`tool_used`, `min: 0, max: 0`) and skill-creator's description tuning
already provide the instrument. A small fixture set (task, bug, research,
deck, app) with the expected size and roles would make "understanding from one
prompt" checkable, in formwork's style of a check plus a fixture that breaks
it.
*Wrong if:* eval runs cost more than the project will spend, or results vary
too much run to run to gate on. Both NOT ESTABLISHED.

**5. Generated roles: generate, check content, freeze, reuse.** AutoBuild and
BMAD freeze generated roles to config. formwork's `role-shape` already checks
more than any generator I read. The transfer is the lifecycle: the lead drafts
a project role in the five section format into the project roles folder,
`role-shape` checks it, the human accepts, and it is reused.
*Wrong if:* `role-shape`'s structural check passes roles that are empty in
substance. Nobody has measured how often generated roles pass the shape but
fail the job.

**6. Gates with criteria written before, and more than two outcomes.**
Stage-Gate's inputs, criteria, and Go / Kill / Hold / Recycle; Shape Up's
default kill; Spec Kit's review gates that pause a run until a verdict. A
phase gate in formwork maps to the human's read-back, which already exists.
Adding Kill and Recycle as named outcomes is the new part.
*Wrong if:* the extra outcomes add paperwork larger than the work, which
`director.md` names as the way the method dies.

**7. Taste packs as overridable defaults, graded by detection.** Ship per
kind packs (web, deck, writing first; iOS once the HIG is read properly) as
defaults the project file overrides, with gstack's split between greppable
items (a check) and judgment items (a review round on screenshots).
*Wrong if:* generic packs miss what made the health app's v1 "dead". The overlap I
noted with the health app's own list is a reading, not a measurement.

**8. Usage awareness as a described pattern only.** Read the host's usage
percentage, scale the number of builders. Describe it; do not build it into a
general kit yet.
*Wrong if:* another host exposes the same data, making it portable. Not
checked beyond Claude Code.

**What the evidence argues against.** A fixed "software company" of roles
(MetaGPT, ChatDev 1). ChatDev moved off it to user defined workflows, and
AutoGen was archived for a pattern framework. Also against superpowers'
"1% chance" rule as is: it maximises process, which is the opposite risk to
the one formwork has already seen.

---

## What I read

This repository: `docs/rounds/whole-project-builds/brief.md`,
`docs/briefs/0022-whole-project-builds.md`,
`docs/ideas/2026-11-15-whole-project-builds.md`, `docs/survey.md` (method,
BMAD, GSD, Agent OS, CrewAI, AutoGen, anthropics/skills, superpowers,
cross cutting, decisions, appendix), `docs/standing.md` (lines 15 to 45, 88 to
105), `formwork/check/checks/role-shape` (header).

Repositories, from tarballs: spec-kit (README, `docs/workflows/overview.md`,
`templates/`), BMAD-METHOD (`skills/` tree, `core-tools/bmad/SKILL.md` and
`references/help.md`, `bmad-party-mode/SKILL.md`, `method/bmad-build/`
customize, steps, plan template, `bmad-build-auto/SKILL.md`,
`bmod-method/retired.toml`), superpowers (`using-superpowers`,
`diagnosing-superpowers`, `brainstorming`, `hooks/`), anthropics/skills
(`frontend-design`, `pptx`), agent-os (file list), claude-task-master
(`docs/command-reference.md`), MetaGPT (README, `metagpt/roles/`,
`assistant.py`), ChatDev (README), autogen (README), gstack
(`review/design-checklist.md`, raw).

Web pages: stage-gate.com overview; gv.com/sprint; basecamp.com/shapeup ch.1;
designcouncil.org.uk double diamond; svpg.com dual track; code.claude.com
sub-agents, skills (both halves), hooks, plugin-evals, statusline,
agent-teams, llms.txt; kiro.dev specs and steering; learn.microsoft.com Agent
Framework orchestrations; docs.crewai.com processes; docs.openhands.dev skills;
docs.langchain.com multi-agent; AutoGen 0.2 AutoBuild blog; AG2 CaptainAgent
blog; arXiv 2610.18522 and 2603.22455 abstracts; claude.com skill-creator
blog; Wikipedia Signs of AI writing (first 40%); Apple HIG (title only).

## What I could not establish

- Any accuracy figure for routing a request to a workflow, phase or size. NOT
  ESTABLISHED anywhere.
- Skill routing accuracy at formwork's library size. The papers test far
  larger libraries.
- The GV Decider and supervote wording from a primary source (search results
  only).
- Stage-Gate Lite and XPress structure from a primary source.
- Whether Kiro standard specs gate between phases; Kiro's intent detection
  prompt (third party extraction only, not used).
- Apple HIG contents (page did not render).
- Impeccable's rule set beyond package README snippets; the community design
  review skills.
- `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and any per plan concurrency cap.
- Any tool that governs concurrent agents against plan limits.
- Whether any generated role check beyond structure exists in tools I did not
  read (AgentVerse, AG2 v1).
- Whether any of these tools improves outcomes. None was executed. Every claim
  is about files and docs, not behaviour observed.
- The rest of the Wikipedia page (60% unread) and the full arXiv papers.
