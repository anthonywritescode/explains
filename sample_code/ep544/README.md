# [docker: secrets at build time! (intermediate)](https://youtu.be/aK6sJDOn2Hc)

Today we tackle another tricky problem with docker: secrets!  I show a few ways to get this wrong (where the secret ends up in the image) and then show off a buildkit feature that solves this nicely!

## Interactive examples

### Bash

```bash
docker build --build-arg SECRET='hello hello secret' -t test .
docker history test

readlink -f $(which docker)

# DOCKER_BUILDKIT=1 docker build ...

docker build --secret id=mysecret,src=$PWD/secretfile -t test .
docker history test
docker history test --no-trunc

docker build -t test .

# Start the ssh agent and add ssh key to it

docker build --ssh default -t test .
```
