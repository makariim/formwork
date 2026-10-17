---
status: accepted
date: 2026-10-17
deciders: [the maintainer]
consulted: []
informed: []
---

<!-- Proposed by an agent. It becomes a decision when the maintainer changes
     the status to accepted. Until then nothing here is decided. -->

# 0001. Text sent as the human goes through humanizer

## What made this a decision

Agents write text that goes out under the human's name: docs, wiki pages,
emails, messages, GitHub comments. The `humanizer` skill rewrites such text so
it does not read as machine-written. It was adopted on these terms after a
test on three real texts: for text sent to people; not for agents' reports
and replies to the human; one bold per section kept.

The skill is a third party's instructions, about 8,000 tokens, run inside
every agent that writes for the human. Upstream ships often: 40 commits between
2026-09-05 and 2026-10-17
(`gh api "repos/blader/humanizer/commits?since=2026-09-05T00:00:00Z&until=2026-10-17T23:59:59Z&per_page=100" --jq length`),
and two major versions.

## What matters here

- Text other people read in the human's name reads like them, without added
  facts.
- Replies and reports to the human keep the shape they asked for: headings,
  bullets, one bold per section.
- A new upstream version takes effect only when somebody has read it.

## Options we looked at

- **Pinned copy in the kit**, at one commit, with formwork's change to §19 in
  a separate file, placed by `formwork roles`. Updated by hand.
- **Install from upstream or a plugin marketplace.** Always current, and the
  next version applies without anyone reading it.
- **Do nothing.** Agents write the human's messages, comments and docs in their
  default voice.

## What we chose, and why

Proposed: **the pinned copy**, blader/humanizer at commit
`8c307f367c91bd974002f10f2be2965d642c13df` (3.1.0), in
`formwork/skills/humanizer/`. Because it is in the kit, every repository on
formwork gets it the same way. Because it is pinned, an update is a read diff
and a changed line (`formwork/skills/humanizer/UPSTREAM.md`).

The rule is in `formwork/style.md`, which every generated role points at.
Text written to be sent or published as the human goes through the skill in
embedded mode first. An agent's reports, briefs, standing brief and replies to
the human do not. Messages under about three sentences may skip it.

§19 is overridden in `formwork/skills/humanizer/local.md`. Decorative and
labelled bold is removed, and one bold per section is kept.

## What follows

**Good:**
- One copy of the skill and one rule, reaching every repository through the
  kit.
- The test found it clearly better on a personal message, slightly better on
  a PR-comment-shaped text, and it caught its own first draft dropping words.

**Bad:**
- About 8,000 tokens each time it loads.
- The pin goes stale. Upstream fixes arrive only when somebody does the update.
- Nothing checks that an agent used it. It is advice, like the rest of
  `style.md`.
- Only Claude Code gets the skill placed where it loads. On the other runtimes
  an agent has to read the two files itself.
- The evidence is one test of three texts by an agent, and one upstream blind
  test that was not verified.

## What would make us revisit this

Text that went through it reads worse to the people who received it, or loses
or adds a fact. Or an upstream version changes what §19 means, so `local.md`
no longer fits.
