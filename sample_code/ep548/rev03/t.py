from typing import TypeVar

Z = TypeVar('Z', bound=int)


def f[T: C, U, V](x: T) -> list[T]:
    return [x]


async g[T](): ...

class D[T]: pass

class C: pass

Old = int

from typing import TypeAlias

Newer: TypeAlias = "Foo"

type Newest = int

type NewestWithGeneric[T: int] = list[T]
