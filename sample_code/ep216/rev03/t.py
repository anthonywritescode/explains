import functools


@functools.lru_cache(maxsize=None)
def trib(n: int) -> int:
    print(f'trib({n})')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return trib(n - 1) + trib(n - 2) + trib(n - 3)
