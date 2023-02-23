"""module docstring"""

import dis


def g():
    return True


def f():
    """function docstring"""

    assert g(), 'hello'

    if False:
        print('never runs')

    if __debug__:
        print('hi')

    print('hello hello')


f()
dis.dis(f)
