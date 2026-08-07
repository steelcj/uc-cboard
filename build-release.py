#!/usr/bin/env python3
#
# source
#   project: uc-cboard
#   path: build-release.py
#
"""
build-release.py, cut a uc-cboard release from a pinned upstream cboard tag.

This is a maintainer-run script, never an end-user tool. It has no
relationship to manage-cboard.py (the osat-fluent-cboard-tool consumer),
which only ever fetches what this script publishes.

Sequence:
    1. Resolve the target upstream tag (cboard-org/cboard) to a commit SHA
    2. Shallow-clone that commit into a scratch directory
    3. yarn install --ignore-scripts   (verified 2026-08-06: completes clean)
    4. yarn build, with NODE_OPTIONS=--max-old-space-size=4096
       (default heap OOMs on this build; confirmed via V8 heap-exhaustion
       trace, not a code failure — see scoping notes)
    5. Package build/ as a tarball
    6. Write a SHA256 checksum
    7. Report the artefact path and checksum; publishing the GitHub
       Release itself is a separate, deliberate step (not automated here,
       matching cut-release.py's stance of stopping before push)

Usage:
    build-release.py --tag 1.39.0
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

UPSTREAM_REPO = "cboard-org/cboard"
UPSTREAM_CLONE_URL = f"https://github.com/{UPSTREAM_REPO}.git"
API_TAG_URL = f"https://api.github.com/repos/{UPSTREAM_REPO}/git/refs/tags"

SCRATCH_DIR = Path("scratch-cboard")
DIST_DIR = Path("dist")

BUILD_ENV_EXTRA = {"NODE_OPTIONS": "--max-old-space-size=4096"}


def fail(msg: str) -> None:
    print(f"[BUILD ERROR] {msg}", file=sys.stderr)
    sys.exit(1)


def run(cmd: list[str], cwd: Path, env: dict | None = None) -> None:
    full_env = os.environ.copy()
    if env:
        full_env.update(env)
    result = subprocess.run(cmd, cwd=cwd, env=full_env)
    if result.returncode != 0:
        fail(f"command failed ({result.returncode}): {' '.join(cmd)}")


def resolve_tag_sha(tag: str) -> str:
    url = f"{API_TAG_URL}/{tag}"
    req = urllib.request.Request(url, headers={"User-Agent": "uc-cboard-build"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except Exception as exc:  # noqa: BLE001
        fail(f"could not resolve tag {tag!r} via GitHub API: {exc}")
    sha = data.get("object", {}).get("sha")
    if not sha:
        fail(f"unexpected API response resolving tag {tag!r}: {data!r}")
    return sha


def clone_at_commit(sha: str) -> None:
    if SCRATCH_DIR.exists():
        current = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=SCRATCH_DIR,
            capture_output=True, text=True,
        )
        if current.returncode == 0 and current.stdout.strip() == sha:
            log(f"scratch clone already at {sha[:12]}; skipping re-clone")
            return
        shutil.rmtree(SCRATCH_DIR)
    run(["git", "clone", UPSTREAM_CLONE_URL, str(SCRATCH_DIR)], cwd=Path("."))
    run(["git", "checkout", sha], cwd=SCRATCH_DIR)


def build() -> None:
    run(["yarn", "install", "--ignore-scripts"], cwd=SCRATCH_DIR)
    run(["yarn", "build"], cwd=SCRATCH_DIR, env=BUILD_ENV_EXTRA)
    if not (SCRATCH_DIR / "build" / "index.html").is_file():
        fail("build completed but build/index.html is missing")


def package(tag: str, sha: str) -> Path:
    DIST_DIR.mkdir(exist_ok=True)
    artefact_name = f"uc-cboard-{tag}.tar.gz"
    artefact_path = DIST_DIR / artefact_name
    build_dir = SCRATCH_DIR / "build"

    with tarfile.open(artefact_path, "w:gz") as tar:
        tar.add(build_dir, arcname=f"cboard-{tag}")

    checksum = hashlib.sha256(artefact_path.read_bytes()).hexdigest()
    checksum_path = DIST_DIR / f"{artefact_name}.sha256"
    checksum_path.write_text(f"{checksum}  {artefact_name}\n", encoding="utf-8")

    provenance_path = DIST_DIR / f"uc-cboard-{tag}.provenance.json"
    provenance_path.write_text(
        json.dumps(
            {
                "upstream_repo": UPSTREAM_REPO,
                "upstream_tag": tag,
                "upstream_commit": sha,
                "artefact": artefact_name,
                "sha256": checksum,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    return artefact_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Cut a uc-cboard release.")
    parser.add_argument("--tag", required=True, help="Upstream cboard release tag, e.g. 1.39.0")
    args = parser.parse_args()

    print(f"[BUILD] resolving upstream tag {args.tag!r}...")
    sha = resolve_tag_sha(args.tag)
    print(f"[BUILD] tag {args.tag!r} -> commit {sha}")

    print("[BUILD] cloning at pinned commit...")
    clone_at_commit(sha)

    print("[BUILD] installing (--ignore-scripts) and building...")
    build()

    print("[BUILD] packaging artefact...")
    artefact_path = package(args.tag, sha)

    print(f"[BUILD] done: {artefact_path}")
    print(f"[BUILD] checksum: {(DIST_DIR / (artefact_path.name + '.sha256')).read_text().strip()}")
    print("[BUILD] publishing the GitHub Release is a separate, deliberate step.")


if __name__ == "__main__":
    main()
