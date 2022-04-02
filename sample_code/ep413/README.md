# [what is rpath? (+relocatability) (intermediate - advanced)](https://youtu.be/01fnuhjMwc0)

Today I talk about rpath and how it's a useful mechanism to make relocatable redistributables (such as python wheels!)

## Interactive examples

### Bash

```bash
sudo apt install libsass-dev

gcc t.c
gcc t.c -lsass

./a.out
ldd a.out

docker run -ti --rm -v $PWD:/src:ro ubuntu:focal bash

cd /src/
ls

./a.out
exit

mkdir lib
cp /lib/x86_64-linux-gnu/libsass.so.1 lib/
tree

gcc -Wl,-rpath=lib t.c -lsass
ldd a.out
objdump a.out
ls

docker run -ti --rm -v $PWD:/src:ro ubuntu:focal bash

cd /src/
ldd a.out

./a.out
exit

virtualenv venv
. venv/bin/activate
pip install onigurumacffi

dpkg -l | grep onig

ls venv/lib/python*/site-packages
ldd venv/lib/python*/site-packages/*onig*.so
```
