# [how do I make an empty generator? (intermediate)](https://youtu.be/b0mUqJc4a2g)

today I talk about how (and a little bit why) to make an empty generator in python!  the syntax is a little quirky but I show you the details about what makes a generator a generator and why it's tricky to write an empty one!

## Interactive examples

### Python

```python
def f(): pass

f()

import dis
dis.dis(f)

def gen():
    yield

gen()
list(gen())

def gen():
    return
    yield

gen()
list(gen())

import inspect
inspect.isgeneratorfunction(gen)
```

### Bash

```bash
python3
python3 -m pydoc inspect

virtualenv venv
. venv/bin/activate
pip install mypy

mypy --warn-unreachable t.py
```
