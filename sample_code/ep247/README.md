# [python: exception catching and isinstance gotcha (beginner - intermediate)](https://youtu.be/dS8rdjZrCaA)

Today I talk about exception handling in python, how to handle multiple types, how to handle variables types, and the difference between `except` and `isinstance`

## Interactive examples

### Python

```python
# python2
try:
    raise AssertionError('foo')
except AssertionError, TypeError:
    pass

TypeError

#python3
try:
    raise AssertionError('foo')
except AssertionError, TypeError:

x = 5

isinstance(x, (int, (int, (float, str))))

try:
    raise AssertionError('foo')
except (AssertionError, (TypeError, ValueError)):
    pass
```

### Python debugger (pdb)

```
issubclass(int, C)
```

### Bash

```bash
python t.py
python2
python -m pydoc contextlib
python t2.py
```
