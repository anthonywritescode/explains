# [reset a clone with git clean! (beginner - intermediate)](https://youtu.be/cE9IRYDMoS8)

Today I talk about a command I use pretty often to reset a repository back to a clean state!  the "nuclear" options to `git clean`

## Setup commands

```bash
git clone git@github.com:asottile/pyupgrade
# git clone https://github.com/asottile/pyupgrade
cd pyupgrade

virtualenv venv
. venv/bin/activate
pip install tox
```

## Interactive examples

### Bash

```bash
tox -e py38
ls .tox/
git status
touch foo
mkdir bar
touch bar/wat
mkdir empty
git status

git clone git@github.com:asottile/astpretty
git clean --help
git clean -fxfd --dry-run
git clean --dry-run
git clean -d --dry-run
git clean -df --dry-run
git clean -dff --dry-run
git clean -x --dry-run
git clean -xd --dry-run
git clean -fxfd
git clean -f -x -f -d
git status
```
