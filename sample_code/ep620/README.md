# [linus messed up the linux git history (so now there's a new git option)](https://youtu.be/Drz8PgWSR4Y)

today we talk about unrelated git histories and how one accidentally crept into the linux kernel!

## Setup commands

```bash
git clone git@github.com:jaseci-labs/archived-jaseci jaseci-archived
git clone --no-checkout git@github.com:torvalds/linux --filter tree:0
```

## Interactive examples

### Bash

```bash
cd jaseci-archived/
git log --max-parents=0

git show <commit_hash>
git log -- components/.gitignore

cd ..
git clone git@github.com:asottile/astpretty
cd astpretty/

git remote add tokenize-rt git@github.com:asottile/tokenize-rt
git fetch --all

git checkout origin/main -b my-branch
git merge
git merge tokenize-rt/main

git merge --help
git merge tokenize-rt/main --allow-unrelated-histories

cd ..

git clone git@github.com:asottile/test-plz-ignore
cd test-plz-ignore/

git log
git log --max-parents=0

cd ../linux/
git log --max-parents=0

cd ../test-plz-ignore/
git pull --ff-only
git log --max-parents=0
```
