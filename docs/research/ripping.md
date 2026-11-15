# Ripping (getripping): motion and story principles

Research only, 2026-11-15. Nothing in the kit, any brief or `docs/standing.md`
was changed. Everything below was read without logging in anywhere. No video
was downloaded or played. Quotes are short and linked. No assets were copied.

**The picture first.** Ripping is not a motion design studio, and it is not a
fitness app. It is a paid tool that makes Instagram reels for people who sell
software. Its own reels are marketing videos about selling apps, and they are
made with its own reel styles. So its lessons come from two places: the
motion in its reel styles (seen as still frames), and the motion on its
website (read in its stylesheets and scripts). Both are good. Its story and
copy are sales copy, and most of that is not taste to copy (see "What not to
take").

Because it is not a fitness, nutrition or training app, the brief's
conditional section **"For the health app" is left out**. the health app still appears under
"For his apps".

---

## Who they are

- **Ripping**, at https://getripping.com. It pairs with Claude Code: "Claude
  does the thinking", and Ripping gives the data, a video studio and a posting
  feed. It requires Claude Code. Price on the page: $99 a month, and a $2,500
  a month done-for-you tier that is listed as full.
- It finds well performing reels in a niche, writes scripts, renders them in
  one of many styles (36 on the home page; the updates page adds dozens more
  in November 2026), posts them, scores them before posting, and turns winners
  into new reels.
- It has **no App Store app**. The phone version is the website added to the
  home screen. Source: the "Mobile app" section of https://getripping.com.
- The person behind it is **Ben Zogby**. The Instagram page
  https://www.instagram.com/getripping/ shows a verified account, 16.3K
  followers, bio "Built and Exited @highstrike" and "Helping Vibe-Founders
  Get Software Users". The page's own claims (an engine "trained on 40M
  winners", $8M revenue, an exit) are theirs. None of them was checked here:
  NOT ESTABLISHED.
- The release notes, https://getripping.com/updates, run from 0.1.0 on
  2026-10-16 to 0.4.57 on 2026-11-14. Young product, shipping daily.
- No YouTube, X, LinkedIn, TikTok, Dribbble or Behance account was found by
  web search. The site links to no social profile at all.

---

## What was seen, and how

| Source | How | What it gave |
|---|---|---|
| Home page | fetched the page, its three stylesheets and 27 script files with `curl`, then searched them | every keyframe, duration, easing and reduced motion rule on the site; how the carousels and the headline behave |
| Reel style posters | 8 still frames (JPG posters the home page itself shows before each preview plays) | what the reel styles look like at one moment |
| Instagram | public embed pages, `instagram.com/reel/<code>/embed/captioned/`, for 29 codes | captions and comment counts for 24 reels (5 returned nothing) |
| Updates page | fetched | how they describe their styles, captions and progress |
| Accessibility page | fetched | WCAG 2.2 AA named as a reference target; nothing about motion |

The numbers in this file come from these commands, run in the job's scratch
folder (`$CLAUDE_JOB_DIR/tmp/dl`):

```
curl -sL https://getripping.com -o index.html
# then each stylesheet and script listed in index.html
grep -o '@keyframes [a-zA-Z0-9_-]*' *.css | sort -u        # 30 keyframes in the shared sheets, 5 more inline
grep -o 'prefers-reduced-motion[^{]*' *.css | sort | uniq -c   # 8 reduce rules in the shared sheets
curl -sL https://www.instagram.com/reel/<code>/embed/captioned/   # one per reel code
```

---

## Their principles

Each one: where it was seen, what it looks like, why it works, how to apply
it. The first five come from the reel styles. The next six come from the
website's code.

### 1. The motion follows the words

**Where.** The style posters on https://getripping.com (Basic Motion, Saas
Scaler Light, Ledger Mint, News Desk), and release 0.4.57 on
https://getripping.com/updates: "video styles that move with your voice".

