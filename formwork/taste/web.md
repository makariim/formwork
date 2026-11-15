# Taste pack: web

For web pages and web apps. Use it with [`screens`](screens.md). Where the
page moves, add [`motion`](motion.md).

**Sources.**
- gstack design checklist, the "AI slop" and typography sections:
  https://raw.githubusercontent.com/garrytan/gstack/main/review/design-checklist.md
- Anthropic's `frontend-design` skill:
  https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- ECC's design quality hook, which only warns, used here as hints:
  `scripts/hooks/design-quality-check.js` in https://github.com/affaan-m/ecc
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

The shape of each item is in [README.md](README.md). Every search pattern below
is a hint for a reviewer. None of them is a check.

---

### web-1 A default font as the voice
**Catches** a page whose type was never chosen: the system font stack as the
main face, or one of the display faces every generated page reaches for.
Frontend-design: "Choose your typefaces deliberately, not the default families
you would reach for on any other project."
**Detected** high for the system stack, medium for overused faces. A hint:
the first family in `font-family` is `system-ui`, `-apple-system` or the
framework default. More than three families on one page is the opposite
fault.

### web-2 A generic headline
**Catches** hero copy that could sit on any product: "Build faster", "The
future of X", "Everything you need", with "Get started" and "Learn more"
under it. This is kit-2 at the top of the page.
**Detected** medium. A hint: search the headings and buttons for stock
phrases and marketing words. Then ask whether the line could be moved to a
competitor's page unchanged.

### web-3 Gradient text
**Catches** a headline filled with a gradient.
**Detected** high. A hint: `background-clip: text` or
`-webkit-background-clip: text`.

### web-4 One word accented in a headline
**Catches** a headline with one word in italic, bold or another colour, a
short tracked capital label (a kicker) above every heading, and all capitals
for labels. Frontend-design lists all three among "the commonest tells of a
generated page".
**Detected** medium. A hint: a `<span>` with its own colour or style inside
an `h1` or `h2`; a short element with `text-transform: uppercase` and letter
spacing just before a heading.

### web-5 Motion on everything
**Catches** a fade and slide up on every section, a hover effect on every
card, images that grow on hover, bouncy easing, a dot that pulses forever.
Frontend-design calls the first two "the generic default". Motion triggered by
interaction must also be possible to turn off (WCAG 2.2, 2.3.3).
**Detected** high for bounce (`cubic-bezier` control points past 1, or
animation names with "bounce"), medium for the rest (`:hover` with
`transform: scale`, `animation: ... infinite` on small round elements).
Check that `prefers-reduced-motion` is honoured.
The [`motion`](motion.md) pack goes further: loops that pause off screen
(motion-13), a designed reduced version (motion-15), and the rest of what
motion says. A loop is fine only when it pauses unseen and stops with
reduced motion on.

### web-6 Everything centred
**Catches** every block of text centred, so the page has no edge to read
from.
**Detected** medium. A hint: most text containers carry
`text-align: center`.

### web-7 Frosted glass as the default surface
**Catches** a blurred translucent panel used for every container, not for the
one thing that floats over content.
**Detected** medium. A hint: `backdrop-filter` on more than one or two
containers.

### web-8 One radius on everything
**Catches** the same large corner radius on buttons, cards, inputs and images,
whatever their size or role. Frontend-design: "one border-radius on
everything regardless of hierarchy".
**Detected** medium. A hint: one `border-radius` value covers almost every
rule that sets one.

### web-9 Numbers and emoji as decoration
**Catches** emoji standing in for icons in headings and buttons, and numbered
markers (01, 02, 03) on content that is not a sequence. Frontend-design: the
markers are "only appropriate if the content actually is a sequence".
**Detected** medium. A hint: emoji in headings, list items and buttons; a
two digit number in its own element before each card title.

### web-10 A coloured border down one side of a card
**Catches** a thick coloured left border used to make a plain card look
designed.
**Detected** high. A hint: `border-left` with a colour on card like elements.

### web-11 Stock colour pairs
**Catches** the pairings that read as generated because they are everywhere:
a warm cream ground with one terracotta accent; near black with one acid green
or vermilion accent; tinted near black standing in for black. All three are
named in frontend-design.
**Detected** low. A search finds the values; only eyes say whether the pair
was chosen for this product.

### web-12 Defaults the look broke
**Catches** what taste choices most often break, though it is not taste:
- a focus ring removed with `outline: none` and nothing put in its place
  (WCAG 2.2, 2.4.7 Focus Visible). Detected high.
- text below 4.5:1 contrast with its background (1.4.3), or controls below
  3:1 (1.4.11). Detected medium, with a contrast tool.
- click targets under 24 by 24 CSS pixels (2.5.8,
  https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
  Detected medium.
- colour as the only way a state is shown (1.4.1). Detected low.

The project's design file may override any other item in this pack. It
should not override this one: these are owned by `accessibility`.
