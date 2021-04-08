from typing import NoReturn


def f() -> NoReturn:
    raise AssertionError('hello hello')


tps = (AssertionError, TypeError)

try:
    f()
except tps as e:
    print(f'caught an error {e!r}')
