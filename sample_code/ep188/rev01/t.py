from typing import final


@final
class _Foo:
    def __init__(self):
        self.x = 1

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x


foo = _Foo()


class Bar(_Foo):
    ...
