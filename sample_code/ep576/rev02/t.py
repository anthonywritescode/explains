from __future__ import annotations

from collections.abc import Generator


def f() -> Generator[int]:
    yield 6
