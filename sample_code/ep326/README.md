# [python: what is repr? (beginner - intermediate)](https://youtu.be/ei1q7m3zLfU)

Today I talk about `repr`, what it is, and how to implement `__repr__` for your own classes!

## Interactive examples

### Python

```python
repr
repr(repr)


class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.x!r})'


C(1)
C('foo' + "bar")


class D: pass
D()

type(D()).__module__
type(D()).__qualname__
C(1).__repr__()
```
