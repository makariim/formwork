---
status: proposed
date: 2026-10-17
deciders: [Muhammad Elsherif]
consulted: [argus]
informed: []
---

<!-- Proposed by an agent, from his words below. It becomes a decision when he
     changes the status to accepted. Until then nothing here is decided. -->

# 0001. Text sent as the human goes through humanizer

## What made this a decision

His words, 2026-10-17: "if it is really strong, i want to adopt really
everywhere that generates text a human supposed to be writing, a doc, a wiki,
a drafted email, a drafted message, a github comment, anything anywhere".

Then: "Keep a pinned copy in formwork, since every repo already uses
formwork". And "yes" to adopting it on these terms, after a test on three real
texts (`argus/research/13-humanizer.md`): for text sent to people; not for
agents' reports and replies to him; one bold per section kept.

The skill is a third party's instructions, about 8,000 tokens, run inside
every agent that writes for him. Upstream ships often: 40 commits between
2026-09-05 and 2026-10-17
(`gh api "repos/blader/humanizer/commits?since=2026-09-05T00:00:00Z&until=2026-10-17T23:59:59Z&per_page=100" --jq length`),
and two major versions.

## What matters here

- Text other people read in his name reads like him, without added facts.
- Replies and reports to him keep the shape he asked for: headings, bullets,
  one bold per section.
- A new upstream version takes effect only when somebody has read it.

## Options we looked at

- **Pinned copy in the kit**, at one commit, with formwork's change to §19 in
  a separate file, placed by `formwork roles`. Updated by hand.
- **Install from upstream or a plugin marketplace.** Always current, and the
  next version applies without anyone reading it.
- **Do nothing.** Agents write his messages, comments and docs in their
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
- The test found it clearly better on a message to a friend, slightly better on
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
