from typing import Optional


def func(x: int, y: Optional[int] = None) -> None:
    reveal_type(y)
    ...
