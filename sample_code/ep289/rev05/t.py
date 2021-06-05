import contextlib


@contextlib.contextmanager
def ctx():
    yield 1


with (
    ctx() as x,
    ctx() as y,
):
    print(x, y)
