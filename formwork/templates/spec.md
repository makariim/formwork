# Spec

Optional. For a new product, or a big change to one. One page, written from
the person's own words, read by them before anything is built.

It is an ordinary brief's output: the brief asks for this page, the report
carries it, and the person's read-back accepts it. Give that brief
`stream: spec`. A build brief that must wait for it carries `starts: after
spec` (see Phases and gates in [`../loop.md`](../loop.md)).

**A small change needs none of this.** One line in a brief is enough.

---

```markdown
# <Product name>

## In one paragraph
What it is, for whom, and why it should exist. Plain words.

## The story
One story, start to finish, that every feature sits inside. A person, a
moment, what they came to do, how it ends. A feature with no place in the
story is a candidate for "Not in version 1".

## Who it is for
The first user, often the person writing this, described as needs anybody
could have. Then who else it is for.

## The parts, placed in the story
Each part named where it happens in the story above, one line each.

## Constraints and values
What it must respect: platforms, offline, privacy, cost, how it should feel.

## Not in version 1
Named, so nobody assumes they were included.

## Must not happen
What would make it wrong even if every part works.

## How it will be built
A paragraph, not a design. The order of phases, if there are several, and
what each one settles.

## Answers and open choices
What the person has already answered, in their words. What is still open,
each with the options and a recommendation.
```

---

## Before the build starts

The default gate for a build: **no build brief before the spec is accepted.**
The spec report carries the read-back; the build brief carries `starts: after
spec`. `formwork check` refuses the build brief while the spec is open or its
read-back is missing.
