# [module level \_\_getattr\_\_ (intermediate)](https://youtu.be/rRwJdMY2f4g)

Today I talk about one of the ways to introduce magic in python -- module level `__getattr__`.  I also walk through the usual uses of this as well as some of the more magical ones!

## Interactive examples

### Python

```python
import t

t.x
t.asdfasdfasdf

import t

t.x
t.c
t.asdfasdfasdf

from py.error import ENOENT
ENOENT

import t
t.foo
```

### Bash

```bash
python t.py

all-repos-grep '^def __getattr__' -- '*.py'

pip install pytest
```
