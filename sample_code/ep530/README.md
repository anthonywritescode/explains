# [why git's --intent-to-add ? (intermediate)](https://youtu.be/GEYfAMpA-38)

Today I go over git's `--intent-to-add` feature and what it gets used for!

## Interactive examples

### Bash

```bash
git clone git@githib.com:asottile/astpretty
cd astpretty/

babi hello
git add --intent-to-add hello
git status

git reset hello
git status

git add hello
git status

git reset hello
git add --intent-to-add hello
git status

git diff
git commit --all -m 'commit the thing'

echo hi > f
git add --intent-to-add f
```
