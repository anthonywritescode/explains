from typing import TypeVar

T = TypeVar('T')


def f(x: T) -> list[T]:
    return [x]
