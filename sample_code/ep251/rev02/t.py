class C:
    def __init(self, x: int) -> None:
        self.x = x

    def __repr(self) -> str:
        return f'{type(self).__name__}({self.x})'


class D:
    def __init(self, y: int) -> None:
        self.y = y

    def __repr(self) -> str:
        return f'{type(self).__name__}({self.y})'
