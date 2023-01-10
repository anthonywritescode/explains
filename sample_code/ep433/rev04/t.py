from typing import Generic
from typing import TypeVarTuple
from typing import TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


class Array(Generic[*Ts]):
    def multiply(self, x: int) -> Array[*Ts]: ...
    def add_dimension(self, t: T) -> Array[*Ts, T]: ...


a: Array[float, int, str] = Array()
reveal_type(a.multiply(2))
reveal_type(a.add_dimension('foo'))
