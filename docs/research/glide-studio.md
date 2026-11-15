---
date: 2026-11-15
by: a research session, from his words of 2026-11-15
source: theglide.studio (all six pages, its CSS and JS bundles, its two embedded videos), instagram.com/theglidestudio (eight public posts through Instagram's own embed pages)
---

# Glide: what a small motion studio teaches about calm, alive motion

## Who they are

Glide is a new web and motion studio for startups. It sells three things:
websites that move, short vertical motion-graphics reels, and launch films.
The site is a Next.js app with Motion (motion.dev) and plain CSS animation.
It has no client work yet. Its Work page shows three "studio studies" made
in code, and a free trial offers eight reels to each of four startups so the
first case studies can be made. The Instagram account had eight posts, all
dated 14 and 15 November 2026, and 168 followers when read. The look is near
black or soft white, one electric blue accent, a hand drawn single-line
logo with a blue dot.

What makes it worth studying is that **the site ships its own motion rules in
its code**: three named curves, four named durations, a stagger, and eight
rules in plain words. Every claim below comes from that file, from the
running pages, from the stills of their two films, or from their captions.

## Contradictions first

1. **Nothing here is proven on a client yet.** Every page, film and reel is
   Glide advertising Glide. The testimonial slot reads "Your words, here
   soon." The principles are stated and practised on their own work only.
2. **"Never bounce, spring or pop" is the stated rule, but the code bends
   it three times.** The apply form's card resizes with a spring
   (`type: "spring", duration: .6, bounce: .12`). The hero's blue dot drops
   in with a small settle (its keyframes go to `translateY(-.16em)` at 72%
   and back). A wrong field shakes (`x: [0, -9, 8, -5, 3, 0]` over 0.45 s).
   Read the rule as "no bounce for show", not "no physics ever".
3. **The site has loops that run forever while you look.** The free-trial
   previews loop every 4.8 s, the hero's floating pieces bob on a 7 s
   cycle, and a "now open" dot pulses every 2.4 s. formwork's `web-5`
   flags "a dot that pulses forever". Glide pauses all of them when they
   leave the screen and when Reduce Motion is on, which is the part to copy.
4. **Their exit curve is an ease-in.** `leave` is `cubic-bezier(.7,0,.84,0)`.
   The `animate` skill says never use ease-in on UI. The two agree in
   practice: Glide uses it only for things leaving, short (0.4 s on headline
   words), after the reader has finished with them.
5. **Their reveal is 700 ms; the `animate` skill caps UI at 300 ms.** Glide's
   700 ms is for words and pictures arriving on a marketing page, which the
   skill also allows to be longer. Their press is 160 ms, inside the skill's
   range. For app UI, keep the skill's numbers.
6. **The YouTube handle `@theglidestudio` is not theirs.** It belongs to a
   figure skating channel called "The glide". Only Instagram is linked from
   the site.

## How this was studied

| Source | What was reachable | How |
|---|---|---|
| theglide.studio: `/`, `/services`, `/work`, `/free-trial`, `/start`, `/privacy` | All text, all CSS, all JS bundles | fetched over HTTPS, read as text; `sitemap.xml` lists the same six pages |
| The site's motion rules | Full object of curves, durations, rules | read from the shared JS bundle (`chunks/998-*.js`) |
| `/work/glide-reel.mp4` (8.0 s, 9:16) | Watched as stills every 0.5 s (16 frames) | the file the home page plays in its own `<video>` tag; stills taken with macOS's built-in AVFoundation, no tool installed; nothing kept |
| `/work/glide-launch.mp4` (15.0 s, 16:9) | Watched as stills every 0.35 s (43 frames), plus the shot list in the site code | same |
| Seven Instagram reels | Full caption, hashtags, cover frame | Instagram's public embed page (`/reel/<id>/embed/captioned/`) |
| One Instagram carousel | Caption and the first slide | same |
| YouTube, TikTok, X, LinkedIn, Dribbble, Behance, Vimeo | Nothing of theirs | see "What I could not see" |

Durations below come from their CSS and JS. Timings inside the films come
from the still timestamps, so they are accurate to the sampling step (0.5 s
and 0.35 s), no better.

## Their motion system, as written in their code

From the site's shared bundle. Short quotes, their words:

| Token | Value | Their use |
|---|---|---|
| `glide` | `cubic-bezier(.65,0,.35,1)` | "The house curve: anything that travels from one place to another" |
| `arrive` | `cubic-bezier(.16,1,.3,1)` | "come in fast and settle slowly, never bouncing" |
| `leave` | `cubic-bezier(.7,0,.84,0)` | "they ease out of the way and go" |
| `press` | 160 ms | "A press, a hover, a toggle." |
| `reveal` | 700 ms | "Words and pictures arriving." |
| `scene` | 1200 ms | "a section assembling, the mark drawing itself" |
| `logo` | 2000 ms | the logo writing itself |
| `stagger` | 60 ms | between siblings |

And eight rules, in their order (paraphrased where long):

1. "Things glide; they never bounce, spring or pop."
2. "One idea per move. If two things move, one leads and one follows."
3. Every section has its own motion, tied to what it says. "No fade-up on everything."
4. "The blue moves last: it lands where the eye should end."
5. "Text holds still long enough to read on a phone."
6. "Motion runs only while it is on screen."
7. Scroll is smooth on computers; "phones keep their own feel."
8. Anyone whose device asks for less motion sees "a calm, still site."

All from https://theglide.studio (the rules are in the page's code, not in its visible text).

## Their principles

Each principle: where it was seen, what it looks like, why it works, how to
apply it.

### 1. Motion explains; it never decorates

- **Where.** The home page's big statement, "Motion that explains, not motion
  that decorates" (https://theglide.studio). Rule 3 above.
- **What it looks like.** As the statement scrolls in, a hand drawn line
  writes itself *under* "explains" and *through* "decorates". The motion is
  the argument: one word is underlined, the other struck out. On Services,
  each of the three offers has its own small demo (a page, a phone reel, a
  film strip) instead of a shared entrance.
- **Why it works.** A viewer reads motion as cause. If a thing moves, they
  expect it to mean something. Motion that means nothing is noise they learn
  to ignore, and then they miss the motion that matters.
- **Apply.** Before animating, write the one sentence the motion says ("this
  card became that page", "this was struck out"). No sentence, no motion.

### 2. Three curves, each with one job

- **Where.** The tokens above; every CSS keyframe and Motion transition on
  the site uses one of them.
- **What it looks like.** Things that travel across the screen speed up and
  slow down evenly (`glide`). Things entering shoot in and take their time to
  settle (`arrive`). Things leaving start slowly and then go (`leave`).
  Headline words rise into place over 0.55 s with `glide`, 24 ms apart, and
  leave upward in 0.4 s with `leave`, 16 ms apart: the exit is faster and
  tighter than the entrance.
- **Why it works.** A small, named set makes everything feel made by one
  hand. Matching the curve to the job means the eye is never surprised:
  arrivals land softly where the eye is going, exits get out of the way.
- **Apply.** Name your curves by job, not by shape (`travel`, `arrive`,
  `leave`), and forbid any curve not on the list. Make exits shorter than
  entrances.

### 3. A few named durations, short for touch, longer for telling

- **Where.** The duration tokens. The reel "One second too long" says a good
  motion is over as you notice it; their rule: "a press takes a blink, a
  reveal under a second" (https://www.instagram.com/reel/Dfvja0XCyIi/).
- **What it looks like.** Buttons and toggles respond in 160 ms. Words
  arrive in 0.55 to 0.7 s. Whole scenes take 1.2 s. Only the logo is
  allowed 2 s.
- **Why it works.** Too slow and people wait for the interface; too fast and
  they lose where something came from. Four sizes cover every case and stop
  guessing.
- **Apply.** Pick three or four durations and give each a sentence of use.
  For app UI keep the press near 150 ms and travel under about 350 ms; keep
  the longer ones for first runs, onboarding and marketing.

### 4. One idea per move: one leads, one follows

- **Where.** Rule 2. Both films.
- **What it looks like.** In the 8 s reel nothing moves except one shape and
  the dot riding on it. The dot draws a line, the line becomes a browser
  frame, the frame becomes a phone, the phone becomes a landscape film
  frame, then everything collapses back to the dot. The headline changes
  only between moves, never during one. In the launch film the dot moves
  first and the line follows behind it, like a pen tip and its ink.
- **Why it works.** The eye can track one thing. When two things move at
  once with equal weight, the viewer has to choose, and usually chooses
  wrong. A leader and a follower read as one gesture.
- **Apply.** Per moment, name the one thing that moves. If something else
  must move, delay it so it follows, and make it smaller or dimmer.

### 5. The accent moves last and lands where the eye should end

- **Where.** Rule 4. The logo study on `/work` ("the blue dot leading as the
  pen tip, then it lands on the i"). The colour notes call electric blue
  "The one accent... One thing per screen."
- **What it looks like.** The logo's line writes "glide"; the blue dot is
  the last thing to settle, dropping onto the i. In the hero the dot falls
  in 0.75 s after the page starts, then one ring spreads from it once. In
  the launch film the call to action button appears only after the dot
  lands. On their cover frames the only blue is the full stop at the end of
  the headline.
- **Why it works.** The last thing to stop moving is where attention rests.
  Ending on the accent hands the viewer to the one place that matters.
- **Apply.** Choose the resting place of each sequence first (the result,
  the button, the number). Make it the last thing to settle and the only
  accented thing on screen.

### 6. One continuous thread carries you between states

- **Where.** "Follow the line" (https://www.instagram.com/reel/DfvanLxhZnb/):
  a line becomes a website, then a reel, then an offer. "Don't lose the
  circle" (https://www.instagram.com/reel/DfvsSxzMWIz/): one circle becomes a
  button, a face, a loading ring and a full stop. "Where did the page go?"
  (https://www.instagram.com/reel/DfwhC1riuuO/): "the card becomes the page,
  and back goes back."
- **What it looks like.** The launch film has no hard cuts. A line leaves
  the page's button, runs under it, draws the chart's curve, flips a toggle
  as it passes, wraps the page, draws out a phone frame and a film frame,
  then pulls free and writes the logo. The cover of the "page" reel shows a
  product card growing into a full screen.
- **Why it works.** A hard cut makes people rebuild the scene from nothing.
  If one element survives the change, they keep their place and understand
  the new state as a version of the old one.
- **Apply.** For each change of screen or state, pick the element that
  survives it (the tapped card, the number, the dot) and move it, rather
  than fading one screen out and another in. Going back runs the same path
  in reverse.

### 7. Show what invisible software does, in three moves

- **Where.** "You can't photograph software"
  (https://www.instagram.com/reel/DfvR2x7CLUH/): software has no shape, so
  show what it does; their example is a message that leaves, is checked, and
  arrives. The cover frame shows a dotted path, a tick in a circle, and the
  blue dot in a focus frame.
- **What it looks like.** An abstract path with three stops: start, check,
  arrive. No screenshot.
- **Why it works.** Three moves is enough for a stranger to follow cause and
  effect, and few enough to remember. Abstract shapes survive a small phone
  screen where a real interface turns to mush.
- **Apply.** When a background process matters to the user (a sync, a
  check, a send), give it a tiny three-beat story: it left, it was handled,
  it arrived. Then stop.

### 8. Edit the demo: keep what matters, big, and let a pointer lead

- **Where.** "A screen recording is not a product demo"; "Keep only what
  matters. Make it big enough for a phone. Let a cursor lead."
  (https://www.instagram.com/reel/Dfv1BkEO_YT/). The `/work` study "An
  interface, assembled" builds a screen piece by piece.
- **What it looks like.** The cover puts a tiny unreadable desktop recording
  beside one big phone card ("Book a call", a few dates, one button) with
  the blue dot as the cursor. On the home page a small cursor glides across
  the hero, presses (scales to 0.86), and returns on a 9 s loop.
- **Why it works.** A recording shows everything, so nobody sees anything.
  Cutting to the one control, at a size that reads, makes the action
  legible.
- **Apply.** Onboarding and help should show one control at a time, large,
  with a single moving pointer or highlight that leads the eye to it.

### 9. Text holds still long enough to read

- **Where.** Rule 5. Both films.
- **What it looks like.** The launch film opens with 2.65 s where nothing
  moves: "Most pages sit still." next to a still product page. It ends with
  the logo and the button held still for about 2.5 s. In the reel each
  headline stays fixed for about a second before the next move. The hero's
  rotating word waits 3.4 s the first time and 2.8 s after.
- **Why it works.** Stillness is what gives motion its meaning. A held frame
  is where reading happens; constant motion is unreadable on a phone.
- **Apply.** Around every motion, budget a hold. After anything with words
  arrives, nothing else moves until it could have been read.

### 10. Design the still frame first

- **Where.** Their process: "Look: Still frames, for your yes," then
  "Motion: Every frame set gliding" (https://theglide.studio). The Services
  page repeats it: the pages are approved still before motion. The
  carousel "Steal our brief" asks three questions, the last being "What
  should they feel?" (https://www.instagram.com/p/Dfuw1KVjiJp/).
- **What it looks like.** Every cover frame of their reels works as a
  poster on its own. Their brief has a field called "The one feeling".
- **Why it works.** If the rest state is right, motion only has to connect
  good states. If the rest state is wrong, no motion saves it. Naming one
  feeling gives every motion decision a test.
- **Apply.** Review each screen as a still first. Write the one feeling the
  product should leave, and judge each motion against it.

### 11. Motion runs only while it is seen, and stops for those who ask

- **Where.** Rules 6 and 8. Services lists "A calm, still version for anyone
  whose device asks for less motion" as part of what a client gets.
- **What it looks like (from the code).** Each animated section is watched
  with an IntersectionObserver; when it leaves the screen it gets
  `data-live="false"` and its loops get `animation-play-state: paused`.
  Videos do not load until they are a screen away. With Reduce Motion on, a
  global rule sets every transition and animation to 0.001 ms; the
  variable font study shows a fixed weight; the running timecode stops; the
  films show a still poster and a play button instead of autoplaying.
- **Why it works.** Motion nobody sees still costs battery and attention.
  The reduced version is designed, not just switched off, so the page still
  makes sense.
- **Apply.** Every loop pauses off screen or when the window is in the
  background. For every motion, decide its still form at the same time:
  what the user sees instead, not just "nothing".

### 12. Respect the platform's own feel

- **Where.** Rule 7: smooth scroll on computers, "phones keep their own
  feel." The hero's pointer parallax listens only to a pointer.
- **What it looks like.** No scroll hijacking on touch. Hover effects only
  for mouse pointers (`pointerType === "mouse"`).
- **Why it works.** People's hands know how their device scrolls. Changing
  it reads as broken, however pretty.
- **Apply.** Never replace native scrolling, sheets or back gestures with
  custom motion on phones. Add motion around them, not instead of them.

## For formwork

These are written generically, in the taste pack shape. **Nothing below has
been added to any pack.** A brief decides that.

**Recommendation: a new `motion` pack**, used with `screens` and with `web`
or `ios`. Motion is shared by web and iOS and does not fit either alone;
`web-5` would point to it. Taste stays a reviewer's call, never a check.
Candidate items:

- **motion-1 Motion with no sentence.** *Catches* motion that cannot be
  said in one sentence of what it shows (came from, became, was removed,
  is happening). *Detected* low: ask the sentence for every animation.
  *Source* Glide's home page and rule 3.
- **motion-2 Two things moving with equal weight.** *Catches* a moment where
  two or more elements move at once and neither leads. One moves; anything
  else follows later and smaller. *Detected* low: watch at half speed and
  count. *Source* Glide rule 2.
- **motion-3 The accent does not land last.** *Catches* a sequence that ends
  on something other than its point, or an accent colour on more than one
  moving thing. *Detected* low. *Source* Glide rule 4.
- **motion-4 A hard cut where something could carry over.** *Catches* a
  screen or state change that fades everything out and in when one element
  (the tapped card, the number) could travel; and a back action that does
  not reverse the path. *Detected* medium: a hint is a navigation with no
  shared-element transition (`matchedGeometryEffect`,
  `navigationTransition(.zoom...)`, View Transitions on the web). *Source*
  Glide reels "Where did the page go?" and "Don't lose the circle".
- **motion-5 Curves and durations with no names.** *Catches* easing and
  timing values written inline, more than three or four of each, so the
  product has no single hand. *Detected* high: count distinct
  `cubic-bezier`, `timingCurve` and duration literals. *Source* Glide's
  tokens.
- **motion-6 Words that move while they should be read.** *Catches* text that
  is still moving, or followed at once by other motion, before it could be
  read. *Detected* low. *Source* Glide rule 5.
- **motion-7 Loops nobody is watching.** *Catches* an animation that runs
  forever, or keeps running off screen or in the background. Ambient motion
  pauses when unseen. *Detected* medium: `infinite`, `repeatForever`, timers,
  with no visibility or scene-phase check. *Source* Glide rule 6; the pulse
  half is already `web-5`.
- **motion-8 A reduced version that is only "off".** *Catches* Reduce Motion
  handled by deleting motion with no designed still state, or not handled
  at all. Reduced means fades and holds, not broken layouts. *Detected*
  high for missing handling (`prefers-reduced-motion`,
  `accessibilityReduceMotion`), low for quality. *Source* Glide rule 8 and
  their Services list; WCAG 2.2 2.3.3.
- **motion-9 Custom motion that replaces the platform's.** *Catches*
  scroll, sheet or back gestures replaced by custom motion on touch devices.
  *Detected* medium. *Source* Glide rule 7.

**Smaller edits to existing packs**, if a brief wants them:

- `web-5` could cite Glide's code as the good counterexample: loops are
  fine only when paused off screen and when reduced motion is set.
- `screens-2` ("one soft light per screen") pairs with motion-2 and
  motion-3: one light, one mover, one accent, ideally the same thing.
- `ios` still lists motion as NOT ESTABLISHED. Glide is not Apple; motion
  items for `ios` should still wait for the HIG motion page to be read.

**A tension to settle in the pack, not here.** Glide says glide curves and
never springs; the `apple-design` skill says springs for anything a finger
touches. They do not really conflict: curves for motion the product starts
(a reveal, a hand-off, a story), springs for motion the user drives (drag,
flick, dismiss), because a spring keeps the finger's speed. Glide's own form
card uses a nearly flat spring (bounce 0.12) for a size change.

## For his apps

His rules for both: one moving thing at a time, no glow everywhere, motion
that means something, Reduce Motion respected. the desktop app is the Mac notch
companion ("gentle motion all day, real reactions, rare words, playful when
clicked"; the notch moves less than the floating one). the health app is the iPhone
training and nutrition app with a Coach and a Nutritionist, near-black, raised
cards, soft glow and smooth motion welcome.

In SwiftUI, Glide's three curves are
`.timingCurve(0.65, 0, 0.35, 1, duration:)` (travel),
`.timingCurve(0.16, 1, 0.3, 1, duration:)` (arrive) and
`.timingCurve(0.7, 0, 0.84, 0, duration:)` (leave). Reduce Motion is
`@Environment(\.accessibilityReduceMotion)`. Durations below are starting
points to feel-check on a device, not measured values.

**1. Motion explains.**
- the desktop app: the notch moves only when something changed for the user (a
  summary is ready, a task finished, a reminder is due). No idle motion
  that says nothing; its "alive" comes from reacting, not from breathing
  forever.
- the health app: when a logged meal changes the day's totals, the number that
  changed is the one that moves. Unchanged rings and cards stay still.

**2. Three curves, named by job.**
- Both apps: one shared `Motion` file with `travel`, `arrive`, `leave` and
  three durations (about 0.15 s press, 0.3 s travel, 0.6 s for rare scenes).
  No inline curves anywhere else.
- the desktop app: the notch expanding uses `arrive`; collapsing uses `leave`,
  shorter, so it gets out of the way of the user's work fast.

**3. Short for touch, longer for telling.**
- the health app: set logging buttons and checkmarks answer in about 0.15 s. Only
  the end-of-workout summary, seen once a session, gets a longer scene.
- the desktop app: clicks on the notch answer at once; the playful reaction "when
  clicked" is the rare-tier delight and can take longer, because it is rare.

**4. One leads, one follows.**
- the desktop app: when an answer arrives, the companion reacts first, then the text
  follows 60 to 100 ms behind, smaller. Never both at once.
- the health app: when the Coach suggests a change, the suggestion card arrives; the
  affected exercise row updates only after, as a follower.

**5. The accent lands last.**
- the health app: the workout complete moment ends on one accented number (the
  personal best, the volume), the last thing to settle. Nothing else on the
  screen carries the accent or the soft glow.
- the desktop app: the morning sentence writes in, and the one action in it (the
  thing that needs the user) is the last element to settle and the only
  coloured one.

**6. One continuous thread.**
- the health app: tapping a meal or exercise card grows that card into its detail
  screen (`matchedGeometryEffect` or the zoom navigation transition); back
  shrinks it into the same place.
- the desktop app: the floating companion and the notch are the same character. When
  it docks, it travels into the notch rather than vanishing in one place and
  appearing in another.
- the desktop app: a Claude Code question that the user answers from the notch
  shrinks back toward the thread it came from, so the user sees where the
  answer went.

**7. Invisible work in three beats.**
- the desktop app: a background AI task shows three quiet beats in the notch:
  started, working (one slow mark, not a spinner loop), done. Then still.
- the health app: syncing with Health or saving a plan: sent, checked, saved, as one
  small mark that changes shape three times, then rests.

**8. Edit the demo.**
- the health app onboarding: one control per step, shown large, with one moving
  highlight leading to the button. No screen recordings in the app or the
  App Store preview; build the preview from the real screens, cut down.
- the desktop app onboarding (bringing in a subscription or an API key): one field
  at a time, with the companion pointing at it.

**9. Text holds still.**
- the desktop app: a summary that arrives in the notch holds still until it could be
  read; no new motion in the notch during that time.
- the health app: Coach and Nutritionist replies arrive, then hold. No shimmer or
  pulse on text the user is reading.

**10. Still frame first.**
- Both: review each screen's resting state in the render gallery before
  adding any motion (the health app already renders motion strips of a view at
  several progress values; the first and last frames of each strip must
  pass as stills).
- Both: write each app's one feeling at the top of its design file, and
  judge every motion against it.

**11. Run only when seen; designed reduced version.**
- the desktop app: its ambient motion pauses when the Mac is idle, the screen is
  locked, a full screen app is in front, or the notch is hidden. With
  Reduce Motion on, reactions become a short cross-fade or a still
  expression change, and docking becomes a fade in place.
- the health app: anything looping (a timer ring, a rest countdown) pauses when the
  app goes to the background (`scenePhase`). With Reduce Motion, card
  growth becomes a cross-fade and number changes become a plain swap.

**12. Platform feel.**
- the health app: keep native sheets, scroll and the back swipe; motion goes around
  them. Drag to dismiss uses a spring that keeps the finger's speed (the
  `apple-design` rule), not a glide curve.
- the desktop app: notch behaviour should feel like the system's own Mac notch and
  menu bar, never like a web page placed in it.

## What I could not see

- **The Instagram reels in motion.** Seven reels were studied from their
  captions and cover frames only. Instagram's public embed page shows a
  still poster and no video, and getting the video would need a login or a
  download tool. I did neither. So for these, timing, easing and sound are
  unknown. Reels: DfvR2x7CLUH, DfvanLxhZnb, Dfvja0XCyIi, DfvsSxzMWIz,
  Dfv1BkEO_YT, DfwhC1riuuO, DfwrVXTBD-G.
- **The carousel past slide one.** The embed exposed only the first slide
  of "Steal our brief"; the rest is known from the caption.
- **Sound.** Both site films were watched as stills; sound was not studied.
  Their Services page says sound "follows the motion".
- **Motion between stills.** Film timings are only as fine as the sampling
  step (0.5 s for the reel, 0.35 s for the launch film). Curves inside the
  films are not established; curves on the site are, from its code.
- **The site as a running page.** No browser was driven, so scroll-linked
  effects (the stretching type study's width 75 to 100 and weight 400 to
  700, the hero's fade and 140 px drift as you scroll) are read from code,
  not watched.
- **Other platforms.** TikTok returned only a script shell with nothing
  readable. LinkedIn returned 403 (login wall). X, Dribbble, Behance and
  Vimeo returned 404 for the handle. YouTube `@theglidestudio` is someone
  else's channel. No other public account is linked from the site.
- **Whether the principles work for clients.** Glide has no published client
  work yet.

Nothing from Glide (images, video, code, logo) was copied into this
repository. The stills were looked at in a temporary folder.
