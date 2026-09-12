#!/usr/bin/env python3
"""Prove the boundary refuses, and prove it lets reading through.

Three things are tested, and the third is the unusual one:

    REFUSED   commands that change the repository
    ALLOWED   commands that only read it, because the report needs them
    KNOWN MISS  evasions this guard does not catch

The third group is asserted deliberately. A blind spot that is tested is a
blind spot somebody has to delete a test to pretend away. An unqualified pass
would read as total coverage, and this is not that.

Python 3, standard library only, no dependencies.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUARD = os.path.join(HERE, "git-boundary")
ALLOW, WARN, REFUSE = 0, 1, 2
results = []


def run(command=None, fmt=None, payload=None, level=None):
    env = dict(os.environ)
    # Each case states its own strength, so a stray setting in the shell this
    # runs from cannot quietly change the result.
    env["FORMWORK_GIT_BOUNDARY"] = level or "block"
    args = [sys.executable, GUARD]
    if command is not None:
        args += ["--command", command]
    if fmt is not None:
        args += ["--format", fmt]
    p = subprocess.run(args, capture_output=True, text=True, env=env,
                       input=json.dumps(payload) if payload is not None else "")
    return p.returncode, (p.stdout + p.stderr).strip()


def expect(label, command, want):
    got, out = run(command=command)
    ok = got == want
    results.append(ok)
    names = {ALLOW: "allow", WARN: "warn", REFUSE: "REFUSE"}
    print("  [%s] %-44s %s" % ("pass" if ok else "FAIL", command, names[want]))
    if not ok:
        print("        got %s: %s" % (names.get(got, got), out.split("\n")[0]))


def main():
    print("REFUSED — changes the repository")
    for c in [
        "git commit -m 'x'",
        "git add .",
        "git push origin main",
        "git merge feature",
        "git rebase -i HEAD~3",
        "git reset --hard",
        "git stash",
        "git tag -a v1 -m x",
        "git branch -D old",
        "git config user.name --add",
        "git remote add origin git@example.com:a/b.git",
        "git worktree add ../wt",
        "git checkout -b new-branch",
        "git switch -c new-branch",
        "gh pr create --fill",
        "gh pr merge 12",
        "glab mr create",
        # wrappers and compound commands
        "sudo git commit -m x",
        "FOO=1 git commit -m x",
        "cd subdir && git commit -m x",
        "git status && git commit -m x",
        "git -C /elsewhere commit -m x",
        "git -c user.name=x commit -m y",
        "echo hi; git push",
        # A subcommand held in a variable cannot be read, so it is not on the
        # read-only list, so it is refused. Caution is the default.
        "C=commit; git $C -m x",
    ]:
        expect("refuse", c, REFUSE)

    print()
    print("ALLOWED — reading only, and the report depends on it")
    for c in [
        "git status",
        "git status --short",
        "git diff",
        "git diff --cached --name-only",
        "git log --oneline -20",
        "git show HEAD",
        "git ls-files",
        "git rev-parse HEAD",
        "git branch",
        "git branch --list",
        "git tag",
        "git remote -v",
        "git worktree list",
        "git config --get user.name",
        "git blame README.md",
        "git describe --tags",
        "ls -la",
        "python3 tools/privacy_scan.py",
        "grep -rn TODO .",
        "git diff && git status",
    ]:
        expect("allow", c, ALLOW)

    print()
    print("KNOWN MISS — asserted, so nobody mistakes these for covered")
    for c in [
        # the whole command is assembled at run time, so the word "git"
        # never appears for the guard to find
        "eval $(echo git commit -m x)",
        # a script on disk commits; this reads the command, not the script
        "./scripts/release.sh",
        "make release",
    ]:
        expect("known miss", c, ALLOW)

    print()
    print("PAYLOADS — the four runtimes, and a refusal to guess")
    for fmt in ("claude-code", "codex", "cursor", "gemini-cli"):
        code, _ = run(fmt=fmt, payload={"tool_input": {"command": "git push"}})
        ok = code == REFUSE
        results.append(ok)
        print("  [%s] %-44s REFUSE" % ("pass" if ok else "FAIL", fmt))

    code, _ = run(fmt="claude-code", payload={"tool_input": {"command": "git log"}})
    ok = code == ALLOW
    results.append(ok)
    print("  [%s] %-44s allow" % ("pass" if ok else "FAIL", "claude-code, a read"))

    # Fails closed. A guard that cannot decide refuses, because a boundary
    # that fails open is a boundary nobody notices has gone.
    code, out = run(fmt="some-other-tool", payload={})
    ok = code == REFUSE
    results.append(ok)
    print("  [%s] %-44s REFUSE, not allow"
          % ("pass" if ok else "FAIL", "an unknown runtime"))

    code, out = run(fmt="claude-code", payload=None)
    ok = code == REFUSE
    results.append(ok)
    print("  [%s] %-44s REFUSE, not allow"
          % ("pass" if ok else "FAIL", "no payload at all"))

    print()
    print("STRENGTH — the same command, three settings")
    for level, want, label in (("block", REFUSE, "block: refuses"),
                               ("warn", WARN, "warn: runs, and says so"),
                               ("off", ALLOW, "off: runs, silently")):
        code, _ = run(command="git commit -m x", level=level)
        ok = code == want
        results.append(ok)
        print("  [%s] %-44s %s"
              % ("pass" if ok else "FAIL", label,
                 {ALLOW: "allow", WARN: "warn", REFUSE: "REFUSE"}[want]))

    # A read is allowed whatever the strength; the report depends on it.
    for level in ("block", "warn", "off"):
        code, _ = run(command="git status", level=level)
        ok = code == ALLOW
        results.append(ok)
        print("  [%s] %-44s allow"
              % ("pass" if ok else "FAIL", "reads pass at strength=%s" % level))

    # Everything below is a hole an audit walked through. Each one was
    # allowed before the fix that follows it in git history.
    print("WRAPPERS — a write hidden behind something else")
    for c in ['bash -c "git commit -m x"',
              'sh -c "git push"',
              'eval "git push"',
              'nice -n 5 git push',
              'timeout 60 git push',
              'env -u FOO git push',
              'sudo -u somebody git push',
              'echo $(git commit -m x)']:
        expect(c, c, REFUSE)

    print("WRAPPERS — and the same wrappers around innocent work")
    for c in ['bash -c "echo hello"', 'nice -n 5 ls', 'timeout 60 git status']:
        expect(c, c, ALLOW)

    print("WRITES WITH NO OPTION AT ALL")
    expect("git config core.hooksPath /dev/null",
           "git config core.hooksPath /dev/null", REFUSE)
    expect("git checkout somefile.py", "git checkout somefile.py", REFUSE)

    print("READS ONCE WRONGLY REFUSED")
    for c in ['git stash list', 'git stash show', 'git notes list',
              'git cherry -v', 'git config --get user.name']:
        expect(c, c, ALLOW)
    expect("git stash", "git stash", REFUSE)

    print("FAILS CLOSED — a payload it cannot read")
    for bad in ("[]", "null", '{"tool_input":{"command":5}}'):
        code, out = run(fmt="claude-code", payload=bad)
        ok = code == REFUSE
        results.append(ok)
        print("  [%s] %-44s %s"
              % ("pass" if ok else "FAIL", "unreadable payload %s" % bad[:20],
                 "REFUSE"))

    print("SECOND AUDIT — grouping, loops, aliases, heredocs into a shell")
    for c in ['(git push)', '{ git push; }',
              'for f in x; do git push; done',
              'while true; do git commit -m x; done',
              'if true; then git push; fi',
              '\\git commit',
              'git submodule foreach git push',
              'gh -R owner/repo pr create',
              'gh --repo a/b pr create',
              'gh api -X POST /repos/a/b/pulls',
              'git config core.hooksPath /dev/null']:
        expect(c, c, REFUSE)
    code, out = run(command="bash <<'EOF'\ngit push\nEOF\n")
    ok = code == REFUSE
    results.append(ok)
    print("  [%s] %-44s %s" % ("pass" if ok else "FAIL",
                               "heredoc fed to a shell", "REFUSE"))

    print("THIRD AUDIT — wrappers that swallowed the command")
    for c in ['sudo -n git push', 'env -i git push', 'sudo -s git push',
              'timeout -k 1 30 git push',
              'git symbolic-ref HEAD refs/heads/evil']:
        expect(c, c, REFUSE)
    for pre in ('bash', 'sudo -n bash', 'nice -n 5 bash', 'timeout 60 bash',
                'env FOO=1 bash'):
        code, out = run(command="%s <<'EOF'\ngit push\nEOF\n" % pre)
        ok = code == REFUSE
        results.append(ok)
        print("  [%s] %-44s %s" % ("pass" if ok else "FAIL",
                                   "heredoc into: " + pre, "REFUSE"))

    print("THIRD AUDIT — reads and branch moves wrongly refused")
    for c in ['git stash show -p', 'git checkout main', 'git checkout v1.2.0',
              'git symbolic-ref --short HEAD',
              'git config --local user.email 2>/dev/null']:
        expect(c, c, ALLOW)
    for name in ('retrieval.md', 'node-setup.md', 'ruby-guide.md'):
        code, out = run(command="cat > docs/%s <<'EOF'\ngit push\nEOF\n" % name)
        ok = code == ALLOW
        results.append(ok)
        print("  [%s] %-44s %s" % ("pass" if ok else "FAIL",
                                   "heredoc written to " + name, "allow"))

    print("SECOND AUDIT — reads that were wrongly refused")
    for c in ['git symbolic-ref --short HEAD',
              'git config --global --get user.name',
              'git config --list --global',
              'git apply --check patch.diff',
              'git fetch origin',
              'for f in x; do echo $f; done',
              'bash -c "echo hello"',
              'gh pr list', 'gh api /repos/a/b']:
        expect(c, c, ALLOW)
    code, out = run(command="cat > notes.md <<'EOF'\ngit commit -m x\nEOF\n")
    ok = code == ALLOW
    results.append(ok)
    print("  [%s] %-44s %s" % ("pass" if ok else "FAIL",
                               "heredoc written to a file", "allow"))

    print()
    print("%d of %d behaved as specified." % (sum(results), len(results)))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
