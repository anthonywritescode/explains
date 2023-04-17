# [when `git add .` doesn't work (intermediate)](https://youtu.be/N0TFxl7A5Hw)

Today I show a particular monorepo case where `git add .` didn't work as the user expected -- and introduce an interesting alternative!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/astpretty
cd astpretty/

nano README.md
cd tests/
git status
git add .
echo $?
git status

git add ..
git status
git reset ..

git add :/
git status

git reset :/
git add ':(top)'
git status
```
