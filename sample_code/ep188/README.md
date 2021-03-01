# [what is a singleton? (and python patterns) (intermediate - advanced)](https://youtu.be/PBCsN29ZG9A)

Today I talk about the singleton pattern and a bunch of different ways to implement it in python!

## Interactive examples

### Python

```python
f1 = _Foo()
f2 = _Foo()
f1 is f2

f1.increment_thing()
f2.get_thing()

f3 = _Foo()
f3.get_thing()
f3 is f2

c1 = C()
c2 = c()
c1 is c2

C
isinstance(c1, C)

D()
d1 = D()
d2 = D()
d1 is d2
```

### Bash

```bash
python -i t.py
```
