# import functools


# @functools.lru_cache
def square(x: float) -> float:
    print(f'running: {x}')
    return x * x
