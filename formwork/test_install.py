#!/usr/bin/env python3
"""Prove the installer keeps its three promises, and refuses when it should.

The installer's promises are the reason anybody will run it on a project that
already has work in it:

    it never needs a clean working tree
    it never moves or deletes a file
    it never demands a document

A promise nobody has tried to break is not evidence, so each one is tried here.

Python 3, standard library only, no dependencies.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
INSTALL = os.path.join(HERE, "install")
results = []


def check(name, got, want, output=""):
    ok = got == want
    results.append(ok)
    print("  [%s] %-52s expected %s, got %s"
          % ("pass" if ok else "FAIL", name, want, got))
    if not ok and output:
        for line in output.strip().split("\n")[:8]:
            print("        %s" % line)


# Every test runs the real installer, and the real installer writes a
# fingerprint record outside the project. Without this the suite wrote
# twenty-one records into the developer's own home directory, one per test.
STATE = tempfile.mkdtemp(prefix="fw-test-state-")


def install(project, *args):
    env = dict(os.environ)
    env["FORMWORK_STATE_DIR"] = os.path.join(STATE, os.path.basename(project))
    p = subprocess.run([sys.executable, INSTALL] + list(args),
                       capture_output=True, text=True, cwd=project, env=env)
    return p.returncode, p.stdout + p.stderr


def project(**dirs):
    """A throwaway project. dirs maps a path to its contents, or None for a dir."""
    d = tempfile.mkdtemp(prefix="fw-install-")
    for rel, content in dirs.items():
        full = os.path.join(d, rel)
        if content is None:
            os.makedirs(full, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full), exist_ok=True)
            open(full, "w", encoding="utf-8").write(content)
    return d


def tree(root):
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            out[os.path.relpath(full, root)] = open(full, encoding="utf-8").read()
    return out


print("A fresh project")
p = project(**{".claude/": None})
code, out = install(p)
check("wires a project that has .claude/", code, 0, out)
check("wrote .formwork.toml", os.path.exists(os.path.join(p, ".formwork.toml")), True)
settings = os.path.join(p, ".claude", "settings.json")
check("wrote .claude/settings.json", os.path.exists(settings), True)
check("and it calls the guard",
      "formwork/guard/git-boundary" in open(settings).read(), True)

print("Running it twice")
before = tree(p)
code, out = install(p)
check("second run is happy", code, 0, out)
check("second run changed nothing", tree(p) == before, True, out)

print("It does not need a clean working tree")
p = project(**{".claude/": None, "src/half-finished.py": "x = 1  # mid-edit\n",
               ".git/HEAD": "ref: refs/heads/main\n"})
code, out = install(p)
check("installs with uncommitted work sitting there", code, 0, out)
check("did not touch the work in progress",
      open(os.path.join(p, "src", "half-finished.py")).read(),
      "x = 1  # mid-edit\n")

print("It adds, and never removes")
p = project(**{".claude/settings.json": json.dumps({
    "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [
        {"type": "command", "command": "my-own-hook"}]}]},
    "somethingElse": {"kept": True}}, indent=2)})
code, out = install(p)
check("merges into settings that already exist", code, 0, out)
after = json.load(open(os.path.join(p, ".claude", "settings.json")))
commands = [h.get("command")
            for entries in after["hooks"].values()
            for e in entries for h in e.get("hooks", [])]
check("kept the hook that was already there", "my-own-hook" in commands, True)
check("kept settings it knows nothing about",
      after.get("somethingElse"), {"kept": True})
check("added the guard", any("git-boundary" in c for c in commands), True)
check("kept a copy of the original",
      os.path.exists(os.path.join(p, ".claude", "settings.json.before-formwork")),
      True)

print("It demands no document")
p = project(**{".claude/": None})
code, out = install(p)
files = set(tree(p))
check("wrote only the two things it said it would",
      files, {".formwork.toml", ".claude/settings.json"}, out)

print("When it cannot tell")
p = project(**{"src/main.py": "pass\n"})
code, out = install(p)
check("no runtime anywhere: refuses rather than guessing", code, 2, out)
check("and says how to tell it", "--runtime" in out, True, out)

p = project(**{".claude/": None, ".cursor/": None})
code, out = install(p)
check("two runtimes: refuses rather than picking one", code, 2, out)

print("An untested runtime is not reported as finished")
p = project(**{".codex/": None})
code, out = install(p)
check("exits 1, not 0", code, 1, out)
check("and says the word untested", "untested" in out, True, out)

print("It will not overwrite a configuration that disagrees")
p = project(**{".claude/": None,
               ".formwork.toml": '[bindings]\nruntime = "cursor"\n'})
code, out = install(p)
check("leaves the existing .formwork.toml alone", code, 1, out)
check("and it still says cursor",
      'runtime = "cursor"' in open(os.path.join(p, ".formwork.toml")).read(),
      True)

print("Broken JSON is left alone rather than replaced")
p = project(**{".claude/settings.json": "{ this is not json"})
code, out = install(p)
check("refuses to clobber it", code, 1, out)
check("and it is untouched",
      open(os.path.join(p, ".claude", "settings.json")).read(),
      "{ this is not json")

print("--dry-run")
p = project(**{".claude/": None})
code, out = install(p, "--dry-run")
check("says what it would do", code, 0, out)
check("and wrote nothing at all", tree(p), {}, out)

print("")
print("%d passed, %d failed" % (results.count(True), results.count(False)))
sys.exit(1 if False in results else 0)
