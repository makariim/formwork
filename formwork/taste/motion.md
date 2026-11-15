# Taste pack: motion

For anything that moves: transitions, entrances, loops, progress, charts that
build, captions in a video. Use it with [`screens`](screens.md), and beside
[`web`](web.md) or [`ios`](ios.md). Motion is shared by the web and by phones
and fits neither pack alone.

**Sources.** Two small studios' public sites and reels, read on 2026-11-15.
Each item links the page it comes from.
- Glide, a web and motion studio. Its site ships its own motion rules in its
  code (named curves, named durations, eight rules), and its reels explain
  them: https://theglide.studio
- Ripping, a tool that makes short vertical videos. Its site's stylesheets
  and scripts, its release notes and its reel styles:
  https://getripping.com and https://getripping.com/updates
- WCAG 2.2, for reduced motion and captions: https://www.w3.org/TR/WCAG22/

Neither studio is proven on a client, and both break their own rules in
places. The items keep the rule, not the studio's look. Nothing here was
measured in this kit.

The shape of each item is in [README.md](README.md). **Taste is never a
check.** Motion is judged by a person watching a recording, in a review round
(`formwork/templates/review-round.md`). Every search pattern below is a hint
for that person, never a gate.

---

## How to look at motion

1. **The still frame first.** Look at the screen at rest before any motion.
   Then look at the first and last frame of each animation as stills: each
   must pass the `screens` pack on its own. If the rest state is wrong, no
   motion saves it. (Glide's process approves still frames before any
   motion: https://theglide.studio)
2. **Then the recording.** Watch it at full speed once, as a user would.
   Then at half speed, or frame by frame, and count what moves.
3. **Then with reduced motion on.** The same screen with the system setting
   for less motion turned on (motion-15).
4. **Report by id**, as with every pack: `motion-2, the checkout: the total
   and the button move together`.

---

## What the motion says

### motion-1 Motion with no sentence
**Catches** an animation that cannot be said in one sentence of what it
shows: this came from there, this became that, this was removed, this is
happening now. And motion on decoration while the thing that changed sits
still. The moving element should be the one carrying the meaning right now:
the value that changed, the step that is current, the word being said.
**Detected** low. Ask for the sentence, for every animation. No sentence, no
motion.
**Source** Glide's home page, "Motion that explains, not motion that
decorates", and its rule against a fade up on everything
(https://theglide.studio). Ripping's reel styles, where the word being
spoken is the one that moves (https://getripping.com, release notes at
https://getripping.com/updates).

### motion-2 Two things moving with equal weight
**Catches** a moment where two or more elements move at once and none
leads, so the eye does not know where to go. One thing moves; anything else
follows later and smaller, or holds still.
**Detected** low. Watch at half speed, or step frame by frame, and count the
moving elements in each frame.
**Source** Glide's rule "One idea per move. If two things move, one leads
and one follows." (https://theglide.studio). Ripping's chart demo, where
only one part moves at any moment (https://getripping.com).

### motion-3 The accent does not land last
**Catches** a sequence that ends on something other than its point, or the
accent colour on more than one moving thing. The last thing to settle is
where the eye stays, so it should be the point. Pairs with `screens-2` (one
soft light) and `screens-8` (one accent): one light, one mover, one accent,
ideally the same thing.
**Detected** low.
**Source** Glide's rule that its accent colour moves last and "lands where
the eye should end" (https://theglide.studio).

### motion-4 A hard cut where something could carry over
**Catches** a change of screen or state that fades everything out and in
when one element (the tapped card, the number, the dot) could travel and
become the new state. And a back action that does not run the same path in
reverse. A hard cut makes the user rebuild the scene from nothing.
**Detected** medium. A hint: a navigation with no shared element
transition. On the web, the View Transitions API; in SwiftUI,
`matchedGeometryEffect` or a zoom navigation transition. A person decides
whether anything should have carried over.
**Source** Glide's reels "Where did the page go?"
(https://www.instagram.com/reel/DfwhC1riuuO/), "the card becomes the page,
and back goes back", and "Don't lose the circle"
(https://www.instagram.com/reel/DfvsSxzMWIz/).

---

## One hand

### motion-5 Curves and durations with no names
**Catches** easing and timing written inline, with more than three or four
distinct values of each, so the product has no single hand. A good set is
small and named by job, not by shape (for example travel, arrive, leave;
press, reveal, scene), and nothing outside the set is used.
**Detected** high. A hint: count the distinct `cubic-bezier(`,
`timingCurve(`, spring parameters and duration literals across the code.
Many distinct values, or values written outside one motion file, is the
candidate.
**Source** Glide's motion tokens, three named curves and four named
durations, read from its site's code (https://theglide.studio).

### motion-6 Exits as slow as entrances, and long journeys
**Catches** an exit that takes as long as the entrance, an entrance that
travels far across the screen, or one that grows from zero size. Leaving is
not news and should get out of the way. Short distances read as settling;
long ones read as travelling, and should mean travel.
**Detected** high for growing from zero (`scale(0)`, `scaleEffect(0)`),
medium for the rest: an exit duration equal to or longer than its entrance.
**Source** Glide's headline, where words leave faster and tighter than they
arrive (https://theglide.studio). Ripping's panels, which arrive in about a
quarter second and leave faster, from near full size, a few pixels away
(https://getripping.com).

### motion-7 Physics everywhere, or a curve under the finger
**Catches** bounce, spring overshoot and squash used as the default for
everything, so nothing feels weighted. And the opposite: a fixed curve on
motion the user drives with a finger (drag, flick, dismiss), where it drops
the finger's speed. The rule that settles both: curves for motion the
product starts (a reveal, a hand off, a story); springs for motion the user
drives, because a spring keeps the finger's speed; and at most one rare
moment that earns visible physics.
**Detected** medium. A hint: count the bounce curves (`cubic-bezier`
control points past 1) and the springs with visible overshoot, then ask
which one moment earns it. For gestures, look for a drag that ends in a
timed animation.
**Source** Glide's rule "Things glide; they never bounce, spring or pop",
which its own form bends with a nearly flat spring for a size change
(https://theglide.studio). Ripping's headline, one word that lands with
weight while everything else on the page stays small and quiet
(https://getripping.com). `web-5` already catches bounce as a default.

---

## Words and numbers

### motion-8 Words that move while they should be read
**Catches** text that is still moving, or is followed at once by other
motion, before it could have been read. Shimmer or pulse on text someone is
reading. After words arrive, nothing else moves until they could be read.
**Detected** low. Watch the recording and read along. If you cannot finish
the line before the next motion, it is a finding.
**Source** Glide's rule "Text holds still long enough to read on a phone."
(https://theglide.studio).

### motion-9 Captions that say it differently
**Catches** for video, voice or anything spoken: on screen words that
summarise or paraphrase what is being said, so the viewer compares two
versions. In an interface: a label that animates in with different words
from the notification, voice or reply it belongs to. Same words, one
version.
**Detected** low. Play it with sound and read along.
**Source** Ripping's script checklist, "keep the same words on screen", and
release notes saying captions "still show the exact script"
(https://getripping.com, https://getripping.com/updates). WCAG 2.2, 1.2.2
Captions (Prerecorded).

### motion-10 A slow first second
**Catches** an opening that delays the point: a splash screen, a logo
sting, an intro sequence, an empty pause before content, a transition that
holds back the thing the person opened the screen for. The first frame
should already show the shape of the result.
**Detected** low. A hint: time from opening to the first useful content, on
the recording.
**Source** Ripping's hook guidance, "Hook in 1 s" and "A number up front"
(https://getripping.com).

### motion-11 A number built all at once, or from nothing real
**Catches** a chart whose parts all animate together, so it reads as noise.
A chart that builds should build in reading order, one part landing before
the next starts: the frame, then the trend, then where you are now, then
what it means. And an animated number or chart that is not real data
(kit-1); if it must be made up, it says so on screen.
**Detected** low. Watch the entrance; ask where each number comes from.
**Source** Ripping's chart demo, built part by part on one shared clock,
and its sample chart labelled "Values illustrative" (https://getripping.com).
kit-1 in [README.md](README.md).

---

## Attention

### motion-12 Entrances that replay, or hide what was already seen
**Catches** an entrance that plays again every time the user returns, or
content already in view that is hidden so it can arrive. An entrance is a
story of arrival; it plays once, and only for things that really arrive.
Content already on screen when the page opens is shown finished.
**Detected** medium. A hint: scroll reveals with no "seen" flag, or an
intersection observer that is never disconnected.
**Source** Ripping's phone fan, which plays once, disconnects its observer,
and shows itself open if it is already in view (https://getripping.com).

### motion-13 Loops nobody is watching, and auto-play that will not yield
**Catches** an animation that runs forever, or keeps running off screen or
in the background. Anything that changes by itself (a carousel, a ticker,
a rotating word) and does not show its timer, pause when hidden, hovered or
focused, or stop for good once the user picks something. Motion spends
attention; it stops when there is none to spend, and never fights a choice.
**Detected** medium. A hint: `infinite`, `repeatForever`, intervals and
timers with no visibility, intersection or scene phase check, and no stop
on first input.
**Source** Glide's rule "Motion runs only while it is on screen."
(https://theglide.studio). Ripping's stages carousel, which runs only when
visible, unhovered and unfocused, shows a filling bar for its timer, and
stops for the visit once a stage is picked (https://getripping.com). The
pulse half is already `web-5`.

### motion-14 Progress that follows the clock
**Catches** a progress bar or percentage driven by elapsed time rather than
completed work. People learn that a timed bar lies. Confirm a finished step
with one small mark, on the frame it finishes.
**Detected** medium. A hint: progress set from a timer or a fixed duration
animation, not from completed steps.
**Source** Ripping's release notes: "The progress bar follows completed
work rather than the clock." (https://getripping.com/updates).

---

## Everyone, and the platform

### motion-15 A reduced version that is only "off"
**Catches** reduced motion handled by deleting the motion with nothing
designed in its place (a blank, a hidden element, a half drawn chart), or
not handled at all. Each animation has a still frame that tells the same
story: the line drawn, the check shown, the bar held at a value that still
reads as "in progress". Reduced means that frame, fades and holds, never a
broken layout.
**Detected** high for missing handling: no `prefers-reduced-motion` rule on
the web, no `accessibilityReduceMotion` read in SwiftUI. Low for quality:
look at the screen with the setting on.
**Source** Glide's rule that a device asking for less motion sees "a calm,
still site" (https://theglide.studio). Ripping's reduce rules, which show
each animation's finished frame (https://getripping.com). WCAG 2.2, 2.3.3
Animation from Interactions.

### motion-16 Custom motion that replaces the platform's
**Catches** scroll, sheets, the back gesture or pull to refresh replaced by
custom motion, most of all on touch devices. Motion goes around the
platform's own behaviour, not instead of it.
**Detected** medium. A hint: smooth scroll libraries active on touch, a
custom sheet or a custom back swipe in place of the system one.
**Source** Glide's rule that scroll is smooth on computers while "phones
keep their own feel" (https://theglide.studio). See also `screens-6`.

---

## What this cannot do

Watch the motion. No program here plays a recording. Every item needs a
person, and a recording, or the real thing on a device.

Say a duration is right. The sources give starting points, not measured
values. Feel them on the real device.

Speak for Apple. `ios` still lists motion as NOT ESTABLISHED until Apple's
motion page in the Human Interface Guidelines is read. Where that page and
this pack disagree, the platform wins.
