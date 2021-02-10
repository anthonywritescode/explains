from typing import Optional


x: Optional[int] = 4


def func(x: int, y: Optional[int] = 5) -> int:
    return x * y
