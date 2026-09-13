"""The `formwork` command.

    formwork init       put the kit into this project
    formwork install    wire it up to your coding agent
    formwork check      run every check
    formwork demo       watch every check refuse a broken input
    formwork roles      rebuild the role files after editing one
    formwork record     write down what the kit looks like now
    formwork test       run every test in the kit
    formwork where      say which kit is being used

WHY THIS EXISTS
---------------
The kit is a folder of files that has to live inside your project, because
your agent's hooks call those files by path. That part cannot be global.

What can be global is the word you type. This module is the word.

HOW IT FINDS THE KIT
--------------------
It looks for a `formwork/` folder in the current directory, then each
directory above it. So the command works anywhere inside your project.

`formwork init` copies a fresh kit out of this package into the current
directory. That copy is what your project uses from then on. Upgrading the
command does not change a project you have already set up, which is
deliberate: a rule that changes under you without a commit is not a rule.

Python 3.8 or newer. No dependencies.
"""
import os
import re
import shutil
import stat
import subprocess
import sys

__all__ = ["main"]

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLED_KIT = os.path.join(HERE, "kit")
BUNDLED_PAGE = os.path.join(HERE, "kit-page", "FORMWORK.md")

try:                                    # Python 3.8 or newer
    from importlib.metadata import version as _version, PackageNotFoundError
except ImportError:                     # pragma: no cover
    _version = None

COMMANDS = [
    ("init",    "put the kit into this project"),
    ("install", "wire it up to your agent. --runtime <name> to choose"),
    ("setup",   "answer a few questions, and write the files nobody knows to write"),
    ("check",   "run every check on this project"),
    ("demo",    "watch every check refuse a broken input"),
    ("roles",   "rebuild the role files after editing one"),
    ("test",    "run every test in the kit"),
    ("record",  "write down what the kit looks like now, after you changed it"),
    ("where",   "say which kit is being used"),
    ("version", "which version of the command this is"),
]

TESTS = [
    os.path.join("guard", "test_boundary.py"),
    os.path.join("guard", "test_protection.py"),
    os.path.join("guard", "test_quality_gate.py"),
    os.path.join("check", "test_gate.py"),
    "test_install.py",
    "test_setup.py",
]


