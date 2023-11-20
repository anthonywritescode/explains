from typing import Generic, TypeVar


type NumberTypes = int | float
type NumberTypes2 = int | float | D

T = TypeVar('T')


def f(x: T) -> T:
    return x


class C(Generic[T]):
    def __init__(self, x: T) -> None:
        self.x = x

    @property
    def my_x(self) -> T:
        return self.x


class D: ...
