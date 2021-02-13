# [what is docker and how does it work? (intermediate)](https://youtu.be/tWvQAxkMaWs)

Today I finally talk about docker, and how it (and linux in a way) works at a high level.  I show some small examples of how it can be useful for development and how it's different from a VM

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit
```

## Interactive examples

### Bash

```bash
dpkg -l | grep linux

docker run --rm -ti ubuntu:xenial bash
docker images | grep xenial
ls
docker images
dpkg -l | grep libyaml-dev

type docker
readlink $(which docker)
cd testing/zipapp/
docker build -t test .
```
