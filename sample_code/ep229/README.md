# [3 ways to fix an accidental git commit to main (beginner - intermediate)](https://youtu.be/4C2lSosT7hc)

Today I show a few strategies for fixing an accidental commit to the main branch (when you meant to commit to a feature branch)

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
cd astpretty/
ls

nano README.md
git status
git add -u
git commit -m 'add whatever feature'
git status

git branch -m feature-branch
git branch
git status
git checkout master
git status

git checkout feature-branch
git branch -D master
git branch -m master
git branch
git status

git checkout -b feature-branch
# git checkout origin/master -b feature-branch
git status
git branch -u origin/master
git status
git checkout master
git reset --hard origin/master
git status
git branch
git checkout feature-branch

cd ..
git init origin
cd origin
git commit -m foo --allow-empty
git config receive.denyCurrentBranch false

cd ..
git clone origin/ fork
cd !$
ls
git status
git branch
git log

git commit -m bar --allow-empty
git status
git push origin HEAD
git -C ../origin log

# nano README.md
echo 'hello world' > README.md
git status
git add README.md
git commit -m 'add readme'
git push origin HEAD
git -C ../origin log

git revert <commit_hash>
# git revert HEAD
git log
git push origin HEAD
git -C ../origin log

git reset --hard <commit_hash>
# git reset --hard HEAD^
git status
git push origin HEAD -f
git -C ../origin log

git reset --hard <commit_hash>
git push origin HEAD

git checkout origin/master -b feature
git revert <commit_hash>
# git revert HEAD
git status
git log

# nano README.md
echo 'hello hello world' > README.md
git status
git add -u
git commit -m 'fix README'

git checkout master
git reset --hard HEAD^^
git push origin HEAD -f
git -C ../origin log

git checkout origin/master -b feature-2
git cherry-pick <commit_hash>
git show
# nano README.md
echo 'hello hello world' > README.md
```
