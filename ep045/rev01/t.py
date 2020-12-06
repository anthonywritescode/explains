class C:
    def __init__(self, lst):
        self._lst = lst

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return C(self._lst[idx])
        else:
            return self._lst[idx]

    def __repr__(self):
        return f'{type(self).__name__}({self._lst})'
