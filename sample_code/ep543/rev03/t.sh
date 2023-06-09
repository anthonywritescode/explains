
set -euo pipefail

f() {
    pushd /tmp >& /dev/null

    echo hello from "$(pwd)"

    popd >& /dev/null
}

f
