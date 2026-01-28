class C:
    @classmethod
    def make(cls) -> C:
        return cls()
