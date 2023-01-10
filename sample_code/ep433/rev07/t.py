from typing import TypeAlias
from typing import Generic
from typing import TypeVarTuple
from typing import TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')

T1: TypeAlias = tuple[int, ...]
T2: TypeAlias = tuple[*T1, str]

reveal_type(T2)


class Array(Generic[*Ts]):
    def multiply(self, x: int) -> Array[*Ts]: ...
    def add_dimension(self, t: T) -> Array[*Ts, T]: ...


a: Array[float, int, str] = Array()
reveal_type(a.multiply(2))
reveal_type(a.add_dimension('foo'))


def f(*args: *tuple[int, *tuple[str, ...]]) -> str:
    arg0, *rest = args
    reveal_type(arg0)
    reveal_type(rest)
    return str(arg0) + ' '.join(rest)
