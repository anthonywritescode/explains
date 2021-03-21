# [python: {...} is faster than dict(...) (intermediate)](https://youtu.be/-v4DmRsL7nc)

Today I talk about why dictionary literals (and other literals) are faster than their function-called counterparts

## Interactive examples

### Python

```python
def f():
    return {'a': 1}

def g():
    return dict(a=1)


import dis
dis.dis(f)
dis.dis(g)

def h():
    return dict(A=1, b=2)

dis.dis(h)

def dict(**kwargs):
    print(kwargs)
    return 5

g()
```
