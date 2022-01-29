import functools
import time


class C:
    def __init__(self, y: int) -> None:
        self.y = y

    @functools.lru_cache(maxsize=None)
    def compute(self, x: int) -> int:
        print('computing ...')
        time.sleep(.5)
        return self.y * x * x

    def __del__(self) -> None:
        print(f'deleting {self}...')
