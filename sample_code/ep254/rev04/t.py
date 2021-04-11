import functools
from typing import Callable


def add(a: float, b: float) -> float:
    print(f'got args: {a=} {b=}')
    return a + b


def make_adder(a: float) -> Callable[[float], float]:
    return lambda b: add(a, b)


add_5 = make_adder(5)

add_6 = functools.partial(add, 6)

returns_20 = functools.partial(add, 10, 10)

add_7 = functools.partial(add, b=7)
