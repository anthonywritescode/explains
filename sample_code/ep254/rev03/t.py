from typing import Callable


# Callable[[float, float], float]
def add(a: float, b: float) -> float:
    return a + b


def make_adder(a: float) -> Callable[[float], float]:
    return lambda b: add(a, b)


add_5 = make_adder(5)
