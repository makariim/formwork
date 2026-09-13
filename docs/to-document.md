---
updated: 2026-09-13
---

# What still needs writing

Live, not history. What the pages owe, so nothing is remembered only in a chat
window.

**This file is meant to be emptied and deleted.** One of the kit's own rules
warns against a "later" file that only grows. The defence is that it has an
end: when version two ships, every line here is written or dropped with a
reason, and the file goes.

Nothing here is a decision. It is a list of writing owed.

---

## Owed

| What | Where it lands |
|---|---|
| Numbers in `docs/` that are now stale | those pages are history and say so at the top. Decide whether that is enough, or mark the figures |
| **Em dashes still in the programs**, in comments and in the findings they print: `0001-x.md — no date`. There it is a column separator, not a pause in a sentence. Left alone on purpose | your call. The prose is done |

## Found by the audits, and left on purpose

| What | Why it stays |
|---|---|
| `style-pointed` goes green when the generated roles are **deleted** rather than fixed | to catch it, the check would have to know which roles ought to exist, which means a second copy of the generator. A checker built out of the thing it checks is not a check. Written on the check itself |
| Four of the ten must-pass fixtures pass **vacuously**: the check exits 0 having examined nothing | arguably correct behaviour, but it means the gate's "shown to accept the right" line counts cases rather than coverage |

## Settled

**0.2.0 is released and tagged**, so the pages and the package agree again.
The About text, website and topics are set on the repository page.

**This project does not use GitHub Releases.** Tags only. Nothing writes
release notes, and no page should tell anybody to look for them.

## Dropped, with the reason

**Skills**, and **a model per role**. Both dropped before starting, so there is
nothing to document. The README lists them as not here, and says the model one
is known to work on Claude Code only, because nobody has read the other three
publishers' documentation.

## Done, and kept here for one release

- the documentation pass: one home per fact, routers fixed, repeated wording
  cut from 240 shared runs of seven words or more to 89, measured across
  twenty one pages
- 328 em dashes replaced in the pages and role files, six repaired by hand,
  one table cell repaired after an audit found it
- `formwork/install` run from a subfolder wrote into that subfolder; the first
  fix moved the bug to a kit run from elsewhere; it now refuses rather than
  guessing, and eight tests watch all three cases
- `formwork setup` edited `[bindings]`, could corrupt a config into
  unparseable TOML, read Ctrl-C as consent, and overwrote a file created while
  it was asking. All four closed, fourteen tests added
- the three new checks each reported clean while examining nothing. Six such
  routes closed, with a fixture each
