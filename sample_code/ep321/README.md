# [docker beside docker (intermediate - advanced)](https://youtu.be/pDysRzgLpgM)

Today I talk about a setup with docker that looks like nested containers but isn't really.  this is often (incorrectly) referred to as "docker in docker" which is a different thing entirely!

## Interactive examples

### Bash

Session 1:

```bash
ls -al /var/run/docker.sock
docker images
docker ps

ps -ef | grep dockerd
ls -al /tmp/foo/

ls
cat foo

ls -al
echo wat | sudo tee foo
echo $PWD
```

Session 2:

```bash
docker run --rm -ti docker sh
which docker
docker run --rm -ti ubuntu:focal bash
exit

docker run -v /var/run/docker.sock:/var/run/docker.sock:rw --rm -ti docker sh
docker run --rm -ti ubuntu:focal bash
exit

cd tmp/
touch foo
ls
echo hi > foo

docker run -v /tmp/foo:/tmp/foo:ro --rm -ti ubuntu:focal bash
cat /tmp/foo/
exit
exit

docker run -v /var/run/docker.sock:/var/run/docker.sock:rw -v $PWD:$PWD:rw --rm -ti docker sh
cd /tmp/explains
ls
touch foo
echo "hi" > foo

docker run --rm -ti -v $PWD:$PWD ubuntu:focal
ls
cat /tmp/explains/foo
exit
exit

docker run -v /var/run/docker.sock:/var/run/docker.sock:rw -v $PWD:/code:rw --rm -ti docker sh
ls /code/

hostname
docker inspect $(hostname)
exit

docker run --hostname foo -v /var/run/docker.sock:/var/run/docker.sock:rw -v $PWD:/code:rw --rm -ti docker sh
hostname
cat /proc/1/cgroup
docker inspect <container_id>
```
