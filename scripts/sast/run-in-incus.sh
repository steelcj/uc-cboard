#!/usr/bin/env bash
# Run the local security scan inside a throwaway Incus container or VM.
#
# Usage: scripts/sast/run-in-incus.sh [--vm] [--keep] [--image IMAGE]
#
#   --vm           use a virtual machine instead of a container
#   --keep         do not delete the instance afterwards (for debugging)
#   --image IMAGE  Incus image to launch (default: images:debian/12)
#
# Reports are written to build-log/sast/<timestamp>/ on the host.
# Exits non-zero if any scanner reports findings or fails to run.

set -euo pipefail

IMAGE="images:debian/12"
USE_VM=0
KEEP=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --vm) USE_VM=1 ;;
    --keep) KEEP=1 ;;
    --image) IMAGE="$2"; shift ;;
    -h|--help) sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

command -v incus >/dev/null || { echo "incus is not installed" >&2; exit 1; }

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
REPORT_DIR="$REPO_ROOT/build-log/sast/$STAMP"
NAME="sast-uc-cboard-$$"

cleanup() {
  if [[ $KEEP -eq 1 ]]; then
    echo "Keeping instance $NAME. Remove it with: incus delete --force $NAME"
  else
    incus delete --force "$NAME" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

launch_args=("$IMAGE" "$NAME" --ephemeral)
[[ $KEEP -eq 1 ]] && launch_args=("$IMAGE" "$NAME")
[[ $USE_VM -eq 1 ]] && launch_args+=(--vm -c limits.cpu=2 -c limits.memory=4GiB)

echo "==> Launching $NAME from $IMAGE"
incus launch "${launch_args[@]}"

echo "==> Waiting for the instance to come online"
for _ in $(seq 1 90); do
  if incus exec "$NAME" -- getent hosts deb.debian.org >/dev/null 2>&1; then
    break
  fi
  sleep 2
done
incus exec "$NAME" -- getent hosts deb.debian.org >/dev/null \
  || { echo "Instance has no network access" >&2; exit 1; }

echo "==> Copying the working tree into the instance"
incus exec "$NAME" -- mkdir -p /work /reports
tar -C "$REPO_ROOT" \
  --exclude=./node_modules --exclude=./build --exclude=./build-log/sast \
  --exclude=./scratch-cboard --exclude=./dist --exclude=./.private \
  -cf - . | incus exec "$NAME" -- tar -C /work --no-same-owner -xf -

echo "==> Running scanners"
set +e
incus exec "$NAME" -- bash /work/scripts/sast/inside.sh
status=$?
set -e

mkdir -p "$(dirname "$REPORT_DIR")"
incus file pull -r "$NAME/reports" "$(dirname "$REPORT_DIR")/"
mv "$(dirname "$REPORT_DIR")/reports" "$REPORT_DIR"
echo "==> Reports saved to ${REPORT_DIR#"$REPO_ROOT"/}"

exit $status
