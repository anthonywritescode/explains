# [python comprehensions leak scope again (intermediate)](https://youtu.be/ONy8xXbdcUc)

Old man yells at walrus -- I show some weird (intentional) scoping issues with comprehensions!

## Interactive examples

### Python

```python
# python 2
[y for y in range(10)]
y

{z for z in range(10)}
z

import dis

def f():
    return [y for y in range(10)]

dis.dis(f)

# python 3
[y for y in range(10)]
y

def f():
    return [y for y in range(10)]

f()

import dis
dis.dis(f)

# python 3.8
def f(x): return x * 2

input_data = [-1, -2, 0, 1, 2]

results = [(x, y, x/y) for x in input_data if (y := f(x)) > 0]

y
```

### Bash

```bash
python2
python3
python3.8
```
