# [python insertion-ordered dicts (beginner - intermediate)](https://youtu.be/thOgrFA7MzI)

Today I talk about insertion ordered dictionaries and when you can rely on them (cpython3.6+) and the differences between `collections.OrderedDict` and normal dict (and recipes if you want to just use dict)

## Interactive examples

### Python

```python
x = {}
x[1] = 2
x[5] = 3
x[3] = 7
x

x[1] = 10
x

del x[1]
x
x[1] = 10
x

import collections
collections.OrderedDict([(1, 2), (3, 4)]) == collections.OrderedDict([(3, 4), (1, 2)])
dict([(1, 2), (3, 4)]) == dict([(3, 4), (1, 2)])
dict([(1, 2), (3, 4)]) == collections.OrderedDict([(3, 4), (1, 2)])

dct = collections.OrderedDict([(1, 2), (3, 4), (5, 6)])
dct.popitem()
dct
dct.popitem(last=False)
dct

dct = collections.OrderedDict([(1, 2), (3, 4), (5, 6)])
dct.move_to_end(3)

dct_eq({1: 2, 3: 4}, {3: 4, 1: 2})
dct_eq({1: 2, 3: 4}, {1: 2, 3: 4})

dct = {1: 2, 3: 4, 5: 6}
dct_popitem(dct)
dct_popitem(dct, last=False)
dct

dct = {1: 2, 3: 4, 5: 6}
dct_move_to_end(dct, 3)
dct
```

### Bash

```bash
python -i t.py
```
