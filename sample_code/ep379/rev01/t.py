from __future__ import annotations

from typing import NamedTuple


class Example(NamedTuple):
    val: int
    children: tuple[Example, ...] = ()


ex1 = Example(1)
ex2 = Example(2, (ex1,))

print(ex1)
print(ex2)
