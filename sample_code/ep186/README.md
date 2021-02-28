# [what is `cd -` / `git checkout -` (beginner)](https://youtu.be/sb1itVtABEk)

Today I talk about `cd -` and `git checkout -` and how they are a quick way to get back to where you were before!

## Interactive examples

### Bash

```bash
mkdir a
mkdir a/b

cd a
cd -
cd -

git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
cd astpretty/
git checkout origin/master -b foo
git checkout -
git checkout -
```
