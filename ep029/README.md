# [git: empty initial commit (beginner - intermediate)](https://youtu.be/BJ4hkYdb1LI)

Today I explain why I put an empty initial commit at the beginning of my repository's history!

## Interactive examples

### Bash

Session 1:
```bash
git init x
git init y
cd x/
ls
git commit -m 'empty initial commit' --allow-empty
git show
touch foo
touch bar
git add .
git status
git commit -m 'initial commit'
echo '*.pyc' > .gitignore
git commit -m 'add gitignore'
git status
git log
git rebase -i <empty commit id>
git log
```

Session 2:
```bash
cd y
touch foo bar
git add .
git commit -m 'initial commit'
echo '*.pyc' > .gitignore
git add !$
git commit -m 'add gitignore'
git log
git rebase -i --root
git log
touch baz
git add .
git commit --amend
```
