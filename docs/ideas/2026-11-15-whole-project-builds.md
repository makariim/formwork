# Idea: formwork for building a whole project (noted 2026-11-15)

From the maintainer, after building the desktop app and the health app with formwork. His words: "i am very happy with the autonomy and the formwork cycle and the roles and everything, but i still want to enhance and strengthen it more ... formwork is very good in iterating over a specific kind of task, or maybe managing the agent lifecycle, but we need to enhance it more to handle building a whole project as well, so it sth over or i dont know under or beside the current structure, and the new project build or app or system or whatever, definitely needs lots of new roles and agents, and needs also to be dynamic in building and spawning those agents".

Not decided. Kept for when he returns to formwork.

## What the health app showed was missing

He had to say by hand, every time, things a project layer should carry:

- **The phase cycle for a whole product**: spec, research, design, build, verify, review rounds, release. Each phase run without interrupting him, each ending in one plain report and his read-back. Today this lives in the director's head and in each brief.
- **A research round shape**: every researcher writes the question and why it matters, theory, state of the art, what it means for this product, ranked proposals with evidence, risks. Then cross reading, one synthesis ("the story"), a challenger, and a spec update. (the health app brief 0001.)
- **A taste and anti AI slop checklist**: pills only for real choices, one soft light per screen, no glowing buttons, solid colours, no icon tiles, no decoration posing as data, one neutral surface, plain copy that says the thing. (the health app `docs/design/round-2/director-ai-check.md`.) Plus "clean is not the same as alive": v1 was correct and dead.
- **User first, not feature first**: one story above every feature; the user zero pattern (build on one real person, write every feature as a general need).
- **Review rounds on the running product**: our own team reviews in parallel with him, on its own device, findings by journey with screenshots, then fixes his notes and ours together.
- **Release and device pipeline**: in his projects, a remote machine signs, ships and installs on a message, never on a schedule. He was clear this is **not** a formwork feature: "the mac air pipeline btw shouldnt be a persistent thing, remember, formwork itself is a general repo". At most, formwork could describe the general pattern of a release step owned by another machine or session; his Air setup stays in his projects.

## What a project layer might add

- A project template: phases, their briefs, their report shapes, their gates (what must be true before the next phase).
- **Dynamic roles**: the lead spawns the specialists a phase needs (creative director, motion designer, nutrition scientist, illustrator) from a role library, writing new project roles on the fly in the five section format, instead of a fixed set.
- Taste packs and checklists per product kind (iOS app, Mac app, web, deck).
- A cross phase record: what the person decided, in their words, and which phase it binds.
- Usage awareness: how many builders run at once against the person's plan limits.

## Open questions for him

- Over, under or beside the current kit: a separate "project" layer, a pack, or part of the director role?
- How much should be fixed templates and how much generated per project?
