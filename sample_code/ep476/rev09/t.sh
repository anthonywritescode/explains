set -euxo pipefail

image=precommitci/runner-image
tag=latest-full

auth_token="$(
    curl "https://auth.docker.io/token?service=registry.docker.io&scope=repository:$image:pull" |
    jq --raw-output .token
)"

resp="$(
    curl \
        -H "Authorization: Bearer $auth_token" \
        -H "Accept: application/vnd.docker.distribution.manifest.list.v2+json, application/vnd.docker.distribution.manifest.v2+json;q=.9" \
        "https://registry-1.docker.io/v2/$image/manifests/$tag"
)"

# https://{registry}/v2/{image}/blobs/{blob}

# curl \
#     --location \
#     -v \
#     -H "Authorization: Bearer $auth_token" \
#     "https://registry-1.docker.io/v2/$image/blobs/$(jq --raw-output .config.digest <<< "$resp" | sed 's/:/%3A/g')" | jq .

blob="$(jq --raw-output '.layers[-1].digest' <<< "$resp" | sed 's/:/%3A/g')"
curl \
    --output out.tgz \
    --location \
    -v \
    -H "Authorization: Bearer $auth_token" \
    "https://registry-1.docker.io/v2/$image/blobs/$blob"
