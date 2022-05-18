from __future__ import annotations

from typing import Callable
from typing import Protocol
from typing import TypeVar


class MultInt(Protocol):
    def __mul__(self: T, x: int) -> T: ...


T = TypeVar('T', bound=MultInt)


def double(x: T) -> T:
    return x * 2


In = TypeVar('In')
Out = TypeVar('Out')


def my_map(fn: Callable[[In], Out], lst: list[In]) -> list[Out]:
    ret = []
    for thing in lst:
        ret.append(fn(thing))
    return ret


print(my_map(lambda x: str(x), [1, 2, 3]))
reveal_type(my_map(lambda x: str(x), [1, 2, 3]))
