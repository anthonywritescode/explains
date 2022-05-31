from typing import assert_never


def f(x: int) -> None:
    assert_never(x)
    assert False, 'unreachable'
    raise AssertionError(f'unreachable: {x}')
