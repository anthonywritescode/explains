# [python: what is `__main__` / `__main__.py` ? (beginner - intermediate)](https://youtu.be/FRxDmVVm0d0)

Today I show what `__main__` means for python (the two places you'll run into it) as well as how to make modules and packages runnable with `__main__.py`!

## Interactive examples

### Bash

```bash
python t.py
python -c 'import t'

mkdir mymod
touch mymod/__init__.py

virtualenv venv
. venv/bin/activate

pip install pre-commit
python -m pre_commit --help

python -m mymod
python -m t
```
