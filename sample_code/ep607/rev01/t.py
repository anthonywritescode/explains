from __future__ import annotations
from typing import Self


def get_foo() -> Foo:
    return Foo()


class Foo:
    @classmethod
    def identity(cls, obj: Self) -> Self:
        return obj

    @classmethod
    def use_identity(cls) -> Self:
        return cls.identity(get_foo())  # This fails


def use_identity_2() -> Foo:
    return Foo.identity(get_foo())  # This succeeds
