# [what is podman vs docker (beginner - intermediate)](https://youtu.be/lkg5QJsoCCQ)

Today I talk about some of the differences between podman and docker and why I've been using podman recently!

## Interactive examples

### Bash

Session 1:

```bash
podman run --rm -ti ubuntu:focal
type docker
readlink -f $(which docker)
ps -ef | grep podman
```

Session 2:

```bash
ps -ef | grep docker
ls /var/run/docker.sock -al

sudo curl --unix-socket /var/run/docker.sock http:/v2/version | jq .
sudo docker version
```
