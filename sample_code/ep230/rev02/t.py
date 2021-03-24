import time


def f():
    return (1, ) * 1000000


t0 = time.monotonic()

for _ in range(10):
    f()

t1 = time.monotonic()


print(f'{t1 - t0:.5f}')
