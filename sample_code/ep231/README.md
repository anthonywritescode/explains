# [how to search a repo using `git grep` (beginner)](https://youtu.be/2MCtRv1ZIFQ)

Today I talk about what I consider one of my most powerful tools when working in a git repository: git grep!  it searches files, and only files which are checked in

## Setup commands

```bash
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty

cd astpretty/
```

## Interactive examples

### Bash

```bash
git remote -v
git grep --help

git grep Tuple
git grep 'main\(.+\)'
git grep -E 'main\(.+\)'

git grep -l -E 'main\(.+\)'
babi $(git grep -l -E 'main\(.+\)')

git grep -l -E 'main\(.+\)' -- tests
babi $(git grep -l -E 'main\(.+\)' -- tests)

git grep -l -E 'main\(.+\)' -- '*.py'
git grep -l -E 'main\(.+\)' -- *.py

echo git grep -l -E 'main\(.+\)' -- *.py
echo git grep -l -E 'main\(.+\)' -- '*.py'

git grep -L -E 'main\(.+\)' -- '*.py'
git grep -L -E 'main\(.+\)'
```
