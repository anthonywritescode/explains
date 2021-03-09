#!/usr/bin/bash
set -euxo pipefail

set -x

set -e

set -u

set -o pipefail

echo hi

echo hello | bash -c 'echo fail >&2; exit 1' | echo wat

echo hello
