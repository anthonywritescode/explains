import functools
from typing import Callable
from typing import ParamSpec
from typing import TypeVar


P = ParamSpec('P')
R = TypeVar('R')


def prints_hi(f: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(f)
    def prints_hi_inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print('ohai')
        return f(*args, **kwargs)
    return prints_hi_inner


@prints_hi
def hello(name: str) -> int:
    print(f'hello hello {name}')
    return 5


x = hello('anthony')
print(x)
