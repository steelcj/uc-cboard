#!/usr/bin/env python3
#
# source
#   project: uc-cboard
#   path: publish-cboard-release.py
#
"""
publish-cboard-release.py, publish an already-cut, already-built
uc-cboard release via gh.

Deliberate deviation from sat-doc-automa's shared publish-release.py:
that script's determinism gate builds its tarball with `git archive`
on the tagged commit, i.e. it publishes the repository's own source.
uc-cboard's release artifact is Cboard's *built* static output
(build-release.py's product), which is never committed to this repo
(decision: B, keep built output out of git; see project notes). git
archive on this repo would therefore never contain the thing being
published. This script exists because that mismatch is real, not
because the shared ceremony is being skipped out of convenience.

What this script keeps from the shared ceremony: refusal discipline
(tag must exist, must be pushed, release must not already exist),
gh as the only backend (matches decision--gh-cli-for-release-asset-
publishing), and changelog-section-as-release-notes. What it drops:
the git-archive build step and its determinism gate, replaced by
build-release.py's own guarantee (pinned upstream commit + SHA256,
recorded in the .provenance.json file it writes alongside the
tarball).

Sequence: guard (tag exists locally, tag:VERSION matches) -> guard
(tag pushed to origin) -> guard (dist/ contains a tarball, checksum,
and provenance file for this version) -> guard (gh authenticated, no
existing release for this tag) -> gh release create, attaching all
three dist/ files -> report the release URL.

Usage:
    publish-cboard-release.py
    publish-cboard-release.py --dry-run
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent

VERSION_FILE = _HERE / "VERSION"
CHANGELOG_FILE = _HERE / "CHANGELOG.md"
DIST_DIR = _HERE / "dist"
REMOTE = "origin"


def log(msg: str) -> None:
    print(f"[publish-cboard-release] {msg}")


def fail(msg: str) -> None:
    print(f"[publish-cboard-release ERROR] {msg}", file=sys.stderr)
    sys.exit(1)


def run(*args: str, check: bool = True) -> str:
    result = subprocess.run(list(args), cwd=_HERE, capture_output=True, text=True)
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        fail(f"command failed: {' '.join(args)}" + (f"\n  {detail}" if detail else ""))
    return result.stdout or ""


def git(*args: str, **kw) -> str:
    return run("git", *args, **kw)


def read_version() -> str:
    if not VERSION_FILE.is_file():
        fail(f"{VERSION_FILE.name} not found.")
    return VERSION_FILE.read_text(encoding="utf-8").strip()


def refuse_unless_tagged(tag: str, version: str) -> None:
    if not git("tag", "--list", tag).strip():
        fail(f"Tag {tag} does not exist. Cut the release first:\n"
             f"  cut-release.py {version}")
    tag_version = git("show", f"{tag}:VERSION").strip()
    if tag_version != version:
        fail(f"{tag}:VERSION is {tag_version!r} but VERSION is {version!r}.")


def refuse_unless_pushed(tag: str) -> None:
    out = git("ls-remote", "--tags", REMOTE, f"refs/tags/{tag}")
    if f"refs/tags/{tag}" not in out:
        fail(f"Tag {tag} is not on {REMOTE}. Push first:\n"
             f"  git push && git push {REMOTE} {tag}")


def find_artifacts(version: str) -> list[Path]:
    if not DIST_DIR.is_dir():
        fail(f"{DIST_DIR.name}/ not found. Run build-release.py --tag "
             f"<upstream-tag> first.")
    matches = sorted(DIST_DIR.glob(f"uc-cboard-*{version}*"))
    # Fall back to whatever is in dist/ if version isn't embedded in the
    # upstream tag string used by build-release.py's naming.
    if not matches:
        matches = sorted(DIST_DIR.glob("uc-cboard-*"))
    if not matches:
        fail(f"No artefacts found in {DIST_DIR.name}/. Run build-release.py "
             f"first.")
    tarballs = [f for f in matches if f.suffix == ".gz"]
    if not tarballs:
        fail(f"No .tar.gz artefact found in {DIST_DIR.name}/.")
    return matches


def changelog_section(version: str) -> str:
    if not CHANGELOG_FILE.is_file():
        return ""
    text = CHANGELOG_FILE.read_text(encoding="utf-8")
    heading = f"## [{version}]"
    start = text.find(heading)
    if start == -1:
        log(f"note: no '{heading}' section in {CHANGELOG_FILE.name}; "
            f"publishing without release notes")
        return ""
    body_start = text.index("\n", start) + 1
    nxt = text.find("\n## [", body_start)
    return text[body_start: nxt if nxt != -1 else len(text)].strip() + "\n"


def gh_preflight(tag: str) -> None:
    import shutil
    if not shutil.which("gh"):
        fail("gh not found. Install the GitHub CLI and authenticate: "
             "gh auth login")
    auth = subprocess.run(["gh", "auth", "status"], cwd=_HERE,
                           capture_output=True, text=True)
    if auth.returncode != 0:
        fail("gh is not authenticated. Run: gh auth login")
    view = subprocess.run(["gh", "release", "view", tag], cwd=_HERE,
                           capture_output=True, text=True)
    if view.returncode == 0:
        fail(f"A release for {tag} already exists. Releases are never "
             f"reused; fix forward with the next version.")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="publish-cboard-release.py",
        description="Publish an already-cut, already-built uc-cboard "
                    "release via gh.")
    parser.add_argument("--dry-run", action="store_true",
                         help="Run all guards, skip the actual publish.")
    args = parser.parse_args()

    version = read_version()
    tag = f"v{version}"

    refuse_unless_tagged(tag, version)
    refuse_unless_pushed(tag)
    artifacts = find_artifacts(version)
    log(f"tag {tag} verified locally and on {REMOTE}")
    log(f"artefacts: {', '.join(f.name for f in artifacts)}")

    gh_preflight(tag)

    notes = changelog_section(version)
    args_gh = ["gh", "release", "create", tag,
               *[str(f) for f in artifacts],
               "--title", f"uc-cboard {version}",
               "--verify-tag"]
    if notes:
        notes_file = DIST_DIR / "RELEASE_NOTES.md"
        notes_file.write_text(notes, encoding="utf-8")
        args_gh += ["--notes-file", str(notes_file)]
    else:
        args_gh += ["--notes", ""]

    if args.dry_run:
        log("dry run; would run: " + " ".join(args_gh))
        return 0

    result = subprocess.run(args_gh, cwd=_HERE, capture_output=True, text=True)
    if result.returncode != 0:
        fail("gh release create failed:\n  "
             + (result.stderr or result.stdout).strip())

    url = run("git", "remote", "get-url", REMOTE).strip()
    base = url[:-4] if url.endswith(".git") else url
    if base.startswith("git@github.com:"):
        base = "https://github.com/" + base[len("git@github.com:"):]
    print()
    log(f"published {tag}:")
    print(f"  {base}/releases/tag/{tag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
