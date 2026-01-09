from collections.abc import Generator


def f() -> Generator[int, None, None]:
    yield 6