**What it looks like.** The caption is built word by word as it is spoken.
Words already said stay on screen in grey; the word being said now is bright
("And third **people**"). A new word arrives out of a blur: in the site's
looping demo (`k4-word` in the main stylesheet) a word starts at opacity 0,
4px blur, 10px low and 90% size, and is sharp after about half a second
(7% of a 7 second loop) on `cubic-bezier(.22, 1, .36, 1)`. The one word that
matters gets a highlighter box ("**100,000 users** happens", "We grew to
**2,400**"), and in one frame a cursor is clicking it.

**Why it works.** The eye always knows where to look. The thing that moves is
the thing being said, so motion and meaning are the same event.

**How to apply.** Make the moving element the one that carries the current
meaning: the word being said, the value that just changed, the step that is
now. Everything else holds still.

### 2. One idea, one picture

**Where.** The HeyGen Presenter poster (a leaking bucket), the Basic Motion
poster (a calendar of crossed out days above a locked "a dollar" button), and
the script checklist on the home page: "one idea per line".

**What it looks like.** Each beat of the script gets one literal picture of
its idea. Churn is a bucket with water pouring out of holes while a tap fills
it. A trial that converts nobody is a calendar of crossed days and a paywall
button. The picture is big, centred, and alone.

**Why it works.** The motion explains instead of decorating. A viewer with
the sound off still gets the point.

**How to apply.** Before animating, write the one sentence the animation must
say. If no picture says it, do not animate it.

### 3. Build the number in reading order, one part at a time

**Where.** The `k4-*` keyframes in the main stylesheet (a 7 second looping
chart demo), and the Saas Scaler and Ledger Mint posters.

**What it looks like.** The demo is a choreography on one shared clock, and
each part enters only after the last one has landed:

| Part of the 7 s loop | What moves |
|---|---|
| 14% to 30% | bars grow up from the bottom, overshoot to 108%, settle at 97% then 100% |
| 28% to 50% | the line draws itself (`stroke-dashoffset`) |
| 48% to 60% | the dot at the end appears, swells to 150%, settles to 100% |
| 52% to 58% | the key label lights up |
| 86% to 95% | everything leaves together, quickly |

In the posters the big number (100,000; 2,400) sits above a curve with
milestone dots at 10, 100 and 1,000. The bar race poster carries a small
label, "Values illustrative".

**Why it works.** It reads like a sentence: the frame, then the trend, then
where you are now, then what it means. Only one thing moves at any moment, so
a busy chart still feels calm. The "illustrative" label is the honest minimum
when the numbers are not real.

**How to apply.** Order the entrance the way a person reads the chart. Let
each part land before the next starts. Never animate made up data as if it
were real (kit-1); label it, or use real numbers.

### 4. The first second says the point

**Where.** The script checklist and hook guidance on https://getripping.com:
"Hook in 1 s", "A number up front", "Names the enemy", hook in the first 3
seconds. The sample score report advises cutting dead air sooner and teasing
the payoff early.

**What it looks like.** Reel captions are the claim itself: "Stop selling AI
tools. Sell the job." "Only 4 out of every 100 new apps make $10K a month."
No intro, no logo sting.

**Why it works.** Attention is decided at once. A slow opening loses people
before the point arrives.

**How to apply.** In an interface, the first frame of any transition should
already show the result's shape. No splash screens, no empty pauses before
content, no animation that delays the thing the person opened the screen for.

### 5. The same words on screen as spoken

**Where.** The script checklist: "keep the same words on screen". Release
0.4.43: captions "still show the exact script".

**What it looks like.** The caption is the script, word for word, not a
summary of it.

**Why it works.** Two versions of one message make the viewer compare them.
One version is calm. It is also what makes captions useful to people who
cannot hear the audio.

**How to apply.** A label that animates in says exactly what the voice,
notification or reply says. Do not paraphrase between layers.

### 6. Auto-play stops when nobody is watching, and for good once you take over

**Where.** The stages carousel ("Printing Money is Simple") in the script
`0ruj-ach0ikjv.js` and its inline styles.

**What it looks like.** Each stage stays for 7 seconds. A thin bar under the
stage fills from left to right over those 7 seconds (`scaleX` 0 to 1,
linear), so you can see when it will change. It moves to the next stage only
when the bar's animation ends. The bar runs only when all of these hold: at
least 35% of the carousel is on screen, the browser tab is visible, the mouse
is not over it, and it does not have keyboard focus. The moment a visitor
picks a stage, auto-play stops for the rest of the visit. With Reduce Motion
on there is no auto-play at all, and moving to a stage jumps instead of
scrolling smoothly. The style strip below it scrolls slowly (one loop takes
90 s), pauses on hover, and with Reduce Motion it stops and becomes a row you
scroll yourself.

**Why it works.** Motion spends attention. It stops when there is no
attention to spend, and it never fights the person once they have chosen.

**How to apply.** Anything that changes by itself shows its timer, pauses
when hidden, hovered or focused, and hands control over permanently on the
first touch.

### 7. Entrances play once, and never for what you have already seen

**Where.** The phone fan in the "Mobile app" section, same script.

**What it looks like.** Five phone screens start stacked behind the centre one
(1.5em low, 92% size). When the section scrolls 30% into view they fan out
over 1.1 s on `cubic-bezier(.22, 1, .36, 1)`, the centre first and each outer
phone 70 ms later per step away from the centre. The observer then
disconnects, so it never plays again. If the section is already in the top
80% of the window when the page loads, or Reduce Motion is on, the phones are
simply shown open. Hovering one lifts it 0.6em in 300 ms.

**Why it works.** An entrance is a story of arrival. Replaying it, or hiding
something the person can already see so it can arrive, is noise.

**How to apply.** Give an entrance only to things that really arrive. Play it
once. If the content is already in view, show it finished.

### 8. Reduced motion shows the finished frame that tells the story

**Where.** The eight reduce rules in the shared stylesheet and the two inline
ones.

**What it looks like.** With Reduce Motion on, the demo chart's line is shown
fully drawn, the words and dots are visible, the bars stand at full height,
and the progress bar is held at 60% so it still reads as "in progress". The
check mark is shown drawn. The rotating headline word does not rotate: the
script checks the setting before it ever starts the timer. Shimmer text
becomes plain text.

**Why it works.** Reduced motion is not a blank. Each animation has an end
frame that says the same thing standing still.

**How to apply.** For every animation, decide its still frame first: the
frame that tells the whole story with no movement. That is what Reduce Motion
shows.

### 9. Spend the physical moment in one place

**Where.** The home page headline, "Turn Instagram Into A Money Printer For
Your SaaS", inline styles `join-drop` and `join-knocked`, and the rotating
word script.

**What it looks like.** The last word of the headline changes every 1.5 s.
The new word drops in from above in 0.56 s: it falls with an accelerating
curve, squashes as it lands (105% wide, 86% tall), bounces up 9% while
stretching, and settles. The old word is knocked off: it falls down and tilts
6 degrees in 0.3 s. The headline's width eases to the new word's measured
width in 0.45 s, measured again after the fonts load, so the line never
jumps. Everywhere else on the site the motion is small and quiet: a 6px rise
over 0.5 s, steps in 0.28 s, tour cards 10px and 98% size in 0.35 s.

**Why it works.** One place has weight and character, so the rest can stay
still. The entry and exit are one physical story: the new word lands, the old
one falls away.

**How to apply.** Choose the one moment that earns physics, and keep every
other motion short and plain. The 1.5 s endless loop with a shine sweep is
too busy for a calm product; the idea to take is the single landing, not the
loop.

### 10. Progress and confirmation tell the truth

**Where.** Releases 0.4.34 and 0.4.35: "The progress bar follows completed
work rather than the clock." Release 0.4.46: reels "are never finished with
plain text cards". The `check-draw` and `check-pop` rules in the shared
stylesheet.

**What it looks like.** Progress moves only when work is done. A finished
step gets a check that draws its own stroke (0.35 s, ease out, 50 ms after
the step ends), with a small pop from 60% to 115% to 100% size.

**Why it works.** A progress bar on a timer lies, and people learn that. A
confirmation that draws itself at the moment of completion is felt, and it
is small enough to repeat.

**How to apply.** Tie every progress mark to real completed steps, never to
elapsed time. Confirm a finished act with one small drawn mark, on the frame
it finishes.

### 11. Arrive gently, leave quickly, move a short way

**Where.** The panel view transitions in the shared stylesheet, and the rise
and tour rules.

**What it looks like.** A panel slides in over 0.26 s on
`cubic-bezier(.2, .8, .2, 1)` and leaves in 0.18 s. Most entrances travel 6
to 16 pixels and start at 94% to 98% size, never from zero.

**Why it works.** Leaving is not news, so it should not take attention.
Short distances read as "settling", long ones as "travelling".

**How to apply.** Make exits shorter than entrances. Keep entrance distances
small. Start from near full size.

### What not to take

Their own site breaks several items in this kit's packs, and the reels lean
on sales tactics:

- Endless motion: shimmer sweeps on text and on a navigation item (3.8 s
  loop), pulsing dots and a breathing orb (web-5).
- Gradient text in headlines (web-3), and an orange button with a coloured
  glow (screens-2).
- Copy about the product and money ("Money Printer"), and "comment RIP"
  calls to action on most reel captions (kit-2): 18 of the 24 captions
  read ask the viewer to comment a keyword.
- A bounce curve in the shared sheet (`cubic-bezier(.2,.9,.3,1.4)`), used for
  small pops. Fine on a rare check mark, wrong as a default.

---

## For formwork

The kit's packs today cover looks. Motion appears only as one item, web-5
("Motion on everything"), and the ios pack lists motion as NOT ESTABLISHED.
Ripping's principles are general enough to be **a new `motion` pack** that
assumes `screens`, used beside `web` or `ios`. A sketch, written generically,
in the pack shape. This is a proposal for a brief, not a change.

| Id and name | Catches | Detected | A hint |
|---|---|---|---|
| motion-1 One thing moves at a time | several elements animating at once, so nothing leads | low | step the screen frame by frame; count moving elements per frame |
| motion-2 Motion carries the current meaning | animation on decoration while the changed value sits still | low | ask "what does this movement tell me?" for each one |
| motion-3 Reduced motion shows the finished frame | Reduce Motion that blanks, hides, or leaves a half drawn state | medium | every animation has a `prefers-reduced-motion` or Reduce Motion branch; look at that frame |
| motion-4 Auto-play yields | carousels, loops or tickers that run off screen, under the pointer or focus, or keep going after a touch | medium | search for intervals and infinite animations; check for visibility and intersection checks and a stop on first input |
| motion-5 Entrances play once | entrances that replay on every return, or hide content already in view so it can arrive | medium | scroll reveals without a "seen" flag or a disconnected observer |
| motion-6 Progress reports work, not time | progress bars and percentages driven by a clock | medium | progress tied to a timer, not to completed steps |
| motion-7 Charts build in reading order, from real data | all chart parts animating together, or animated numbers that are not real (kit-1) | low | watch the entrance; ask where each number comes from |
| motion-8 One physical moment | springs, bounce and squash used everywhere instead of at one rare moment | medium | count bounce curves and springs with overshoot; then ask which moment earns it |
| motion-9 Leave faster than you arrive | exits as slow as entrances, long travel, entrances from zero size | high for zero size, medium for the rest | `scale(0)`; exit duration equal to or longer than entry |
| motion-10 First frame shows the point | splash screens, intro sequences, pauses before content | low | time from open to the first useful content |

Where it fits otherwise:

- **web**: web-5 could gain motion-4's hint (no visibility or intersection
  check on auto-play) and motion-3's (a reduce branch that leaves nothing on
  screen).
