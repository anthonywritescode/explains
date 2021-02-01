# [faster than git clone! (beginner - intermediate)](https://youtu.be/YtK1uOa2VpM)

Today I show two different ways to clone a repository (especially a big one) much much faster!  I also show how to clone an arbitrary commit speedily as well

## Interactive examples

### Bash

```bash
time git clone git@github.com:pypa/virtualenv
rm -rf virtualenv/

time git clone git@github.com:pypa/virtualenv --depth=1
cd virtualenv/
git log
git blame src/virtualenv/info.py

git init pre-commit-hooks
cd pre-commit-hooks/
git remote add origin git@github.com:pre-commit/pre-commit-hooks
git remote -v
git -c protocol.version=2 fetch --depth=1 origin v3.0.0
git checkout FETCH_HEAD
git log

git clone --depth=1 git@github.com:python/cpython
```
