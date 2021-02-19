from typing import Union
from typing import overload
from typing import Protocol


class Indexable(Protocol):
    def __index__(self) -> int: ...


@overload
def bytes_getitem(b: bytes, idx: Indexable) -> int: ...
@overload
def bytes_getitem(b: bytes, idx: slice) -> bytes: ...


def bytes_getitem(b: bytes, idx: Union[Indexable, slice]) -> Union[int, bytes]:
    # if isinstance(idx, int):
    #     return ...
    # else:
    #     return ...
    return b[idx]


foo = b'100'
print(bytes_getitem(foo, 0) - ord('0'))


class C:
    def __index__(self) -> int:
        return 2


print(bytes_getitem(foo, C()))
