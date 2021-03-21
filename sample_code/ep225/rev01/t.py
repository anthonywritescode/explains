from typing import Any
from typing import Iterable


def my_any(it: Iterable[Any]) -> bool:
    for item in it:
        if item:
            return True
    else:
        return False


def my_all(it: Iterable[Any]) -> bool:
    for item in it:
        if not item:
            return False
    else:
        return True
