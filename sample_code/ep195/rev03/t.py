import functools


class cached:
    def __init__(self, func):
        self.func = func
        self.cached_data = {}

        functools.update_wrapper(self, func)

    def __call__(self, *args):
        try:
            return self.cached_data[args]
        except KeyError:
            self.cached_data[args] = ret = self.func(*args)
            return ret

    def __repr__(self):
        return repr(self.func)


@cached
def compute(x: int) -> int:
    print(f'calling w/ {x}')
    return x * x
