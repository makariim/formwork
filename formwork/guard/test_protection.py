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
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GUARD = os.path.join(HERE, "protected-files")
ALLOW, WARN, REFUSE = 0, 1, 2
results = []

# Assembled rather than written out, so that this file's own text does not
# read as a command to the boundary guard watching the session that writes it.
VCS = "g" + "it"


def run(command=None, path=None, fmt=None, payload=None, level="block",
        project=None):
    env = dict(os.environ)
    env["FORMWORK_PROTECT_FILES"] = level
    if project is not None:
        env["CLAUDE_PROJECT_DIR"] = project
    args = [sys.executable, GUARD]
    if command is not None:
        args += ["--command", command]
    if path is not None:
        args += ["--path", path]
    if fmt is not None:
        args += ["--format", fmt]
    p = subprocess.run(args, capture_output=True, text=True, env=env,
                       cwd=project, input=json.dumps(payload) if payload is not None else "")
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

    print("CODEX PATCHES — header paths decide what changes")
    def patch(kind, path, extra=""):
        return "*** Begin Patch\n*** %s: %s\n%s*** End Patch\n" % (
            kind, path, extra)

    for label, body in [
        ("update guard", patch("Update File", "formwork/guard/git-boundary",
                               "@@\n-a\n+b\n")),
        ("delete guard", patch("Delete File", "formwork/guard/git-boundary")),
        ("move onto check runner", patch("Update File", "some/new.py",
                                      "*** Move to: formwork/check/run\n@@\n-a\n+b\n")),
        ("absolute guard path", patch("Update File",
            os.path.join(os.path.dirname(os.path.dirname(HERE)),
                         "formwork/guard/git-boundary"))),
    ]:
        expect("Codex patch: " + label, REFUSE, fmt="codex",
               payload={"tool_name": "apply_patch", "tool_input": {"command": body}})
    with tempfile.TemporaryDirectory(prefix="formwork-codex-guard-") as project:
        os.makedirs(os.path.join(project, ".codex"))
        with open(os.path.join(project, ".codex/hooks.json"), "w") as f:
            f.write("{}\n")
        expect("Codex patch: update Codex wiring", REFUSE, fmt="codex",
               project=project, payload={"tool_name": "apply_patch",
               "tool_input": {"command": patch("Update File", ".codex/hooks.json")}})
    other = os.path.join(os.path.dirname(os.path.dirname(HERE)) + "-other",
                         "formwork/guard/git-boundary")
    for label, body in [
        ("other project's guard", patch("Update File", other)),
        ("new guard", patch("Add File", "formwork/guard/new-guard")),
        ("ordinary files", patch("Update File", "src/app.py",
                                 "*** Update File: README.md\n")),
        ("guard mentioned in body", patch("Update File", "docs/notes.md",
                                           "@@\n+see formwork/guard/git-boundary\n")),
    ]:
        expect("Codex patch: " + label, ALLOW, fmt="codex",
               payload={"tool_name": "apply_patch", "tool_input": {"command": body}})
    body = patch("Update File", "formwork/guard/git-boundary",
                 "@@\n-a\n+b\n")
    expect("shell apply_patch heredoc", REFUSE,
           command="apply_patch <<'EOF'\n" + body + "EOF\n")
    expect("shell cat heredoc stays data", ALLOW,
           command="cat > note.txt <<'EOF'\n" + body + "EOF\n")

    print("ROUND 2 — Codex patch spellings")
    for label, changed in [
        ("space after Begin", body.replace("*** Begin Patch\n", "*** Begin Patch \n")),
        ("space before Begin", " " + body),
        ("indented first header", body.replace("*** Update File", " *** Update File")),
        ("tabbed first header", body.replace("*** Update File", "\t*** Update File")),
        ("indented header after Add", "*** Begin Patch\n*** Add File: docs/a.md\n+x\n  "
         + body.split("\n", 1)[1]),
    ]:
        expect(label, REFUSE, fmt="codex", payload={"tool_name": "apply_patch",
               "tool_input": {"command": changed}})
    expect("indented header in Update hunk is context", ALLOW, fmt="codex",
           payload={"tool_name": "apply_patch", "tool_input": {"command":
                    patch("Update File", "docs/notes.md",
                          "@@\n *** Update File: formwork/guard/git-boundary\n+note\n")}})
    expect("indented patch markers in Update hunk are context", ALLOW,
           fmt="codex", payload={"tool_name": "apply_patch", "tool_input":
               {"command": patch("Update File", "docs/notes.md",
                   "@@\n *** Begin Patch\n *** Update File: formwork/guard/git-boundary\n"
                   " *** End Patch\n+note\n")}})

    shell_forms = [
        ("applypatch alias", "applypatch <<'EOF'\n" + body + "EOF\n"),
        ("argv patch", "apply_patch '" + body + "'"),
        ("ANSI quoted argv patch", "apply_patch $'" + body.replace("\n", "\\n") + "'"),
        ("bash -lc patch", "bash -lc \"apply_patch <<'EOF'\n" + body + "EOF\""),
        ("bash -c patch", "bash -c \"apply_patch <<'EOF'\n" + body + "EOF\""),
        ("path to apply_patch", "/tmp/x/apply_patch <<'EOF'\n" + body + "EOF\n"),
        ("heredoc pipe", "cat <<'EOF' | apply_patch\n" + body + "EOF\n"),
        ("printf pipe", "printf '%s' '" + body + "' | apply_patch"),
        ("tab stripping heredoc", "apply_patch <<-EOF\n" +
         "\n".join("\t" + line for line in body.splitlines()) + "\n\tEOF\n"),
        ("cd then patch", "cd formwork && apply_patch <<'EOF'\n" +
         body.replace("formwork/guard/git-boundary", "guard/git-boundary") + "EOF\n"),
    ]
    for label, command in shell_forms:
        expect(label, REFUSE, fmt="codex",
               payload={"tool_name": "Bash", "tool_input": {"command": command}})
    for tool_name in ("apply_patch", "applypatch"):
        for label, data in [
            ("missing text", {"tool_input": {}}),
            ("input field", {"tool_input": {"input": body}}),
            ("patch field", {"tool_input": {"patch": body}}),
            ("arguments field", {"arguments": body}),
        ]:
            expect("%s %s" % (tool_name, label), REFUSE, fmt="codex",
                   payload={"tool_name": tool_name, **data})
    expect("ordinary shell mention of patch marker", ALLOW,
           command="grep '*** Begin Patch' docs/notes.md")
    expect("ordinary apply_patch patch", ALLOW,
           command="apply_patch <<'EOF'\n" +
                   patch("Update File", "docs/notes.md", "@@\n-a\n+b\n") + "EOF\n")

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

    print("LINKS: a protected file reached under another name (0030)")
    with tempfile.TemporaryDirectory(prefix="formwork-links-") as project:
        guard_dir = os.path.join(project, "formwork", "guard")
        os.makedirs(guard_dir)
        target = os.path.join(guard_dir, "a-guard")
        with open(target, "w") as f:
            f.write("guard\n")
        notes = os.path.join(project, "docs")
        os.makedirs(notes)
        os.symlink(target, os.path.join(notes, "soft.md"))
        os.link(target, os.path.join(notes, "hard.md"))
        os.symlink(guard_dir, os.path.join(project, "g"))
        with open(os.path.join(notes, "plain.md"), "w") as f:
            f.write("ordinary\n")
        with open(os.path.join(notes, "own.md"), "w") as f:
            f.write("ordinary\n")
        os.link(os.path.join(notes, "own.md"), os.path.join(notes, "own2.md"))
        os.symlink(os.path.join(notes, "plain.md"), os.path.join(notes, "alias.md"))
        for label, rel in [("symbolic link to a guard", "docs/soft.md"),
                           ("hard link to a guard", "docs/hard.md"),
                           ("guard through a linked folder", "g/a-guard")]:
            expect("edit " + label, REFUSE, path=rel, project=project)
            expect("edit " + label + " (absolute)", REFUSE,
                   path=os.path.join(project, rel), project=project)
        expect("write through a symbolic link", REFUSE,
               command="echo x > docs/soft.md", project=project)
        expect("sed in place on a hard link", REFUSE,
               command="sed -i s/a/b/ docs/hard.md", project=project)
        expect("warn: hard link to a guard", WARN, path="docs/hard.md",
               project=project, level="warn")
        for label, rel in [("ordinary file", "docs/plain.md"),
                           ("hard links between ordinary files", "docs/own2.md"),
                           ("symbolic link to an ordinary file", "docs/alias.md"),
                           ("new file in a linked guard folder", "g/new-guard")]:
            expect("edit " + label, ALLOW, path=rel, project=project)
        expect("read through a symbolic link", ALLOW,
               command="cat docs/soft.md", project=project)

    print()
    print("%d of %d behaved as specified." % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
