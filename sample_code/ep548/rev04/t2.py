from typing import TypedDict, Unpack


class D(TypedDict):
    x: int
    y: str


def f(**kwargs: Unpack[D]): pass


f(x=1, y='foo')
