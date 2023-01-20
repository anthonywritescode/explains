def f() -> None:
    raise AssertionError('hello hello')


try:
    f()
except AssertionError:
    pass
