from collections.abc import Callable
from typing import Any, Generic, TypeVar

empty = object()
R = TypeVar('R')


class Lazy(Generic[R]):
    def __init__(self, f: Callable[[], R]) -> None:
        self._f = f
        self._inst = empty

    def lazy_func(self) -> str:
        return 'hello hello'

    def __getattr__(self, attr: str) -> Any:
        if self._inst is empty:
            self._inst = self._f()

        return getattr(self._inst, attr)


class C:
    def __init__(self) -> None:
        print('expensive!')

    def foo(self) -> None:
        print('foo() was called')

    def f(self) -> int:
        return 4


def make_c() -> C:
    return C()


lazy = Lazy(make_c)
lazy.foo()
lazy.foo()

reveal_type(lazy.lazy_func())
reveal_type(lazy.f())
