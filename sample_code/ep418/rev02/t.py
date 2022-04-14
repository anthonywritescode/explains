from __future__ import annotations

from typing import TypeVar

CSelf = TypeVar('CSelf', bound='C')


class C:
    def __init__(self, x: int) -> None:
        self.x = x

    def clone(self: CSelf) -> CSelf:
        return type(self)(self.x)

    @classmethod
    def make(cls: type[CSelf], y: int) -> CSelf:
        return cls(y * y)


class D(C):
    pass


reveal_type(C.make(2))
reveal_type(C(2).clone())

reveal_type(D.make(2))
reveal_type(D(2).clone())
