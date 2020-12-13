# [undoing an accidental git commit (intermediate)](https://youtu.be/EcciszFDpn8)

Today I show how to remove an accidental git commit using either reset or rebase!

## Setup commands

```bash
git clone git@github.com:asottile/scratch
# git clone https://github.com/asottile/scratch

cd scratch
```

## Interactive examples

### Bash

```bash
git reset --hard <commit_hash>

git show <commit_hash>

nano .gitconfig

git status

git pull --ff-only

git reset --soft <commit_hash>^

git status

git diff --staged

git reset .gitconfig

git diff

git status

git checkout -- .

git pull --ff-only

git rebase -i <commit_hash>^

git show <commit_hash>

git log
```
