from typing import Generic, TypeAlias, TypeVar


NumberTypes = int | float
NumberTypes2: TypeAlias = "int | float"

T = TypeVar('T')


def f(x: T) -> T:
    return x


class C(Generic[T]):
    def __init__(self, x: T) -> None:
        self.x = x

    @property
    def my_x(self) -> T:
        return self.x
