# [what is a boolean trap? (programming antipattern) (beginner - intermediate)](https://youtu.be/CnRkXO_a5mI)

Today I talk about a boolean trap, how you can spot one in code review, and how you can fix the problem using a few python features!

## Interactive examples

### Python

```python
import collections
dct = collections.OrderedDict({1: 2, 3: 4, 5: 6})
dct
dct.popitem(True)

def odict_popitem(dct, last=True):
    return dct.popitem(last=last)

odict_popitem(dct, True)

def odict_popitem(dct, *, last=True):
    return dct.popitem(last=last)

odict_popitem(dct, True)
odict_popitem(dct, last=True)
odict_popitem(dct, lst=True)

dct = collections.OrderedDict({1: 2, 3: 4, 5: 6})
import enum

PopPosition = enum.Enum('PopPosition', 'BEGIN END')
PopPosition.BEGIN
PopPosition.END

from typing import OrderedDict, Tuple, TypeVar

K = TypeVar('K')
V = TypeVar('V')
def odict_popitem(dct: OrderedDict[K, V], pos: PopPosition = PopPosition.END) -> Tuple[K, V]:
    if pos is PopPosition.END:
        return dct.popitem(last=True)
    else:
        return dct.popitem(last=False)

odict_popitem(dct, PopPosition.END)
odict_popitem(dct, pos=PopPosition.END)
```
