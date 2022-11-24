# [partial git commits (intermediate)](https://youtu.be/UJ5fpaeZWsI)

Today we talk about partial git commits and how you can very carefully add / remove only what you want!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

nano README.md
nano astpretty.py

git status
git checkout -p astpretty.py
git diff

git add -p
git status
git diff --staged
git commit -m 'add some branding to README'

pre-commit run --files astpretty.py

git add -u
git diff --staged
git reset -p
git diff --staged
```
