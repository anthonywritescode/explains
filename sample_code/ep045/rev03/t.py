from __future__ import annotations  # python3.7+

from typing import Generic
from typing import overload
from typing import Sequence
from typing import TypeVar
from typing import Union


T = TypeVar('T')


class C(Generic[T]):
    def __init__(self, lst: Sequence[T]) -> None:
        self._lst = lst

    @overload
    def __getitem__(self, idx: int) -> T: ...

    @overload
    def __getitem__(self, idx: slice) -> C[T]: ...

    def __getitem__(self, idx: Union[slice, int]) -> Union[C[T], T]:
        if isinstance(idx, slice):
            return C(self._lst[idx])
        else:
            return self._lst[idx]

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self._lst})'


inst = C([1, 2, 3])
reveal_type(inst[1:])
reveal_type(inst[1])
