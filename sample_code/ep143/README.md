# [easy fake objects with python's SimpleNamespace (beginner - intermediate)](https://youtu.be/8XvyHj8ndg8)

Today I talk about a bit of a hidden gem in python: the SimpleNamespace class!  I also demo a few usecases for testing (where I find it to be the most useful)

## Interactive examples

### Python

```python
from types import SimpleNamespace
import types

types.TracebackType
SimpleNamespace()
SimpleNamespace(a='asdf', b=2, c=123.123)
obj = SimpleNamespace(a='asdf', b=2, c=123.123)
obj.a
obj.b
obj.c
obj.d = 123
obj

class NS:
    pass

NS.a = 123
NS

class NS:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f'{type(self).__name__}({attrs})'

NS(a='1', b='2')
```

### Bash

```bash
python t.py
```
