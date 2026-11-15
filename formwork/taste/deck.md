# Taste pack: deck

For slides: a talk, a pitch, a readout, a board update.

**Sources.**
- The assertion-evidence approach: "you build your presentations on succinct
  messages (assertions), rather than phrase topics" and "you provide visual
  evidence rather than bulleted lists". https://www.assertion-evidence.com/
- Edward Tufte, notes on slides in technical work:
  https://www.edwardtufte.com/notebook/powerpoint-does-rocket-science-and-better-techniques-for-technical-reports/
- Anthropic's `frontend-design` skill, for the stock stat treatment:
  https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md

The shape of each item is in [README.md](README.md). Taste is never a check:
these are for a reviewer looking at the rendered slides.

---

### deck-1 A topic for a title
**Catches** slide titles that name a subject ("Results", "Market", "Next
steps") instead of saying what the slide shows. The title is the claim, as one
sentence: "Search time fell by half after the index change."
**Detected** medium. A hint: list every title. Titles of one to three words,
or with no verb, are candidates.

### deck-2 Bullets as the body
**Catches** a slide whose evidence is a bulleted list. Tufte calls such lists
"base-touching grunts, which show effects without causes". Give the evidence:
a chart, a picture, a table, a short worked example.
**Detected** medium. A hint: count the slides whose body is mostly list
items.

### deck-3 A chart as decoration
**Catches** kit-1 on a slide: a chart drawn to fill space, made up or rounded
into a shape, or with no source. Tufte: "presented as decoration, not
evidence". Every chart says where its numbers came from, on the slide.
**Detected** low. Ask of every chart: what is the source, and what would
change if the numbers were different?

### deck-4 The stock stat slide
**Catches** a big number with a small label, a row of supporting stats and a
gradient accent, used for every figure. Frontend-design: "the default
treatment". One number with its comparison and its source says more.
**Detected** medium. A hint: several slides built from the same big number
component.

### deck-5 Too little on the slide
**Catches** slides with one fact each, so the audience never sees two things
side by side. Tufte asks why slides run "at 2% of the data richness of
routine tables found in the sports section". When the point is a comparison,
show the comparison on one slide.
**Detected** low. Look for runs of slides that each carry one number from
the same set.

### deck-6 Slides about the deck
**Catches** kit-2 on slides: an agenda that lists the titles, "Thank you",
"Questions?", "Key takeaways" that repeat the slides. Each slide earns its
place by saying something.
**Detected** medium. A hint: search titles for agenda, overview, thank you,
questions, takeaways, summary.

### deck-7 Stock pictures and icons for evidence
**Catches** a photo of people at a laptop, a lightbulb icon, a handshake,
standing where evidence should be.
**Detected** low. Ask of every image: is it the real thing this slide is
about?

---

A project's design file, or the brief, wins over this pack.
