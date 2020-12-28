from __future__ import annotations

from typing import Type


class C:
    def foo(self: C, arg: float) -> float:
        return 5 * arg

    @classmethod
    def make_c(cls: Type[C], arg) -> C:
        ...
