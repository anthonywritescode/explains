# [python: what is hashability? (intermediate)](https://youtu.be/fQtNXBJp8Q4)

Today I talk about what it means to be "hashable" and how to define your own  `__hash__` method (or disable it!)

## Interactive examples

### Python

```python
class C: pass

{C(): 3}

dct = {C(): 3}
dct[C()]

{C(), C()}

x = 1
x = 2
x = (1, 2)
x
x[0] = 2

hash(-1)
hash(-2)

C.__hash__
C().__hash__()
C().__hash__()
C().__eq__(C())

c = C()
id(c)
c.__hash__()
c
c == c
c == C()
c is c
c is C()

class D:
    __hash__ = None

{D()}
D() == D()

class E:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return isinstance(other, type(self)) and other.x == self.x

E.__repr__ = lambda self: f'{type(self).__name__}({self.x})'
x = E(1)
x

y = E(2)
x == y

z = E(2)
y == z

{x, y, z}

class F:
    def __init__(self, x):
        self.x = x
    def __hash__(self):
        return hash((self.x,))
    def __eq__(self, other):
        return isinstance(other, type(self)) and other.x == self.x
    def __repr__(self):
        return f'{type(self).__name__}({self.x})'

F(1)
F(2)
hash(F(1)) == hash(F(1))
{F(1), F(2), F(3), F(1)}

from collections import Hashable
issubclass(F, Hashable)
issubclass(E, Hashable)
issubclass(D, Hashable)
issubclass(C, Hashable)

class G:
    def __hash__(self): raise TypeError('not hashable')

issubclass(G, Hashable)
```