def find_kit(start=None, complete_only=True):
    """The nearest formwork/ folder at or above here, or None.

    complete_only=False also returns a folder that looks like a kit but is
    missing pieces. Without that, a damaged kit produced three different
    answers from three commands and no way forward.
    """
    d = os.path.abspath(start or os.getcwd())
    while True:
        candidate = os.path.join(d, "formwork")
        looks_like = os.path.isdir(candidate) and (
            os.path.isdir(os.path.join(candidate, "guard"))
            or os.path.isdir(os.path.join(candidate, "check"))
            or os.path.isdir(os.path.join(candidate, "roles")))
        if os.path.isdir(candidate) and os.path.isfile(
                os.path.join(candidate, "check", "run")):
            return candidate
        if looks_like and not complete_only:
            return candidate
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def make_runnable(root):
    """Give every program in the kit its execute bit back.

    A wheel does not reliably carry file modes, and a check that cannot run is
    treated by the gate as a failure rather than a pass. So this is not
    cosmetic.
    """
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                with open(p, "rb") as fh:
                    if fh.read(2) != b"#!":
                        continue
            except OSError:
                continue
            mode = os.stat(p).st_mode
            os.chmod(p, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            fixed += 1
    return fixed


def cmd_init(args):
    if any(a.startswith("-") for a in args):
        print("formwork init [directory]")
        print("")
        print("  Puts the kit into a directory. Defaults to this one.")
        print("  `formwork init --help` used to create a folder called")
        print("  --help, with a kit inside it.")
        return 0
    if not os.path.isdir(BUNDLED_KIT):
        print("ERROR: this copy of the command has no kit bundled with it.",
              file=sys.stderr)
        print("       Clone the repository and copy formwork/ in by hand.",
              file=sys.stderr)
        return 2

    target = os.path.abspath(args[0]) if args else os.getcwd()
    dest = os.path.join(target, "formwork")

    if os.path.exists(dest):
        print("There is already a formwork/ folder here.")
        print("Nothing was changed. Delete it first if you meant to start "
              "again.")
        return 1

    # Without the filter, pip's own bytecode caches travel into the user's
    # project and get committed by their first `git add .`
    above = find_kit(os.path.dirname(target) if os.path.dirname(target) else None)
    if above and os.path.dirname(os.path.dirname(above)) != target:
        print("There is already a kit above this folder, at %s." % above)
        print("Two kits in one tree is almost never what somebody wants.")
        print("Nothing was changed. Pass a directory if you meant it:")
        print("    formwork init /somewhere/else")
        return 1

    try:
        shutil.copytree(BUNDLED_KIT, dest,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    except OSError as e:
        print("ERROR: could not write into %s: %s" % (target, e),
              file=sys.stderr)
        return 2
    n = make_runnable(dest)

    page = os.path.join(target, "FORMWORK.md")
    wrote_page = False
    if os.path.isfile(BUNDLED_PAGE) and not os.path.exists(page):
        shutil.copy2(BUNDLED_PAGE, page)
        wrote_page = True

    print("wrote  formwork/        the kit, %d programs made runnable" % n)
    if wrote_page:
        print("wrote  FORMWORK.md     the method on one page")
    print("")
    print("Next:  formwork install --runtime claude-code")
    return 0


def run_in_kit(rel, args):
    kit = find_kit()
    if kit is None:
        broken = find_kit(complete_only=False)
        if broken:
            print("ERROR: there is a formwork/ folder at %s, and it is "
                  "incomplete." % broken, file=sys.stderr)
            print("       formwork/check/run is missing. Delete the folder "
                  "and run `formwork init` again.", file=sys.stderr)
            return 2
        print("ERROR: no formwork/ folder here, or in any folder above this "
              "one.", file=sys.stderr)
        print("       Run `formwork init` first, or change to a project that "
              "has one.", file=sys.stderr)
        return 2
    program = os.path.join(kit, rel)
    if not os.path.isfile(program):
        print("ERROR: %s is missing from the kit at %s" % (rel, kit),
              file=sys.stderr)
        return 2
    if not os.access(program, os.X_OK):
        make_runnable(kit)
    project = os.path.dirname(kit)
    try:
        return subprocess.run([sys.executable, program] + list(args),
                              cwd=project).returncode
    except OSError as e:
        print("ERROR: could not run %s: %s" % (rel, e), file=sys.stderr)
        return 2


TOTAL = re.compile(r"(\d+) of \1 behaved as specified|(\d+) passed, 0 failed")


def cmd_test():
    kit = find_kit()
    if kit is None:
        print("ERROR: no formwork/ folder here.", file=sys.stderr)
        return 2
    # The tests exercise the guards with paths relative to the project root,
    # so they must run from there. Running them from wherever the person
    # happened to be standing failed 44 of them for the wrong reason.
    project = os.path.dirname(kit)
    failed = []
    total = 0
    for t in TESTS:
        full = os.path.join(kit, t)
        if not os.path.isfile(full):
            continue
        print("\n%s" % t, flush=True)
        p = subprocess.run([sys.executable, full], cwd=project,
                           capture_output=True, text=True)
        sys.stdout.write(p.stdout)
        sys.stderr.write(p.stderr)
        if p.returncode != 0:
            failed.append(t)
        # Add the suites up. The README states one number and this command
        # used to end on the smallest of five, so a reader checking the claim
        # concluded it was inflated twelvefold.
        for m in TOTAL.finditer(p.stdout):
            total += int(m.group(1) or m.group(2))
    print("")
    if failed:
        print("FAILED: %s" % ", ".join(failed), file=sys.stderr)
        return 1
    print("%d tests, all passed" % total)
    return 0


def cmd_version():
    """Which version this is.

    Every bug report worth having starts with this, and the first version of
    this command did not have it.
    """
    v = "unknown"
    if _version is not None:
        try:
            v = _version("formwork-kit")
        except Exception:
            v = "not installed as a package"
    print("formwork-kit %s" % v)
    kit = find_kit()
    if kit:
        print("kit at %s" % kit)
    return 0


def cmd_where():
    kit = find_kit()
    if kit is None:
        broken = find_kit(complete_only=False)
        if broken:
            print("An incomplete kit at %s. formwork/check/run is missing."
                  % broken)
            print("Delete that folder and run `formwork init` again.")
            return 1
        print("No kit here. `formwork init` puts one in this folder.")
        return 1
    print("kit      %s" % kit)
    print("project  %s" % os.path.dirname(kit))
    print("command  %s" % HERE)
    return 0


def usage():
    print("formwork <command>")
    print("")
    for name, what in COMMANDS:
        print("  %-8s %s" % (name, what))
    print("")
    print("Everything here runs a program inside your project's formwork/")
    print("folder. You can always run those directly instead.")
    return 0


def main(argv=None):
    argv = list(sys.argv if argv is None else argv)
    if len(argv) >= 2 and argv[1] in ("--version", "-V"):
        return cmd_version()
    if len(argv) < 2 or argv[1] in ("help", "-h", "--help"):
        return usage()
    cmd, rest = argv[1], argv[2:]
    if cmd == "init":
        return cmd_init(rest)
    if cmd == "install":
        return run_in_kit("install", rest)
    if cmd == "setup":
        return run_in_kit("setup", rest)
    if cmd == "check":
        return run_in_kit(os.path.join("check", "run"), rest)
    if cmd == "demo":
        return run_in_kit(os.path.join("check", "run"), ["--demo-fail"] + rest)
    if cmd == "roles":
        return run_in_kit("build", rest)
    if cmd == "test":
        return cmd_test()
    if cmd == "where":
        return cmd_where()
    if cmd in ("version", "--version", "-V"):
        return cmd_version()
    if cmd == "record":
        kit = find_kit()
        target = os.path.dirname(kit) if kit else "."
        return run_in_kit(os.path.join("check", "checks", "kit-integrity"),
                          ["--record", target] + rest)
    print("ERROR: no such command: %s" % cmd, file=sys.stderr)
    print("", file=sys.stderr)
    usage()
    return 2


if __name__ == "__main__":
    sys.exit(main())
