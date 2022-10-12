# [what is "short circuiting"? (beginner - intermediate)](https://youtu.be/tsrlQ8v4UaM)

Today I go over short-circuit evaluation and how you can use it to avoid errors as well as some tricks for (ab)using logical operators.

## Interactive examples

### Python

```python
True and False
True or False

def t():
    print('returning True')
    return True

def f():
    print('returning False')
    return False

True or f() or t() or f()
False and t() and f()

False & t() & f()

123 and 234
123 and 234 and 0
123 and 234 and 0 and False

0 or False or []
123 or 234 or True

x = None
if x is not None and x.foo():
    print('got truthy from foo()')

if x.foo() and x is not None:
    print('got truthy from foo()')

class C:
    def foo(self) -> bool:
        return True

x = C()
if x is not None and x.foo():
    print('got truthy from foo()')

def f(x):
    x = x or C()
    print(x)

f(False)
f(None)
f([])
f(())
f('')

def f(x):
    x = x if x is not None else C()
    print(f'{x=}')

f(None)
f([])

1 ^ 1
1 ^ 0
0 ^ 1
0 ^ 0
```

### Bash

```bash
python
```
