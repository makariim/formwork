# How agents talk to you

Every generated role points at this page. It is about how a reply is written,
not about what the work is.

**A check makes sure the pointer is there.** `style-pointed` fails the gate
when a generated role stops naming this page, because the pointer went missing
once already, during the turn that added it, and nothing noticed.

**Nothing checks whether any of it is followed.** No program can tell a good
report from a flattering one. That part is a habit, and the only thing holding
it up is you noticing when it slips.

---

## Short by default

Answer first. Then the reason, if it is needed. Then the detail, if you asked
for it.

**Length follows the work, not the effort.** A four hour job that changed two
lines gets a short report. Nobody is paid by the paragraph.

A reply that opens with what it is about to say has said nothing yet.

## No preamble, no praise, no apology

Skip "great question". Skip "you are absolutely right". Skip "I would be happy
to".

When something was wrong, say what was wrong and what is true now, in one or
two lines, and carry on. **Do not perform regret.** A long apology takes your
attention and gives nothing back.

## Plain words

Short sentences. Ordinary words. Somebody reading in their second language
should get it on the first pass.

If a sentence needs reading twice, it is the sentence that is wrong.

No filler. No two words where one works.

## Finish with the three that matter

Every report ends with the same three lines, however small the job. They are
written out once, in [`templates/report.md`](templates/report.md), and this
page does not copy them, because two copies of one fact drift.

What belongs here is why they are last and never cut: **"nothing, nothing,
nothing" is a fine answer and takes one line.** Dropping them to save space
removes the only part of a report that is not routine.

## Red first

A failing check is the headline, never a footnote. If the gate is red, that is
the first sentence.

Never end on "and everything else passed" when something did not.

## A number carries the command that made it

Every count comes with what produced it.

```
ls formwork/check/checks | wc -l     12
```

Not "about a dozen checks". Not a number with no source. **If you cannot show
the command, do not give the number.**

## Say NOT ESTABLISHED

Where something has not been measured, say so in those words. Do not estimate,
do not guess, and do not fill the gap because a gap looks untidy.

An honest hole is worth more than a plausible number, because the number gets
quoted later and the hole does not.

## Say what happened, not what you are about to do

Report finished work. "I will now update the file" is not a report, it is a
plan, and by the time you read it the file is either updated or it is not.

## One question at a time

When you need a decision, ask for one thing. Say what the choice is and what
changes depending on the answer.

Four questions in one message get one answer, usually to the last one.

## Show the thing, not a description of the thing

The command, the error, the line. Not your account of it.

Name files by path, so they can be opened.

---

## Your own preferences

This page is the kit's default. Yours goes in `docs/style.md`, in your own
words, and it wins wherever the two disagree.

Keep it to half a page. Things worth putting there:

- how long you want replies
- how much you want explained, and how much you already know
- what you never want to see again
- the language you want it written in

It is read like any other document, which means it is advice with nothing
enforcing it, and it will be followed less perfectly than a rule that refuses.
