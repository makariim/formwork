#!/usr/bin/env python3
"""Prove the gate can fail.

The gate's whole job is refusing. A gate nobody has watched refuse is not
evidence of anything, so this exercises every way it is supposed to say no.

    green     a sound project                     -> 0
    red       a check that finds something        -> 1
    red       a broken input that does not break  -> 1
    cannot    no checks at all                    -> 2
    cannot    a check with no broken input        -> 2

Python 3, standard library only, no dependencies.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.join(HERE, "run")
results = []


def check(name, got, want, output=""):
    ok = got == want
    results.append(ok)
    print("  [%s] %-46s expected %d, got %d"
          % ("pass" if ok else "FAIL", name, want, got))
    if not ok and output:
        for line in output.strip().split("\n")[:6]:
            print("        %s" % line)


def run_gate(gate_dir, *args):
    p = subprocess.run([sys.executable, os.path.join(gate_dir, "run")] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def build_gate(project_files, checks, fixtures, passes=None):
    """A throwaway project with its own copy of the gate inside it.

    The runner takes the project root to be two levels above itself, so the
    layout here mirrors a real fork: <project>/formwork/check/.
    """
    root = tempfile.mkdtemp(prefix="formwork-gate-")
    gate = os.path.join(root, "formwork", "check")
    os.makedirs(os.path.join(gate, "checks"))
    os.makedirs(os.path.join(gate, "fixtures"))
    shutil.copy(RUN, os.path.join(gate, "run"))
    os.chmod(os.path.join(gate, "run"), 0o755)

    for rel, text in project_files.items():
        full = os.path.join(root, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8").write(text)

    for name, body in checks.items():
        p = os.path.join(gate, "checks", name)
        open(p, "w", encoding="utf-8").write(body)
        os.chmod(p, 0o755)

    for kind, table in (("must-fail", fixtures), ("must-pass", passes or {})):
        for cname, cases in table.items():
            for case, files in cases.items():
                d = os.path.join(gate, "fixtures", cname, kind, case)
                os.makedirs(d)
                for fn, text in files.items():
                    open(os.path.join(d, fn), "w", encoding="utf-8").write(text)

    return root, gate


# A check that fails when it finds a file called "wrong.md".
FINDS_WRONG = '''#!/usr/bin/env python3
import os, sys
root = sys.argv[1]
ex = [os.path.abspath(p) for p in os.environ.get("FORMWORK_EXCLUDE","").split(os.pathsep) if p]
hits = []
for dp, dns, fns in os.walk(root):
    here = os.path.abspath(dp)
    if any(here == e or here.startswith(e + os.sep) for e in ex):
        dns[:] = []
        continue
    hits += [os.path.join(dp, f) for f in fns if f == "wrong.md"]
print("%d found" % len(hits))
sys.exit(1 if hits else 0)
'''

# A check that never fails, whatever it is given. The gate must notice.
NEVER_FAILS = '''#!/usr/bin/env python3
import sys
print("all fine, always")
sys.exit(0)
'''


def main():
    print("THE GATE")

    # green - a sound project, one check, one input that does break it
    root, gate = build_gate({"README.md": "fine\\n"},
                            {"finds-wrong": FINDS_WRONG},
                            {"finds-wrong": {"has-one": {"wrong.md": "x\\n"}}},
                            {"finds-wrong": {"has-none": {"fine.md": "x\\n"}}})
    code, out = run_gate(gate)
    check("green: sound project, check proved able to fail", code, 0, out)
    shutil.rmtree(root)

    # red - the check finds something in the project
    root, gate = build_gate({"README.md": "fine\\n", "docs/wrong.md": "x\\n"},
                            {"finds-wrong": FINDS_WRONG},
                            {"finds-wrong": {"has-one": {"wrong.md": "x\\n"}}},
                            {"finds-wrong": {"has-none": {"fine.md": "x\\n"}}})
    code, out = run_gate(gate)
    check("red: a check finds something", code, 1, out)
    shutil.rmtree(root)

    # red - the broken input does not break the check
    root, gate = build_gate({"README.md": "fine\\n"},
                            {"never-fails": NEVER_FAILS},
                            {"never-fails": {"supposedly-broken": {"a.md": "x\\n"}}},
                            {"never-fails": {"fine": {"b.md": "x\\n"}}})
    code, out = run_gate(gate)
    check("red: a check that cannot fail", code, 1, out)
    shutil.rmtree(root)

    # cannot run - a check with no broken input at all
    root, gate = build_gate({"README.md": "fine\\n"},
                            {"finds-wrong": FINDS_WRONG},
                            {})
    code, out = run_gate(gate)
    check("cannot run: a check ships no broken input", code, 2, out)
    shutil.rmtree(root)

    # cannot run - nothing to run
    root, gate = build_gate({"README.md": "fine\\n"}, {}, {})
    code, out = run_gate(gate)
    check("cannot run: no checks at all", code, 2, out)
    shutil.rmtree(root)

    # the teaching mode must itself refuse when a broken input does not break
    root, gate = build_gate({"README.md": "fine\\n"},
                            {"never-fails": NEVER_FAILS},
                            {"never-fails": {"supposedly-broken": {"a.md": "x\\n"}}},
                            {"never-fails": {"fine": {"b.md": "x\\n"}}})
    code, out = run_gate(gate, "--demo-fail")
    check("red: --demo-fail catches a check that cannot fail", code, 1, out)
    shutil.rmtree(root)

    # A check that recognises the fixture's name instead of reading it. This
    # passed the gate before fixtures were anonymised.
    NAME_CHEAT = """#!/usr/bin/env python3
