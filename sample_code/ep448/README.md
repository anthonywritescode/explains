# [docker: fast CI rebuilds with --cache-from (intermediate)](https://youtu.be/77j6JFBTmTc)

Today I show how to speed up docker builds by using `--cache-from` (and why it's necessary at all!)

## Interactive examples

### Bash

```bash
docker images
# docker pull ghcr.io/deadsnakes/focal

git clone git@github.com:deadsnakes/runbooks
cd runbooks/
ls

ls dockerfiles/Dockerfile.focal
docker build -t img - < dockerfiles/Dockerfile.focal

docker history --no-trunc ghcr.io/deadsnakes/focal
docker build --cache-from ghcr.io/deadsnakes/focal -t img - < dockerfiles/Dockerfile.focal
```
