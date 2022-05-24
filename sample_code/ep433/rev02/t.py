from typing import Generic
from typing import TypeVarTuple
from typing import Unpack

Ts = TypeVarTuple('Ts')


class C(Generic[Unpack[Ts]]):
    ...
