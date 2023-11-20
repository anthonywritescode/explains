from typing import TypeVar


T = TypeVar('T', bound=int)


def f(t: T) -> T:
    return t


def f[T: int](t: T) -> T:
    return t
