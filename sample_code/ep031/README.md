# [python variable unpackings (beginner - intermediate)](https://youtu.be/ObWh1AYClI0)

Today I explain how python implements multiple assignment, multiple return values, and other unpackings as well as PEP 448 (generalized unpackings!)

## Interactive examples

### Python

```python
x = 2
x, y = [1, 2]
print(x)
print(y)

rhs = iter([1, 2])
x = next(rhs)
y = next(rhs)
x
y
x = y = 2

def f():
    return 1, 2

f()
type(f())
foo = f()
foo
z, a = foo()
z
a

lst = [(1, 2), (3, 4)]

for a, b in lst:
    print(f'a: {a}')
    print(f'b: {b}')

lst2 = [(1, 2)]
(a, b), = lst2
a
b

import contextlib

@contextlib.contextmanager
def ctx():
    yield 1, 2

with ctx() as (a, b):
    print(f'{a=}')
    print(f'{b=}')

x, y = {'a': 1, 'b': 2}
x
y

dct_iter = iter({'a': 1, 'b': 2})
next(dct_iter)
next(dct_iter)

# https://www.python.org/dev/peps/pep-0448/
lst = [1, 2, 3, 4, 5]
x = lst[0]
y = lst[1:]
x
y
x, y = lst[0], lst[1:]

x, *y = [1, 2, 3, 4, 5]
x
y

x, *y = (1, 2, 3, 4, 5)
x
y
```
