import functools
from typing import List


@functools.lru_cache(maxsize=10)
def func(x: int) -> List[int]:
    return [x] * x


lst = func(1)
lst.append(5)
