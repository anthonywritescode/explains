# [dealing with merge conflicts (beginner - intermediate)](https://youtu.be/vQY309QQfuQ)

Today I walk through a merge conflict and a rebase conflict and walk you through how I go about resolving them!

## Interactive examples

### Bash

Session 1:

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

git checkout <commit_hash> -b my-feature-branch
nano README.md

git add !$
git commit -m "my readme feature"

git branch -u origin/main
git status

git pull origin HEAD
git status

ls .git/

babi README.md
git status

git add README.md
git diff --staged
git status

git commit

git reflog
git reset --hard <commit_hash>

git pull origin HEAD --rebase
git status

nano README.md
git add -u
git status

git rebase --continue
git status
```

Session 2:

```bash
cd astpretty/

git branch
git log

git merge-base my-feature-branch origin/HEAD
git diff $(!!) origin/HEAD

git diff $(merge-base my-feature-branch origin/HEAD) origin/HEAD
git diff my-feature-branch...origin/HEAD
```
