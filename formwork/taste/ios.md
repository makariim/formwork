# Taste pack: iOS

For iPhone and iPad apps. Use it with [`screens`](screens.md).

**Source.** Apple's Human Interface Guidelines, read on 2026-11-15 through the
JSON behind each page (`https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<page>.json`).
Seven pages were read: materials, color, buttons, typography, tab bars,
writing, charts. The page for each item is linked.

**This pack is short on purpose.** Only what was read is here. Layout,
navigation bars, toolbars, icons and SF Symbols, motion, app icons,
accessibility as a whole, and the rest of each long page beyond what was read:
NOT ESTABLISHED. Read those pages before adding an item for them.

The HIG is Apple's guidance for its platforms, and changes with each release.
Where a project targets an older system, its design file says so and wins.

The shape of each item is in [README.md](README.md). Taste is never a check.

---

### ios-1 Glass only on controls, and sparingly
**Catches** translucent glass used on content (cards, rows, backgrounds), or on
everything. HIG: "Don't use Liquid Glass in the content layer." "Use Liquid
Glass effects sparingly."
**Detected** medium. A hint: `.glassEffect(` or a `Material` background on
views inside a list or scroll view.
**Source** https://developer.apple.com/design/human-interface-guidelines/materials

### ios-2 One meaning per colour, and never colour alone
**Catches** the same colour meaning two things, and a state shown by colour
only. HIG: "Avoid using the same color to mean different things." "Avoid
relying solely on color to differentiate between objects, indicate
interactivity, or communicate essential information." Colours must work in
light, dark and increased contrast.
**Detected** low for meaning, medium for hard coded values. A hint: literal
RGB or hex values where a system or asset colour would adapt. HIG: "Avoid
hard-coding system color values in your app."
**Source** https://developer.apple.com/design/human-interface-guidelines/color

### ios-3 One or two prominent buttons per view
**Catches** several filled, tinted or glowing buttons competing on one screen
(see screens-2). HIG: "Keep the number of prominent buttons to one or two per
view." Every button has a hit region of at least 44 by 44 points.
**Detected** medium. A hint: count `.borderedProminent` and custom filled
button styles per screen.
**Source** https://developer.apple.com/design/human-interface-guidelines/buttons

### ios-4 Type the system can scale
**Catches** fixed point sizes that ignore Dynamic Type, text below the
minimum, light weights, and too many typefaces. HIG: default 17 pt, minimum
11 pt on iOS and iPadOS; "avoid light font weights"; "Minimize the number of
typefaces you use, even in a highly customized interface."
**Detected** high for fixed sizes and light weights. A hint:
`.font(.system(size:` with no scaling, `.ultraLight`, `.thin`, `.light`.
Then run the screen at the largest text size and look.
**Source** https://developer.apple.com/design/human-interface-guidelines/typography

### ios-5 Tabs for places, not actions
**Catches** a custom bottom bar, a tab that performs an action, tabs with no
labels, or a "more" tab. HIG: "Use a tab bar to support navigation, not to
provide actions." "Include tab labels to help with navigation." "Avoid
overflow tabs."
**Detected** medium. A hint: a custom `HStack` pinned to the bottom in place
of `TabView`; a tab whose selection opens a sheet.
**Source** https://developer.apple.com/design/human-interface-guidelines/tab-bars

### ios-6 Labels are verbs, not cute
**Catches** kit-2 in the interface. HIG: "When labeling buttons and links,
it's almost always best to use a verb." "just saying 'Send' often works
better than 'Let's do it!'" Say "tap", never "click", on a touch device.
**Detected** medium. A hint: list every button label; look for ones with no
verb, exclamation marks, or "click".
**Source** https://developer.apple.com/design/human-interface-guidelines/writing

### ios-7 The data leads the chart
**Catches** kit-1 in a chart: grid lines, labels and colour louder than the
marks, or a chart with no summary of what it shows. HIG: "you want the data
itself to be most prominent"; "Summarize the main message of your chart";
"use actual values in your descriptions."
**Detected** low.
**Source** https://developer.apple.com/design/human-interface-guidelines/charts
