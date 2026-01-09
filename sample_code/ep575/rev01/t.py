
q: float = 1
x: float = False
y: float = NotImplemented


def f(x: float) -> bool:
    return x.is_integer()


f(1)


class C:
    def __init__(self, x: int) -> None:
        self._x = x

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, C):
            return NotImplemented
        else:
            self._x < other._x


C(5) < 4
