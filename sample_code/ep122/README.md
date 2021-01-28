# [python: what is \_\_slots\_\_ and \_\_dict\_\_ (intermediate)](https://youtu.be/2d3vZhF-2aA)

Today I talk about `__slots__` and `__dict__` and how they relate to objects!

## Interactive examples

### Python

```python
c = C()
c.__dict__
c.x = 2
c.__dict__
c.__dict__['a'] = 3
c.a

d = D()
d.__dict__
d.x = 2
d.y = 3
d.x
d.y
d.z = 4

e = E()
e.__dict__
e.x = 2
e.y = 3
e.__dict__
e.z = 4
e.__dict__
```

### Bash

```bash
python -i t.py
```
