from typing import List
from typing import Tuple


def f() -> Tuple[int, str, float]:
    return 1, 'foo', 1.5


def g() -> Tuple[int, ...]:
    x: List[int] = [1, 2, 3, 4]
    return tuple(x)
