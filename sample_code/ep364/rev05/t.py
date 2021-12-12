from __future__ import annotations


def f(x: list[int] | None = None) -> None:
    reveal_type(x)
    if x is None:
        x = []

    x.append(2)
    print(x)
