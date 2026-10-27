---
dc:title: "Local Security Scan With Incus"
dcterms:version: "0.1.0"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic)"
dc:description: "How to check uc-cboard for security problems on your own computer, inside a throwaway Incus container or virtual machine, using only open source tools. Replaces the GitHub CodeQL workflow."
dcterms:created: "2026-10-04"
dcterms:modified: "2026-10-04"
dc:format: "text/markdown"
dc:language: "en"
sat:language_bcp47: "en"
dc:identifier: "local-security-scan-with-incus"
dcterms:rightsHolder: "Christopher Steel"
dc:rights: >
  Copyright 2026 Christopher Steel.
  SPDX-License-Identifier: GPL-3.0-or-later
sat:uuid: ""
sat:repository: "uc-cboard"
sat:path: "en/docs/guides/devops/"
sat:migration_status: pre-sat
sat:changelog:
  - version: "0.1.0"
    date: "2026-10-04"
    author: "Christopher Steel"
    notes: "Initial draft, written with Claude Opus 5.5 (Anthropic). Covers the local scan that replaces the GitHub CodeQL workflow."
---

# Local Security Scan With Incus

Version: 0.1.0
Status: Draft
Style Guide: style-guide--plain-language-for-general-audiences

## Abstract

This guide shows how to check uc-cboard for common security problems on your own computer. The check runs inside a short-lived Incus container, so nothing is installed on your computer. It uses only open source tools. It replaces the GitHub CodeQL workflow, which this project no longer uses.

## What this check does

A security scan reads the project's files and looks for known kinds of mistakes. It does not run the app. It looks for four things:

