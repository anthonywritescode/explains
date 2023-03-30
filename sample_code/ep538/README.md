# [weird python identity quirk? (intermediate)](https://youtu.be/w4GasVbjIbA)

In today's video we explain a weird quirk of identity -- and why something that seems equivalent is actually very different

## Interactive examples

### Python

```python
's' * 2 is 's' * 2

i = 2
's' * i is 's' * i

import dis
def f():
    's' * 2 is 's' * 2

def g():
    i = 2
    's' * i is 's' * i

dis.dis(g)
dis.dis(f)

f.__code__.co_consts
```


### Bash

```bash
python
```
