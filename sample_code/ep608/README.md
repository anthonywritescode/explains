# [python: the assret incident](https://youtu.be/vLra6vLMzY4)

today we're talking about namespacing and some mistakes and fixes python has made!

## Interactive examples

### Python

```python
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))
Point(1, 2)
Point(x=1, y=2)

inst = Point(x=1, y=1)
inst._asdict()

import dataclasses

@dataclasses.dataclass
class Point:
    x: int
    y: int

Point
Point(1, 2)
Point(x=1, y=2)

inst = Point(x=1, y=2)
dir(inst)

dataclasses.fields(inst)

@dataclasses.dataclass
class Point2:
    _x: int
    _y: int

dataclasses.fields(Point2)
namedtuple('Point2', ('_x', '_y'))

from unittest import mock

m = mock.Mock()
m
m()
m(1, 2)
m(1, x=2)
m.foo = 2

import os

with mock.patch.object(os, 'getcwd', return_value='wat'):
    print(os.getcwd())

dir(m)

m = mock.Mock()
m(1, 2)
m.assert_called_once_with(1, 2)
m.assert_called_twice_with(1, 2)
m.foo.bar.baz.whatever.whatever

from unittest import mock
m = mock.Mock()
m.assert_called_twice_with(1, 2)
m.assret(1, 2)
```

### Bash

```bash
python3

docker run --rm -ti python:3.4-slim
```
