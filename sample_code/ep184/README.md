# [what is `git -C ...` (intermediate)](https://youtu.be/YXDn2qtK8GI)

Today I show a neat trick for using `git` in other directories without needing `cd` -- `git -C dir ...`!

## Setup commands

```bash
git clone git@github.com:asottile/astpretty
# git clone https://github.com/asottile/astpretty
```

## Interactive examples

### Bash

Session 1:

```bash
man git
ls
git -C astpretty/ status
```

Session 2:

```bash
cd astpretty/
git status
```
