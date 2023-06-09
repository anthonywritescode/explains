
set -euxo pipefail

f() {
    wd="$(pwd)"
    cd /tmp

    echo hello from "$(pwd)"

    cd "$wd"
}

f
