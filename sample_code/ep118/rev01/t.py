import collections
from typing import NamedTuple


# old, kinda hacky (py2+)
C = collections.namedtuple('C', ('x', 'y', 'z'))
C.__new__.__defaults__ = (1, 2)


# old, override __new__ manually (py2+)
class C2(collections.namedtuple('C2', ('x', 'y', 'z'))):
    __slots__ = ()

    def __new__(cls, x, y=1, z=2):
        # return super(C2, cls).__new__(cls, x, y, z)
        return super().__new__(cls, x, y, z)


# newish, py3.7+
C3 = collections.namedtuple('C3', ('x', 'y', 'z'), defaults=(1, 2))


# python3.6+ (3.6.1+)
class C4(NamedTuple):
    x: int
    y: int = 1
    z: int = 2
