# uc-cboard

Universal Cake's build and release pipeline for [Cboard](https://github.com/cboard-org/cboard), a libre AAC (augmentative and alternative communication) web application. This is not a fork claiming the Cboard name; it's UC's packaging layer around upstream, producing checksummed, pinned release artifacts consumed by [`osat-fluent-cboard-manager`](https://github.com/steelcj/osat-fluent-cboard-manager).

## What's actually here right now

This repository currently also holds a one-time vendored snapshot of upstream Cboard's source tree, taken directly from `cboard-org/cboard`. It is a snapshot, not a tracked mirror: this repository does not currently pull upstream changes, and nothing in the release pipeline depends on it. Its original README is preserved at [`README-upstream-cboard.md`](README-upstream-cboard.md).

If this proves useful, the plan is to move toward regularly pulling from upstream rather than a one-time grab. That decision isn't made yet, and this README describes the current state, not the intended future one.

## The release pipeline

The release artifact is Cboard's **built static output**, not this repository's own source, not the vendored snapshot above. `build-release.py` always clones a fresh copy of `cboard-org/cboard` at a pinned upstream tag, independent of whatever source tree happens to be sitting in this repository, and builds from that fresh clone.

```
build-release.py --tag <upstream-tag>
```

Clones upstream at the pinned tag, resolves the commit SHA, runs `yarn install --ignore-scripts` and `yarn build` (with `NODE_OPTIONS=--max-old-space-size=4096`, the default heap limit is not enough for this build), and writes a tarball, a SHA256 checksum, and a `.provenance.json` recording the upstream tag and commit to `dist/`.

```
cut-release.py patch|minor|major
```

Bumps this repository's own `VERSION`, rolls `CHANGELOG.md`'s Unreleased section into a dated entry, commits, tags. Synced unmodified from `sat-doc-automa`; has no dependency on the build artifact and needs none.

```
git push && git push origin vX.Y.Z
```

Pushing stays a deliberate, separate act, same as everywhere else in this collection.

```
publish-cboard-release.py
```

Publishes the `dist/` artifacts from `build-release.py` as a GitHub Release via `gh`. This is **not** `sat-doc-automa`'s shared `publish-release.py` — that script's determinism gate builds its tarball with `git archive` on this repository's own tagged commit, which would never contain the actual release artifact (Cboard's build output lives only in `dist/`, deliberately never committed; see the deviation note in this repository's `ff-manifest-uc-cboard.yaml` entry in `sat-doc-automa`). `publish-cboard-release.py` is repo-local, not synced, and replaces it.

## Versioning

This repository's own `VERSION` tracks the UC packaging pipeline, not Cboard's version. A given release corresponds to one pinned upstream tag, recorded in that release's `.provenance.json` and release notes.

## Licence

Cboard's own code is GPL-3.0, copyright Assistive Technology LLC & Cboard contributors; see `README-upstream-cboard.md` and `LICENSE.txt`. This repository's own build and release scripts are licensed separately; see each file's own licence block.
