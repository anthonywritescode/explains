import functools
import time
from typing import Callable, TypeVar, ParamSpec


P = ParamSpec('P')
R = TypeVar('R')


def timing(name: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def timing_dec(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def timing_dec_impl(*args: P.args, **kwargs: P.kwargs) -> R:
            t0 = time.monotonic()
            try:
                return func(*args, **kwargs)
            finally:
                t1 = time.monotonic()
                print(f'LOG: {name} took: {t1 - t0}')
        return timing_dec_impl
    return timing_dec


@timing('g.timing')
def g(x: int) -> int:
    return x ** x


g(10)
reveal_type(g(10))
