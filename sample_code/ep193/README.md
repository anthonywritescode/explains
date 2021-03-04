# [git: cleaning up merged branches (beginner - intermediate)](https://youtu.be/5O8PzE4nJTQ)

Today I talk about techniques for cleaning up merged branches (both local and remote)

## Setup commands

```bash
git clone git@github.com:asottile/pyupgrade
# git clone https://github.com/asottile/pyupgrade
cd pyupgrade
```

## Interactive examples

### Bash

```bash
git branch
git checkout origin/master -b test
git status
git commit --allow-empty -m foo

git checkout master
git status

git pull
git branch --merged
git branch --merged | grep -v '\*'
git branch --merged | grep -v '\*' | xargs git branch -d

git checkout master
git branch --remote --merged
git branch --remote --merged | grep -v '>'
git branch --remote --merged | grep -v '>' | grep -v master | sed s'|origin/||g'
git branch --remote --merged | grep -v '>' | grep -v master | sed s'|origin/||g' | xargs --replace git push origin :{}
```
