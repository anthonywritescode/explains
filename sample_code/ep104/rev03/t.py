from __future__ import annotations  # python 3.7+


class C:
    def __init__(self, x: int) -> None:
        self.x = x

    def __repr__(self) -> str:
        return f'{type(self).__name__}.make({self.x})'

    @classmethod
    def make(cls, x: int) -> C:
        return cls(x)


print(C.make(2))
# reveal_type(C.make(2))
