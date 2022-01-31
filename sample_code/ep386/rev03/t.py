import functools
import logging
from typing import Callable
from typing import Concatenate
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


def add_logger(
    f: Callable[Concatenate[logging.Logger, P], R],
) -> Callable[P, R]:
    @functools.wraps(f)
    def add_logger_inner(*args: P.args, **kwargs: P.kwargs) -> R:
        logger = logging.getLogger(f.__module__)
        return f(logger, *args, **kwargs)
    return add_logger_inner


@add_logger
def do_something(logger: logging.Logger, name: str, age: int) -> None:
    logger.warning('oh noes!')
    print(f'hello {name}, I hear your age is {age}')
    return age * age


logging.basicConfig()
x = do_something('jeff', 22)
print(x)
