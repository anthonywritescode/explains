class cached:
    def __init__(self, func):
        self.func = func
        self.cached_data = {}

    def __call__(self, *args):
        try:
            return self.cached_data[args]
        except KeyError:
            self.cached_data[args] = ret = self.func(*args)
            return ret


@cached
def compute(x: int) -> int:
    print(f'calling w/ {x}')
    return x * x
