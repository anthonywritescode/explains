from typing import NoReturn


def f() -> NoReturn:
    raise AssertionError('hello hello')


try:
    f()
except AssertionError as e:
    print(f'caught an error {e!r}')
