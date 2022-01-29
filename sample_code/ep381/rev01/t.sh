#!/usr/bin/env bash
set -euxo pipefail

cd ../python-node-semvar

# timeout value for seconds depends on how fast your CPU is!
timeout 2.5 python -m pytest nodesemver/ || exit 1
