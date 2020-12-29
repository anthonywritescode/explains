from typing import Generator


def my_range(x: int) -> Generator[int, None, None]:
    value = 0
    while value < x:
        yield value
        value += 1
