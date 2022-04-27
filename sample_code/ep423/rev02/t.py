class C:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self.__y = y


class D(C):
    def __init__(self, z: int) -> None:
        super().__init__(1, 2)
        self._z = z
