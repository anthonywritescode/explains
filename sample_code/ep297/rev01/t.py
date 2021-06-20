from typing import Generator


def gen() -> Generator[int, str, bool]:
    s = yield 1
    reveal_type(s)
