# [what is immutability? (beginner - intermediate)](https://youtu.be/OjLxyRyzzuY)

Today I talk about the concept of immutability and all the things that are immutable in python.  I also talk about how to enforce "immutability" using typing!

## Interactive examples

### Python

```python
tp = (1, 2, 3)
tp[0]
tp[0] = 2

tp + (1,)
tp

x = 1
x = 2

True
True + 1

'foo'
x = 'foo'
x[0]
x[0] = 'g'

b'foo'
bt = bytearray(b'foo')
bt
bt[0] = ord(b'g')
bt

123.4
123 + 5j

import functools
from typing import List

@functools.lru_cache(maxsize=10)
def func(x: int) -> List[int]:
    return [x] * x


func(1)

lst = func(1)
lst
lst.append(5)
lst.extend((1, 2, 3))
lst

func(1)

x = {1: 2}
x[3] = 4
x
```

### Bash

```bash
python

virtualenv venv
. venv/bin/activate
pip install mypy

python t.py
mypy t.py
```
