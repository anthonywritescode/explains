from typing import Final


class C:
    foo: Final = 5


class D(C):
    foo = 6


print(D.foo)
