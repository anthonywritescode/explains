from typing import Generic
from typing import TypeVarTuple

Ts = TypeVarTuple('Ts')


class C(Generic[*Ts]):
    ...
