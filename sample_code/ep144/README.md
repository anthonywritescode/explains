# [what is a git tag? (beginner - intermediate)](https://youtu.be/34CQxHXzD4w)

Today I talk about git tags (lightweight and not) and how they differ from branches

## Setup commands

```bash
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
cd astpretty
```

## Interactive examples

### Bash

```bash
git log --oneline --decorate --graph
git tag test
git log --oneline --decorate --graph
git tag test2 <commit_hash>
git tag test3 <commit_hash> -m 'tag test3'
git log --oneline --decorate --graph
git show test3
git show test2
git tag --sign test5
git show test5
```
