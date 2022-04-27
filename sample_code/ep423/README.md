# [double underscored names are NOT "more private" (beginner - intermediate)](https://youtu.be/IVqLW1NWtPc)

I see this mistake all the time!  so I explain how it works and why the feature exists!

## Interactive examples

### Python

```python
c = C(1, 2)
c._x
c._y

from typing import NamedTuple

class NT(NamedTuple):
    x: int
    y: int


NT(1, 2)
nt = NT(1, 2)

c = C(1, 2)
c._x
c.__y
c._C__y

d = D(1)
d._C__y
```

### Bash

```bash
python -im t
```
