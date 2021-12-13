# [python: what is weakref? (intermediate - advanced)](https://youtu.be/GGKerIMqHCk)

Today I talk about reference counting and the `weakref` module and some use cases for weak references (and why they're not often needed!)

## Interactive examples

### Python

```python
class C:
    def __del__(self):
        print(f'bye! {self=}')

C()
_
1

c = C()
import sys
sys.getrefcount(c)

d = c
sys.getrefcount(c)
sys.getrefcount(c)

d = None
sys.getrefcount(c)
c = None

c = C()
import weakref
d = weakref.ref(c)
sys.getrefcount(c)
d
d()
_
1

c = C()
import weakref
d = weakref.ref(c)
print(d())
c = 5
print(d())


c = C()
c.c = c
c.c.c.c.c.c.c
1
c = None

import gc
gc.collect()

c = C()
c.x = 1
c.x

c.c = weakref.proxy(c)
c.c.c.c.c.c.x
c = None

hash(C())
dct = weakref.WeakKeyDictionary()
c = C()
dct[c] = 2
print(list(dct.items()))
c = None
print(list(dct.items()))
```

### Bash

```bash
# python3
python
```
