# [recovering from git mistakes w/ ORIG\_HEAD (intermediate)](https://youtu.be/yhtq_PSekdo)

Today I show another technique for recovering from git mistakes by utilizing `ORIG_HEAD`.  I also show a cool technique to use it to redo a commit

## Interactive examples

### Bash

```bash
# git clone https://github.com/asottile/astpretty
git clone git@github.com:asottile/astpretty
cd astpretty/

ls .git
cat .git/HEAD

git reset --hard HEAD^^^^

ls .git
cat .git/ORIG_HEAD

git log ORIG_HEAD
git status

git reset --hard ORIG_HEAD
git status

git reflog

cd ..
git init foo
cd !$

touch file.txt
git add !$

git status
git commit -m "first commit"

nano file.txt
nano .env

git add .
git commit -m "hello world"
git show

git reset HEAD^ --soft
git reset .env
git status

nano .gitignore
git add .gitignore

git show ORIG_HEAD
git commit -C ORIG_HEAD
```
