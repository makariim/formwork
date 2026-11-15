---
brief: 0032
date: 2026-11-15
---

# 0032 The motion taste pack

## For you

The motion pack is in `formwork/taste/motion.md`: 16 items from the Glide and Ripping studies, each with what it catches, how it is detected and a linked public source. Where both studies said the same thing, I merged them into one item.
`web-5`, the `screens`, `web` and `ios` packs, both round templates and `route.md` now point to it. Taste is still judged on pictures and recordings, never by a check.
No guard refused anything, so there is no patch. All 571 tests pass. The gate is red on one check, `work-paired`: 0031 and 0032 are both open, and the limit is one. Your read-back on 0031 clears it.
The Ripping material was not in the brief. A Director session asked for it while I worked, and I took it in. Undo motion-9 to motion-12 and motion-14 if you did not want it.

## For the director

### Contradictions

- The brief names only `glide-studio.md`. A Director session message, received mid work, added `docs/research/ripping.md` ("fold in the items that are new... Merge overlaps... keep its 'What not to take' out"). I treated it as part of 0032. The brief file itself was not edited.
- His global instructions say to set the brief to `status: done`. `work-paired` refuses done without his read-back, so 0032 stays `open`, as with 0027 to 0031.
- The gate was already red before I started: doc-links (the brief links to `formwork/taste/motion.md`, which did not exist yet) and work-paired (0031 open, waiting for his read-back). Writing the pack cleared doc-links. work-paired is not mine to clear.

### What changed

| file | change |
|---|---|
| `formwork/taste/motion.md` | new. How to look at motion (still frame first, then the recording at full and half speed, then with reduced motion on). 16 items in five groups. What it cannot do. |
| `formwork/taste/README.md` | `motion` row in the packs table. One line on what it assumes and that it is judged on recordings. "pictures" became "pictures and recordings". |
| `formwork/taste/web.md` | top line points to `motion`. `web-5` points to motion-13 and motion-15: a loop is fine only when it pauses unseen and stops with reduced motion on. |
| `formwork/taste/screens.md` | top line: the first and last frame of every animation must pass `screens` as stills. `screens-2` points to motion-2 and motion-3. |
| `formwork/taste/ios.md` | top line points to `motion`. Motion stays NOT ESTABLISHED for Apple; the general pack applies until Apple's motion page is read, and Apple wins where they disagree. |
| `formwork/templates/design-round.md` | if the samples move, add `motion` and give reviewers recordings. |
| `formwork/templates/review-round.md` | where the product moves, `motion` is judged on recordings. |
| `formwork/route.md` | `motion` in the list of packs a brief can name; "pictures and recordings". |

### The items, and where each comes from

| id | name | detected | sources |
|---|---|---|---|
| motion-1 | Motion with no sentence | low | Glide rule 3 + Ripping 1 and 2 (motion follows the words), merged |
| motion-2 | Two things moving with equal weight | low | Glide rule 2 + Ripping's one at a time, merged |
| motion-3 | The accent does not land last | low | Glide rule 4 |
| motion-4 | A hard cut where something could carry over | medium | Glide reels |
| motion-5 | Curves and durations with no names | high | Glide tokens |
| motion-6 | Exits as slow as entrances, and long journeys | high / medium | Glide headline + Ripping 11, merged |
| motion-7 | Physics everywhere, or a curve under the finger | medium | Glide rule 1 and its own spring + Ripping 9; settles the curves vs springs tension the Glide study left to the pack |
| motion-8 | Words that move while they should be read | low | Glide rule 5 |
| motion-9 | Captions that say it differently | low | Ripping 5; WCAG 2.2 1.2.2 |
| motion-10 | A slow first second | low | Ripping 4 |
| motion-11 | A number built all at once, or from nothing real | low | Ripping 3; kit-1 |
| motion-12 | Entrances that replay, or hide what was already seen | medium | Ripping 7 |
| motion-13 | Loops nobody is watching, and auto-play that will not yield | medium | Glide rule 6 + Ripping 6, merged |
| motion-14 | Progress that follows the clock | medium | Ripping 10 |
| motion-15 | A reduced version that is only "off" | high / low | Glide rule 8 + Ripping 8, merged; WCAG 2.2 2.3.3 |
| motion-16 | Custom motion that replaces the platform's | medium | Glide rule 7 |

Left out on purpose: Ripping's "What not to take" (as asked), both studies' "For his apps" sections, and Glide principles 7 and 8 (three beats for invisible work, edit the demo). Those two are advice on what to build, not patterns a reviewer catches. Glide principle 10 (still frame first) went into "How to look at motion", not an item.

### What was run

Nothing that wrote outside the repository. The guard was asked about each target with `formwork/guard/protected-files --path <file>`: all returned 0 (not protected). One `python3` heredoc and one `sed -i ''` made the pointer edits.

### The check

`formwork/fw test`: 571 tests, all passed.

`formwork/fw check`: **GATE red, 1 check failed.** 17 ok (doc-links, hidden-unicode, kit-leak-scan, kit-integrity and the rest). FAIL work-paired: "2 briefs are open and the limit is 1: docs/briefs/0031-three-gaps.md, docs/briefs/0032-motion-pack.md".

`grep -n "[—–]"` over every file touched: no dashes.

### Git status

Nothing staged. `git status --short`:

    M docs/standing.md                    (not mine: the Glide decision line, from the planning session)
    M formwork/route.md
    M formwork/taste/README.md
    M formwork/taste/ios.md
    M formwork/taste/screens.md
    M formwork/taste/web.md
    M formwork/templates/design-round.md
    M formwork/templates/review-round.md
   ?? docs/briefs/0032-motion-pack.md
   ?? docs/research/glide-studio.md
   ?? docs/research/ripping.md
   ?? formwork/taste/motion.md
   ?? docs/reports/0032-motion-pack.md

### The three that matter

- **Done but not asked for.** The Ripping items (see Contradictions). A "How to look at motion" section at the top of the pack, so a reviewer knows to use recordings and reduced motion.
- **Asked for but not done.** None. `deck` was not pointed to the pack; the brief did not name it, though the Ripping study suggests motion-11 fits there.
- **Wrong in the brief.** Nothing in the files. The brief's list of Glide items matched the research. The research's motion-8 and motion-9 are the "any others" the brief allowed for.

accepted: 2026-11-15
in my words: accepted, the motion pack looks good
