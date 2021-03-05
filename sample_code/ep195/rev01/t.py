import functools


def cached(func):
    cached_data = {}

    @functools.wraps(func)
    def cached_dec(*args):
        try:
            return cached_data[args]
        except KeyError:
            cached_data[args] = ret = func(*args)
            return ret

    return cached_dec


@cached
def compute(x: int) -> int:
    print(f'calling w/ {x}')
    return x * x
