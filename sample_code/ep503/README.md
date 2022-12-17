# [docker: multi-stage builds (intermediate)](https://youtu.be/OVYNUg0aODw)

Today I talk about docker multi-stage builds -- why they're useful, and yet why I tend to avoid them!

## Interactive examples

### Bash

```bash
docker images
docker build -t img .
docker run --rm -ti img bash
hello-hello-world
exit

docker images | head -5

docker run --rm -ti img bash
du -hs /usr/local/bin/hello-hello-world

docker build -t img .
docker images | head -5

docker run --rm -ti img bash
hello-hello-world
exit

dpkg -l | grep uuid
apt-cache search uuid-dev

docker build -t img-build --target builder .
docker build -t img --target final .
```
