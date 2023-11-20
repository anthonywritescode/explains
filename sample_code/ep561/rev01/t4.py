from typing import TypeVarTuple


Ts = TypeVarTuple('Ts')


def f(*a: Ts) -> None: ...


def f[*Ts](*a: Ts) -> None: ...
