# [the docker registry api (advanced)](https://youtu.be/Ce9var-Fty8)

Recently I've been toying around with the docker registry api and I figured I'd show you how it works (and some neat things you can get out of it)

## Interactive examples

### Bash

```bash
# docker pull registry-1.docker.io/library/ubuntu:focal
curl https://registry-1.docker.io/v2/
curl -v https://registry-1.docker.io/v2/

bash -x t.sh

# https://{registry}/v2/{image}/manifests/{tag}

auth_token="$(curl 'https://auth.docker.io/token?service=registry.docker.io&scope=repository:precommitci/runner-image:pull' | jq --raw-output .token)" && curl -H "Authorization: Bearer $auth_token" https://registry-1.docker.io/v2/precommitci/runner-image/manifests/latest

bash t.sh
tar --list -f out.tgz
```
