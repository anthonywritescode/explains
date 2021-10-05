
class C:
    def __enter__(self):
        return self

    def __exit__(self, tp, exc, tb):
        print('world')


with C():
    assert False, "print('hello')"
