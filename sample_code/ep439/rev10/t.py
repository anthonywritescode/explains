from typing import Sequence
from typing import TypeGuard
from typing import TypeVar


T = TypeVar('T')


def list_of(y: Sequence[object], tp: type[T]) -> TypeGuard[list[T]]:
    return isinstance(y, list) and all(isinstance(x, tp) for x in y)


def f(x: list[str] | list[int]) -> None:
    if list_of(x, str):
        reveal_type(x)
    elif list_of(x, int):
        reveal_type(x)
    else:
        return None
