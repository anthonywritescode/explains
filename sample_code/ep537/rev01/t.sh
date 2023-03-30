set -euo pipefail

image=pre-commit-ci/runner-image
tag=latest

auth_token="$(
    curl "https://ghcr.io/token?scope=repository:$image:pull" |
    jq --raw-output .token
)"

curl \
    -v \
    -H "Authorization: Bearer $auth_token" \
    "https://ghcr.io/v2/$image/manifests/$tag" |&
    grep -i docker-content-digest

echo
