import functools
from typing import Sequence


@functools.lru_cache(maxsize=10)
def func(x: int) -> Sequence[int]:
    return [x] * x


lst = func(1)
lst.append(5)
