# Taste pack: screens

For any rendered screen: a web page, a phone app, a desktop app. The `web` and
`ios` packs build on this one.

**Source.** Adapted from one project's director check of ten design samples,
done after the person said the samples still felt machine made. Each point
there became a rule for the next phase. They are written here as general
rules, with no product or person in them. Where a public source says the same,
it is cited.

The shape of each item is in [README.md](README.md). Taste is never a check:
these are for a reviewer looking at pictures.

---

### screens-1 Pills only for real choices
**Catches** rounded outlined chips everywhere: status, finished items, labels,
numbers in capsules. A pill says "you can pick this". Things that are done are
plain text with a small mark, or a mark on a timeline.
**Detected** medium. A hint: count the pill shaped elements on one screen
(fully rounded corners with a border or a tint). More than one group that is
not a choice is a candidate.

### screens-2 One soft light per screen, and buttons never glow
**Catches** glow on everything: buttons, rings, routes, results, cards. At most
one soft light per screen, on the one thing that is happening now.
**Detected** high for web, low elsewhere. A hint for web: a coloured shadow
with no offset (`box-shadow: 0 0 ...`). The gstack checklist calls this
"glowing edges on dark surfaces".
**Source** also https://raw.githubusercontent.com/garrytan/gstack/main/review/design-checklist.md

### screens-3 Solid colours, unless a gradient means something
**Catches** gradients by default: gradient buttons, gradient bars, gradient
blobs. A gradient is fine where it carries meaning, such as time of day or a
change along a scale.
**Detected** medium. A hint: `linear-gradient`, `radial-gradient`,
`LinearGradient`. Stock purple to blue gradients are the commonest form (also
flagged by ECC's design quality hook, `scripts/hooks/design-quality-check.js`
in https://github.com/affaan-m/ecc). Then ask what the gradient means.

### screens-4 No icon in a coloured tile
**Catches** an icon placed on a coloured square or circle as decoration, on
every row or card. Icons stand on their own, in the colour of their meaning.
A tile is fine where the tile is the object itself, such as a photo.
**Detected** low. The gstack checklist lists "icons in colored circles as
decoration" at the same level.

### screens-5 One neutral surface
**Catches** cards each washed in their own pastel tint. Colour lives in the
content (a number, an icon, a bar), not as a wash over the card.
**Detected** medium. A hint: more than two distinct background tints on card
elements on one screen.

### screens-6 Standard navigation
**Catches** custom back, close and add buttons made of the same big frosted
circles in every corner. Use the platform's own navigation. A circle only
where the platform uses one.
**Detected** low. Compare the screen's top and bottom bars with the platform's
standard ones.

### screens-7 Placeholders that look fake
**Catches** a grid with a blob for a map, grey boxes for photos, labels that
collide. A placeholder that ships looks like a product nobody finished. Use
the real component, or leave the space out.
**Detected** low. Look at every map, image and dense label area at the real
size.

### screens-8 One accent per row
**Catches** several accent colours side by side, so nothing leads. Colour by
meaning stays, but one category colour per row, and the screen's main colour
wins.
**Detected** low. Count the distinct accent colours in the top third of the
screen.

### screens-9 The same card, repeated
**Catches** all content chopped into identical rounded cards in a uniform
grid, whatever the content is. Different content gets a different shape.
**Detected** medium. A hint: a grid of three or more siblings with the same
classes or the same component and the same size. ECC's design quality hook
warns on uniform card grids; Anthropic's `frontend-design` skill calls it "the
SaaS-card kit". https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md

---

The two kit items most often broken on screens are kit-1 (decoration posing
as data) and kit-2 (copy that talks about the app). See [README.md](README.md).
