

x = 1  # global scope


def f():

    try:
        raise AssertionError('foo')
    except AssertionError as e:
        print(repr(e))


f()
