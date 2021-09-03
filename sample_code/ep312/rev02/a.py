from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from b import B


def f(b: 'B') -> None:
    b.say_hello()


def g() -> None:
    print('hello hello world')
