import functools


def dec(cls):
    @functools.wraps(cls)
    class D(cls):
        decorated = True

    return D


@dec
class C:
    hello = 'world'
