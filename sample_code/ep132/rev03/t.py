from typing import Final
from typing import final


class C:
    foo: Final = 5

    @final
    def hello(self) -> None:
        print('hello hello world')


class D(C):
    def hello(self) -> None:
        print('goodbye world')


D().hello()
