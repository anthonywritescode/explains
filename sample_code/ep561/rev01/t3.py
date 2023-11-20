from typing import TypeVar


T = TypeVar('T', str, bytes)


def f(t: T) -> T:
    return t


def f[T: (str, bytes)](t: T) -> T:
    return t


U = TypeVar('U', covariant=True)
U = TypeVar('U', infer_variance=True)
