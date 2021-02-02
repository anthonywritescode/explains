from typing import final


@final
class C:
    def hello(self) -> None:
        print('hello hello world')


class D(C):
    def hello(self) -> None:
        print('goodbye world')


D().hello()
