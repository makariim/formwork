#!/usr/bin/env python3
"""Prove setup asks, writes, and never takes a file that already exists.

Setup writes two files a person would otherwise never know to write. Two
properties matter more than the questions:

    it never overwrites something you wrote
    it never hangs waiting for an answer nobody is going to type

The second one is the dangerous one. This program will be run by people
inside scripts and inside agents, where nothing is typing.

Python 3, standard library only, no dependencies.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SETUP = os.path.join(HERE, "setup")
results = []


def check(name, got, want, output=""):
    ok = got == want
    results.append(ok)
    print("  [%s] %-52s expected %s, got %s"
          % ("pass" if ok else "FAIL", name, want, got))
    if not ok and output:
        for line in output.strip().split("\n")[:8]:
            print("        %s" % line)


def project(config=None, **files):
    """A throwaway project with a copy of the kit in it."""
    d = tempfile.mkdtemp(prefix="fw-setup-")
    shutil.copytree(HERE, os.path.join(d, "formwork"),
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc",
                                                  "fixtures"))
    if config is not None:
        open(os.path.join(d, ".formwork.toml"), "w",
             encoding="utf-8").write(config)
    for rel, content in files.items():
        full = os.path.join(d, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8").write(content)
    return d


def setup(project_dir, *args, **kw):
    p = subprocess.run([sys.executable,
                        os.path.join(project_dir, "formwork", "setup")]
                       + list(args), capture_output=True, text=True,
                       cwd=project_dir, input=kw.get("typed", ""))
    return p.returncode, p.stdout + p.stderr


def read(project_dir, rel):
    try:
        return open(os.path.join(project_dir, rel), encoding="utf-8").read()
    except OSError:
        return None


# The real file ends with a block of comments after the last key. A new key
# appended to the end of the section lands underneath them, which is valid and
# reads like a mistake, so the shape is part of the test.
CONFIG = ('[bindings]\nruntime = "claude-code"\n\n[strength]\n'
          'git_boundary = "block"   # block | warn | off\n'
          'protect_files = "block"\n\n'
          '# [rules] is deliberately absent, and that is the point.\n')


print("With nothing typing at it")
p = project(config=CONFIG)
code, out = setup(p)
check("refuses rather than hanging", code, 2, out)
check("and says to use --defaults", "--defaults" in out, True, out)
check("and wrote nothing", read(p, "docs/style.md"), None)

print("--defaults")
p = project(config=CONFIG)
code, out = setup(p, "--defaults")
check("writes both files", code, 0, out)
check("wrote docs/style.md", read(p, "docs/style.md") is not None, True, out)
check("wrote docs/standing.md", read(p, "docs/standing.md") is not None, True,
      out)

print("The standing brief it writes is a brief, not a page about briefs")
body = read(p, "docs/standing.md") or ""
check("has the updated line", body.lstrip().startswith("---"), True)
check("carries every required heading",
      all(("## " + h) in body for h in
          ("What we are building", "Where we are now", "What is decided",
           "What is open", "What is next", "What we tried and stopped")), True)
check("and is not the template page",
      "Save it as `docs/standing.md`" in body, False)

print("The check it has to satisfy")
gate = subprocess.run([sys.executable,
                       os.path.join(p, "formwork", "check", "checks",
                                    "standing-current"), p],
                      capture_output=True, text=True)
check("standing-current accepts what setup wrote", gate.returncode, 0,
      gate.stdout + gate.stderr)

print("Running it twice")
before = read(p, "docs/style.md")
code, out = setup(p, "--defaults")
check("second run is happy, not an error", code, 0, out)
check("and left the file exactly alone", read(p, "docs/style.md"), before)

print("It never takes a file you wrote yourself")
p = project(config=CONFIG, **{"docs/style.md": "mine, do not touch\n"})
code, out = setup(p, "--defaults")
check("leaves it", read(p, "docs/style.md"), "mine, do not touch\n", out)
check("and says so", "you already have" in out, True, out)

print("--dry-run")
p = project(config=CONFIG)
code, out = setup(p, "--dry-run", "--defaults")
check("says what it would do", code, 0, out)
check("and wrote nothing at all", read(p, "docs/style.md"), None, out)

print("Strength")
p = project(config=CONFIG)
code, out = setup(p, "--defaults")
check("the default leaves the configuration alone",
      read(p, ".formwork.toml"), CONFIG, out)

# The interactive path is the only way to ask for warn, so it is driven here
# through a terminal. Without a terminal setup refuses, which is the test
# above.
print("The folders it starts")
p = project(config=CONFIG)
code, out = setup(p, "--defaults")
check("started docs/decisions", read(p, "docs/decisions/README.md") is not None,
      True, out)
check("started docs/briefs", read(p, "docs/briefs/README.md") is not None,
      True, out)
check("started docs/reports", read(p, "docs/reports/README.md") is not None,
      True, out)
gate = subprocess.run([sys.executable,
                       os.path.join(p, "formwork", "check", "checks",
                                    "work-paired"), p],
                      capture_output=True, text=True)
check("work-paired accepts the empty folders", gate.returncode, 0,
      gate.stdout + gate.stderr)
gate = subprocess.run([sys.executable,
                       os.path.join(p, "formwork", "check", "checks",
                                    "decision-ids"), p],
                      capture_output=True, text=True)
check("decision-ids accepts the empty folder", gate.returncode, 0,
      gate.stdout + gate.stderr)

print("Asking for warn, through a real terminal")
p = project(config=CONFIG)
script = (
    "import os, pty, sys\n"
    "pid, fd = pty.fork()\n"
    "if pid == 0:\n"
    "    os.chdir(%r)\n"
    "    os.execv(sys.executable, [sys.executable, %r])\n"
    # length, knowing, language, never, building, now, next,
    # strength=warn, budget=5, folders, standing, write it
    "os.write(fd, b'1\\n2\\n\\n\\nA contact sheet tool\\nReading works\\n"
    "Make the size a setting\\n2\\n5\\n1\\n1\\n1\\n')\n"
    "out = b''\n"
    "try:\n"
    "    while True:\n"
    "        d = os.read(fd, 4096)\n"
    "        if not d: break\n"
    "        out += d\n"
    "except OSError:\n"
    "    pass\n"
    % (p, os.path.join(p, "formwork", "setup")))
subprocess.run([sys.executable, "-c", script], capture_output=True, text=True,
               timeout=60)
conf = read(p, ".formwork.toml") or ""
check("git_boundary is now warn", 'git_boundary = "warn"' in conf, True, conf)
check("protect_files is now warn", 'protect_files = "warn"' in conf, True,
      conf)
check("the comment on the line survived", "block | warn | off" in conf, True,
      conf)
check("[bindings] was not touched", 'runtime = "claude-code"' in conf, True,
      conf)
check("gate_budget was added", "gate_budget = 5" in conf, True, conf)
check("and it went inside [strength], above the closing comments",
      conf.index("gate_budget") < conf.index("# [rules]"), True, conf)

standing = read(p, "docs/standing.md") or ""
check("the standing brief carries what was typed",
      "A contact sheet tool" in standing, True, standing[:300])
check("and the template line it replaced is gone",
      "One paragraph. This changes rarely" in standing, False)
gate = subprocess.run([sys.executable,
                       os.path.join(p, "formwork", "check", "checks",
                                    "standing-current"), p],
                      capture_output=True, text=True)
check("standing-current accepts the seeded brief", gate.returncode, 0,
      gate.stdout + gate.stderr)

print("Saying no at the end changes nothing")
p = project(config=CONFIG)
script = (
    "import os, pty, sys\n"
    "pid, fd = pty.fork()\n"
    "if pid == 0:\n"
    "    os.chdir(%r)\n"
    "    os.execv(sys.executable, [sys.executable, %r])\n"
    "os.write(fd, b'\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n2\\n')\n"
    "try:\n"
    "    while os.read(fd, 4096): pass\n"
    "except OSError:\n"
    "    pass\n"
    % (p, os.path.join(p, "formwork", "setup")))
subprocess.run([sys.executable, "-c", script], capture_output=True, text=True,
               timeout=60)
check("wrote no style file", read(p, "docs/style.md"), None)
check("and left the configuration alone", read(p, ".formwork.toml"), CONFIG)

print("")
print("%d passed, %d failed" % (results.count(True), results.count(False)))
sys.exit(1 if False in results else 0)
