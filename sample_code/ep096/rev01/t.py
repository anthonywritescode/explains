from typing import Type


class C:
    pass


class D(C):
    pass


def f1(c: C) -> None:
    ...


def f2(c: Type[C]) -> None:
    ...


f1(C())  # ok
f1(D())  # ok
# f1(2)  # not ok
# f1(C)  # not ok
f2(C)    # ok
f2(D)    # ok
f2(int)  # not ok
f2(C())  # not ok
