# [top 10 new things in python 3.10 (beginner - intermediate)](https://youtu.be/jUwPmbHnlt0)

3.10 is coming!  here's the new things to look out for!

## Interactive examples

### Python

```python
# python3.10

from typing import Union
Union[int, str]
int | str
type(int | str)

1231341234
(1231341234).bit_count()
(12313412341111).bit_count()

dct = {1: 2, 3: 4}
dct.keys()
dct.keys().mapping

import sys
sys.stdlib_module_names
sys.builtin_module_names

'__hello__' in sys.stdlib_module_names
import __hello__

anext
next
aiter
iter

lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
for x, y in  zip(lst1, lst2):
    print(f'{x=} {y=}')

for x, y in  zip(lst1, lst2, strict=True):
    print(f'{x=} {y=}')

lst1 = iter([1, 2, 3])
lst2 = iter([1, 2, 3, 4, 5])
for x, y in  zip(lst1, lst2, strict=True):
    print(f'{x=} {y=}')
```

### Bash

```bash
python3.10 --version --version
python3.10 t.py
python3.8 t.py
wc -l !$
pypy3 t.py
```
