# [what is manylinux? (intermediate - advanced)](https://youtu.be/80j-MRtHMek)

Today I talk about the manylinux standard for python distributions and discuss why it was created, how it works, and how to turn off manylinux!

## Interactive examples

### Bash

Session 1:

```bash
virtualenv venv
. venv/bin/activate
pip wheel pycurl
ls

unzip pycurl*.whl
ldd pycurl*.so

rm -rf curl/ pycurl*
pip downlaod onigurumacffi
rm cffi*.whl pycparser*.whl
ls

mkdir y
cd y
unzip ../onigurumacffi*.whl

ldd _onigurumacffi.abi3.so
```

Session 2:

```bash
git clone git@github.com/asottile/onigurumacffi
cd onigurumacffi/
ls
nano bin/build-manylinux-wheels

docker pull quay.io/pypa/manylinux1_x86_64:latest
docker run --rm -ti quay.io/pypa/manylinux1_x86_64 bash
/opt/python/cp36-cp36m/bin/pip wheel --no-deps --no-binary :all: editdistance-s
ls

auditwheel --help
auditwheel repair editdistance-s*.whl
ls wheelhouse/

uname -a
cat /etc/redhat-release
```
