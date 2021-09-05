# [python has an optimizer? (intermediate)](https://youtu.be/i8uNgEchr20)

Today I talk about python's peephole optimizer and how it ~optimizes some expressions and branches

## Interactive examples

### Python

```python
import dis


def f():
    x = 2 + 2
    return x

dis.dis(f)


def f():
    x = 2 + 2 * 5 + 3
    return x

dis.dis(f)


def f():
    s = 'foo' + 'bar'

dis.dis(f)


def f():
    b = True and False

dis.dis(f)


def f():
    if True:
        if False:
            print('hi')

dis.dis(f)
```
