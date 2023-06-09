
set -euo pipefail

f() {
    pushd /tmp

    echo hello from "$(pwd)"

    popd
}

f
