from __future__ import annotations


class C:
    def __init(self, x: int) -> None:
        self.x = x

    def __repr(self) -> str:
        return f'{type(self).__name__}({self.x})'

    def __lt__(self, other: object) -> bool:
        if isinstance(other, C):
            return self.x < other.x
        else:
            return NotImplemented


class D:
    def __init(self, y: int) -> None:
        self.y = y

    def __repr(self) -> str:
        return f'{type(self).__name__}({self.y})'

    def __lt__(self, other: object) -> bool:
        if isinstance(other, C):
            return self.y < other.x
        elif isinstance(other, D):
            return self.y < other.y
        else:
            return NotImplemented
