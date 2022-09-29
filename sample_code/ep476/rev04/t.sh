set -euxo pipefail

image=precommitci/runner-image

auth_token="$(
    curl "https://auth.docker.io/token?service=registry.docker.io&scope=repository:$image:pull" |
    jq --raw-output .token
)"

curl \
    -H "Authorization: Bearer $auth_token" \
    -H "Accept: application/vnd.docker.distribution.manifest.list.v2+json, application/vnd.docker.distribution.manifest.v2+json;q=.9" \
    https://registry-1.docker.io/v2/$image/manifests/latest | jq .
