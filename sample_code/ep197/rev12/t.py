

x = 1  # global scope


def f():
    e = 1
    e2 = None
    try:
        raise AssertionError('foo')
    except AssertionError as e:
        e2 = e
        print(repr(e))
        # implicit `del e`
    print('2', repr(e2))


f()
