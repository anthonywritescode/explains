# [python descriptors! (advanced)](https://youtu.be/vBys0SwYvCQ)

Today I to into detail about data descriptors, non-data descriptors, what the point of them is, as well as a quick example!

## Interactive examples

### Python

```python
class Q:
    pass


q = Q()
q.x = 1
q.__dict__


C.__init__
C.__init__.__get__
C().__init__

c = C()
meth = C.__init__.__get__(c, type(c))
meth
meth()

c = C()
c.d = 10
c.d
c._d

c = C()
c.f

C.f
C.f.__get__

q = Q()
q.f
q.f
q.__dict__
```

### Bash

```bash
python t.py
python -i t.py
```
