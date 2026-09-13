# The rest of the rules

Thirty-four. Not for reading end to end. Find the one that matches the
situation you are in.

Advice, except one that names a check. What else is blocked is in
`FORMWORK.md`. The thirteen you meet daily are in `core.md`.

Some carry a **warning**. That means the rule costs something real, or stops
working outside the conditions it was learned in. The warning is part of the
rule, not a footnote.

---

## Working with documents

### One document owns each kind of fact

**Advice.**

Every kind of information has exactly one home. Two documents saying the same
thing is a problem **even while both are right**, because they will not stay
right. Fix it by deleting one, not by keeping them in step.

**Catches:** two copies of a fact drifting apart, with nothing announcing it.

**Warning:** nothing checks this for you. No tool anywhere does. It is a habit
with no net under it.

---

### A small fixed set of documents

**Advice.**

Give each of these one home: what the project is and will not become · the plan
and its order · boundaries and who decides · what exists right now · decisions
you have accepted · how work gets done · ideas parked for later.

Seven is what this method used. A published twelve-section standard exists and
is not obviously worse. Pick one and keep it.

**Catches:** a fact with nowhere obvious to live, which ends up in three places
or none.

---

### Documents say what is true now

**Advice.**

A sentence explaining that something was removed or renamed is history. History
lives in version control. Documents describe the present.

**Catches:** documents that grow into a changelog, where the description of what
is actually true is outnumbered by the story of how it got there.

---

### Park open questions with a status, not in a graveyard

**Advice.**

Deferred questions get a status on the thing they belong to, not a separate file
that only grows.

**Catches:** a "later" document nobody opens, which quietly becomes where ideas
go to die.

---

## Before you start

### Say the scope back before touching anything

**Advice.**

Before the first edit, write down what you understood: the goal, what is in
scope, what is explicitly out, which files you expect to touch, what you will
run to check it.

**Catches:** a misunderstanding, while it is still free. After the first edit it
is not.

---

### Checks and documents are part of the work

**Advice.**

Verification and document updates belong to the piece of work, not to a tidy-up
afterwards. If a document states something your change makes untrue, fix it now,
or write down why nothing needed changing.

**Catches:** deferred documentation, which does not get written. Same for
deferred checks.

**Warning:** every piece of work is bigger than the change that prompted it.
That is the price.

---

### The gate belongs to one owner

**Advice.**

Whoever owns the checks owns them, no matter which piece of work trips over a
broken one. Work that hits a broken check reports it and leaves it alone.

Working alone, the rule still holds in a different shape: **the check is never
edited by the work that it just failed.**

**Catches:** a check quietly edited until it goes green.

---

### Never invent a source

**Advice.**

If a claim needs backing and there is none, write that.

**Catches:** a made-up citation, which is the most expensive error available,
because it looks exactly like a real one.

---

### A pass says what it did not look at

**Advice.**

When a check passes, it should be clear what it did not examine. Keep that list
next to the check.

**Catches:** a green result read as total coverage, when it only ever looked at
a third of the problem.

---

## Rounds

A round is several agents arguing about one question. Skip this section if you
work alone with one agent.

### The lead holds no position

**Advice.**

One role runs the round, hands out questions, and does none of the design.

The separation is structural rather than courteous. Owning a piece of the design
means scrutinising that piece less harshly than the rest, and the omission goes
unseen because the same role writes the record.

**Catches:** the one piece of a design nobody reviewed properly.

**Warning:** a whole agent producing no design. On a small question that is most
of what you spend.

---

### Somebody argues against, every time

**Advice.**

One role's whole job is making the case against. Not balanced, not looking for
the middle. Present in every round without exception.

It says plainly when it has no good objection. Invented objections train
everyone to ignore it.

**Catches:** a group of agents agreeing, which reads exactly like being right.

**Warning:** it pays for itself only when the round was heading somewhere wrong,
and you cannot know that in advance.

---

### Split by who decides, not by topic

**Advice.**

Divide questions so no two people can answer the same one. Split by who owns the
answer. What must exist, what we would measure, what it costs to keep running,
why not. Rather than by subject.

**Catches:** two agents landing on one answer after being handed one question.
It wears the appearance of corroboration and is paid-for duplication.

---

### One prepared briefing, not everyone reading everything

**Advice.**

The lead reads widely, alone, and writes one briefing: the constraints in its
own words with file and line, what already exists, what has failed before, and
the numbered questions.

A briefing that quotes whole documents has rebuilt the problem it was meant to
remove.

**Catches:** everyone paying to read the same material.

**Warning:** the lead becomes a single point of misunderstanding. A wrong
briefing is wrong for everybody.

---

### Different reading for different people

**Advice.**

No two participants get the same reading list. Anyone needing something outside
theirs names the file, says which question needs it, reads it, and says so.

**Catches:** cost, and a split by ownership that is real rather than nominal.

---

### Read everything before answering anything

**Advice.**

The lead reads every answer in full before replying to any of them.

**Catches:** anchoring the whole round on whichever answer arrived first.

---

### One challenge, one reply, then closed

**Advice.**

Put the strongest objection to whoever holds the position. They concede, refute,
or adjust. Then it is over.

Before spending anything on it, try to settle the objection yourself by reading
a file.

**Catches:** two agents arguing forever, which is the easiest way to spend a
budget and produce nothing.

---

### Three ways a disagreement can end

**Advice.**

Settle it, but only if a document decides it, and name the file. Park it,
writing down both sides and what changes depending on which is right. Or stop
the round, if other answers depend on the outcome, and go to the human now.

A candid unresolved question counts as an achievement rather than a hole.

**Catches:** a record that reads as settled and is not.

---

### Everyone agreeing is a warning sign

**Advice.**

