# [prefer tuples to lists! (intermediate)](https://youtu.be/8nvfOjvOF5w)

Today I talk about the three reasons why I prefer tuples over lists!

## Interactive examples

### Python

```python
lst = []
tup = ()

import sys

sys.getsizeof(lst)
sys.getsizeof(tup)

sys.getsizeof([1, 2, 3])
sys.getsizeof((1, 2, 3))

import dis

def f():
    x = (1, 2, 3)
    return x[1]


def g():
    x = [1, 2, 3]
    return x[1]


dis.dis(g)
dis.dis(f)

import subprocess
subprocess.check_call(['echo', 'hello hello world'])
subprocess.check_call(('echo', 'hello hello world'))
```

### Bash

```bash
python3
```
