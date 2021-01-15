# [git apply and manual stashing (intermediate)](https://youtu.be/4LXTaikZfco)

Today I talk about `git apply` and a workflow I use to temporarily store diffs.

## Setup commands

```bash
git clone git@github.com:asottile/babi
# git clone https://github.com/asottile/babi
cd babi
```

## Interactive examples

### Bash

```bash
babi setup.cfg
git diff
git diff > backwards.patch
cat backwards.patch
git status

git checkout -- .
git status
babi setup.cfg

git apply backwards.patch
git status

git checkout -- .
git status

patch --help
patch -p1 -i backwards.patch
git diff
```
