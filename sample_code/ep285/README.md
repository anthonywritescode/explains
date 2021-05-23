# [line buffering vs. block buffering (intermediate)](https://youtu.be/gdU1QiKKSbE)

Today I talk about the differences between two common buffering strategies and how it affects both `python` and `grep` -- and why I choose to use `--line-buffering` for grep!

## Interactive examples

### Bash

Session 1:

```bash
nano ~/.bash_aliases
unalias grep
type grep

python t.py
python t.py | cat
python -u t.py | grep hi
PYTHONUNBUFFERED=1 python t.py | grep hi
python t.py | grep hi | cat
python t.py | grep hi --line-buffered | cat
```

Session 2:

```bash
unalias grep
type grep
python --help | less
# python3 --help | less
```
