# [I run 'rm -rf /' and see what happens (beginner - intermediate)](https://youtu.be/iqqNMZj608s)

Today I totally destroy my machine by running rm -rf / --no-preserve-root.  let's see what happens!

## Interactive examples

### Bash

Session 1:

```bash
rm -rf /

podman run --rm -ti ubuntu:focal bash
# docker run --rm -ti ubuntu:focal bash

ls /
rm -rf /

rm -rf / --no-preserve-root
ls
hash -r
ls

echo *
echo dev/*
echo etc/*
echo proc/*

# --- After restoring the file system ---

ls
bash
exit
ls
mkdir foo
ls
cat /etc/lsb-release
```

Session 2:

```bash
podman create ubuntu:xenial
podman export -o out.tgz <container_hash>
du -hs out.tgz
ls
mkdir x
cd !$

ls
tar -xf ../out.tgz
ls

rm etc/hosts etc/hostname etc/resolv.conf
ls

find -maxdepth 1 -type d
find -maxdepth 1 -type d | xargs --replace podman cp {} <container_hostname_hash>:/{}
```
