#!/usr/bin/env bash
# Runs inside the throwaway instance started by run-in-incus.sh.
# Installs pinned scanner versions, scans /work, writes reports to /reports.

set -uo pipefail

NODE_VERSION="22.14.0"
OPENGREP_VERSION="1.30.0"
OSV_SCANNER_VERSION="2.6.0"
GITLEAKS_VERSION="8.30.1"

ESLINT_PACKAGES=(
  eslint@9.39.5
  eslint-plugin-security@4.2.0
  eslint-plugin-no-unsanitized@4.1.5
  typescript-eslint@8.71.0
  typescript@5.9.3
)

TOOLS=/opt/sast
REPORTS=/reports
mkdir -p "$TOOLS/bin" "$REPORTS"
export PATH="$TOOLS/bin:$TOOLS/node/bin:$PATH"

set -e
echo "--> Installing base packages"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq --no-install-recommends ca-certificates curl git xz-utils >/dev/null

cd "$TOOLS"

echo "--> Installing Node.js $NODE_VERSION"
node_tar="node-v$NODE_VERSION-linux-x64.tar.xz"
curl -fsSLO "https://nodejs.org/dist/v$NODE_VERSION/$node_tar"
curl -fsSL "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt" | grep " $node_tar\$" | sha256sum -c -
mkdir -p node && tar -xJf "$node_tar" -C node --strip-components=1

echo "--> Installing OSV-Scanner $OSV_SCANNER_VERSION"
osv_base="https://github.com/google/osv-scanner/releases/download/v$OSV_SCANNER_VERSION"
curl -fsSLO "$osv_base/osv-scanner_linux_amd64"
curl -fsSL "$osv_base/osv-scanner_SHA256SUMS" | grep " osv-scanner_linux_amd64\$" | sha256sum -c -
install -m 755 osv-scanner_linux_amd64 bin/osv-scanner

echo "--> Installing Gitleaks $GITLEAKS_VERSION"
gl_tar="gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz"
gl_base="https://github.com/gitleaks/gitleaks/releases/download/v$GITLEAKS_VERSION"
curl -fsSLO "$gl_base/$gl_tar"
curl -fsSL "$gl_base/gitleaks_${GITLEAKS_VERSION}_checksums.txt" | grep " $gl_tar\$" | sha256sum -c -
tar -xzf "$gl_tar" -C bin gitleaks

echo "--> Installing Opengrep $OPENGREP_VERSION"
# Opengrep publishes cosign signatures, not a checksum file, so this
# download is pinned by version only.
curl -fsSL -o bin/opengrep \
  "https://github.com/opengrep/opengrep/releases/download/v$OPENGREP_VERSION/opengrep_manylinux_x86"
chmod 755 bin/opengrep

echo "--> Installing ESLint and security plugins"
npm init -y >/dev/null
npm install --no-audit --no-fund --silent "${ESLINT_PACKAGES[@]}"

# The scan runs against a copy of the repo, so it is safe to drop the
# scan config and tool modules into it. The repo has no node_modules of
# its own in this copy.
ln -s "$TOOLS/node_modules" /work/node_modules
git config --global --add safe.directory /work
cp /work/scripts/sast/eslint.config.mjs /work/eslint.config.mjs
set +e

# Each scanner runs even if an earlier one fails; results are summarised at the end.
declare -A results
run() {
  local name="$1"; shift
  echo
  echo "==== $name"
  "$@"
  local rc=$?
  # Every tool here exits 1 for findings; anything else means the tool itself failed.
  case $rc in
    0) results[$name]="pass" ;;
    1) results[$name]="FAIL, findings" ;;
    *) results[$name]="FAIL, tool error (exit $rc)" ;;
  esac
}

cd /work

run "ESLint security rules" bash -c \
  'npx --no-install eslint --max-warnings 0 src scripts \
     -f json -o /reports/eslint.json; rc=$?; \
   npx --no-install eslint src scripts | tee /reports/eslint.txt; exit $rc'

run "Opengrep custom rules" \
  opengrep scan --config scripts/sast/opengrep-rules.yml --no-git-ignore --error \
    --sarif-output=/reports/opengrep.sarif --text src

run "OSV-Scanner dependencies" bash -c \
  'osv-scanner scan source -L yarn.lock | tee /reports/osv-scanner.txt; exit ${PIPESTATUS[0]}'

run "Gitleaks git history" \
  gitleaks git /work --config /work/scripts/sast/gitleaks.toml --redact --no-banner \
    --report-format sarif --report-path /reports/gitleaks-history.sarif

run "Gitleaks working tree" \
  gitleaks dir /work --config /work/scripts/sast/gitleaks.toml --redact --no-banner \
    --report-format sarif --report-path /reports/gitleaks-tree.sarif

echo
echo "==== Summary"
for name in "ESLint security rules" "Opengrep custom rules" "OSV-Scanner dependencies" \
            "Gitleaks git history" "Gitleaks working tree"; do
  printf '  %-28s %s\n' "$name" "${results[$name]}"
done | tee /reports/summary.txt
! grep -q FAIL /reports/summary.txt
