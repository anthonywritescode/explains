from typing import assert_never


def f(x: int) -> None:
    assert_never(x)


f(1)