- **ios**: nothing should be added until Apple's motion page in the Human
  Interface Guidelines is read, as the ios pack itself says.
- **deck**: motion-7 (build a chart in reading order) is already close to the
  deck pack's spirit and could be cited there.

Sources for the pack would be Ripping's site as read here, plus the public
motion references a brief chooses. As with every pack, none of this was
measured.

---

## For his apps

His rules: one moving thing at a time, no glow everywhere, motion that means
something, Reduce Motion respected. the desktop app is the chief of staff app on the
Mac, with its ink drop character, the notch and one chat. the health app is the
iPhone app for training and food, rooted at Today, with The Road, Capture,
kept days and weeks held, and no guilt.

**1. Motion follows the words.**
- the desktop app: while a reply streams, only the newest words carry the fade in; the
  drop's eyes track the line being written, then settle when the answer ends.
- the desktop app: the one status line is replaced in place with a short crossfade on
  a real phase change, never a spinner beside it.
- the health app: when the Coach's answer says "protein is 40 g short", that number
  in the ring or bar under the message lights once as the sentence reaches
  it.

**2. One idea, one picture.**
- the health app: a week held is a short path of seven marks; each kept day lands on
  it as it is kept. A comeback gets its own small mark, named in words.
- the desktop app: a reminder that is set moves once from the reply into its place in
  today's list, so the person sees where it went.

