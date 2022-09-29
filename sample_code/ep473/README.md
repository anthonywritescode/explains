# [docker multi-arch images (intermediate)](https://youtu.be/G6wCo1WBPTo)

Today we talk about multi-architecture images and how to build them with docker and podman!

## Interactive examples

### Bash

```bash
docker login ghcr.io

sudo docker run --privileged --rm tonistiigi/binfmt --install arm64
docker buildx create --use

babi Dockerfile

docker buildx build --push --tag ghcr.io/<username>/multiarch-example:latest --platform linux/arm64,linux/amd64 .

docker buildx build --push --tag ghcr.io/<username>/multiarch-example2:latest-arm64 --platform linux/arm64 .
docker buildx build --push --tag ghcr.io/<username>/multiarch-example2:latest-amd64 --platform linux/amd64 .

docker manifest create ghcr.io/<username>/multiarch-example2:latest --amend ghcr.io/<username>/multiarch-example2:latest-amd64 ghcr.io/<username>/multiarch-example2:latest-arm64
docker manifest push ghcr.io/<username>/multiarch-example2:latest

sudo apt install qemu-user-static
podman buildx build --platform linux/arm64 --tag ghcr.io/<username>/whatever .
podman manifest create ...
```
