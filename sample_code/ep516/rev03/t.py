import contextlib


def f() -> None:
    raise AssertionError('hello hello')


try:
    f()
except AssertionError:
    pass


with contextlib.suppress(AssertionError, ValueError):
    raise ValueError
    f()