**3. Build the number in reading order.**
- the health app: on The Road, the weight trend draws, then today's dot settles, then
  the one hero number appears. Each lands before the next. Real numbers only.
- the desktop app: the weekly review counts closed items up once, after the list has
  appeared, never in parallel with it.

**4. The first second says the point.**
- the health app: opening the app shows Today with the next thing ready. No splash,
  no greeting animation before content.
- the desktop app: the first frame of a reply is the answer's first words; the
  thinking form appears only if the turn is slow.

**5. Same words everywhere.**
- the health app and the desktop app: the notification text, the Live Activity line and the
  in-app line are the same sentence.

**6. Auto-play yields.**
- the desktop app: the drop breathes only while a run works, pauses when the window or
  notch is hidden, and is still with Reduce Motion (already the rule in its
  handbook; keep it).
- the health app: the rest timer in the live workout is the progress ring itself, so
  the motion is the timer; it stops the moment he taps "next set".

**7. Entrances play once.**
- the health app: the morning reveal of Today plays once per day, not every time he
  returns to the screen.
- the desktop app: a card that persists across relaunch appears finished, not
  animated in again.

**8. Reduced motion shows the finished frame.**
- the health app: the weekly path shows all marks placed; rings show their final
  fill; a kept day shows its mark without the landing.
