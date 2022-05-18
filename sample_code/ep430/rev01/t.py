from __future__ import annotations

from typing import TypeVar

T = TypeVar('T')


def double(x: T) -> T:
    return x * 2
