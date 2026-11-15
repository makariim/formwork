---
brief: 0029
date: 2026-11-15
---

# 0029 Taste packs

## For you

Step 7 of the research is in. A new folder, `formwork/taste/`, holds optional taste packs. None of them sets a look.
`formwork/taste/README.md` has the three kit items for every product: decoration never poses as data; copy says the thing, not the feature; every screen is asked "generic or machine made?" and "dead?". It also has the pack shape: each item says what it catches and how it is found (high, medium, low).
Four packs: `screens` (your director check rewritten as nine general rules, with no product or person in them), `web` (12 items), `deck` (7) and `ios` (7). Each one cites its public sources.
The Apple guidelines could be read this time, through the JSON behind each page. I read seven pages only, so the iOS pack is short. Everything else in it is marked NOT ESTABLISHED.
ECC's signals (generic headlines, card grids, stock gradients, default fonts) appear only as search hints inside items. No check was added. Taste stays a review round on pictures.
The routing table, the design round and the review round now point to the packs. A project names its packs in its own design file, and that file always wins.
No guard refused anything. 557 tests pass and the gate is green with all 16 checks. If you re-record fingerprints after review, that is the only step left. The brief stays `open` until your read-back.

## For the director

### Contradictions

- His global instructions say to set the brief to `status: done`. `work-paired` refuses done without the read-back, so the brief stays `open`, as with 0027 and 0028.
- The research said the Apple guidelines fetch failed. This time the HTML pages were not tried. The DocC JSON (`developer.apple.com/tutorials/data/design/human-interface-guidelines/<page>.json`) returned real content for all seven pages asked. So the iOS pack is not NOT ESTABLISHED as a whole, only past those seven pages. Several of those pages are long, and the fetch tool read only the first 100,000 characters of `color` and `typography`.
- "Pack" already means a group of roles in `formwork/glossary.md`. The new entry "Taste pack" starts with "Not a group of roles" to keep the two apart.

### Choices made

- One shared pack, `screens`, for the director check patterns, since they hold for web and phone alike. `web` and `ios` say they build on it. That avoids writing the same nine items twice.
- Item ids (`kit-1`, `screens-2`, `web-4`, `ios-3`, `deck-1`) so a project can override an item in one line and a review finding can name one.
- How a project names packs is a convention, one line in its design file (`Taste packs: screens, web`), with no parser and no check. A check reading it would be the first step toward a taste check.
- `web-12` (focus rings, contrast, target size, colour alone) is accessibility, not taste. It is in the web pack because a look most often breaks it, and it says a project should not override it, as `accessibility` owns it. It cites WCAG 2.2 criterion numbers.
- The two Stride points already covered by kit items (decoration as data, copy about the app) are not repeated in `screens`; the pack points back to kit-1 and kit-2.
- The visual role file was not changed. The brief did not ask, and role files are generated, so a change would mean `fw roles` and a wider diff.

### What changed

- `formwork/taste/README.md` (new): three kit items, pack shape, the pack list, how a project uses them, what this cannot do.
- `formwork/taste/screens.md` (new): nine items adapted from the director check (pills, one soft light, solid colours, no icon tiles, one neutral surface, standard navigation, fake placeholders, one accent per row, the same card repeated).
- `formwork/taste/web.md` (new): twelve items. Sources: gstack design checklist, Anthropic's `frontend-design` skill, ECC's design quality hook (hints only), WCAG 2.2.
- `formwork/taste/deck.md` (new): seven items. Sources: assertion-evidence, Edward Tufte's notebook page on slides, `frontend-design`.
- `formwork/taste/ios.md` (new): seven items from the HIG pages materials, color, buttons, typography, tab bars, writing, charts.
- `formwork/templates/design-round.md`: a "Taste packs" section.
- `formwork/templates/review-round.md`: look with the named packs, report by id, the design file wins, never a check.
- `formwork/route.md`: a paragraph under "Templates for a phase" on naming packs.
- `formwork/glossary.md`: "Taste pack" entry.
- `formwork/limits.md`: "No check judges taste".
- `README.md`: a `taste/` row in the kit table.
- `CHANGELOG.md`: one Unreleased entry.

### Sources read

| Source | How |
|---|---|
| https://raw.githubusercontent.com/garrytan/gstack/main/review/design-checklist.md | fetched, summarised by the fetch tool |
| https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md | fetched, quotes taken |
| HIG JSON for materials, color, buttons, typography, tab-bars, writing, charts | fetched, quotes taken; color and typography only the first 100,000 characters |
| https://www.w3.org/TR/WCAG22/ and the 2.5.8 Understanding page | fetched |
| https://www.assertion-evidence.com/ | fetched |
| https://www.edwardtufte.com/notebook/powerpoint-does-rocket-science-and-better-techniques-for-technical-reports/ | fetched |
| ECC design quality hook | not fetched again; taken from `docs/research/ecc-ideas.md` |
| the Stride director check | read only, on this machine |

All quotes came through a fetch tool that summarises with a small model. They were not compared with the pages by hand: a quote may be slightly off. NOT ESTABLISHED that each is verbatim.

### What was run

| Command | Result |
|---|---|
| `formwork/fw test` | "557 tests, all passed" |
| `formwork/fw check` | "GATE: green. 16 check(s), each shown to reject the wrong and accept the right." `kit-leak-scan`, `doc-links`, `kit-integrity` ok |
| grep for em and en dashes in `formwork/taste/*.md` and in added diff lines | none |
| `grep -rn -i "stride\|metformin\|muhammad\|his " formwork/taste/` | no product or person named |

### Not done

- Fingerprints: his to re-record after review if needed (the gate is green now).
- Brief left `open` until the read-back.
- No other repository touched. No git writes. `docs/standing.md` not edited beyond what was already in the tree.

accepted: 2026-11-15
in my words: next, he re-recorded the fingerprints and committed the taste packs
