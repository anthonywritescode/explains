from typing import assert_type


def f(x: int | str) -> None:
    if isinstance(x, int):
        print(f'got int: {x}')
        return

    # ...

    assert_type(x, str)


f(1)
