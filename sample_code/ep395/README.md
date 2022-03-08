# [why did I run `cd $PWD` ??? (beginner - intermediate)](https://youtu.be/7tSVb0d0fyA)

Today I show off a bit of an odd command that looks like a mistake -- but also has some useful applications!

## Interactive examples

### Bash

Session 1:

```bash
# git clone https://github.com/pre-commit/identify
git clone git@github.com:pre-commit/identify
rm -rf identify/
git clone git@github.com:pre-commit/identify
ls ./identify

python -c 'import os; print(os.environ["PWD"])'
cd $PWD
```

Session 2:

```bash
cd identify
git status
ls

ls
git status

echo $PWD
pwd

cd $PWD
ls
```
