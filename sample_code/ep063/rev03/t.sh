#!/usr/bin/env bash
set -euxo pipefail

if [ -n "${NAME}" ]; then
    ARG="--name=${NAME}"
else
    ARG=''
fi

python -c 'import sys; print(sys.argv[1:])' $ARG
