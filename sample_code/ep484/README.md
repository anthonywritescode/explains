# [how does swapping work in python? (beginner - intermediate)](https://youtu.be/cMiqfkpMh08)

Today I show a common swapping technique in python and how it gets optimized by the compiler.  I also show roughly how the stack-based execution works for this

## Interactive examples

### Python

```python
x = 1
y = 2

z = x

x = y
y = z

x
y

x, y = y, x
x, y

z = (y, x)
z
x, y = z
x, y

def f(x, y):
    y, x = x, y
    print(y, x)

import dis
dis.dis(f)

def f(x, y):
    z = (x, y)
    y, x = z

dis.dis(f)
```

### Bash

```bash
python
```
