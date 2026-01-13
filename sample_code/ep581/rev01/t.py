from collections.abc import Generator


def f() -> Generator[int]:
    yield 1
