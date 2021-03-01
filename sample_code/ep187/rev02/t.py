from typing import Protocol


class Indexable(Protocol):
    def __index__(self) -> int: ...


class C:
    def __index__(self) -> int:
        return 2


c = C()
if isinstance(c, Indexable):
    print('it is indexable')
else:
    print('not indexable')
