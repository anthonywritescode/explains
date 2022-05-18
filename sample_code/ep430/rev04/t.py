from __future__ import annotations

from typing import Protocol
from typing import TypeVar


class MultInt(Protocol):
    def __mul__(self: T, x: int) -> T: ...


T = TypeVar('T', bound=MultInt)


def double(x: T) -> T:
    return x * 2


reveal_type(double([1]))
reveal_type(double(1))
reveal_type(double(1.5))
