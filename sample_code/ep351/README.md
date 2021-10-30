# [pretty recursive diffs! (beginner - intermediate)](https://youtu.be/vEUFrmrS7Hc)

Today I show a technique I use to compare lots of files at once -- and a small trick with `git` to make them prettier!

## Interactive examples

### Bash

```bash
virtualenv venv
. venv/bin/activate
bash ./t.sh

man diff

diff <(echo a) <(echo b)
diff -u <(echo a) <(echo b)

diff -r out_baseline/ out_master/
diff -u -r out_baseline/ out_master/

git diff --no-index out_baseline/ out_master/
diff -ur out_baseline/ out_master/
diff -s -ur out_baseline/ out_master/

man git-diff
```
