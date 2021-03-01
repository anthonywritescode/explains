from typing import Protocol


class Indexable(Protocol):
    def __index__(self) -> int: ...


class C:
    def __index__(self) -> int:
        return 2


x: Indexable = C()
