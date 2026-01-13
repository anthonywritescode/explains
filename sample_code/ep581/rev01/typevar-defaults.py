class C[T, U=T]:
    def __init__(self, val: T, other: U | None = None) -> None:
        self.val = val
        if other is None:
            self.other = val
        else:
            self.other = other


reveal_type(C(1))
reveal_type(C(1, 'wat'))