- the desktop app: the character holds its mood pose for the state (thinking, done,
  needs you); colour alone does not carry the state.

**9. One physical moment.**
- the health app: the only spring with a little bounce is a held week (weekly, rare),
  with one success haptic on the same frame. Daily logging stays plain.
- the desktop app: the "done" settle of the drop is the one moment with weight; every
  other change is a fade.

**10. Progress and confirmation tell the truth.**
- the health app: the medicine check draws only on the one named medicine he tapped,
  with one light haptic; never an "all taken" animation.
- the health app: a meal photo being read shows real steps (photo read, items found,
  numbers ready), not a timed bar.
- the desktop app: "Reminder set" draws a small check beside its Undo, once.

**11. Leave faster than you arrive.**
- the health app: Capture opens as a sheet that settles in, and closes faster than it
  opened.
- the desktop app: a dismissed card leaves in about two thirds of its entry time and
  travels a short way.

---

## What could not be seen

- **The reels as video.** No reel was played or downloaded, by the brief's
  rule. Only one still per style (8 posters on the home page) and the
  captions of 24 Instagram reels were seen. The motion between frames in the
  reels, the sound, the voice and the spoken script are NOT ESTABLISHED.
  Instagram offers no public transcript.
- **The 11 reels on the profile page** show only "Clip" without a login.
  Their captions were read only where the reel's code was also on the home
  page or in the profile's public embed (6 from the embed, 18 from the home
  page; 5 more codes returned nothing).
- **Story highlights** ("My Story", "Get Ripping", "Q/A") need a login. Not
  seen.
- **The app inside** needs an account. Its motion was read only as code in
  the shared stylesheet (the `k4-*` chart demo, tour cards, check marks,
  panel transitions). Where those appear in the app is NOT ESTABLISHED.
- **The other styles.** The home page lists 36 styles and the updates page
  adds about 50 more in November 2026, including voice reactive and 3D ones.
  Only 8 posters were seen.
- **Other platforms.** No YouTube, X, LinkedIn, TikTok, Dribbble or Behance
  presence was found by web search. That is not proof there is none.
- **Their claims** about views, revenue, followers and the "40M winners"
  engine were not checked.
