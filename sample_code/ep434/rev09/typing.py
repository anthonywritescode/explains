from typing import Generic
from typing import TypeAlias
from typing import TypeVarTuple


Ts = TypeVarTuple('Ts')


class Array(Generic[*Ts]):
    ...


x: Array[int, int, float]


def double(a: Array[*Ts]) -> Array[*Ts]:
    ...


def add_dimention(a: Array[*Ts]) -> Array[int, *Ts]:
    ...


t: TypeAlias = tuple[int, int]
t2: TypeAlias = tuple[*t, float, str]  # tuple[int, int, float, str]

t3: TypeAlias = tuple[str, *tuple[int, ...]]


def f(*args: *t3):
    s, *ints = args
