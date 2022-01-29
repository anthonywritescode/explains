import time


class C:
    def __init__(self, y: int) -> None:
        self.y = y

    def compute(self, x: int) -> int:
        print('computing ...')
        time.sleep(.5)
        return self.y * x * x
