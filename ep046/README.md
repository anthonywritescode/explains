# [fixing a git mistake with reflog (intermediate)](https://youtu.be/R8R9_eT2law)

Today I show a technique that has saved me many headaches while working with git (rebases / amends / merges / etc.)

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit

cd pre-commit
```

## Interactive examples

### Bash

```bash
git reflog
git log
git branch -r
git merge <branch_name>
git status

git reflog
git reset --hard <commit_hash>
git log

nano setup.cfg
git add -u
git commit --amend
git reset --hard <commit_hash>
git reset --hard <amended_commit_hash>
```
