# [python: traceback basics + raise from (beginner - intermediate)](https://youtu.be/wc6W-RaMJ7k)

Today I talk about tracebacks!  how to read them, why python's are the right-side-up, and how `raise from` affects multi-tracebacks!

## Interactive examples

### Python

```python
raise AssertionError('hello hello')

raise AssertionError('hello hello') from None

try:
    exec('print(')
except SyntaxError as e:
    raise AssertionError('hello hello') from e
```

### Bash

```bash
git clone git@github.com:asottile/pyupgrade
# git clone https://github.com/asottile/pyupgrade
cd pyupgrade/

tox --devenv venv
. venv/bin/activate

babi pyupgrade/_plugins/set_literals.py
babi t.py
pyupgrade t.py

git grep 'except.*'
babi pyupgrade/_main.py
pyupgrade t.py
```
