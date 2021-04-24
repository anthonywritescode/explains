import contextlib


@contextlib.contextmanager
def ctx():
    print('before')
    try:
        yield
    finally:
        print('after')


class C:
    def __enter__(self):
        self.ctx = ctx()
        self.ctx.__enter__()

    def __exit__(self, tp, inst, tb):
        return self.ctx.__exit__(tp, inst, tb)
