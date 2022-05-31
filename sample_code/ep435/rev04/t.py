from typing import assert_never


def f(x: int | str) -> None:
    if isinstance(x, int):
        print(f'got int: {x}')
    elif isinstance(x, str):
        print(f'got str: {x}')
    else:
        assert_never(x)


f(1)
