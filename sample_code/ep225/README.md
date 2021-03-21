# [python: how do any / all work? (beginner)](https://youtu.be/NO8frFR7ZxU)

Today I talk about the any / all builtins in python, show some examples, and then show you how to implement your own versions of them

## Interactive examples

### Python

```python
any
all

any(())
all(())

any((0, 0, 0))
any((0, 0, 1))
any((0, 1, 0))

def gen():
    print('before first')
    yield 0
    print('before second')
    yield 1
    print('before third')
    yield 0

any(gen())

n = 0
if n != 0 and 1 / n == .5:
    print('n was 2')

if all((n != 0, 1 / n == .5)):
    print('n was 2')

all(gen())

def gen():
    print('before first')
    yield 0
    print('before second')
    yield 1
    print('before third')
    yield 0

my_any(())
my_any((0, 0, 0))
my_any((0, 1, 0))
my_any(gen())

my_all(())
my_all((0, 1, 1))
my_all((1, 1, 1))

my_all((1, 1, 'foo'))
all((1, 1, 'foo'))

help(any)
help(all)
```

### Bash

```bash
python -i t.py
```
