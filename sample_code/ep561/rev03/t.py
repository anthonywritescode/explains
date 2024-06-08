from typing import Generic, TypeVar


type NumberTypes = int | float
type NumberTypes2 = int | float | D
type MyList[T] = list[T]


def g(q: MyList[int]) -> None: ...


def f[T](x: T) -> T:
    return x


class C[T]:
    def __init__(self, x: T) -> None:
        self.x = x

    @property
    def my_x(self) -> T:
        return self.x


class D: ...
