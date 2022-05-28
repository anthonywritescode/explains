from typing import assert_never
from typing import assert_type
from typing import Generic
from typing import Never
from typing import TypeVar


T = TypeVar('T')


class TypedDict(Generic[T]):
    x: T


def f1() -> Never:  # -> NoReturn
    ...


def f() -> str | None:
    ...


x = f()

# assert x is not None

assert_never(x is None)
assert_type(x, str)

print('hello ' + x)
