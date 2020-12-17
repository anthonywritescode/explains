#!/usr/bin/env bash
set -euxo pipefail

args=()

if [ -n "${NAME}" ]; then
    args+=("--name=${NAME}")
fi

python -c 'import sys; print(sys.argv[1:])' "${args[@]}"

# somescript foo bar baz
# ==> exec docker run ... "$@"
# ==> exec docker run ... "$*"
