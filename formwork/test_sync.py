#!/usr/bin/env python3
"""Prove `formwork/sync` copies the kit, keeps what is the target's own, and stops.

Every case runs against a scratch kit, made a git repository on the spot, and
a scratch target. Nothing here touches a real project.

    a dry run writes nothing
    a kit with uncommitted changes is refused, and so is one with no commit
    a file the target owns survives, by default and by its .formwork.toml
    a kit file the kit no longer has is removed from the target
    the fingerprints are never recorded

Python 3, standard library only, no dependencies.
"""
import datetime
import os
import shutil
import stat
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SYNC = os.path.join(HERE, "sync")
results = []


def check(name, got, want, output=""):
    ok = got == want
    results.append(ok)
    shown = lambda v: repr(v) if isinstance(v, str) else v
    print("  [%s] %-52s expected %s, got %s"
          % ("pass" if ok else "FAIL", name, shown(want), shown(got)))
    if not ok and output:
        for line in output.strip().split("\n")[:12]:
            print("        %s" % line)


def write(root, rel, text, executable=False):
    full = os.path.join(root, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)
    if executable:
        os.chmod(full, os.stat(full).st_mode | stat.S_IXUSR)


def read(root, rel):
    full = os.path.join(root, rel)
    return open(full, encoding="utf-8").read() if os.path.isfile(full) else None


def git(root, *args):
    subprocess.run(["git", "-C", root, "-c", "user.name=t",
                    "-c", "user.email=t@example.invalid",
                    "-c", "commit.gpgsign=false"] + list(args),
                   check=True, capture_output=True)


def kit(commit=True):
    """A scratch kit: the real sync program and a few files, committed."""
    d = tempfile.mkdtemp(prefix="fw-sync-kit-")
    os.makedirs(os.path.join(d, "formwork"))
    shutil.copy2(SYNC, os.path.join(d, "formwork", "sync"))
    write(d, "FORMWORK.md", "# Formwork, new\n")
    write(d, "formwork/loop.md", "the loop, new\n")
    write(d, "formwork/check/run", "#!/bin/sh\nexit 0\n", executable=True)
    write(d, "formwork/rules/core.md", "kit rules\n")
    write(d, "README.md", "not part of the kit\n")
    git(d, "init", "-q")
    git(d, "remote", "add", "origin", "https://github.com/someone/kit.git")
    if commit:
        git(d, "add", "-A")
        git(d, "commit", "-q", "-m", "kit")
    return d


def hub(local=None):
    """A scratch target holding an older copy and files of its own."""
    d = tempfile.mkdtemp(prefix="fw-sync-hub-")
    write(d, "FORMWORK.md", "# Formwork, old\n")
    write(d, "formwork/loop.md", "the loop, old\n")
    write(d, "formwork/gone.md", "the kit dropped this\n")
    write(d, "formwork/gone/deeper.md", "and this\n")
    write(d, "formwork/roles/project/mine.md", "the hub's own role\n")
    write(d, "formwork/SOURCE.txt", "pinned: formwork 0000000 (x/y), copied 2000-01-01\n")
    write(d, "formwork/rules/core.md", "hub edited rules\n")
    write(d, "formwork/__pycache__/x.cpython-310.pyc", "bytes\n")
    write(d, "docs/standing.md", "the hub's own docs\n")
    toml = "[bindings]\nruntime = \"claude-code\"\n"
    if local:
        toml += "local = [%s]\n" % ", ".join('"%s"' % p for p in local)
    toml += "\n[strength]\ngit_boundary = \"block\"\n"
    write(d, ".formwork.toml", toml)
    return d


def snapshot(root):
    out = {}
    for dp, dn, fns in os.walk(root):
        for f in fns:
            full = os.path.join(dp, f)
            out[os.path.relpath(full, root)] = open(full, "rb").read()
    return out


def sync(kit_dir, *args, env=None):
    p = subprocess.run([sys.executable, os.path.join(kit_dir, "formwork", "sync")]
                       + list(args), capture_output=True, text=True,
                       env=env)
    return p.returncode, p.stdout + p.stderr


state = tempfile.mkdtemp(prefix="fw-sync-state-")
ENV = dict(os.environ, FORMWORK_STATE_DIR=state)
ENV.pop("FORMWORK_FINGERPRINTS", None)

print("A dry run shows everything and writes nothing")
k, h = kit(), hub()
before = snapshot(h)
code, out = sync(k, h, "--dry-run", env=ENV)
check("it succeeds", code, 0, out)
check("the target is byte for byte unchanged", snapshot(h) == before, True, out)
check("it names a file it would copy", "  + formwork/loop.md" in out, True, out)
check("it names a file it would remove", "  - formwork/gone.md" in out, True, out)
check("it names the pin it would write",
      "pinned: formwork " in out and "(someone/kit)" in out, True, out)
