import sys
from typing import Tuple


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

TokenPosition: TypeAlias = Tuple[int, int, int, int, str]

CAlias: TypeAlias = "C"


def f(x: TokenPosition) -> str: ...


class C:
    pass
