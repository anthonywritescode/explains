from typing import Callable


# Callable[[float, float], float]
def add(a: float, b: float) -> float:
    return a + b


def make_adder(a: float) -> Callable[[float], float]:
    def adder_inner(b: float) -> float:
        return add(a, b)
    return adder_inner


add_5 = make_adder(5)
