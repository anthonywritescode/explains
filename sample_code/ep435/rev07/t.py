from typing import Never


def assert_never(x: Never) -> None:
    raise AssertionError(f'unreachable: {x!r}')
