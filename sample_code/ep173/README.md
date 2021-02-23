# [python: binary search the easy way (interview tips) (intermediate)](https://youtu.be/icoYNPoTZ44)

Today I go over the much much easier way to handle binary search!  I've found this is much better than trying to implement it on the fly in an interview setting.

## Interactive examples

### Python

```python
x = [1, 2, 5, 10, 20, 25]
value = 11

import bisect
bisect.bisect(x, value)
x.insert(bisect.bisect(x, value), value)
x
```

### Bash

```bash
python -m pydoc bisect
all-repos-grep 'import bisect'
```
