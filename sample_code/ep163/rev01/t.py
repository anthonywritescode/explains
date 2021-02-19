from typing import Union
from typing import overload


# divmod(T, T) -> Tuple[T, T]:


@overload
def bytes_getitem(b: bytes, idx: int) -> int: ...
@overload
def bytes_getitem(b: bytes, idx: slice) -> bytes: ...


def bytes_getitem(b: bytes, idx: Union[int, slice]) -> Union[int, bytes]:
    # if isinstance(idx, int):
    #     return ...
    # else:
    #     return ...
    return b[idx]


foo = b'100'
print(bytes_getitem(foo, 0) - ord('0'))
