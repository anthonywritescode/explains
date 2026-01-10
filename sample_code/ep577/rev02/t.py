from __future__ import annotations

from collections.abc import Generator


def gen() -> Generator[object, None, None]:
    yield from ()
