#!/usr/bin/env python3
"""Prove the role generator keeps what a role author wrote, and says where it cannot.

A role may carry description, model, skills and color. Two properties matter:

    on Claude Code all four arrive in the generated agent
    on a runtime with no documented key for them, none is written, and the
    generated file says the role asked for them

And a third, which is why this suite pins bytes: a role with none of the four
generates exactly what it did before they existed.

Python 3, standard library only, no dependencies.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
results = []


def check(name, got, want, output=""):
    ok = got == want
    results.append(ok)
    print("  [%s] %-52s expected %s, got %s"
          % ("pass" if ok else "FAIL", name, want, got))
    if not ok and output:
        for line in output.strip().split("\n")[:8]:
            print("        %s" % line)


SECTIONS = """
**Owns.** %s

**Does not own.** Anything else.

**Tools.** Reading and writing.

**Stops when.** It is compared.

**Would be wrong if.** A byte moved.
"""


def role(name, extra="", owns="Checking that a role comes out as it should."):
    return ("---\nname: %s\npack: project\nowns: %s-job\n"
            "tools: [read, write]\n%s---\n\n# %s\n%s"
            % (name, name, extra, name.title(), SECTIONS % owns))


def project(**roles):
    """A throwaway project holding the generator and the roles given."""
    d = tempfile.mkdtemp(prefix="fw-build-")
    os.makedirs(os.path.join(d, "formwork", "roles", "project"))
    shutil.copy(BUILD, os.path.join(d, "formwork", "build"))
    for name, text in roles.items():
        open(os.path.join(d, "formwork", "roles", "project", name + ".md"),
             "w", encoding="utf-8").write(text)
    return d


def build(project_dir, *args):
    p = subprocess.run([sys.executable,
                        os.path.join(project_dir, "formwork", "build")]
                       + list(args), capture_output=True, text=True,
                       cwd=project_dir)
    return p.returncode, p.stdout + p.stderr


def read(project_dir, rel):
    full = os.path.join(project_dir, rel)
    if not os.path.exists(full):
        return None
    return open(full, encoding="utf-8").read()


def frontmatter(text):
    return text.split("\n---\n", 1)[0] if text else ""


# What the generator produced for this role before the four keys existed,
# taken from the 0.2.1 generator. Written with \u2014 so this file carries no
# em dash of its own.
PLAIN_OWNS = "Checking that a role with none of the new keys comes out as before."
BANNER = ("<!-- GENERATED FROM formwork/roles/project/plain.md \u2014 DO NOT "
          "EDIT. -->\n<!-- Change the source and run formwork roles. A "
          "hand-edit here fails the gate. -->\n")
STYLE = ("> **How to write a reply:** `formwork/style.md`. If the project has "
         "a `docs/style.md`, that one wins.\n")
BODY = "# Plain\n" + SECTIONS % PLAIN_OWNS
BEFORE = {
    ".claude/agents/plain.md":
        "---\nname: plain\ndescription: %s\ntools: Read, Glob, Grep, Write, "
        "Edit\n---\n\n%s\n%s\n%s" % (PLAIN_OWNS, BANNER, STYLE, BODY),
    ".gemini/agents/plain.md":
        "---\nname: plain\ndescription: %s\nkind: local\n---\n\n%s\n%s\n"
        "> **This role's tool grant is not expressed here.** It asks for "
        "`read`, `write`, and gemini-cli does not have a documented name for "
        "`write`. An incomplete allowlist would quietly remove a tool the "
        "role needs, so none is written. The grant is advice on this "
        "runtime.\n\n%s" % (PLAIN_OWNS, BANNER, STYLE, BODY),
    ".codex/agents/plain.toml":
        "# GENERATED FROM formwork/roles/project/plain.md \u2014 DO NOT "
        "EDIT.\n# Change the source and run formwork roles. A hand-edit here "
        "fails the gate.\n\nname = \"plain\"\ndescription = \"%s\"\n\n"
        "# This runtime has a sandbox mode rather than a tool list, so\n"
        "# the grant read, write is not expressed here. It is advice on "
        "Codex.\n\ndeveloper_instructions = \"\"\"\nHow to write a reply: "
        "formwork/style.md. If the project has a docs/style.md, that one "
        "wins.\n\n%s\"\"\"\n" % (PLAIN_OWNS, BODY),
}

FULL = ("description: Phase 0 triage for a pull request. Use to open a "
        "review. Returns the map, not the review itself.\n"
        "model: opus\n"
        "skills:\n  - pr-review\n  - fact-check\n"
        "color: blue\n")

print("A role with none of the four keys generates what it did before")
p = project(plain=role("plain", owns=PLAIN_OWNS))
code, out = build(p, "--all")
check("the generator runs", code, 0, out)
for rel, want in sorted(BEFORE.items()):
    check("%s is byte-identical" % rel, read(p, rel) == want, True,
          read(p, rel) or "")

print("All four keys reach the Claude Code agent")
p = project(full=role("full", FULL))
code, out = build(p, "--runtime", "claude-code")
check("the generator runs", code, 0, out)
fm = frontmatter(read(p, ".claude/agents/full.md"))
check("its own description, not the Owns sentence",
      "\ndescription: Phase 0 triage for a pull request. Use to open a review."
      " Returns the map, not the review itself.\n" in fm + "\n", True, fm)
check("the model as written", "\nmodel: opus" in fm, True, fm)
check("skills as a YAML list",
      "\nskills:\n  - pr-review\n  - fact-check" in fm, True, fm)
check("the color as written", "\ncolor: blue" in fm, True, fm)
check("the tool grant is still there",
      "\ntools: Read, Glob, Grep, Write, Edit" in fm, True, fm)

print("Skills written on one line are read the same way")
p = project(inline=role("inline", 'skills: [pr-review, "fact-check"]\n'))
code, out = build(p, "--runtime", "claude-code")
fm = frontmatter(read(p, ".claude/agents/inline.md"))
check("both skills arrive as a list",
      "\nskills:\n  - pr-review\n  - fact-check" in fm, True, fm)

print("On Codex and Gemini CLI the role says what it asked for instead")
p = project(full=role("full", FULL))
code, out = build(p, "--all")
check("the generator runs", code, 0, out)
gemini = read(p, ".gemini/agents/full.md")
codex = read(p, ".codex/agents/full.toml")
for label, text in (("gemini-cli", gemini), ("codex", codex)):
    head = frontmatter(text) if label == "gemini-cli" else \
        text.split('developer_instructions = """', 1)[0]
    check("%s has no model key" % label, "model:" in head
          or "model =" in head, False, head)
    check("%s has no skills key" % label, "skills:" in head
          or "skills =" in head, False, head)
    check("%s has no color key" % label, "color:" in head
          or "color =" in head, False, head)
    check("%s carries the note" % label,
          "This role asks for model" in text and "pr-review" in text
          and "no documented way to say so" in text, True, text)
    check("%s still gets the role's own description" % label,
          "Phase 0 triage for a pull request." in head, True, head)

print("A key written with nothing in it is refused, not ignored")
p = project(empty=role("empty", "model:\n"))
code, out = build(p, "--runtime", "claude-code")
check("the generator refuses", code, 2, out)
check("and names the key", "model:" in out and "empty.md" in out, True, out)
check("nothing is written",
      read(p, ".claude/agents/empty.md"), None, out)

print("A quoted description is not double-quoted in TOML")
p = project(quoted=role("quoted", 'description: "Triage: one line."\n'))
code, out = build(p, "--runtime", "codex")
check("the TOML carries it once",
      'description = "Triage: one line."' in (read(p, ".codex/agents/"
                                                  "quoted.toml") or ""),
      True, read(p, ".codex/agents/quoted.toml") or out)

print("")
print("%d passed, %d failed" % (results.count(True), results.count(False)))
sys.exit(1 if False in results else 0)
