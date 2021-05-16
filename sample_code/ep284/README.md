# [git: check in executable file (+ on windows) (beginner - intermediate)](https://youtu.be/Ud6t-mIyhsw)

Today I show how to check in an executable script, and the tricky command to do it on windows (which doesn't really have the same permissions model)

## Interactive examples

### Bash

Session 1:

```bash
git init x
cd !$
git commit -m 'initial empty commit' --allow-empty

babi t.sh
./t.sh
chmod +x t.sh
touch t
ls -al
./t.sh
git add t.sh
git diff --staged
git add t
git diff --staged
git commit -m 'check in executable script'

cd ..
ls
git clone x z
cd z
ls -al
```

### Windows CMD

```batch
mkdir tmp
cd tmp
git init x
cd x
git commit --allow-empty -m "empty initial commit"
chmod +x t.py
t.py
ls -al
chmod -x t.py
t.py
git add t.py
git diff --staged
git update-index --chmod=+x t.py
git diff --staged
```
