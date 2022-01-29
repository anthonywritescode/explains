import functools
import time


class C:
    def __init__(self, y: int) -> None:
        self.y = y

    def compute(self, x: int) -> int:
        print('computing ...')
        time.sleep(.5)
        return self.y * x * x

    compute = functools.lru_cache(maxsize=None)(compute)

    def __del__(self) -> None:
        print(f'deleting {self}...')
