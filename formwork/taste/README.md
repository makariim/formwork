# Taste packs

Optional. A taste pack is a list of things that make a rendered product look
generic, machine made or dead, for one kind of product. A project names the
packs it wants. Nothing here is a default for the look. Colours, fonts,
spacing and mood belong to the project.

**Taste is never a check.** No program in this kit judges a look. Taste is
judged by people and roles looking at pictures, in a review round
(`formwork/templates/review-round.md`). Some items below say a pattern can be
found with a search. That search is a hint for the reviewer, never a gate.

---

## The three kit items

These hold for every product kind, whatever the project's own taste. They are
the only taste content the kit carries on its own authority.

### kit-1 Decoration never poses as data
**Catches** a chart, sparkline, progress bar, map or picture that looks like
information but is not. Charts are drawn only from real numbers that mean
something to the reader. No fake pictures: a real image of the real thing, or
nothing.
**Detected** low. Needs eyes: ask "where does this number come from?" for every
mark that looks like data. A hint: a chart whose values are written as
literals in the code, or a placeholder image shipped as content.

### kit-2 Copy says the thing, not the feature
**Catches** text that talks about the product instead of telling the reader
something: lines that explain the interface, announce a feature, or praise
it. Say what is true and what to do.
**Detected** medium. A hint: stock calls to action ("Get started", "Learn
more", "Unlock", "Seamless", "Powerful") and sentences whose subject is the
product. The writing half is the `humanizer` skill.

### kit-3 Two questions for every rendered screen
**Catches** a screen that passes every rule and is still wrong. Each rendered
screen, slide or page gets two questions, answered in a sentence each:
1. Does it look generic, or machine made?
2. Does it look dead?

Clean is not the same as alive. Removing every "AI touch" can remove the life
too, and that is a failure of its own.
**Detected** low. Only by looking at the picture. This is the review round's
job.

---

## The shape of a pack

A pack is one file, `formwork/taste/<kind>.md`. Each item has:

| Part | Says |
|---|---|
| an id and a name | `web-4 Gradient text`. The id is how a project or a finding refers to it |
| **Catches** | what goes wrong, in one or two sentences |
| **Detected** | how it is found: **high** (a pattern a search could find), **medium** (a search finds candidates, a person decides), **low** (needs eyes) |
| a hint | where to look. A search pattern, a place in the picture, a question |
| **Source** | where the item comes from, with a link |

The high, medium and low levels follow the gstack design checklist
(https://raw.githubusercontent.com/garrytan/gstack/main/review/design-checklist.md).
Even a high item stays a hint: it says where to look, and a person decides.

---

## The packs

| Pack | For | Sources |
|---|---|---|
| [`screens`](screens.md) | any rendered screen: web, phone, desktop | adapted from one project director's check of real design samples, written as general rules |
| [`web`](web.md) | web pages and web apps | gstack design checklist, Anthropic's `frontend-design` skill, WCAG 2.2 |
| [`deck`](deck.md) | slides | assertion-evidence, Edward Tufte |
| [`ios`](ios.md) | iPhone and iPad apps | Apple's Human Interface Guidelines, as far as they were read |

`web` and `ios` assume `screens`. A writing pack already exists as the
`humanizer` skill in `formwork/skills/humanizer/`.

---

## How a project uses them

1. **Name them.** In the project's own design file (for example
   `docs/design.md`), one line near the top:
   `Taste packs: screens, web`.
2. **Override them.** The project's design file always wins. To turn an item
   off or change it, write one line there:
   `web-7 off: frosted panels are our look, decided in 0012`.
   An item the project overrides is not a finding.
3. **Point to them.** A design round brief names the packs the samples must
   pass. A review round brief names the packs the reviewers look with.
4. **Report by id.** A finding names the item: `screens-2, the checkout page:
   three glowing buttons`.

A project with no design file, or one that names no pack, uses only the three
kit items. A project may write its own pack in the same shape, in its own
folder. It is never copied back into the kit unless a brief says so.

---

## What this cannot do

Tell taste from habit. Every item here is a pattern that often reads as
generic. In one product it may be exactly right, which is why the project
overrides. A screen that passes every item can still be dead (kit-3), and only
a person looking at it will say so.

Know that the sources are right. They are public, cited, and adapted. None of
them was measured in this kit.
