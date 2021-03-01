from typing import final


@final
class _Foo:
    _inst = None
    _inited = False

    def __new__(cls) -> '_Foo':
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __init__(self):
        if type(self)._inited:
            return
        self.x = 1
        type(self)._inited = True

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x


def singleton(cls):
    inst = cls()

    def get_instance():
        return inst

    return get_instance


@singleton
class C:
    def __init__(self):
        self.x = 1


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        try:
            return Singleton._instances[cls]
        except KeyError:
            obj = cls.__new__(cls, *args, **kwargs)
            cls.__init__(obj, *args, **kwargs)
            ret = Singleton._instances[cls] = obj
            return ret


class D(metaclass=Singleton):
    def __init__(self) -> None:
        self.x = 1

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x
