#!/usr/bin/bash
# set -euxo pipefail
set -x

set -e

set -u

echo hi

echo hello | bash -c 'echo fail >&2; exit 1' | echo wat

echo hello

# set -o pipefail
