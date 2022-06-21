# [what is an --orphan git branch? (intermediate)](https://youtu.be/XLuD7KJLMwE)

Today I walk through what an orphan branch is and a few use cases I have for creating them!

## Interactive examples

### Bash

Session 1:

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

git status
git branch -r

git checkout --orphan gh-pages
git log
git status

git reset .
git status

git clean -fxfd
git status
ls

git commit --allow-empty -m 'empty initial commit'
PRE_COMMIT_ALLOW_NO_CONFIG=1 git commit --allow-empty -m 'empty initial commit'

nano README.md
git add !$
PRE_COMMIT_ALLOW_NO_CONFIG=1 git commit -m 'add readme'

git status
git log
git log main
git log main --oneline | wc -l
ls

git merge main
git merge main --allow-unrelated-histories

git status
git merge --abort
git status
```

Session 2:

```bash
git init wat
cd !$
git log
```
