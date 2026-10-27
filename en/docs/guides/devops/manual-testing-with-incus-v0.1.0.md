---
dc:title: "Manual Testing With Incus"
dcterms:version: "0.1.0"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic)"
dc:description: "How to test uc-cboard by hand inside an Incus container: the security scan one tool at a time, the Jest unit tests, and the Playwright end-to-end tests against a local copy of the app."
dcterms:created: "2026-10-04"
dcterms:modified: "2026-10-04"
dc:format: "text/markdown"
dc:language: "en"
sat:language_bcp47: "en"
dc:identifier: "manual-testing-with-incus"
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
    notes: "Initial draft, written with Claude Opus 5.5 (Anthropic). Steps are ordered by headings, not numbers, until the final draft. Unit test steps run and confirmed on 2026-10-04, with measured download size and the current failures of the full unit test suite."
---

# Manual Testing With Incus

Version: 0.1.0
Status: Draft
Style Guide: style-guide--plain-language-for-general-audiences

## Abstract

This guide shows how to test uc-cboard by hand inside an Incus container. It covers three kinds of test: the security scan, run one tool at a time, the unit tests, and the end-to-end tests. Doing it by hand lets you stop between steps, look around, and run only the part you care about. For the one-command version of the security scan, see *Local Security Scan With Incus* <a name="apa-scan-guide-citation"></a>([Steel, 2026a](#apa-scan-guide-reference)).

## How to use this guide

The tasks are in order from top to bottom. Each heading is one task. Do them in the order shown, unless a section says you can skip it.

Each command block says where to run it. "On your computer" means a terminal on your own machine, in the top folder of the uc-cboard project. "Inside the container" means a shell inside the test container, which you open in the task "Open a shell in the container".

## Status of this draft

The security scan steps match `make sast`, which has run twice on 2026-10-04. The unit test steps were run as written on 2026-10-04, in a container, and worked. The end-to-end test steps have not been run yet in Incus. Treat them as a first draft, and note anything that does not work as written.

## Before you start

### Words used in this guide

A **container** is a small, separate Linux system that runs on your computer. **Incus** is the program that creates and runs containers <a name="apa-incus-create-citation"></a>([Linux Containers, n.d.-a](#apa-incus-create-reference)). A **virtual machine**, or VM, is like a container but more separate, because it runs its own full operating system. Incus calls both of them **instances**.

A **unit test** checks one small piece of code on its own, without running the whole app. This project's unit tests use Jest <a name="apa-jest-citation"></a>([Jest, n.d.](#apa-jest-reference)).

An **end-to-end test** runs the whole app in a real web browser and clicks through it the way a person would. This project's end-to-end tests use Playwright <a name="apa-playwright-browsers-citation"></a>([Microsoft, n.d.-a](#apa-playwright-browsers-reference)).

### What you need

You need Incus installed and working. The command below lists your instances. It should print a table, even if the table is empty.

On your computer:

```bash
incus list
```

You also need internet access. The container downloads its tools while you work.

### How much this downloads

Manual testing uses a lot of network data the first time, and again every time you start a new container. Rough sizes:

- The security scan tools: about 165 MB.
- Node.js, Yarn and the base tools for unit and end-to-end tests: about 50 MB.
- The project's packages for unit and end-to-end tests: about 195 MB, measured on 2026-10-04. Once installed, they take about 1.3 GB of disk in the container, plus 1.5 GB for Yarn's own copy.
- The test web browsers for end-to-end tests: a few hundred MB more. This has not been measured yet.

To save data, keep one container and reuse it while you work, instead of making a new one for each test. *Proposal: Minimizing Network Bandwidth for Local Testing* describes ways to cut this further <a name="apa-bandwidth-proposal-citation"></a>([Steel, 2026b](#apa-bandwidth-proposal-reference)).

### Why the scan and the tests use different containers

The security scan and the tests each set up the project folder inside the container in their own way. The scan links in its own tool packages where the project's packages would go, and the tests need the project's real packages there. If both run in one container, they get in each other's way. This guide uses a container named `uc-cboard-scan` for the scan, and one named `uc-cboard-test` for the unit and end-to-end tests.

## Set up a test container

Do these tasks once for each container. In the commands below, `NAME` holds the container's name. Set it first, in every new terminal on your computer.

For the security scan, on your computer:

```bash
NAME=uc-cboard-scan
```

For the unit and end-to-end tests, on your computer:

```bash
NAME=uc-cboard-test
```

### Launch the container

This command creates a new Debian 12 container and starts it. It prints "Launching" and returns in a few seconds when the image is already on your computer, or longer the first time.

On your computer:

```bash
incus launch images:debian/12 "$NAME"
```

To use a virtual machine instead, see "Use a virtual machine instead" near the end of this guide.

### Wait for the network

The container needs a few seconds to connect to the network. This command waits until it can look up a web address, then returns with no output.

On your computer:

```bash
until incus exec "$NAME" -- getent hosts deb.debian.org >/dev/null 2>&1; do sleep 2; done
```

### Copy the project in

This command copies the project folder into the container, at `/work`. It includes changes you have not committed. It skips folders that are large and not needed, such as `node_modules` and `build`, and the `.private` folder, which holds secrets. It prints nothing when it works.

On your computer, in the top folder of the project:

```bash
incus exec "$NAME" -- mkdir -p /work
tar --exclude=./node_modules --exclude=./build --exclude=./build-log/sast \
    --exclude=./scratch-cboard --exclude=./dist --exclude=./.private \
    -cf - . | incus exec "$NAME" -- tar -C /work --no-same-owner -xf -
```

### Open a shell in the container

This command opens a command prompt inside the container, as its `root` user. The prompt changes to show the container's name. Type `exit` to leave it.

On your computer:

```bash
incus shell "$NAME"
```

## Run the security scan by hand

Use the `uc-cboard-scan` container for this section.

### Install the scan tools and run the full scan

The project's scan script installs every tool, then runs the whole scan once. This takes a few minutes. It ends with a summary that has one line for each tool. Each line says `pass` or `FAIL`.

Inside the container:

```bash
bash /work/scripts/sast/inside.sh
```

After this, the tools stay installed in the container. You can run any one of them again, as shown in the next tasks.

### Make the tools easy to run

This command tells the shell where the tools are, and moves into the project folder. Run it again each time you open a new shell in the container.

Inside the container:

```bash
export PATH=/opt/sast/bin:/opt/sast/node/bin:$PATH
cd /work
```

### Run ESLint on its own

ESLint reads the JavaScript code and reports risky patterns <a name="apa-eslint-citation"></a>([OpenJS Foundation, n.d.-b](#apa-eslint-reference)). This command checks the `src` and `scripts` folders, and prints each problem with its file and line number.

Inside the container:

```bash
npx --no-install eslint src scripts
```

To check one file only, name it instead. For example:

```bash
npx --no-install eslint src/i18n.js
```

### Run Opengrep on its own

Opengrep looks for the project's own code patterns, listed in `scripts/sast/opengrep-rules.yml`. This command prints each match with its rule and location, or no findings if there are none.

Inside the container:

```bash
opengrep scan --config scripts/sast/opengrep-rules.yml --no-git-ignore src
```

To try a change to a rule, edit the rules file inside the container with a text editor, then run the command again. Copy the change back to the project on your computer when it works.

### Run OSV-Scanner on its own

OSV-Scanner checks the project's packages in `yarn.lock` against a public list of known security problems. It prints a table with one row for each problem, and the version that fixes it.

Inside the container:

```bash
osv-scanner scan source -L yarn.lock
```

### Run Gitleaks on its own

Gitleaks looks for passwords, keys and tokens. The first command checks the full Git history. The second checks the current files. Both use the project's settings, which skip test files with fake tokens. `--redact` hides any secret it finds, and shows only where it is.

Inside the container:

```bash
gitleaks git /work --config scripts/sast/gitleaks.toml --redact
gitleaks dir /work --config scripts/sast/gitleaks.toml --redact
```

Add `-v` to either command to see each finding in full detail.

### Copy the scan reports back

The full scan saved its reports in `/reports` inside the container. These commands copy them to your computer, into a new folder under `build-log/sast/` named for the date and time. Git ignores that folder.

On your computer, in the top folder of the project:

```bash
incus file pull -r uc-cboard-scan/reports build-log/sast/
mv build-log/sast/reports "build-log/sast/manual-$(date +%Y%m%d-%H%M%S)"
```

## Run the unit tests

Use the `uc-cboard-test` container for this section and the next one. These steps were run as written on 2026-10-04 and worked. The container needs about 3 GB of free disk for this section.

### Install Node.js and Yarn

Node.js runs JavaScript outside a web browser. Yarn installs the project's packages. These commands install the base tools, download Node.js 22.14.0, check it against the checksum its makers publish, and turn on Yarn. A checksum is a code that changes if even one byte of a file changes, so a match shows the download is complete and unchanged. The checksum line should print `OK`, and the last line should print `1.22.22`.

Inside the container:

```bash
apt-get update
apt-get install -y --no-install-recommends ca-certificates curl git xz-utils
cd /opt
curl -fsSLO https://nodejs.org/dist/v22.14.0/node-v22.14.0-linux-x64.tar.xz
curl -fsSL https://nodejs.org/dist/v22.14.0/SHASUMS256.txt | grep " node-v22.14.0-linux-x64.tar.xz$" | sha256sum -c -
mkdir -p node && tar -xJf node-v22.14.0-linux-x64.tar.xz -C node --strip-components=1
echo 'export PATH=/opt/node/bin:$PATH COREPACK_ENABLE_DOWNLOAD_PROMPT=0' >> /root/.bashrc
source /root/.bashrc
corepack enable
cd /work && yarn --version
```

Corepack is the part of Node.js that installs the exact Yarn version the project names in `package.json` <a name="apa-corepack-citation"></a>([OpenJS Foundation, n.d.-a](#apa-corepack-reference)).

### Install the project's packages

This command installs every package the project uses, exactly as listed in `yarn.lock`. It took about 2 minutes on 2026-10-04. It prints warnings about old packages, which are normal for this project. It should end with `Done`.

Inside the container, in `/work`:

```bash
yarn install --frozen-lockfile
```

`--frozen-lockfile` stops Yarn from changing `yarn.lock`. If Yarn says the lock file needs updating, stop and fix that on your computer first.

### Run the same tests as CircleCI

This command runs the same group of unit tests that CircleCI runs: the Board, Communicator, App, Settings, Account and UI tests. It prints each test file with a pass or fail mark, then a summary of how many tests passed. On 2026-10-04, all 60 test files, 399 tests and 65 snapshots passed, in about 20 seconds.

Inside the container, in `/work`:

```bash
CI=true yarn test --runInBand --no-watchman --testPathPattern="/Board|Communicator|App|Settings|Account|UI/"
```

`CI=true` makes the tests run once and stop, instead of waiting for file changes. `--runInBand` runs the tests one at a time, which uses less memory.

CircleCI also adds `--updateSnapshot`. A snapshot is a saved copy of what a piece of the screen should look like. `--updateSnapshot` replaces any snapshot that no longer matches, so a changed screen never fails the test. This guide leaves it out, so you can see when a screen has changed.

### Run all the unit tests

This command runs every unit test in the project, not only the CircleCI group.

Inside the container, in `/work`:

```bash
CI=true yarn test --runInBand --no-watchman
```

On 2026-10-04 this did not finish. The tests outside the CircleCI group have problems of their own, which CircleCI never shows because it does not run them:

- `src/providers/SpeechProvider/__tests__/SpeechProvider.actions.test.js` causes an error that is never caught, in `src/providers/SpeechProvider/tts.js` at line 36. The error stops Jest before it prints its summary. Jest is the tool that runs the unit tests.
- `src/components/WelcomeScreen/CboardLogo/CboardLogo.test.js` fails because the logo changed. The saved snapshot expects `/images/logo_no_words.svg`, and the app now uses `/images/logo-white-slogan.png`.
- `src/components/WelcomeScreen/WelcomeScreen.test.js` fails with `Cannot read properties of undefined (reading 'WelcomeScreen')`, at line 218 of `WelcomeScreen.container.js`.
- `src/providers/SpeechProvider/__tests__/SpeechProvider.reducer.test.js` fails because its expected state no longer matches the code. For example, the code now adds `elevenLabsApiKey`.
- `src/api/api.test.js` fails with `No request to respond to!` in its language test.

These are problems in the tests or the code, not in this guide. Until they are fixed, expect this command to fail.

### Run one test file

To run one test file, name it at the end of the command. For example, this runs the tests for the board's tiles:

Inside the container, in `/work`:

```bash
CI=true yarn test --runInBand --no-watchman src/components/Board/Tile/Tile.test.js
```

## Run the end-to-end tests

Use the `uc-cboard-test` container, after the tasks in "Run the unit tests" up to and including "Install the project's packages". These steps have not been run yet.

### Build the app

This command builds the app the same way the project's `Dockerfile` does. It makes a ready-to-serve copy of the app in the `build` folder. It takes several minutes and ends with a message that the build folder is ready.

Inside the container, in `/work`:

```bash
NODE_OPTIONS=--max-old-space-size=4192 yarn build
```

### Serve the app

This command starts a small web server for the built app, on port 3000, and leaves it running in the background. Its messages go to `/tmp/serve.log`. The second command checks that it is running. It should print a line with `200 OK`.

Inside the container, in `/work`:

```bash
nohup npx --yes serve@14.2.6 -s build -l 3000 > /tmp/serve.log 2>&1 &
sleep 5 && curl -sI http://127.0.0.1:3000 | head -1
```

### Look at the app yourself

You can open the app in the web browser on your computer. This command shows the container's network address, in the IPV4 column.

On your computer:

```bash
incus list uc-cboard-test
```

Open `http://` followed by that address and `:3000` in your web browser, for example `http://10.119.134.50:3000`. This is useful for checking a change by eye, before or after the automated tests.

### Install the test browsers

Playwright runs the tests in its own copies of Chromium and Firefox. This command downloads both, plus the system files they need. It takes a few minutes.

Inside the container, in `/work`:

```bash
npx playwright install --with-deps chromium firefox
```

### Point Playwright at the local app

The project's Playwright settings test the shared QA website at `https://app.qa.cboard.io`, not your own copy. These commands make a small settings file that keeps every other setting, but tests the app served in the container instead <a name="apa-playwright-config-citation"></a>([Microsoft, n.d.-b](#apa-playwright-config-reference)). The file lives only inside the container.

Inside the container, in `/work`:

```bash
cat > playwright.incus.config.ts <<'EOF'
import { defineConfig } from '@playwright/test';
import base from './playwright.config';

export default defineConfig({
  ...base,
  use: { ...base.use, baseURL: 'http://127.0.0.1:3000' },
});
EOF
```

### Run the tests

This command runs the tests that do not need a user account: the `unlogged` folder and the smoke tests. It runs them in Chromium, Firefox and a mobile phone screen size. It prints one line for each test, then a summary.

Inside the container, in `/work`:

```bash
npx playwright test -c playwright.incus.config.ts tests/unlogged tests/smoke.spec.js
```

To run in one browser only, add `--project=chromium`, `--project=firefox` or `--project=mobile`. To run one test file, name it instead of the folders.

The tests in `tests/logged` need a real user account and a working Cboard server for logging in. A local copy of the app does not have one, so this guide leaves them out.

### Copy the test report back

Playwright saves a report you can open in a web browser. These commands copy it, and the raw results, to your computer. Git already ignores both folders.

On your computer, in the top folder of the project:

```bash
incus file pull -r uc-cboard-test/work/playwright-report .
incus file pull -r uc-cboard-test/work/test-results .
```

Open `playwright-report/index.html` in your web browser to see the results.

## Test a change you made

### Copy changed files in again

After you change files on your computer, copy the project into the container again. This command is the same as in "Copy the project in". It replaces changed files and adds new ones. It keeps the container's installed packages, because it does not copy `node_modules`.

On your computer, in the top folder of the project:

```bash
tar --exclude=./node_modules --exclude=./build --exclude=./build-log/sast \
    --exclude=./scratch-cboard --exclude=./dist --exclude=./.private \
    -cf - . | incus exec "$NAME" -- tar -C /work --no-same-owner -xf -
```

It does not remove files you deleted on your computer. If that matters for your test, start a new container instead.

For end-to-end tests, build the app again after copying, then restart the web server. This command stops the old server.

Inside the container:

```bash
pkill -f 'serve@14.2.6'
```

Then repeat "Build the app" and "Serve the app".

## Clean up

### Delete the container

When you are done, delete the container. This removes everything in it, including the downloaded tools and packages. The next container downloads them again, so keep the container while you are still testing.

On your computer:

```bash
incus delete --force uc-cboard-scan
incus delete --force uc-cboard-test
```

## Use a virtual machine instead

A virtual machine gives stronger walls between the tests and your computer. It is slower to start and needs more memory. Building the app needs at least 4 GiB.

To use one, change only the task "Launch the container". This command launches a virtual machine with 4 processors and 8 GiB of memory.

On your computer:

```bash
incus launch images:debian/12 "$NAME" --vm -c limits.cpu=4 -c limits.memory=8GiB
```

Every other task works the same. "Wait for the network" can take a minute longer, while the virtual machine starts up.

## Decisions and why they were made

### Use separate containers for the scan and the tests

**Decided:** run the security scan in `uc-cboard-scan` and the tests in `uc-cboard-test`.

**Why:** the scan script links its own tool packages into the project folder, where the tests need the project's real packages.

**Other options:** one shared container, removing the scan's link before installing the project's packages. This was not chosen because it is easy to forget, and the error it causes is confusing.

### Test a built copy of the app, not the development server

**Decided:** build the app and serve the build for end-to-end tests.

**Why:** the built app is what people actually use. It also matches how the `Dockerfile` builds the app.

**Other options:** the development server, `yarn start`. It starts faster after a change, but it is slower to run tests against, and it differs from the real app.

### Leave out `--updateSnapshot`

**Decided:** run the unit tests without `--updateSnapshot`, unlike CircleCI.

**Why:** with it, a changed screen silently replaces the saved snapshot and never fails. A manual test should show those changes.

**Other options:** match CircleCI exactly. This was not chosen because it hides the changes manual testing is meant to find.

### Leave out the logged-in end-to-end tests

**Decided:** run only the tests that do not need an account.

**Why:** the logged-in tests need a real user account and a Cboard server. A local copy of the app does not have one.

**Other options:** run them against the shared QA website. That tests the QA website, not your changes, so it does not belong in this guide.

### Show order with headings, not numbers

**Decided:** each task is its own heading, in order from top to bottom, with no numbered steps.

**Why:** while the guide is a draft, tasks are easy to add, remove and move. Numbers would need fixing after every change. Numbers may be added in the final draft.

**Other options:** numbered steps from the start. This was not chosen for the reason above.

## License

This document, *Manual Testing With Incus*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [GNU General Public License v3.0 or later](https://www.gnu.org/licenses/gpl-3.0.html).

## Resources

### Project documents

- [Local Security Scan With Incus](#apa-scan-guide-reference)
- [Proposal: Minimizing Network Bandwidth for Local Testing](#apa-bandwidth-proposal-reference)

### Incus

- [How to create instances](#apa-incus-create-reference)

### Testing tools

- [Jest command line options](#apa-jest-reference)
- [Playwright browsers](#apa-playwright-browsers-reference)
- [Playwright test configuration](#apa-playwright-config-reference)
- [ESLint](#apa-eslint-reference)
- [Corepack](#apa-corepack-reference)

## References

<a name="apa-jest-reference"></a>Jest. (n.d.). *Jest CLI options*. Retrieved October 4, 2026, from https://jestjs.io/docs/cli
[Return to citation](#apa-jest-citation)

<a name="apa-incus-create-reference"></a>Linux Containers. (n.d.-a). *How to create instances*. Incus documentation. Retrieved October 4, 2026, from https://linuxcontainers.org/incus/docs/main/howto/instances_create/
[Return to citation](#apa-incus-create-citation)

<a name="apa-playwright-browsers-reference"></a>Microsoft. (n.d.-a). *Browsers*. Playwright documentation. Retrieved October 4, 2026, from https://playwright.dev/docs/browsers
[Return to citation](#apa-playwright-browsers-citation)

<a name="apa-playwright-config-reference"></a>Microsoft. (n.d.-b). *Test configuration*. Playwright documentation. Retrieved October 4, 2026, from https://playwright.dev/docs/test-configuration
[Return to citation](#apa-playwright-config-citation)

<a name="apa-corepack-reference"></a>OpenJS Foundation. (n.d.-a). *Corepack*. Node.js documentation. Retrieved October 4, 2026, from https://nodejs.org/api/corepack.html
[Return to citation](#apa-corepack-citation)

<a name="apa-eslint-reference"></a>OpenJS Foundation. (n.d.-b). *ESLint*. Retrieved October 4, 2026, from https://eslint.org/
[Return to citation](#apa-eslint-citation)

<a name="apa-scan-guide-reference"></a>Steel, C. (2026a). *Local security scan with Incus* (Version 0.1.0) [Guide]. uc-cboard repository, `en/docs/guides/devops/`.
[Return to citation](#apa-scan-guide-citation)

<a name="apa-bandwidth-proposal-reference"></a>Steel, C. (2026b). *Proposal: Minimizing network bandwidth for local testing* (Version 0.1.0) [Proposal]. uc-cboard repository, `en/docs/proposals/`.
[Return to citation](#apa-bandwidth-proposal-citation)

## Changelog

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft: security scan by hand, unit tests and end-to-end tests in Incus containers, ordered by headings until the final draft. Unit test steps run and confirmed on 2026-10-04 |
