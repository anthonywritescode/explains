# [the worst git repo (and how I fixed it)](https://youtu.be/Ia6S3cbCrNs)

today I show off how I used `git-filter-repo` and other techniques to fix the history of a really large repository

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install git-filter-repo
```

## Interactive examples

### Bash

```bash
du -hs jaseci/.git

git remote -v
git -C jaseci/ remote -v

cd jaseci/
git log --max-parents=0
git show <commit_hash>

git log -- components/.editorconfig
git log --all -- components/.editorconfig

venv/bin/pip freeze
python3 important-roots.py jaseci/

bash large.sh | less
wc -l rewrite.py

mv jaseci/ original
time python3 rewrite.py

cd ..
git clone git@github.com:asottile/tokenize-rt
cd tokenize-rt/

git log --oneline --first-parent
git show --format=%ct <commit_hash>
git show --format=%cd <commit_hash>

git remote rm origin
git rebase -i <commit_hash>^
git rebase --continue

git log
git log --oneline --first-parent
git show --format=%cd <commit_hash>

git log --help
git show --format=%cd' %cn' <commit_hash>

git log --grep 'Merge branch'
git log --oneline --decorate --graph <commit_hash>
git show <commit_hash>
```
