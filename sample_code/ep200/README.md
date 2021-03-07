# [all about xargs ! (beginner - intermediate)](https://youtu.be/ED9AUfFrak8)

xargs is by far one of the most useful commandline tools I know -- I teach the main things you need to use it so you can look like a commandline wizard too!

## Setup commands

```bash
virtualenv venv
. venv/bin/activate
pip install flake8
```

## Interactive examples

### Bash

```bash
man xargs
touch foo bar

ls *
ls * | xargs echo hello hello

xargs --show-limits
xargs --no-run-if-empty --show-limits

ls * | xargs --verbose echo hello hello
ls * | xargs -t echo hello hello
ls * | xargs -t -n1 echo hello hello
ls * | xargs -t --replace echo hello hello
ls * | xargs -t -I{} echo hello hello
ls * | xargs -t -I{} echo hello hello {} {} {} {} {}
ls * | xargs -t -I{} cp {} {}.bak
ls
rm *.bak

git clone git@github.com:pre-commit/pre-commit
cd pre-commit/

ls * | xargs echo hello hello
ls * | xargs
ls * | xargs echo
ls * | xargs -t
flake8 pre_commit/

git ls-files -- '*.py'
git ls-files -- '*.py' | grep testing
git ls-files -- '*.py' | grep testing | xargs flake8
git ls-files -- '*.py' | grep testing | xargs -t flake8

grep ^processor /proc/cpuinfo

git ls-files -- '*.py' | grep testing | xargs -t -P 5 flake8
git ls-files -- '*.py' | grep testing | xargs -t -P 5 -n 5 flake8
git ls-files -- '*.py' | grep testing | xargs -t -P 5 -n 2 flake8

cd ..
ls
rm -rf pre-commit/
touch 'hello hello world'

ls
ls | xargs --verbose -n1
ls -1
ls -1 | xargs --verbose -n1
ls -1 | xargs -d'\n' --verbose -n1

find -maxdepth 1 -type f
find -maxdepth 1 -type f | xargs -d'\n' --verbose -t
find -maxdepth 1 -type f | xargs -d'\n' --verbose -n1
find -maxdepth 1 -type f -print0
find -maxdepth 1 -type f -print0 | hd -c
find -maxdepth 1 -type f -print0 | xargs -0
find -maxdepth 1 -type f -print0 | xargs -0 -n1
find -maxdepth 1 -type f -print0 | xargs -0 -n1 -t

cd pre-commit
git ls-files -z
git ls-files -z | xargs -0 -n1 | head -5

find -maxdepth 1 -type f
find -maxdepth 1 -type f | grep ohai
find -maxdepth 1 -type f | grep ohai | xargs --verbose
find -maxdepth 1 -type f | grep ohai | xargs --verbose flake8
find -maxdepth 1 -type f | grep ohai | xargs --verbose --no-run-if-empty flake8

ls

find -maxdepth 1 -type f -print0 | xargs -0 echo rm
find -maxdepth 1 -type f -print0 | xargs -0 --replace echo bash -x 'mv {} {}.bak'
find -maxdepth 1 -type f -print0 | xargs -0 --replace bash -x 'echo mv {} {}.bak'
find -maxdepth 1 -type f -print0 | xargs -0 --replace bash -xc 'echo mv {} {}.bak'
find -maxdepth 1 -type f -print0 | xargs -0 --replace bash -xc 'mv {} {}.bak'
```
