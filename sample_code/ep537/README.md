# [docker pull by sha256 digest (advanced)](https://youtu.be/AiAU7wnPCrQ)

Today I talk about the "repeatable" way to pull docker images -- by digest!

## Interactive examples

### Bash

```bash
podman manifest inspect ghcr.io/pre-commit/runner-image:latest
podman manifest inspect ghcr.io/getsentry/image-mirror-library-posgres:9.6-alpine

podman pull ghcr.io/getsentry/image-mirror-library-posgres@sha256:<hash>
podman tag ghcr.io/getsentry/image-mirror-library-posgres@sha256:<hash> ghcr.io/getsentry/image-mirror-library-posgres:9.6-alpine
podman run --rm -ti ghcr.io/getsentry/image-mirror-library-posgres:9.6-alpine

bash t.sh
podman pull ghcr.io/pre-commit-ci/runner-image@sha256:<hash>
```
