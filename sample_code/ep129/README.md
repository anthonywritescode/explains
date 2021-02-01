# [git diff A...B (3 dots) (beginner - intermediate)](https://youtu.be/WRXmm-E77aY)

Today I talk about the difference between `git diff A...B` and `git diff A..B` (3 vs 2 dots) and why it's useful!

## Setup commands

```bash
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
cd astpretty
```

## Interactive examples

### Bash

```bash
git log --oneline --graph --decorate
git checkout <commit_hash> -b feature_branch
nano astpretty.py
git status
git add -u
git commit -m 'add hello world'
git diff master
git diff master..HEAD
git diff master...HEAD
git merge-base master HEAD
git diff $(git merge-base master HEAD)..HEAD
git diff $(git merge-base master HEAD)...HEAD
```
