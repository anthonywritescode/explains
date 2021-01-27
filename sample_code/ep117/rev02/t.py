class C:
    def __init__(self, x: int) -> None:
        self._x = x

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value

    @x.deleter
    def x(self) -> None:
        ...


x = C(123).x
reveal_type(x)
