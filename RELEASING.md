# Publishing a release

**For the maintainer.** It is here in the open because the steps are worth
copying, and because a project that hides how it ships is harder to trust. One
step near the end needs files that only exist on the maintainer's machine, and
it says so.

**The agent never runs any of these.** Every one of them changes something
outside your machine.

---

## Names

| | |
|---|---|
| **The package** | `formwork-kit` |
| **The command** | `formwork` |

Set in `pyproject.toml`. Do not change either one after the first release.

---

## Before you publish anything

```
formwork check     must say green
formwork demo      must reject every broken input
formwork test      every test must pass
```

> [!NOTE]
> **The next step is for this repository's maintainer only.** It will not work
> in a fork, and you do not need it.

This kit was extracted from two private projects, so two scanners check that
nothing from them reached the public files. They live outside the repository,
because a list of forbidden words committed next to the thing it protects
publishes the very words it guards.

```
python3 ~/.formwork/tools/privacy_scan.py .
python3 ~/.formwork/tools/overlap_scan.py .
```

**Both must say clean.** A red scan is not something to think about. It is a
stop.

---

## Bump the version

One line in `pyproject.toml`:

```toml
version = "0.1.0"
```

First number: a fork would break. Second: something was added. Third: a fix.

**A rule changing counts as breaking**, even though no code moved. Somebody's
green gate going red after an upgrade is the surprise this kit exists to
prevent.

---

## Build and check the package

**Clear out the last release first.** `twine upload dist/*` sends everything in
that folder, including artifacts from versions you already published.

```
rm -rf dist/
python3 -m pip install --upgrade build twine
python3 -m build
python3 -m twine check dist/*
```

### Check the kit is really in there

The wheel holds the kit under `formwork_cli/kit/`. The sdist holds it under
`formwork/`. **They are different, so check them differently.** Counting is
better than looking at the first twenty lines:

```
unzip -l dist/formwork_kit-*.whl | grep -c 'formwork_cli/kit/guard/'     # 6
unzip -l dist/formwork_kit-*.whl | grep -c 'formwork_cli/kit/check/checks/'  # 9
unzip -l dist/formwork_kit-*.whl | grep -c 'formwork_cli/kit/roles/'     # 29

tar tzf dist/formwork_kit-*.tar.gz | grep -c 'formwork/guard/'           # 6
tar tzf dist/formwork_kit-*.tar.gz | grep -c 'formwork/roles/'           # 29
```

**If any of those is zero, stop.** `formwork init` would put an empty folder
into somebody's project, and nobody would tell you.

Check nothing private travelled:

```
unzip -l dist/formwork_kit-*.whl \
  | grep -E '\.git/|__pycache__|\.DS_Store' \
  | grep -v fixtures
```

That should print nothing. The `grep -v fixtures` matters: the check fixtures
contain small pretend projects with their own `docs/` folders, and those are
test data, not this repository's documentation.

---

## Try it before the world does

**Use a fresh state directory.** The kit keeps one fingerprint record per
project under `~/.formwork/`, and you already have records there. Without this,
the smoke test can go red over an old record rather than over the release.

```
rm -rf /tmp/try && python3 -m venv /tmp/try
/tmp/try/bin/pip install dist/formwork_kit-*.whl

rm -rf /tmp/newproject && mkdir /tmp/newproject && cd /tmp/newproject
export FORMWORK_STATE_DIR=/tmp/trystate && rm -rf /tmp/trystate

/tmp/try/bin/formwork init
/tmp/try/bin/formwork install --runtime claude-code
/tmp/try/bin/formwork check
/tmp/try/bin/formwork test
```

**Both must be green.** If not, the release is broken for every new user and
nobody will tell you. Then `unset FORMWORK_STATE_DIR`.

## Publish

Test it on the practice server first:

```
python3 -m twine upload --repository testpypi dist/*
```

Then the real one:

```
python3 -m twine upload dist/*
```

You need an API token from `pypi.org/manage/account/token`. Never put it in a
file inside this repository.

---

## Commit, then tag

The version bump is a change like any other. Commit it before tagging, or the
tag points at a commit that does not contain it.

```
git add pyproject.toml
git commit -m "0.1.0"
git push

git tag -a v0.1.0 -m "0.1.0"
git push origin v0.1.0
```

## After publishing

**Install it the way a stranger would**, from the real index, and run the four
commands from the README. Not the wheel from `dist/`. The published one.

```
pipx install formwork-kit
```

**Then read your own project page** at `pypi.org/project/formwork-kit`.

The README is that page, and two things in it do not survive the trip. The logo
at the top is a relative path, so it shows as a broken image. Relative links
point at GitHub and will not resolve. Look at the page rather than assuming.

---

## If a release is bad

**You cannot replace a version on PyPI.** The number is used once and never
again.

**Yank it, do not delete it.**

Yanking hides the version from new installs while leaving it available to
anybody who pinned that exact number. Deleting breaks them. There is a button
for it on the project page under Manage.

Then fix the problem, bump the last number, and publish again:

```
rm -rf dist/
python3 -m build
python3 -m twine upload dist/*
```
