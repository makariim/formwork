#!/usr/bin/env python3
"""Prove the end-of-turn gate blocks, and prove the budget behaves.

The budget is the part that matters. A guard that refuses once was defeated
under test elsewhere; a guard that refuses for ever strands the work. This
exercises both edges and everything between.

Python 3, standard library only, no dependencies.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GUARD = os.path.join(HERE, "quality-gate")
ALLOW, REFUSE = 0, 2
results = []


def check(name, got, want, output=""):
    ok = got == want
    results.append(ok)
    print("  [%s] %-50s expected %d, got %d"
          % ("pass" if ok else "FAIL", name[:50], want, got))
    if not ok and output:
        for line in output.strip().split("\n")[:4]:
            print("        %s" % line)


def build(aggregate_exit, config="", state=None):
    """A throwaway project whose aggregate exits however we say."""
    root = tempfile.mkdtemp(prefix="fw-gate-")
    os.makedirs(os.path.join(root, "formwork", "check"))
    gate = os.path.join(root, "formwork", "check", "run")
    open(gate, "w").write(
        "#!/usr/bin/env python3\n"
        "print('aggregate output')\n"
        "import sys; sys.exit(%d)\n" % aggregate_exit)
    os.chmod(gate, 0o755)
    open(os.path.join(root, ".formwork.toml"), "w").write(config)
    open(os.path.join(root, "README.md"), "w").write("a project\n")
    if state:
        os.makedirs(state, exist_ok=True)
    return root


def run(root, session="s1", state=None, env_extra=None):
    env = dict(os.environ)
    env["CLAUDE_PROJECT_DIR"] = root
    env["FORMWORK_STATE_DIR"] = state or os.path.join(root, "state")
    env.pop("FORMWORK_GATE", None)
    if env_extra:
        env.update(env_extra)
    p = subprocess.run([sys.executable, GUARD, "--format", "claude-code"],
                       capture_output=True, text=True, env=env,
                       input=json.dumps({"session_id": session}))
    return p.returncode, (p.stdout + p.stderr).strip()


def main():
    print("THE END-OF-TURN GATE")

    root = build(0)
    code, out = run(root)
    check("green aggregate: the turn may finish", code, ALLOW, out)
    shutil.rmtree(root)

    root = build(1)
    code, out = run(root)
    check("red aggregate: the turn is refused", code, REFUSE, out)
    shutil.rmtree(root)

    # The aggregate itself failing to run is not a pass.
    root = build(0)
    os.remove(os.path.join(root, "formwork", "check", "run"))
    code, out = run(root)
    check("no aggregate at all: refused, not waved through", code, REFUSE, out)
    shutil.rmtree(root)

    print()
    print("THE BUDGET")

    root = build(1, config='[strength]\ngate_budget = "2"\n')
    state = os.path.join(root, "state")
    seq = []
    for i in range(4):
        code, out = run(root, session="budget-test", state=state)
        seq.append(code)
    ok = seq == [REFUSE, REFUSE, ALLOW, ALLOW]
    results.append(ok)
    print("  [%s] %-50s %s"
          % ("pass" if ok else "FAIL", "refuses twice, then stands aside", seq))
    # And it must say plainly that nothing was fixed.
    code, out = run(root, session="budget-test", state=state)
    told = "NOTHING BELOW HAS BEEN FIXED" in out
    results.append(told)
    print("  [%s] %-50s" % ("pass" if told else "FAIL",
                            "when spent, it says nothing was fixed"))
    shutil.rmtree(root)

    # A different session gets its own budget.
    root = build(1, config='[strength]\ngate_budget = "1"\n')
    state = os.path.join(root, "state")
    run(root, session="one", state=state)
    code, _ = run(root, session="one", state=state)
    first_spent = code == ALLOW
    code, _ = run(root, session="two", state=state)
    second_fresh = code == REFUSE
    results.append(first_spent and second_fresh)
    print("  [%s] %-50s" % ("pass" if first_spent and second_fresh else "FAIL",
                            "each session gets its own budget"))
    shutil.rmtree(root)

    print()
    print("STRENGTH")

    for level, want in (("block", REFUSE), ("warn", ALLOW), ("off", ALLOW)):
        root = build(1, config='[strength]\naggregate_gate = "%s"\n' % level)
        code, out = run(root, session="strength-%s" % level)
        check("red aggregate at strength=%s" % level, code, want, out)
        shutil.rmtree(root)

    # warn must still say what happened rather than going quiet.
    root = build(1, config='[strength]\naggregate_gate = "warn"\n')
    code, out = run(root, session="warn-loud")
    loud = "red" in out.lower()
    results.append(loud)
    print("  [%s] %-50s" % ("pass" if loud else "FAIL",
                            "warn still reports the failure"))
    shutil.rmtree(root)

    print()
    print("REFUSING TO GUESS")

    root = build(1)
    env = dict(os.environ)
    env["CLAUDE_PROJECT_DIR"] = root
    p = subprocess.run([sys.executable, GUARD, "--format", "nope"],
                       capture_output=True, text=True, env=env, input="{}")
    check("an unknown runtime: refused", p.returncode, REFUSE)
    p = subprocess.run([sys.executable, GUARD],
                       capture_output=True, text=True, env=env, input="")
    check("no arguments at all: refused", p.returncode, REFUSE)
    shutil.rmtree(root)

    print()
    print("%d of %d behaved as specified." % (sum(1 for r in results if r),
                                              len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
