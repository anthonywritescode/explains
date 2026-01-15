#!/usr/bin/bash
# set -euxo pipefail
set -x

set -e

echo hi

retc=0
bash -c 'echo fail >&2; exit 15' || retc=$?
if [ $retc = 15 ]; then
    echo it exited fifteen
else
    echo it exited "$retc"
fi

echo hello

# set -u
# set -o pipefail
