# [python @decorators - (intermediate)](https://youtu.be/WDMr6WolKUM)

Probably the most asked question on my channel -- what are those funny @ signs!

I explain a simple decorator, a decorator factory, and some common decorators you'll find in python.

## Interactive examples

### Python

```python
import t

t.f(1)
t.f.__name__
t.f.__doc__
t.f.__annotations__

t.f.__module__
t.f.__wrapped__


import t
c = t.C(5)
c.x
c.y
t.C.func()
t.C(5).func()
```

### Bash

```bash
python -i t.py
```
