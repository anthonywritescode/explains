import contextlib


@contextlib.contextmanager
def ctx():
    print('before')
    try:
        yield
    finally:
        print('after')


@contextlib.contextmanager
def ctx2():
    print('before2')
    try:
        yield
    finally:
        print('after2')
        raise AssertionError('oops')


class C:
    def __enter__(self):
        self.ctx = ctx()
        self.ctx.__enter__()
        self.ctx2 = ctx2()
        self.ctx2.__enter__()

    def __exit__(self, tp, inst, tb):
        self.ctx2.__exit__(tp, inst, tb)
        self.ctx.__exit__(tp, inst, tb)
