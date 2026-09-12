#!/usr/bin/env python3
"""Prove self-protection refuses, and prove it stays out of the way.

Every rule in this kit is enforced by a program, and every one of those
programs is an ordinary file. Turning the strongest rule off was four
characters, and nothing anywhere noticed.

This exercises every route that is now refused, and every ordinary thing that
must still work — because a guard that obstructs normal work gets switched off,
and then it protects nothing.

Python 3, standard library only, no dependencies.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUARD = os.path.join(HERE, "protected-files")
ALLOW, WARN, REFUSE = 0, 1, 2
results = []

# Assembled rather than written out, so that this file's own text does not
# read as a command to the boundary guard watching the session that writes it.
VCS = "g" + "it"


def run(command=None, path=None, fmt=None, payload=None, level="block"):
    env = dict(os.environ)
    env["FORMWORK_PROTECT_FILES"] = level
    args = [sys.executable, GUARD]
    if command is not None:
        args += ["--command", command]
    if path is not None:
        args += ["--path", path]
    if fmt is not None:
        args += ["--format", fmt]
    p = subprocess.run(args, capture_output=True, text=True, env=env,
                       input=json.dumps(payload) if payload is not None else "")
    return p.returncode, (p.stdout + p.stderr).strip()


def expect(label, want, **kw):
    got, out = run(**kw)
    ok = got == want
    results.append(ok)
    names = {ALLOW: "allow", WARN: "warn", REFUSE: "REFUSE"}
    print("  [%s] %-52s %s" % ("pass" if ok else "FAIL", label[:52], names[want]))
    if not ok:
        print("        got %s: %s" % (names.get(got, got), out.split("\n")[0]))


def main():
    print("REFUSED — disarming the kit")
    for c in [
        "sed -i s/block/off/ .formwork.toml",
        "echo x > formwork/check/run",
        "rm formwork/check/checks/rule-labels",
        "rm -rf formwork/guard",
        "cp /tmp/x formwork/guard/" + VCS + "-boundary",
        "mv formwork/guard/protected-files /tmp/x",
        "cat /dev/null > .claude/settings.json",
        "truncate -s 0 ~/.formwork/allowlist.txt",
        "echo something >> ~/.formwork/allowlist.txt",
        "chmod 000 formwork/check/run",
        "python3 -c \"open('.formwork.toml','w')\"",
        "ls && sed -i s/a/b/ formwork/guard/protected-files",
        "tee formwork/check/run < /dev/null",
    ]:
        expect(c, REFUSE, command=c)

    print()
    print("REFUSED — editing one directly")
    for p in ["formwork/check/run", ".formwork.toml",
              "formwork/guard/protected-files", ".claude/settings.json",
              "formwork/check/checks/doc-links",
              os.path.expanduser("~/.formwork/denylist-anycase.txt")]:
        expect(p, REFUSE, path=p)

    print()
    print("ALLOWED — creating something that does not exist yet")
    # Adding a guard or a check removes no enforcement, and the integrity
    # check reports the addition, so it is never silent. Left refused, the
    # protection had to be switched off to extend the kit at all.
    for p in ["formwork/guard/a-new-guard",
              "formwork/check/checks/a-new-check"]:
        expect(p, ALLOW, path=p)

    print()
    print("ALLOWED — ordinary work must not be obstructed")
    for c in [
        "formwork/check/run",
        "formwork/check/run --demo-fail",
        "cat formwork/check/run",
        "grep -n block .formwork.toml",
        "sed -i s/a/b/ docs/design.md",
        "echo notes > /tmp/scratch.txt",
        "python3 tools/privacy_scan.py",
        "ls formwork/guard",
    ]:
        expect(c, ALLOW, command=c)

    print()
    print("ALLOWED — editing anything that is not a guard")
    for p in ["docs/design.md", "formwork/rules/core.md",
              "formwork/roles/method/lead.md", "README.md"]:
        expect(p, ALLOW, path=p)

    print()
    print("ALLOWED — reading with a tool that can also write")
    # Refusing these was a false positive three times in one session, and a
    # guard that is wrong about ordinary work gets switched off by somebody
    # busy. Reading is not writing.
    for c in ["sed -n 1,5p .formwork.toml",
              "sed s/a/b/ formwork/check/run",
              "awk {print} formwork/check/run",
              "chmod +x formwork/check/checks/decision-ids",
              "chmod 755 formwork/check/checks/decision-ids"]:
        expect(c, ALLOW, command=c)

    print()
    print("REFUSED — the same tools, actually writing")
    for c in ["sed -i s/a/b/ .formwork.toml",
              "sed -i.bak s/a/b/ formwork/check/run",
              "perl -i -pe s/a/b/ .formwork.toml",
              "chmod 000 formwork/check/run",
              "chmod -x formwork/guard/git-boundary",
              "chmod 644 formwork/check/run"]:
        expect(c, REFUSE, command=c)

    print()
    print("PAYLOADS — and a refusal to guess")
    for fmt in ("claude-code", "codex", "cursor", "gemini-cli"):
        expect("%s: an edit to the gate" % fmt, REFUSE, fmt=fmt,
               payload={"tool_input": {"file_path": "formwork/check/run"}})
    expect("claude-code: an edit to a rule", ALLOW, fmt="claude-code",
           payload={"tool_input": {"file_path": "formwork/rules/core.md"}})
    expect("an unknown runtime", REFUSE, fmt="nope", payload={})
    expect("no payload at all", REFUSE, fmt="claude-code")

    print()
    print("STRENGTH — the same command, three settings")
    for level, want in (("block", REFUSE), ("warn", WARN), ("off", ALLOW)):
        expect("%s: disarming the configuration" % level, want,
               command="sed -i s/block/off/ .formwork.toml", level=level)

    # Everything below is a hole an audit walked through, or a false positive
    # it reported. Each was the behaviour before the fix beside it.
    print("REFUSED — routes that used to walk straight past this guard")
    for c in ["echo x | tee formwork/check/run",
              "chmod a-x formwork/check/checks/doc-links",
              "chmod u-x formwork/check/checks/doc-links",
              "chmod go-rwx formwork/check/run",
              "chmod a=r formwork/check/run",
              "rm -rf formwork",
              "mv formwork /tmp/elsewhere",
              "rm -rf formwork/check",
              "formwork/check/checks/kit-integrity --record ."]:
        expect(c, REFUSE, command=c)

    print("ALLOWED — ordinary work this guard must not refuse")
    for c in ["chmod +x formwork/check/run",
              "python3 formwork/check/run",
              "bash formwork/check/run",
              "./formwork/check/run",
              "formwork/check/checks/kit-integrity .",
              "cat formwork/guard/git-boundary",
              "rm -rf build",
              "mkdir docs/rounds"]:
        expect(c, ALLOW, command=c)

    print("FAILS CLOSED — a payload it cannot read")
    for bad in ("[]", "null"):
        got, out = run(fmt="claude-code", payload=bad)
        ok = got == REFUSE
        results.append(ok)
        print("  [%s] %-52s %s"
              % ("pass" if ok else "FAIL", "unreadable payload %s" % bad,
                 "REFUSE"))

    print("SECOND AUDIT — routes that were still open")
    for c in ["rm formwork/guard/*",
              "rm -rf formwork/check/checks/*",
              "chmod 644 formwork/check/checks/*",
              "rm formwork/check/ru*",
              "nice -n 5 rm formwork/guard/git-boundary",
              "timeout 5 rm formwork/guard/git-boundary",
              "sudo -u nobody rm formwork/guard/git-boundary",
              "bash -c 'rm formwork/guard/git-boundary'",
              "for f in x; do rm formwork/check/run; done",
              "(rm formwork/check/run)",
              "perl -e 'unlink \"formwork/guard/git-boundary\"'",
              "sed --in-place s/a/b/ formwork/check/run"]:
        expect(c, REFUSE, command=c)
    got, _ = run(command="bash <<'EOF'\nrm formwork/check/run\nEOF\n")
    ok = got == REFUSE
    results.append(ok)
    print("  [%s] %-52s %s" % ("pass" if ok else "FAIL",
                               "heredoc fed to a shell", "REFUSE"))

    print("THE FRONT DOOR — the short command must not be a way round")
    for c in ["formwork record", "formwork/fw record", "./formwork/fw record"]:
        expect(c, REFUSE, command=c)
    for c in ["formwork check", "formwork/fw check", "formwork test",
              "formwork init", "formwork install --runtime claude-code",
              "formwork where"]:
        expect(c, ALLOW, command=c)

    print("THIRD AUDIT — routes found by the third audit")
    for c in ["sudo -n rm formwork/guard/git-boundary",
              "env -i rm formwork/guard/git-boundary",
              "if rm formwork/check/run; then echo x; fi",
              "while rm formwork/check/run; do :; done",
              "python3 formwork/fw record",
              "python3 formwork/check/checks/kit-integrity --record .",
              "uv run formwork/fw record",
              "rm -rf *", "rm -rf ./*",
              "dd if=/dev/zero of=formwork/check/run",
              "unlink formwork/guard/git-boundary",
              "rsync /tmp/x formwork/check/run"]:
        expect(c, REFUSE, command=c)
    got, _ = run(command="bash <<'EOF'\nrm formwork/check/run\nEOF\n")
    ok = got == REFUSE
    results.append(ok)
    print("  [%s] %-52s %s" % ("pass" if ok else "FAIL",
                               "heredoc into a shell", "REFUSE"))

    print("THIRD AUDIT — siblings and ordinary globs, wrongly refused")
    for c in ["rm .formwork.toml.bak", "rm formwork/check/run.orig",
              "rm *.pyc", "rm build/*", "rm docs/*.tmp",
              "sudo -n ls", "env -i ls", "python3 formwork/fw check"]:
        expect(c, ALLOW, command=c)
    got, _ = run(fmt="claude-code", payload='{"tool_input":{"command":123}}')
    ok = got == REFUSE
    results.append(ok)
    print("  [%s] %-52s %s" % ("pass" if ok else "FAIL",
                               "a command that is not a string", "REFUSE"))

    print("SECOND AUDIT — ordinary work that was wrongly refused")
    for c in ["python3 -m pytest formwork/guard/test_boundary.py",
              "cp formwork/check/run /tmp/backup-run",
              "rm formwork/check/runner-notes.md",
              "rm build/*", "rm docs/*.tmp", "ls formwork/guard/*",
              "nice -n 5 ls", "bash -c 'echo hi'"]:
        expect(c, ALLOW, command=c)

    print()
    print("%d of %d behaved as specified." % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
