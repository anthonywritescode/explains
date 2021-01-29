import collections


class C(collections.namedtuple('C', ('x', 'y'))):
    __slots__ = ()

    @property
    def area_from_origin(self) -> int:
        return self.x * self.y
