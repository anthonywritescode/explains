# [python: easy comparable classes with functools.total\_ordering (intermediate)](https://youtu.be/po7iMzrgJwA)

Today I show how to easily make classes comparable in python!

## Interactive examples

### Python

```python
class C: pass

C() < C()
C() > C()
C() >= C()
C() <= C()

C() != C()
C() == C()

C(1)
C(1) < C(2)
C(1) > C(2)
C(1) >= C(2)
C(1) <= C(2)

x = y = 6
not (x < y) and not (y < x)

object.__eq__

C(1) <= C(2)
C(2) <= C(2)
C(2) >= C(2)

# not a.__lt__(b)
```

### Bash

```bash
python -i t.py
```
