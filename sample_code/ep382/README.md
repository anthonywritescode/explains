# [don't lru\_cache methods! (intermediate)](https://youtu.be/sVjtp6tGo0g)

Today I show a common pitfall with `lru_cache` and how it will almost always be a memory leak if used on a method!

## Interactive examples

### Python

```python
C(10).compute(4)

c = C(10)
c.compute(4)
c.compute(4)

C(10).compute(4)
C(10).compute(4)

c = C(10)
c = None

C(10)
_
2 + 2

c = C(10)
c.compute(4)
c = None

C.compute.cache_info()

c = C(10)
c.compute(4)
c = None

import gc
gc.collect()
```

### Bash

```bash
python -i t.py
```
