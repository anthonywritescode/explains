from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class Indexable(Protocol):
    def __index__(self) -> int: ...


class C:
    def __index__(self) -> float:
        return 2.


c = C()
if isinstance(c, Indexable):
    print('it is indexable')
else:
    print('not indexable')

print(issubclass(C, Indexable))

# x: Indexable = C()
