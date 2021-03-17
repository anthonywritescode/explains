# [listing only directories with `ls` (beginner)](https://youtu.be/rNANZNxEUAo)

Today I show a common tip with `ls` to show only directories!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit

cd pre-commit
```

## Interactive examples

### Bash

```bash
ls
man ls

ls -d
ls -d */
ls */

find -maxdepth 1 -type d
find -maxdepth 1 -type d
find -mindepth 1 -maxdepth 1 -type d
find -mindepth 1 -maxdepth 2 -type d
```
