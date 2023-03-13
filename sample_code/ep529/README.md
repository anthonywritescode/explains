# [positional / named only without `*` or `/`? (intermediate)](https://youtu.be/DatCgcsF6B8)

Today's video is a bit of a puzzle!  how to implement python's named-only / positional-only arguments but without the special syntax!

## Interactive examples

### Python

```python
def f(*, bar): print(bar)

f(1)
f(bar=1)

def f(bar, /): pass

f(bar=1)

def f(**kwargs): pass

f(1)
f(bar=1)

def f(**kwargs):
    bar = kwargs.pop('bar')
    if kwargs:
        raise TypeError(f'unexpected named arguments {", ".join(sorted(kwargs))}')

f()
f(bar=1)
f(bar=1, barasdfasdfasdf=1)

def f(*args): pass

f(bar=1)
f(1)
f(1, 2, 3, 4, 5)

def f(*args): print(args)

f(1)
f(1, 2, 3, 4, 5)

def f(*args):
    bar, = args
    print(bar)

f(1)
f(1, 2)
f()
```

### Bash

```bash
python
```
