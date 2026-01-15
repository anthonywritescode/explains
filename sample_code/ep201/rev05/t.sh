#!/usr/bin/bash
# set -euxo pipefail
set -x

# set -e

echo hi

bash -c 'echo fail >&2; exit 1'
echo $?

echo hello

# set -u
# set -o pipefail
