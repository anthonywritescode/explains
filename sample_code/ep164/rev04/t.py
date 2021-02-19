from typing import Union
from typing import overload
from typing import Protocol
from typing import Optional
from typing import NamedTuple


class Indexable(Protocol):
    def __index__(self) -> int: ...


class _TreeNode(Protocol):
    left: Optional['_TreeNode']

    # @property
    # def left(self) -> Optional['_TreeNode']: ...
    @property
    def right(self) -> Optional['_TreeNode']: ...
    @property
    def value(self) -> int: ...


class TreeNode(NamedTuple):
    left: Optional[_TreeNode]
    right: Optional[_TreeNode]
    value: int


@overload
def bytes_getitem(b: bytes, idx: Indexable) -> int: ...
@overload
def bytes_getitem(b: bytes, idx: slice) -> bytes: ...


def bytes_getitem(b: bytes, idx: Union[Indexable, slice]) -> Union[int, bytes]:
    if isinstance(idx, slice):
        return b[idx]
    else:
        return b[int(idx)]


foo = b'100'
print(bytes_getitem(foo, 0) - ord('0'))


class C:
    def __index__(self) -> int:
        return 2


print(bytes_getitem(foo, C()))
