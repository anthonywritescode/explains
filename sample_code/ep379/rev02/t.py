from __future__ import annotations

from typing import NamedTuple
from typing import Protocol


class _Example(Protocol):
    @property
    def val(self) -> int: ...
    @property
    def children(self) -> tuple[_Example, ...]: ...
    def val_squared(self) -> int: ...


class Example(NamedTuple):
    val: int
    children: tuple[_Example, ...] = ()

    def val_squared(self) -> int:
        return self.val * self.val


ex1 = Example(1)
ex2 = Example(2, (ex1,))

print(ex1)
print(ex2)
