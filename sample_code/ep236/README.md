# [how to make a virtualenv from cpython source (intermediate)](https://youtu.be/2ETZsYF5c7s)

Today I show how to set up a virtualenv directly from the cpython source tree

## Setup commands

```bash
git clone git@github.com:python/cpython
# git clone https://github.com/python/cpython

cd cpython
```

## Interactive examples

### Bash

```bash
mkdir prefix
./configure --prefix $PWD/prefix
echo $?

make -j5
make install
./python

echo $PWD/prefix
ls $PWD/prefix
ls /usr/
ls $PWD/prefix/bin

./prefix/bin/python3 -m venv venv310a5
virtualenv venv310a5_venv -p prefix/bin/python3
. venv310a5_venv/bin/activate

python --version
pip install pre-commit
```