Signs the round is too comfortable: everything fits with no friction, the
objections were all easy to answer, nobody said they would have done it
differently, a proposal was accepted with nobody naming what it costs.

On seeing it, point at whatever assumption went unexamined, and require
somebody to defend that.

**Catches:** comfortable agreement, which is the normal failure, not the normal
success.

**Warning:** do not require that somebody disagree. Manufactured conflict is
worse than none, and the challenger's own rules forbid it.

---

### Two failures the same way means stop

**Advice.**

A failed agent is not replaced automatically. Two failures of one kind point at
the surroundings rather than the work; end the round there and report.

Better still: record whether a failure was the environment or the work, and let
that decide.

**Catches:** a whole budget spent reproducing one broken thing.

---

### Escalate in a fixed shape

**Advice.**

The question in one sentence. The first position, whose it is, its strongest
reason. The second position, likewise. What turns on the outcome. Whatever you were
unable to resolve, and why the written record leaves it open. Then a recommendation,
or an honest statement that you have no grounds for one.

No transcript. What is needed is the fork, not the road to it.

**Catches:** a long argument dumped on somebody who has to reconstruct the
decision from it.

---

### A role appears when its subject exists

**Advice.**

Do not create a role for something you are not doing. No application, no
application role. No code, no code review role.

**Catches:** a team designed for the project you imagine rather than the one in
front of you.

---

## Writing to a human

### Two parts, always

**Advice.**

First: what happened, what needs you, what is next. Plain words, short
sentences, point before reason, every code name explained where it appears.

Then the substantiation: which files, which commands, their output, what you
confirmed and by what means, and anything deferred with its reason.

Same reader. Different depth.

**Catches:** a reader who has to choose between a summary that leaves out what
they need and a wall they will not read.

**Warning:** everything gets written twice. And this shape was tuned to one
particular person.

---

### Do not waste the human's turns

**Advice.**

Do not ask what you could read. Put three questions in one message, not three
messages. Paste the text you are referring to. "see above" has cost whole
round trips. Name who should answer and hand over the message ready to send.

**Catches:** a person spending their day carrying messages between two systems
that cannot see each other.

**Warning:** this assumes you are that person. If your setup is different, these
rules solve a problem you do not have.

---

### Interrupt for two things only

**Advice.**

Interrupt for what cannot be undone, and for what breaks so quietly nobody would
notice. Everything else goes in the report.

**Catches:** either being interrupted constantly, or losing something
irrecoverable because it did not seem urgent.

**Warning:** the original version of this rule assumed somebody checking every
day. If you open your project once a week, a "note" can sit there for a week.
Set the line where it suits you.

---

## Designing

### Generalise on the second real case

**Advice.**

Build the general version when you have a second real use, not when you expect
one.

**Catches:** an abstraction designed against a guess, which you then maintain
forever.

---

### Ask what this component actually adds

**Advice.**

When something new is proposed. Another service, another store, a queue, a
workflow engine. Ask two questions. What does it do that nothing here already
does? And who operates it in six months?

**Catches:** the components that look like progress and are mostly maintenance.

**Warning:** this rule came from one person's experience on two projects. If
your project genuinely needs the thing, the rule knows nothing about that. It is
a question, not a veto.

---

### Name which of your own rules this breaks

**Advice.**

Write down what your project is not. Then ask every proposal which of those it
is drifting toward, and how far.

**Catches:** drift, where every single step is defensible and the destination is
not.

---

### Something stored that nothing reads

**Advice.**

Where you are storing what nothing consumes, establish its consumer and the
moment of consumption. An anticipated feature is not a consumer.

**Catches:** storage that costs you now and shapes your design as though it
mattered.

---

### Ask how it fails quietly

**Advice.**

Put this to every proposal: in what manner does it fail while escaping notice?

**Catches:** quiet wrongness, which accumulates, as against visible failure,
which gets fixed.

---

### What does this cost in six months

**Advice.**

Ask what becomes easier, what becomes harder, and what new risk appears. Ask who
will be maintaining it and what they will have forgotten.

**Catches:** maintenance burden treated as somebody else's problem, when it is
yours.

---

## Above the repository

### The state between sessions lives in a file

**Enforced** by `formwork/check/checks/standing-current`.

The state a project is in between pieces of work belongs in `docs/standing.md`,
updated before a conversation closes rather than afterwards. What goes in it is
[`../templates/standing.md`](../templates/standing.md).

The check compares its date against your newest decision and round.

**Catches:** the plan living in one chat window, which means it ends when the
window does, and the next conversation starts from somebody's memory.

**Warning:** nothing can tell whether what you wrote is true. The check reads
the date, the headings and the empty bullets. Those catch the way this file
actually fails, and no more.

---

### Keep planning and working in separate conversations

**Advice.**

One conversation decides what happens next and judges what comes back. Another
does the work in the repository and stops. See
[`../threads.md`](../threads.md).

**Catches:** the plan being buried under the work. A session that reads fifty
files still has the plan in it somewhere, underneath everything it read.

---

### The human carries the messages

**Advice.**

Nothing moves between the two layers on its own. A person moves the text. The
planning conversation may read the repository, and it still cannot see the
working session, nor the working session it.

**Catches:** work done twice, and work done against a decision that was already
made upstairs.

**Warning:** the relay is a person copying and pasting, so it is slow and it can
be skipped. What stops it being skipped is that the standing brief is a file
and a check reads its date. **No team has run this.** NOT ESTABLISHED beyond
one person.

---

### Whole reports travel up, not summaries

**Advice.**

What goes back up is the entire report, not somebody's account of it.

**Catches:** a summary that keeps the routine part and drops the three lines a
report exists for. Those are the first things anybody shortening it cuts,
because they read like exceptions rather than results.
