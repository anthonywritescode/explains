from __future__ import annotations

import sys

if sys.version_info >= (3, 11):
    from typing import Self  # python.3.11+
else:
    from typing_extensions import Self  # needs mypy support


class C:
    def __init__(self, x: int) -> None:
        self.x = x

    def clone(self: Self) -> Self:
        return type(self)(self.x)

    @classmethod
    def make(cls: type[Self], y: int) -> Self:
        return cls(y * y)


class D(C):
    pass


reveal_type(C.make(2))
reveal_type(C(2).clone())

reveal_type(D.make(2))
reveal_type(D(2).clone())
