#!/usr/bin/bash
# set -euxo pipefail
set -x

set -e

set -u

echo hi

if [ -z "${x:-}" ]; then
    echo x is empty
    echo setting x to default
    x=some_default
fi

echo "hello $x hello"

echo hello

# set -o pipefail
