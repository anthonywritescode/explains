# [python parameter defaults are (mutable) globals (intermediate)](https://youtu.be/x7kRGQNUJ5I)

Today we talk about parameter defaults in python and why you shouldn't use mutable default values (as well as typing-compatible patterns to fix it!)

## Interactive examples

### Python

```python
f
f()
f(2)

f.__defaults__
f.__defaults__ = (9001,)
f()

f()
f([1, 2])

f([1, 3])
f([1, 3])

f()
f()
f.__defaults__
```

### Bash

```bash
python -i -m t

virtualenv venv
. venv/bin/activate
pip install mypy

mypy t.py
```
