# [why \_\_slots\_\_ = () (namedtuples) (intermediate)](https://youtu.be/BSNd_kxHXL8)

Today I talk about why it's necessary to set `__slots__ = ()` when inheriting from namedtuple classes

## Interactive examples

### Python

```python
C(1, 2)
c = C(1, 2)
c.area_from_origin

c = C(9, 8)
c.area_from_origin

c.x
c.x = 1000
c.y = 123123
c.sdfgsdfg = 234234
c.sdfgsdfg
c.__dict__
c.__dict__['x'] = 123123
c.x
C.x

c = C(9, 8)
c.area_from_origin
c.asdfasdf = 123
```

### Bash

```bash
python -i t.py
```
