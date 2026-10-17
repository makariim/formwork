# Upstream

`SKILL.md` and `LICENSE` in this folder are copied byte for byte from:

    repository  https://github.com/blader/humanizer
    commit      8c307f367c91bd974002f10f2be2965d642c13df
    version     3.1.0
    date        2026-10-16 (commit date)
    licence     MIT, Copyright (c) 2025 Siqi Chen, in LICENSE beside this file
    sha256      0612f1dfb1672b0ea9b97e139bf1f06cabe98d8b27424fe8ff01e1fb4cc99cad  SKILL.md
                4ac4810254ab36d45419141aeb8e69bf50652cfafe5b2dab947d06d44e5cbf96  LICENSE

Do not edit either file. Formwork's one change to the skill is in
[`local.md`](local.md), and `formwork roles` puts the two together into
`.claude/skills/humanizer/SKILL.md`.

## Nothing updates on its own

The skill is a third party's instructions, run inside every agent that writes
text for you. A new upstream version takes effect only when somebody chooses
it. To update:

1. Read the upstream diff from the commit above to the new one, all of it:
   `gh api repos/blader/humanizer/compare/8c307f367c91...<new-sha>`
2. Fetch `SKILL.md` and `LICENSE` at the new commit, and nothing else.
3. Check that `local.md` still makes sense against the new section numbers.
4. Change the commit, version, date and sha256 lines above.
5. Run `formwork roles`, then `formwork check`.
6. Commit it, so the update is one line in version control with your name on it.
