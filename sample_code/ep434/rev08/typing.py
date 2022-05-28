

class C:
    def clone(self: Self) -> Self:
        return type(self)()

    @classmethod
    def make(cls: type[Self]) -> Self:
        ...


class D(C):
    pass


D.clone()  # D
