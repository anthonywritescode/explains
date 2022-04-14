from __future__ import annotations


class C:
    def __init__(self, x: int) -> None:
        self.x = x

    def clone(self) -> C:
        return type(self)(self.x)

    @classmethod
    def make(cls, y: int) -> C:
        return cls(y * y)


class D(C):
    pass


reveal_type(C.make(2))
reveal_type(C(2).clone())

reveal_type(D.make(2))
reveal_type(D(2).clone())
