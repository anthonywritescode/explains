from __future__ import annotations

from typing import Tuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

TokenPosition: TypeAlias = Tuple[int, int, int, int, str]

CAlias: TypeAlias = "C"


def f(x: TokenPosition) -> str: ...


class C:
    pass
