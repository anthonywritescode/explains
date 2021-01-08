# [git fetch (--prune) (beginner - intermediate)](https://youtu.be/oj19T3N2NHY)

Today I talk about `git fetch` as well as the `--prune` argument to it (and why I use it!)

## Interactive examples

### Bash

Session 1:

```bash
cd pyupgrade
git checkout origin/master -b feature1
git branch -r
git branch

git push origin HEAD
git branch -r

# --- After deleting feature1 branch ---

git branch -r
git fetch
git fetch --prune
git branch -r

git config --global fetch.prune true
```

Session 2:

```bash
git clone git@github.com:asottile/pyupgrade
# git clone https://github.com/asottile/pyupgrade

git clone https://github.com/asottile/pyupgrade pyupgrade2
cd pyupgrade2

git branch -r
git branch

git fetch
git branch -r

git push origin :feature1
# git push origin -d feature1
git branch -r
```

### Notes

```text

remote repo:

refs/heads/master
# refs/heads/PR1 deleted
refs/heads/feature1
refs/heads/feature2

|           ^
| fetch     |
|           | push
v           |


==================

local filesystem:


==> git metadata

origin/master/master
# origin/master/PR1 delete this with --prune
origin/master/feature1
origin/master/feature2

|
| checkout
v

==> checked out branches

  master
* feature1
```
