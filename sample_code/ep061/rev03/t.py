import os
import sys


a_const = 1

_a_const = 1


def a_func():
    return os.path.join('hello', 'world')


def _a_private_func():
    return sys.executable


class AClass:
    pass


class _APrivateClass:
    pass


__all__ = ('_a_const', AClass.__name__)
