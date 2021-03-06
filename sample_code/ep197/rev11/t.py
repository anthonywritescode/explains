

x = 1  # global scope


def f():
    e = 1
    try:
        raise AssertionError('foo')
    except AssertionError as e:
        print(repr(e))
        # implicit `del e`
    print(repr(e))


f()
