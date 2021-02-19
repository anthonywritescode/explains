# [python typing: @overload (intermediate)](https://youtu.be/rY9NZ-tXiDQ)

Today I talk about the @overload decorator for typing and how it can be used to signal typed-dispatch to a type checker!  I also demo a few quick use cases

## Interactive examples

### Python

```python
foo = b'foo'
foo
list(foo)
foo[0]
foo[1:]
foo[0.]

class C:
    def __index__(self): return 2

foo[C()]
foo[slice(1, None, None)]
```

### Bash

```bash
virtualenv venv
. venv/bin/activate
pip install mypy

python t.py
mypy t.py
```
