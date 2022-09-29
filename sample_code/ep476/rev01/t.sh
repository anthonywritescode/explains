set -euxo pipefail

auth_token="$(
    curl 'https://auth.docker.io/token?service=registry.docker.io&scope=repository:precommitci/runner-image:pull' |
    jq --raw-output .token
)"

curl \
    -H "Authorization: Bearer $auth_token" \
    -H "Accept: application/vnd.docker.distribution.manifest.v2+json" \
    https://registry-1.docker.io/v2/precommitci/runner-image/manifests/latest