import sys, os
sys.exit(1 if "broken" in sys.argv[1] else 0)
"""
    root, gate = build_gate({"README.md": "fine\n"},
                            {"cheat": NAME_CHEAT},
                            {"cheat": {"broken": {"a.md": "x\n"}}},
                            {"cheat": {"ok": {"a.md": "x\n"}}})
    code, out = run_gate(gate)
    check("red: a check that reads the name, not the input", code, 1, out)
    shutil.rmtree(root)

    # A check that never returns used to hang the gate for ever.
    HANG = """#!/usr/bin/env python3
import time
time.sleep(600)
"""
    root, gate = build_gate({"README.md": "fine\n"},
                            {"slow": HANG},
                            {"slow": {"broken": {"a.md": "x\n"}}},
                            {"slow": {"ok": {"a.md": "x\n"}}})
    env_before = os.environ.get("FORMWORK_CHECK_TIMEOUT")
    os.environ["FORMWORK_CHECK_TIMEOUT"] = "2"
    code, out = run_gate(gate)
    if env_before is None:
        del os.environ["FORMWORK_CHECK_TIMEOUT"]
    else:
        os.environ["FORMWORK_CHECK_TIMEOUT"] = env_before
    check("cannot run: a check that never returns", code, 2, out)
    shutil.rmtree(root)

    # An audit removed a check with one allowed `chmod` and watched the gate
    # report green over the remaining ones. A missing check must never look
    # like a passing check.
    root, gate = build_gate({"README.md": "fine\n"},
                            {"finds-wrong": FINDS_WRONG,
                             "also-finds-wrong": FINDS_WRONG},
                            {"finds-wrong": {"has-one": {"wrong.md": "x\n"}},
                             "also-finds-wrong": {"has-one": {"wrong.md": "x\n"}}},
                            {"finds-wrong": {"has-none": {"fine.md": "x\n"}},
                             "also-finds-wrong": {"has-none": {"fine.md": "x\n"}}})
    os.chmod(os.path.join(gate, "checks", "also-finds-wrong"), 0o644)
    code, out = run_gate(gate)
    check("cannot run: a check present but not executable", code, 2, out)
    shutil.rmtree(root)

    # A malformed timeout must be status 2, not a traceback with status 1.
    root, gate = build_gate({"README.md": "fine\n"},
                            {"finds-wrong": FINDS_WRONG},
                            {"finds-wrong": {"has-one": {"wrong.md": "x\n"}}},
                            {"finds-wrong": {"has-none": {"fine.md": "x\n"}}})
    before = os.environ.get("FORMWORK_CHECK_TIMEOUT")
    os.environ["FORMWORK_CHECK_TIMEOUT"] = "not-a-number"
    code, out = run_gate(gate)
    if before is None:
        del os.environ["FORMWORK_CHECK_TIMEOUT"]
    else:
        os.environ["FORMWORK_CHECK_TIMEOUT"] = before
    check("cannot run: a timeout that is not a number", code, 2, out)
    shutil.rmtree(root)

    print()
    print("%d of %d behaved as specified." % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
