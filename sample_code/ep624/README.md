# [you only need 15ish git commands](https://youtu.be/y6meVhckYmQ)

today I show a whirlwind tour of the most common git commands I use

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
```

## Interactive examples

### Bash

```bash
grep -oP '\bgit( -C [^ ]+)? [^ ]+' t | sed -r 's/ -C [^ ]+//g' | sort | uniq -c | sort -rn
cd /tmp/
ls

git clone <directory>
git clone git@github.com:asottile/astpretty
git clone git@github.com:asottile/astpretty --depth=1

cd astpretty/
git log
cd ..

rm -rf astpretty/
git clone git@github.com:asottile/astpretty -b main
rm -rf astpretty/

git init astpretty
cd astpretty/

git remote
git remote add origin git@github.com:asottile/astpretty
git remote
git remote -v

git fetch
git switch main
git branch

cd ..
ls
cd -

git status
echo 'hello hello' >> README.md

git diff
git diff --staged

git add --help
git add README.md
git status

git reset README.md
git status

git add -u README.md
git restore README.md
git status
git restore --help

ls
git rm tox.ini
git status

git mv setup.py{,2}
git status

touch random junk
git add .
git status

git reset junk random
git status

echo 'hi hi' >> README.md
git add -u
git status

echo 'hi' >> README.md
echo "print('hi')" >> astpretty.py
git status
git diff

git add -p
git status
git reset -p

git commit
git commit -m 'commit message'

unset PROMPT_COMMAND
rm .git/hooks/pre-commit
# pre-commit uninstall

git add -u
git commit -m 'some other changes'

echo 'garbage' >> README.md
git add -u

git status
git commit -m 'add some garbage' -m 'some description'

git show
git log

cd ..
git init foo
cd !$

git commit -m 'empty initial commit'
git commit -m 'empty initial commit' --allow-empty
git commit --allow-empty-message --allow-empty
git show

cd -
cd astpretty/

echo 'more garbage' >> README.md
git add -u
git status

git commit --amend
git commit --amend --no-edit
git show

git tag
git checkout v.1.4.0
git status

git show
git checkout <commit_hash>
git checkout <commit_hash>^^^

git branch
git checkout main
git checkout origin/main -b new-branch

git -C <directory> grep set-head
git remote set-head origin --auto
git checkout origin/HEAD -b new-branch2

git status
git switch new-brach

git checkout v1.4.0 -- setup.py
git status

git reset
git status

git checkout -- .
git status

git branch
echo 'hi hi' >> README.md
git add !$

git status
git commit -m 'hi'

git push
git remote -v
git branch

git push origin HEAD
git push origin :new-branch

git branch
git checkout origin/main^^^^^^^^^^^^^ -b old-branch
git branch -u origin/main
git status

echo 'break' >> astpretty.py
git add -u
git commit -m 'update astpretty (breaking it)'
git status
git log

git pull origin main
git pull --no-ff origin main
git status

git show
git log

git show HEAD^
git reset --hard HEAD^

git reflog
git reset --hard <ref>
git reset --soft HEAD^
git status

git reset --hard HEAD^

git fetch
git fetch origin
git fetch --all
git merge origin/main

git reset --hard HEAD^
git status

git rebase -i origin/main
git rebase -i origin/HEAD
git status

git show
git log

cd ../pre-commit

git log --oneline
git log --oneline --decorate
git log --oneline --decorate --graph

git log -G ls-remote
git log -p -G ls-remote

git log --oneline
git log --format='%h %ae'
git log --format='%ae' | sort | uniq -c | sort -rn

git blame pre_commit/store.py
git blame -w pre_commit/store.py
git blame -e -w pre_commit/store.py
git blame -M3 -e -w pre_commit/store.py

git blame pre_commit/store.py
git show <commit_hash>

git ls-files
git ls-files -- '*.py'
git ls-files -- '*.rb'
git ls-files -- '*.go'

nano $(git ls-files -- '*.sh')

git grep
git grep LOCAL_REPO_VERSION
git grep -l LOCAL_REPO_VERSION
nano $(git grep -l LOCAL_REPO_VERSION)

nano ~/.gitconfig
nano .git/config

cd ../astpretty/
git status

git clean --help
git clean -fxfd
git clean --dry-run -fxfd

tox -e py313
git status
git clean --dry-run -fxfd
nano .gitignore
```
