# Bringing in somebody else's skill

A skill is a file of instructions that runs inside your agents. A skill
written by somebody else is their instructions, running in your project. Bring
one in the way the kit brought in its own one, `humanizer`
([`skills/humanizer/UPSTREAM.md`](skills/humanizer/UPSTREAM.md)): from one
commit you can name, with its licence beside it, and with a record that says
exactly which bytes you took.

The kit ships no catalogue of skills, and never fetches one. You fetch. The
kit only says how to keep what you fetched.

---

## Before you bring one in

1. **Look for an existing role first.** Most stack and craft knowledge already
   has an owner in `formwork/roles/`. A skill adds depth to a role; it does not
   replace one.
2. **Find the licence.** A file with no licence is not free to use, the rule
   in `formwork/roles/packs/legal.md`. No licence file in the source
   repository means you do not bring it in. Ask the author, or write your own.
3. **Read all of it.** It will run in every agent that loads it, with that
   agent's tools.

---

## Where it lives in a project

```
.claude/skills/<name>/
    SKILL.md        copied byte for byte from the source
    LICENSE         the source's licence file, copied byte for byte
    UPSTREAM.md     where both came from, from formwork/templates/upstream.md
```

- **Not under `formwork/`.** `formwork sync` replaces that folder with the
  kit's own copy, and a skill there would be deleted on the next sync.
- **`.claude/skills/`** is where Claude Code finds a project's skills. The kit
  does not know where Codex, Gemini CLI or Cursor read skills from (NOT
  ESTABLISHED), so on those the role that uses it reads the file by its path.
- **The name must not be one the kit ships.** `formwork roles` will not
  overwrite a file it did not make, so a clash leaves yours in place and says
  so, but the kit's skill is then missing.
- **Never edit `SKILL.md` or `LICENSE`.** Your own change goes in the project
  role that uses the skill, under a heading such as "Where this project differs
  from the skill". Then an update stays a straight copy.

---

## Who uses it

A role names it, in the project's own role for that work
(`formwork/roles/HOW-TO-ADD-A-ROLE.md` says how to write one):

```
skills:
  - <name>
```

On Claude Code that binds the skill to the role when `formwork roles` runs.
Elsewhere the generated file notes it, so say in the role's body: "read
`.claude/skills/<name>/SKILL.md` before you start". A skill no role names is a
file nobody reads; naming it only in a brief works for that one brief.

---

## The record

Copy [`templates/upstream.md`](templates/upstream.md) to
`.claude/skills/<name>/UPSTREAM.md` and fill in every line:

| line | where it comes from |
|---|---|
| repository | the source's address |
| commit | the full commit you copied from, never a branch name |
| version and date | the source's own version, if it has one, and the commit date |
| licence | its name and copyright line, as the LICENSE file says |
| sha256 | one line per file, from `shasum -a 256 SKILL.md LICENSE` |

A record that names a branch, or has no sha256, cannot tell you later whether
the file in front of you is the file you read.

**A skill written in this project needs no record.** Put one line in its
folder's `UPSTREAM.md` instead: `written here, no upstream`.

---

## Nothing updates on its own

A new upstream version takes effect only when somebody chooses it. To update:

1. Read the upstream diff from the recorded commit to the new one, all of it.
2. Fetch `SKILL.md` and `LICENSE` at the new commit, and nothing else.
3. Check that the project role's own change still fits.
4. Change the commit, version, date and sha256 lines.
5. Run `formwork roles`, then `formwork check`.
6. Commit it, so the update is one change in version control with your name on
   it.

---

## What this does not do

- **It does not judge the skill.** Whether it is any good is the role's call,
  and the reviewer's.
- **It does not check the licence lets you do what you do with it.** That is
  `legal`.
- **It does not stop somebody editing the copied file.** The check
  `skill-provenance` notices at the next `formwork check`: it fails a skill
  folder with no record, no licence, no full commit, or a file whose sha256 no
  longer matches. It fetches nothing, so it cannot tell whether the commit is
  real.
