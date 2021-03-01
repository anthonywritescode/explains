from typing import final


@final
class _Foo:
    def __init__(self):
        self.x = 1

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x


_foo = None


def get_foo():
    global _foo
    if _foo is None:
        _foo = _Foo()
    return _foo
