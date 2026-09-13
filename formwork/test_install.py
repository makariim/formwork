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
    # The copy of the kit inside this throwaway project, never the one in the
    # repository. The installer works on the project that holds it, so running
    # the repository's own copy here would write into the repository.
    p = subprocess.run([sys.executable,
                        os.path.join(project, "formwork", "install")]
                       + list(args),
                       capture_output=True, text=True, cwd=project, env=env)
    return p.returncode, p.stdout + p.stderr


def project(**dirs):
    """A throwaway project with a copy of the kit in it.

    dirs maps a path to its contents, or None for a directory.
    """
    d = tempfile.mkdtemp(prefix="fw-install-")
    shutil.copytree(HERE, os.path.join(d, "formwork"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc",
                                                  "fixtures"))
    for rel, content in dirs.items():
        full = os.path.join(d, rel)
        if content is None:
            os.makedirs(full, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full), exist_ok=True)
            open(full, "w", encoding="utf-8").write(content)
    return d


def tree(root):
    """Everything in the project except the kit itself.

    The kit is copied in when the project is made, and it is not something the
    installer wrote, so counting it would make every "wrote nothing" test wrong
    by two hundred files.
    """
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if os.path.join(dirpath, d) != os.path.join(root,
                                                                   "formwork")]
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

print("It demands no document, and writes only what it said it would")
p = project(**{".claude/": None})
code, out = install(p)
files = set(tree(p))
# The configuration, the wiring, and the generated roles. Nothing else: no
# documents demanded, no folders invented, nothing touched in src/.
#
# This used to assert two files and pass, because the throwaway project had no
# kit in it and the generator had nothing to generate from. The harness was
# wrong, not the installer.
check("wrote the configuration and the wiring",
      {".formwork.toml", ".claude/settings.json"} <= files, True, out)
strays = {f for f in files
          if f not in (".formwork.toml", ".claude/settings.json")
          and not f.startswith(os.path.join(".claude", "agents") + os.sep)}
check("and nothing else at all", strays, set(), out)
check("the roles it generated are all it generated",
      len(files) - 2, 28, out)

def outside(project, *args, **kw):
    """Run the installer from somewhere, and see what the WHOLE tree did.

    Every other helper looks only inside the project. An audit pointed out
    that the bugs in this area all write somewhere else, so nothing in the
    suite could see them.
    """
    env = dict(os.environ)
    env["FORMWORK_STATE_DIR"] = os.path.join(STATE, "outside")
    p = subprocess.run([sys.executable, kw["script"]] + list(args),
                       capture_output=True, text=True, cwd=kw["cwd"], env=env)
    return p.returncode, p.stdout + p.stderr


def listing(d):
    return sorted(os.listdir(d))


print("It refuses rather than wiring the wrong thing")
# Three ways the installer has picked the wrong target. The first two shipped:
# the working directory, then the kit's own location. Each fix moved the bug
# rather than closing it, so all three are held down here.
home = tempfile.mkdtemp(prefix="fw-outer-")
proj = os.path.join(home, "proj")
os.makedirs(os.path.join(proj, ".claude"))
shutil.copytree(HERE, os.path.join(proj, "formwork"),
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc",
                                              "fixtures"))
before_home = listing(home)

stranger = tempfile.mkdtemp(prefix="fw-stranger-")
shutil.copytree(HERE, os.path.join(stranger, "formwork"),
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc",
                                              "fixtures"))

code, out = outside(proj, "--runtime", "claude-code",
                    script=os.path.join(stranger, "formwork", "install"),
                    cwd=proj)
check("a kit from elsewhere, run in a project that has its own: refused",
      code, 2, out)
check("and it wired nothing in the project",
      os.path.exists(os.path.join(proj, ".formwork.toml")), False, out)
check("and nothing in the stranger's folder",
      os.path.exists(os.path.join(stranger, ".formwork.toml")), False, out)

bare = tempfile.mkdtemp(prefix="fw-bare-")
os.makedirs(os.path.join(bare, ".claude"))
code, out = outside(bare, "--runtime", "claude-code",
                    script=os.path.join(stranger, "formwork", "install"),
                    cwd=bare)
check("a kit from elsewhere, run where there is no kit: refused", code, 2, out)
check("and wrote nothing there", listing(bare), [".claude"], out)

# Fed through a pipe, __file__ is <stdin>, so the program cannot tell where it
# lives. It used to answer anyway, and wrote into the parent of the project.
piped = subprocess.run(
    [sys.executable, "-"] + ["--runtime", "claude-code"],
    stdin=open(os.path.join(proj, "formwork", "install")),
    capture_output=True, text=True, cwd=proj,
    env=dict(os.environ, FORMWORK_STATE_DIR=os.path.join(STATE, "piped")))
check("fed through a pipe: refused rather than guessing", piped.returncode, 2,
      piped.stdout + piped.stderr)
check("and wrote nothing above the project", listing(home), before_home,
      piped.stdout + piped.stderr)

print("Run from a subfolder, it still means the project")
p = project(**{".claude/": None, "src/main.py": "pass\n"})
sub = os.path.join(p, "src")
env = dict(os.environ)
env["FORMWORK_STATE_DIR"] = os.path.join(STATE, "subfolder")
run = subprocess.run([sys.executable,
                      os.path.join(p, "formwork", "install")],
                     capture_output=True, text=True, cwd=sub, env=env)
out = run.stdout + run.stderr
# It used to take the working directory as the project. From a subfolder that
# meant looking for the agent's folder in the wrong place and refusing, or,
# with --runtime given, writing a second configuration into the subfolder and
# calling it a success while the real project stayed unwired.
check("finds the runtime one level up", run.returncode, 0, out)
check("wrote the configuration in the project",
      os.path.exists(os.path.join(p, ".formwork.toml")), True, out)
check("and nothing into the subfolder",
      sorted(os.listdir(sub)), ["main.py"], out)
# The old message said "which is where this kit lives", which was asserted and
# never verified, and was false in three of the cases above. This checks the
# named target instead of the wording.
named = [l for l in out.split("\n") if l.startswith("Installing into ")]
check("names one target", len(named), 1, out)
check("and it is the project, not the subfolder",
      os.path.realpath(named[0][len("Installing into "):].rstrip(".")),
      os.path.realpath(p), out)

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
