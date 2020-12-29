from typing import Iterator


def my_range(x: int) -> Iterator[int]:
    value = 0
    while value < x:
        yield value
        value += 1
