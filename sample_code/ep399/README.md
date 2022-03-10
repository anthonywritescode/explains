# [what is a .so / .dll / shared object? (intermediate - advanced)](https://youtu.be/PDkKz3zQVls)

Today I introduce the concept of "shared objects" -- show you how to build against them, how they work, how to inspect them, and how python's c module system utilizes them!

## Interactive examples

### Bash

```bash
dpkg -l | grep uuid-dev
dpkg -L uuid-dev

gcc t.c
gcc t.c -l uuid

./a.out
ldd a.out

cat /etc/ld.so.conf.d/*
tail -n999 /etc/ld.so.conf.d/*

docker run -ti --rm -v $PWD/a.out:/a.out ubuntu:focal bash

ldd a.out
rm /lib/x86_64-linux-gnu/libuuid.so.*
ldd a.out
./a.out
exit

docker run -v $PWD/a.out:/a.out:ro -ti --rm ubuntu:jammy bash
./a.out
exit

nm a.out
nm --undefined-only a.out
nm --dynamic /lib/x86_64-linux-gnu/libuuid.so.*
ldd /lib/x86_64-linux-gnu/libuuid.so.*

virtualenv venv
. venv/bin/activate
pip install onigurumacffi

ls venv/lib/python*/site-packages/
ldd venv/lib/python*/site-packages/_onigurumacffi*.so
nm --defined venv/lib/python*/site-packages/_onigurumacffi*.so
```
