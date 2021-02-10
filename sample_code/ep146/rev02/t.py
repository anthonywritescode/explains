from typing import Optional


x: Optional[int] = 4


def func(x: int, y: int = 5) -> int:
    reveal_type(y)
    return x * y
