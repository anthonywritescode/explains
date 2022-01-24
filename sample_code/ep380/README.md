# [git: what does "fast forward" mean? (intermediate)](https://youtu.be/Vy0JIwQoI-E)

Today we talk a bit about git merges and what "fast forward" means as well as go over the `--ff-only` and `--no-ff` tags!

## Interactive examples

### Bash

```bash
# git clone https://github.com/asottile/astpretty
git clone git@github.com:asottile/astpretty
cd astpretty/

git reset --hard HEAD^^^^^^^^^
git log
git fetch
git log --decorate origin/master --oneline --graph
git merge origin/master

git reset --hard HEAD^^^^^^^^^
git merge --ff-only origin/master

git reset --hard HEAD^^^^^^^^^
git commit -m 'some commit' --allow-empty
git log
git merge --ff-only origin/master
git merge origin/master
git merge --abort

git reset --hard origin/master
git status
git checkout origin/master -b feature
git commit -m 'foo' --allow-empty
git log

git checkout master
git merge feature
git log

git reset --hard origin/master
git merge --no-ff feature
git log

git reset --hard origin/master
git merge --no-ff --no-edit feature
git show
```
