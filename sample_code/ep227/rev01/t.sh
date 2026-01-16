#!/usr/bin/env bash
set -euxo pipefail

x=1

if [ "$x" -eq 1 ]; then
    echo hello hello world
else
    echo nope
fi
