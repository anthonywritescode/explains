# [debugging with dir() (+\_\_dir\_\_) (beginner - intermediate)](https://youtu.be/LxCdn18eGng)

Today I talk about the dir() builtin and how it's helpful for debugging when tab complete isn't working!

## Setup commands

```bash
git clone git@github.com:pre-commit/pre-commit
# git clone https://github.com/pre-commit/pre-commit
cd pre-commit

virtualenv venv
. venv/bin/activate
pip install -e .
```

## Interactive examples

### Python debugger (pdb)

```
list
dir(hook)
pp dir(hook)
hook.entry
dir()
ll .
```

### Python

```python
c = C()
c.a
c.s
c.S
c.asdfasdf
dir(c)
```

### Bash

```bash
babi pre-commit/languages/python.py
pre-commit run flake8 --all-files
python -i t.py
```
