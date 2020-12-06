# [python implicit string joining (beginner - intermediate)](https://youtu.be/5Zto6VYsNsI)

Today I explain a tricky "feature" of python that is pretty easy to trip up on: string literal joining.

## Interactive examples

### Python

```python
'hello' 'world'

def f():
    return 'hello' 'world'

import dis
dis.dis(f)

def f():
    return 'hello' + 'world'

dis.dis(f)

x = 'thing'
'hello' f'{x}!'
```

### Bash

```bash
gcc t.c
./a.out
```