- **Risky code patterns.** ESLint is a tool that reads JavaScript and flags code that breaks a rule <a name="apa-eslint-citation"></a>([OpenJS Foundation, 2026](#apa-eslint-reference)). Two add-on rule sets look for security mistakes, such as building a file path from user input or putting raw HTML on the page <a name="apa-eslint-plugin-security-citation"></a>([ESLint Community, 2026](#apa-eslint-plugin-security-reference); <a name="apa-no-unsanitized-citation"></a>[Mozilla, 2026](#apa-no-unsanitized-reference)).
- **Project rules.** Opengrep finds code that matches a pattern you write <a name="apa-opengrep-citation"></a>([Opengrep, 2026](#apa-opengrep-reference)). This project's own patterns live in `scripts/sast/opengrep-rules.yml`. You can add to them.
- **Known weak packages.** A dependency is a package of code that this project borrows from someone else. OSV-Scanner checks each dependency in `yarn.lock` against a public list of known problems <a name="apa-osv-scanner-citation"></a>([Google, 2026](#apa-osv-scanner-reference)).
- **Leaked secrets.** A secret is a password, key, or token. Gitleaks looks for secrets in the files and in the full Git history <a name="apa-gitleaks-citation"></a>([Gitleaks, 2026](#apa-gitleaks-reference)).

## Why the check runs in a container

A container is a small, separate Linux system that runs on your computer. Incus is the program that creates and runs it <a name="apa-incus-citation"></a>([Linux Containers, 2026](#apa-incus-reference)). The scan starts a fresh container, copies the project into it, and runs the tools there. When the scan ends, Incus deletes the container.

This keeps your computer clean. The scan tools and their downloads never touch your own system. Each scan also starts from the same clean state, so results do not depend on what else is installed on your computer.

A virtual machine, or VM, is like a container but more separate. It runs its own full operating system. It is slower to start, but it gives stronger walls between the scan and your computer. You can choose either one.

## What you need

You need Incus installed and set up, with a working network bridge. You can check this by listing your instances. The command below should print a table, even if the table is empty.

```bash
incus list
```

The container needs internet access. It downloads the scan tools each time. OSV-Scanner also sends the names and versions of the project's dependencies to the osv.dev service to look them up. It does not send your code.

## How to run the scan

Open a terminal in the top folder of the uc-cboard project. Run the command below to scan in a container. It prints each step as it goes and ends with a summary.

```bash
make sast
```

To scan in a virtual machine instead, run the command below. It gives the VM 2 processors and 4 GiB of memory.

```bash
make sast SAST_ARGS=--vm
```

To keep the container after the scan, so you can look around inside it, run the command below. The script prints the command to delete it when you are done.

```bash
make sast SAST_ARGS=--keep
```

The scan includes changes you have not committed yet. It skips `node_modules`, `build`, `dist`, `scratch-cboard`, and `.private`.

## How to read the results

At the end, the scan prints a summary with one line for each tool. Each line says `pass` or `FAIL`. A `FAIL` line also says why. `findings` means the tool found problems. `tool error` means the tool itself did not work, so its results are missing. The command exits with an error if any line says `FAIL`.

The scan saves full reports in a new folder named for the date and time, under `build-log/sast/`. For example, a scan at 2:30 PM on 4 October 2026 saves to `build-log/sast/20261004-143000/`. Git ignores this folder, so reports are never committed by mistake.

| File | What it holds |
|------|---------------|
| `summary.txt` | The pass or fail line for each tool |
| `eslint.txt` | ESLint findings, easy to read |
| `eslint.json` | The same ESLint findings, for other tools |
| `opengrep.sarif` | Opengrep findings |
| `osv-scanner.txt` | Weak dependencies and how to fix them |
| `gitleaks-history.sarif` | Secrets found in past commits |
| `gitleaks-tree.sarif` | Secrets found in the current files |

SARIF is a standard file format for scan results <a name="apa-sarif-citation"></a>([OASIS, 2020](#apa-sarif-reference)). Many code editors can open it. In VS Code, the SARIF Viewer extension shows each finding next to the line of code.

Gitleaks hides the secret itself in its reports. It shows where the secret is, but not its value.

The first scan will likely report problems. Much of the code came from the original Cboard project, and some findings may be old. Treat the first report as a starting list, not as a sign that something just broke.

## How to change what the scan checks

The scan files live in `scripts/sast/`:

- `run-in-incus.sh` starts the container, copies the project in, and brings the reports back.
- `inside.sh` runs inside the container. It installs the tools and runs them.
- `eslint.config.mjs` lists the ESLint rules. It is separate from the project's own `.eslintrc`, and does not change how the project builds.
- `opengrep-rules.yml` holds this project's own Opengrep patterns.
- `gitleaks.toml` tells Gitleaks to skip test files. Test files hold fake tokens that look like real ones.

To add a project rule, add an entry to `opengrep-rules.yml`. Each rule has an ID, a message, and a pattern that shows the code to find. The Opengrep documentation explains the pattern format.

To turn off an ESLint rule that gives too many false alarms, set it to `'off'` in `eslint.config.mjs`. The file already does this for `security/detect-object-injection`. That rule flags almost every `object[key]` in the code.

Tool versions are fixed at the top of `inside.sh`. To update a tool, change its version number there. The script checks each download against the checksum its maker publishes, except Opengrep, which does not publish one.

## Decisions and why they were made

### Remove CodeQL

**Decided:** Remove the GitHub CodeQL workflow.

**Why:** CodeQL is free to use only for open source code hosted on GitHub. Its license is not an open source license. It runs only on GitHub's own servers, so no one could run the same check on their own computer.

**Other options:** Keep CodeQL next to the local scan. This was not chosen because it keeps a check that depends on one company's service and license.

### Use only open source tools and rules

**Decided:** Use ESLint, eslint-plugin-security, eslint-plugin-no-unsanitized, Opengrep, OSV-Scanner, and Gitleaks. Each uses an open source license: MIT, Apache 2.0, MPL 2.0, or LGPL 2.1.

**Why:** Anyone can run, read, and change these tools without extra terms.

**Other options:** Semgrep's own rule library, and the opengrep-rules library based on it. These were not chosen. Their licenses add terms, such as the Commons Clause, that limit use. Opengrep itself is open source, so the scan uses it with this project's own rules only.

### Run in a throwaway container

**Decided:** Run every scan in a new Incus container or VM, then delete it.

**Why:** Nothing is installed on your computer. Each scan starts from the same clean state.

**Other options:** Install the tools directly on your computer. This was not chosen because results would depend on what else is installed. Docker was also an option. Incus was chosen because it can run both containers and VMs with the same commands.

### Copy the project in instead of sharing the folder

**Decided:** Copy the project into the container at the start of each scan.

**Why:** A copy works the same in containers and VMs. The scan can also change its copy, for example to add its own ESLint config, without touching your files.

**Other options:** Share the project folder into the container as read-only. This was not chosen because shared folders behave differently in containers and VMs, and file ownership can get in the way.

## License

This document, *Local Security Scan With Incus*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [GNU General Public License v3.0 or later](https://www.gnu.org/licenses/gpl-3.0.html).

## Resources

### Scan tools

- [ESLint](#apa-eslint-reference)
- [eslint-plugin-security](#apa-eslint-plugin-security-reference)
- [eslint-plugin-no-unsanitized](#apa-no-unsanitized-reference)
- [Opengrep](#apa-opengrep-reference)
- [OSV-Scanner](#apa-osv-scanner-reference)
- [Gitleaks](#apa-gitleaks-reference)

### Containers and file formats

- [Incus](#apa-incus-reference)
- [SARIF](#apa-sarif-reference)

## References

<a name="apa-eslint-plugin-security-reference"></a>ESLint Community. (2026). *eslint-plugin-security* (Version 4.2.0) [Computer software]. https://github.com/eslint-community/eslint-plugin-security
[Return to citation](#apa-eslint-plugin-security-citation)

<a name="apa-gitleaks-reference"></a>Gitleaks. (2026). *Gitleaks* (Version 8.30.1) [Computer software]. https://github.com/gitleaks/gitleaks
[Return to citation](#apa-gitleaks-citation)

<a name="apa-osv-scanner-reference"></a>Google. (2026). *OSV-Scanner* (Version 2.6.0) [Computer software]. https://github.com/google/osv-scanner
[Return to citation](#apa-osv-scanner-citation)

<a name="apa-incus-reference"></a>Linux Containers. (2026). *Incus documentation*. https://linuxcontainers.org/incus/docs/main/
[Return to citation](#apa-incus-citation)

<a name="apa-no-unsanitized-reference"></a>Mozilla. (2026). *eslint-plugin-no-unsanitized* (Version 4.1.5) [Computer software]. https://github.com/mozilla/eslint-plugin-no-unsanitized
[Return to citation](#apa-no-unsanitized-citation)

<a name="apa-sarif-reference"></a>OASIS. (2020). *Static Analysis Results Interchange Format (SARIF) version 2.1.0*. https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html
[Return to citation](#apa-sarif-citation)

<a name="apa-eslint-reference"></a>OpenJS Foundation. (2026). *ESLint* (Version 9.39.5) [Computer software]. https://eslint.org/
[Return to citation](#apa-eslint-citation)

<a name="apa-opengrep-reference"></a>Opengrep. (2026). *Opengrep* (Version 1.30.0) [Computer software]. https://github.com/opengrep/opengrep
[Return to citation](#apa-opengrep-citation)

## Changelog

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft, covering the local Incus scan that replaces the GitHub CodeQL workflow |
