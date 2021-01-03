# [git: a checked-in directory (intermediate)](https://youtu.be/_qCzcB80fAY)

Today I demo a technique to have a checked in directory in git, but ignore all of its contents!

## Interactive examples

### Bash

Session 1:

```bash
cd /tmp
mkdir explains
cd !$
ls

git init .
mkdir local
git status
touch local/build_output
git status

nano .gitignore
git status
rm .gitignore

nano local/.gitignore
git status

git commit --allow-empty -m 'initial empty commit'
git add --force local/.gitignore
git status

git checkout -- .
git commit -m 'force add local gitignore'

nano local/.gitignore
git diff
git status
git checkout -- .

git reset local/
git status
git reset local/.gitignore
git rm local/.gitignore
git status

git commit --amend
git reset --hard HEAD^
git status

nano local/.gitignore
git status
git add local/
git reset local/.gitignore
git status

git add local/
git commit -m 'add local direcotry'
```

Session 2:

```bash
cd /tmp/
git clone explains explains2
cd explains2
ls

cd ..
rm -rf explains2
git clone explains explains2
cd explains2
ls local/
```