check("it says nothing was written", "Nothing was written" in out, True, out)

print("A kit with uncommitted changes is refused")
k, h = kit(), hub()
write(k, "formwork/loop.md", "edited, not committed\n")
before = snapshot(h)
code, out = sync(k, h, env=ENV)
check("a changed file is refused", code, 1, out)
check("and the reason is named", "uncommitted" in out, True, out)
check("the target is unchanged", snapshot(h) == before, True, out)
code, out = sync(k, h, "--dry-run", env=ENV)
check("a dry run is refused too", code, 1, out)
k = kit()
write(k, "formwork/new.md", "untracked\n")
code, out = sync(k, h, env=ENV)
check("an untracked file is refused", code, 1, out)
k = kit(commit=False)
code, out = sync(k, h, env=ENV)
check("a kit with no commit is refused", code, 1, out)
check("and says to commit", "no commit" in out, True, out)

print("A real sync copies the kit and keeps the target's own files")
k, h = kit(), hub()
code, out = sync(k, h, env=ENV)
check("it succeeds", code, 0, out)
check("a kit file is overwritten", read(h, "formwork/loop.md"), "the loop, new\n", out)
check("FORMWORK.md is overwritten", read(h, "FORMWORK.md"), "# Formwork, new\n", out)
check("a new kit file arrives executable",
      os.access(os.path.join(h, "formwork", "check", "run"), os.X_OK), True, out)
check("the sync program itself travels", read(h, "formwork/sync") is not None, True, out)
check("a file outside the kit does not travel", read(h, "README.md"), None, out)
check("a project role is preserved",
      read(h, "formwork/roles/project/mine.md"), "the hub's own role\n", out)
check("the target's docs are untouched",
      read(h, "docs/standing.md"), "the hub's own docs\n", out)
check("bytecode caches are left alone",
      os.path.isfile(os.path.join(h, "formwork", "__pycache__",
                                  "x.cpython-310.pyc")), True, out)
head = subprocess.run(["git", "-C", k, "rev-parse", "--short", "HEAD"],
                      capture_output=True, text=True).stdout.strip()
check("SOURCE.txt names the commit, origin and date",
      read(h, "formwork/SOURCE.txt"),
      "pinned: formwork %s (someone/kit), copied %s\n"
      % (head, datetime.date.today().isoformat()), out)

print("A kit file the kit no longer has is removed")
check("the dropped file is gone", read(h, "formwork/gone.md"), None, out)
check("a dropped folder is gone",
      os.path.exists(os.path.join(h, "formwork", "gone")), False, out)
check("and both are listed",
      "  - formwork/gone.md" in out and "  - formwork/gone/deeper.md" in out,
      True, out)

print("It stops before recording, and says what to run")
check("it prints the record command",
      "kit-integrity --record %s" % h in out, True, out)
check("it prints roles and check",
      "formwork/fw roles && formwork/fw check" in out, True, out)
check("no fingerprints were written", os.listdir(state), [], out)

print("A second sync finds nothing to copy")
code, out = sync(k, h, env=ENV)
check("it succeeds", code, 0, out)
check("nothing to copy or remove",
      "copy 0 file(s)" in out and "remove 0 file(s)" in out, True, out)

print("A path the target names as local is preserved")
k, h = kit(), hub(local=["formwork/rules/core.md"])
code, out = sync(k, h, env=ENV)
check("it succeeds", code, 0, out)
check("the local file keeps the target's words",
      read(h, "formwork/rules/core.md"), "hub edited rules\n", out)
k, h = kit(), hub(local=["formwork/rules/"])
write(h, "formwork/rules/extra.md", "the hub's extra rule\n")
code, out = sync(k, h, env=ENV)
check("a local folder keeps a file the kit lacks",
      read(h, "formwork/rules/extra.md"), "the hub's extra rule\n", out)
k, h = kit(), hub(local=["../elsewhere"])
code, out = sync(k, h, env=ENV)
check("a local path outside the project cannot run", code, 2, out)

print("A bad target is refused")
k = kit()
code, out = sync(k, os.path.join(k, "no-such-folder"), env=ENV)
check("a missing folder cannot run", code, 2, out)
code, out = sync(k, k, env=ENV)
check("the kit itself is refused", code, 1, out)
code, out = sync(k, env=ENV)
check("no target prints usage", code == 2 and "usage" in out, True, out)

print("")
print("%d passed, %d failed" % (results.count(True), results.count(False)))
sys.exit(1 if False in results else 0)
