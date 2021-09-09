# [git: main vs. origin/main (beginner - intermediate)](https://youtu.be/f-92I_gxgjA)

Today I go over the difference between `main` and `origin/main` as well as the most reliable ways to get a fresh branch and to pull in fresh changes from a git remote!

## Setup commands

Simulate clone of git repository back in time:

```bash
git clone git@github.com:asottile/astpretty tmp
# git clone https://github.com/asottile/astpretty tmp

git -C tmp reset --hard 8455ab7f
git clone tmp astpretty

git -C astpretty remote set-url origin git@github.com:asottile/astpretty
# git -C astpretty remote set-url origin https://github.com:asottile/astpretty
```

## Interactive examples

### Bash

Session 1:

```bash
git branch
git checkout origin/master -b mybranch
git log master
git log origin/master

git checkout master
git reset --hard HEAD^^^

git checkout mybranch
git log master

# Session 2

git branch
git commit -m 'foo' --allow-empty

git merge master
git merge origin/master
git log

git reset --hard HEAD^
git pull origin master

git fetch && git checkout origin/master -b mybranch2
git pull origin master
```

Session 2:

```bash
git log origin/master
git fetch
git log origin/master
```
