import functools


def dec(cls):
    @functools.wraps(cls, updated=())
    class D(cls):
        decorated = True

    return D


@dec
class C:
    hello = 'world'
